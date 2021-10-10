from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..serializers import GalleryImageSerializer
from roommates.models import Gallery, GalleryImage


class ImageDetailView(APIView):
    """
    Image Detail Endpoint
    GET: Get a specific image within a specified gallery by uuid
    DELETE: Delete a specific image within a specified gallery by uuid
    """
    
    permission_classes = [IsAuthenticated,]


    def get(self, request, gallery_id, image_id, format=None):
        """
        Return specified image within the gallery
        """
        gallery_image = self._get_image(gallery_id, image_id)

        data = {
            'image': gallery_image.image,
            'image_name': gallery_image.image_name
        }

        serializer = GalleryImageSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.initial_data)
    

    def delete(self, request, gallery_id, image_id, format=None):
        """
        Delete specified image instance
        """
        gallery_image = self._get_image(gallery_id, image_id)

        gallery_image.delete()
        return Response(None, status=status.HTTP_200_OK)


    def _get_image(self, gallery_id, image_id):
        """
        Get specified image instance if it exists 
        """
        gallery = Gallery.objects.filter(uuid=gallery_id).first()

        if not gallery:
            raise NotFound("Gallery does not exist")

        image = GalleryImage.objects.filter(
            gallery__id=gallery.id
        ).filter(
            image_name=image_id
        ).first()

        if not image:
            raise NotFound("Image does not exist")

        return image


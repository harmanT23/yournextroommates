from rest_framework import status, generics
from rest_framework.exceptions import APIException, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from roommates.models import Gallery
from ..serializers import (
    GallerySerializer,
    GalleryDetailSerializer,
    GalleryImageUploadSerializer
)

class GalleryCreateView(generics.CreateAPIView):
    """
    Gallery Create Endpoint
    - POST: Creates a new gallery for a user or listing
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated,]


class GalleryDetailView(APIView):
    """
    Gallery Detail Endpoint
    - GET: Returns all of the images for the gallery
    - POST: Upload one or more images to the gallery
    - DELETE: Delete the gallery and all its images
    """

    permission_classes = [IsAuthenticated,]

    def get(self, request, gallery_id, format=None):
        """
        Return all images within the gallery
        """
        gallery = self.get_gallery(gallery_id)
        serializer = GalleryDetailSerializer(gallery)
        return Response(serializer.data)
    

    def post(self, request, gallery_id, format=None):
        """
        Upload one or more images to the gallery
        """
        gallery = self.get_gallery(gallery_id)

        imgs_upload_status = {
            'uploaded': [],
            'errors': []
        }

        if not request.FILES:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        try:
            for key, file in request.FILES.items():                
                data = {
                    'gallery': gallery.pk,
                    'image': file
                }
                serializer = GalleryImageUploadSerializer(data=data, context={'request': request})

                if serializer.is_valid():
                    serializer.save()
                    imgs_upload_status['uploaded'].append({
                        'image': serializer.data['image'],
                    })
            
                else:
                    imgs_upload_status['errors'].append({
                        'filename': file.name,
                        'error': serializer.errors
                    })
        
            return Response(imgs_upload_status, status=status.HTTP_200_OK)

        except Exception as e:
            raise APIException(e)


    def delete(self, request, gallery_id, format=None):
        """
        Delete gallery and all the images within it
        """
        gallery = self.get_gallery(gallery_id)
        gallery.delete()
        return Response(None, status=status.HTTP_200_OK)
        
        
    def get_gallery(self, gallery_id):
        """
        Get specified gallery instance if it exists 
        """
        gallery = Gallery.objects.filter(
            uuid=gallery_id
        ).first()

        if not gallery:
            raise NotFound("Gallery does not exist.")

        return gallery

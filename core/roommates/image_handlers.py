import uuid
from io import BytesIO
from PIL import Image
from django.core.files import File
import core.settings as app_settings

def compress_resize_image(image, width, height):
    """
    Takes a given image, resizes it the specified width and height and
    saves the image either as a png by default or if the image was of jpeg
    format it will retain that formatting. 
    """
    img = Image.open(image).convert('RGB')
    img_io = BytesIO()
    img_name = image.name.split('.')[0]
    img_ext = image.name.split('.')[-1]

    img = img.resize((width, height), Image.ANTIALIAS)

    if img_ext in ['jpeg', 'jpg']:
        img.save(img_io, format='jpeg', optimize=True, quality=55)
        new_img = File(img_io, name='%s.jpeg' % img_name,)
    else:
        img.save(img_io, format='png', optimize=True, quality=55)
        new_img = File(img_io, name='%s.png' % img_name,)
    return new_img


def upload_user_profile_image(instance, filename):
    """
    Creates a file path for a user's unique profile image. The path
    is made unique for each user by using a unique uuid. Filename is specified
    as avatar.
    """
    ext = filename.split('.')[-1]
    n_filename = f'avatar.'+ ext
    return f'images/users/profile/{uuid.uuid4()}/{n_filename}'

def upload_gallery_image(instance, filename):
    """
    Uploads an image for user or listing gallery.
    The gallery is stored in a folder specified by the listing or user id.
    For security purposes filenames are replaced with a unique uuid.
    """
    ext = filename.split('.')[-1]
    n_filename = f'{uuid.uuid4()}.' + ext
    gallery_type = 'listings' if instance.gallery.is_listing_or_user_gallery \
        else 'users'
        
    return (
        f'{app_settings.GALLERY_SUBDIRECTORY}'
        f'{gallery_type}/{instance.gallery.uuid}/{n_filename}'
    )
    
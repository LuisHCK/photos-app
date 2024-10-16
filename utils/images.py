from PIL import Image
from io import BytesIO
from django.core.files import File


def compress(image: File, max_height: int = 850, max_width: int = 10000, quality: int = 80) -> File:
    """
    Compress and optimize image
    """
    temp_img = Image.open(image)
    temp_io = BytesIO()

    ratio = min(
        max_width / float(temp_img.size[0]), max_height / float(temp_img.size[1]))

    target_size = (int(temp_img.size[0] * ratio),
                   int(temp_img.size[1] * ratio))

    # Reescale image preserving aspect ratio
    # Convert to RGB then resize image and save
    temp_img = temp_img\
        .convert('RGB')\
        .resize(target_size, Image.LANCZOS)\
        .save(temp_io, 'JPEG', quality=quality, optimize=True)

    new_image = File(temp_io, name=image.name)
    return new_image

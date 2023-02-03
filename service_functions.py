from urllib.parse import urlparse, unquote
import requests
import os


class ExtensionException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ExtensionException, {0} '.format(self.message)
        else:
            return 'ExtensionException has been raised'


def make_default_dir():
    default_local_image_dir = os.path.join(os.getcwd(), r'default_images')
    return default_local_image_dir


def get_response(url, headers=None, params=None):
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    return response.content


def get_filename_and_extension(for_ext_url):
    image_extensions = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']
    splitted_text = os.path.splitext(urlparse(for_ext_url).path)
    extension = splitted_text[1]
    filename = unquote(os.path.split(splitted_text[0])[1])
    if extension in image_extensions:
        return f"{filename}{extension}"
    else:
        raise ExtensionException('Wrong file extension')


def download_image(image_path, url, index, params=None):

    filename_and_extension = get_filename_and_extension(url)
    filename = os.path.join(f"{image_path}", f"{index}{filename_and_extension}")
    with open(filename, 'wb') as file:
        file.write(get_response(url, params=params))


def fetch_images(image_dir, whose_images, params=None):
    for image_index, image_url in enumerate(whose_images):
        download_image(image_dir, image_url, str(image_index), params=params, )


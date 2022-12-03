from urllib.parse import urlparse, unquote
import requests
import os
from pathlib import Path
from datetime import datetime
import json


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
        return filename + extension
    else:
        return None


def download_image(url, index):
    local_image_dir = os.path.join(os.getcwd(), r'images\\')
    Path(local_image_dir).mkdir(parents=True, exist_ok=True)
    filename_and_extension = get_filename_and_extension(url)
    if filename_and_extension:
        filename = local_image_dir + index + filename_and_extension
        with open(filename, 'wb') as file:
            file.write(get_response(url))


def split_date_to_url(date):
    year = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date().strftime("%Y")
    month = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date().strftime("%m")
    day = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date().strftime("%d")
    return year + '/' + month + '/' + day + '/'


def fetch_images(whose_images):
    for image_index, image_url in enumerate(whose_images):
        download_image(image_url, str(image_index))



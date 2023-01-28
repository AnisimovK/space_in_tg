import argparse
from dotenv import dotenv_values
from pathlib import Path
from service_functions import get_response, fetch_images, make_default_dir
import json


def get_nasa_image_links(params):
    response_content = json.loads(get_response('https://api.nasa.gov/planetary/apod', params=params))
    images_links = [image_data['url'] for image_data in response_content if image_data['media_type'] == 'image']
    return images_links


if __name__ == '__main__':
    params_nasa = {'api_key': dict(dotenv_values(".env"))['NASA_API_KEY']}

    parser = argparse.ArgumentParser(
        description='[-h] [-count your_count] [-p image_path]'
    )
    parser.add_argument('-count', help='images count', default='3')
    parser.add_argument('-p', help='image_path count', default=str(make_default_dir()))
    params_nasa['count'] = parser.parse_args().count
    image_dir = parser.parse_args().p
    Path(image_dir).mkdir(parents=True, exist_ok=True)
    fetch_images(image_dir, get_nasa_image_links(params_nasa))

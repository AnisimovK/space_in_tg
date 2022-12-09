import argparse
from dotenv import dotenv_values
from service_functions import get_response, fetch_images
import json


def get_nasa_image_links(params):
    response_content = json.loads(get_response('https://api.nasa.gov/planetary/apod', params=params))
    images_links = [image_data['url'] for image_data in response_content if image_data['media_type'] == 'image']
    return images_links


if __name__ == '__main__':
    params_nasa = {'api_key': dict(dotenv_values(".env"))['API_KEY']}

    parser = argparse.ArgumentParser(
        description='[-h] [-count your_count] '
    )
    parser.add_argument('--count', help='images count', default='3')
    params_nasa['count'] = parser.parse_args().count
    fetch_images(get_nasa_image_links(params_nasa))

import argparse
from dotenv import dotenv_values
from service_functions import *


def get_nasa_image_links(params):
    response_content = json.loads(get_response('https://api.nasa.gov/planetary/apod', params=params))
    images_links = []
    for image_data in response_content:
        images_links.append(image_data['url'])
    return images_links


if __name__ == '__main__':
    params_nasa = {'api_key': dict(dotenv_values(".env"))['api_key']}

    parser = argparse.ArgumentParser(
        description='[-h] [-count your_count] '
    )
    parser.add_argument('--count', help='images count')
    input_count = parser.parse_args().count
    if input_count:
        params_nasa['count'] = str(input_count)
    else:
        params_nasa['count'] = '3'
    fetch_images(get_nasa_image_links(params_nasa))

import argparse
from service_functions import get_response, fetch_images
import json


def get_spacex_image_links(launch_id):
    response_content = json.loads(get_response(f"https://api.spacexdata.com/v5/launches/{launch_id}"))
    images_links = response_content['links']['flickr']['original']
    return images_links


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='[-h] [-id ID] '
    )
    parser.add_argument('--id', help='launch id', default='latest')
    launch_id_from_user = parser.parse_args().id
    fetch_images(get_spacex_image_links(launch_id_from_user))

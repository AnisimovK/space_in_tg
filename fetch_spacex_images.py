import argparse
from pathlib import Path
from service_functions import get_response, fetch_images, make_default_dir
import json


def get_spacex_image_links(launch_id):
    response_content = json.loads(get_response(f"https://api.spacexdata.com/v5/launches/{launch_id}"))
    images_links = response_content['links']['flickr']['original']
    return images_links


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='[-h] [-id ID] [-p image_path]'
    )
    parser.add_argument('-id', help='launch id', default='latest')
    parser.add_argument('-p', help='image_path', default=str(make_default_dir()))
    launch_id_from_user = parser.parse_args().id
    image_dir = parser.parse_args().p
    Path(image_dir).mkdir(parents=True, exist_ok=True)
    fetch_images(image_dir, get_spacex_image_links(launch_id_from_user))

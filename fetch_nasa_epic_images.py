from service_functions import get_response, fetch_images, make_default_dir
from dotenv import dotenv_values
import json
import datetime
from pathlib import Path
import argparse

def get_nasa_epic_image_links(params):
    images_links = []
    root_of_image_link = 'https://api.nasa.gov/EPIC/archive/natural/'
    response_content = json.loads(get_response('https://api.nasa.gov/EPIC/api/natural/images', params=params))
    for image_data in response_content:
        img_name = image_data['image']
        img_datetime = image_data['date'].split()
        img_date = datetime.date.fromisoformat(img_datetime[0])
        url = f"{root_of_image_link}{img_date.strftime('%Y/%m/%d')}/" \
              f"png/{img_name}" \
              f".png"
        images_links.append(url)
    return images_links


if __name__ == '__main__':
    params_nasa = {'api_key': dict(dotenv_values(".env"))['NASA_API_KEY']}
    parser = argparse.ArgumentParser(
        description='[-h] [-p image_path] '
    )
    parser.add_argument('-p', help='image_path', default=str(make_default_dir()))
    image_dir = parser.parse_args().p
    Path(image_dir).mkdir(parents=True, exist_ok=True)
    fetch_images(image_dir, get_nasa_epic_image_links(params_nasa), params=params_nasa)

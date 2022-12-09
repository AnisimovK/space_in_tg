from service_functions import get_response, fetch_images
from dotenv import dotenv_values
import json
import datetime


def get_nasa_epic_image_links(params):
    images_links = []
    root_of_image_link = 'https://api.nasa.gov/EPIC/archive/natural/'
    response_content = json.loads(get_response('https://api.nasa.gov/EPIC/api/natural/images', params=params))
    for image_data in response_content:
        img_name = image_data['image']
        img_datetime = image_data['date'].split()
        img_date = datetime.date.fromisoformat(img_datetime[0])
        url = f"{root_of_image_link}{img_date.year}/{img_date.strftime('%m')}/{img_date.strftime('%d')}/png/{img_name}" \
              f".png"
        images_links.append(url)
    return images_links


if __name__ == '__main__':
    params_nasa = {'api_key': dict(dotenv_values(".env"))['NASA_API_KEY']}
    fetch_images(get_nasa_epic_image_links(params_nasa), params=params_nasa)

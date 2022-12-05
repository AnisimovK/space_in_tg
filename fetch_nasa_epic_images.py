from service_functions import *
from dotenv import dotenv_values
import json


def get_nasa_epic_image_links(params):
    images_links = []
    root_of_image_link = 'https://api.nasa.gov/EPIC/archive/natural/'
    response_content = json.loads(get_response('https://api.nasa.gov/EPIC/api/natural/images', params=params))
    for image_data in response_content:
        images_links.append(root_of_image_link + split_date_to_url(image_data['date']) + 'png/' + image_data['image']
                            + '.png?api_key=' + params_nasa['api_key'])
    return images_links


if __name__ == '__main__':
    params_nasa = {'api_key': dict(dotenv_values(".env"))['api_key']}
    fetch_images(get_nasa_epic_image_links(params_nasa))


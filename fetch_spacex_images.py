import argparse
from service_functions import *


def get_spacex_image_links(launch_id):
    if launch_id:
        response_content = json.loads(get_response(f"https://api.spacexdata.com/v5/launches/{launch_id}"))
        images_links = response_content['links']['flickr']['original']
    else:
        response_content = json.loads(get_response(f"https://api.spacexdata.com/v5/launches/latest"))
        images_links = response_content['links']['flickr']['original']
    return images_links


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='[-h] [-id ID] '
    )
    parser.add_argument('--id', help='launch id')
    launch_id_from_user = parser.parse_args().id
    fetch_images(get_spacex_image_links(launch_id_from_user))





    # try:
    #     if is_bitlink(token, user_url):
    #         clicks_count = count_clicks(token, user_url)
    #         print('Count clicks :', clicks_count)
    #     else:
    #         bitly_url = shorten_url(token, user_url)
    #         print(f'Bitlink : {bitly_url}')
    # except requests.exceptions.HTTPError:
    #     print("You have entered incorrect url, or you made too much requests")
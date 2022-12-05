import os
import random
import argparse
import time
from pathlib import Path
from dotenv import load_dotenv
import telegram


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="""\
        Скрипт автоматически публикует фотографии каждые 'period' часов.\n
        При отсутсвии параметра 'period' публикация происходит каждые 4 часа."""
    )
    parser.add_argument('-period', help='периодичность публикации картинок в часах', type=float, default=4)
    args = parser.parse_args()
    img_folder_path = "images"
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    tg_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=tg_token)

    while True:
        imgs_in_folder = os.listdir(img_folder_path)
        rand_img_name = random.choice(imgs_in_folder)
        filepath = Path(img_folder_path, rand_img_name)
        try:
            with open(filepath, 'rb') as file:
                bot.send_photo(
                    chat_id=telegram_chat_id,
                    photo=file
                )
        except telegram.error.NetworkError as e:
            print(e)
        time.sleep(float(args.period) * 3600)







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
    TG_TOKEN = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=TG_TOKEN)

    while True:
        try:
            imgs_in_folder = os.listdir(img_folder_path)
            if imgs_in_folder:
                rand_img_name = random.choice(imgs_in_folder)
                filepath = Path(img_folder_path, rand_img_name)
                with open(filepath, 'rb') as file:
                    bot.send_photo(
                        chat_id=telegram_chat_id,
                        photo=file
                    )
            else:
                print("Images folder is empty!")
        except FileNotFoundError:
            print("Images folder doesn't exist!")
        time.sleep(float(args.period) * 3600)







from waveshare_epd import epd2in13_V4
from PIL import Image, ImageDraw, ImageFont
import time
import os

def main():
    epd = epd2in13_V4.EPD()
    epd.init()

    epd.Clear(0xFF)

    base_path = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_path, 'images')

    while True:
        for filename in os.listdir(images_dir):
            if filename.endswith('.png'):
                image_path = os.path.join(images_dir, filename)
                image = Image.open(image_path).convert('1')
                image = image.resize((epd.height, epd.width), Image.ANTIALIAS)
                image = image.rotate(180)
                epd.display(epd.getbuffer(image))
                time.sleep(10)

    epd.Clear(0xFF)
    epd.sleep()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()
    finally:
        epd2in13_V4.epdconfig.module_exit()

from waveshare_epd import epd2in13_V4
from PIL import Image, ImageDraw, ImageFont
import time

def main():
    epd = epd2in13_V4.EPD()
    epd.init()

    epd.Clear(0xFF)

    image = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)

    draw.text((10, 10), 'Hello, World!', font=font, fill=0)
    image = image.rotate(180)
    epd.display(epd.getbuffer(image))

    time.sleep(2)

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

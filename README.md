# capagotchi

## initial setup

- download raspberry pi imager
- install os onto microsd
- attach eink HAT to header
- power on
- connect to wifi (use hotspot to bypass name/password)
- pi packages
  - sudo apt update && sudo apt upgrade -y
  - sudo apt install python3-pip git
- display
  - git clone (insert repo)
  - python3 -m venv capagotchi-env
  - source capagotchi-env/bin/activate
  - pip3 install .
  - pip3 install spidev gpiozero RPi.GPIO pillow numpy lgpio
  - python3 src/main.py

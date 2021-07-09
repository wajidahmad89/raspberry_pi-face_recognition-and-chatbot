

#!/bin/bash

cd ~/.virtualenvs

. faregenv/bin/activate



cd /home/pi/Desktop/facrec

python facrec_main.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle



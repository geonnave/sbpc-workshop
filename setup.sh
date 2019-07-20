#!/bin/bash

sudo apt-get install openssh-server vim git python-dev python3-dev

cd .cv2py37
./opencv_py37.sh
cd ..

pip3 install requirements.txt

exit 0

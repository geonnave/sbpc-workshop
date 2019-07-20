#!/bin/bash

[ -z "$(grep 'alias python' ~/.bashrc)" ] && echo "alias python=python3" >> ~/.bashrc

sudo apt-get install openssh-server vim git python3-dev python3-pip python3-setuptools idle3

cd .cv2py37
sudo ./opencv_py37.sh $@
cd ..

pip3 install wheel
pip3 install idlex
pip3 install -r requirements.txt

exit 0

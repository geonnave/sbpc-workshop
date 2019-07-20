#!/bin/bash

sudo apt-get install openssh-server vim git python-dev python3-dev python-pip python3-pip python-setuptools python3-setuptools

cd .cv2py37
sudo ./opencv_py37.sh $@
cd ..

pip3 install wheel
pip3 install -r requirements.txt

[ -z "$(grep 'alias python' ~/.bashrc)" ] && echo "alias python=python3" >> .bashrc

exit 0

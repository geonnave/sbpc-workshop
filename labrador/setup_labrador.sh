#!/bin/bash

[ -z "$(grep 'alias python' ~/.bashrc)" ] && echo "alias python=python3" >> ~/.bashrc

sudo apt-get install openssh-server vim git python3-dev python3-pip python3-setuptools idle3

CV_LIB=/home/caninos/lib/opencv_py37/lib/
cd .cv2py37
[ "$1" == "--no-deps" ] && no_deps=--no-deps || no_deps=deps
sudo ./opencv_py37.sh $1 $CV_LIB
cd ..

pip3 install wheel
pip3 install -r requirements.txt

pip3 install idlex
cat << EOF > ./idle.sh
#!/bin/bash

export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:$CV_LIB
/home/caninos/.local/bin/idlex

exit 0
EOF

read -p "Pronto."

exit 0


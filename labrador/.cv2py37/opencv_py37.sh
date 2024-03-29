
install_deps() {
	sudo apt-get update
	sudo apt-get -y upgrade

	# Build tools:
	sudo apt-get install -y build-essential cmake

	# GUI (if you want GTK, change 'qt5-default' to 'libgtkglext1-dev' and remove '-DWITH_QT=ON'):
	sudo apt-get install -y qt5-default libvtk6-dev

	# Media I/O:
	sudo apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev \
				libopenexr-dev libgdal-dev

	# Video I/O:
	sudo apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev \
				libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm \
				libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev

	# Parallelism and linear algebra libraries:
	sudo apt-get install -y libtbb-dev libeigen3-dev

	# Python:
	sudo apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy

	# Documentation:
	sudo apt-get install -y doxygen
}

[ "$1" != "--no-deps" ] && install_deps

HOME=/home/caninos
[ ! -z "$2" ] && CV_LIB=$2 || exit 1
echo CV_LIB is $CV_LIB

mkdir -p $CV_LIB
cp -r ./lib/* $CV_LIB/

sudo cp "$CV_LIB"/python3/cv2.cpython-37m-arm-linux-gnueabihf.so /usr/local/lib/python3.7/dist-packages/cv2.so

sudo touch /etc/ld.so.conf.d/opencv.conf
sudo echo "$CV_LIB" > /etc/ld.so.conf.d/opencv.conf
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CV_LIB" >> $HOME/.bashrc
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CV_LIB" >> $HOME/.profile

exit 0

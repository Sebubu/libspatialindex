#!/usr/bin/env bash

# Install this library to import the rtree index which is used in polygon_list.py

echo Install libspatialindex
apt-get update
apt-get -y install autoconf automake libtool git build-essential

cd build

git clone https://github.com/libspatialindex/libspatialindex.git

#cd libspatialindex
#./autogen.sh
#./configure; make; make install; ldconfig



echo Installation completed


#!/usr/bin/env bash

# Install this library to import the rtree index which is used in polygon_list.py

echo - Build spatialindex
cd ../builded

if [ -f ./libspatialindex/compile ]; then
    echo - Already built before
fi

if [ ! -f ./libspatialindex/compile ]; then
    echo - Start build
    apt-get update
    apt-get -y install autoconf automake libtool git build-essential

    git clone https://github.com/libspatialindex/libspatialindex.git
    cd libspatialindex
    ./autogen.sh
    ./configure; make;
    cd ..
    echo - Build completed
fi










#!/usr/bin/env bash

# Install this library to import the rtree index which is used in polygon_list.py

echo - Build spatialindex
cd libspatialindex_sbu

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
    ./configure; make; make
    cd ..
    echo - Build completed
fi
ls
rm -rf ../build/lib/libspatialindex_sbu/libspatialindex
cp -R libspatialindex ../build/lib/libspatialindex_sbu








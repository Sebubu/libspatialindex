#!/usr/bin/env bash

# Install this library to import the rtree index which is used in polygon_list.py

echo Install libspatialindex

cd libspatialindex
make install; ldconfig
echo Installation completed


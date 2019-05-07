#!/bin/bash

export PYTHONPATH=/usr/bin/python3
BASE_DIR=$(pwd)
export PYQTDESIGNERPATH=$BASE_DIR/flfielddb:$BASE_DIR/fltabledb:$BASE_DIR/fltable

designer

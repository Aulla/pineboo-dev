#!/bin/bash

#export PYTHONPATH=/usr/bin/python3
BASE_DIR=$(pwd)
export PYQTDESIGNERPATH=/home/aulla/repos/github/pineboo-dev/plugins_designer/python
export PYTHONPATH=/home/aulla/repos/github/pineboo-dev/plugins_designer/widgets
export QT_DEBUG_PLUGINS=1
designer

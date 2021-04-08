# https://github.com/baoboa/pyqt5/blob/master/examples/designer/plugins/plugins.py

from PyQt6 import QtCore, QtWidgets
import os
import sys


app = QtWidgets.QApplication(sys.argv)
base = os.path.dirname(__file__)

env = QtCore.QProcessEnvironment.systemEnvironment()
env.insert('PYQTDESIGNERPATH', os.path.join(base, 'python'))
env.insert('PYTHONPATH', os.path.join(base, 'widget'))

designer = QtCore.QProcess()
designer.setProcessEnvironment(env)
designer_bin = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.BinariesPath)

if sys.platform == 'darwin':
    designer_bin += '/Designer.app/Contents/MacOS/Designer'
else:
    designer_bin += '/designer'

designer.start(designer_bin)
designer.waitForFinished(-1)

sys.exit(designer.exitCode())

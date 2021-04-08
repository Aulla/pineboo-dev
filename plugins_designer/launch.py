# https://github.com/baoboa/pyqt5/blob/master/examples/designer/plugins/plugins.py

from PyQt6 import QtCore, QtWidgets
import os
import sys


app = QtWidgets.QApplication(sys.argv)
base = os.path.dirname(__file__)

env = QtCore.QProcessEnvironment.systemEnvironment()
env.insert('PYQTDESIGNERPATH', os.path.join(base, 'python'))
env.insert('PYTHONPATH', os.path.join(base, 'widgets'))
env.insert('QT_DEBUG_PLUGINS', "1")

designer = QtCore.QProcess()
designer.setProcessEnvironment(env)

designer_bin = None

if sys.platform == 'darwin':
    designer_bin = QtCore.QLibraryInfo.LibraryPath.BinariesPath
    designer_bin += '/Designer.app/Contents/MacOS/Designer'
else:
    designer_bin = '/usr/bin/designer'

print("Lanzando", designer_bin)
print("Plugings especificados en", os.path.join(base, 'python'))
print("Controles especificados en", os.path.join(base, 'widget'))
designer.start(designer_bin)
designer.waitForFinished(-1)

sys.exit(designer.exitCode())

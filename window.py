import sys
from PyQt4 import QtGui
from win32api import GetSystemMetrics
#tried to make the application begin in the middle of the screen but i failed
#will try to make it happen for todolist application
app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(50,100,500,500)
window.setWindowTitle("Python GUI")

window.show();

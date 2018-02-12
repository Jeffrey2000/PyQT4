import sys
from PyQt4 import QtGui

#Python OOP for GUI, makes sense for anything that may interact with it in a dynamic way

class mainFrame(QtGui.QMainWindow):

    def __init__(self):
        super(mainFrame, self).__init__(); # Calling the superclasses constructor function. But why?
        #ok just read that __init__ isn't a constructor -- it's an initializer
        #.. __new__ is the constructor and it's not automatically invoked
        self.setGeometry(50,50,500,500);
        self.setWindowTitle("Jeffrey's Application")
        self.setWindowIcon(QtGui.QIcon('jlogo.png'));
        self.show();


app = QtGui.QApplication(sys.argv);
appFrame = mainFrame()
sys.exit(app.exec_());


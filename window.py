import sys
from PyQt4 import QtGui,QtCore 

class mainFrame(QtGui.QMainWindow):

    def __init__(self):
        super(mainFrame, self).__init__();
        self.setGeometry(50,50,500,500);
        self.setWindowTitle("Jeffrey's Application")
        self.setWindowIcon(QtGui.QIcon('jlogo.png'));
        self.buttonQuit();


    def buttonQuit(self):
        quitButton = QtGui.QPushButton("Quit",self); 
      
        quitButton.clicked.connect(self.button_resize);#Takes reference to function


        #sizeHint() and minimumSizeHint() return suggested size and minimum suggested size respectively
        quitButton.resize(quitButton.sizeHint())
        quitButton.move(100,100);
        self.show();

        

    def close_application(self):
        print("Application closed");
        sys.exit();

    def button_resize(self):
        self.setWindowTitle("ZenithList")

    



def frameLoop():
    app = QtGui.QApplication(sys.argv);
    appFrame = mainFrame()
    sys.exit(app.exec_());


frameLoop();

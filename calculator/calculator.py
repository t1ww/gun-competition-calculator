# imports
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# code
def window():
   app = QApplication(sys.argv)
   
   widget = QWidget()
   widget.setGeometry(100,100,200,50)
   widget.setWindowTitle("PyQt5")

   label = QLabel(widget)
   label.setText("Hello World!")
   label.move(50,20)
   
   widget.show()
   sys.exit(app.exec_())

# main
if __name__ == '__main__':
   window()
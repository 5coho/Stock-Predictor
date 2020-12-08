"""
--The main file--

To start the program run this file

Creates The QApplication, Initializes GUI, then displays it.

"""


#Metadata
__author__          = "Scott Howes, Braeden Van Der Velde"
__credits__         = "Scott Howes, Braeden Van Der Velde"
__email__           = "showes@unbc.ca, "
__python_version__  = "3.9.0"


#imports go here
import sys
from seq_gui import seq_gui
from PyQt5.QtWidgets import QApplication


#defining the main function
#creates and shows the create node gui
def main():
    app = QApplication(sys.argv)
    gui = seq_gui()
    gui.show()
    sys.exit(app.exec_())


#running main()
if __name__ == "__main__":
    main()

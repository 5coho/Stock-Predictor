"""
--The main file--

To start the program run this file

Creates The QApplication, Initializes GUI, then displays it.

"""


#Metadata
__author__          = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__credits__         = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__email__           = "showes@unbc.ca, velde@unbc.ca, leary@unbc.ca"
__python_version__  = "3.8.1"


#imports go here
import sys
from gui import stock_gui
from PyQt5.QtWidgets import QApplication


#defining the main function
#creates and shows the create node gui
def main():
    app = QApplication(sys.argv)
    gui = stock_gui()
    gui.show()
    sys.exit(app.exec_())


#running main()
if __name__ == "__main__":
    main()

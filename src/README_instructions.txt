-Starting the Software
There are two ways to start our software. The first being through Python and the
second, by running the provide executable file, Stock Predictor.exe.
Below explains the steps involved for each.


-Installing Python
To install Python, please visit www.python.org for details. We built our project 
using Python version 3.8 but Python version 3.9 should also work.. maybe


-Dependencies
The full list of dependencies for our software outlined in requirements.txt:

altgraph==0.17
certifi==2020.12.5
chardet==3.0.4
click==7.1.2
future==0.18.2
idna==2.10
joblib==0.17.0
lxml==4.6.2
multitasking==0.0.9
numpy==1.19.3
pandas==1.1.5
pandas-datareader==0.9.0
pefile==2019.4.18
plotly==4.14.1
pyinstaller==4.1
pyinstaller-hooks-contrib==2020.10
PyQt5==5.15.1
pyqt5-plugins==5.15.1.2.0.1
PyQt5-sip==12.8.1
pyqt5-tools==5.15.1.3
PyQtWebEngine==5.15.2
python-dateutil==2.8.1
python-dotenv==0.15.0
pytz==2020.4
pywin32-ctypes==0.2.0
qt5-applications==5.15.1.2.1
qt5-tools==5.15.1.1.0.1
requests==2.25.0
retrying==1.3.3
scikit-learn==0.23.2
scipy==1.5.4
six==1.15.0
sklearn==0.0
threadpoolctl==2.1.0
urllib3==1.26.2
yfinance==0.1.55

To install all dependencies, using a command prompt or other shell environment
navigate to the requirements.txt file located in our projects src file folder.
Next, enter the following command:

    pip install -r requirements.txt

This will instruct pip, Python's package manager, to install all necessary
dependencies required to run our software.


-Running main.py
To run the software, navigate to the src file folder and enter:

    python main.py

This will run the main.py file and a GUI should appear.


-Using Executable
For convenience we have included an executable. To run the executable file,
navigate to our projects src file folder and double click on Stock Predictor.exe.
Our projects GUI should then appear.
NOTE: This executable is a shortcut.


-Predicting The Next Day Stock Price
To predict the Open, High, Low, and Close of a stock following the following
steps:
    1) Select a stock from combobox
    2) select a start date
    3) select an end date
    4) hit the plot button
    5) now, hit the predict button in the Linear Regression groupbox
    6) the predicted values will now appear in the appropriate labels
    7) profit (probably not)

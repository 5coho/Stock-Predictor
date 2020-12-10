#! /bin/bash

#This shell script will creat an executable for our project
#Ensure all python dependencies are install before running this script
#------NOTE------
#For some reason, numpy version 1.19.4 does not work well with pyinstaller
#only version 1.19.3 will work.

#creating executable
"pyinstaller" --onefile -i "media/chart.ico" --name="Stock Predictor" --noconsole main.py

#copying Stock Predictor executable to project root
cp "dist/Stock Predictor" .

#removing Stock Predictor.spec file created by pyinstaller
rm "Stock Predictor.spec"

#removing build folder created by pyinstaller
rm -r build

#removing dist folder created by pyinstaller
rm -r dist

# PyQt5_faceReognise

## Introduction
this is a project using PyQt5 GUI to show the face rocognise results. 
  
run this project,make sure you have the tensorflow and facenet foundation knowledge.

the recognise result has two methods:web_url、open local file
 
the recognise model can recogise parts of idols、gyms、politicians.more detail ,please reference the classiy.py .

## Dependencies

    sudo pip3 install PyQt5         

    sudo apt-get install python3-pyqt5 
    sudo apt-get install pyqt5-dev-tools
    sudo apt-get install qttools5-dev-tools

    qtchooser -run-tool=designer -qt=5       #open qtCreator

    python3 -m PyQt5.uic.pyuic main.ui -o main.py   #compile a .ui file to .py 
## Run the Project

    python show.py

# Results
1. recognise the local picture

![Figure_1](/data/Figure_1.png)

2. recognise according to a web url

![Figure_1-1](/data/Figure_1-1.png)

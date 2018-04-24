# -*- coding: utf-8 -*-
"""
Created on 21/03/2016

@author: Charlie Bourigault
@contact: bourigault.charlie@gmail.com

Please report issues and request on the GitHub project from ChrisEberl (Python_DIC)
More details regarding the project on the GitHub Wiki : https://github.com/ChrisEberl/Python_DIC/wiki

Current File: This file manages the main gui application on start-up and include functions to create process and threads
"""

import sys, multiprocessing
from PyQt5.QtWidgets import QApplication, QDockWidget,QActionGroup,QMainWindow,QFileDialog,QProgressDialog ,QDialog,QTabWidget,QAction, QVBoxLayout,QGridLayout, QSpinBox, QDoubleSpinBox, QWidget, QLabel, QLineEdit, QPushButton, QStatusBar, QMessageBox, QHBoxLayout, QGroupBox, QTableWidget, QTableWidgetItem, QAbstractItemView, QComboBox, QStyledItemDelegate, QCompleter, QCheckBox, QProgressBar,QSizePolicy, QMenuBar, QToolBar
from PyQt5.QtCore import Qt, QSize, QLocale, QThread, QObject, pyqtSignal, pyqtSlot, QMetaObject, Q_ARG, QCoreApplication, QTimer, QTime, QFileInfo
from PyQt5.QtGui import QValidator, QDoubleValidator,QRegExpValidator, QIntValidator, QImage, QPixmap, QIcon 
from interface import initApp, devMode

#PARAMETERS
PROFILE_FILE = 'profile.cfg'
DEFAULT_PROFILE = (['User','Guest'],['Default','1'],['FullScreen','0'],['Width','800'],['Height','600'],['CorrSize','15'],['nbProcesses','1']) #default values when new profile is created and when no profile file found
DEV_MODE = 0
#END PARAMETERS

class MainWindow(QMainWindow):
    def __init__(self): #initiate the main window
        super(MainWindow, self).__init__()
        initApp.initProfile(self, PROFILE_FILE, DEFAULT_PROFILE)
        initApp.setUpInterface(self, self.currentProfile)
        self.devWindow = devMode.DevMode(self, DEV_MODE)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    multiprocessing.set_start_method('spawn')
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

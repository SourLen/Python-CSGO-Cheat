import ctypes, keyboard, configparser, os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from Utils.Utilities import strtobool
import string
import random

class Ui_MainWindow(object):
    def __init__(self):
        self.Trigger = False
        self.Wallhack = False
        self.Bhop = False
        self.Noflash = False
        self.Togglefov = False
        self.Triggerkey = ""
        self.Fov = False
        self.Fovkey = ""
        self.Radar = False
        self.Aimbot = False
        self.Silentaim = False
        self.Baim = False
        self.Fovt = int()
        self.auto_strafe = False
        self.WRGB = [0, 0, 0]
        self.Ergb = [0, 0, 0]
        self.Argb = [0, 0, 0]
        self.Allies = False
        self.Enemies = False
        self.Healthbased = False
        self.RCS = False
        self.AimRCS = False
        self.Aimfov = int()
        self.Fovvaluke = int()
        self.Aimbotkey = str()
        self.Holdfov = False
        self.Eteam = False
        self.Chams = False
        self.spotted = False
        self.healthbasedWH = False
        self.sens = 0  # for testing 0.5 to 1.5
        self.random = 0  # for testing 5 to 25
        self.legitvar = False

    def legit(self):
        self.legitvar = True
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(True)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(True)
        self.checkBox_7.setChecked(True)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(False)
        self.checkBox_11.setChecked(False)
        self.checkBox_12.setChecked(True)
        self.checkBox_13.setChecked(False)
        self.checkBox_14.setChecked(True)
        self.checkBox_15.setChecked(False)
        self.checkBox_16.setChecked(False)
        self.checkBox_17.setChecked(False)
        self.checkBox_18.setChecked(False)
        self.checkBox_19.setChecked(True)
        self.comboBox.setCurrentText("GREEN")
        self.comboBox_2.setCurrentText("GREEN")
        self.lineEdit.setText("8")
        self.lineEdit_6.setText("30")
        self.lineEdit_7.setText("30")
        self.lineEdit_2.setText(self.lineEdit_8.text() if keyboard.is_modifier(self.lineEdit_8.text()) else "shift")
        self.update()

    def createConfig(self):
        self.update()
        config = configparser.ConfigParser()
        config["Visual"] = {
            "Glow": self.Wallhack,
            "GlowColor": self.comboBox_3.currentText(),
            "Chams": self.Chams,
            "Enemies": self.Enemies,
            "Teammates": self.Allies,
            "EColor": self.comboBox.currentText(),
            "AColor": self.comboBox_2.currentText(),
            "NoFlash": self.Noflash,
            "Radar": self.Radar,
        }
        config["MISC"] = {
            "FovChanger": self.Fov,
            "Hold": self.Holdfov,
            "FOVValue": self.Fovvaluke,
            "FovKey": self.Fovkey,
            "Bhop": self.Bhop,
            "AutoStrafe": self.auto_strafe
        }
        config["Aim"] = {
            "Aimbot": self.Aimbot,
            "RCSAim": self.AimRCS,
            "Silentaim": self.Silentaim,
            "BodyAim": self.Baim,
            "AimFov": self.Aimfov,
            "Spotted": self.spotted,
            "AimKey": self.Aimbotkey,
            "SmoothAim": self.smooth,
            "Smoothness": self.lineEdit_6.text(),
            "Random": self.checkBox_19.isChecked(),
            "Randomness": self.lineEdit_7.text(),
            "Triggerbot": self.Trigger,
            "Triggerkey": self.Triggerkey,
            "RCS": self.RCS
        }
        config["Legit"] = {
            "Legit": self.legitvar
        }
        self.filename = self.lineEdit_9.text() + ".ini"
        with open(f"./Configs/{self.filename}", "w+") as configfile:
            config.write(configfile)
        self.label_14.setText(self.lineEdit_9.text())

    def loadConfig(self):
        config = configparser.ConfigParser()
        self.filename = self.lineEdit_10.text() + ".ini"
        self.filepath = f"./Configs/{self.filename}"
        if os.path.isfile(self.filepath):
            config.read(self.filepath)
            if strtobool(config["Legit"]["Legit"]):
                self.legit()
            else:
                try:
                    self.checkBox.setChecked(strtobool(config["Visual"]["Glow"]))
                    self.comboBox_3.setCurrentText(config["Visual"]["GlowColor"])
                    self.checkBox_2.setChecked(strtobool(config["Visual"]["Chams"]))
                    self.checkBox_4.setChecked(strtobool(config["Visual"]["Enemies"]))
                    self.checkBox_5.setChecked(strtobool(config["Visual"]["Teammates"]))
                    self.comboBox.setCurrentText(config["Visual"]["EColor"])
                    self.comboBox_2.setCurrentText(config["Visual"]["AColor"])
                    self.checkBox_3.setChecked(strtobool(config["Visual"]["NoFlash"]))
                    self.checkBox_6.setChecked(strtobool(config["Visual"]["Radar"]))
                    self.checkBox_18.setChecked(strtobool(config["MISC"]["FovChanger"]))
                    self.checkBox_15.setChecked(strtobool(config["MISC"]["Hold"]))
                    self.lineEdit_3.setText(config["MISC"]["FOVValue"])
                    self.lineEdit_5.setText(config["MISC"]["FovKey"])
                    self.checkBox_16.setChecked(strtobool(config["MISC"]["Bhop"]))
                    self.checkBox_17.setChecked(strtobool(config["MISC"]["AutoStrafe"]))
                    self.checkBox_7.setChecked(strtobool(config["Aim"]["Aimbot"]))
                    self.checkBox_8.setChecked(strtobool(config["Aim"]["RCSAim"]))
                    self.checkBox_9.setChecked(strtobool(config["Aim"]["Silentaim"]))
                    self.checkBox_10.setChecked(strtobool(config["Aim"]["BodyAim"]))
                    self.lineEdit.setText(config["Aim"]["AimFov"])
                    self.checkBox_12.setChecked(strtobool(config["Aim"]["Spotted"]))
                    self.lineEdit_2.setText(config["Aim"]["AimKey"])
                    self.checkBox_14.setChecked(strtobool(config["Aim"]["SmoothAim"]))
                    self.lineEdit_6.setText(config["Aim"]["Smoothness"])
                    self.checkBox_19.setChecked(strtobool(config["Aim"]["Random"]))
                    self.lineEdit_7.setText(config["Aim"]["Randomness"])
                    self.checkBox_13.setChecked(strtobool(config["Aim"]["Triggerbot"]))
                    self.checkBox_11.setChecked(strtobool(config["Aim"]["RCS"]))
                    self.lineEdit_4.setText(config["Aim"]["Triggerkey"])
                except Exception as e:
                    pass
            self.label_14.setText(self.lineEdit_10.text())

        else:
            ctypes.windll.user32.MessageBoxW(0, "No file with this name exists", "Wrong File Error", 1)

    def saveConfig(self):
        self.filename = self.lineEdit_11.text() + ".ini"
        if os.path.isfile(f"./Configs/{self.filename}"):
            try:
                self.update()
                config = configparser.ConfigParser()
                config["Visual"] = {
                    "Glow": self.Wallhack,
                    "GlowColor": self.comboBox_3.currentText(),
                    "Chams": self.Chams,
                    "Enemies": self.Enemies,
                    "Teammates": self.Allies,
                    "EColor": self.comboBox.currentText(),
                    "AColor": self.comboBox_2.currentText(),
                    "NoFlash": self.Noflash,
                    "Radar": self.Radar,
                }
                config["MISC"] = {
                    "FovChanger": self.Fov,
                    "Hold": self.Holdfov,
                    "FOVValue": self.Fovvaluke,
                    "FovKey": self.Fovkey,
                    "Bhop": self.Bhop,
                    "AutoStrafe": self.auto_strafe
                }
                config["Aim"] = {
                    "Aimbot": self.Aimbot,
                    "RCSAim": self.AimRCS,
                    "Silentaim": self.Silentaim,
                    "BodyAim": self.Baim,
                    "AimFov": self.Aimfov,
                    "Spotted": self.spotted,
                    "AimKey": self.Aimbotkey,
                    "SmoothAim": self.smooth,
                    "Smoothness": self.lineEdit_6.text(),
                    "Random": self.checkBox_19.isChecked(),
                    "Randomness": self.lineEdit_6.text(),
                    "Triggerbot": self.Trigger,
                    "Triggerkey": self.Triggerkey,
                    "RCS": self.RCS
                }
                config["Legit"] = {
                    "Legit": self.legitvar
                }
                with open(f"./Configs/{self.filename}", "w") as configfile:
                    config.write(configfile)
                self.label_14.setText(self.lineEdit_11.text())
            except Exception as e:
                print(e)
                pass
        else:
            ctypes.windll.user32.MessageBoxW(0,"Create a new config file first", "This file doesnt exist", 1)

    def update(self):
        update = True
        while update:
            self.Wallhack = self.checkBox.isChecked()
            self.Chams = self.checkBox_2.isChecked()
            self.Noflash = self.checkBox_3.isChecked()
            self.Enemies = self.checkBox_4.isChecked()
            self.Allies = self.checkBox_5.isChecked()
            if self.comboBox.currentText() == "GREEN":
                self.Ergb = [0, 255, 0]
            elif self.comboBox.currentText() == "RED":
                self.Ergb = [255, 0, 0]
            elif self.comboBox.currentText() == "BLUE":
                self.Ergb = [0, 0, 255]
            elif self.comboBox.currentText() == "ORANGE":
                self.Ergb = [255, 69, 0]
            if self.comboBox_2.currentText() == "GREEN":
                self.Argb = [0, 255, 0]
            elif self.comboBox_2.currentText() == "RED":
                self.Argb = [255, 0, 0]
            elif self.comboBox_2.currentText() == "BLUE":
                self.Argb = [0, 0, 255]
            elif self.comboBox_2.currentText() == "ORANGE":
                self.Argb = [255, 69, 0]
            if self.comboBox_3.currentText() == "Healthbased":
                self.healthbasedWH = True
                self.WRGB = [0, 0, 0]
            elif self.comboBox_3.currentText() == "GREEN":
                self.healthbasedWH = False
                self.WRGB = [0, 255, 0]
            elif self.comboBox_3.currentText() == "RED":
                self.healthbasedWH = False
                self.WRGB = [255, 0, 0]
            elif self.comboBox_3.currentText() == "BLUE":
                self.healthbasedWH = False
                self.WRGB = [0, 0, 255]
            elif self.comboBox_3.currentText() == "Orange":
                self.healthbasedWH = False
                self.WRGB = [255, 69, 0]
            self.Radar = self.checkBox_6.isChecked()
            self.Aimbot = self.checkBox_7.isChecked()
            self.AimRCS = self.checkBox_8.isChecked()
            self.Silentaim = self.checkBox_9.isChecked()
            self.Baim = self.checkBox_10.isChecked()
            self.Aimfov = int(self.lineEdit.text())
            self.spotted = self.checkBox_12.isChecked()
            self.Trigger = self.checkBox_13.isChecked()
            self.Aimbotkey = self.lineEdit_2.text().lower()
            self.RCS = self.checkBox_11.isChecked()
            self.Holdfov = self.checkBox_15.isChecked()
            self.Fovvaluke = int(self.lineEdit_3.text())
            self.Bhop = self.checkBox_16.isChecked()
            self.auto_strafe = self.checkBox_17.isChecked()
            self.Fov = self.checkBox_18.isChecked()
            self.Fovkey = self.lineEdit_5.text()
            self.Triggerkey = self.lineEdit_4.text()
            self.smooth = self.checkBox_14.isChecked()
            if self.checkBox_14.isChecked():
                if 0 < int(self.lineEdit_6.text()) < 100:
                    self.sens = int(self.lineEdit_6.text()) / 100
                    self.sens += 0.5
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Please enter a value from 0 to 100", "Error in Config", 1)
            if self.checkBox_19.isChecked():
                if 0 < int(self.lineEdit_7.text()) < 100:
                    self.random = 5 + (int(self.lineEdit_7.text()) / 5)
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Please enter a value from 0 to 100", "Error in Config", 1)
            if self.Aimbot and not keyboard.is_modifier(self.Aimbotkey):
                ctypes.windll.user32.MessageBoxW(0, "Please enter an valid Aimbot Key", "Error in Config", 1)
            if self.Silentaim and not self.Aimbot:
                ctypes.windll.user32.MessageBoxW(0, "Select Aimbot if you wanna use Silentaim", "Error in Config", 1)
            if self.Trigger and not keyboard.is_modifier(self.Triggerkey):
                ctypes.windll.user32.MessageBoxW(0, "Please select a correct Triggerbotkey", "Error in Config", 1)
            if self.Fov and not keyboard.is_modifier(self.Fovkey):
                ctypes.windll.user32.MessageBoxW(0, "Please select a correct Fovkey", "Error in Config", 1)
            self.label_14.setText("None/Unsaved")
            update = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 633)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 671))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(50, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(50, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(50, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(70, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(70, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(270, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(50, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(200, 520, 211, 51))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(270, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.checkBox_15 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_15.setGeometry(QtCore.QRect(70, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setObjectName("checkBox_15")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 100, 101, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox_16 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_16.setGeometry(QtCore.QRect(50, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_17.setGeometry(QtCore.QRect(50, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_17.setFont(font)
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_18.setGeometry(QtCore.QRect(50, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_18.setFont(font)
        self.checkBox_18.setObjectName("checkBox_18")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 520, 211, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 150, 101, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 151, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(180, 100, 151, 31))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_7.setGeometry(QtCore.QRect(50, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_8.setGeometry(QtCore.QRect(70, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_9.setGeometry(QtCore.QRect(70, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_10.setGeometry(QtCore.QRect(70, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(70, 200, 51, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(130, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox_12 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_12.setGeometry(QtCore.QRect(70, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_13.setGeometry(QtCore.QRect(390, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 300, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_11.setGeometry(QtCore.QRect(390, 120, 141, 21))
        self.checkBox_11.setObjectName("checkBox_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(390, 60, 201, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox_14 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_14.setGeometry(QtCore.QRect(70, 350, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setObjectName("checkBox_14")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 390, 51, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(130, 390, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.checkBox_19 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_19.setGeometry(QtCore.QRect(70, 440, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_19.setFont(font)
        self.checkBox_19.setObjectName("checkBox_19")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 520, 211, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 480, 51, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(130, 480, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 500, 211, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(210, 320, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(210, 90, 201, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(130, 130, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(200, 170, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 110, 201, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(20, 200, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(150, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 260, 201, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(150, 520, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 410, 211, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(10, 350, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_11.setGeometry(QtCore.QRect(150, 360, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(390, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(390, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        processName = ''.join(random.choices(string.ascii_uppercase + string.digits, k = random.randint(4, 10)))
        MainWindow.setWindowTitle(_translate("MainWindow", processName))
        self.checkBox.setText(_translate("MainWindow", "GLOW"))
        self.checkBox_2.setText(_translate("MainWindow", "CHAMS"))
        self.checkBox_3.setText(_translate("MainWindow", "NOFLASH"))
        self.checkBox_4.setText(_translate("MainWindow", "ENEMIES"))
        self.checkBox_5.setText(_translate("MainWindow", "TEAMMATES"))
        self.comboBox.setItemText(0, _translate("MainWindow", "GREEN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.comboBox.setItemText(2, _translate("MainWindow", "BLUE"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ORANGE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Healthbased"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "GREEN"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "RED"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "BLUE"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "ORANGE"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Healthbased"))
        self.checkBox_6.setText(_translate("MainWindow", "RADAR"))
        self.pushButton.setText(_translate("MainWindow", "UPDATE"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Healthbased"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "GREEN"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "RED"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "BLUE"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "ORANGE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "VISUALS"))
        self.checkBox_15.setText(_translate("MainWindow", "HOLD TO CHANGE FOV"))
        self.lineEdit_3.setText(_translate("MainWindow", "120"))
        self.checkBox_16.setText(_translate("MainWindow", "BHOP"))
        self.checkBox_17.setText(_translate("MainWindow", "AUTO STRAFE"))
        self.checkBox_18.setText(_translate("MainWindow", "FOV CHANGER"))
        self.pushButton_3.setText(_translate("MainWindow", "UPDATE"))
        self.lineEdit_5.setText(_translate("MainWindow", "control"))
        self.label_2.setText(_translate("MainWindow", "FOV KEY"))
        self.label_3.setText(_translate("MainWindow", "FOV VALUE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "MISC"))
        self.checkBox_7.setText(_translate("MainWindow", "AIMBOT"))
        self.checkBox_8.setText(_translate("MainWindow", "RCS WITH AIMBOT"))
        self.checkBox_9.setText(_translate("MainWindow", "SILENTAIM"))
        self.checkBox_10.setText(_translate("MainWindow", "BODY AIM"))
        self.lineEdit.setText(_translate("MainWindow", "120"))
        self.label.setText(_translate("MainWindow", "AIMBOT FOV"))
        self.checkBox_12.setText(_translate("MainWindow", "ONLY SPOTTED"))
        self.checkBox_13.setText(_translate("MainWindow", "TRIGGERBOT"))
        self.lineEdit_2.setText(_translate("MainWindow", "AIMBOT KEY"))
        self.checkBox_11.setText(_translate("MainWindow", "RCS"))
        self.lineEdit_4.setText(_translate("MainWindow", "TRIGGERBOT KEY"))
        self.checkBox_14.setText(_translate("MainWindow", "Smooth/Magnetic Aim"))
        self.lineEdit_6.setText(_translate("MainWindow", "50"))
        self.label_4.setText(_translate("MainWindow", "Smoothness %"))
        self.checkBox_19.setText(_translate("MainWindow", "Random First Snappoint"))
        self.pushButton_2.setText(_translate("MainWindow", "UPDATE"))
        self.lineEdit_7.setText(_translate("MainWindow", "50"))
        self.label_5.setText(_translate("MainWindow", "Randomness %"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "AIM"))
        self.pushButton_4.setText(_translate("MainWindow", "Enable Legitbot"))
        self.lineEdit_8.setText(_translate("MainWindow", "AIMBOT KEY"))
        self.label_7.setText(_translate("MainWindow", "-enables low-fov, smooth, random Aimbot"))
        self.label_8.setText(_translate("MainWindow", "-enables Chams, Radar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Legit"))
        self.pushButton_5.setText(_translate("MainWindow", "Create new Config"))
        self.label_9.setText(_translate("MainWindow", "Config Name"))
        self.lineEdit_9.setText(_translate("MainWindow", "example"))
        self.label_10.setText(_translate("MainWindow", "Config Name"))
        self.lineEdit_10.setText(_translate("MainWindow", "example"))
        self.pushButton_6.setText(_translate("MainWindow", "Load Config"))
        self.label_11.setText(_translate("MainWindow", "Config files are saved under ./Configs"))
        self.pushButton_7.setText(_translate("MainWindow", "Save current Config"))
        self.label_12.setText(_translate("MainWindow", "Config Name"))
        self.lineEdit_11.setText(_translate("MainWindow", "example"))
        self.label_13.setText(_translate("MainWindow", "Current Config:"))
        self.label_14.setText(_translate("MainWindow", "None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Config"))
        self.pushButton.clicked.connect(self.update)
        self.pushButton_2.clicked.connect(self.update)
        self.pushButton_3.clicked.connect(self.update)
        self.pushButton_4.clicked.connect(self.legit)
        self.pushButton_5.clicked.connect(self.createConfig)
        self.pushButton_6.clicked.connect(self.loadConfig)
        self.pushButton_7.clicked.connect(self.saveConfig)

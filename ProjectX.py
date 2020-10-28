
import keyboard
import time
from win32gui import GetWindowText, GetForegroundWindow
import threading
import pymem
import pymem.process
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

offsets = 'https://raw.githubusercontent.com/kadeeq/ProjectX/main/offsets/offsets.json'
response = requests.get(offsets).json()


dwEntityList = int(response["signatures"]["dwEntityList"])
dwGlowObjectManager = int(response["signatures"]["dwGlowObjectManager"])
m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])
m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
dwForceJump = int(response["signatures"]["dwForceJump"])
dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
m_fFlags = int(response["netvars"]["m_fFlags"])
dwForceAttack = int(response["signatures"]["dwForceAttack"])
m_iCrosshairId = int(response["netvars"]["m_iCrosshairId"])


bhop_taste = "space"


class Ui_MainWindow(object):
    def __init__(self):
        self.trigc = False
        self.whc = False
        self.bhc = False
        self.triggerkey = ""

    def setupUi(self, MainWindow):
        color = "color: white"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(316, 385)
        MainWindow.setFixedSize(316, 385)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./pics/bgv7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setPixmap(QtGui.QPixmap("./pics/bgv7.png"))
        self.label.setGeometry(QtCore.QRect(0, 0, 316, 385))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 280, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setToolTipDuration(1)
        self.pushButton.setStyleSheet("background-color: black:\n"
"border: 1px solid black")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setStyleSheet("color: red")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(100, 60, 111, 41))
        self.checkBox.setStyleSheet(color)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 110, 111, 41))
        self.checkBox_2.setStyleSheet(color)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(100, 160, 111, 41))
        self.checkBox_3.setStyleSheet(color)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 230, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 230, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet(color)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 161, 41))
        self.label_2.setStyleSheet(color)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(color)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project X"))
        self.pushButton.setText(_translate("MainWindow", "UPDATE"))
        self.checkBox.setText(_translate("MainWindow", "Bunnyhop"))
        self.checkBox_2.setText(_translate("MainWindow", "Wallhack"))
        self.checkBox_3.setText(_translate("MainWindow", "Triggerbot"))
        self.label.setText(_translate("MainWindow", "Triggerkey:"))
        self.label_2.setText(_translate("MainWindow", "Project X"))

    def update(self):
        update = True
        while update:
            self.trigc = self.checkBox_3.isChecked()
            self.bhc = self.checkBox.isChecked()
            self.whc = self.checkBox_2.isChecked()
            self.triggerkey = self.lineEdit.text()
            update = False

    def bh(self):
        pm = pymem.Pymem("csgo.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        bhm = True
        while bhm:
            while self.bhc is True:
                if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                    continue

                if keyboard.is_pressed(bhop_taste):
                    force_jump = client + dwForceJump
                    player = pm.read_int(client + dwLocalPlayer)
                    if player:
                        on_ground = pm.read_int(player + m_fFlags)
                        if on_ground and on_ground == 257:
                            pm.write_int(force_jump, 5)
                            time.sleep(0.08)
                            pm.write_int(force_jump, 4)

                time.sleep(0.002)
            while self.bhc is False:
                time.sleep(0.001)
                continue

    def trigger(self):
        pm = pymem.Pymem("csgo.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        triggerm = True
        while triggerm:
            while self.trigc is True:
                if not keyboard.is_pressed(self.triggerkey):
                    time.sleep(0.1)

                if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                    continue

                if keyboard.is_pressed(self.triggerkey):
                    player = pm.read_int(client + dwLocalPlayer)
                    entity_id = pm.read_int(player + m_iCrosshairId)
                    entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

                    entity_team = pm.read_int(entity + m_iTeamNum)
                    player_team = pm.read_int(player + m_iTeamNum)

                    if 0 < entity_id <= 64 and player_team != entity_team:
                        pm.write_int(client + dwForceAttack, 6)

                    time.sleep(0.006)
            while self.trigc is False:
                time.sleep(0.001)
                continue

    def wh(self):
        pm = pymem.Pymem("csgo.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        whm = True
        while whm:
            while self.whc is True:

                glow_manager = pm.read_int(client + dwGlowObjectManager)

                for i in range(1, 32):  # Das sind die Spieler Entities
                    entity = pm.read_int(client + dwEntityList + i * 0x10)

                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        entity_glow = pm.read_int(entity + m_iGlowIndex)

                        if entity_team_id == 2:  # Terrorist
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)

                        elif entity_team_id == 3:
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)
            while self.whc is False:
                time.sleep(0.001)
                continue



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    threadtrigger = threading.Thread(target=ui.trigger)
    threadbh = threading.Thread(target=ui.bh)
    threadwh = threading.Thread(target=ui.wh)
    threadbh.start()
    threadtrigger.start()
    threadwh.start()
    sys.exit(app.exec_())

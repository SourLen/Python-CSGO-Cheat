import time
import threading
import keyboard, mouse
import pymem
import pymem.process
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from math import *
import ctypes
import random

# Im not going to clean this file, and leave it as is.


offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get( offsets ).json()
bhop_taste = "space"
m_iCompetitiveWins = int(response["netvars"]["m_iCompetitiveWins"])
dwEntityList = int( response["signatures"]["dwEntityList"] )
dwGlowObjectManager = int( response["signatures"]["dwGlowObjectManager"] )
m_iGlowIndex = int( response["netvars"]["m_iGlowIndex"] )
m_iTeamNum = int( response["netvars"]["m_iTeamNum"] )
dwForceJump = int( response["signatures"]["dwForceJump"] )
dwLocalPlayer = int( response["signatures"]["dwLocalPlayer"] )
m_fFlags = int( response["netvars"]["m_fFlags"] )
dwForceAttack = int( response["signatures"]["dwForceAttack"] )
m_iCrosshairId = int( response["netvars"]["m_iCrosshairId"] )
m_flFlashMaxAlpha = int( response["netvars"]["m_flFlashMaxAlpha"] )
m_iDefaultFOV = (13116)
dwClientState = int( response["signatures"]["dwClientState"] )
m_iHealth = int( response["netvars"]["m_iHealth"] )
dwViewMatrix = int( response["signatures"]["dwViewMatrix"] )
m_dwBoneMatrix = int( response["netvars"]["m_dwBoneMatrix"] )
dwClientState_ViewAngles = int( response["signatures"]["dwClientState_ViewAngles"] )
m_vecOrigin = int( response["netvars"]["m_vecOrigin"] )
m_vecViewOffset = int( response["netvars"]["m_vecViewOffset"] )
dwbSendPackets = int( response["signatures"]["dwbSendPackets"] )
dwInput = int( response["signatures"]["dwInput"] )
clientstate_net_channel = int( response["signatures"]["clientstate_net_channel"] )
clientstate_last_outgoing_command = int( response["signatures"]["clientstate_last_outgoing_command"] )
m_bSpotted = int( response["netvars"]["m_bSpotted"] )
m_iShotsFired = int( response["netvars"]["m_iShotsFired"] )
m_aimPunchAngle = int( response["netvars"]["m_aimPunchAngle"] )
m_bGunGameImmunity = int( response["netvars"]["m_bGunGameImmunity"] )
m_bIsDefusing = int( response["netvars"]["m_bIsDefusing"] )
m_bDormant = int( response["signatures"]["m_bDormant"] )
dwClientState_PlayerInfo = int( response["signatures"]["dwClientState_PlayerInfo"] )
dwPlayerResource = int( response["signatures"]["dwPlayerResource"] )
m_iCompetitiveRanking = int( response["netvars"]["m_iCompetitiveRanking"] )
eteam = False
antivacv2 = random.randint(1,100)
antivac = "foqnmwordqowjm333q3q3q3q5q4q3"
print(antivac)
print(antivacv2)

user32 = ctypes.windll.user32
def is_press(key):
    if key != "x2" and key != "x" and key != "right" and key != "wheel" and key != "left":
        return keyboard.is_pressed(key)
    else:
        return mouse.is_pressed(key)

def GetWindowText(handle, length=100):

    window_text = ctypes.create_string_buffer(length)
    user32.GetWindowTextA(
        handle,
        ctypes.byref(window_text),
        length
    )

    return window_text.value


def GetForegroundWindow():

    return user32.GetForegroundWindow()

def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex

    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey


def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY


def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True


def nanchecker(first, second):
    if isnan( first ) or isnan( second ):
        return False
    else:
        return True


def Distance(src_x, src_y, src_z, dst_x, dst_y, dst_z):
    try:
        diff_x = src_x - dst_x
        diff_y = src_y - dst_y
        diff_z = src_z - dst_z
        return sqrt( diff_x * diff_x + diff_y * diff_y + diff_z * diff_z )
    except:
        pass


def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    try:
        delta_x = localpos1 - enemypos1
        delta_y = localpos2 - enemypos2
        delta_z = localpos3 - enemypos3
        hyp = sqrt( delta_x * delta_x + delta_y * delta_y + delta_z * delta_z )
        x = asin( delta_z / hyp ) * 57.295779513082
        y = atan( delta_y / delta_x ) * 57.295779513082
        if delta_x >= 0.0:
            y += 180.0
    except:
        return 0,0
    return x, y




class Ui_MainWindow( object ):

    def __init__(self):
        self.trigc = False
        self.whc = False
        self.bhc = False
        self.nf = False
        self.fovtog = False
        self.triggerkey = ""
        self.fovt = False
        self.fovkey = ""
        self.radarc = False
        self.aimc = False
        self.silentshit = False
        self.baim = False
        self.Fov = int()
        self.pm = pymem.Pymem( "csgo.exe" )
        self.client = pymem.process.module_from_name( self.pm.process_handle, "client.dll" ).lpBaseOfDll
        self.engine = pymem.process.module_from_name( self.pm.process_handle, "engine.dll" ).lpBaseOfDll
        self.rcse = False
        self.aimrcs = False
        self.aimfov = int()
        self.fovvalue = int()
        self.aimkey = str()
        self.larryfov = False

    def update(self):
        update = True
        while update:
            self.radarc = self.checkBox_3.isChecked()
            self.whc = self.checkBox.isChecked()
            self.nf = self.checkBox_2.isChecked()
            self.fovt = self.checkBox_4.isChecked()
            self.trigc = self.checkBox_5.isChecked()
            self.aimc = self.checkBox_6.isChecked()

            self.baim = self.checkBox_7.isChecked()
            if self.baim and not self.aimc:
                print('Activate aimbot to use the "Aim for Body function')
                self.checkBox_7.setChecked(False)

            if self.aimc:
                try:
                    self.aimfov = float( self.lineEdit_4.text() )
                    if self.lineEdit_6.text() == "MB5":
                        self.aimkey = "x2"
                    elif self.lineEdit_6.text()=="MB4":
                        self.aimkey = "x"
                    elif self.lineEdit_6.text() == "ML":
                        self.aimkey = "left"
                    elif self.lineEdit_6.text() == "MR":
                        self.aimkey = "right"
                    else:
                        self.aimkey = str( self.lineEdit_6.text() )
                except:
                    print( "Use different aimbot values" )
                    self.aimc = False
                    self.checkBox_6.setChecked( False )
            if self.fovt:
                try:
                    self.fovvalue = int( self.lineEdit.text() )
                    if self.lineEdit_2.text() == "MB5":
                        self.fovkey = "x2"
                    elif self.lineEdit_2.text() == "MB4":
                        self.fovkey = "x"
                    elif self.lineEdit_2.text() == "ML":
                        self.fovkey = "left"
                    elif self.lineEdit_2.text() == "MR":
                        self.fovkey = "right"
                    else:
                        self.fovkey = str(self.lineEdit_2.text())
                except:
                    print( "Use different fov values" )
            try:
                if self.lineEdit_3.text() == "MB5":
                    self.triggerkey  = "x2"
                elif self.lineEdit_3.text() == "MB4":
                    self.triggerkey  = "x"
                elif self.lineEdit_3.text() == "ML":
                    self.triggerkey  = "left"
                elif self.lineEdit_3.text() == "MR":
                    self.triggerkey = "right"
                else:
                    self.triggerkey = str(self.lineEdit_3.text())
            except:
                print("Use a different triggerkey")
            self.bhc = self.checkBox_8.isChecked()
            self.rcse = self.checkBox_10.isChecked()
            self.silentshit = self.checkBox_9.isChecked()
            if self.silentshit and not self.aimc:
                print( "You need to activate aimbot to use silentaim" )
                self.silentshit = False
                self.checkBox_9.setChecked( False )

            self.larryfov = self.checkBox_11.isChecked()
            if self.larryfov and not self.fovt:
                print( 'You need to activate Fov Changer to use the "Hold to change function"' )
                self.larryfov = False
                self.checkBox_11.setChecked( False )

            self.aimrcs = self.checkBox_12.isChecked()
            update = False
        time.sleep( 1 )

    def setupUi(self, ProjectMarya):
        ProjectMarya.setObjectName( "ProjectMarya" )
        ProjectMarya.resize( 960, 456 )
        font = QtGui.QFont()
        font.setFamily( "Calibri" )
        font.setPointSize( 20 )
        ProjectMarya.setFont( font )
        icon = QtGui.QIcon()
        ProjectMarya.setWindowIcon( icon )
        self.centralwidget = QtWidgets.QWidget( ProjectMarya )
        self.centralwidget.setObjectName( "centralwidget" )
        self.checkBox = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox.setGeometry( QtCore.QRect( 120, 180, 161, 41 ) )
        font = QtGui.QFont()
        font.setFamily( "MS Shell Dlg 2" )
        font.setPointSize( 20 )
        self.checkBox.setFont( font )
        self.checkBox.setObjectName( "checkBox" )
        self.checkBox_2 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_2.setGeometry( QtCore.QRect( 120, 230, 161, 41 ) )
        font = QtGui.QFont()
        font.setFamily( "MS Shell Dlg 2" )
        font.setPointSize( 20 )
        self.checkBox_2.setFont( font )
        self.checkBox_2.setObjectName( "checkBox_2" )
        self.checkBox_3 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_3.setGeometry( QtCore.QRect( 120, 280, 161, 51 ) )
        font = QtGui.QFont()
        font.setFamily( "MS Shell Dlg 2" )
        font.setPointSize( 20 )
        self.checkBox_3.setFont( font )
        self.checkBox_3.setObjectName( "checkBox_3" )
        self.checkBox_4 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_4.setGeometry( QtCore.QRect( 120, 90, 181, 41 ) )
        font = QtGui.QFont()
        font.setFamily( "MS Shell Dlg 2" )
        font.setPointSize( 20 )
        self.checkBox_4.setFont( font )
        self.checkBox_4.setObjectName( "checkBox_4" )
        self.checkBox_5 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_5.setGeometry( QtCore.QRect( 370, 90, 181, 41 ) )
        font = QtGui.QFont()
        font.setFamily( "MS Shell Dlg 2" )
        font.setPointSize( 20 )
        self.checkBox_5.setFont( font )
        self.checkBox_5.setObjectName( "checkBox_5" )
        self.checkBox_6 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_6.setGeometry( QtCore.QRect( 370, 140, 181, 41 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.checkBox_6.setFont( font )
        self.checkBox_6.setObjectName( "checkBox_6" )
        self.checkBox_7 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_7.setGeometry( QtCore.QRect( 390, 230, 181, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 15 )
        self.checkBox_7.setFont( font )
        self.checkBox_7.setObjectName( "checkBox_7" )
        self.lineEdit_2 = QtWidgets.QLineEdit( self.centralwidget )
        self.lineEdit_2.setGeometry( QtCore.QRect( 810, 160, 131, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 13 )
        self.lineEdit_2.setFont( font )
        self.lineEdit_2.setStyleSheet( "border:None" )
        self.lineEdit_2.setObjectName( "lineEdit_2" )
        self.lineEdit_4 = QtWidgets.QLineEdit( self.centralwidget )
        self.lineEdit_4.setGeometry( QtCore.QRect( 810, 260, 131, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 13 )
        self.lineEdit_4.setFont( font )
        self.lineEdit_4.setStyleSheet( "border:None" )
        self.lineEdit_4.setObjectName( "lineEdit_4" )
        self.lineEdit = QtWidgets.QLineEdit( self.centralwidget )
        self.lineEdit.setGeometry( QtCore.QRect( 810, 110, 131, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 13 )
        self.lineEdit.setFont( font )
        self.lineEdit.setStyleSheet( "border:None" )
        self.lineEdit.setObjectName( "lineEdit" )
        self.label = QtWidgets.QLabel( self.centralwidget )
        self.label.setGeometry( QtCore.QRect( 590, 100, 161, 41 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.label.setFont( font )
        self.label.setObjectName( "label" )
        self.checkBox_8 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_8.setGeometry( QtCore.QRect( 370, 310, 151, 51 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.checkBox_8.setFont( font )
        self.checkBox_8.setObjectName( "checkBox_8" )
        self.lineEdit_6 = QtWidgets.QLineEdit( self.centralwidget )
        self.lineEdit_6.setGeometry( QtCore.QRect( 810, 300, 131, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 13 )
        self.lineEdit_6.setFont( font )
        self.lineEdit_6.setStyleSheet( "border:None;\n"
                                       "" )
        self.lineEdit_6.setObjectName( "lineEdit_6" )
        self.label_2 = QtWidgets.QLabel( self.centralwidget )
        self.label_2.setGeometry( QtCore.QRect( 590, 150, 201, 41 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.label_2.setFont( font )
        self.label_2.setObjectName( "label_2" )
        self.label_3 = QtWidgets.QLabel( self.centralwidget )
        self.label_3.setGeometry( QtCore.QRect( 590, 200, 181, 41 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.label_3.setFont( font )
        self.label_3.setObjectName( "label_3" )
        self.label_4 = QtWidgets.QLabel( self.centralwidget )
        self.label_4.setGeometry( QtCore.QRect( 590, 250, 151, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.label_4.setFont( font )
        self.label_4.setObjectName( "label_4" )
        self.lineEdit_3 = QtWidgets.QLineEdit( self.centralwidget )
        self.lineEdit_3.setGeometry( QtCore.QRect( 810, 210, 131, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 13 )
        self.lineEdit_3.setFont( font )
        self.lineEdit_3.setStyleSheet( "border:None" )
        self.lineEdit_3.setObjectName( "lineEdit_3" )
        self.label_6 = QtWidgets.QLabel( self.centralwidget )
        self.label_6.setGeometry( QtCore.QRect( 590, 300, 181, 41 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.label_6.setFont( font )
        self.label_6.setObjectName( "label_6" )
        self.pushButton = QtWidgets.QPushButton( self.centralwidget )
        self.pushButton.setGeometry( QtCore.QRect( 20, 340, 221, 91 ) )
        font = QtGui.QFont()
        font.setPointSize( 30 )
        self.pushButton.setFont( font )
        self.pushButton.setStyleSheet( "" )
        self.pushButton.setObjectName( "pushButton" )
        self.checkBox_9 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_9.setGeometry( QtCore.QRect( 390, 190, 161, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "MS Shell Dlg 2" )
        font.setPointSize( 15 )
        self.checkBox_9.setFont( font )
        self.checkBox_9.setObjectName( "checkBox_9" )
        self.checkBox_10 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_10.setGeometry( QtCore.QRect( 370, 370, 201, 41 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.checkBox_10.setFont( font )
        self.checkBox_10.setObjectName( "checkBox_10" )
        self.checkBox_11 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_11.setGeometry( QtCore.QRect( 140, 140, 211, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 15 )
        self.checkBox_11.setFont( font )
        self.checkBox_11.setObjectName( "checkBox_11" )
        self.checkBox_12 = QtWidgets.QCheckBox( self.centralwidget )
        self.checkBox_12.setGeometry( QtCore.QRect( 390, 270, 171, 31 ) )
        font = QtGui.QFont()
        font.setPointSize( 15 )
        self.checkBox_12.setFont( font )
        self.checkBox_12.setObjectName( "checkBox_12" )
        self.pushButton_2 = QtWidgets.QPushButton( self.centralwidget )
        self.pushButton_2.setGeometry( QtCore.QRect( 750, 360, 201, 71 ) )
        font = QtGui.QFont()
        font.setPointSize( 20 )
        self.pushButton_2.setFont( font )
        self.pushButton_2.setObjectName( "pushButton_2" )
        self.pushButton.clicked.connect( self.update )
        self.pushButton_2.clicked.connect( self.rankreveal )
        ProjectMarya.setCentralWidget( self.centralwidget )
        self.statusbar = QtWidgets.QStatusBar( ProjectMarya )
        self.statusbar.setObjectName( "statusbar" )
        ProjectMarya.setStatusBar( self.statusbar )

        self.retranslateUi( ProjectMarya )
        QtCore.QMetaObject.connectSlotsByName( ProjectMarya )

    def retranslateUi(self, ProjectMarya):
        _translate = QtCore.QCoreApplication.translate
        ProjectMarya.setWindowTitle( _translate( "ProjectMarya", "ProjectX" ) )
        self.checkBox.setText( _translate( "ProjectMarya", "Wallhack" ) )
        self.checkBox_2.setText( _translate( "ProjectMarya", "NoFlash" ) )
        self.checkBox_3.setText( _translate( "ProjectMarya", "Radar" ) )
        self.checkBox_4.setText( _translate( "ProjectMarya", "FOV Changer" ) )
        self.checkBox_5.setText( _translate( "ProjectMarya", "Triggerbot" ) )
        self.checkBox_6.setText( _translate( "ProjectMarya", "Aimbot" ) )
        self.checkBox_7.setText( _translate( "ProjectMarya", "Aim for Body" ) )
        self.lineEdit_2.setText( _translate( "ProjectMarya", "e.g c" ) )
        self.lineEdit_4.setText( _translate( "ProjectMarya", "any number" ) )
        self.lineEdit.setText( _translate( "ProjectMarya", "any number" ) )
        self.label.setText( _translate( "ProjectMarya", "FOV Value" ) )
        self.checkBox_8.setText( _translate( "ProjectMarya", "Bunnyhop" ) )
        self.lineEdit_6.setText( _translate( "ProjectMarya", "e.g alt" ) )
        self.label_2.setText( _translate( "ProjectMarya", "FOV Toggle Key" ) )
        self.label_3.setText( _translate( "ProjectMarya", "Triggerbot Key" ) )
        self.label_4.setText( _translate( "ProjectMarya", "Aimbot FOV" ) )
        self.lineEdit_3.setText( _translate( "ProjectMarya", "e.g shift" ) )
        self.label_6.setText( _translate( "ProjectMarya", "Aimbot Key" ) )
        self.pushButton.setText( _translate( "ProjectMarya", "UPDATE" ) )
        self.checkBox_9.setText( _translate( "ProjectMarya", "Silentaim" ) )
        self.checkBox_10.setText( _translate( "ProjectMarya", "Recoil Control" ) )
        self.checkBox_11.setText( _translate( "ProjectMarya", "Hold To Change" ) )
        self.checkBox_12.setText( _translate( "ProjectMarya", "RCS with Aimbot" ) )
        self.pushButton_2.setText( _translate( "ProjectMarya", "Rank Reveal" ) )

    def main(self):

        pm = pymem.Pymem( "csgo.exe" )
        client = pymem.process.module_from_name( pm.process_handle, "client.dll" ).lpBaseOfDll
        engine = pymem.process.module_from_name( pm.process_handle, "engine.dll" ).lpBaseOfDll
        player = pm.read_uint( client + dwLocalPlayer )
        engine_pointer = pm.read_uint( engine + dwClientState )
        oldpunchx = 0.0
        oldpunchy = 0.0
        while True:
            try:
                if not GetWindowText(GetForegroundWindow()).decode(
                        'cp1252') == "Counter-Strike: Global Offensive - Direct3D 9":
                    time.sleep(1)
                    continue

                pm.write_uchar( engine + dwbSendPackets, 1 )
                target = None
                olddistx = 111111111111
                olddisty = 111111111111
                if client and engine and pm:
                    try:
                        player = pm.read_uint( client + dwLocalPlayer )
                        engine_pointer = pm.read_uint( engine + dwClientState )
                        glow_manager = pm.read_uint( client + dwGlowObjectManager )
                        crosshairID = pm.read_uint( player + m_iCrosshairId )
                        getcrosshairTarget = pm.read_uint( client + dwEntityList + (crosshairID - 1) * 0x10 )
                        immunitygunganme = pm.read_uint( getcrosshairTarget + m_bGunGameImmunity )
                        localTeam = pm.read_uint( player + m_iTeamNum )
                        crosshairTeam = pm.read_uint( getcrosshairTarget + m_iTeamNum )
                    except:
                        print( "Round not started yet" )
                        time.sleep( 5 )
                        continue

                for i in range( 1, 64 ):
                    entity = pm.read_uint( client + dwEntityList + i * 0x10 )

                    if entity:
                        try:
                            entity_glow = pm.read_uint( entity + m_iGlowIndex )
                            entity_team_id = pm.read_uint( entity + m_iTeamNum )
                            entity_isdefusing = pm.read_uint( entity + m_bIsDefusing )
                            entity_hp = pm.read_uint( entity + m_iHealth )
                            entity_dormant = pm.read_uint( entity + m_bDormant )
                        except:
                            print( "Could not load Players Infos (Should only do this once)" )
                            time.sleep( 2 )
                            continue

                        if entity_hp > 50 and not entity_hp == 100:
                            r, g, b = 255, 165, 0
                        elif entity_hp < 50:
                            r, g, b = 255, 0, 0
                        elif entity_hp == 100 and entity_team_id == 2:
                            r, g, b = 0, 255, 0
                        else:
                            r, g, b = 0, 255, 0

                        if self.aimc and localTeam != entity_team_id and entity_hp > 0:
                            entity_bones = pm.read_uint( entity + m_dwBoneMatrix )
                            localpos_x_angles = pm.read_float( engine_pointer + dwClientState_ViewAngles )
                            localpos_y_angles = pm.read_float( engine_pointer + dwClientState_ViewAngles + 0x4 )
                            localpos1 = pm.read_float( player + m_vecOrigin )
                            localpos2 = pm.read_float( player + m_vecOrigin + 4 )
                            localpos_z_angles = pm.read_float( player + m_vecViewOffset + 0x8 )
                            localpos3 = pm.read_float( player + m_vecOrigin + 8 ) + localpos_z_angles
                            if self.baim:
                                try:
                                    entitypos_x = pm.read_float( entity_bones + 0x30 * 5 + 0xC )
                                    entitypos_y = pm.read_float( entity_bones + 0x30 * 5 + 0x1C )
                                    entitypos_z = pm.read_float( entity_bones + 0x30 * 5 + 0x2C )
                                except:
                                    continue
                            else:
                                try:
                                    entitypos_x = pm.read_float( entity_bones + 0x30 * 8 + 0xC )
                                    entitypos_y = pm.read_float( entity_bones + 0x30 * 8 + 0x1C )
                                    entitypos_z = pm.read_float( entity_bones + 0x30 * 8 + 0x2C )
                                except:
                                    continue
                            X, Y = calcangle( localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z )
                            newdist_x, newdist_y = calc_distance( localpos_x_angles, localpos_y_angles, X, Y )
                            if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= self.aimfov and newdist_y <= self.aimfov:
                                olddistx, olddisty = newdist_x, newdist_y
                                target, target_hp, target_dormant = entity, entity_hp, entity_dormant
                                target_x, target_y, target_z = entitypos_x, entitypos_y, entitypos_z
                        if self.aimc and is_press( self.aimkey ) and player:
                            if target and target_hp > 0 and not target_dormant:
                                pitch, yaw = calcangle( localpos1, localpos2, localpos3, target_x, target_y, target_z )
                                normalize_x, normalize_y = normalizeAngles( pitch, yaw )
                                punchx = pm.read_float( player + m_aimPunchAngle )
                                punchy = pm.read_float( player + m_aimPunchAngle + 0x4 )
                                if self.silentshit:
                                    pm.write_uchar( engine + dwbSendPackets, 0 )
                                    Commands = pm.read_uint( client + dwInput + 0xF4 )
                                    VerifedCommands = pm.read_uint( client + dwInput + 0xF8 )
                                    Desired = pm.read_uint( engine_pointer + clientstate_last_outgoing_command ) + 2
                                    OldUser = Commands + ((Desired - 1) % 150) * 100
                                    VerifedOldUser = VerifedCommands + ((Desired - 1) % 150) * 0x68
                                    m_buttons = pm.read_uint( OldUser + 0x30 )
                                    Net_Channel = pm.read_uint( engine_pointer + clientstate_net_channel )
                                    if pm.read_uint( Net_Channel + 0x18 ) < Desired:
                                        pass
                                    elif self.aimrcs:
                                        pm.write_float( OldUser + 0x0C, normalize_x )
                                        pm.write_float( OldUser + 0x10, normalize_y)
                                        pm.write_int( OldUser + 0x30, m_buttons | (1 << 0) )
                                        pm.write_float( VerifedOldUser + 0x0C, normalize_x - (punchx * 2) )
                                        pm.write_float( VerifedOldUser + 0x10, normalize_y - (punchy * 2) )
                                        pm.write_int( VerifedOldUser + 0x30, m_buttons | (1 << 0) )
                                        pm.write_uchar( engine + dwbSendPackets, 1 )
                                    else:
                                        pm.write_float( OldUser + 0x0C, normalize_x )
                                        pm.write_float( OldUser + 0x10, normalize_y )
                                        pm.write_int( OldUser + 0x30, m_buttons | (1 << 0) )
                                        pm.write_float( VerifedOldUser + 0x0C, normalize_x )
                                        pm.write_float( VerifedOldUser + 0x10, normalize_y )
                                        pm.write_int( VerifedOldUser + 0x30, m_buttons | (1 << 0) )
                                        pm.write_uchar( engine + dwbSendPackets, 1 )

                                elif self.aimrcs and pm.read_uint( player + m_iShotsFired ) > 1:
                                    pm.write_float( engine_pointer + dwClientState_ViewAngles, normalize_x - (punchx * 2) )
                                    pm.write_float( engine_pointer + dwClientState_ViewAngles + 0x4,
                                                    normalize_y - (punchy * 2) )
                                else:
                                    pm.write_float( engine_pointer + dwClientState_ViewAngles, normalize_x )
                                    pm.write_float( engine_pointer + dwClientState_ViewAngles + 0x4,
                                                    normalize_y )

                        if self.radarc == True:
                            pm.write_int( entity + m_bSpotted, 1 )

                        if self.whc and entity_team_id == 2 and (
                                eteam or localTeam != 2) and not entity_dormant:

                            pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float( r ) )  # R
                            pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float( g ) )  # G
                            pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float( b ) )  # B
                            pm.write_float( glow_manager + entity_glow * 0x38 + 0x14, float( 255 ) )  # A

                            pm.write_int( glow_manager + entity_glow * 0x38 + 0x28, 1 )  # Enable


                        elif self.whc and entity_team_id == 3 and (
                                eteam or localTeam != 3) and not entity_dormant:  # Anti Glow

                            pm.write_float( glow_manager + entity_glow * 0x38 + 0x8, float( r ) )  # R
                            pm.write_float( glow_manager + entity_glow * 0x38 + 0xC, float( g ) )  # G
                            pm.write_float( glow_manager + entity_glow * 0x38 + 0x10, float( b ) )  # B
                            pm.write_float( glow_manager + entity_glow * 0x38 + 0x14, float( 255 ) )  # A

                            pm.write_int( glow_manager + entity_glow * 0x38 + 0x28, 1 )  # Enable

                        else:
                            pass


                if self.trigc and is_press(
                        self.triggerkey ) and 0 < crosshairID <= 64 and localTeam != crosshairTeam:
                    pm.write_int( client + dwForceAttack, 6 )

                if self.nf and player:
                    flash_value = player + m_flFlashMaxAlpha
                    if flash_value:
                        self.pm.write_float( flash_value, float( 0 ) )

                if self.rcse:
                    if pm.read_uint( player + m_iShotsFired ) > 2:
                        rcs_x = pm.read_float( engine_pointer + dwClientState_ViewAngles )
                        rcs_y = pm.read_float( engine_pointer + dwClientState_ViewAngles + 0x4 )
                        punchx = pm.read_float( player + m_aimPunchAngle )
                        punchy = pm.read_float( player + m_aimPunchAngle + 0x4 )
                        newrcsx = rcs_x - (punchx - oldpunchx) * 2
                        newrcsy = rcs_y - (punchy - oldpunchy) * 2
                        oldpunchx = punchx
                        oldpunchy = punchy
                        if nanchecker( newrcsx, newrcsy ) and checkangles( newrcsx, newrcsy ):
                            pm.write_float( engine_pointer + dwClientState_ViewAngles, newrcsx )
                            pm.write_float( engine_pointer + dwClientState_ViewAngles + 0x4, newrcsy )
                    else:
                        oldpunchx = 0.0
                        oldpunchy = 0.0
                        newrcsx = 0.0
                        newrcsy = 0.0


                if not self.larryfov:

                    if self.fovt and player and self.fovtog:
                        fovshit = player + m_iDefaultFOV
                        pm.write_int( fovshit, self.fovvalue )

                    if not self.fovt or not self.fovtog:
                        fovshit = player + m_iDefaultFOV
                        pm.write_int( fovshit, 90 )

                    if self.fovt and is_press( self.fovkey ):
                        self.fovtog = not self.fovtog
                        time.sleep( 0.25 )

                if self.larryfov and player:
                    fovshit = player + m_iDefaultFOV
                    if is_press( self.fovkey ):
                        self.pm.write_int( fovshit, self.fovvalue )
                    else:
                        self.pm.write_int( fovshit, 90 )

                if self.bhc:
                    if is_press( "space" ):
                        force_jump = client + dwForceJump
                        on_ground = pm.read_uint( player + m_fFlags )
                        if player and on_ground == 257 or on_ground == 263:
                            pm.write_int( force_jump, 6 )
            except:
                continue

    def rankreveal(self):
        pm = pymem.Pymem( "csgo.exe" )
        client = pymem.process.module_from_name( pm.process_handle, "client.dll" )
        engine = pymem.process.module_from_name( pm.process_handle, "engine.dll" )
        ranks = ["Unranked",
                    "Silver I",
                     "Silver II",
                     "Silver III",
                     "Silver IV",
                     "Silver Elite",
                     "Silver Elite Master",
                     "Gold Nova I",
                     "Gold Nova II",
                     "Gold Nova III",
                     "Gold Nova Master",
                     "Master Guardian I",
                     "Master Guardian II",
                     "Master Guardian Elite",
                     "Distinguished Master Guardian",
                     "Legendary Eagle",
                     "Legendary Eagle Master",
                     "Supreme Master First Class",
                     "The Global Elite"]
        for i in range( 0, 32 ):
            entity = pm.read_uint( client.lpBaseOfDll + dwEntityList + i * 0x10 )

            if entity:
                entity_team_id = pm.read_uint( entity + m_iTeamNum )
                if entity_team_id :
                    player_info = pm.read_uint(
                            (pm.read_uint( engine.lpBaseOfDll + dwClientState )) + dwClientState_PlayerInfo )
                    player_info_items = pm.read_uint( pm.read_uint( player_info + 0x40 ) + 0xC )
                    info = pm.read_uint( player_info_items + 0x28 + (i * 0x34) )
                    playerres = pm.read_uint( client.lpBaseOfDll + dwPlayerResource )
                    rank = pm.read_uint( playerres + m_iCompetitiveRanking + (i * 4 ))
                    wins = pm.read_uint(playerres + m_iCompetitiveWins + i * 4)
                    if pm.read_string( info + 0x10 ) != 'GOTV':
                        print(rank)
                        print( pm.read_string( info + 0x10 ) + "   -->   " + ranks[rank] )
                        print(wins)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication( sys.argv )
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi( Dialog )
    Dialog.show()
    threading.Thread( target=ui.main ).start()
    sys.exit( app.exec_() )


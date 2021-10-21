from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_MainWindow( object ):

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
        self. Ergb = [0,0,0]
        self.Argb = [0,0,0]
        self.Allies = False
        self.Enemies = False
        self.Healthbased = True
        self.RCS = False
        self.AimRCS = False
        self.Aimfov = int()
        self.Fovvaluke = int()
        self.Aimbotkey = str()
        self.Holdfov = False
        self.Eteam = False
        self.Chams = True

    def update(self):
        update = True
        while update:
            self.Radar = self.checkBox_3.isChecked()
            self.Wallhack = self.checkBox.isChecked()
            self.Noflash = self.checkBox_2.isChecked()
            self.Togglefov = self.checkBox_4.isChecked()
            self.Trigger = self.checkBox_5.isChecked()
            self.Aimbot = self.checkBox_6.isChecked()
            self.Baim = self.checkBox_7.isChecked()
            if self.Baim and not self.Aimbot:
                print('Activate aimbot to use the "Aim for Body function')
                self.checkBox_7.setChecked(False)

            if self.Aimbot:
                try:
                    self.Aimfov = float( self.lineEdit_4.text() )
                    self.Aimbotkey = str( self.lineEdit_6.text() )
                except:
                    print( "Use different aimbot values" )
                    self.Aimbot = False
                    self.checkBox_6.setChecked( False )
            if self.Togglefov:
                try:
                    self.Fovvaluke = int( self.lineEdit.text() )
                    self.Fovkey = str(self.lineEdit_2.text())

                except:
                    print( "Use different fov values" )
            try:
                self.Triggerkey= str(self.lineEdit_3.text())
            except:
                print("Use a different triggerkey")
            self.Bhop = self.checkBox_8.isChecked()
            self.RCS = self.checkBox_10.isChecked()
            self.Silentaim = self.checkBox_9.isChecked()
            if self.Silentaim and not self.Aimbot:
                print( "You need to activate aimbot to use silentaim" )
                self.Silentaim = False
                self.checkBox_9.setChecked( False )

            self.Holdfov = self.checkBox_11.isChecked()
            if self.Holdfov and not self.Togglefov:
                print( 'You need to activate Fov Changer to use the "Hold to change function"' )
                self.Holdfov = False
                self.checkBox_11.setChecked( False )

            self.AimRCS = self.checkBox_12.isChecked()
            self.auto_strafe = False
            update = False
        time.sleep( 1 )

        print("Update")

    def setupUi(self, ProjectMarya):
        ProjectMarya.setObjectName( "ProjectMarya" )
        ProjectMarya.resize( 960, 456 )
        font = QtGui.QFont()
        font.setFamily( "Calibri" )
        font.setPointSize( 20 )
        ProjectMarya.setFont( font )
        icon = QtGui.QIcon()
        icon.addPixmap( QtGui.QPixmap( "./pics/bgv7.png" ), QtGui.QIcon.Normal, QtGui.QIcon.Off )
        icon.addPixmap( QtGui.QPixmap( "./pics/bgv7.png" ), QtGui.QIcon.Selected, QtGui.QIcon.On )
        ProjectMarya.setWindowIcon( icon )
        ProjectMarya.setStyleSheet( "background-image:url(./pics/bgv7)" )
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
        #self.pushButton_2.clicked.connect( self.rankreveal )
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

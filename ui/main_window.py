# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_src/main_window.ui'
#
# Created: Mon Jun 30 01:33:48 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 843)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"background: #34353b;\n"
"border: none;\n"
"\n"
"")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollFrame = QtGui.QFrame(self.centralwidget)
        self.scrollFrame.setStyleSheet("#scrollFrame {\n"
"background: #4f535b;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.scrollFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.scrollFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.scrollFrame.setObjectName("scrollFrame")
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtGui.QScrollArea(self.scrollFrame)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet("#scrollArea {\n"
"background: #4f535b;\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"color: #F1F1F1;\n"
"border: 1px solid black;\n"
"background: #34353b;\n"
"min-height: 19;\n"
"}\n"
"\n"
"QFrame.sidebarFrame {\n"
"\n"
"background: #43464e;\n"
"border: 1px solid #34353b;\n"
"border-radius: 9px;\n"
"\n"
"}\n"
"\n"
"QFrame.sidebarFrame QLabel {\n"
"color: #F1F1F1;\n"
"font-weight: bold;\n"
"background: #43464e\n"
"}\n"
"\n"
"QFrame.sidebarFrame QTextEdit {\n"
"background: #34353b;\n"
"border: 1px solid black;\n"
"font-size: 8pt;\n"
"color: #F1F1F1;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QTextEdit:hover {\n"
"background: #43464e;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QPushButton {\n"
"background: #34353b;\n"
"border: 1px solid black;\n"
"color: #f1f1f1;\n"
"font-size: 8pt;\n"
"height: 23px;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QPushButton:hover {\n"
"background: #43464e;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QLineEdit {\n"
"background: #34353b;\n"
"color: #F1F1F1;\n"
"border: 1px solid black;\n"
"font-size: 8pt;\n"
"height: 21px;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QLineEdit:hover {\n"
"background: #43464e;\n"
"}\n"
"\n"
"\n"
"\n"
"QFrame.sidebarFrame QPushButton:hover {\n"
"background: #43464e;\n"
"}\n"
"QFrame.sidebarFrame QCheckBox {\n"
"background: #34353b;\n"
"border: 1px solid black;\n"
"color: #f1f1f1;\n"
"font-size: 8pt;\n"
"height: 21px;\n"
"}\n"
"\n"
"QProgressBar:horizontal {\n"
"border: 1px solid black;\n"
"background: #4f535b;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal {\n"
"background: #34353b\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 807, 805))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.scrollFrame, 0, 1, 1, 1)
        self.sidebarFrame = QtGui.QFrame(self.centralwidget)
        self.sidebarFrame.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebarFrame.sizePolicy().hasHeightForWidth())
        self.sidebarFrame.setSizePolicy(sizePolicy)
        self.sidebarFrame.setMinimumSize(QtCore.QSize(150, 0))
        self.sidebarFrame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.sidebarFrame.setAutoFillBackground(False)
        self.sidebarFrame.setStyleSheet("#sidebarFrame {\n"
"background: #4f535b;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 18px;\n"
"     height: 18px;\n"
" }\n"
"\n"
"QFrame.sidebarFrame {\n"
"\n"
"background: #43464e;\n"
"border: 1px solid #34353b;\n"
"border-radius: 9px;\n"
"\n"
"}\n"
"\n"
"QFrame.sidebarFrame QLabel {\n"
"color: #F1F1F1;\n"
"font-weight: bold;\n"
"background: #43464e\n"
"}\n"
"\n"
"QFrame.sidebarFrame QTextEdit {\n"
"background: #34353b;\n"
"border: 1px solid black;\n"
"font-size: 8pt;\n"
"color: #F1F1F1;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QTextEdit:hover {\n"
"background: #43464e;\n"
"}\n"
"\n"
"label_6 {\n"
"color: green;\n"
"font-weight: normal;\n"
"}\n"
"\n"
"\n"
"QFrame.sidebarFrame QPushButton {\n"
"background: #34353b;\n"
"border: 1px solid black;\n"
"color: #f1f1f1;\n"
"font-size: 8pt;\n"
"height: 23px;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QPushButton:hover {\n"
"background: #43464e;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QLineEdit {\n"
"background: #34353b;\n"
"color: #F1F1F1;\n"
"border: 1px solid black;\n"
"font-size: 8pt;\n"
"height: 21px;\n"
"}\n"
"\n"
"QFrame.sidebarFrame QLineEdit:hover {\n"
"background: #43464e;\n"
"}\n"
"\n"
"\n"
"\n"
"QFrame.sidebarFrame QPushButton:hover {\n"
"background: #43464e;\n"
"}\n"
"QFrame.sidebarFrame QCheckBox {\n"
"background: #34353b;\n"
"border: 1px solid black;\n"
"color: #f1f1f1;\n"
"font-size: 8pt;\n"
"height: 21px;\n"
"}\n"
"\n"
"QProgressBar:horizontal {\n"
"border: 1px solid black;\n"
"background: #4f535b;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal {\n"
"background: #34353b\n"
"}")
        self.sidebarFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.sidebarFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.sidebarFrame.setObjectName("sidebarFrame")
        self.gridLayout_3 = QtGui.QGridLayout(self.sidebarFrame)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.statusFrame = QtGui.QFrame(self.sidebarFrame)
        self.statusFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.statusFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.statusFrame.setObjectName("statusFrame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.statusFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(self.statusFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.progressBar = QtGui.QProgressBar(self.statusFrame)
        self.progressBar.setMinimum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.gridLayout_3.addWidget(self.statusFrame, 4, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.sidebarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.refBox = QtGui.QCheckBox(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refBox.sizePolicy().hasHeightForWidth())
        self.refBox.setSizePolicy(sizePolicy)
        self.refBox.setObjectName("refBox")
        self.verticalLayout_2.addWidget(self.refBox)
        self.metaBox = QtGui.QCheckBox(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metaBox.sizePolicy().hasHeightForWidth())
        self.metaBox.setSizePolicy(sizePolicy)
        self.metaBox.setChecked(False)
        self.metaBox.setObjectName("metaBox")
        self.verticalLayout_2.addWidget(self.metaBox)
        self.forceBox = QtGui.QCheckBox(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forceBox.sizePolicy().hasHeightForWidth())
        self.forceBox.setSizePolicy(sizePolicy)
        self.forceBox.setStyleSheet("")
        self.forceBox.setIconSize(QtCore.QSize(10, 10))
        self.forceBox.setChecked(False)
        self.forceBox.setObjectName("forceBox")
        self.verticalLayout_2.addWidget(self.forceBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.refreshButton = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy)
        self.refreshButton.setMinimumSize(QtCore.QSize(50, 23))
        self.refreshButton.setMaximumSize(QtCore.QSize(16777215, 23))
        self.refreshButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_4.addWidget(self.refreshButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame = QtGui.QFrame(self.sidebarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLine = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLine.sizePolicy().hasHeightForWidth())
        self.searchLine.setSizePolicy(sizePolicy)
        self.searchLine.setObjectName("searchLine")
        self.horizontalLayout.addWidget(self.searchLine)
        self.searchButton = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QtCore.QSize(50, 23))
        self.searchButton.setMaximumSize(QtCore.QSize(16777215, 23))
        self.searchButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.searchButton.setAutoDefault(False)
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.frame_4 = QtGui.QFrame(self.sidebarFrame)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtGui.QLabel(self.frame_4)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtGui.QLabel(self.frame_4)
        self.label_6.setStyleSheet("\n"
"QFrame.sidebarFrame QLabel {\n"
"\n"
"font-weight: normal;\n"
"\n"
"}\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.memberId = QtGui.QLineEdit(self.frame_4)
        self.memberId.setText("")
        self.memberId.setObjectName("memberId")
        self.verticalLayout_6.addWidget(self.memberId)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtGui.QLabel(self.frame_4)
        self.label_7.setStyleSheet("\n"
"QFrame.sidebarFrame QLabel {\n"
"\n"
"font-weight: normal;\n"
"\n"
"}\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.passHash = QtGui.QLineEdit(self.frame_4)
        self.passHash.setText("")
        self.passHash.setObjectName("passHash")
        self.verticalLayout_7.addWidget(self.passHash)
        self.gridLayout_4.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.cancelSettings = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelSettings.sizePolicy().hasHeightForWidth())
        self.cancelSettings.setSizePolicy(sizePolicy)
        self.cancelSettings.setMinimumSize(QtCore.QSize(50, 23))
        self.cancelSettings.setMaximumSize(QtCore.QSize(16777215, 23))
        self.cancelSettings.setSizeIncrement(QtCore.QSize(0, 0))
        self.cancelSettings.setObjectName("cancelSettings")
        self.horizontalLayout_7.addWidget(self.cancelSettings)
        self.submitSettings = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitSettings.sizePolicy().hasHeightForWidth())
        self.submitSettings.setSizePolicy(sizePolicy)
        self.submitSettings.setMinimumSize(QtCore.QSize(50, 23))
        self.submitSettings.setMaximumSize(QtCore.QSize(16777215, 23))
        self.submitSettings.setSizeIncrement(QtCore.QSize(0, 0))
        self.submitSettings.setObjectName("submitSettings")
        self.horizontalLayout_7.addWidget(self.submitSettings)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtGui.QLabel(self.frame_4)
        self.label_8.setStyleSheet("\n"
"QFrame.sidebarFrame QLabel {\n"
"\n"
"font-weight: normal;\n"
"\n"
"}\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.directories = QtGui.QTextEdit(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directories.sizePolicy().hasHeightForWidth())
        self.directories.setSizePolicy(sizePolicy)
        self.directories.setMaximumSize(QtCore.QSize(16777215, 75))
        self.directories.setObjectName("directories")
        self.verticalLayout_5.addWidget(self.directories)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.sidebarFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.searchLine, QtCore.SIGNAL("returnPressed()"), self.searchButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.searchLine, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.refBox)
        MainWindow.setTabOrder(self.refBox, self.metaBox)
        MainWindow.setTabOrder(self.metaBox, self.forceBox)
        MainWindow.setTabOrder(self.forceBox, self.refreshButton)
        MainWindow.setTabOrder(self.refreshButton, self.memberId)
        MainWindow.setTabOrder(self.memberId, self.passHash)
        MainWindow.setTabOrder(self.passHash, self.directories)
        MainWindow.setTabOrder(self.directories, self.cancelSettings)
        MainWindow.setTabOrder(self.cancelSettings, self.submitSettings)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SadPanda Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.statusFrame.setProperty("class", QtGui.QApplication.translate("MainWindow", "sidebarFrame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_3.setProperty("class", QtGui.QApplication.translate("MainWindow", "sidebarFrame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Gallery Options", None, QtGui.QApplication.UnicodeUTF8))
        self.refBox.setText(QtGui.QApplication.translate("MainWindow", "Search directories for galleries", None, QtGui.QApplication.UnicodeUTF8))
        self.metaBox.setText(QtGui.QApplication.translate("MainWindow", "Get metadata for new galleries", None, QtGui.QApplication.UnicodeUTF8))
        self.forceBox.setText(QtGui.QApplication.translate("MainWindow", "Reobtain all gallery information", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setProperty("class", QtGui.QApplication.translate("MainWindow", "sidebarFrame", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_4.setProperty("class", QtGui.QApplication.translate("MainWindow", "sidebarFrame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Member ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setProperty("class", QtGui.QApplication.translate("MainWindow", "smallText", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Password Hash", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setProperty("class", QtGui.QApplication.translate("MainWindow", "smallText", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelSettings.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.submitSettings.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Folders  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setProperty("class", QtGui.QApplication.translate("MainWindow", "smallText", None, QtGui.QApplication.UnicodeUTF8))
        self.directories.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

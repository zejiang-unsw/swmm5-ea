# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_.ui'
#
# Created: Fri Dec 07 16:50:13 2012
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SWMM5EA(object):
    def setupUi(self, SWMM5EA):
        SWMM5EA.setObjectName(_fromUtf8("SWMM5EA"))
        SWMM5EA.resize(825, 650)
        self.centralwidget = QtGui.QWidget(SWMM5EA)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        SWMM5EA.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(SWMM5EA)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 825, 18))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_File_2 = QtGui.QMenu(self.menuBar)
        self.menu_File_2.setObjectName(_fromUtf8("menu_File_2"))
        self.menuOptimization = QtGui.QMenu(self.menuBar)
        self.menuOptimization.setObjectName(_fromUtf8("menuOptimization"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        SWMM5EA.setMenuBar(self.menuBar)
        self.Main_toolbar = QtGui.QToolBar(SWMM5EA)
        self.Main_toolbar.setMovable(True)
        self.Main_toolbar.setFloatable(True)
        self.Main_toolbar.setObjectName(_fromUtf8("Main_toolbar"))
        SWMM5EA.addToolBar(QtCore.Qt.TopToolBarArea, self.Main_toolbar)
        self.statusbar = QtGui.QStatusBar(SWMM5EA)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SWMM5EA.setStatusBar(self.statusbar)
        self.curve_window = QtGui.QDockWidget(SWMM5EA)
        self.curve_window.setMinimumSize(QtCore.QSize(300, 300))
        self.curve_window.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.curve_window.setObjectName(_fromUtf8("curve_window"))
        self.dockWidgetContents_7 = QtGui.QWidget()
        self.dockWidgetContents_7.setObjectName(_fromUtf8("dockWidgetContents_7"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.curve_window.setWidget(self.dockWidgetContents_7)
        SWMM5EA.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.curve_window)
        self.dockWidget = QtGui.QDockWidget(SWMM5EA)
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.textEdit_tab = QtGui.QWidget()
        self.textEdit_tab.setObjectName(_fromUtf8("textEdit_tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.textEdit_tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.textEdit = QtGui.QTextEdit(self.textEdit_tab)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_4.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.textEdit_tab, _fromUtf8(""))
        self.textEdit_2_tab = QtGui.QWidget()
        self.textEdit_2_tab.setObjectName(_fromUtf8("textEdit_2_tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.textEdit_2_tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.textEdit_2 = QtGui.QTextEdit(self.textEdit_2_tab)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout_5.addWidget(self.textEdit_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.textEdit_2_tab, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        SWMM5EA.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.action_Insert_Slots = QtGui.QAction(SWMM5EA)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/spreadsheet.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Insert_Slots.setIcon(icon)
        self.action_Insert_Slots.setObjectName(_fromUtf8("action_Insert_Slots"))
        self.action_Load_SWMM_File = QtGui.QAction(SWMM5EA)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/document_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Load_SWMM_File.setIcon(icon1)
        self.action_Load_SWMM_File.setObjectName(_fromUtf8("action_Load_SWMM_File"))
        self.action_EditProject = QtGui.QAction(SWMM5EA)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_EditProject.setIcon(icon2)
        self.action_EditProject.setObjectName(_fromUtf8("action_EditProject"))
        self.actionSave_As = QtGui.QAction(SWMM5EA)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/document_save_as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon3)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.action_SaveProject = QtGui.QAction(SWMM5EA)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/document_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SaveProject.setIcon(icon4)
        self.action_SaveProject.setObjectName(_fromUtf8("action_SaveProject"))
        self.action_NewProject = QtGui.QAction(SWMM5EA)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/document_new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_NewProject.setIcon(icon5)
        self.action_NewProject.setObjectName(_fromUtf8("action_NewProject"))
        self.action_OpenProject = QtGui.QAction(SWMM5EA)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/project_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_OpenProject.setIcon(icon6)
        self.action_OpenProject.setObjectName(_fromUtf8("action_OpenProject"))
        self.actionRun_Optimization = QtGui.QAction(SWMM5EA)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/media_playback_start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_Optimization.setIcon(icon7)
        self.actionRun_Optimization.setObjectName(_fromUtf8("actionRun_Optimization"))
        self.actionPause_Optimization = QtGui.QAction(SWMM5EA)
        self.actionPause_Optimization.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/media_playback_pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause_Optimization.setIcon(icon8)
        self.actionPause_Optimization.setObjectName(_fromUtf8("actionPause_Optimization"))
        self.actionStop_Optimization = QtGui.QAction(SWMM5EA)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/player_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop_Optimization.setIcon(icon9)
        self.actionStop_Optimization.setObjectName(_fromUtf8("actionStop_Optimization"))
        self.actionHelp_About = QtGui.QAction(SWMM5EA)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/help_about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp_About.setIcon(icon10)
        self.actionHelp_About.setObjectName(_fromUtf8("actionHelp_About"))
        self.actionHelp_Users_Guide = QtGui.QAction(SWMM5EA)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/help_contents.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp_Users_Guide.setIcon(icon11)
        self.actionHelp_Users_Guide.setObjectName(_fromUtf8("actionHelp_Users_Guide"))
        self.actionInitialize_model = QtGui.QAction(SWMM5EA)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/res/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInitialize_model.setIcon(icon12)
        self.actionInitialize_model.setObjectName(_fromUtf8("actionInitialize_model"))
        self.menu_File.addAction(self.action_NewProject)
        self.menu_File.addAction(self.action_OpenProject)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_SaveProject)
        self.menu_File.addAction(self.actionSave_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_EditProject)
        self.menu_File_2.addAction(self.action_Load_SWMM_File)
        self.menu_File_2.addSeparator()
        self.menu_File_2.addAction(self.action_Insert_Slots)
        self.menuOptimization.addAction(self.actionInitialize_model)
        self.menuOptimization.addAction(self.actionRun_Optimization)
        self.menuOptimization.addAction(self.actionPause_Optimization)
        self.menuOptimization.addAction(self.actionStop_Optimization)
        self.menuHelp.addAction(self.actionHelp_Users_Guide)
        self.menuHelp.addAction(self.actionHelp_About)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_File_2.menuAction())
        self.menuBar.addAction(self.menuOptimization.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.Main_toolbar.addAction(self.action_NewProject)
        self.Main_toolbar.addAction(self.action_OpenProject)
        self.Main_toolbar.addAction(self.action_EditProject)
        self.Main_toolbar.addAction(self.action_SaveProject)
        self.Main_toolbar.addAction(self.actionSave_As)
        self.Main_toolbar.addSeparator()
        self.Main_toolbar.addAction(self.action_Load_SWMM_File)
        self.Main_toolbar.addAction(self.action_Insert_Slots)
        self.Main_toolbar.addSeparator()
        self.Main_toolbar.addAction(self.actionInitialize_model)
        self.Main_toolbar.addAction(self.actionRun_Optimization)
        self.Main_toolbar.addAction(self.actionPause_Optimization)
        self.Main_toolbar.addAction(self.actionStop_Optimization)
        self.Main_toolbar.addSeparator()
        self.Main_toolbar.addAction(self.actionHelp_Users_Guide)
        self.Main_toolbar.addAction(self.actionHelp_About)

        self.retranslateUi(SWMM5EA)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SWMM5EA)

    def retranslateUi(self, SWMM5EA):
        SWMM5EA.setWindowTitle(QtGui.QApplication.translate("SWMM5EA", "SWMM5 EA", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("SWMM5EA", "&Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File_2.setTitle(QtGui.QApplication.translate("SWMM5EA", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptimization.setTitle(QtGui.QApplication.translate("SWMM5EA", "Optimization", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("SWMM5EA", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.Main_toolbar.setWindowTitle(QtGui.QApplication.translate("SWMM5EA", "Main toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.textEdit_tab), QtGui.QApplication.translate("SWMM5EA", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.textEdit_2_tab), QtGui.QApplication.translate("SWMM5EA", "Errors and Warnings", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Insert_Slots.setText(QtGui.QApplication.translate("SWMM5EA", "&Insert Slots", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load_SWMM_File.setText(QtGui.QApplication.translate("SWMM5EA", "&Load SWMM File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_EditProject.setText(QtGui.QApplication.translate("SWMM5EA", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_EditProject.setToolTip(QtGui.QApplication.translate("SWMM5EA", "Edit Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("SWMM5EA", "Save &As", None, QtGui.QApplication.UnicodeUTF8))
        self.action_SaveProject.setText(QtGui.QApplication.translate("SWMM5EA", "&Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NewProject.setText(QtGui.QApplication.translate("SWMM5EA", "&New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenProject.setText(QtGui.QApplication.translate("SWMM5EA", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.action_OpenProject.setToolTip(QtGui.QApplication.translate("SWMM5EA", "Open a saved project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_Optimization.setText(QtGui.QApplication.translate("SWMM5EA", "Run Optimization", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_Optimization.setToolTip(QtGui.QApplication.translate("SWMM5EA", "Start optimization run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause_Optimization.setText(QtGui.QApplication.translate("SWMM5EA", "Pause Optimization", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause_Optimization.setToolTip(QtGui.QApplication.translate("SWMM5EA", "Pause at the end of this generation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop_Optimization.setText(QtGui.QApplication.translate("SWMM5EA", "Stop Optimization", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop_Optimization.setToolTip(QtGui.QApplication.translate("SWMM5EA", "Completely stop the Optimization", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp_About.setText(QtGui.QApplication.translate("SWMM5EA", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp_About.setToolTip(QtGui.QApplication.translate("SWMM5EA", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp_Users_Guide.setText(QtGui.QApplication.translate("SWMM5EA", "&Users\' Guide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp_Users_Guide.setToolTip(QtGui.QApplication.translate("SWMM5EA", "Users\' Guide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInitialize_model.setText(QtGui.QApplication.translate("SWMM5EA", "Initialize_model", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInitialize_model.setToolTip(QtGui.QApplication.translate("SWMM5EA", "Initialize the optimization", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

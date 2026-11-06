from modules.transactions import *
from modules.morelo import *
from modules.version import *
from modules.db import *

missingLibs = False
try:
	import math
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install math')
	missingLibs = True
try:
	import io
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install io')
	missingLibs = True
try:
	import time
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install time')
	missingLibs = True
try:
	import datetime
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install datetime')
	missingLibs = True
try:
	import pathlib
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install pathlib')
	missingLibs = True
try:
	import sys
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install sys')
	missingLibs = True
try:
	import json
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install json')
	missingLibs = True
try:
	import threading
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install threading')
	missingLibs = True
try:
	from subprocess import run, Popen, PIPE, DEVNULL
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install subprocess')
	missingLibs = True
try:
	import configparser
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install configparser')
	missingLibs = True
try:
	from psutil import NoSuchProcess, AccessDenied, ZombieProcess, process_iter
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install psutil')
	missingLibs = True
try:
	from time import sleep
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install time')
	missingLibs = True
try:
	from tkinter import Tk, filedialog
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install tkinter')
	missingLibs = True
try:
	from random import choice
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install random')
	missingLibs = True
try:
	import string
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install string')
	missingLibs = True
try:
	import queue
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install queue')
	missingLibs = True
try:
	import os
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install os')
	missingLibs = True
try:
	import requests
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install requests')
	missingLibs = True
try:
	import pyperclip
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install pyperclip')
	missingLibs = True
try:
	import image
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install image')
	missingLibs = True
try:
	import shutil
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install shutil')
	missingLibs = True
try:
	from PyQt5.QtWidgets import *
	from PyQt5.QtGui import *
	from PyQt5.QtCore import *
except:
	pass
	print('ERROR: Missing module, try install it by command: python -m pip install PyQt5')
	missingLibs = True
if missingLibs:
	sleep(5)
	sys.exit()
#qrCode module is optional
noQR = False
try:
	import qrcode
except:
	noQR = True
	print('INFO: QRCode module not found, running without it')
#time measurment
def TimerInit():
	return int(round(time.time() * 1000))
	
def TimerDiff(hTimer):
	return int(round(time.time() * 1000)) - hTimer

def randomString(stringLength=10):
	letters = string.ascii_lowercase
	return ''.join(choice(letters) for i in range(stringLength))
#Checking process exists
def ProcessExists(processName):
	for proc in process_iter():
		try:
			if processName.lower() in proc.name().lower():
				return True
		except (NoSuchProcess, AccessDenied, ZombieProcess):
			pass
	return False
#closing process by name
def ProcessClose(processName):
	for proc in process_iter():
		try:
			if processName.lower() in proc.name().lower():
				proc.kill()
		except (NoSuchProcess, AccessDenied, ZombieProcess):
			pass
	return False
#updating controls (widgets) style
def GUICtrlUpdateStyle(control):
	style = control.type + '''#''' + control.objectName() + ''' {
				font-size: ''' + control.myfontsize + ''';
				font-weight: ''' + control.myfontweight + ''';
				background: ''' + control.mybackgroundcolor + ''';
				color: ''' + control.mycolor + ''';
				border: ''' + control.myborder + ''';
			}
		'''
	if control.type == 'QLineEdit':
		style += control.type + '''#''' + control.objectName() + ''' {
				padding: 0px 5px 0px 5px;
			}
		'''
	if control.type == 'QPushButton':
		style += control.type + '''#''' + control.objectName() + ''':hover {
				background: ''' + control.myhoverbackgroundcolor + ''';
				color: ''' + control.myhovercolor + ''';
			}
		'''
	control.setStyleSheet(style)

initStyle = '''
	QPushButton {
		background: rgba(255, 255, 255, 15%);
		color: rgb(26, 188, 156);
		border-radius: 50%;
		font-size: 22px;
	}
	QPushButton:hover {
		background: rgba(26, 188, 156, 50%);
		color: white;
	}
'''

#modyfing controls (widgets) style attributes
def GUICtrlSetBkColor(control, color):
	control.mybackgroundcolor = color
	GUICtrlUpdateStyle(control)

def GUICtrlSetHoverBkColor(control, color):
	control.myhoverbackgroundcolor = color
	GUICtrlUpdateStyle(control)
	
def GUICtrlSetFontWeight(control, weight):
	control.myfontweight = weight
	GUICtrlUpdateStyle(control)
	
def GUICtrlSetColor(control, color):
	control.mycolor = color
	GUICtrlUpdateStyle(control)
	
def GUICtrlSetFontSize(control, size):
	control.myfontsize = size
	GUICtrlUpdateStyle(control)
#validating amount is propertly formatted
def ValidAmount(szAmount):
	szChrset = "0123456789."
	for iChr in range(0, len(szAmount), 1):
		if not szAmount[iChr] in szChrset:
			return 0
	return 1
	
def find_str(s, char):
	index = 0

	if char in s:
		c = char[0]
		for ch in s:
			if ch == c:
				if s[index:index+len(char)] == char:
					return index

			index += 1

	return -1
	
	

class Worker(QRunnable):
	def __init__(self, fn, *args, **kwargs):
		super(Worker, self).__init__()
		self.fn = fn

	@pyqtSlot()
	def run(self):
		self.fn()
		
#Main window class
class App(QWidget):
	addTx = pyqtSignal(list)
	sortTx = pyqtSignal()

	def __init__(self):
		#initial values for some variables
		super().__init__()
		self.transactions = Transactions()
		self.threadpool = QThreadPool()
		self.ctrlCount = 0
		self.walletRPC = 0
		self.xi_daemon = 0
		self.XiNetworkState, self.walletBalance, self.walletBalanceLocked = 0, 0, 0
		self.wallet_address = ''
		self.wallet_keys = {'view' : '', 'spend' : '', 'seed' : ''}
		self.exit_from_tray = False
		self.nodeSync = 0
		self.networkSync = 0
		self.lastScan = 0
		self.notQueue = queue.Queue()
		self.running = True
		self.pwd = ''
		self.scanning = False
		self.pipe = 0
		self.addTx.connect(self.AddTx)
		self.sortTx.connect(self.SortTx)
		print('INFO: Window config initialized')
		self.initUI()
		
		#Start wallet network thread
		self.net_thread = Worker(self.NetworkThread)
		self.threadpool.start(self.net_thread)

		# Request morelo price in background thread
		self.price_thread = Worker(self.PriceThread)
		self.threadpool.start(self.price_thread)

	#custom close event
	def closeEvent(self, event):
		#checking if minimize to tray instead of closing checbox is checked
		if self.hCheckboxTrayClose.isChecked() and not self.exit_from_tray:
			#if yes just hide main window and ignore close event
			self.hide()
			event.ignore()
		else:
		#if no close wallet
			#update config
			with open("Wallet.ini", "w") as configfile:
				config.write(configfile)
			#check wallet was launched in offline mode
			if not '--offline' in app.arguments():
				#send close signal to wallet's rpc
				self.morelo.wallet.stop()
				#close daemon
				self.morelo.daemon.stop()
			#destroy tray icon
			self.tray_icon.hide()
			#close background thread
			self.running = False
			event.accept()
	
	def initUI(self):
		print('INFO: Generating window controls')
		#window title and size
		self.setWindowTitle('Morelo GUI Wallet v' + version)
		self.setFixedSize(800, 470)
		self.tabsControls = {}
		
		#Image background
		background = QLabel(self)
		background.setPixmap(QPixmap("./assets/bg.png").scaledToWidth(800, Qt.SmoothTransformation))
		
		self.hLabelLogo = self.GUICtrlCreateLabel('MORELO', 0, 0, 800, 150, 0, 0, '60px')
		self.hLabelLogo.setAlignment(Qt.AlignCenter)
		self.hLabelInit = self.GUICtrlCreateLabel('Initializing...', 470, 100, 0, 0, 0, 0, '14px')
		self.hLabelInit.hide()
		#self.hLabelCopyrights = self.GUICtrlCreateLabel('All rights reserved © 2019-2023 MrKris7100', 520, 450, 0, 0, 0, 0, '12px')
		self.hLabelTip = self.GUICtrlCreateLabel('What you want to do?', 250, 320, 300, 0, 0, 0, '14px')
		self.hLabelTip.setAlignment(Qt.AlignCenter)
		self.hLabelTip.hide()
		self.hLabelInitErr = self.GUICtrlCreateLabel('Failed to start daemon', 250, 300, 300, 0, 0, '#b53b3b', '14px')
		self.hLabelInitErr.setAlignment(Qt.AlignCenter)

		#Pasword prompt controls
		self.hLabelPass = self.GUICtrlCreateLabel('This wallet is protected, enter password to unlock', 250, 220, 300, 0, 0, 0, '11px')
		self.hLabelPassSet = self.GUICtrlCreateLabel('Specify password for new wallet (can be empty)', 250, 220, 300, 0, 0, 0, '11px')
		self.hInputPass = self.GUICtrlCreateInput('', 250, 240, 230, 30)
		self.hButtonPass = self.GUICtrlCreateButton('Unlock', 485, 240, 60, 30)
		self.hButtonPassSet = self.GUICtrlCreateButton('Done', 485, 240, 60, 30)
		self.hLabelPassWrong = self.GUICtrlCreateLabel("Wrong password", 250, 270, 100, 20, 0, '#b53b3b')
		self.hLabelPass.hide()
		self.hButtonPass.hide()
		self.hInputPass.hide()
		self.hLabelPassSet.hide()
		self.hButtonPassSet.hide()
		self.hLabelPassWrong.hide()
		self.hLabelInitErr.hide()
		
		#create / open / restore wallet buttons
		self.hButtonCreate = self.GUICtrlCreateButton('', 150, 200, 100, 100)
		GUICtrlSetBkColor(self.hButtonCreate, "url('./assets/wallet_new.png')")
		GUICtrlSetHoverBkColor(self.hButtonCreate, "url('./assets/wallet_new_hover.png')")
		self.hButtonCreate.installEventFilter(self)
		self.hButtonCreate.hide()
		
		self.hButtonOpen = self.GUICtrlCreateButton('', 350, 200, 100, 100)
		GUICtrlSetBkColor(self.hButtonOpen, "url('./assets/wallet_open.png')")
		GUICtrlSetHoverBkColor(self.hButtonOpen, "url('./assets/wallet_open_hover.png')")
		self.hButtonOpen.installEventFilter(self)
		self.hButtonOpen.hide()
		
		self.hButtonRestore = self.GUICtrlCreateButton('', 550, 200, 100, 100)
		GUICtrlSetBkColor(self.hButtonRestore, "url('./assets/wallet_restore.png')")
		GUICtrlSetHoverBkColor(self.hButtonRestore, "url('./assets/wallet_restore_hover.png')")
		self.hButtonRestore.installEventFilter(self)
		self.hButtonRestore.hide()
		
		#left panel controls
		#Background rects
		self.box1 = self.GUICtrlCreateBox('rgba(255, 255, 255, 15%)', 0, 0, 200, 145)
		self.box2 = self.GUICtrlCreateBox('rgba(255, 255, 255, 15%)', 0, 325, 200, 115)
		self.box3 = self.GUICtrlCreateBox('rgba(255, 255, 255, 15%)', 0, 445, 800, 25)
		
		#Log out button
		self.hButtonLogout = self.GUICtrlCreateButton("Log Out", 725, 410, 70, 30)
		self.hButtonLogout.hide()
		
		#Balance labels
		self.hLabelGalaxia = self.GUICtrlCreateLabel("MORELO", 0, 0, 200, 60, 0, 0, '32px')
		self.hLabelGalaxia.setAlignment(Qt.AlignHCenter)
		self.hLabelBalance = self.GUICtrlCreateLabel("Balance", 25, 60, 0, 0, 0, 0, '11px', 'normal')
		self.hLabelBalanceValue = self.GUICtrlCreateLabel('0.000000', 25, 70, 175, 35, 0, 'white', '22px', 'normal')
		self.hLabelBalanceLocked = self.GUICtrlCreateLabel("Locked balance", 25, 105, 0, 0, 0, 0, '11px' , 'normal')
		self.hLabelBalanceLockedValue = self.GUICtrlCreateLabel('0.000000', 25, 115, 175, 25, 0, 'white', '18px', 'normal')
		#Network status
		self.hLabelNetwork = self.GUICtrlCreateLabel("Network status:", 5, 448, 0, 0, 'transparent', 0, '14px', 'bold')
		self.hLabelNetworkStatus = self.GUICtrlCreateLabel("Disconnected", 125, 450, 150, 0, 'transparent', '#fc7c7c', '11px', 'bold')
		self.hLabelNetworkDiff = self.GUICtrlCreateLabel("Network diff: 1000000000", 250, 450, 190, 0, 'transparent', 0, '11px', 'bold')
		self.hLabelNetworkHashrate = self.GUICtrlCreateLabel("Network hashrate: 0", 400, 450, 190, 0, 'transparent', 0, '11px', 'bold')
		self.hLabelMoreloPrice = self.GUICtrlCreateLabel("Price: Unknown", 600, 450, 190, 0, 'transparent', 0, '11px', 'bold')
		#Navigation
		self.activeTab = self.hButtonSend = self.GUICtrlCreateButton('Send', 0, 150, 200, 35, 'rgba(230, 140, 0, 50%)', 'white')
		self.hButtonReceive = self.GUICtrlCreateButton("Receive", 0, 185, 200, 35)
		self.hButtonHistory = self.GUICtrlCreateButton("Transactions", 0, 220, 200, 35)
		self.hButtonSettings = self.GUICtrlCreateButton("Settings", 0, 255, 200, 35)
		self.hButtonAbout = self.GUICtrlCreateButton("About", 0, 290, 200, 35)
		
		self.navButtons = (self.hButtonSend, self.hButtonReceive, self.hButtonHistory, self.hButtonSettings, self.hButtonAbout)
		#controls grouping
		self.tabsControls['leftpanel'] = [self.box1, self.box2, self.box3, self.hLabelGalaxia, self.hLabelBalance,
											self.hLabelBalanceValue, self.hLabelBalanceLocked, self.hLabelBalanceLockedValue,
											self.hLabelNetwork, self.hButtonSend, self.hButtonReceive,
											self.hButtonHistory, self.hButtonSettings, self.hLabelNetworkStatus, self.hButtonAbout,
											self.hLabelNetworkDiff, self.hLabelNetworkHashrate, self.hLabelMoreloPrice]
		
		#Send TAB
		self.hInputAmount = self.GUICtrlCreateInput('', 215, 30, 250, 30, 'rgba(255, 0, 0, 15%)')
		validator = QDoubleValidator()
		validator.setBottom(0.000000001)
		validator.setDecimals(9)
		locale = QLocale('English')
		locale.setNumberOptions(QLocale.RejectGroupSeparator);
		validator.setLocale(locale)
		self.hInputAmount.setValidator(validator)
		self.hInputAddress = self.GUICtrlCreateInput('', 215, 80, 250, 30, 'rgba(255, 0, 0, 15%)')
		validator = QRegExpValidator(QRegExp("[e][m][ois][1-9a-zA-Z]{95}"))
		self.hInputAddress.setValidator(validator)
		self.hInputPaymentID = self.GUICtrlCreateInput('', 215, 130, 125, 30)
		validator = QRegExpValidator(QRegExp("([0-9a-fA-F]{16}|[0-9a-fA-F]{64})"))
		self.hInputPaymentID.setValidator(validator)
		
		self.hLabelAmount = self.GUICtrlCreateLabel("Amount", 215, 15)
		self.hLabelAmountErr = self.GUICtrlCreateLabel("Please enter amount", 335, 60, 130, 20, 0, '#b53b3b')
		self.hLabelAmountErr.setAlignment(Qt.AlignRight)
		self.hLabelAddress = self.GUICtrlCreateLabel("Receiver address", 215, 65)
		self.hLabelAddressErr = self.GUICtrlCreateLabel("Please enter address", 335, 110, 130, 20, 0, '#b53b3b')
		self.hLabelAddressErr.setAlignment(Qt.AlignRight)
		self.hLabelPaymentID = self.GUICtrlCreateLabel("Payment ID (Optional)", 215, 115)
		
		self.hButtonAmountAll = self.GUICtrlCreateButton("or All", 475, 30, 50, 30)
		self.hButtonAddressPaste = self.GUICtrlCreateButton("Paste", 475, 80, 50, 30)
		self.hButtonSendSend = self.GUICtrlCreateButton("Send", 215, 170, 50, 30)
		#grouping controls
		self.tabsControls[self.hButtonSend.objectName()] = [self.hInputAmount, self.hInputAddress, self.hInputPaymentID, self.hLabelAmount, self.hLabelAmountErr,
											self.hLabelAddress, self.hLabelAddressErr, self.hLabelPaymentID, self.hButtonAmountAll, self.hButtonAddressPaste,
											self.hButtonSendSend]
											
		#Receive TAB
		self.hInputWalletAddress = self.GUICtrlCreateInput('', 215, 30, 250, 30, 'rgba(255, 255, 255, 15%)')
		self.hInputWalletAddress.setReadOnly(True)
		
		self.hLabelWalletAddress = self.GUICtrlCreateLabel("Wallet address", 215, 15)
		self.QrAddress = self.GUICtrlCreateLabel('', 215, 65, 225, 225)
		
		self.hButtonWalletCopy = self.GUICtrlCreateButton("Copy", 475, 30, 50, 30)
		#grouping controls
		self.tabsControls[self.hButtonReceive.objectName()] = [self.hInputWalletAddress, self.hLabelWalletAddress, self.hButtonWalletCopy, self.QrAddress]
		
		#Settings TAB
		
		self.hCheckboxTrayCloseBk = self.GUICtrlCreateBox('rgba(255, 255, 255, 15%)', 215, 15, 25, 25)
		self.hCheckboxTrayClose = self.GUICtrlCreateCheckBox('', 215, 15)
		self.hCheckboxTrayCloseText = self.GUICtrlCreateLabel('Hide to tray instead of closing', 245, 20, 0, 0, 0, 0, '13px')
		
		self.hCheckboxNotsBk = self.GUICtrlCreateBox('rgba(255, 255, 255, 15%)', 215, 45, 25, 25)
		self.hCheckboxNots = self.GUICtrlCreateCheckBox('', 215, 45)
		if 'wallet' in config:
			if int(config['wallet']['trayclose']):
				self.hCheckboxTrayClose.setCheckState(2)
			if int(config['wallet']['disablenotifications']):
				self.hCheckboxNots.setCheckState(2)
		self.hCheckboxNotsText = self.GUICtrlCreateLabel('Disable notifications', 245, 50, 0, 0, 0, 0, '13px')
		
		self.hLabelNode = self.GUICtrlCreateLabel('Network connection', 215, 155, 0, 0, 0, 0, '13px')
		self.hLabelSelInfo = self.GUICtrlCreateLabel('Changes requiring restart', 215, 205, 130, 20, 0, '#b53b3b')
		self.hLabelSelInfo.hide()
		
		self.hDropDownNode = self.GUICtrlCreateDropDown(self, 215, 175, 180, 30, ['Run local node', 'Use public node #1', 'Use public node #2', 'Use custom node'], self.SelectNode)
		
		self.hLabelUrl = self.GUICtrlCreateLabel('Custom node address', 450, 160)
		self.hLabelUrl.hide()
		self.hInputUrl = self.GUICtrlCreateInput('http://', 450, 175, 180, 30)
		self.hInputUrl.hide()
		
		self.hLabelUrlPort = self.GUICtrlCreateLabel('Custom node port', 450, 210)
		self.hLabelUrlPort.hide()
		self.hInputUrlPort = self.GUICtrlCreateInput('', 450, 225, 75, 30)
		self.hInputUrlPort.setValidator(QIntValidator(1, 65535))
		self.hInputUrlPort.hide()
		
		self.hLabelKeys = self.GUICtrlCreateLabel('Wallet keys and seed', 215, 75, 0, 0, '13px')
		self.hButtonKeys = self.GUICtrlCreateButton('Show', 215, 95, 50, 30)
		
		#Keys controls
		self.hInputSpend = self.GUICtrlCreateInput('', 215, 30, 250, 30)
		self.hInputSpend.setReadOnly(True)
		self.hInputView = self.GUICtrlCreateInput('', 215, 80, 250, 30)
		self.hInputView.setReadOnly(True)
		self.hInputSeed = self.GUICtrlCreateInput('', 215, 130, 250, 30)
		self.hInputSeed.setReadOnly(True)
		
		self.hLabelSpend = self.GUICtrlCreateLabel("Private spend key", 215, 15)
		self.hLabelView = self.GUICtrlCreateLabel("Private view key", 215, 65)
		self.hLabelSeed = self.GUICtrlCreateLabel("Mnemonic seed", 215, 115)
		
		self.hButtonBack = self.GUICtrlCreateButton("Back", 215, 170, 50, 30)
		self.tabsControls['keys'] = [self.hInputSpend, self.hInputView, self.hInputSeed,
		self.hLabelSpend, self.hLabelView, self.hLabelSeed, self.hButtonBack]
		for ctrl in self.tabsControls['keys']:
			ctrl.hide()
		
		
		#grouping controls
		self.tabsControls[self.hButtonSettings.objectName()] = [self.hLabelKeys, self.hButtonKeys, self.hDropDownNode, self.hCheckboxNots, self.hCheckboxNotsBk, self.hCheckboxNotsText,
		self.hCheckboxTrayClose, 
		self.hCheckboxTrayCloseBk, self.hCheckboxTrayCloseText, self.hLabelNode]
		
		#Transactions TAB
		self.hTableTransactions = QTableWidget(0, 3, self)
		self.hTableTransactions.move(215, 15)
		self.hTableTransactions.setFixedSize(570, 205)
		self.hTableTransactions.verticalHeader().hide()
		self.hTableTransactions.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.hTableTransactions.setHorizontalHeaderLabels(['Date', 'Tx hash', 'Amount'])
		self.hTableTransactions.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
		self.hTableTransactions.horizontalHeader().resizeSection(0, 160)
		self.hTableTransactions.horizontalHeader().resizeSection(1, 230)
		self.hTableTransactions.horizontalHeader().resizeSection(2, 163)
		self.tabsControls[self.hButtonHistory.objectName()] = [self.hTableTransactions]
		#About TAB
		self.hLabelAbout = self.GUICtrlCreateLabel('''Morelo GUI Wallet v''' + version + '''

Author: MrKris7100

Special thanks to njamnjam, MadHater, EMPEROR and other people from Morelo Network team.

This program is not official part of Morelo Network.
This program uses 3rd party applications: morelod and morelo-wallet-rpc from Morelo Network.

If you enjoy the program you can support me by donating some MRL using button below.''', 215, 15, 0, 0, 0, 0, '11px')
		self.hButtonDonate = self.GUICtrlCreateButton('Donate', 215, 150, 75, 30)
		
		#Init config controls
		self.hLabelNodeType = self.GUICtrlCreateLabel('Network connection type', 250, 205, 0, 0, '13px')
		self.hLabelPath = self.GUICtrlCreateLabel('Wallet working directory', 250, 150)
		self.hInputPath = self.GUICtrlCreateInput(config['wallet']['workdir'].replace('"', ''), 250, 170, 200, 30)
		self.hInputPath.setReadOnly(True)
		self.hButtonBrowse = self.GUICtrlCreateButton('Browse', 455, 170, 60, 30)
		self.hButtonOk = self.GUICtrlCreateButton('Ok', 520, 170, 30, 30)
		self.tabsControls['initconfig'] = [self.hButtonOk, self.hLabelNodeType, self.hLabelPath, self.hInputPath, self.hButtonBrowse,
		self.hDropDownNode]
		
		self.tabsControls[self.hButtonAbout.objectName()] = [self.hLabelAbout, self.hButtonDonate]
		#hiding controls
		for ctrl in self.tabsControls[self.hButtonAbout.objectName()]:
			ctrl.hide()
		for ctrl in self.tabsControls[self.hButtonReceive.objectName()]:
			ctrl.hide()
		for ctrl in self.tabsControls[self.hButtonSettings.objectName()]:
			ctrl.hide()
		for ctrl in self.tabsControls[self.hButtonHistory.objectName()]:
			ctrl.hide()
		for ctrl in self.tabsControls['initconfig']:
			ctrl.hide()
		#checking connection type in config	
		if config['wallet']['connection'] == 'local':
			self.hDropDownNode.hLabelSelection.setText('Run local node')
		elif config['wallet']['connection'] == 'ext1':
			self.hDropDownNode.hLabelSelection.setText('Use public node #1')
		elif config['wallet']['connection'] == 'ext2':
			self.hDropDownNode.hLabelSelection.setText('Use public node #2')
		elif config['wallet']['connection'] == 'custom':
			self.hDropDownNode.hLabelSelection.setText('Use custom node')
		url = config['wallet']['url'].split(':')
		self.hInputUrl.setText(url[0] + ':' + url[1])
		self.hInputUrlPort.setText(url[2])
		
		# Create tray menu
		self.tray_menu = QMenu()
		self.tray_show = QAction("Show")
		self.tray_show.triggered.connect(self.tray_event)
		self.tray_exit = QAction("Exit")
		self.tray_exit.triggered.connect(self.tray_exit_proc)
		self.tray_menu.addAction(self.tray_show)
		self.tray_menu.addAction(self.tray_exit)
		
		#Create tray icon
		self.tray_icon = QSystemTrayIcon()
		#add menu to tray
		self.tray_icon.setContextMenu(self.tray_menu)
		self.tray_icon.activated.connect(self.tray_event)
		#Set window and tray icon
		self.tray_icon.setIcon(QIcon("./morelo.ico"))
		self.setWindowIcon(QIcon("./morelo.ico"))
		
		#hiding left panel
		for ctrl in self.tabsControls['leftpanel']:
				ctrl.hide()
		for ctrl in self.tabsControls[self.hButtonSend.objectName()]:
			ctrl.hide()
		self.tray_icon.show()
		self.show()
	
	def GetWalletKeys(self):
		self.wallet_keys = self.morelo.wallet.get_keys()
		if not self.wallet_keys:
			print("ERROR: Can't read wallet keys")

	def MoreloGetPrice(self):
		try:
			response = requests.get("https://xeggex.com/api/v2/asset/getbyticker/MRL", headers={'Content-Type': 'application/json'})
			data = json.loads(response.text)
			self.morelo_price = data['usdValue']
		except:
			self.morelo_price = "Unknown"

	def PriceThread(self):
		self.MoreloGetPrice()
		self.hLabelMoreloPrice.setText("Price: " + str(self.morelo_price) + " USD")
		interval = Timer()
		while self.running:
			if interval.get() > 60000:
				interval.reset()
				self.MoreloGetPrice()
				self.hLabelMoreloPrice.setText("Price: " + str(self.morelo_price) + " USD")
			sleep(0.05)

	#detecting hover event on create / open / restore wallet buttons and modify "tooltip" with right text
	def eventFilter(self, obj, event):
		type = event.type()
		if obj.isEnabled():
			if type == 129:
				if obj == self.hButtonCreate:
					self.hLabelTip.setText('Create new wallet')
				elif obj == self.hButtonOpen:
					self.hLabelTip.setText('Open existing wallet')
				elif obj == self.hButtonRestore:
					self.hLabelTip.setText('Restore wallet from seed')
			if type == 128 and (obj == self.hButtonCreate or obj == self.hButtonOpen or obj == self.hButtonRestore):
				self.hLabelTip.setText('What you want to do?')
		return 0
	
	def tray_exit_proc(self):
		self.exit_from_tray = True
		self.close()
	
	def tray_event(self, reason):
		if reason == QSystemTrayIcon.DoubleClick or reason == QWidgetAction.Trigger:
			self.show()
			self.setWindowState(Qt.WindowNoState)
	
	def UpdateWalletAddress(self):
		self.hInputWalletAddress.setText(self.wallet_address)
	
	def UpdateQrCode(self):
		buf = io.BytesIO()
		qr = qrcode.QRCode(version=1, box_size=5, border=1)
		qr.add_data(self.wallet_address)
		qr.make(True)#self.wallet_address)
		img = qr.make_image(fill_color="black", back_color="white")
		img.save(buf, "PNG")
		qt_pixmap = QPixmap()
		qt_pixmap.loadFromData(buf.getvalue(), "PNG")
		self.QrAddress.setPixmap(qt_pixmap)

	class GUICtrlCreateDropDown():
		def __init__(self, parent, posX, posY, sizeX, sizeY, items, parser):
			super().__init__()
			
			self.expanded = False
			self.items = items
			self.sizeX = sizeX
			self.sizeY = sizeY
			
			self.hLabelSelection = parent.GUICtrlCreateLabel(str(items[0]), posX, posY, sizeX - sizeY, sizeY, 'rgba(255, 255, 255, 15%);text-align: left;padding-left: 3px', 0, '14px', 'bold')
			
			self.hButtonSelect = parent.GUICtrlCreateButton('▼', posX + sizeX - sizeY, posY, sizeY, sizeY)
			self.hButtonSelect.clicked.connect(self.toggle)
			
			for item in range(len(self.items)):
				self.items[item] = parent.GUICtrlCreateButton(str(self.items[item]), posX, posY + sizeY + (sizeY * item), sizeX, sizeY, 'rgba(255, 255, 255, 15%);text-align: left;padding-left: 7px')
				self.items[item].hide()
				self.items[item].clicked.connect(parser)
				self.items[item].clicked.connect(lambda *args, item=item: self.select(items[item].text()))
		
		def move(self, posX, posY):
			self.hLabelSelection.move(posX, posY)
			self.hButtonSelect.move(posX + self.sizeX - self.sizeY, posY)
			for item in range(len(self.items)):
				self.items[item].move(posX, posY + self.sizeY + (self.sizeY * item))
				
		
		def select(self, item):
			self.hLabelSelection.setText(item)
			self.toggle()
		
		def toggle(self):
			if self.expanded:
				for item in self.items:
					item.hide()
				GUICtrlSetBkColor(self.hButtonSelect, 'rgba(255, 255, 255, 15%)')
				GUICtrlSetColor(self.hButtonSelect, 'rgb(230, 140, 0)')
				self.hButtonSelect.setText('▼')
			else:
				for item in self.items:
					item.show()
				GUICtrlSetBkColor(self.hButtonSelect, 'rgba(230, 140, 0, 50%)')
				GUICtrlSetColor(self.hButtonSelect, 'white')
				self.hButtonSelect.setText('▲')
			self.expanded = not self.expanded
		def hide(self):
			for item in self.items:
				item.hide()
			self.hButtonSelect.hide()
			self.hLabelSelection.hide()
			self.expanded = True
			self.toggle()
			
		def show(self):
			self.hButtonSelect.show()
			self.hLabelSelection.show()
	
	#custom button creating function
	def GUICtrlCreateButton(self, text, left, top, width = 0, height = 0, background = 0, color = 0, fontsize = 0, fontweight = 0):
		button = QPushButton(text, self)
		self.ctrlCount += 1
		button.setObjectName(str(self.ctrlCount))
		if width: button.setFixedWidth(width)
		if height: button.setFixedHeight(height)
		button.move(left, top)
		button.type = 'QPushButton'
		button.myfontsize = fontsize if fontsize else '14px'
		button.myfontweight = fontweight if fontweight else 'bold'
		button.mybackgroundcolor = background if background else 'rgba(255, 255, 255, 15%)'
		button.mycolor = color if color else 'rgb(230, 140, 0)'
		button.myborder = 'none'
		button.myhoverbackgroundcolor = 'rgba(230, 140, 0, 50%)'
		button.myhovercolor = 'white'
		GUICtrlUpdateStyle(button)
		button.clicked.connect(self.button_proc)
		return button
		
	#custom checkbox creating function
	def GUICtrlCreateCheckBox(self, text, left, top):
		checkbox = QCheckBox(text, self)
		self.ctrlCount += 1
		checkbox.setObjectName(str(self.ctrlCount))
		checkbox.move(left, top)
		checkbox.type = 'QCheckBox'
		checkbox.toggled.connect(self.checkbox_proc)
		return checkbox
	
	#creating rectangles using labels
	def GUICtrlCreateBox(self, color, left, top, width, height):
		box = QLabel(self)
		box.move(left, top)
		box.setFixedSize(width, height)
		box.setStyleSheet('background-color: ' + color)
		box.setAlignment(Qt.AlignHCenter)
		box.setAlignment(Qt.AlignVCenter)
		return box
	
	#custom label creating function
	def GUICtrlCreateLabel(self, text, left, top, width = 0, height = 0, background = 0, color = 0, fontsize = 0, fontweight = 0):
		label = QLabel(text, self)
		self.ctrlCount += 1
		label.setObjectName(str(self.ctrlCount))
		if width: label.setFixedWidth(width)
		if height: label.setFixedHeight(height)
		label.move(left, top)
		label.type = 'QLabel'
		label.mywidth = str(width) if width else 'initial'
		label.myheight = str(height) if height else 'initial'
		label.myfontsize = fontsize if fontsize else '10px'
		label.myfontweight = fontweight if fontweight else 'bold'
		label.mybackgroundcolor = background if background else 'transparent'
		label.mycolor = color if color else 'rgb(230, 140, 0)'
		label.myborder = 'none'
		GUICtrlUpdateStyle(label)
		return label
	
	#custom input creating function
	def GUICtrlCreateInput(self, text, left, top, width, height, background = 0, color = 0, fontsize = 0, fontweight = 0):
		input = QLineEdit(self)
		self.ctrlCount += 1
		input.setObjectName(str(self.ctrlCount))
		input.move(left, top)
		input.type = 'QLineEdit'
		input.setFixedSize(width, height)
		# Use the actual parameter so explicitly requested input font sizes are preserved.
		input.myfontsize = fontsize if fontsize else '14px'
		input.myfontweight = fontweight if fontweight else 'bold'
		input.mybackgroundcolor = background if background else 'rgba(255, 255, 255, 15%)'
		input.mycolor = color if color else 'rgb(230, 140, 0)'
		input.myborder = 'none'
		GUICtrlUpdateStyle(input)
		input.setText(text)
		input.textChanged.connect(self.input_proc)
		input.editingFinished.connect(self.input_proc_end)
		return input
		
	#network status update function (visual)
	def NetworkState(self, state, percent = 0):
		match state:
			case 1:
				GUICtrlSetColor(self.hLabelNetworkStatus, '#f7ff91')
				self.hLabelNetworkStatus.setText("Syncing (" + '%.2f' % percent + "%)")
			case 2:
				GUICtrlSetColor(self.hLabelNetworkStatus, 'rgb(26, 188, 156)')
				self.hLabelNetworkStatus.setText("Synced")
			case 3: 
				GUICtrlSetColor(self.hLabelNetworkStatus, '#fc7c7c')
				self.hLabelNetworkStatus.setText("Disconnected")
		self.XiNetworkState = state
	
	#node type selection
	def SelectNode(self):
		obj = self.sender()
		lastSetting = config['wallet']['connection']
		if obj == self.hDropDownNode.items[0]:
			config['wallet']['connection'] = 'local'
			config['wallet']['url'] = 'http://127.0.0.1:38302'
		elif obj == self.hDropDownNode.items[1]:
			config['wallet']['connection'] = 'remote'
			config['wallet']['url'] = 'http://80.60.19.222:38302' #Sniper's public node
		elif obj == self.hDropDownNode.items[2]:
			config['wallet']['connection'] = 'remote'
			config['wallet']['url'] = 'http://'
		elif obj == self.hDropDownNode.items[3]:
			config['wallet']['connection'] = 'custom'
		if lastSetting != config['wallet']['connection']:
			if config['wallet']['connection'] == 'custom':
				for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
					ctrl.show()
			else:
				for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
					ctrl.hide()
	
	#buttons event processing function
	def button_proc(self):
		obj = self.sender()
		if obj != self.activeTab:
			#Switching TABS
			if obj in self.navButtons:
				if config['wallet']['connection'] == 'custom':
					if obj == self.hButtonSettings:
						for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
							ctrl.show()
					else:
						for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
							ctrl.hide()
				if self.activeTab == self.hButtonSettings:
					for ctrl in self.tabsControls['keys']:
						ctrl.hide()
				GUICtrlSetBkColor(self.activeTab, 'rgba(255, 255, 255, 15%)')
				GUICtrlSetColor(self.activeTab, 'rgb(230, 140, 0)')
				for ctrl in self.tabsControls[self.activeTab.objectName()]:
					ctrl.hide()
				GUICtrlSetBkColor(obj, 'rgba(230, 140, 0, 50%)')
				GUICtrlSetColor(obj, 'white')
				for ctrl in self.tabsControls[obj.objectName()]:
					ctrl.show()
				self.activeTab = obj
			else:
				#Initial config ok button
				if obj == self.hButtonOk:
					for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
							ctrl.hide()
					self.pipe = 'config'
				#Show keys button
				elif obj == self.hButtonKeys:
					for ctrl in self.tabsControls[self.hButtonSettings.objectName()]:
						ctrl.hide()
					for ctrl in self.tabsControls['keys']:
						ctrl.show()
				#Keys back button
				elif obj == self.hButtonBack:
					for ctrl in self.tabsControls[self.hButtonSettings.objectName()]:
						ctrl.show()
					for ctrl in self.tabsControls['keys']:
						ctrl.hide()
				#initial config browse button
				elif obj == self.hButtonBrowse:
					self.hDropDownNode.hButtonSelect.setEnabled(False)
					self.hButtonBrowse.setEnabled(False)
					self.hButtonOk.setEnabled(False)
					tkroot = Tk()
					tkroot.withdraw()
					file_path = filedialog.askdirectory(title='Select directory')
					tkroot.destroy()
					print(file_path)
					if file_path and pathlib.Path(file_path).exists():
						self.hInputPath.setText(file_path)
						config['wallet']['workdir'] = file_path
					self.hDropDownNode.hButtonSelect.setEnabled(True)
					self.hButtonBrowse.setEnabled(True)
					self.hButtonOk.setEnabled(True)
				#logout button
				elif obj == self.hButtonLogout:
					print("INFO: Log Out")
					for ctrl in self.tabsControls['leftpanel']:
						ctrl.hide()
					for ctrl in self.tabsControls[self.activeTab.objectName()]:
						ctrl.hide()
					self.hButtonCreate.show()
					self.hButtonOpen.show()
					self.hButtonRestore.show()
					self.hLabelTip.show()
					self.hLabelLogo.show()
					self.hButtonLogout.hide()
					self.pipe = 'logout'
					try:
						self.morelo.wallet.stop()
					except:
						pass
				#submit password (On wallet opening)
				elif obj == self.hButtonPass:
					self.hLabelInit.show()
					self.hLabelPass.hide()
					self.hInputPass.hide()
					self.hButtonPass.hide()
					self.pwd = self.hInputPass.text()
					if self.pwd == '': self.pwd = -1
					self.pipe = 'postpassword'
				elif obj == self.hButtonRestore:
					self.hButtonCreate.hide()
					self.hButtonOpen.hide()
					self.hButtonRestore.hide()
					self.hLabelTip.hide()
					self.hLabelInit.hide()
					self.hLabelMnemonic.show()
					self.hInputMnemonic.show()
					self.hButtonMnemonic.show()
				#submit password (On wallet creation)
				elif obj == self.hButtonPassSet:
					self.pwd = self.hInputPass.text()
					self.hButtonCreate.hide()
					self.hButtonOpen.hide()
					self.hButtonRestore.hide()
					self.hLabelTip.hide()
					self.pipe = 'newwallet'
				#Donate button
				elif obj == self.hButtonDonate:
					self.hInputAddress.setText(donate_address)
					self.hInputPaymentID.setText('DONATE')
					self.hButtonSend.click()
				#Wallet open button
				elif obj == self.hButtonOpen:
					self.hButtonCreate.setEnabled(False)
					self.hButtonOpen.setEnabled(False)
					self.hButtonRestore.setEnabled(False)
					tkroot = Tk()
					tkroot.withdraw()
					file_path = filedialog.askopenfilename(title='Select wallet file', filetypes=[('All files', '*')])
					tkroot.destroy()
					if pathlib.Path(file_path).is_file():
						filename = file_path.split("/").pop()
						config['wallet']['file'] = filename
						with open("Wallet.ini", "w") as configfile:
							config.write(configfile)
						shutil.copyfile(file_path, config['wallet']['workdir'] + "/" + filename)
						shutil.copyfile(file_path + ".keys", config['wallet']['workdir'] + "/" + filename + ".keys")
						self.hLabelInit.show()
						self.hButtonCreate.hide()
						self.hButtonOpen.hide()
						self.hButtonRestore.hide()
						self.hLabelTip.hide()
						self.pipe = 'walletrpc'
					self.hButtonCreate.setEnabled(True)
					self.hButtonOpen.setEnabled(True)
					self.hButtonRestore.setEnabled(True)
				#Wallet create button
				elif obj == self.hButtonCreate:
					random_container = randomString(10)
					config['wallet']['file'] = str(pathlib.Path(random_container))
					self.filename = random_container
					self.hButtonCreate.hide()
					self.hButtonOpen.hide()
					self.hButtonRestore.hide()
					self.hLabelTip.hide()
					self.hLabelInit.hide()
					self.hLabelPassSet.show()
					self.hInputPass.show()
					self.hButtonPassSet.show()
				#Amount all button
				elif obj == self.hButtonAmountAll and self.walletBalance > 0:
					self.hInputAmount.setText('%.6f' % float(self.walletBalance - 0.01))
				#Address copy button
				elif obj == self.hButtonWalletCopy:
					threading.Timer(0, self.AddressToClip).start()
				#Address paste button
				elif obj == self.hButtonAddressPaste:
					threading.Timer(0, self.AddressFromClip).start()
				#Send founds button
				elif obj== self.hButtonSendSend:
					sending = True
					if not self.hInputAddress.hasAcceptableInput() or not self.hInputAmount.hasAcceptableInput() or float(self.hInputAmount.text()) + 0.01 > self.walletBalance:
						self.controlBlink(3, 0.15)
						sending = False
					if sending:
						respond = self.morelo.wallet.transfer(self.hInputAddress.text(), float(self.hInputAmount.text()), self.hInputPaymentID.text())
						self.hInputAddress.setText('')
						self.hInputAmount.setText('')
						if 'error' in respond:
							print('Unable to send transaction (' + respond['error']['message'] + ')')
							self.tray_icon.showMessage('Unable to send transaction', respond['error']['message'], msecs=3000)
						else:
							print('Transaction sent! Tx hash (' + respond['result']['tx_hash'] + ')')
							self.tray_icon.showMessage('Transaction sent!', 'Tx hash (' + respond['result']['tx_hash'] + ')', msecs=3000)
	
	def AddressToClip(self):
		pyperclip.copy(self.wallet_address)
	
	def AddressFromClip(self):
		self.hInputAddress.setText(pyperclip.paste())
	
	#procesing data when entering data in inputs is done
	def input_proc_end(self):
		obj = self.sender()
		if obj == self.hInputAmount:
			if obj.hasAcceptableInput(): obj.setText('%.9f' % float(obj.text()))
		elif obj == self.hInputUrl or obj == self.hInputUrlPort:
			config['wallet']['url'] = self.hInputUrl.text() + ':' + self.hInputUrlPort.text()
			with open("Wallet.ini", "w") as configfile:
				config.write(configfile)
	
	#some inputs validation 
	def input_proc(self):
		obj = self.sender()
		if obj == self.hInputAmount:
			GUICtrlSetBkColor(self.hInputAmount, 'rgba(255, 0, 0, 15%)')
			if obj.hasAcceptableInput():
				if float(obj.text()) > self.walletBalance:
					self.hLabelAmountErr.setText('Not enought founds')
				else:
					self.hLabelAmountErr.setText('')
					GUICtrlSetBkColor(self.hInputAmount, 'rgba(255, 255, 255, 15%)')
			else:
				self.hLabelAmountErr.setText('Invalid amount' if obj.text() != '' else 'Please enter amount')
				
		elif obj == self.hInputAddress:
			#Checking typed address
			obj.setText(obj.text().replace(' ', ''))
			GUICtrlSetBkColor(self.hInputAddress, 'rgba(255, 0, 0, 15%)')
			if obj.hasAcceptableInput():
				self.hLabelAddressErr.setText('')
				GUICtrlSetBkColor(self.hInputAddress, 'rgba(255, 255, 255, 15%)')
			else:
				# Calling text() checks the entered value; the bound method itself is always truthy.
				self.hLabelAddressErr.setText('Invalid address' if obj.text() != '' else 'Please enter address')
				
		elif obj == self.hInputUrl:
			if obj.text() == '' or obj.text()[0:7] != 'http://':
				obj.setText('http://')
		return
	
	#checkbox clicking processing
	def checkbox_proc(self):
		obj = self.sender()
		if obj == self.hCheckboxTrayClose:
			config['wallet']['trayclose'] = str(int(obj.isChecked()))
		elif obj == self.hCheckboxNots:
			config['wallet']['disablenotifications'] = str(int(obj.isChecked()))
		#Update config file
		with open("Wallet.ini", "w") as configfile:
			config.write(configfile)
	
	#function to blink (show and hide in loop) controls
	def controlBlink(self, times = 5, delay = 0.1):
		threading.Timer(0, self.blinkProc, args=[times, delay]).start()
		
	def blinkProc(self, times, delay):
		for i in range(times):
			if not self.hInputAmount.hasAcceptableInput() or float(self.hInputAmount.text()) + 0.01 > self.walletBalance: self.hLabelAmountErr.hide()
			# Blink address feedback from the address validator, not from the amount field.
			if not self.hInputAddress.hasAcceptableInput(): self.hLabelAddressErr.hide()
			sleep(delay)
			if self.activeTab != self.hButtonSend: break
			if not self.hInputAmount.hasAcceptableInput() or float(self.hInputAmount.text()) + 0.01 > self.walletBalance: self.hLabelAmountErr.show()
			# Keep address feedback synchronized with its own validation state.
			if not self.hInputAddress.hasAcceptableInput(): self.hLabelAddressErr.show()
			sleep(delay)
	
	#Get network height from blockchain explorer
	#https://github.com/monero-project/monero/issues/1404
	#Problem with target_height in response
	def GetNetworkHeight(self):
		try:
			response = requests.get("https://explorer.morelonetwork.pl/api/networkinfo", headers={'Content-Type': 'application/json'})
			data = json.loads(response.text)
			return data['data']['height']
		except:
			return 0
	
	#network status update 
	def NetworkUpdate(self):
		if not self.running:
			return
		wallet_height = self.morelo.wallet.get_height()
		wallet_height = wallet_height['result']['height']
		nodeInfo = self.morelo.daemon.get_info()
		self.nodeSync = nodeInfo['result']['height']
		#self.networkSync = nodeInfo['result']['target_height']
		#Get network height from explorer
		self.networkSync = self.GetNetworkHeight()
		print(self.nodeSync, self.networkSync)
		diff = nodeInfo['result']['difficulty']
		self.hLabelNetworkDiff.setText("Network diff: " + str(diff))
		diff = math.floor(diff / 120)
		#hashrate formatting
		if diff < 1000:
			diff = str(diff) + " H/s"
		elif diff < 1000000:
			diff = str('%.2f' % (diff / 1000)) + " kH/s"
		elif diff < 1000000000:
			diff = str('%.2f' % (diff / 1000000)) + " MH/s"
		self.hLabelNetworkHashrate.setText("Network hashrate: " + str(diff))
		walletInfo = self.morelo.wallet.get_balance()
		#locked and unlocked balance calculations
		if walletInfo:
			self.walletBalance = walletInfo['result']['unlocked_balance'] / 1000000000
			self.walletBalanceLocked = (walletInfo['result']['balance'] / 1000000000) - self.walletBalance
			if self.walletBalanceLocked < 0:
				self.walletBalanceLocked *= -1
		if wallet_height < self.networkSync:
			self.NetworkState(1, wallet_height / self.networkSync * 100)
		else:
			if self.XiNetworkState != 2:
				self.NetworkState(2)
				print('INFO: Network synced')
	
    #Background thread
	def NetworkThread(self):
		#Initial config
		if not pathlib.Path("Wallet.ini").is_file():
			print('INFO: No wallet config, initial setup')
			for ctrl in self.tabsControls['initconfig']:
				ctrl.show()
			self.hDropDownNode.move(250, 220)
			self.hLabelUrl.move(450, 205)
			self.hInputUrl.move(450, 220)
			self.hLabelUrlPort.move(450, 255)
			self.hInputUrlPort.move(450, 270)
			while self.running:
				if self.pipe == 'config':
					break
			self.hDropDownNode.move(215, 175)
			self.hLabelUrl.move(450, 160)
			self.hInputUrl.move(450, 175)
			self.hLabelUrlPort.move(450, 210)
			self.hInputUrlPort.move(450, 225)
			for ctrl in self.tabsControls[self.hButtonSettings.objectName()]:
				ctrl.hide()
			for ctrl in self.tabsControls['initconfig']:
				ctrl.hide()
			newwallet = True
			with open("Wallet.ini", "w") as configfile:
				config.write(configfile)
			print('INFO: Config saved')
		#reading config file
		config.read("Wallet.ini")
		self.hLabelInit.show()
		if '--offline' in app.arguments():
			print('INFO: Running wallet in offline mode')
			self.runOffline()
		else:
			daemon = False
			local = True if config["wallet"]["connection"] == "local" else False
				
			#Initializing morelo daemon and wallet RPC
			self.morelo = Morelo(config['wallet']['workdir'], d_url = config['wallet']['url'], local=local)
			
			#Check connection with external node if is choosen
			if config['wallet']['connection'] != 'local':
				print('INFO: Connecting to', config['wallet']['url'] + '...')
				if self.morelo.daemon.wait():
					daemon = True
				else:
					print('ERROR: Unable connect to external node, using local instead')
					self.morelo = Morelo(config['wallet']['workdir'], d_url = "http://127.0.0.1:38301", local=True)
                    
			#Waiting for connection to daemon
			if not daemon:
				print('INFO: Connecting to local node...')
				if self.morelo.daemon.wait():
					daemon = True
				else:
					print('ERROR: Unable connect to local node')

            #Waiting for wallet RPC
			self.morelo.wallet.wait();
			#Closing wallet if something was fucking wrong with connection
			if not daemon:
				print('ERROR: No connection to daemon, closing wallet...')
				sleep(2.5)
				self.close()
				return
			#checking wallet in config exists or is not configured
			if not pathlib.Path(config['wallet']['workdir'] + '/' + config['wallet']['file']).is_file():
                #if no show open / create / restore wallet buttons
				print('ERROR: Wallet file not found')
				self.hButtonCreate.show()
				self.hButtonOpen.show()
				self.hButtonRestore.show()
				self.hLabelTip.show()
				self.hLabelInit.hide()
			else:
				#if yes we going further
				print('INFO: Loading wallet file', config['wallet']['workdir'] + '/' + config['wallet']['file'])
				self.pipe = 'walletrpc'
			#magic here
			#\/ this loop for logout and re logging feature
			while self.running:
				#\/ this loop waiting for user choice if any wallet doesnt exist or we logout
				while self.running:
					#we going to run wallet rpc
					if self.pipe == 'walletrpc':
						break
					#user wants to make new wallet
					elif self.pipe == 'newwallet':
						self.hLabelInit.show()
						#Generate new wallet
						self.hLabelPassSet.hide()
						self.hInputPass.hide()
						self.hButtonPassSet.hide()
						while self.running:
							respond = self.morelo.wallet.create(config['wallet']['file'], self.hInputPass.text())
							print(respond)
							if 'result' in respond:
								break
						#update wallet config
						with open("Wallet.ini", "w") as configfile:
							config.write(configfile)
						break
					else:
						sleep(0.05)
				#next magic loop
				while self.running:
					result = self.WaitForWalletRPC()
					#password is good or wallet doesnt have password
					if result == 'ok':
						self.pipe = False
						break
					#wallet have password
					elif result == 'requirepassword':
						self.hLabelInit.hide()
						self.hLabelPass.show()
						self.hInputPass.show()
						self.hButtonPass.show()
						self.pipe = False
						while self.pipe != 'postpassword':
							sleep(0.05)
					#user enter wrong password
					elif result == 'wrongpassword':
						print('ERROR: Wrong password')
						self.hLabelPassWrong.show()
						self.hInputPass.show()
						self.hButtonPass.show()
						self.hLabelInit.hide()
						self.pipe = False
						while self.pipe != 'postpassword':
							sleep(0.05)
					sleep(0.05)
				if(self.pwd) == "":
					print('INFO: Wallet started (No password)')
				else:
					print('INFO: Wallet started (Password is correct)')
				#i dont remember why this shit exist here but leave that
				self.wallet_address = self.morelo.wallet.get_address()
				print('INFO: Wallet address:', self.wallet_address)
				self.UpdateWalletAddress()
				self.UpdateBalance()
				self.NetworkUpdate()
				#hide some controls and show other
				self.hLabelInit.hide()
				self.hLabelLogo.hide()
				self.hButtonCreate.hide()
				self.hButtonOpen.hide()
				self.hButtonRestore.hide()
				self.hLabelTip.hide()
				self.hButtonLogout.show()
				for ctrl in self.tabsControls['leftpanel']:
					ctrl.show()
				for ctrl in self.tabsControls[self.hButtonSend.objectName()]:
					ctrl.show()
				if not noQR:
					#generate QrCode for our wallet address
					self.UpdateQrCode()
				#main networking and notifications loop
				updateInterval = Timer()
				while self.running and self.pipe != 'logout':
					try:
						item = self.notQueue.get(False)
						if not int(config['wallet']['disablenotifications']): self.tray_icon.showMessage('New transaction', item[0] + '\nNew transaction found\nTx hash (' + item[1] + ')\nAmount: ' + item[2], msecs=2500)
					except:
						pass
					if updateInterval.get() > 2500:
						self.NetworkUpdate()
						self.UpdateBalance()
						self.UpdateTransactions()
						updateInterval.reset()
					sleep(0.05)
				#finally the end of this fucking loops magic

	#running wallet rpc and waiting for his respond
	def WaitForWalletRPC(self):
		#opening wallet using RPC
		response = self.morelo.wallet.open(config['wallet']['file'], self.hInputPass.text())
		walletRPC = False
		#waiting for respond or crash
		if 'result' in response:
			walletRPC = True
			return 'ok'
		if 'error' in response:
			if response['code'] == -1:
				return 'retry'
			if self.pwd == '':
				return 'requirepassword'
			else:
				return 'wrongpassword'
		else:
			return 'ok'

	#running wallet in offline mode, it's not offline in meaning of without networking but only for GUI debbuging
	#i will delete that later on stable releases
	def runOffline(self):
		for ctrl in self.tabsControls['leftpanel']:
			ctrl.show()
		for ctrl in self.tabsControls[self.hButtonSend.objectName()]:
			ctrl.show()
		self.UpdateWalletAddress()
		self.walletBalance = 1.234
		self.UpdateBalance()
		if not noQR: self.UpdateQrCode()
		self.hLabelInit.hide()
		self.hLabelLogo.hide()
		date = datetime.datetime.fromtimestamp(1576705196)
		self.addTx.emit([str(date), '4437459bac024c7ce3fc0ecf63ef482466fd19141f46709c1cd640aeb6c20e27', str(1.234000)])
	
	def hideWindow(self):
		self.hide()
	
	#add transaction to table
	def AddTx(self, data):
		self.hTableTransactions.insertRow(0)
		for i in range(3):
			item = QTableWidgetItem(data[i])
			item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled )
			self.hTableTransactions.setItem(0, i, item)
	
	#sort table
	def SortTx(self):
		self.hTableTransactions.sortItems(0, Qt.DescendingOrder)
	
	#read transactions from wallet then add them to table, scan and add incoming transactions to table
	def UpdateTransactions(self):
		print('INFO: checking for transactions')
		if not self.running or not self.networkSync or self.networkSync <= 1 or self.scanning or self.lastScan >= self.networkSync:
			return
		self.scanning = True
		# Scan bounded, non-overlapping height ranges and advance the cursor only after success.
		scan_start = max(1, self.lastScan)
		scan_count = min(10000, self.networkSync - scan_start + 1)
		full_scan = self.lastScan < 1
		try:
			if full_scan:
				print('INFO: Full tx list request')
			else:
				print('INFO: Partial tx list request, blocks from', scan_start, 'to', scan_start + scan_count - 1)
			transactions = self.morelo.wallet.get_transfers(scan_start, scan_count)
			for transaction in transactions:
				# Prevent duplicate table entries and notifications when a range is retried.
				if self.transactions.get(transaction):
					continue
				tx_info = self.morelo.wallet.get_transfer(transaction)
				transfer = tx_info['result']['transfer']
				self.transactions.add(tx_info)
				date = datetime.datetime.fromtimestamp(int(transfer['timestamp']))
				amount = transfer['amount'] / 1000000000
				if transfer['type'] == 'out':
					amount *= -1
				self.addTx.emit([str(date), transaction, '%.6f' % amount])
				if not full_scan and transfer['type'] == 'in':
					print('New transaction found! Amount:' + str(amount) + ' (' + transaction + ')')
					self.IncomingTx(transaction, str(amount), str(date))
			self.lastScan = scan_start + scan_count
			print('INFO: ', len(transactions), 'transactions added to table')
		except (KeyError, TypeError, ValueError, requests.RequestException) as error:
			# Keep the cursor unchanged after an RPC failure so the missing range is retried.
			print("ERROR: Can't update transaction history:", error)
		finally:
			self.scanning = False
	
	def IncomingTx(self, hash, amount, time):
		self.notQueue.put([time, hash, amount])
	
	def UpdateBalance(self):
		self.hLabelBalanceValue.setText('%.6f' % self.walletBalance)
		self.hLabelBalanceLockedValue.setText('%.6f' % self.walletBalanceLocked)
		
	def UpdateKeys(self):
		self.hInputSpend.setText(self.wallet_keys['spend'])
		self.hInputView.setText(self.wallet_keys['view'])
		self.hInputSeed.setText(self.wallet_keys['seed'])

style = '''
			QHeaderView::section {
				background-color: rgba(230, 140, 0, 50%);
				color: white;
				padding-left: 4px;
				border: 1px solid rgb(230, 140, 0);
				font-weight: bold;
			}
			QHeaderView {
				background: transparent;
			}
			QHeaderView::section:checked
			{
				background-color: rgba(230, 140, 0, 50%);
				color: white;
				padding-left: 4px;
				border: 1px solid rgb(230, 140, 0);
			}
			QTableWidget {
				gridline-color: rgb(230, 140, 0);
				background-color: rgba(255, 255, 255, 15%);
				border: 1px solid rgb(230, 140, 0);
				color: rgb(230, 140, 0);
			}
			QTableWidget::item {
				border-left: 1px solid rgb(230, 140, 0);
				background: transparent;
			}	
			QTableWidget::item:focus {
				border-left: 1px solid rgb(230, 140, 0);
				background: transparent;
				color: rgb(230, 140, 0);
			}	
			QTableWidget::item:selected {
				border-left: 1px solid rgb(230, 140, 0);
				background: transparent;
				color: rgb(230, 140, 0);
			}	
			QCheckBox {
				background-color: transparent;
				color: rgb(230, 140, 0);
				width: 25px;
				height: 25px;
				font-size: 12px;
			}
			QCheckBox::indicator {
				width: 25px;
				height: 25px;
				background-color: transparent;
			}
			QCheckBox::indicator:checked {
				margin: 7.5px 7.5px 7.5px 7.5px;
				width: 10px;
				height: 10px;
				background-color: rgb(230, 140, 0);
			}
			QCheckBox::indicator:unchecked {
				width: 25px;
				height: 25px;
			}
			QScrollBar:vertical {
				border: none;
				background: transparent;
				width: 15px;
				margin: 22px 0 22px 0;
			}
			QScrollBar::handle:vertical {
				border-top: 1px solid rgb(230, 140, 0);
				border-bottom: 1px solid rgb(230, 140, 0);
				background: rgba(230, 140, 0, 50%);
				min-height: 20px;
			}
			QScrollBar::add-line:vertical {
				border: 1px solid rgb(230, 140, 0);
				background: rgba(230, 140, 0, 50%);
				height: 20px;
				subcontrol-position: bottom;
				subcontrol-origin: margin;
			}

			QScrollBar::sub-line:vertical {
				border: 1px solid rgb(230, 140, 0);
				background: rgba(230, 140, 0, 50%);
				height: 20px;
				subcontrol-position: top;
				subcontrol-origin: margin;
			}
			QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
				border: 2px solid rgb(230, 140, 0);
				width: 3px;
				height: 3px;
				background: white;
			}

			QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
				background: none;
			}
		'''

if __name__ == '__main__':
	donate_address = 'emo1MrKriSGc5AfEyUaEMMExVkKpPbNXSiUcNdNWX4W8KK5NH8E9zMiBi35QJii89SYwZmSyNBdWUYmGFJvphYUM4qRL5E33bq'
	config = configparser.ConfigParser()
	config['wallet'] = {'workdir' : str(pathlib.Path(str(pathlib.Path.home()) + '/morelo')), 'file' : '', 'url' : 'http://127.0.0.1:38302', 'connection' : 'local', 'trayclose' : 0, 'disablenotifications' : 0}
	if not '--offline' in sys.argv:
		#check morelo binaries exists
		pathwalletRPC = 'morelo-wallet-rpc.exe' if os.name == 'nt' else 'morelo-wallet-rpc'
		pathDaemon = 'morelod.exe' if os.name == 'nt' else 'morelod'
		if not pathlib.Path(pathwalletRPC).is_file() or not pathlib.Path(pathDaemon).is_file():
			print('ERROR: morelo binaries not found! Make sure to have "morelod" and "morelo-wallet-rpc" files in wallet folder')
			sleep(5)
			sys.exit()
	app = QApplication(sys.argv)
	app.setStyleSheet(style)
	print('INFO: Running main window')
	ex = App()
	#GUI main thread
	sys.exit(app.exec_())

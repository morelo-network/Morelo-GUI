missingLibs = False
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
	from subprocess import run, Popen, PIPE, CREATE_NO_WINDOW, CREATE_NEW_CONSOLE
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
noQR = False
try:
	import qrcode
except:
	noQR = True
	print('INFO: QRCode module not found, running without it')

def TimerInit():
	return int(round(time.time() * 1000))
	
def TimerDiff(hTimer):
	return int(round(time.time() * 1000)) - hTimer

def randomString(stringLength=10):
	letters = string.ascii_lowercase
	return ''.join(choice(letters) for i in range(stringLength))

def ProcessExists(processName):
	for proc in process_iter():
		try:
			if processName.lower() in proc.name().lower():
				return True
		except (NoSuchProcess, AccessDenied, ZombieProcess):
			pass
	return False
	
def ProcessClose(processName):
	for proc in process_iter():
		try:
			if processName.lower() in proc.name().lower():
				proc.kill()
		except (NoSuchProcess, AccessDenied, ZombieProcess):
			pass
	return False

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
		background: rgba(255, 255, 255, 10%);
		color: rgb(26, 188, 156);
		border-radius: 50%;
		font-size: 22px;
	}
	QPushButton:hover {
		background: rgba(26, 188, 156, 50%);
		color: white;
	}
'''

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

def SendTransaction(receiver, amount, pay_id):
	response = requests.post('http://127.0.0.1:38070/json_rpc', data='{"jsonrpc":"2.0","method":"sendTransaction","password":"","params":{"transfers":[{"address":"' + receiver + '","amount":' + str(int(amount * 1000000)) + '}],"fee":10000}}', headers={'Content-Type':'application/json'})
	return json.loads(response.text)
   
def GetWalletBalance():
	response = requests.post('http://127.0.0.1:38070/json_rpc', data='{"method" : "getBalance", "password":"", "params" : {}, "id" : "", "jsonrpc" : "2.0"}', headers={'Content-Type':'application/json'})
	return json.loads(response.text)
   
def GetWalletAddress():
	response = False
	try:
		response = requests.post('http://127.0.0.1:38070/json_rpc', data='{"method" : "getAddresses", "password":"","params" : {}, "id" : "", "jsonrpc" : "2.0"}', headers={'Content-Type':'application/json'})
		response = json.loads(response.text)
	except:
		sleep(0.1)
	return response

def GetWalletTransactions(start, count):
	transactions = []
	response = requests.post('http://127.0.0.1:38070/json_rpc', data='{"jsonrpc":"2.0","id":null,"method":"getTransactionHashes","password":"","params":{"first_block_height":' + str(start) + ',"block_count":' + str(count) +',"block_hash":""}}', headers={'Content-Type':'application/json'})
	data = json.loads(response.text)
	if 'error' not in data:
		for block in data['result']['items']:
			for hash in block['transaction_hashes']:
				transactions.append(hash)
	else:
		print("ERROR: Can't get transaction list")
	return transactions
	
def GetTransactionInfo(hash):
	response = requests.post('http://127.0.0.1:38070/json_rpc',data='{"jsonrpc":"2.0","method":"getTransaction","password":"","params":{"transaction_hash":"' + hash + '"}}',headers={'Content-Type':'application/json'})
	return json.loads(response.text)

class App(QWidget):
	addTx = pyqtSignal(str, str, str)

	def __init__(self):
		super().__init__()
		self.title = 'Galaxia GUI Wallet'
		self.width = 800
		self.height = 470
		self.ctrlCount = 0
		self.timer = 0
		self.notifications = 0
		self.pgservice = 0
		self.xi_daemon = 0
		self.XiNetworkState, self.walletBalance, self.walletBalanceLocked = 0, 0, 0
		self.wallet_address = 'gxi123'
		self.exit_from_tray = False
		self.valid_amount = False
		self.valid_address = False
		self.nodeSync = 0
		self.networkSync = 0
		self.lastScan = 0
		self.notQueue = queue.Queue()
		self.pg_initialized = False
		self.running = True
		self.pwd = ''
		self.scanning = False
		self.netSelect = False
		self.netChanged = False
		self.pipe = 0
		self.addTx.connect(self.AddTx)
		print('INFO: Window config initialized')
		self.initUI()
		
	def closeEvent(self, event):
		#Tray close
		if self.hCheckboxTrayClose.isChecked() and not self.exit_from_tray:
			self.hide()
			event.ignore()
		else:
			if not '--offline' in app.arguments():
				try:
					requests.post('http://127.0.0.1:38070/json_rpc', data='{"method" : "shutdown", "params" : {}, "id" : "", "jsonrpc" : "2.0"}', headers={'Content-Type':'application/json'})
				except:
					pass
				if self.xi_daemon: self.xi_daemon.terminate()
			if self.timer: self.timer.cancel()
			if self.notifications: self.notifications = False
			self.tray_icon.hide()
			self.running = False
			event.accept()
	
	def initUI(self):
		print('INFO: Generating window controls')
		self.setWindowTitle(self.title)
		self.setFixedSize(self.width, self.height)
		self.tabsControls = {}

		self.hShow = self.GUICtrlCreateButton('', 0, 0)
		self.hOffline = self.GUICtrlCreateButton('', 0, 0)
		
		#Image background
		background = QLabel(self)
		background.setPixmap(QPixmap("./assets/bg.png"))
		
		self.hLabelLogo = self.GUICtrlCreateLabel('GALAXIA', 0, 0, 800, 150, 0, 0, '60px')
		self.hLabelLogo.setAlignment(Qt.AlignCenter)
		self.hLabelInit = self.GUICtrlCreateLabel('initializing...', 470, 100, 0, 0, 0, 0, '14px')
		self.hLabelCopyrights = self.GUICtrlCreateLabel('All rights reserved © 2019 MrKris7100', 550, 450, 0, 0, 0, 0, '12px')
		self.hLabelTip = self.GUICtrlCreateLabel('What you want to do?', 250, 320, 300, 0, 0, 0, '14px')
		self.hLabelTip.setAlignment(Qt.AlignCenter)
		self.hLabelTip.hide()
		self.hLabelInitErr = self.GUICtrlCreateLabel('Failed to start daemon', 250, 300, 300, 0, 0, '#b53b3b', '14px')
		self.hLabelInitErr.setAlignment(Qt.AlignCenter)
		
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
		
		self.hButtonCreate = self.GUICtrlCreateButton('', 250, 200, 100, 100)
		GUICtrlSetBkColor(self.hButtonCreate, "url('./assets/wallet_new.png')")
		GUICtrlSetHoverBkColor(self.hButtonCreate, "url('./assets/wallet_new_hover.png')")
		self.hButtonCreate.installEventFilter(self)
		self.hButtonCreate.hide()
		
		self.hButtonOpen = self.GUICtrlCreateButton('', 450, 200, 100, 100)
		GUICtrlSetBkColor(self.hButtonOpen, "url('./assets/wallet_open.png')")
		GUICtrlSetHoverBkColor(self.hButtonOpen, "url('./assets/wallet_open_hover.png')")
		self.hButtonOpen.installEventFilter(self)
		self.hButtonOpen.hide()
		
		'''
		Left Panel controls
		'''
		#Background rects
		self.box1 = self.GUICtrlCreateBox('rgba(255, 255, 255, 10%)', 0, 0, 200, 145)
		self.box2 = self.GUICtrlCreateBox('rgba(255, 255, 255, 10%)', 0, 325, 200, 80)
		self.box3 = self.GUICtrlCreateBox('rgba(255, 255, 255, 10%)', 0, 410, 200, 60)
		
		#Balance labels
		self.hLabelGalaxia = self.GUICtrlCreateLabel("GALAXIA", 0, 0, 200, 60, 0, 0, '32px')
		self.hLabelGalaxia.setAlignment(Qt.AlignHCenter)
		self.hLabelBalance = self.GUICtrlCreateLabel("Balance", 25, 60, 0, 0, 0, 0, '11px', 'normal')
		self.hLabelBalanceValue = self.GUICtrlCreateLabel('0.000000', 25, 70, 175, 35, 0, 'white', '22px', 'normal')
		self.hLabelBalanceLocked = self.GUICtrlCreateLabel("Locked balance", 25, 105, 0, 0, 0, 0, '11px' , 'normal')
		self.hLabelBalanceLockedValue = self.GUICtrlCreateLabel('0.000000', 25, 115, 175, 25, 0, 'white', '18px', 'normal')
		#Network status
		self.hLogoGreen = QPixmap('./assets/logo_green.png').scaledToWidth(50, Qt.SmoothTransformation)
		self.hLogoRed = QPixmap('./assets/logo_red.png').scaledToWidth(50, Qt.SmoothTransformation)
		self.hLogoYellow = QPixmap('./assets/logo_yellow.png').scaledToWidth(50, Qt.SmoothTransformation)
		self.hLabelNetworkIcon = self.GUICtrlCreateLabel('', 5, 415, 50, 50)
		self.hLabelNetworkIcon.setPixmap(self.hLogoRed)
		self.hLabelNetwork = self.GUICtrlCreateLabel("Network status", 60, 425, 0, 0, 'transparent', 0, '14px', 'bold')
		self.hLabelNetworkStatus = self.GUICtrlCreateLabel("Disconnected", 60, 435, 145, 30, 'transparent', '#fc7c7c', '11px', 'bold')
		#Nav
		self.activeTab = self.hButtonSend = self.GUICtrlCreateButton('Send', 0, 150, 200, 35, 'rgba(26, 188, 156, 50%)', 'white')
		self.hButtonReceive = self.GUICtrlCreateButton("Receive", 0, 185, 200, 35)
		self.hButtonHistory = self.GUICtrlCreateButton("Transactions", 0, 220, 200, 35)
		self.hButtonSettings = self.GUICtrlCreateButton("Settings", 0, 255, 200, 35)
		self.hButtonAbout = self.GUICtrlCreateButton("About", 0, 290, 200, 35)
		
		self.navButtons = (self.hButtonSend, self.hButtonReceive, self.hButtonHistory, self.hButtonSettings, self.hButtonAbout)
		
		self.tabsControls['leftpanel'] = [self.box1, self.box2, self.box3, self.hLabelGalaxia, self.hLabelBalance,
											self.hLabelBalanceValue, self.hLabelBalanceLocked, self.hLabelBalanceLockedValue,
											self.hLabelNetworkIcon, self.hLabelNetwork, self.hButtonSend, self.hButtonReceive,
											self.hButtonHistory, self.hButtonSettings, self.hLabelNetworkStatus, self.hButtonAbout]
		
		#Send TAB
		self.hInputAmount = self.GUICtrlCreateInput('', 215, 30, 250, 30, 'rgba(255, 0, 0, 15%)')
		validator = QDoubleValidator()
		validator.setBottom(0.000001)
		validator.setDecimals(6)
		locale = QLocale('Enblish')
		locale.setNumberOptions(QLocale.RejectGroupSeparator);
		validator.setLocale(locale)
		self.hInputAmount.setValidator(validator)
		self.hInputAddress = self.GUICtrlCreateInput('', 215, 80, 250, 30, 'rgba(255, 0, 0, 15%)')
		self.hInputPaymentID = self.GUICtrlCreateInput('', 215, 130, 125, 30)
		
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
		
		self.tabsControls[self.hButtonSend.objectName()] = [self.hInputAmount, self.hInputAddress, self.hInputPaymentID, self.hLabelAmount, self.hLabelAmountErr,
											self.hLabelAddress, self.hLabelAddressErr, self.hLabelPaymentID, self.hButtonAmountAll, self.hButtonAddressPaste,
											self.hButtonSendSend]
											
		#Receive TAB
		self.hInputWalletAddress = self.GUICtrlCreateInput('', 215, 30, 250, 30, 'rgba(255, 255, 255, 10%)')
		self.hInputWalletAddress.setReadOnly(True)
		
		self.hLabelWalletAddress = self.GUICtrlCreateLabel("Wallet address", 215, 15)
		self.QrAddress = self.GUICtrlCreateLabel('', 215, 65, 225, 225)
		
		self.hButtonWalletCopy = self.GUICtrlCreateButton("Copy", 475, 30, 50, 30)
		
		self.tabsControls[self.hButtonReceive.objectName()] = [self.hInputWalletAddress, self.hLabelWalletAddress, self.hButtonWalletCopy, self.QrAddress]
		
		#Settings TAB
		self.hCheckboxStartupBk = self.GUICtrlCreateBox('rgba(255, 255, 255, 10%)', 215, 15, 25, 25)
		self.hCheckboxStartup = self.GUICtrlCreateCheckBox('', 215, 15)
		if int(config['wallet']['autostart']):
			self.hCheckboxStartup.setCheckState(2)
		self.hCheckboxText = self.GUICtrlCreateLabel('Run at windows startup', 245, 20, 0, 0, 0, 0, '13px')
		
		self.hCheckboxTrayCloseBk = self.GUICtrlCreateBox('rgba(255, 255, 255, 10%)', 215, 45, 25, 25)
		self.hCheckboxTrayClose = self.GUICtrlCreateCheckBox('', 215, 45)
		if int(config['wallet']['trayclose']):
			self.hCheckboxTrayClose.setCheckState(2)
		self.hCheckboxTrayCloseText = self.GUICtrlCreateLabel('Hide to tray instead of closing', 245, 50, 0, 0, 0, 0, '13px')
		
		self.hCheckboxAutoHideBk = self.GUICtrlCreateBox('rgba(255, 255, 255, 10%)', 215, 75, 25, 25)
		self.hCheckboxAutoHide = self.GUICtrlCreateCheckBox('', 215, 75)
		if int(config['wallet']['autohide']):
			self.hCheckboxAutoHide.setCheckState(2)
		self.hCheckboxAutoHideText = self.GUICtrlCreateLabel('Hide to tray on startup', 245, 80, 0, 0, 0, 0, '13px')
		
		self.hCheckboxNotsBk = self.GUICtrlCreateBox('rgba(255, 255, 255, 10%)', 215, 105, 25, 25)
		self.hCheckboxNots = self.GUICtrlCreateCheckBox('', 215, 105)
		if int(config['wallet']['disablenotifications']):
			self.hCheckboxNots.setCheckState(2)
		self.hCheckboxNotsText = self.GUICtrlCreateLabel('Disable notifications', 245, 110, 0, 0, 0, 0, '13px')
		
		self.hLabelNode = self.GUICtrlCreateLabel('Network connection', 215, 155, 0, 0, 0, 0, '13px')
		self.hLabelSelInfo = self.GUICtrlCreateLabel('Changes requiring restart', 215, 205, 130, 20, 0, '#b53b3b')
		self.hLabelSelInfo.hide()
		
		self.hLabelSelection = self.GUICtrlCreateInput('', 215, 175, 150, 30)
		self.hLabelSelection.setReadOnly(True)

		self.hButtonSelect = self.GUICtrlCreateButton('▼', 365, 175, 30, 30)
		
		self.hButtonSelectLocal = self.GUICtrlCreateButton('Run local node', 215, 205, 180, 30, 'rgba(255, 255, 255, 10%);text-align: left;padding-left: 7px')
		self.hButtonSelectLocal.hide()
		self.hButtonSelectPublic1 = self.GUICtrlCreateButton('Use public node #1', 215, 235, 180, 30, 'rgba(255, 255, 255, 10%);text-align: left;padding-left: 7px')
		self.hButtonSelectPublic1.hide()
		self.hButtonSelectPublic2 = self.GUICtrlCreateButton('Use public node #2', 215, 265, 180, 30, 'rgba(255, 255, 255, 10%);text-align: left;padding-left: 7px')
		self.hButtonSelectPublic2.hide()
		self.hButtonSelectManual = self.GUICtrlCreateButton('Use custom node', 215, 295, 180, 30, 'rgba(255, 255, 255, 10%);text-align: left;padding-left: 7px')
		self.hButtonSelectManual.hide()
		
		self.hLabelUrl = self.GUICtrlCreateLabel('Custom node address', 450, 160)
		self.hLabelUrl.hide()
		self.hInputUrl = self.GUICtrlCreateInput('http://', 450, 175, 180, 30)
		self.hInputUrl.hide()
		
		self.hLabelUrlPort = self.GUICtrlCreateLabel('Custom node port', 450, 210)
		self.hLabelUrlPort.hide()
		self.hInputUrlPort = self.GUICtrlCreateInput('', 450, 225, 75, 30)
		self.hInputUrlPort.setValidator(QIntValidator(1, 65535))
		self.hInputUrlPort.hide()
		
		
		self.tabsControls[self.hButtonSettings.objectName()] = [self.hCheckboxNots, self.hCheckboxNotsBk, self.hCheckboxNotsText,
		self.hCheckboxStartup, self.hCheckboxStartupBk, self.hCheckboxText, self.hCheckboxTrayClose, 
		self.hCheckboxTrayCloseBk, self.hCheckboxTrayCloseText, self.hCheckboxAutoHide, self.hCheckboxAutoHideBk, self.hCheckboxAutoHideText, self.hLabelNode, 
		self.hLabelSelection, self.hButtonSelect]
		
		#Transactions TAB
		self.hTableTransactions = QTableWidget(0, 3, self)
		self.hTableTransactions.move(215, 15)
		self.hTableTransactions.setFixedSize(570, 205)
		self.hTableTransactions.verticalHeader().hide()
		self.hTableTransactions.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.hTableTransactions.setHorizontalHeaderLabels(['Date', 'Tx hash', 'Amount', 'From address'])
		self.hTableTransactions.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
		self.hTableTransactions.horizontalHeader().resizeSection(0, 120)
		self.hTableTransactions.horizontalHeader().resizeSection(1, 265)
		self.hTableTransactions.horizontalHeader().resizeSection(2, 183)
		self.tabsControls[self.hButtonHistory.objectName()] = [self.hTableTransactions]
		#About TAB
		self.hLabelAbout = self.GUICtrlCreateLabel('''Galaxia GUI Wallet v1.0

Author: MrKris7100

Special thanks to njamnjam, MadHater, EMPEROR and other people from Galaxia team.

This program is not official part of Galaxia project.
This program uses 3rd party applications: xi-daemon and xi-pgservice from Galaxia project.

If you enjoy the program you can support me by donating some GLX using button below.''', 215, 15, 0, 0, 0, 0, '11px')
		self.hButtonDonate = self.GUICtrlCreateButton('Donate', 215, 150, 75, 30)
		
		self.tabsControls[self.hButtonAbout.objectName()] = [self.hLabelAbout, self.hButtonDonate]
		
		for ctrl in self.tabsControls[self.hButtonAbout.objectName()]:
			ctrl.hide()
		for ctrl in self.tabsControls[self.hButtonReceive.objectName()]:
			ctrl.hide()
		for ctrl in self.tabsControls[self.hButtonSettings.objectName()]:
			ctrl.hide()
		for ctrl in self.tabsControls[self.hButtonHistory.objectName()]:
			ctrl.hide()
			
		if config['wallet']['connection'] == 'local':
			self.hLabelSelection.setText('Run local node')
		elif config['wallet']['connection'] == 'ext1':
			self.hLabelSelection.setText('Use public node #1')
		elif config['wallet']['connection'] == 'ext2':
			self.hLabelSelection.setText('Use public node #2')
		elif config['wallet']['connection'] == 'custom':
			self.hLabelSelection.setText('Use custom node')
		url = config['wallet']['url'].split(':')
		self.hInputUrl.setText(url[0] + ':' + url[1])
		self.hInputUrlPort.setText(url[2])
		
		# Create the menu
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
		self.tray_icon.setIcon(QIcon(self.hLogoGreen))
		self.setWindowIcon(QIcon(self.hLogoGreen))
		
		for ctrl in self.tabsControls['leftpanel']:
				ctrl.hide()
		for ctrl in self.tabsControls[self.hButtonSend.objectName()]:
			ctrl.hide()
		self.tray_icon.show()
		#Wallet initialization
		threading.Timer(0.05, self.NetworkThread).start()
	
	def GetNodeInfo(self):
		response = False
		try:
			response = requests.post(daemon_url + '/rpc', data='{"method" : "explorer.info.node", "params" : null, "id" : "", "jsonrpc" : "2.0"}', headers={'Content-Type':'application/json'})
		except:
			pass
		if response:
			response.json = json.loads(response.text)
		return response
		
	def WaitForDaemon(self):
		timeout = TimerInit()
		while TimerDiff(timeout) < 5000:
			nodeInfo = self.GetNodeInfo()
			if nodeInfo and 'result' in nodeInfo.json:
				return True
			sleep(0.5)
		return False
	
	def eventFilter(self, obj, event):
		type = event.type()
		if obj.isEnabled():
			if type == 129:
				if obj == self.hButtonCreate:
					self.hLabelTip.setText('Create new wallet')
				elif obj == self.hButtonOpen:
					self.hLabelTip.setText('Open existing wallet')
			if type == 128 and (obj == self.hButtonCreate or obj == self.hButtonOpen):
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
		button.mybackgroundcolor = background if background else 'rgba(255, 255, 255, 10%)'
		button.mycolor = color if color else 'rgb(26, 188, 156)'
		button.myborder = 'none'
		button.myhoverbackgroundcolor = 'rgba(26, 188, 156, 50%)'
		button.myhovercolor = 'white'
		GUICtrlUpdateStyle(button)
		button.clicked.connect(self.button_proc)
		return button
		
	def GUICtrlCreateCheckBox(self, text, left, top):
		checkbox = QCheckBox(text, self)
		self.ctrlCount += 1
		checkbox.setObjectName(str(self.ctrlCount))
		checkbox.move(left, top)
		checkbox.type = 'QCheckBox'
		checkbox.toggled.connect(self.checkbox_proc)
		return checkbox
	
	def GUICtrlCreateBox(self, color, left, top, width, height):
		box = QLabel(self)
		box.move(left, top)
		box.setFixedSize(width, height)
		box.setStyleSheet('background-color: ' + color)
		box.setAlignment(Qt.AlignHCenter)
		box.setAlignment(Qt.AlignVCenter)
		return box
	
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
		label.mycolor = color if color else 'rgb(26, 188, 156)'
		label.myborder = 'none'
		GUICtrlUpdateStyle(label)
		return label
		
	def GUICtrlCreateInput(self, text, left, top, width, height, background = 0, color = 0, fontsize = 0, fontweight = 0):
		input = QLineEdit(self)
		self.ctrlCount += 1
		input.setObjectName(str(self.ctrlCount))
		input.move(left, top)
		input.type = 'QLineEdit'
		input.setFixedSize(width, height)
		input.myfontsize = fontisze if fontsize else '14px'
		input.myfontweight = fontweight if fontweight else 'bold'
		input.mybackgroundcolor = background if background else 'rgba(255, 255, 255, 10%)'
		input.mycolor = color if color else 'rgb(26, 188, 156)'
		input.myborder = 'none'
		GUICtrlUpdateStyle(input)
		input.setText(text)
		input.textChanged.connect(self.input_proc)
		input.editingFinished.connect(self.input_proc_end)
		return input
		
	def XiNetworkSetState(self, iState, iPercent = 0):
		if iState != self.XiNetworkState:
			self.XiNetworkState = iState
			if self.XiNetworkState == 0:
				print('INFO: Network disconnected')
				GUICtrlSetColor(self.hLabelNetworkIcon, '#fc7c7c')
				GUICtrlSetColor(self.hLabelNetworkStatus, '#fc7c7c')
				self.hLabelNetworkStatus.setText("Disconnected")
				self.hLabelNetworkIcon.setPixmap(self.hLogoRed)
			elif self.XiNetworkState == 1:
				GUICtrlSetColor(self.hLabelNetworkIcon, '#f7ff91')
				GUICtrlSetColor(self.hLabelNetworkStatus, '#f7ff91')
				self.hLabelNetworkStatus.setText("Syncing (" + '%.2f' % iPercent + "%)")
				self.hLabelNetworkIcon.setPixmap(self.hLogoYellow)
			elif self.XiNetworkState == 2:
				print('INFO: Network synced')
				GUICtrlSetColor(self.hLabelNetworkIcon, 'rgb(26, 188, 156)')
				GUICtrlSetColor(self.hLabelNetworkStatus, 'rgb(26, 188, 156)')
				self.hLabelNetworkStatus.setText("Synced")
				self.hLabelNetworkIcon.setPixmap(self.hLogoGreen)
		elif iState == 1:
			self.hLabelNetworkStatus.setText("Syncing (" + '%.2f' % iPercent + "%)")
	
	def button_proc(self):
		obj = self.sender()
		if self.netSelect and obj != self.hButtonSelect:
			for item in [self.hButtonSelectLocal, self.hButtonSelectPublic1, self.hButtonSelectPublic2, self.hButtonSelectManual]:
				item.hide()
			GUICtrlSetBkColor(self.hButtonSelect, 'rgba(255, 255, 255, 10%)')
			GUICtrlSetColor(self.hButtonSelect, 'rgb(26, 188, 156)')
			self.hButtonSelect.setText('▼')
			self.netSelect = False
			if self.netChanged:
				self.hLabelSelInfo.show()
		if obj != self.activeTab:
			#Switching TABS
			if obj in self.navButtons:
				if self.netChanged:
					if obj == self.hButtonSettings:
						self.hLabelSelInfo.show()
					else:
						self.hLabelSelInfo.hide()
				if config['wallet']['connection'] == 'custom':
					if obj == self.hButtonSettings:
						for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
								ctrl.show()
					else:
						for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
								ctrl.hide()
				GUICtrlSetBkColor(self.activeTab, 'rgba(255, 255, 255, 10%)')
				GUICtrlSetColor(self.activeTab, 'rgb(26, 188, 156)')
				for ctrl in self.tabsControls[self.activeTab.objectName()]:
					ctrl.hide()
				GUICtrlSetBkColor(obj, 'rgba(26, 188, 156, 50%)')
				GUICtrlSetColor(obj, 'white')
				for ctrl in self.tabsControls[obj.objectName()]:
					ctrl.show()
				self.activeTab = obj
			else:
				if obj in [self.hButtonSelectLocal, self.hButtonSelectPublic1, self.hButtonSelectPublic2, self.hButtonSelectManual]:
					lastSetting = config['wallet']['connection']
					if obj == self.hButtonSelectLocal:
						config['wallet']['connection'] = 'local'
						self.hLabelSelection.setText('Run local node')
						config['wallet']['url'] = 'http://127.0.0.1:22869'
					elif obj == self.hButtonSelectPublic1:
						config['wallet']['connection'] = 'ext1'
						config['wallet']['url'] = 'http://5.172.219.176:22869'
						self.hLabelSelection.setText('Use public node #1')
					elif obj == self.hButtonSelectPublic2:
						config['wallet']['connection'] = 'ext2'
						config['wallet']['url'] = 'http://5.172.219.176:22869'
						self.hLabelSelection.setText('Use public node #2')
					elif obj == self.hButtonSelectManual:
						config['wallet']['connection'] = 'custom'
						self.hLabelSelection.setText('Use custom node')
					if lastSetting != config['wallet']['connection']:
						print('zmieniono cfg')
						if config['wallet']['connection'] == 'custom':
							for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
								ctrl.show()
						else:
							for ctrl in [self.hLabelUrl, self.hInputUrl, self.hLabelUrlPort, self.hInputUrlPort]:
								ctrl.hide()
						self.hLabelSelInfo.show()
						self.netChanged = True
						with open("Wallet.ini", "w") as configfile:
							config.write(configfile)
				if obj == self.hButtonSelect:
					if self.netSelect:
						for item in [self.hButtonSelectLocal, self.hButtonSelectPublic1, self.hButtonSelectPublic2, self.hButtonSelectManual]:
							item.hide()
						GUICtrlSetBkColor(self.hButtonSelect, 'rgba(255, 255, 255, 10%)')
						GUICtrlSetColor(self.hButtonSelect, 'rgb(26, 188, 156)')
						self.netSelect = False
						self.hButtonSelect.setText('▼')
					else:
						for item in [self.hButtonSelectLocal, self.hButtonSelectPublic1, self.hButtonSelectPublic2, self.hButtonSelectManual]:
							item.show()
						GUICtrlSetBkColor(self.hButtonSelect, 'rgba(26, 188, 156, 50%)')
						GUICtrlSetColor(self.hButtonSelect, 'white')
						self.netSelect = True
						self.hButtonSelect.setText('▲')
						self.hLabelSelInfo.hide()
				elif obj == self.hOffline:
					self.runOffline()
				elif obj == self.hButtonPass:
					self.hLabelInit.show()
					self.hLabelPass.hide()
					self.hInputPass.hide()
					self.hButtonPass.hide()
					self.pwd = self.hInputPass.text()
					if self.pwd == '': self.pwd = -1
					self.pipe = 'postpassword'
				elif obj == self.hButtonPassSet:
					self.pwd = self.hInputPass.text()
					self.pipe = 'newwallet'
				elif obj == self.hShow:
					self.showWindow()
				#Donate button
				elif obj == self.hButtonDonate:
					self.hInputAddress.setText(donate_address)
					self.hInputPaymentID.setText('DONATE')
					self.hButtonSend.click()
				#Wallet open button
				elif obj == self.hButtonOpen:
					self.hButtonCreate.setEnabled(False)
					self.hButtonOpen.setEnabled(False)
					tkroot = Tk()
					tkroot.withdraw()
					file_path = filedialog.askopenfilename(title='Select wallet file', filetypes=[('Wallet containers', '*.wallet')])
					tkroot.destroy()
					if pathlib.Path(file_path).is_file():
						config['wallet']['path'] = file_path
						with open("Wallet.ini", "w") as configfile:
							config.write(configfile)
						self.hLabelInit.show()
						self.hButtonCreate.hide()
						self.hButtonOpen.hide()
						self.hLabelTip.hide()
						self.pipe = 'pgservice'
					else:
						self.hButtonCreate.setEnabled(True)
						self.hButtonOpen.setEnabled(True)
				#Wallet create button
				elif obj == self.hButtonCreate:
					random_container = randomString(10)
					config['wallet']['path'] = random_container + '.wallet'
					self.hButtonCreate.hide()
					self.hButtonOpen.hide()
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
					if not self.valid_address or not self.hInputAmount.hasAcceptableInput() or float(self.hInputAmount.text()) + 0.01 > self.walletBalance:
						self.controlBlink(3, 0.15)
						sending = False
					if sending:
						respond = SendTransaction(self.hInputAddress.text(), float(self.hInputAmount.text()), 133791)
						self.hInputAddress.setText('')
						self.hInputAmount.setText('')
						if 'error' in respond:
							print('Unable to send transaction (' + respond['error']['message'] + ')')
							self.tray_icon.showMessage('Unable to send transaction', respond['error']['message'], msecs=3000)
						else:
							print('Transaction sent! Tx hash (' + respond['result']['transaction_hash'] + ')')
							self.tray_icon.showMessage('Transaction sent!', 'Tx hash (' + respond['result']['transaction_hash'] + ')', msecs=3000)
	
	def AddressToClip(self):
		pyperclip.copy(self.wallet_address)
	
	def AddressFromClip(self):
		self.hInputAddress.setText(pyperclip.paste())
	
	def input_proc_end(self):
		obj = self.sender()
		if obj == self.hInputAmount:
			dot = find_str(obj.text(), '.')
			if obj.text() != '' and ValidAmount(obj.text()) and float(obj.text()) > 0 and not (dot >= 0 and len(obj.text()) > 7 + dot): obj.setText('%.6f' % float(obj.text()))
		elif obj == self.hInputUrl or obj == self.hInputUrlPort:
			config['wallet']['url'] = self.hInputUrl.text() + ':' + self.hInputUrlPort.text()
			with open("Wallet.ini", "w") as configfile:
				config.write(configfile)
	
	def input_proc(self):
		obj = self.sender()
		if obj == self.hInputAmount:
			if obj.text() == '' or float(obj.text()) == 0 :
				self.hLabelAmountErr.setText('Please enter amount')
			elif float(obj.text()) + 0.01 > self.walletBalance:
				self.hLabelAmountErr.setText('Not enought founds')
			elif not obj.hasAcceptableInput():
				self.hLabelAmountErr.setText('Invalid amount')
			else:
				self.hLabelAmountErr.setText('')
			if obj.hasAcceptableInput() and float(obj.text()) + 0.01 <= self.walletBalance:
				GUICtrlSetBkColor(self.hInputAmount, 'rgba(255, 255, 255, 10%)')
			else:
				GUICtrlSetBkColor(self.hInputAmount, 'rgba(255, 0, 0, 15%)')
		elif obj == self.hInputAddress:
			#Checking typed address
			self.valid_address = False
			if obj.text() == '': #Not entered
				self.hLabelAddressErr.setText('Please enter address')
			elif len(obj.text()) != 98: #Too short
				self.hLabelAddressErr.setText('Invalid address')
			elif obj.text()[0:3] != 'gxi': #Not valid - no prefix
				self.hLabelAddressErr.setText('Invalid address')
			else:
				self.hLabelAddressErr.setText('')
				self.valid_address = True
			if self.valid_address:
				GUICtrlSetBkColor(self.hInputAddress, 'rgba(255, 255, 255, 10%)')
			else:
				GUICtrlSetBkColor(self.hInputAddress, 'rgba(255, 0, 0, 15%)')
		elif obj == self.hInputUrl:
			if obj.text() == '' or obj.text()[0:7] != 'http://':
				obj.setText('http://')
		return
		
	def checkbox_proc(self):
		obj = self.sender()
		if obj == self.hCheckboxStartup:
			config['wallet']['autostart'] = str(int(obj.isChecked()))
		elif obj == self.hCheckboxTrayClose:
			config['wallet']['trayclose'] = str(int(obj.isChecked()))
		elif obj == self.hCheckboxAutoHide:
			config['wallet']['autohide'] = str(int(obj.isChecked()))
		elif obj == self.hCheckboxNots:
			config['wallet']['disablenotifications'] = str(int(obj.isChecked()))
		#Update config file
		with open("Wallet.ini", "w") as configfile:
			config.write(configfile)
	
	def controlBlink(self, times = 5, delay = 0.1):
		threading.Timer(0, self.blinkProc, args=[times, delay]).start()
		
	def blinkProc(self, times, delay):
		for i in range(times):
			if not self.hInputAmount.hasAcceptableInput() or float(self.hInputAmount.text()) + 0.01 > self.walletBalance: self.hLabelAmountErr.hide()
			if not self.valid_address: self.hLabelAddressErr.hide()
			sleep(delay)
			if self.activeTab != self.hButtonSend: break
			if not self.hInputAmount.hasAcceptableInput() or float(self.hInputAmount.text()) + 0.01 > self.walletBalance: self.hLabelAmountErr.show()
			if not self.valid_address: self.hLabelAddressErr.show()
			sleep(delay)
	
	def XiNetworkUpdate(self):
		nodeInfo = self.GetNodeInfo()
		self.nodeSync = nodeInfo.json['result']['chain']['top_height']
		self.networkSync = nodeInfo.json['result']['p2p']['height']
		walletInfo = GetWalletBalance()
		self.walletBalance = walletInfo['result']['available_balance'] / 1000000
		self.walletBalanceLocked = walletInfo['result']['locked_amount'] / 1000000
		if self.networkSync and self.networkSync > 1:
			if self.nodeSync < self.networkSync:
				self.XiNetworkSetState(1, self.nodeSync / self.networkSync * 100)
			else:
				self.XiNetworkSetState(2)
		else:
			self.XiNetworkSetState(0)
	
	def NetworkThread(self):
		global daemon_url
		if '--offline' in app.arguments():
			print('INFO: Running wallet in offline mode')
			self.runOffline()
		else:
			if int(config['wallet']['autohide']):
				print('INFO: Hiding window to tray')
				self.tray_icon.showMessage('Info', 'Wallet hidden to tray', msecs=3000)
			else:
				self.hShow.click()
			daemon = False
			if ProcessExists("xi-daemon"):
				ProcessClose("xi-daemon")
			if config['wallet']['connection'] != 'local':
				print('INFO: Connecting to', config['wallet']['url'] + '...')
				if self.WaitForDaemon():
					daemon = True
				else:
					print('ERROR: Unable connect to external node')
					daemon_url = 'http://127.0.0.1:22869'
			if not daemon:
				print('INFO: Starting local node...')
				self.xi_daemon = Popen("xi-daemon --p2p-local-ip --rpc-server --block-explorer-enable --network Galaxia.MainNet", creationflags = CREATE_NO_WINDOW)
				if self.WaitForDaemon():
					daemon = True
				else:
					print('ERROR: Unable connect to local node')
			if not daemon:
				print('ERROR: No connection to daemon, closing wallet...')
				sleep(2.5)
				self.close()
				return
			else:
				if not pathlib.Path(config['wallet']['path']).is_file():
					print('ERROR: Wallet file not found')
					self.hButtonCreate.show()
					self.hButtonOpen.show()
					self.hLabelTip.show()
					self.hLabelInit.hide()
					if int(config['wallet']['autohide']): self.hShow.click()
				else:
					print('INFO: Wallet file found')
					self.pipe = 'pgservice'
			while True:
				if self.pipe == 'pgservice':
					break
				elif self.pipe == 'newwallet':
					self.hLabelInit.show()
					#Generate new wallet
					self.hLabelPassSet.hide()
					self.hInputPass.hide()
					self.hButtonPassSet.hide()
					run('xi-pgservice.exe -g -w "' + config['wallet']['path'] +'" --network Galaxia.MainNet -p "' + self.pwd + '"', creationflags = CREATE_NO_WINDOW)
					with open("Wallet.ini", "w") as configfile:
						config.write(configfile)
					break
				else:
					sleep(0.05)
			#Pg service initializing
			if ProcessExists("xi-pgservice"):
				ProcessClose("xi-pgservice")
			if self.pwd == -1:
				print('INFO: Starting xi-pgservice (New wallet generated)')
			else:
				print('INFO: Starting xi-pgservice (Password protected check)')
			while True:
				result = self.WaitForPg()
				if result == 'ok':
					break
				elif result == 'requirepassword':
					self.hLabelInit.hide()
					self.hLabelPass.show()
					self.hInputPass.show()
					self.hButtonPass.show()
					self.pipe = False
					while self.pipe != 'postpassword':
						sleep(0.05)
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
			print('INFO: Wallet started (Password is correct)')
			walletAddresses = GetWalletAddress()
			if walletAddresses:
				self.wallet_address = walletAddresses['result']['addresses'][0]
			self.UpdateWalletAddress()
			self.UpdateBalance()
			self.hLabelInit.hide()
			self.hLabelLogo.hide()
			self.hButtonCreate.hide()
			self.hButtonOpen.hide()
			self.hLabelTip.hide()
			for ctrl in self.tabsControls['leftpanel']:
				ctrl.show()
			for ctrl in self.tabsControls[self.hButtonSend.objectName()]:
				ctrl.show()
			if not noQR:
				self.UpdateQrCode()
			while self.running:
				try:
					item = self.notQueue.get(False)
					if not int(config['wallet']['disablenotifications']): self.tray_icon.showMessage('New transaction', item[0] + '\nNew transaction found\nTx hash (' + item[1] + ')\nAmount: ' + item[2], msecs=2500)
				except:
					pass
				self.XiNetworkUpdate()
				self.UpdateBalance()
				self.UpdateTransactions()
				sleep(2.5)
					
	def WaitForPg(self):
		url = daemon_url[7:].split(':')
		addr = url[0]
		port = url[1]
		self.pgservice = Popen('xi-pgservice.exe -w "' + config['wallet']['path'] + '" --rpc-legacy-security --network Galaxia.MainNet -p "' + str(self.pwd) + '" --daemon-address ' + addr + ' --daemon-port ' + port, stdout=PIPE, creationflags = CREATE_NO_WINDOW)
		timeout = TimerInit()
		pgservice = False
		while self.pgservice.poll() is None:
			if TimerDiff(timeout) > 2500:
				pgservice = True
				break
			else:
				sleep(0.05)
		if not pgservice:
			stdout = str(self.pgservice.communicate()[0])
			if 'password is wrong' in stdout:
				if self.pwd == '':
					return 'requirepassword'
				else:
					return 'wrongpassword'
			else:
				print("That shouldn't happen!!!")
				self.close()
		else:
			return 'ok'

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
		self.hButtonCreate.hide()
		self.hButtonOpen.hide()
		self.hLabelTip.hide()
		date = datetime.datetime.fromtimestamp(1576705196)
		self.addTx.emit(str(date), '4437459bac024c7ce3fc0ecf63ef482466fd19141f46709c1cd640aeb6c20e27', str(1.234000))
		self.hShow.click()

	def showWindow(self):
		self.show()
	
	def hideWindow(self):
		self.hide()
	
	def AddTx(self, col0, col1, col2):
		self.hTableTransactions.insertRow(0)
		self.hTableTransactions.setItem(0, 0, QTableWidgetItem(col0))
		self.hTableTransactions.setItem(0, 1, QTableWidgetItem(col1))
		self.hTableTransactions.setItem(0, 2, QTableWidgetItem(col2))
	
	def UpdateTransactions(self):
		transactions = []
		fullScan = False
		#Update transaction table
		if self.networkSync and self.networkSync > 1 and self.lastScan != self.networkSync and not self.scanning:
			self.scanning = True
			if self.lastScan < 2:
				print('INFO: Full tx list request')
				fullScan = True
				transactions = GetWalletTransactions(1, self.networkSync)
				self.lastScan = self.networkSync
			elif self.networkSync - self.lastScan > 0:
				print('INFO: Partial tx list request, blocks from', self.lastScan, ' to ', self.networkSync)
				transactions =  GetWalletTransactions(self.lastScan, self.networkSync - self.lastScan) 
				self.lastScan = self.networkSync
			else:
				self.scanning = False
				return
			if len(transactions):
				#Get transactions hashes list
				for transaction in transactions:
					tx_info = GetTransactionInfo(transaction)
					date = datetime.datetime.fromtimestamp(int(tx_info['result']['transaction']['timestamp']))
					amount = tx_info['result']['transaction']['amount']
					amount = amount / 1000000
					self.addTx.emit(str(date), transaction, str(amount))
					if not fullScan:
						print('New transaction found! Amount:' + str(amount) + ' (' + transaction + ')')
						self.IncomingTx(transaction, str(amount), str(date))
				print('INFO: ', len(transactions), 'transactions added to table')
			else:
				print('INFO: No new transactions found')
			self.scanning = False
	
	def IncomingTx(self, hash, amount, time):
		self.notQueue.put([time, hash, amount])
	
	def UpdateBalance(self):
		self.hLabelBalanceValue.setText('%.6f' % self.walletBalance)
		self.hLabelBalanceLockedValue.setText('%.6f' % self.walletBalanceLocked)

style = '''
			QHeaderView::section {
				background-color: rgba(26, 188, 156, 50%);
				color: white;
				padding-left: 4px;
				border: 1px solid rgb(26, 188, 156);
				font-weight: bold;
			}
			QHeaderView {
				background: rgba(255, 255, 255, 10%);
			}
			QHeaderView::section:checked
			{
				background-color: rgba(26, 188, 156, 50%);
				color: white;
				padding-left: 4px;
				border: 1px solid rgb(26, 188, 156);
			}
			QTableWidget {
				gridline-color: rgb(26, 188, 156);
				background-color: transparent;
				border: 1px solid rgb(26, 188, 156);
				color: rgb(26, 188, 156);
			}
			QTableWidget::item {
				width
				border-left: 1px solid rgb(26, 188, 156);
				background: rgba(255, 255, 255, 10%);
			}	
			QTableWidget::item:focus {
				border-left: 1px solid rgb(26, 188, 156);
				background: rgba(255, 255, 255, 10%);
				color: rgb(26, 188, 156);
			}	
			QCheckBox {
				background-color: transparent;
				color: rgb(26, 188, 156);
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
				background-color: rgb(26, 188, 156);
			}
			QCheckBox::indicator:unchecked {
				width: 25px;
				height: 25px;
			}
		'''

if __name__ == '__main__':
	donate_address = 'enter donate address here'
	config = configparser.ConfigParser()
	#Initial config
	if not pathlib.Path("Wallet.ini").is_file():
		print('INFO: No wallet config, generate new config file')
		newwallet = True
		with open("Wallet.ini", "w") as configfile:
			config['wallet'] = {'path' : '', 'url' : 'http://127.0.0.1:22869', 'connection' : 'local', 'trayclose' : 0, 'autostart' : 0, 'autohide' : 0, 'disablenotifications' : 0}
			config.write(configfile)
			print('INFO: Config saved')
	config.read("Wallet.ini")
	daemon_url = config['wallet']['url']
	if not '--offline' in sys.argv:
		pathPg = 'xi-pgservice.exe' if os.name == 'nt' else 'xi-pgservice'
		pathDaemon = 'xi-daemon.exe' if os.name == 'nt' else 'xi-daemon'
		if not pathlib.Path(pathPg).is_file() or not pathlib.Path(pathDaemon).is_file():
			print('ERROR: Galaxia binaries not found! Make sure to have "xi-daemon" and "xi-pgservice" files in wallet folder')
			sleep(5)
			sys.exit()
	app = QApplication(sys.argv)
	app.setStyleSheet(style)
	ex = App()
	print('INFO: Running main window')
	sys.exit(app.exec_())

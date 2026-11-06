import json, sys, os.path, random, string, asyncio, shutil, requests, time, re, datetime, os
from modules.logger import *
from discord.utils import get

#Variables for API data
Globals = {
	'networkInfo': None,
	'moreloInfo': [None, None, None],
	'blockInfo': None,
	'coingeckoInfo': None,
	'emissionInfo': None,
	'poolsInfo': None
}

#Check is config file passed in arguments
if len(sys.argv) > 1:
	cfg_file = sys.argv[1]
	Log("Custom config path used")
	if not os.path.exists(sys.argv[1]):
		Log("Config file doesn't exist.", ERROR)
		exit()
else:
	cfg_file = "config.json"

#Loading config
try:
	f = open(cfg_file)
	config = json.load(f)
	Log("Config file loaded")
except:
	Log("Config file fucked up, bye!", ERROR)
	exit()

#Hashrate formating
def Suffix(num):
	if num < 1000:
		num = "%.2f" % num + " H/s"
	elif num < 1000000:
		num = "%.2f" % (num / 1000) + " kH/s"
	elif num < 1000000000:
		num = "%.2f" % (num / 1000000) + " MH/s"
	elif num < 1000000000000: #Po po po power! 
		num = "%.2f" % (num / 1000000000) + " GH/s"
	return num 
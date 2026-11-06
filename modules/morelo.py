import subprocess
from modules.timer import *
from modules.api import *
import time
import os
import signal
import atexit
import os
import subprocess


def _process_options():
	# CREATE_NEW_PROCESS_GROUP is Windows-only, so only pass it on platforms that define it.
	if os.name == 'nt':
		return {'creationflags': subprocess.CREATE_NEW_PROCESS_GROUP}
	return {}

class Morelo():
	def __init__(self, workdir, local = True, d_url = 'http://127.0.0.1:38302', w_port = 38340):
		self.api = API(d_url, w_port)
		self.daemon = self.Daemon(local, d_url, workdir, self.api)
		self.wallet = self.Wallet(workdir, w_port, self.api, d_url)
		
		
	class Daemon():
		def __init__(self, local, d_url, workdir, api):
			self.api = api
			self.local = local
			if self.local:
				self.process = self.run(workdir)
				# A stopped child may already have exited when Python runs its shutdown hooks.
				atexit.register(self.stop)
			
		def run(self, workdir):
			# Pass each argument separately so paths with spaces work without shell parsing.
			return subprocess.Popen([os.path.join(os.getcwd(), 'morelod'), '--data-dir', workdir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, **_process_options())

		def stop(self):
			if self.local:
				# Avoid raising when the daemon has already shut down.
				if self.process.poll() is None:
					self.process.terminate()
					return True
				return False
			else:
				return False

		def wait(self):
			timeout = Timer()
			while timeout.get() < 15000:
				try:
					nodeInfo = self.api.daemon.get_info()
					if nodeInfo and 'result' in nodeInfo:
						return True
				except:
					pass
				time.sleep(1)
			return False
		
		def get_info(self):
			req1 = self.api.daemon.sync_info()
			req2 = self.api.daemon.get_connections()
			req3 = self.api.daemon.get_info()
			#Check response is valid, remote node fix
			if not 'result' in req1:
				return False
			#some shitty mixing responses json
			req1['result']['difficulty'] = 0
			target_height = 0
			if 'connections' in req2['result']:
				for conn in req2['result']['connections']:
					if conn['height'] > target_height:
						target_height = conn['height']
			req1['result']['target_height'] = target_height
			if req3:
				req1['result']['difficulty'] = req3['result']['difficulty']
			return req1
			
	class Wallet():
		def __init__(self, workdir, w_port, api, d_url):
			self.api = api
			self.process = self.run(workdir, w_port, d_url)
			# A stopped child may already have exited when Python runs its shutdown hooks.
			atexit.register(self.stop)

		def wait(self):
			timeout = Timer()
			while timeout.get() < 15000:
				try:
					walletInfo = self.api.wallet.get_version()
					if walletInfo and 'result' in walletInfo:
						return True
				except:
					pass
				time.sleep(1)
			return False
		def stop(self):
			# Stop the RPC service cleanly, falling back to process termination on RPC failure.
			try:
				return self.api.wallet.stop()
			except Exception:
				if self.process.poll() is None:
					self.process.terminate()
				return False
			
		def create(self, filename, password = ""):
			return self.api.wallet.create(filename, password)
			
		def run(self, workdir, w_port, d_url):
			# Use the wallet RPC's correctly spelled daemon flag and avoid shell string parsing.
			args = [os.path.join(os.getcwd(), 'morelo-wallet-rpc'), '--daemon-address', d_url, '--wallet-dir', workdir, '--rpc-bind-port', str(w_port), '--disable-rpc-login']
			return subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, **_process_options())
		
		def open(self, file, password = ""):
			return self.api.wallet.open(file, password)
			
		def get_balance(self):
			return self.api.wallet.get_balance()
			
		def get_address(self):
			data = self.api.wallet.get_address()
			return data['result']['address']
			
		def get_transfers(self, start, count):
			transactions = []
			data = self.api.wallet.get_transfers(start, count)
			if 'in' in data['result']:
				for block in data['result']['in']:
					transactions.append(block['txid'])
			if 'out' in data['result']:
				for block in data['result']['out']:
					transactions.append(block['txid'])
			return transactions
			
		def get_transfer(self, tx_hash):
			return self.api.wallet.get_transfer(tx_hash)
			
		def transfer(self, receipent, amount, txid = ""):
			return self.api.wallet.transfer(receipent, amount, txid)
		
		def get_keys(self):
			return self.api.wallet.get_keys()

		def get_version(self):
			return self.api.wallet.get_version()

		def get_height(self):
			return self.api.wallet.get_height()
			
		
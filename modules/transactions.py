class Transactions():
	def __init__(self):
		self.transactions = []
		
	def add(self, tx):
		self.transactions.append(self.Transaction(tx))
		
	def get(self, txid):
		for tx in self.transactions:
			# Compare the hash exposed by the wrapper instead of subscripting a Transaction object.
			if tx.get_hash() == txid:
				return tx
		return False
		
	def remove(self, txid):
		for tx in self.transactions:
			# Keep removal consistent with get(), which indexes transactions by their RPC hash.
			if tx.get_hash() == txid:
				self.transactions.remove(tx)
				return True
		return False
		
	class Transaction():
		def __init__(self, data):
			self.data = data
			
		def get_hash(self):
			# Wallet RPC versions place the hash either on the result or its transfer record.
			result = self.data.get('result', {})
			transfer = result.get('transfer', {})
			return transfer.get('txid', result.get('txid'))
			
		def get_transfers(self):
			# Normalize single-transfer and multi-transfer RPC responses for consumers.
			result = self.data.get('result', {})
			if 'transfers' in result:
				return result['transfers']
			transfer = result.get('transfer')
			return [transfer] if transfer else []
		
		def get_transfer(self, i):
			return self.get_transfers()[i]
			
		def get_fee(self):
			# Sum per-transfer fees without shadowing the running total.
			return sum(transfer.get('fee', 0) for transfer in self.get_transfers())
			
		def get_amount(self):
			amount = 0
			# Use safe lookups so partial RPC records do not crash the transaction history.
			for transfer in self.get_transfers():
				if transfer.get('type') == 'in':
					amount += transfer.get('amount', 0)
				elif transfer.get('type') == 'out':
					amount -= transfer.get('amount', 0)
			return amount
		
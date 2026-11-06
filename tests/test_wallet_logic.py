import unittest
from unittest.mock import patch

from modules.api import API
from modules.morelo import Morelo
from modules.transactions import Transactions


class WalletApiTests(unittest.TestCase):
	def setUp(self):
		self.wallet = API().wallet

	def test_balance_returns_account_totals(self):
		account_balance = {
			"balance": 500,
			"unlocked_balance": 300,
			"per_subaddress": [{"address_index": 0, "balance": 250, "unlocked_balance": 150}],
		}
		with patch.object(self.wallet, "post", return_value={"result": account_balance}):
			self.assertEqual(self.wallet.get_balance()["result"], account_balance)

	def test_transfer_uses_exact_atomic_units(self):
		with patch.object(self.wallet, "post", return_value={"result": {}}) as post:
			self.wallet.transfer("address", "1.000000001")
		self.assertEqual(post.call_args.args[1]["destinations"][0]["amount"], 1000000001)

	def test_transfer_rejects_fractional_atomic_units(self):
		with self.assertRaises(ValueError):
			self.wallet.transfer("address", "0.0000000001")

	def test_transfer_range_uses_count_and_numeric_heights(self):
		with patch.object(self.wallet, "post", return_value={}) as post:
			self.wallet.get_transfers(101, 10000)
		self.assertEqual(post.call_args.args[1]["min_height"], 101)
		self.assertEqual(post.call_args.args[1]["max_height"], 10100)


class TransactionTests(unittest.TestCase):
	def test_lookup_remove_fee_and_net_amount(self):
		# Regression coverage for broken wrapper lookup and fee accumulation.
		data = {"result": {"transfer": {"txid": "hash", "fee": 4, "amount": 12, "type": "out"}}}
		transactions = Transactions()
		transactions.add(data)
		transaction = transactions.get("hash")
		self.assertEqual(transaction.get_fee(), 4)
		self.assertEqual(transaction.get_amount(), -12)
		self.assertTrue(transactions.remove("hash"))
		self.assertFalse(transactions.get("hash"))

	def test_multi_transfer_amount_and_fees(self):
		transaction = Transactions.Transaction({"result": {"transfers": [
			{"fee": 2, "amount": 10, "type": "in"},
			{"fee": 3, "amount": 4, "type": "out"},
		]}})
		self.assertEqual(transaction.get_fee(), 5)
		self.assertEqual(transaction.get_amount(), 6)


class ProcessLaunchTests(unittest.TestCase):
	@patch("modules.morelo.subprocess.Popen")
	def test_daemon_arguments_preserve_workdir_as_one_argument(self, popen):
		daemon = Morelo.Daemon.__new__(Morelo.Daemon)
		daemon.run("/wallet data")
		args = popen.call_args.args[0]
		self.assertEqual(args[-2:], ["--data-dir", "/wallet data"])
		self.assertNotIn("shell", popen.call_args.kwargs)

	@patch("modules.morelo.subprocess.Popen")
	def test_wallet_rpc_uses_correct_daemon_option(self, popen):
		wallet = Morelo.Wallet.__new__(Morelo.Wallet)
		wallet.run("/wallet data", 38340, "http://127.0.0.1:38302")
		args = popen.call_args.args[0]
		self.assertIn("--daemon-address", args)
		self.assertNotIn("--daemon-addres", args)


if __name__ == "__main__":
	unittest.main()

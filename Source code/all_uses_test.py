import unittest
from bank import bank_transaction

class TestBankTransactionDataFlowAllUsesMethod(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bank_transaction(1000, 'deposit', 5000), 6000)

    def test_2(self):
        self.assertEqual(bank_transaction(1000, 'withdrawal', 500), 500)

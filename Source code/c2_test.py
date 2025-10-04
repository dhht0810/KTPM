import unittest
from bank import bank_transaction

class TestBankTransactionControlFlowC2Method(unittest.TestCase):
    def test_1(self):
        with self.assertRaises(ValueError):
            bank_transaction(-10, 'deposit', 500)

    def test_2(self):
        self.assertEqual(bank_transaction(1000, 'deposit', 5000), 6000)
            
    def test_3(self):
        self.assertEqual(bank_transaction(1000, 'deposit', 0), 1000)

    def test_4(self):
        with self.assertRaises(ValueError):
            bank_transaction(1000, 'deposit', 1000001)

    def test_5(self):
        self.assertEqual(bank_transaction(1000, 'withdrawal', 500), 500)

    def test_6(self):
        with self.assertRaises(ValueError):
            bank_transaction(1000, 'transfer', 500)

    def test_7(self):
        with self.assertRaises(ValueError):
            bank_transaction(1000, 'withdrawal', 1500)
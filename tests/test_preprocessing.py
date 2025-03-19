import unittest
from src.preprocessing import nettoyer_sequence

class TestPreprocessing(unittest.TestCase):
    def test_nettoyage(self):
        self.assertEqual(nettoyer_sequence("ACGXTGCA123"), "ACGTGCA")

if _name_ == '_main_':
    unittest.main()

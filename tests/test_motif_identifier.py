import unittest
from src.motif_identifier import identifier_motif

class TestMotifIdentifier(unittest.TestCase):
    def test_motif_present(self):
        self.assertTrue(identifier_motif("ACGTACGT", "ACGT"))

    def test_motif_absent(self):
        self.assertFalse(identifier_motif("ACGTACGT", "TATA"))

if _name_ == '_main_':
    unittest.main()

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gates.gates import Gates

class GatesTests(unittest.TestCase):
    def test_and_gate(self):
        self.assertEqual(Gates.and_gate(True, True, False), False)
        self.assertEqual(Gates.and_gate(False, True, False), False)
        self.assertEqual(Gates.and_gate(False, False, False), False)
        self.assertEqual(Gates.and_gate(True, True, True), True)
    
    def test_or_gate(self):
        self.assertEqual(Gates.or_gate(True, True, False), True)
        self.assertEqual(Gates.or_gate(False, True, False), True)
        self.assertEqual(Gates.or_gate(False, False, False), False)
        self.assertEqual(Gates.or_gate(True, True, True), True)
        
    def test_not_gate(self):
        self.assertEqual(Gates.not_gate(True), False)
        self.assertEqual(Gates.not_gate(False), True)

    def test_nand_gate(self):
        self.assertEqual(Gates.nand_gate(True, True, False), True)
        self.assertEqual(Gates.nand_gate(False, True, False), True)
        self.assertEqual(Gates.nand_gate(False, False, False), True)
        self.assertEqual(Gates.nand_gate(True, True, True), False)

    def test_nor_gate(self):
        self.assertEqual(Gates.nor_gate(True, True, False), False)
        self.assertEqual(Gates.nor_gate(False, True, False), False)
        self.assertEqual(Gates.nor_gate(False, False, False), True)
        self.assertEqual(Gates.nor_gate(True, True, True), False)
        
    def test_xnor_gate(self):
        self.assertEqual(Gates.xnor_gate(True, True, False), True)
        self.assertEqual(Gates.xnor_gate(False, True, False), False)
        self.assertEqual(Gates.xnor_gate(False, False, False), True)
        self.assertEqual(Gates.xnor_gate(True, True, True), False)

if __name__ == "__main__":
     unittest.main()

from unittest import TestCase

class TestBinarySearcher(TestCase):
    def test_one(self):
        self.assertEqual(BinarySearcher.binary_search([1, 1, 1, 1], 0), [False, 0])


import unittest

from src.main.data_structure.list_exercise import*

class TestList(unittest.TestCase):

    def test_sort_list_bubble_asc(self):
        self.assertEqual(sort_list_buble_asc([10,9,8,7,6,5,4,3,2,1]),[1,2,3,4,5,6,7,8,9,10])


    def test_sort_list_bubble_asc_string(self):
        self.assertEqual(sort_list_buble_asc(['A','B','C','F','E','D','Z','L','P']),['A','B','C','D','E','F','L','P','Z'])

    def test_sort_bubble_dec(self):
        self.assertEqual(sort_list_buble_dec([1,2,3,4,5,6,7,8,9,10]),[10,9,8,7,6,5,4,3,2,1])

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 100), "Yes")
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 1000), "No")
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 390), "Yes")
        self.assertEqual(binary_search([1, 5], 100), "No")
    
    def test_binary_search2(self):
        self.assertEqual(binary_search2([1, 5, 15, 35, 100, 305, 390], 100), "Y")
        self.assertEqual(binary_search2([1, 5, 15, 35, 100, 305, 390], 1000), "N")
        self.assertEqual(binary_search2([1, 5, 15, 35, 100, 305, 390], 390), "Y")
    
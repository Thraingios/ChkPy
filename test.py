import unittest, os
from main import main

''' 
Author(s): Nick
Created date: 11/30/21
Description: This file exists to house the test cases for the main file
'''
class TestMain(unittest.TestCase):
    def test_report_mode_normal(self):
        """
        tests report mode on a single file, best case scenario
        """

        result = os.system('../chkpy filetest.py -r')
        print (result)
        

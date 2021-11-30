import unittest, sys
from main import main


''' 
Author(s): Nick
Created date: 11/30/21
Description: This file exists to house the test cases for the main file
'''
class Logger():
    """
    I needed something here in order to catch the output of main since the actual file itself doesnt actually return anything
    but rather prints it to the console. this should allow for redirection of the console and make it so i can parse it within the tests
    """
    stdout = sys.stdout
    messages = []
    def start(self): 
        sys.stdout = self
    def stop(self): 
        sys.stdout = self.stdout
    def write(self, text): 
        self.messages.append(text)
    def ret(self):
        return self.messages
    def reset(self):
        self.messages = []

class TestReport(unittest.TestCase):
    def test_report_mode_normal(self):
        """
        tests report mode on a single file, best case scenario
        just testing to see if it at least runs both functions that its supposed to.
        """
        log = Logger()
        log.reset()
        log.start()
        main(['filetest.py', '-r'])
        log.stop()
        messages = log.ret()
        keys = ['OUTPUT FROM PYLINT!', 'OUTPUT FROM PYCODESTYLE!']
        self.assertIn(keys[0], messages[0])
        self.assertIn(keys[1], messages[2])
        

    def test_report_mode_wrong_file(self):
        """
        tests report mode to see if it runs with a file that doesnt exist, 
        which while it should run both the functions, should also report back that the file doesnt exist
        """
        log= Logger()
        log.reset()
        log.start()
        main(['b.py', '-r'])
        log.stop()
        messages = log.ret()
        keys = ['OUTPUT FROM PYLINT!', 'OUTPUT FROM PYCODESTYLE!', 'does not exist']
        self.assertIn(keys[0], messages[0])
        self.assertIn(keys[1], messages[2])
        self.assertIn(keys[2], messages[0])

class TestDev(unittest.TestCase):
    def test_dev_mode_normal(self):
        """
        tests dev mode on a single file, best case scenario
        just testing to see if it at least runs both functions that its supposed to.
        """
        log = Logger()
        log.reset()
        log.start()
        main(['filetest.py', '-d'])
        log.stop()
        messages = log.ret()
        keys = ['OUTPUT FROM PYLINT!', 'OUTPUT FROM PYCODESTYLE!','RUNNING AUTOPEP8 WITH AGRESSIVENESS LVL 3']
        self.assertIn(keys[2], messages[0])
        self.assertIn(keys[1], messages[4])
        self.assertIn(keys[0], messages[2])
        

    def test_dev_mode_wrong_file(self):
        """
        tests dev mode to see if it runs with a file that doesnt exist, 
        which while it should run both the functions, should also report back that the file doesnt exist
        """
        log= Logger()
        log.reset()
        log.start()
        main(['b.py', '-d'])
        log.stop()
        messages = log.ret()
        keys = ['OUTPUT FROM PYLINT!', 'OUTPUT FROM PYCODESTYLE!','RUNNING AUTOPEP8 WITH AGRESSIVENESS LVL 3', 'does not exist']
        self.assertIn(keys[2], messages[0])
        self.assertIn(keys[1], messages[4])
        self.assertIn(keys[0], messages[2])
        self.assertIn(keys[3], messages[2])

class TestDefault(unittest.TestCase):
    def test_default_mode_normal(self):
        """
        tests report mode on a single file, best case scenario
        just testing to see if it at least runs both functions that its supposed to.
        """
        log = Logger()
        log.reset()
        log.start()
        main(['filetest.py'])
        log.stop()
        messages = log.ret()
        keys = ['OUTPUT FROM PYLINT!', 'OUTPUT FROM PYCODESTYLE!','RUNNING AUTOPEP8 WITH AGRESSIVENESS LVL 3']
        self.assertIn(keys[0], messages[0])
        self.assertIn(keys[1], messages[2])
        self.assertIn(keys[2], messages[4])
        self.assertIn(keys[0], messages[6])
        self.assertIn(keys[1], messages[8])
        

    def test_default_mode_wrong_file(self):
        """
        tests default mode to see if it runs with a file that doesnt exist, 
        which while it should run both the functions, should also report back that the file doesnt exist
        """
        log= Logger()
        log.reset()
        log.start()
        main(['b.py'])
        log.stop()
        messages = log.ret()
        keys = ['OUTPUT FROM PYLINT!', 'OUTPUT FROM PYCODESTYLE!','RUNNING AUTOPEP8 WITH AGRESSIVENESS LVL 3', 'does not exist']
        self.assertIn(keys[0], messages[0])
        self.assertIn(keys[3], messages[0])
        self.assertIn(keys[1], messages[2])
        self.assertIn(keys[2], messages[4])
        self.assertIn(keys[0], messages[6])
        self.assertIn(keys[1], messages[8])
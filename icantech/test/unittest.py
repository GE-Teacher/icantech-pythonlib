from os import chdir
from os.path import dirname
chdir(dirname(__file__))

import unittest
from main import *
import main

import icantech

class UnitTest(unittest.TestCase):
	# Init
    def __init__(self, methodName):
        self.test_script_words = icantech.replit.observe.get_test_script_words()
        self.definded_modules = icantech.replit.observe.definded.modules(
            main, self.test_script_words.keys()
        )
        self.definded_objects = icantech.replit.observe.definded.objects(
            main, self.test_script_words.keys()
        )
        super().__init__(methodName)
	# End init

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_use_numpy(self):
        icantech.replit.unittest.RequiredModuleTest(
            self, 'test numpy', 'numpy', self.definded_modules
        ).run()

    def test_use_pandas(self):
        icantech.replit.unittest.RequiredModuleTest(
            self, 'test pandas', 'pandas', self.definded_modules
        ).run()

    def test_use_pandas2(self):
        icantech.replit.unittest.RequiredModuleTest(
            self, 'test pandas2', 'pandas2', self.definded_modules
        ).run()

    def test_invalid_keyword_0(self):
        icantech.replit.unittest.InvalidObjectTest(
            self, 'key sleepy', self.test_script_words, 'sleepy'
        ).run()

    def test_invalid_keyword_1(self):
        icantech.replit.unittest.InvalidObjectTest(
            self, 'key sleep', self.test_script_words, 'sleep'
        ).run()

    def test_invalid_keyword_2(self):
        icantech.replit.unittest.InvalidKeywordTest(
            self, 'key if', self.test_script_words, 'if'
        ).run()

    def test_invalid_keyword_3(self):
        icantech.replit.unittest.InvalidKeywordTest(
            self, 'key elif', self.test_script_words, 'elif'
        ).run()

    def test_invalid_keyword_4(self):
        icantech.replit.unittest.InvalidOperatorTest(
            self, 'key ==', self.test_script_words, '=='
        ).run()

    def test_invalid_keyword_5(self):
        icantech.replit.unittest.InvalidOperatorTest(
            self, 'key >>', self.test_script_words, '>>'
        ).run()

    def test_limit_time1(self):
        icantech.replit.unittest.LimitTimeTest(
            self, 'time', 1, main.limited_time
        ).run(2)
    
    def test_limit_time2(self):
        icantech.replit.unittest.LimitTimeTest(
            self, 'time', 3, main.limited_time
        ).run(2)

    def test_case_0(self):
        icantech.replit.unittest.RecursionTest(
            self, 'recursion', main.recursion
        ).run()

if __name__ == '__main__':
    unittest.main()
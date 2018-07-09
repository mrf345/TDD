from unittest import TestCase, TestLoader, TextTestRunner
from  simple_functions import (
    print_something, print_something_slowly)
from time import time

class Testing_Something(TestCase):
    def setUp(self):
        """ Setting initial variables """
        self.testing_value = "Something to test"
        self.start_time = time()
        
    def tearDown(self):
        """ To print for each unit """
        
        print("\33[92m %s\33[0m: %s%f\33[0m" % (
                self.id(),
                "\33[100m" if (time() - self.start_time) > 2 else "\33[7m",
                time() - self.start_time
        ))

    def test_printing_something(self):
        """ To test the value printed """
        self.assertEqual(self.testing_value,
            print_something('Something to test'))
    
    def test_printing_something_slowly(self):
        """ To test the value printed slowly """
        self.assertEqual(self.testing_value,
        print_something_slowly(
            'Something to test',
            5))

if __name__ == '__main__':
    TextTestRunner(
        verbosity=0).run(
            TestLoader().loadTestsFromTestCase(
                Testing_Something
            )
        )
from unittest import TestCase, TestLoader, TextTestRunner
from  simple_functions import (
    print_something, 
    print_something_heavily)
from time import time, sleep
from psutil import virtual_memory

class Testing_Something(TestCase):
    def floatMem(self, toFloat):
        """ To float memory total """
        return float(
            "%s.%s" % (
                str(toFloat)[:4],
                str(toFloat)[5:7]
            )
        )

    def setUp(self):
        """ Setting initial variables """
        self.testing_value = "Something to test"
        self.start_time = time()
        self.start_mem = virtual_memory()[1]

    def tearDown(self):
        """ To print for each unit """
        print("\33[92m %s\33[0m: %s%f Seconds\33[0m %s MB" % (
                self.id(),
                "\33[100m" if (time() - self.start_time) > 2 else "\33[7m",
                time() - self.start_time,
                # str(self.floatMem()) + ' : ' + str(self.start_mem)
                self.floatMem(self.start_mem - virtual_memory()[1])
        ))
        sleep(2)

    def test_printing_something(self):
        """ To test the value printed """
        self.assertEqual(self.testing_value,
            print_something('Something to test'))

    def test_printing_something_heavily(self):
        """ To test the value printed with memory overloading """
        self.assertEqual(self.testing_value,
        print_something_heavily(
            'Something to test',
            10000000))


if __name__ == '__main__':
    TextTestRunner(
        verbosity=0).run(
            TestLoader().loadTestsFromTestCase(
                Testing_Something
            )
        )
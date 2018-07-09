from unittest import TestCase, main
from  simple_functions import print_something

class Testing_Something(TestCase):
    def setUp(self):
        """ Setting initial variables """
        self.testing_value = "Something to test"

    def test_printing_something(self):
        """ To test the value printed """
        self.assertEqual(self.testing_value,
            print_something('Something to test'))

if __name__ == '__main__':
    main()
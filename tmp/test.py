# unit tests
#    + doc: https://docs.python.org/3/library/unittest.html 

import unittest

# personal packages
import test_example
import test_data

def test_run_all(sefl):
    tests: unittest.suite.TestSuite = unittest.TestLoader.discover("src/test")

    results: unittest.TestResult()

    tests.run(results)
    return results



if __name__ == '__main__':
    unittest.main()
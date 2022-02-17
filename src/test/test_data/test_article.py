import unittest

# personal imports
from journals2data import data

class TestSource(unittest.TestCase):

    def test___str__(self):
        test_source: data.Source = data.Source(
            'a', 'b', "c", None
        )
        expected_str: str = """
        {"url": "a", "language": "b", "scrap_frequency": "c", "output_filepath": "None"}
        """
        self.assertEqual(
            str(test_source), expected_str
        )
    
    

if __name__ == '__main__':
    unittest.main()

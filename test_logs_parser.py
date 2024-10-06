from logs_parser import parse_log_file , parse_mapping_file , write_tag_count , write_combination_count
from unittest.mock import patch
import unittest



# I have added just a few test cases.

class TestLogParserFunction(unittest.TestCase):


    def test_nonexistent_file_exception(self):
        with self.assertRaises(RuntimeError) as context:
            parse_log_file('invalid_log.txt', {})



class TestMappingParserFunction(unittest.TestCase):

    def test_nonexistent_file_exception(self):
        with self.assertRaises(RuntimeError) as context:
            parse_mapping_file('invalid_log.txt')


class TestWriteTagCountFunction(unittest.TestCase):

    def test_nonexistent_file_exception(self):
        with self.assertRaises(RuntimeError) as context:
            write_tag_count('/invalid_path/test_output.txt', {})


class TestWriteCombinationCountFunction(unittest.TestCase):

    def test_nonexistent_file_exception(self):
        with self.assertRaises(RuntimeError) as context:
            write_combination_count('/invalid_path/test_output.txt', {})


if __name__ == "__main__":
    unittest.main()

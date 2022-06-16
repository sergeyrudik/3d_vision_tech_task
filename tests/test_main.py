import unittest

from main import main


class TestMain(unittest.TestCase):

    def test_main_shorter_25(self):
        """
        test string shorter than 25 characters
        """
        test_string = 'string shorter than 25'
        result = main(article=test_string)

        self.assertIsInstance(result, str)
        self.assertEqual(result, test_string)

    def test_main_longer_25(self):
        """
        test string longer than 25 characters and dots at the new title
        """
        result = main(article='string longer than 25 characters')

        self.assertIsInstance(result, str)
        self.assertTrue(result.endswith('...'))
        self.assertEqual(result, 'string longer than 25...')

    def test_main_check_letter_or_not_space_at_the_end(self):
        """
        test string shorter than 25 characters and not space at the end
        """
        test_string = 'string shorter than 25'
        result = main(article=test_string)

        self.assertIsInstance(result, str)
        self.assertTrue(result.endswith('25'))
        self.assertFalse(result.endswith(' '))
        self.assertEqual(result, test_string)

    def test_main_input_int(self):
        """
        test with input int to article
        """
        with self.assertRaises(TypeError):
            main(article=123)

    def test_main_input_bool(self):
        """
        test with input bool to article
        """
        with self.assertRaises(TypeError):
            main(article=True)

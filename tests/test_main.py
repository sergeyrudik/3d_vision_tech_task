import unittest

from main import main


class TestMain(unittest.TestCase):

    def test_main_shorter_25(self):
        result = main(article='string shorter than 25')

        self.assertIsInstance(result, str)
        self.assertEqual(result, 'string shorter than 25')

    def test_main_longer_25(self):
        result = main(article='string longer than 25 characters')

        self.assertIsInstance(result, str)
        self.assertEqual(result, 'string longer than 25...')

    def test_main_check_dots_at_the_end(self):
        result = main(article='string longer than 25 characters and dots')

        self.assertIsInstance(result, str)
        self.assertTrue(result.endswith('...'))
        self.assertEqual(result, 'string longer than 25...')

    def test_main_check_letter_or_not_space_at_the_end(self):
        result = main(article='string shorter than 25')

        self.assertIsInstance(result, str)
        self.assertTrue(result.endswith('25'))
        self.assertFalse(result.endswith(' '))
        self.assertEqual(result, 'string shorter than 25')

    def test_main_input_int(self):
        with self.assertRaises(TypeError):
            main(article=123)

    def test_main_input_bool(self):
        with self.assertRaises(TypeError):
            main(article=True)

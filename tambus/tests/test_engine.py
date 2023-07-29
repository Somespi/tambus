import unittest
from enginetests import TambusEngine

class TranslateTestCase(unittest.TestCase):

    def setUp(self):
        self.engine = TambusEngine()

    def test_translate_with_variables(self):
        content = "Hello, {name}!"
        kwargs = {"name": "John"}
        expected_result = "Hello, John!"
        result = self.engine.translate(content, kwargs)
        self.assertEqual(result, expected_result)

    def test_translate_expressions(self):
        content = "The result is {result[0]}"
        kwargs = {"result": [42, 43,22, 23]}
        expected_result = "The result is 42"
        result = self.engine.translate(content, kwargs)
        self.assertEqual(result, expected_result)

    def test_translate_if(self):
        content = "{#if condition} True {/if}"
        kwargs = {"condition": True}
        expected_result = " True "
        result = self.engine.translate(content, kwargs)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
import unittest
from analyzer import CodeAnalyzer


class TestCodeAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = CodeAnalyzer()

    def test_valid_python_code(self):
        code = """
def calculate_sum():
    '''Calculate two numbers.'''
    return 10 + 20
"""
        result = self.analyzer.analyze(code)
        self.assertEqual(result, [])

    def test_missing_docstring(self):
        code = """
def calculate_sum():
    return 10 + 20
"""
        result = self.analyzer.analyze(code)
        self.assertTrue(
            any(issue["type"] == "Documentation" for issue in result)
        )

    def test_bare_except(self):
        code = """
def calculate():
    try:
        return 10
    except:
        return None
"""
        result = self.analyzer.analyze(code)
        self.assertTrue(
            any(issue["type"] == "Code Quality" for issue in result)
        )

    def test_syntax_error(self):
        code = "def calculate(:"
        result = self.analyzer.analyze(code)
        self.assertEqual(result[0]["type"], "Syntax Error")


if __name__ == "__main__":
    unittest.main()

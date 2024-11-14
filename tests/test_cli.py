import unittest
from cli import matrix_output_preprocess


class TestMatrixOutputPreprocess(unittest.TestCase):
    def test_empty_matrix(self):
        matrix = []
        expected_output = ""
        self.assertEqual(matrix_output_preprocess(matrix), expected_output)

    def test_single_element_matrix(self):
        matrix = [[1]]
        expected_output = "   1\nA   1"
        self.assertEqual(matrix_output_preprocess(matrix), expected_output)

    def test_single_row_matrix(self):
        matrix = [[1, 2, 3]]
        expected_output = "   1  2  3\nA   1  2  3"
        self.assertEqual(matrix_output_preprocess(matrix), expected_output)

    def test_single_column_matrix(self):
        matrix = [[1], [2], [3]]
        expected_output = "   1\nA   1\nB   2\nC   3"
        self.assertEqual(matrix_output_preprocess(matrix), expected_output)

    def test_multiple_rows_and_columns_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = "   1  2  3\nA   1  2  3\nB   4  5  6\nC   7  8  9"
        self.assertEqual(matrix_output_preprocess(matrix), expected_output)


if __name__ == "__main__":
    unittest.main()

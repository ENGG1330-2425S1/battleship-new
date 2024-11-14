import unittest
from unittest.mock import patch
from game_logic.helper import (
    validate_direction_input,
    process_position_input,
    create_position_array,
    handle_position_input,
    dict_find_key_by_value,
)


class TestHelperFunctions(unittest.TestCase):

    def test_validate_direction_input(self):
        self.assertEqual(validate_direction_input("H"), (True, None))
        self.assertEqual(validate_direction_input("V"), (True, None))
        self.assertEqual(
            validate_direction_input("X"), (False, "Warning: Invalid direction.")
        )

    def test_process_position_input_valid(self):
        matrix = [[0] * 5 for _ in range(5)]
        self.assertEqual(process_position_input("A1", matrix), ((0, 0), None))
        self.assertEqual(process_position_input("B2", matrix), ((1, 1), None))

    def test_process_position_input_invalid(self):
        matrix = [[0] * 5 for _ in range(5)]
        self.assertEqual(
            process_position_input("Z1", matrix),
            (None, "Warning: Position out of bounds."),
        )
        self.assertEqual(
            process_position_input("A6", matrix),
            (None, "Warning: Position out of bounds."),
        )
        self.assertEqual(
            process_position_input("1A", matrix), (None, "Warning: Invalid position.")
        )

    def test_create_position_array(self):
        matrix = [[0] * 3 for _ in range(3)]
        expected_positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.assertEqual(create_position_array(matrix), expected_positions)

    def test_handle_position_input(self):
        matrix = [[0] * 5 for _ in range(5)]
        self.assertEqual(handle_position_input("A1", matrix), (0, 0))
        self.assertEqual(handle_position_input("B2", matrix), (1, 1))
        self.assertIsNone(handle_position_input("Z1", matrix))
        self.assertIsNone(handle_position_input("A6", matrix))
        self.assertIsNone(handle_position_input("1A", matrix))

    def test_dict_find_key_by_value(self):
        dictionary = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(dict_find_key_by_value(dictionary, 2), "b")
        self.assertIsNone(dict_find_key_by_value(dictionary, 4))


if __name__ == "__main__":
    unittest.main()

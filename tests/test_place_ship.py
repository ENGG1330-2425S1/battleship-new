import unittest
from constants import ships, ship_labels
from unittest.mock import patch
from game_logic.place_ship import (
    handle_place_ships,
    random_place_ship,
    user_place_ships,
)


class TestPlaceShip(unittest.TestCase):
    def setUp(self):
        self.matrix = [["~"] * 10 for _ in range(10)]

    def test_handle_place_ships_horizontal_success(self):
        matrix, error = handle_place_ships(self.matrix, "destroyer", "H", 0, 0)
        self.assertIsNone(error)
        self.assertEqual(matrix[0][0], ship_labels["destroyer"])
        self.assertEqual(matrix[0][1], ship_labels["destroyer"])

    def test_handle_place_ships_vertical_success(self):
        matrix, error = handle_place_ships(self.matrix, "destroyer", "V", 0, 0)
        self.assertIsNone(error)
        self.assertEqual(matrix[0][0], ship_labels["destroyer"])
        self.assertEqual(matrix[1][0], ship_labels["destroyer"])

    def test_handle_place_ships_horizontal_out_of_bounds(self):
        matrix, error = handle_place_ships(self.matrix, "destroyer", "H", 0, 9)
        self.assertEqual(error, "Warning: Ship placement is out of horizontal bounds.")

    def test_handle_place_ships_vertical_out_of_bounds(self):
        matrix, error = handle_place_ships(self.matrix, "destroyer", "V", 9, 0)
        self.assertEqual(error, "Warning: Ship placement is out of vertical bounds.")

    def test_handle_place_ships_position_occupied(self):
        self.matrix[0][0] = ship_labels["destroyer"]
        matrix, error = handle_place_ships(self.matrix, "submarine", "H", 0, 0)
        self.assertEqual(error, f"Warning: Position already occupied by destroyer.")

    def test_random_place_ship(self):
        matrix = random_place_ship(self.matrix)
        ship_positions = sum(row.count(ship_labels["destroyer"]) for row in matrix)
        self.assertEqual(ship_positions, ships["destroyer"])


if __name__ == "__main__":
    unittest.main()

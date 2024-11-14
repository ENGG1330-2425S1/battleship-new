import unittest
from game_logic.battle import (
    attack,
    merge_grids,
    check_win,
    get_attacked_positions,
)


class TestBattle(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            ["~", "~", "~", "~"],
            ["~", "A", "~", "~"],
            ["~", "~", "B", "~"],
            ["~", "~", "~", "~"],
        ]
        self.hitted_matrix = [
            ["~", "~", "~", "~"],
            ["~", "~", "~", "~"],
            ["~", "~", "~", "~"],
            ["~", "~", "~", "~"],
        ]

    def test_attack_hit(self):
        matrix, hitted_matrix, result, message = attack(
            1, 1, self.matrix, self.hitted_matrix
        )
        self.assertTrue(result)
        self.assertEqual(hitted_matrix[1][1], "X")
        self.assertIn("hit a ship", message)

    def test_attack_miss(self):
        matrix, hitted_matrix, result, message = attack(
            0, 0, self.matrix, self.hitted_matrix
        )
        self.assertTrue(result)
        self.assertEqual(hitted_matrix[0][0], "O")
        self.assertIn("missed", message)

    def test_attack_already_attacked(self):
        self.hitted_matrix[0][0] = "X"
        matrix, hitted_matrix, result, message = attack(
            0, 0, self.matrix, self.hitted_matrix
        )
        self.assertFalse(result)
        self.assertIn("already attacked", message)

    def test_merge_grids(self):
        matrix2 = [
            ["~", "~", "~", "~"],
            ["~", "A", "~", "~"],
            ["~", "~", "B", "~"],
            ["~", "~", "~", "~"],
        ]
        hitted_matrix = [
            ["~", "~", "~", "~"],
            ["~", "X", "~", "~"],
            ["~", "~", "~", "~"],
            ["~", "~", "~", "~"],
        ]
        merged = merge_grids(hitted_matrix, matrix2)
        self.assertEqual(merged[1][1], "X")
        self.assertEqual(merged[2][2], "B")

    def test_check_win(self):
        matrix = [
            ["~", "~", "~", "~"],
            ["~", "~", "~", "~"],
            ["~", "~", "~", "~"],
            ["~", "~", "~", "~"],
        ]
        self.assertTrue(check_win(matrix))

        matrix[1][1] = "A"
        self.assertFalse(check_win(matrix))

    def test_get_attacked_positions(self):
        self.hitted_matrix[0][0] = "X"
        self.hitted_matrix[1][1] = "O"
        attacked_positions = get_attacked_positions(self.hitted_matrix)
        self.assertIn("A1", attacked_positions)
        self.assertIn("B2", attacked_positions)


if __name__ == "__main__":
    unittest.main()

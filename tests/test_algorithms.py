import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

import unittest

from core.map_loader import load_city_map
from algorithms.bfs import bfs
from algorithms.ucs import ucs
from algorithms.greedy import greedy_best_first_search
from algorithms.astar import a_star


class TestSmartRouteAlgorithms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.city = load_city_map("data/city_map.json")

        cls.heuristic = {
            "A": 8,
            "B": 6,
            "C": 7,
            "D": 4,
            "E": 5,
            "F": 2,
            "G": 0
        }

    def test_bfs(self):
        result = bfs(
            self.city,
            "A",
            "G"
        )

        self.assertEqual(
            result["status"],
            "success"
        )

        self.assertEqual(
            result["route"][0],
            "A"
        )

        self.assertEqual(
            result["route"][-1],
            "G"
        )

    def test_ucs(self):
        result = ucs(
            self.city,
            "A",
            "G"
        )

        self.assertEqual(
            result["status"],
            "success"
        )

        self.assertGreater(
            result["cost"],
            0
        )

    def test_greedy(self):
        result = greedy_best_first_search(
            self.city,
            "A",
            "G",
            self.heuristic
        )

        self.assertEqual(
            result["status"],
            "success"
        )

        self.assertEqual(
            result["route"][0],
            "A"
        )

        self.assertEqual(
            result["route"][-1],
            "G"
        )

    def test_astar(self):
        result = a_star(
            self.city,
            "A",
            "G",
            self.heuristic
        )

        self.assertEqual(
            result["status"],
            "success"
        )

        self.assertEqual(
            result["route"][0],
            "A"
        )

        self.assertEqual(
            result["route"][-1],
            "G"
        )

    def test_invalid_source(self):
        with self.assertRaises(KeyError):
            bfs(
                self.city,
                "X",
                "G"
            )

    def test_same_source_destination(self):
        result = bfs(
            self.city,
            "A",
            "A"
        )

        self.assertEqual(
            result["status"],
            "success"
        )

        self.assertEqual(
            result["route"],
            ["A"]
        )


if __name__ == "__main__":
    unittest.main()
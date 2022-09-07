import unittest
from wall_follower import WallFollower as solve

class TestWallFollower(unittest.TestCase):

    def setUp(self):
        self.maze = []
        self.marked = []

    def test_init(self):
        length_maze = len(self.maze)
        length_marked = len(self.marked)
        self.assertEqual(length_maze, length_marked)

    def test_check_south(self):
        pass

    def test_check_north(self):
        pass

    def test_check_east(self):
        pass

    def test_check_west(self):
        pass


if __name__ == "__main__":
    unittest.main()
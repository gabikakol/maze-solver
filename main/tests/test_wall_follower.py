import unittest
from wall_follower import WallFollower as solve

class TestWallFollower(unittest.TestCase):

    def setUp(self):

        self.maze = [
            ['#', '.', '#', '#', '#', '#'], 
            ['#', '.', '.', '.', '.', '#'], 
            ['#', '#', '.', '#', '.', '#'], 
            ['#', '#', '.', '#', '#', '#'], 
            ['#', '.', '.', '.', '.', '#'], 
            ['#', '#', '.', '#', '.', '#'], 
            ['#', '#', '.', '#', '#', '#']]

        self.marked = [
            ['#', 1, '#', '#', '#', '#'], 
            ['#', 1, 2, 2, 2, '#'], 
            ['#', '#', 1, '#', 3, '#'], 
            ['#', '#', 1, '#', '#', '#'], 
            ['#', 0, 2, 2, 2, '#'], 
            ['#', '#', 1, '#', 3, '#'], 
            ['#', '#', 1, '#', '#', '#']]

        self.steps = [
            [0, 1, 'S'], [1, 1, 'S'], [1, 2, 'E'], 
            [1, 3, 'E'], [1, 4, 'E'], [2, 4, 'S'], 
            [2, 4, 'N'], [2, 4, 'N'], [1, 4, 'N'], 
            [1, 3, 'W'], [1, 2, 'W'], [2, 2, 'S'], 
            [3, 2, 'S'], [4, 2, 'S'], [4, 3, 'E'], 
            [4, 4, 'E'], [5, 4, 'S'], [5, 4, 'N'], 
            [5, 4, 'N'], [4, 4, 'N'], [4, 3, 'W'], 
            [4, 2, 'W'], [5, 2, 'S'], [6, 2, 'S']]


    def test_init(self):

        length_maze = len(self.maze)
        length_marked = len(self.marked)
        self.assertEqual(length_maze, length_marked)


    def test_check_south(self):

        path = solve.check_south(self,2,2)
        self.assertEqual(len(path),3)

        path2 = [3,2,"S"]
        self.assertEqual(path, path2)


    def test_check_north(self):

        path = solve.check_north(self,2,4)
        self.assertEqual(len(path),3)

        path2 = [1,4,"N"]
        self.assertEqual(path,path2)


    def test_check_east(self):

        path = solve.check_east(self,1,3)
        self.assertEqual(len(path),3)

        path2 = [1,4,"E"]
        self.assertEqual(path,path2)


    def test_check_west(self):

        path = solve.check_west(self,4,5)
        self.assertEqual(len(path), 3)
        
        path2 = [4,4,"W"]
        self.assertEqual(path,path2)


if __name__ == "__main__":
    unittest.main()
import unittest
from generate_maze import GenerateMaze as maze

class TestGenerate(unittest.TestCase):

    def test_init_start_point(self):
        list = [[3,3], [10,15], [67,98]]
        for i in range(len(list)):
            sublist = list[i]
            self.width, self.height = sublist[0], sublist[-1]
            coord = maze.init_start_point(self)
            x, y = coord[0], coord[-1]
            x_bool = True if 1<=x<=self.width-2 else False
            y_bool = True if 1<=x<=self.height-2 else False
            self.assertTrue(x_bool)
            self.assertTrue(y_bool)

    def setUp(self):
        self.maze = [["#",".","#","#"],[".",".",".","#"],["#",".","#","."], [".",".","#","."]]
        self.walls = [[0,1]]

    def test_upper_wall(self):
        maze.upper_wall(self, 2+1, 2)
        self.assertEqual(self.maze[2][2], "#")
        self.assertEqual(self.walls[-1], [2, 2])
        maze.upper_wall(self, 0+1, 1)
        self.assertEqual(self.maze[1][0], ".")
        self.assertEqual(self.walls[0], [0,1])

    def test_bottom_wall(self):
        maze.bottom_wall(self, 2-1, 2)
        self.assertEqual(self.maze[2][2], "#")
        self.assertEqual(self.walls[-1], [2, 2])
        maze.bottom_wall(self, 0-1, 1)
        self.assertEqual(self.maze[1][0], ".")
        self.assertEqual(self.walls[0], [0,1])

    def test_left_wall(self):
        maze.left_wall(self, 2, 2+1)
        self.assertEqual(self.maze[2][2], "#")
        self.assertEqual(self.walls[-1], [2, 2])
        maze.left_wall(self, 0, 1+1)
        self.assertEqual(self.maze[1][0], ".")
        self.assertEqual(self.walls[0], [0,1])

    def test_right_wall(self):
        maze.right_wall(self, 2, 2-1)
        self.assertEqual(self.maze[2][2], "#")
        self.assertEqual(self.walls[-1], [2, 2])
        maze.right_wall(self, 0, 1-1)
        self.assertEqual(self.maze[1][0], ".")
        self.assertEqual(self.walls[0], [0,1])

    def test_count_cells_around(self):
        counter = maze.count_cells_around(self, [2,2])
        cell=self.maze[2][2]
        self.assertEqual(counter,3)
        self.assertNotEqual(cell, ".")

    def test_remove_wall(self):
        self.walls = [[1,1], [55,3], [97,22]]
        random_wall = [2,3]
        maze.remove_wall(self, random_wall)
        self.assertEqual(self.walls, [[1,1], [55,3], [97,22]])
        random_wall = [55,3]
        maze.remove_wall(self, random_wall)
        self.assertEqual(self.walls, [[1,1],[97,22]])

    def test_entrance_exit(self):
        self.width, self.height = 3,4
        maze.entrance_exit(self)
        entrance_bool = True if 0<=self.entrance<=2 else False
        exit_bool = True if 0<=self.exit<=2 else False
        self.assertTrue(entrance_bool)
        self.assertTrue(exit_bool)

if __name__ == "__main__":
    unittest.main()

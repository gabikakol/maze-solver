import unittest
from tremaux import Tremaux as solve

class TestFind(unittest.TestCase):

    def setUp(self):

        self.marked = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.walkable = [[".",".","x","."],[".","x","x","."],["x",".",".","."],["x",".",".","x"],[".","x",".","x"]]
        self.moves = {(0, 0): 'from_left', (0, 1): 'from_bottom', (0, 2): 'from_right', (0, 3): 'from_top', 
        (1, 0): 'from_top', (1, 1): 'from_bottom', (1, 2): 'from_bottom', (1, 3): 'from_left', 
        (2, 0): 'from_left', (2, 1): 'from_top', (2, 2): 'from_top', (2, 3): 'from_top', 
        (3, 0): 'from_bottom', (3, 1): 'from_bottom', (3, 2): 'from_left', (3, 3): 'from_bottom'}
    

    def test_init(self):

        length_marked = len(self.marked)
        length_walkable = len(self.walkable)
        self.assertEqual(length_marked, length_walkable)


    def test_junction_from_top(self):

        next_move = solve.junction_from_top(self,2,2)
        self.assertEqual(next_move,('from_top', 3, 2))
        self.assertNotEqual(2,len(self.walkable)-1)

        row,column=0,2
        next_move = solve.junction_from_top(self,row,column)
        self.assertEqual(next_move,('from_left', 0, 3))
        self.assertNotEqual(column,len(self.walkable[0]))

        row,column=0,1
        next_move = solve.junction_from_top(self,row,column)
        self.assertEqual(next_move,('from_right', 0, 0))
        self.assertNotEqual(column,0)


    def test_junction_from_left(self):

        next_move = solve.junction_from_left(self,0,0)
        self.assertEqual(next_move,('from_top', 1, 0))
        self.assertNotEqual(1, len(self.walkable)-1)

        row,column=3,1
        next_move = solve.junction_from_left(self,row,column)
        self.assertEqual(next_move,('from_left', 3, 2))
        self.assertNotEqual(row,len(self.walkable[0]))

        row,column=2,3
        next_move = solve.junction_from_left(self,row,column)
        self.assertEqual(next_move,('from_bottom', 1, 3))
        self.assertNotEqual(row,0)

        
    def test_junction_from_right(self):
        
        next_move = solve.junction_from_right(self,1,1)
        self.assertEqual(next_move,('from_top',2,1))
        self.assertNotEqual(1,len(self.walkable)-1)

        row,column=2,3
        next_move = solve.junction_from_right(self,row,column)
        self.assertNotEqual(column,0)
        self.assertEqual(next_move,('from_right',2,2))

        row,column=2,0
        next_move = solve.junction_from_right(self,row,column)
        self.assertEqual(next_move,('from_bottom',1,0))
        self.assertNotEqual(row,0)
        

    def test_junction_from_bottom(self):

        next_move = solve.junction_from_bottom(self,2,0)
        self.assertEqual(next_move,('from_left', 2, 1))
        self.assertNotEqual(2,len(self.walkable)-1)
        
        row,column=3,2
        next_move = solve.junction_from_bottom(self,row,column)
        self.assertEqual(next_move,('from_right', 3, 1))
        self.assertNotEqual(column,0)

        row,column=1,0
        next_move = solve.junction_from_bottom(self,row,column)   
        self.assertEqual(next_move,('from_bottom', 0, 0))   
        self.assertNotEqual(row,0)  


    def test_scan_for_exit(self):

        self.exit = 3
        exit = solve.scan_for_exit(self,4,3)
        self.assertTrue(exit)
        self.assertEqual(self.marked[4][3],1)

        exit = solve.scan_for_exit(self,2,1)
        self.assertFalse(exit)
        self.assertEqual(self.marked[2][1],0)

           
    def test_return_to_junction(self):

        row,column=2,1
        next_move = solve.return_to_junction(self,"from_top",row,column)
        self.assertEqual(next_move, ('from_bottom', 1, 1))
        self.assertNotEqual(row,0)

        next_move = solve.return_to_junction(self,"from_right",0,0)
        self.assertEqual(next_move, ('from_bottom', 0, 1))

        row,column = 0,0
        direction = self.moves[(row,column)]
        self.assertEqual(direction, "from_left")

        row, column = 2,1
        direction = self.moves[(row, column)]
        self.assertEqual(direction, "from_top")

        row,column = 3,1
        direction = self.moves[(row,column)]
        self.assertEqual(direction, "from_bottom")

        row,column = 0,2
        direction = self.moves[(row,column)]
        self.assertEqual(direction, "from_right")
        
        
if __name__ == "__main__":
    unittest.main()
import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer

########## TEST ##########
class MonteCarloTestSuite(unittest.TestCase):
    def test_01_die_init(self):
        # create instance
        dieA = Die(np.array([1,2,3,4,5,6]))
        
        message = "'weights' should be instance of np.ndarray"
        self.assertIsInstance(dieA.weights, np.ndarray, message)
    
    def test_02_chng_wght(self):
        # create instance
        dieA = Die(np.array([1,2,3,4,5,6]))
        before_l = len(dieA.weights.copy())
        before = dieA.weights.copy()
        dieA.chng_wght(4,2)
        after_l = len(dieA.weights)
        after = dieA.weights

        self.assertEqual(before_l, after_l, "length of 'weights' should remain constant")
        self.assertFalse(np.array_equal(before, after), "'weights' should change after calling method 'chng_wght'")
    
    def test_03_roll_die(self):
        # create instance
        dieA = Die(np.array([1,2,3,4,5,6]))

        message = "method should return a list"
        self.assertIsInstance(dieA.roll_die(), list, message)
    
    def test_04_dataframe(self):
        # create instance
        dieA = Die(np.array([1,2,3,4,5,6]))

        message = "method should return a pd.DataFrame"
        self.assertIsInstance(dieA.dataframe(), pd.DataFrame, message)
    
    def test_05_game_init(self):
        # create instances
        dieA = Die(np.array([1,2,3,4,5,6]))
        dieB = Die(np.array([1,2,3,4,5,6]))
        dieA.chng_wght(3,4)
        dieB.chng_wght(4,3)
        dice=[dieA, dieB]
        game = Game(dice)

        message = "'dice' should be instance of list"
        self.assertIsInstance(game.dice, list, message)
    
    def test_06_play(self):
        # create instances
        dieA = Die(np.array([1,2,3,4,5,6]))
        dieB = Die(np.array([1,2,3,4,5,6]))
        dieA.chng_wght(3,4)
        dieB.chng_wght(4,3)
        dice=[dieA, dieB]
        game = Game(dice)
        game.play(10)

        message = "'__df2' should be instance of pd.DataFrame"
        self.assertIsInstance(game._Game__df2, pd.DataFrame, message)
    
    def test_07_play_results(self):
        # create instances
        dieA = Die(np.array([1,2,3,4,5,6]))
        dieB = Die(np.array([1,2,3,4,5,6]))
        dieA.chng_wght(3,4)
        dieB.chng_wght(4,3)
        dice=[dieA, dieB]
        game = Game(dice)
        game.play(10)
        
        message = "method should return a pd.DataFrame"
        self.assertIsInstance(game.play_results(), pd.DataFrame, message)
    
    def test_08_analyzer_init(self):
        # create instances
        dieA = Die(np.array([1,2,3,4,5,6]))
        dieB = Die(np.array([1,2,3,4,5,6]))
        dieA.chng_wght(3,4)
        dieB.chng_wght(4,3)
        dice=[dieA, dieB]
        game = Game(dice)
        game.play(10)
        analyzed = Analyzer(game)

        message = "'play_results' should instance of a pd.DataFrame"
        self.assertIsInstance(analyzed.play_results, pd.DataFrame, message)
    
    def test_09_jackpot(self):
        # create instances
        dieA = Die(np.array([1,2,3,4,5,6]))
        dieB = Die(np.array([1,2,3,4,5,6]))
        dieA.chng_wght(3,4)
        dieB.chng_wght(4,3)
        dice=[dieA, dieB]
        game = Game(dice)
        game.play(10)
        analyzed = Analyzer(game)

        message = "method should return an int"
        self.assertIsInstance(analyzed.jackpot(), int, message)
    
    def test_10_face_count(self):
        # create instances
        dieA = Die(np.array([1,2,3,4,5,6]))
        dieB = Die(np.array([1,2,3,4,5,6]))
        dieA.chng_wght(3,4)
        dieB.chng_wght(4,3)
        dice=[dieA, dieB]
        game = Game(dice)
        game.play(10)
        analyzed = Analyzer(game)

        message = "method should return a pd.DataFrame"
        self.assertIsInstance(analyzed.face_count(), pd.DataFrame, message)
    
    def test_11_combo_count(self):
        # create instances
        dieA = Die(np.array([1,2,3,4,5,6]))
        dieB = Die(np.array([1,2,3,4,5,6]))
        dieA.chng_wght(3,4)
        dieB.chng_wght(4,3)
        dice=[dieA, dieB]
        game = Game(dice)
        game.play(10)
        analyzed = Analyzer(game)

        message = "method should return a pd.DataFrame"
        self.assertIsInstance(analyzed.combo_count(), pd.DataFrame, message)

    def test_12_perm_count(self):
        # create instances
        dieA = Die(np.array([1,2,3,4,5,6]))
        dieB = Die(np.array([1,2,3,4,5,6]))
        dieA.chng_wght(3,4)
        dieB.chng_wght(4,3)
        dice=[dieA, dieB]
        game = Game(dice)
        game.play(10)
        analyzed = Analyzer(game)

        message = "method should return a pd.DataFrame"
        self.assertIsInstance(analyzed.perm_count(), pd.DataFrame, message)

########## Run TEST ##########
if __name__ == '__main__':
    unittest.main(verbosity=3)
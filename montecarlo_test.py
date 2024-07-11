import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    def test_01_die_init(self):
        dieA = Die(np.array([1,2,3,4,5,6]))
        actual = type(dieA.weights) 
        expected = np.ndarray
        self.assertEqual(actual, expected)
    
    def test_02_chng_wght(self):
        dieA = Die(np.array([1,2,3,4,5,6]))
        before_l = len(dieA.weights.copy())
        before = dieA.weights.copy()
        dieA.chng_wght(4,2)
        after_l = len(dieA.weights)
        after = dieA.weights

        self.assertEqual(before_l, after_l, 'length of weights should remain constant')
        self.assertFalse(np.array_equal(before, after), 'weights array should change')
    
    def test_03_roll_die(self):
        dieA = Die(np.array([1,2,3,4,5,6]))
        
    
    def test_04_dataframe(self):
        pass
    
    def test_05_game_init(self):
        pass
    
    def test_06_play(self):
        pass
    
    def test_07_play_results(self):
        pass
    
    def test_08_analyzer_init(self):
        pass
    
    def test_09_jackpot(self):
        pass
    
    def test_10_face_count(self):
        pass
    
    def test_11_combo_count(self):
        pass
    
    def test_12_perm_count(self):
        pass




if __name__ == '__main__':
    unittest.main(verbosity=3)
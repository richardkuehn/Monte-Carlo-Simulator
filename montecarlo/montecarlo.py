import numpy as np
import pandas as pd

# Class 'Die'
class Die:
    '''
    TO DO: insert docstring here
    '''
    # init
    def __init__(self, faces):
        # check if numpy array
        if not isinstance(faces, np.ndarray):
            raise TypeError("'faces' argument must be numpy array")
        
        # check if integers or strings
        if faces.dtype not in (np.int32, np.int64, np.dtype('U')):
            raise TypeError("'faces' argument must contain integers or strings")
        
        # check if unique values
        if not (len(faces) == len(np.unique(faces))):
            raise TypeError("'faces' argument must contain unique values")
        
        # assign variable
        self.faces = faces

        # assign weights
        self.weights = np.ones(len(faces))
        
        # create private df
        self.__df = pd.DataFrame(self.weights, index=self.faces, columns=['weights'])
        self.__df.index.name = 'faces'

    # method 1: change weights
    def chng_wght(self, face_val, new_wght):
        # check for 'face_val' in __df
        if face_val not in self.__df.index:
            raise IndexError(f"'face_val' argument must be between {self.__df.index[0]} and {self.__df.index[-1]}")
        
        # check for int, float, or castable str
        if isinstance(new_wght, (int, float)):
            pass
        elif isinstance(new_wght, str):
            try: new_wght = float(new_wght)
            except ValueError: 
                raise TypeError("'new_wght' argument must be data type 'int', 'float', or castable 'str'") 
        
        # update __df with 'new_wght'
        self.__df.loc[face_val,'weights'] = new_wght
        self.weights = self.__df['weights'].values

        # inform of change
        return(f"face value '{face_val}' has been given new weight '{new_wght}'")

    # method 2: roll die one or more times
    def roll_die(self, rolls=1):
        # check 'rolls' is int and greater than 1
        if not isinstance(rolls, int) or rolls < 1:
            raise ValueError("'rolls' must be an integer greater than 0")
        
        # return result of rolls
        normalized = self.weights / self.weights.sum()
        return np.random.choice(self.faces, size=rolls, p=(normalized))

    # method 3: show die's current state: returns copy of private die dataframe
    def dataframe(self):
        return self.__df

##########################
# # checking work for CLASS DIE    
# die = Die(np.array([1,2,3,4,5,6]))
# die.faces
# die.weights

# die.chng_wght(4, 3)
# die.weights
# die.roll(10)
# die.dataframe()

# face = np.array([1,2,3,4,5,6])
# face.dtype
# face2 = np.array(['a', 'b', 'c', 'd'])
# face2.dtype
#########################

#########################
# SETUP for CLASS GAME
# die1 = Die(np.array([1,2,3,4,5,6]))
# die2 = Die(np.array([1,2,3,4,5,6]))

# die1.chng_wght(3,4)
# die2.chng_wght(4,3)

# dice=[die1, die2]
# type(dice)
########################

class Game:
    '''
    TO DO: insert docstring
    '''
    # init
    def __init__(self, dice):
        # check if 'dice' is a list
        if not isinstance(dice, list):
            raise ValueError("'dice' must be a list")
        
        # check if 'dice' contains Die objects
        for die in dice:
            if not isinstance(die, Die):
                raise ValueError("All items in 'dice' must be instances of the Die class")
        
        # assign variable
        self.dice = dice

    # method 1: roll dice and save to private df
    def play(self, rolls):
        # check if integer
        if type(rolls) != int:
            raise ValueError("'rolls' must be an integer")
        
        # create empty df with index from 1 to rolls
        self.__df2 = pd.DataFrame(index = range(1, rolls + 1))
        self.__df2.index.name = 'roll #'
        
        # iterate roll_die over dice
        # this needs to be making the columns using the name of the die
        for i, x in enumerate(self.dice, start = 1):
            self.__df2[f'die{i}'] = x.roll_die(rolls)

    # method 2: results of .play
    def play_results(self, form = 'wide'):
        if form not in ('wide', 'narrow'):
            raise ValueError("'form' must equal 'wide' or 'narrow'")
        if (form == 'wide'):
            return self.__df2
        if (form == 'narrow'):
            return self.__df2.stack()


#############################
# checking work for CLASS GAME
# game = Game(dice)
# game.play(4)
# game.play_results()
# game.play_results(form='narrow')
#############################

# set up for CLASS ANALYZE
# dieA = Die(np.array([1,2,3,4,5,6]))
# dieB = Die(np.array([1,2,3,4,5,6]))
# dieC = Die(np.array([1,2,3,4,5,6]))

# dieA.chng_wght(3,4)
# dieB.chng_wght(4,3)
# type(dieB.weights)

# dice=[dieA, dieB, dieC]

# game = Game(dice)
# game.play(10)
# gameplay_df = game.play_results()
# gameplay_narrow = game.play_results(form='narrow')
# gameplay_df.columns
# type(gameplay_df)

class Analyzer:
    '''
    TO DO: insert docstring
    '''
    # init
    def __init__(self, game):
        # check that 'game' is Game object
        if not isinstance(game, Game):
            raise ValueError("'game' must be instance of the Game class")
        
        self.play_results = game.play_results()
        self.faces_array = game.dice[0].faces

    # method 1: jackpot where all faces are the same
    def jackpot(self):
        # add +1 to 'i' if only 1 unique value
        i = 0
        for col in self.play_results.columns:
            if self.play_results[col].nunique() == 1:
                i += 1

        # return count of 
        if i == 0: return (f'0 Jackpots :(')
        elif i == 1: return ('1 Jackpot!')
        elif i > 1: return (f'{i} Jackpots!')

    # method 2:
    def face_count(self):
        # create zeros dataframe with index = rolls and columns = faces
        counts_df = pd.DataFrame(columns=self.faces_array, index=self.play_results.index).fillna(0)
        counts_df.columns.name = 'faces_counts'

        # iterate through rows in 'self.play_results'
        for index, row in self.play_results.iterrows():
        # count occurrence of each face
            for face in row:
                counts_df.at[index, face] += 1

        # return updated df
        return counts_df

    # method 3:
    def combo_count(self):
        '''
        TO DO: insert docstring
        '''
        combos = [self.play_results.iloc[x].values.tolist() for x in range(0, len(self.play_results))]
        combo_sort = [sorted(x) for x in combos]
        df_sort = pd.DataFrame(combo_sort)
        df_sort.columns = [f'die{i}' for i in range(1, (len(df_sort.columns) + 1))]
        df3 = df_sort.value_counts(ascending=True)
        df3.columns = 'combo_counts'
        # rename column to combo_count
        return df3
        
    # method 4:
    def perm_count(self):
        # essentially combo count but order matters --> just use value_count
        # rename column to perm_counts
        perms = self.play_results.value_counts(ascending=True)
        perms.columns = 'perm_counts'
        return perms


#########################################
# check work for CLASS ANALYZER
# Analyzer Tests
# analyzed = Analyzer(game)
# analyzed.jackpot()
# analyzed.face_count()
# analyzed.combo_count()
# analyzed.perm_count()
#########################################

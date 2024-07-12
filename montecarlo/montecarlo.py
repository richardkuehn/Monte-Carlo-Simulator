import numpy as np
import pandas as pd

########## class 'Die' ##########
class Die:
    '''
    TO DO: insert docstring here
    '''
    # init
    def __init__(self, faces):
        '''
        TO DO: insert docstring here
        '''    
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
        '''
        TO DO: insert docstring here
        '''    
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
        '''
        TO DO: insert docstring here
        '''    
        # check 'rolls' is int and greater than 1
        if not isinstance(rolls, int) or rolls < 1:
            raise ValueError("'rolls' must be an integer greater than 0")
        
        # return result of rolls
        normalized = self.weights / self.weights.sum()
        return list(np.random.choice(self.faces, size=rolls, p=(normalized)))

    # method 3: show die's current state: returns copy of private die dataframe
    def dataframe(self):
        '''
        TO DO: insert docstring here
        '''    
        return self.__df


########## class 'Game' ##########
class Game:
    '''
    TO DO: insert docstring
    '''
    # init
    def __init__(self, dice):
        '''
        TO DO: insert docstring here
        '''    
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
        '''
        TO DO: insert docstring here
        '''
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
        '''
        TO DO: insert docstring here
        '''
        if form not in ('wide', 'narrow'):
            raise ValueError("'form' must equal 'wide' or 'narrow'")
        if (form == 'wide'):
            return self.__df2
        if (form == 'narrow'):
            return self.__df2.stack().to_frame(name='die value')


########## class 'Analyzer' ##########
class Analyzer:
    '''
    TO DO: insert docstring
    '''
    # init
    def __init__(self, game):
        '''
        TO DO: insert docstring here
        '''
        # check that 'game' is Game object
        if not isinstance(game, Game):
            raise ValueError("'game' must be instance of the Game class")
        
        self.play_results = game.play_results()
        self.faces_array = game.dice[0].faces

    # method 1: jackpot where all faces are the same
    def jackpot(self):
        '''
        TO DO: insert docstring here
        '''
        # add +1 to 'i' if only 1 unique value
        i = 0
        for col in self.play_results.columns:
            if self.play_results[col].nunique() == 1:
                i += 1

        # return count of 
        if i == 0: return (f'0 Jackpots :(')
        elif i == 1: return ('1 Jackpot!')
        elif i > 1: return (f'{i} Jackpots!')

    # method 2: count occurence of faces in each roll
    def face_count(self):
        '''
        TO DO: insert docstring here
        '''
        # create zeros dataframe with index = rolls and columns = faces
        counts_df = pd.DataFrame(columns=self.faces_array, index=self.play_results.index)
        counts_df = counts_df.infer_objects().fillna(0)
        counts_df.columns.name = 'faces_counts'

        # iterate through rows in 'self.play_results'
        for index, row in self.play_results.iterrows():
        # count occurrence of each face
            for face in row:
                counts_df.at[index, face] += 1

        # return updated df
        return counts_df

    # method 3: count combinations of rolls
    def combo_count(self):
        '''
        TO DO: insert docstring
        '''
        combos = [self.play_results.iloc[x].values.tolist() for x in range(0, len(self.play_results))]
        combo_sort = [sorted(x) for x in combos]
        df_sort = pd.DataFrame(combo_sort)
        df_sort.columns = [f'die{i}' for i in range(1, (len(df_sort.columns) + 1))]
        df3 = df_sort.value_counts(ascending=True)
        return df3.to_frame(name='combo_counts')
        
    # method 4: count permutations of rolls
    def perm_count(self):
        '''
        TO DO: insert docstring here
        '''
        # essentially combo count but order matters --> just use value_count
        perms = self.play_results.value_counts(ascending=True)
        return perms.to_frame(name='perm_counts')


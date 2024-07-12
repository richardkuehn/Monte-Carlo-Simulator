## Monte Carlo Simulator


#### Synopsis
This application creates three related classes ('Die', 'Game', and 'Analyzer') to simulate processes that rely on repeated random sampling. Below are the steps to install, import, and use the code to create a simulation.

##### Step 1: Install
```sh
pip install -e .
```

##### Step 2: Import
```python
from montecarlo import Die, Game, Analyzer
```

##### Step 3: Create Die
i. create 'Die' object with numpy array
```python
dieA = Die(np.array([1,2,3,4,5,6]))
```
ii. peek at attribute 'faces'
```python
dieA.faces
```
iii. peek at attribute 'weights'
```python
dieA.weights
```
iv. use method 'chng_wght' where **a** is the face and **b** is the new weight
```python
a = 4
b = 3
dieA.chng_wght(a,b)

print("new die weights:" + str(dieA.weights))
```
v. use method 'roll_die' where **x** is the number of rolls
```python
x = 10
dieA.roll_die(x)
```
vi. use method 'dataframe' to see a dataframe consisting of faces and weights
```python
dieA.dataframe()
```

##### Step 4: Create Game
i. create list 'dice' with 'Die' objects
```python
dieA = Die(np.array([1,2,3,4,5,6]))
dieB = Die(np.array([1,2,3,4,5,6])) 
dieC = Die(np.array([1,2,3,4,5,6]))

dice=[dieA, dieB, dieC] # All 'Die' objects need to have same 'faces' for 'Game'
```
ii. create 'Game' object
```python
game = Game(dice)
game.dice   # should return list of 'Die' objects
```
iii. use method 'play' where **x** is number of rolls dice and method 'play_results' to wide dataframe
```python
game.play(4)
game.play_results()
```
iv. use method 'play_results' and specify form as 'narrow' to see narrow dataframe
```python
game.play_results(form='narrow')
```

##### Step 5: Create Analyzer
i. create 'Die' objects and 'Game' object
```python
dieA = Die(np.array([1,2,3,4,5,6]))
dieB = Die(np.array([1,2,3,4,5,6]))
dieC = Die(np.array([1,2,3,4,5,6]))

dice=[dieA, dieB, dieC] # All 'Die' objects need to have same 'faces' for 'Game'
game = Game(dice)
```
ii. create 'Analyzer' object
```python
analyzed = Analyzer(game)
```
iii. use method 'jackpot' to see if any dice had all the same sides
```python
analyzed.jackpot()
```
iv. use method 'face_count' to see the faces value counts for each round of rolls
```python
analyzed.face_count()
```
v. use method 'combo_count' to see the combination counts (order independent)
```python
analyzed.combo_count()
```
v. use method 'perm_count' to see the permuation counts (order dependent)
```python
analyzed.perm_count()
```

#### API Description
***Die***


***Game***

***Analyzer***


#### About
Created by Richard 'Ricky' Kuehn from the University of Virginia. To contact, please email *fmt2tg@virginia.edu*

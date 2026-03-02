#Solution for the Challenge By Marwan Abbas: filtering the positive values from a matrix
#import numpy with the nickname np for convenience
import numpy as np
#identifying the array
matrix=np.array([ [1,-2,-3,4],
        [-23, 65, 8, -9]])
#filtering out all the positive numbers only
print(matrix[matrix>0])
#Another Method with a random array generated using random module
matrix1=np.random.default_rng().integers(low=-25,high=26,size=(2,3))
#showing the generated matrix so you can compare
print('\narray:', matrix1)
#filtering the positive elements from our array
print("\nThe positive values from your array: ",matrix1[matrix1>0] )
























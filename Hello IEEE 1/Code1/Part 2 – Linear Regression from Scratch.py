#Task_part2: Linear Regression from Scratch (Normal equation)
#Step1:calling Numpy Library and giving it a nickname (np) for convenience
import numpy as np
#Converting X(house size) and Y(price in thousands) into numpy arrays
house_size=np.array([50, 60, 80, 100, 120])  # X
price_in_thousands=np.array([150, 180, 240, 300, 330]) #Y
#reshaping X as a column vector
house_size_column=house_size.reshape(-1,1)
print("\nhouse size as a column vector: \n",house_size_column)
#adding a bias column of ones
#step1:generating a column of ones
bias=np.ones((house_size_column.shape[0],1) )
#Step2:addition
house_size_bias=np.hstack(( bias, house_size_column))
print('\nHouse Size with a bias column added: \n',house_size_bias)
#Computing the parameter vector θ using the Normal Equation:  θ = (Xᵀ X)⁻¹ Xᵀ y, 
#such that x=house_size_bias, y=price_in_thousands
#step1: Obtaining Xᵀ, i.e house_size transposed
#since python can't transpose 1d arrays so we'll use the 2d reshaped version we've created previously house_size_bias
house_size_biastranspose=house_size_bias.T
#step2: Obtaining Xᵀ X
xxt=house_size_biastranspose@house_size_bias
#step 3: obtaining (Xᵀ X)⁻¹
#mathematically, we can't find the inverse of a matrix unless we check if the determinant doesn't equal 0 , therefore
#Check determinant condition
if np.linalg.det(xxt)!=0:
    inverse_xxt=np.linalg.inv(xxt)
    print("\nThe Inverse of the bias house size: \n",inverse_xxt)
else:
    print("To find the inverse of a matrix, Its Determinant must NOT equal 0 ")
#step4:computing the parameter THETA from EQn.  Θ = (Xᵀ X)⁻¹ Xᵀ y
theta=inverse_xxt@house_size_biastranspose@price_in_thousands
print("\n Parameter θ=\n",theta.reshape((-1,1)))
#using theta to predict the price of the  house of Size 90 meters squared
#step1: formula: price=theta[0]+theta[1]*size
#step2: obtaining theta[0]:
theta_0=theta[0]
#step3: obtaining theta[1]:
theta_1=theta[1]
#price in thousands 
price=theta_0+theta_1*90
print("\nThe predicted price for a house of 90 meters squared: \n$",price," In Thousands")











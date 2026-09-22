import numpy as np
import random
import pandas as pd
#creating a 1D array:
#create a list and use np.array to convert to array

temp = [20,30,40,50,60]
temperature = np.array(temp)
print(f"The new array is {temperature}")
print(type(temperature))

#An array allows us to work on each item in the array without looping
#We can add +2 to all element in the array temperature
new_temperature = temperature+2
print(f" The new temperature is {new_temperature}")

#Mathematical(Statistical) operations in numpy
#max function
print(f"The maximum temperature is {new_temperature.max()}")
#min function
print(f"The minimum temperature is {new_temperature.min()}")
#mean function
print(f"The mean temperature is {new_temperature.mean()}")
#sum function
print(f"The sum of the temperatures is {new_temperature.sum()}")

#Generating numbers using random:
#Generating numbers given a range,use random.randint
numbers = np.random.randint(1,10,size=4)
print(f"The random generated numbers: {numbers}")
#We can generate an array with array items being zero
zero_array = np.zeros(10)
print(f"This is the zero array: {zero_array}")
#We can generate an array with items being one
one_array = np.ones(2)
print(f"The one array is: {one_array}")
#To generate numbers from 0-9
gen_numbers = np.arange(10)
print(f"Numbers from 0-9: {gen_numbers}")

#2D array 
student_grade = np.array([
    [80,90,50],
    [50,60,70],
    [10,20,30]
])
print(f"The scores for the following students are: {student_grade}")
#to find the shape of your dataset use shape method
print(f"The size of our data is a {student_grade.shape}")
#use [row,column] to access list
print(f"The first element of student 1's scores is {student_grade[0,0]}")
#use size to find total number of elements
print(f"The total elements is {student_grade.size}")

#Intro to Pandas
#Pandas is a library that is usee for database works
#It uses a data structure called dataframe similar to excel tables/sheets

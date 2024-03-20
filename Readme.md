# Data Science Mantorship Program:
### In Numpy axis = 0 means row 
### In Numpy axis = 1 means column 

digram of Aggregation( digram shape is show, which class are aggrigate)
![alt text](<Screenshot 2024-03-17 141313.png>)



inheritance digram, triangle, which class attach the triangle that is parent class and other is child class
![alt text](<Screenshot 2024-03-17 141742.png>)


# Inheritance Typs
* Single Inheritance
* Multilevel Inheritance
* Hierarchical Inheritance
* Multiple Inheritance(Diamond Problem)
* Hybrid Inheritance

## Inheritance in summary
A class can inherit from another class.

Inheritance improves code reuse

Constructor, attributes, methods get inherited to the child class

The parent has no access to the child class

Private properties of parent are not accessible directly in child class

Child class can override the attributes or methods. This is called method overriding

super() is an inbuilt function which is used to invoke the parent class methods and constructor

## multi Inheritance diagram
![alt text](<Screenshot 2024-03-18 120344.png>)

### Hiercal Inheritance diagram
![alt text](<Screenshot 2024-03-18 120838.png>)

## Polymorphism
* Method Overriding
* Method Overloading
* Operator Overloading


## What is numpy?
* NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

* At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types


### Numpy Arrays Vs Python Sequences
* NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.

* The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.

* NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

* A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.





### Spliting Digram, 
![alt text](<Screenshot 2024-03-19 193045.png>)



## Brodcasting 
*  The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.
* The smaller array is “broadcast” across the larger array so that they have compatible shapes.

#### Broadcasting Rules

**1. Make the two arrays have the same number of dimensions.**<br>
- If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.<br>


**2. Make each dimension of the two arrays the same size.**<br>
- If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
- If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.

<img src = "https://jakevdp.github.io/PythonDataScienceHandbook/figures/02.05-broadcasting.png">


### np.sort
* Return a sorted copy of an array.

* https://numpy.org/doc/stable/reference/generated/numpy.sort.html

### np.append
* The numpy.append() appends values along the mentioned axis at the end of the array

* https://numpy.org/doc/stable/reference/generated/numpy.append.html

### np.concatenate
* numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

* https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html

### np.unique
* With the help of np.unique() method, we can get the unique values from an array given as     parameter in np.unique() method.

* https://numpy.org/doc/stable/reference/generated/numpy.unique.html/



### np.expand_dims
* With the help of Numpy.expand_dims() method, we can get the expanded dimensions of an array

* https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html

### np.where
* The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.

* https://numpy.org/doc/stable/reference/generated/numpy.where.html



### np.argmax
* The numpy.argmax() function returns indices of the max element of the array in a particular axis.

* https://numpy.org/doc/stable/reference/generated/numpy.argmax.html

### np.cumsum
* numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis.

* https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html


### np.percentile
* numpy.percentile()function used to compute the nth percentile of the given data (array elements) along the specified axis.

* https://numpy.org/doc/stable/reference/generated/numpy.percentile.html


###  np.histogram
* Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.

* https://numpy.org/doc/stable/reference/generated/numpy.histogram.html




































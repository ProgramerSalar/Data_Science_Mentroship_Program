# Data Science Mantorship Program:

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
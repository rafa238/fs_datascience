"""
Created on Mon May 30 23:30:06 2022

@author: rafajl
"""

from typing import List
import math

Vector = List[float]

height_weight_age = [70,#inches
                     170, #pounds
                     40] #years

grades = [95, #exam1
          80, #exam2
          75, #exam3
          62] #exam4

def add(v: Vector, w:Vector) -> Vector:
    """Adds componenewise of two vectors"""
    assert len(v) == len(w), "Vectors are not of the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1,2,3], [4,5,6]) == [5,7,9]
 

def substract(v: Vector, w:Vector) -> Vector:
    """Substracts componenewise of two vectors"""
    assert len(v) == len(w), "Vectors are not of the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert substract([5,7,9], [4,5,6]) == [1,2,3]
 

def vector_sum(vectors: List[Vector]) -> Vector:
    """
    vector_sum: Receive a list of vector and return a list of the sum of all the
    vectors componentwise
    """
    assert vectors, "No vector provided"
    #we cheack that all the vecotors are of the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Vectors has diferent sizes"
    
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[1,2], [3,4],[5,6], [7,8]]) == [16, 20]

def scalar_multiply(c: float, vectors: List[Vector]) -> Vector:
    """Multiply every vector's elements by c"""
    return [c * v_i for v_i in vectors]

def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3,4], [5,6]]) == [3, 4]

def dot(v: Vector, w:Vector) -> float:
    """
        Measure how far is the proyecton of v above w.
        v1*w1 + v2*w2 + ... + vn*wn
    """
    assert len(v) == len(w), "vectors has different lenght"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1,2,3], [4,5,6]) == 32


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

assert sum_of_squares([1,2,3]) == 14 # 1*1 + 2*2 + 3*3

def magnitude(v: Vector) -> float:
    """The length or magnitud of v"""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5

def squared_distance(v: Vector, w:Vector) -> float:
    """computes (v_1 - w_1)**2 + ... + (v_n - w_n)**2 """
    return sum_of_squares(substract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Distance between v and w"""
    return math.sqrt(squared_distance(v, w))

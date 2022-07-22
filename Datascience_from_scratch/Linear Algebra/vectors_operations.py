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
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]
 
def substract(v: Vector, w:Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "No vector provided"
    #we cheack that all the vecotors are of the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Vectors has diferent sizes"
    
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[1,2], [3,4],[5,6], [7,8]]) == [16, 20]

def scalar_multiply(c: float,vectors: List[Vector]) -> Vector:
    return [c * v_i for v_i in vectors]

def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3,4], [5,6]]) == [3, 4]

def dot(v: Vector, w:Vector) -> float:
    assert len(v) == len(w), "vectors has different lenght"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1,2,3], [4,5,6]) == 32


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

assert sum_of_squares([1,2,3]) == 14

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5

def squared_distance(v: Vector, w:Vector) -> float:
    return sum_of_squares(substract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))

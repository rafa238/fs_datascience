#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 00:45:39 2022

@author: rafajl
"""
from typing import List, Tuple, Callable

Vector = List[float]

Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

def shape(A: Matrix, B: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_columns = len(A[0]) if A else 0
    return num_rows, num_columns

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j]
            for A_i in A]

def make_matrix(num_rows: int, 
                num_columns: int, 
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    generate a matrix whose i-th, j-th entry is entry_fn(i,j)
    """
    return [[entry_fn(i,j) for j in range(num_columns)] for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i,j: 1 if i==j else 0)

print(identity_matrix(3))
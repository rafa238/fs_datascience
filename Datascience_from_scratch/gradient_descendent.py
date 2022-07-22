# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:32:26 2022

@author: PC
"""

from typong import Callable

#calculate the derivade
def difference_quotient(f: Callable[[float], float], x: float, h: float):
    return (f(x+h)-f(x))/h

#calculate de partial derivades
def partial_differene_quotient(f: Callable[[Vector], float],
                               v: Vector,
                               i: int,
                               h: float) -> float:
    w = [v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimate_gradient(f: Callable[[Vector], float],
                      v: Vector,
                      h: float = 0.0001):
    return [partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]
    

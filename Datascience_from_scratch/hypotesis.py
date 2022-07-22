# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 21:26:44 2022

@author: PC
"""

from typing import Tuple
import math
from probability import normal_cdf, inverse_normal_cdf
"""
this is a normal distribution and we can see it like a bell 
where mu is the desviation and sigma is the weight.
these functions calculate the cdf(cumulative density function)
right the bell, left the bell, between and outside 
"""
def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    mu = p*n
    sigma = math.sqrt(p * (1-  p) * n)
    return mu, sigma

normal_probability_below = normal_cdf

def normal_probability_above(lo: float, 
                             hi: float, 
                             mu: float=0, 
                             sigma: float = 1) -> float:
    return 1-normal_cdf(lo, mu, sigma)

def normal_probability_between(lo: float, 
                               hi: float, 
                               mu: float = 0, 
                               sigma: float = 1) -> float:
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo: float, 
                               hi: float, 
                               mu: float = 0, 
                               sigma: float = 1) -> float:
    return 1-normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability: float,
                       mu: float = 0,
                       sigma: float = 1) -> float:
    """Returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability: float,
                            mu: float = 0,
                            sigma: float = 1) -> Tuple[float, float]:
    """
    Returns the symmetric (about the mean) bounds
    that contain the specified probability
    """
    tail_probability = (1 - probability) / 2

    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound 


mu_0, sigma_0 = normal_approximation_to_binomial(1000,0.5)
lower_bound, upper_bound = normal_two_sided_bounds(0.95, mu_0, sigma_0)
pro = normal_probability_between(lower_bound, upper_bound, mu_0, sigma_0)
print(lower_bound, upper_bound, 1-pro)
import numpy as np
import pandas as pd


def calculate_gpa(grades, weights, seminars):
    if not isinstance(weights, np.ndarray):
        raise TypeError('Weights must be a ndarray')
    if not isinstance(grades, np.ndarray):
        raise TypeError('Weights must be a ndarray')
    if not isinstance(seminars, np.ndarray):
        raise TypeError('Weights must be a ndarray')
    
    if len(weights) != len(grades) != len(seminars):
        raise Exception('Grades, weights and seminars must have the same length.')
    
    mask = seminars == 0
    gpa = np.average(grades[mask], weights=weights[mask])
    return gpa
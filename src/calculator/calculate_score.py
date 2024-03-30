import numpy as np
import pandas as pd

def calculate_score(gpa, grades, weights, first_year, multiplier):
    total_credits = np.sum(weights)
    first_year_mask = first_year == 1
    passed_mask = grades != 0

    minimum_credits = 0.6 * np.sum(weights[first_year_mask])
    first_year_credits = np.sum(weights[first_year_mask & passed_mask])

    if gpa < 22:
        return 0
    if first_year_credits < minimum_credits:
        return 0

    credits_taken = np.sum(weights[passed_mask])
    delta_credits = credits_taken - minimum_credits
    bonus = multiplier * delta_credits

    score = gpa + bonus
    return score




    
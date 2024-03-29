
import numpy as np
import pandas as pd

class Score_Calculator:
    def __init__(self, grades, credits, course):

        courses = ['BAI', 'BEMACS', 'BESS', 'BIEM', 'BIEF', 'BEMAC', 'CLEAM', 'CLEF', 'CLEAC']
        if course not in courses:
            raise Exception(f'The course "{course}" is not valid.')
        
        if not isinstance(grades, np.ndarray ):
            raise ValueError('Grades must be an ndarray')
        
        if not isinstance(credits, np.ndarray ):
            raise ValueError('Credits must be an ndarray')
        
        self.grades = grades
        self.course = course
        self.credits = credits


        multiplier = {"BAI": 1.02, "BEMACS": 1.02, "BESS": 1.02}

        def calculate_sces(self):
            pass
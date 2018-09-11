# Run with: `python -m unittest discover`

import unittest
from sklearn.externals import joblib

class Test(unittest.TestCase):
    personalities = ['INFJ', 'ENTP', 'INTP', 'INTJ',
    'ENTJ', 'ENFJ', 'INFP', 'ENFP',
    'ISFP', 'ISTP', 'ISFJ', 'ISTJ',
    'ESTP', 'ESFP', 'ESTJ', 'ESFJ']
    def test_prediction(self):

        model = joblib.load('./model/model.pkl')
        text = 'very good day'
        personality = model.predict([text])[0]

        res = personality in self.personalities
        self.assertTrue(res, "bad predicction")

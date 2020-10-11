import pandas as pd
from instance_recommender.recommender import best_reco
from unittest import TestCase


class TestRecommender(TestCase):
    def test_case1(self):

        required_resources = {'vcpu': 17, 'memory': 26}

        instance_df = pd.DataFrame({
            'name': ['m5', 'c5', 'r5'],
            'vcpu': [2, 2, 2],
            'memory': [8, 4, 16],
            'price': [96, 85, 126]
        })

        actual = best_reco(required_resources, instance_df)

        expected = pd.DataFrame({
            'name': instance_df['name'],
            'units': [0, 9, 0]
        })

        assert actual.equals(expected)

    def test_case2(self):

        required_resources = {'vcpu': 17, 'memory': 56}

        instance_df = pd.DataFrame({
            'name': ['m5', 'c5', 'r5'],
            'vcpu': [2, 2, 2],
            'memory': [8, 4, 16],
            'price': [96, 85, 126]
        })

        actual = best_reco(required_resources, instance_df)

        expected = pd.DataFrame({
            'name': instance_df['name'],
            'units': [6, 3, 0]
        })

        assert actual.equals(expected)
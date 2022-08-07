from unittest import TestCase as __TestCase
import matplotlib.pyplot as plt
from behaviorpy.plot import (
    SingleBaselineGraph as _SingleBaselineGraph,
)


class TestSingleBaselineGraph(__TestCase):
    def test_baseline_only(self):
        _SingleBaselineGraph(
            suptitle='Behavior Analysis Plot Example',
        ).add_baseline(
            [1, 3], [2, 3], [3, 2], [4, 4], [5, 3]
        )
        plt.show()
        plt.close('all')

    def test_baseline_and_single_phase_change(self):
        _SingleBaselineGraph(
            suptitle='Behavior Analysis Plot Example',
            title='Single Baseline and Phase Change',
        ).add_baseline(
            [1, 3], [2, 3], [3, 2], [4, 4], [5, 3]
        ).add_phase_change(
            [6, 7], [7, 8], [8, 7], [9, 9], [10, 8]
        )
        plt.show()
        plt.close('all')

    def test_multiple_phase_and_condition_changes(self):
        _SingleBaselineGraph(
            suptitle='Behavior Analysis Plot Example',
            title='Single Baseline and Multiple Phase Changes',
        ).add_baseline(
            [1, 3], [2, 3], [3, 2], [4, 4], [5, 3]
        ).add_phase_change(
            [6, 7], [7, 8], [8, 7], [9, 9], [10, 8]
        ).add_condition_change(
            [11, 3], [12, 3], [13, 2], [14, 4], [15, 3]
        ).add_phase_change(
            [16, 7], [17, 8], [18, 7], [19, 9], [20, 8]
        )

        plt.show()
        plt.close('all')


if __name__ == '__main__':
    import unittest

    unittest.main()

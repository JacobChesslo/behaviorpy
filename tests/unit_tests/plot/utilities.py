from unittest import TestCase as __TestCase
import numpy as np
from matplotlib.lines import Line2D
from behaviorpy.plot._utils import (
    line_from,
    fix_points,
)


class TestLineFrom(__TestCase):
    def setUp(self) -> None:
        self.line_object = Line2D((), ())

    def test_from_line_2d_object(self):
        self.assertIsInstance(
            line_from(self.line_object), Line2D,
            'Failed to return a matplotlib.lines.Line2D instance from a matplotlib.lines.Line2D instance'
        )

    def test_from_list(self):
        self.assertIsInstance(
            line_from([self.line_object, ]), Line2D,
            'Failed to return a matplotlib.lines.Line2D instance from a list of matplotlib.lines.Line2D instance'
        )

    def test_from_tuple(self):
        self.assertIsInstance(
            line_from((self.line_object, )), Line2D,
            'Failed to return a matplotlib.lines.Line2D instance from a tuple of matplotlib.lines.Line2D instance'
        )

    def test_from_numpy_ndarray(self):
        self.assertIsInstance(
            line_from(np.array([self.line_object])), Line2D,
            'Failed to return a matplotlib.lines.Line2D instance from a matplotlib.lines.Line2D instance'
        )

    def test_string_fail(self):
        with self.assertRaises(ValueError):
            self.assertIsInstance(
                line_from('this is a test string'), Line2D,
                'Failed to return a matplotlib.lines.Line2D instance from a matplotlib.lines.Line2D instance'
            )


if __name__ == '__main__':
    import unittest

    unittest.main()

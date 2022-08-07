from unittest import TestCase as __TestCase
from warnings import warn
from behaviorpy.errors import (
    BehaviorPyError,
    BehaviorPyWarning,
)


class TestBehaviorPyError(__TestCase):
    def test_raises_exception(self) -> None:
        with self.assertRaises(BehaviorPyError):
            raise BehaviorPyError('This is an example error')


class TestBehaviorPyWarning(__TestCase):
    def test_warns(self) -> None:
        with self.assertWarns(BehaviorPyWarning):
            warn('This is an example warning', BehaviorPyWarning)


if __name__ == '__main__':
    import unittest

    unittest.main()

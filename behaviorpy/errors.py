"""BehaviorPy: Custom Errors and Exceptions"""


class BehaviorPyError(Exception):
    """BehaviorPy Warning

    See Also
    --------
    Warning : Inherited Class

    Examples
    --------
    >>> raise BehaviorPyError('This is an example BehaviorPy error')
    Traceback ((most recent call last):
    ...
    behaviorpy.errors.BehaviorPyError: This is an example BehaviorPy error
    """
    pass


class BehaviorPyWarning(Warning):
    """BehaviorPy Warning

    See Also
    --------
    Warning : Inherited Class

    Examples
    --------
    >>> import warnings
    >>> warnings.warn('This is an example BehaviorPy warning', BehaviorPyWarning)
    BehaviorPyWarning: This is an example BehaviorPy warning
    """
    pass

import numpy as np
from matplotlib.lines import Line2D


def fix_points(*points) -> np.ndarray:
    """Takes in a list of (x, y) points and returns those points transposed as a 2D numpy.ndarray

    Parameters
    ----------
    points:
        An iterable of (x, y) points

    Returns
    -------
    numpy.ndarray
        An array of x points at index 0 and y points at index 1

    See Also
    --------
    numpy.array : Function used
    numpy.ndarray : Class used

    Examples
    --------
    >>> fix_points((1, 2), (2, 3), (3, 4), (4, 5))
    array([[1, 2, 3, 4],
           [2, 3, 4, 5]])

    >>> fix_points(*[[1, 2], [2, 3], [3, 4], [4, 5]])
    array([[1, 2, 3, 4],
           [2, 3, 4, 5]])
    """
    return np.array(points).transpose()


def line_from(obj) -> Line2D:
    """Extracts the first matplotlib.lines.Line2D instance from passed obj

    Parameters
    ----------
    obj
        Line2D instance or container for

    Returns
    -------
    matplotlib.lines.Line2D
        First instance of a matplotlib.lines.Line2D

    Raises
    ------
    ValueError
        If obj is not a matplotlib.lines.Line2D instance or is an iterable
        If obj is a string

    See Also
    --------
    matplotlib.lines.Line2D : Class sought after

    Examples
    --------
    >>> line_from(matplotlib.lines.Line2D((), ()))
    <matplotlib.lines.Line2D object at 0x7fbac8a39b20>

    >>> line_from([matplotlib.lines.Line2D((), ()), ])
    <matplotlib.lines.Line2D object at 0x7fbac8a39b20>

    >>> line_from([matplotlib.lines.Line2D((), ()), matplotlib.lines.Line2D((), ())])
    <matplotlib.lines.Line2D object at 0x7fbac8a39b20>

    >>> line_from([([(matplotlib.lines.Line2D((), ()), )])])
    <matplotlib.lines.Line2D object at 0x7fbac8a39b20>
    """
    # Return obj if we got it right the first time
    if isinstance(obj, Line2D):
        return obj

    # Duck typing for iterable with length
    try:
        obj.__iter__
        obj.__len__
    except TypeError as err:
        raise ValueError(f'Expected array-like iterable or matplotlib.lines.Line2D, not type {type(obj)}') from err

    # Strings pass duck typing, so check here if we have a string and raise
    #   otherwise this would cause Recursion Error
    if isinstance(obj, str):
        raise ValueError(f'Expected array-like iterable or matplotlib.lines.Line2D, not type {type(obj)}')

    # Return first index from obj
    return line_from(obj[0])

"""BehaviorPy: Behavior-Analysis Library for Python

Single Baseline Graph

BehaviorPy is an open-source software for the behavioral sciences.
"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from behaviorpy.plot._base_plot import (
    Graph as _Graph_,
)
from behaviorpy.plot._utils import (
    fix_points,
    line_from,
)


class SingleBaselineGraph(_Graph_):
    """Single Baseline Graph
    
    Attributes
    ----------
    fig: matplotlib.figure.Figure
        Single Baseline Figure
    ax: matplotlib.axes.Axes
        Single Baseline Plotting Area
    axs: array_like of matplotlib.axes.Axes
        Single Baseline Plotting Areas (Unused)
    _baseline_lines : list of matplotlib.lines.Line2D
        Baseline Line objects
    _condition_lines: list of matplotlib.lines.Line2D
        Condition Change Line objects
    _phase_change_lines: list of matplotlib.lines.Line2D
        Phase Change Line objects
    
    Methods
    -------
    suptitle
        Sets the figures title
    title
        Sets the axes title
    set_baseline
        Resets the plot and sets the baseline
    add_baseline
        Adds a baseline
    add_condition_change
        Adds a condition change
    add_phase_change
        Adds a phase change

    See Also
    --------
    matplotlib : Python package used for plotting
    """
    _data_kwargs = dict(marker='o', linestyle='-', color='black')
    _vertical_line_kwargs = dict(color='gray')
    _condition_change_line_kwargs = dict(linestyle='--')
    _phase_change_line_kwargs = dict(linestyle='-')

    def __init__(self, *args, **kwargs):
        """

        Parameters
        ----------
        args
        kwargs
        """
        super().__init__(*args, **kwargs)

        self.fig, self.ax = plt.subplots(nrows=1, ncols=1)

        # Initialize line lists
        self._reset_line_lists()

        # Plot metadata
        if 'suptitle' in kwargs:
            self.suptitle(kwargs.get('suptitle'))
        if 'title' in kwargs:
            self.title(kwargs.get('title'))

    def suptitle(self, title: str, **kwargs):
        """Sets the figures title

        Parameters
        ----------
        title
        kwargs

        Returns
        -------

        """
        self.fig.suptitle(title, **kwargs)

    def title(self, title: str, **kwargs):
        """Sets the plotted data title

        Parameters
        ----------
        title: str
        kwargs: dict

        Returns
        -------
        """
        self.ax.set_title(title, **kwargs)

    def set_baseline(self, *points, **kwargs):
        """Sets a baseline via (x,y) points

        Parameters
        ----------
        points: tuple of iterable of real_number
            iterable of (x, y) points
        kwargs

        Returns
        -------
        self
        """
        # Clears axis and resets private lists
        self.ax.clear()
        return self._reset_line_lists().add_baseline(*points, **kwargs)

    def add_baseline(self, *points, **kwargs):
        """Adds a baseline via (x,y) points

        Parameters
        ----------
        points: tuple of iterable of real_number
            iterable of (x, y) points
        kwargs

        Returns
        -------
        self
        """
        # Plots data, returns self
        return self._add_data_path(*points, **kwargs)

    def add_phase_change(self, *points, **kwargs):
        """Adds a phase change via (x,y) points

        Parameters
        ----------
        points: tuple of iterable of real_number
            iterable of (x, y) points
        kwargs

        Returns
        -------
        self
        """
        return self._add_data_path(*points, **kwargs)._add_phase_change_vertical_line()

    def add_condition_change(self, *points, **kwargs):
        """Adds a condition change via (x,y) points

        Parameters
        ----------
        points: tuple of iterable of real_number
            iterable of (x, y) points
        kwargs

        Returns
        -------
        self
        """
        return self._add_data_path(*points, **kwargs)._add_condition_change_vertical_line()

    def _add_data_path(self, *points, **kwargs):
        """Adds a data path to the plot

        Parameters
        ----------
        points: tuple of iterable of real_number
            iterable of (x, y) points
        kwargs

        Returns
        -------

        """
        self._data_path_lines.append(self._plot_data(*points, **kwargs))
        return self

    def _add_phase_change_vertical_line(self):
        """Adds a phase change vertical line to the plot

        Returns
        -------
        self
        """
        self._change_lines.append(self._plot_vertical_change_line(**self._phase_change_line_kwargs))
        return self

    def _add_condition_change_vertical_line(self):
        """Adds a condition change vertical line to the plot

        Returns
        -------
        self
        """
        self._change_lines.append(self._plot_vertical_change_line(**self._condition_change_line_kwargs))
        return self

    def _plot_data(self, *points, **kwargs) -> Line2D:
        """Plots data

        Parameters
        ----------
        points: tuple of iterable of real_number
            iterable of (x, y) points
        kwargs: dict


        Returns
        -------
        matplotlib.lines.Line2D

        See Also
        --------
        matplotlib.axes.Axes.plot : Function used to plot a single set of data
        behaviorpy.plot._utils.line_from : Function to extract proper object
        """
        # Fixes points
        x, y = fix_points(*points)

        # Fixes keyword arguments
        fixed_kwargs = dict(**self._data_kwargs)
        fixed_kwargs.update(**kwargs)

        # Plots line data
        return line_from(self.ax.plot(x, y, **fixed_kwargs))

    def _plot_vertical_change_line(self, **kwargs) -> Line2D:
        """Plots a vertical change line

        Parameters
        ----------
        kwargs: dict

        Returns
        -------
        matplotlib.lines.Line2D
            Vertical Line Line Object

        See Also
        --------
        matplotlib.axes.Axes.axvline : Function used to plot a single vertical line
        behaviorpy.plot._utils.line_from : Function to extract proper object
        """
        # Gets where the line should be located (grabs last two plotted _data_path_lines and finds the midpoint)
        x_pts_before_line, x_pts_after_line = [data_path.get_xdata() for data_path in self._data_path_lines[-2:]]
        x_before, x_after = max(x_pts_before_line), min(x_pts_after_line)
        x = (x_after + x_before) / 2

        # Fixes keyword arguments
        fixed_kwargs = dict(**self._vertical_line_kwargs)
        fixed_kwargs.update(**kwargs)
        fixed_kwargs.update(dict(
            ymin=kwargs.get('ymin', 0.0), ymax=kwargs.get('ymax', 1.0), clip_on=kwargs.get('clip_on', True)
        ))

        # Plots vertical line and appends the line
        return line_from(self.ax.axvline(x, **fixed_kwargs))

    def _reset_line_lists(self):
        """Resets private line attribute lists

        Returns
        -------
        self
        """
        self._change_lines, self._data_path_lines = [], []
        return self

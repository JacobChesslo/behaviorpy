def create_single_baseline_graph_example():
    import matplotlib.pyplot as plt
    import behaviorpy

    # Here we create a graph object with a title
    example_single_baseline_graph = behaviorpy.SingleBaselineGraph(
        suptitle='Behavior Analysis Single Baseline Plot Example',
    )

    # Here we want to add the baseline with a set of x, y points
    example_single_baseline_graph.add_baseline(
        # [x0,y0], [x1,y1], [x2,y2], [x3,y3], [x4,y4], ...
        [1, 3], [2, 3], [3, 2], [4, 4], [5, 3]
    )

    # Say we want to add multiple phase or condition changes.
    # We can do something called 'method chaining' and do it all at once
    example_single_baseline_graph.add_phase_change(
        [6, 7], [7, 8], [8, 7], [9, 9], [10, 8], [11, 9],
    ).add_condition_change(
        [12, 5], [13, 3], [14, 5], [15, 4],
    ).add_phase_change(
        [16, 6], [17, 10], [18, 7], [19, 8], [20, 10],
    )

    plt.show()
    plt.close('all')


if __name__ == '__main__':
    create_single_baseline_graph_example()

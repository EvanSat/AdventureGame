def adjust_points(current_points, adjustment):
    if isinstance(adjustment, int):
        return current_points + adjustment
    else:
        return current_points

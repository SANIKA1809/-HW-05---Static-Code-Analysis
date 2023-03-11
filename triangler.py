def classify_triangle(side_a, side_b, side_c):
    """
    Classify a triangle based on the length of its sides.
    
    Args:
    side_a (int): the length of the first side
    side_b (int): the length of the second side
    side_c (int): the length of the third side
    
    Returns:
    str: the type of triangle, or 'InvalidInput' if the input is invalid
    This module contains functions for classifying triangles based on the length of their sides.

    """
    # requires input values be >= 0 and <= 200
    # all three should be int
    instance_list = [isinstance(side_a, int), isinstance(side_b, int), isinstance(side_c, int)]
    if (max(side_a, side_b, side_c) > 200 or
            min(side_a, side_b, side_c) < 0 or
            not instance_list):
        return 'InvalidInput'

    # this is an extra implementation to give a more accurate output
    if ((side_a >= (side_b + side_c)) or
            (side_b >= (side_a + side_c)) or
            (side_c >= (side_a + side_b))):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if (((side_a ** 2) + (side_b ** 2)) == (side_c ** 2)) or \
            (((side_a ** 2) + (side_c ** 2)) == (side_b ** 2)) or \
            (((side_c ** 2) + (side_b ** 2)) == (side_a ** 2)):
        return 'Right'
    if (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    return 'Isosceles'

def rotate_angle_by_degrees(initial_angle, rotation):
    # Calculate the new angle
    new_angle = initial_angle + (rotation % 360)

    return new_angle

# Test the function
print(rotate_angle_by_degrees(350, 15))  # Should return 5, but won't due to the bug
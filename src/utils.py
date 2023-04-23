from geometry_msgs.msg import Vector3
from turtlesim.msg import Pose as PoseData
from math import atan2


def calculate_to(current_pose, target_pose):
    """
    The turtlesim workspace is a 11x11 square, with the origin (0, 0) at the bottom left corner.
    11x11 considering the turtle's radius for visualization.
    """

    linear = Vector3()
    angular = Vector3()

    # Calculate linear velocity of the turtle
    linear.x = target_pose.x - current_pose.x
    linear.y = target_pose.y - current_pose.y
    linear.z = 0.0

    # Check if the turtle is close enough to the target point
    is_close = abs(linear.x) < 0.2 and abs(linear.y) < 0.2
    # 0.33 is the tolerance, you can change it to any value you want
    # the smaller the value, the more accurate the turtle will be

    if is_close:
        return Vector3(x=0.0, y=0.0, z=0.0), Vector3(x=0.0, y=0.0, z=0.0), True

    # Calculate angular velocity of the turtle (in the Z-axis)
    angular.z = 0.001 * (atan2(linear.y, linear.x) - current_pose.theta)
    """
    0.01 is a gain factor, lower it to make the turtle move slowe
    but more accurately. Higher it to make the turtle move faster but less accurately
    less accurately means that the turtle will drift away from the target point...
    you can test other values, but 0.01 is a good value for this example.
    atan2(y, x) returns the angle between the x-axis and the vector starting at (0, 0) and terminating at (x, y).
    """

    return linear, angular, False


def calculate_rect_points(center_point, size):
    v1 = Vector3(
        x=center_point.x - size / 2, y=center_point.y - size / 2, z=0.0
    )  # bottom-left vertex
    v2 = Vector3(
        x=center_point.x + size / 2, y=center_point.y - size / 2, z=0.0
    )  # bottom-right vertex
    v3 = Vector3(
        x=center_point.x + size / 2, y=center_point.y + size / 2, z=0.0
    )  # top-right vertex
    v4 = Vector3(
        x=center_point.x - size / 2, y=center_point.y + size / 2, z=0.0
    )  # top-left vertex

    return (v1, v2, v3, v4)

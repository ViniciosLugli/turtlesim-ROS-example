from rclpy.node import Node
from geometry_msgs.msg import Vector3
from turtlesim.msg import Pose as PoseData

from utils import calculate_to, calculate_rect_points

from modules.modules_manager import ModulesManager
from modules.clients import *
from modules.parameters import *
from modules.publishers import *
from modules.subscribers import *


class TurtleController(Node):
    __current_turtle1_pose = PoseData()
    __objetive_positions = []
    __objetive_pen_color = {}
    __objetives_cursor = 0

    def __update_current_turtle1_pose(self, pose):
        self.__current_turtle1_pose = pose

    def __init__(self):
        super().__init__("turtle_controller")
        self.__modules_manager = ModulesManager(
            self
        )  # Create a modules manager instance

        # Add modules to the manager
        self.__modules_manager.add(Reset)
        self.__modules_manager.add(SetPen, "turtle1")
        self.__modules_manager.add(Velocity, "turtle1")
        self.__modules_manager.add(Background)
        self.__modules_manager.add(Pose, "turtle1", self.__update_current_turtle1_pose)

        # Reset and set default workspace settings
        self.__modules_manager.access("reset").execute()
        self.__modules_manager.access("background").set_rgb(0, 0, 0)

        """
        The turtlesim workspace is a 11x11 square, with the origin (0, 0) at the bottom left corner.
        11x11 considering the turtle's radius for visualization.
        turtle init in (5.5, 5.5)
        """

        # Windows logo points
        self.__objetive_positions = []

        rect_size = 5.1  # Rect size for objetives

        # Blue square
        center_point = Vector3(x=3.0, y=3.0, z=0.0)
        v1, v2, v3, v4 = calculate_rect_points(center_point, rect_size)
        self.__objetive_pen_color[len(self.__objetive_positions)] = (
            0,
            0,
            0,
        )  # Disable pen for first objetive
        self.__objetive_pen_color[len(self.__objetive_positions) + 1] = (
            0,
            0,
            255,
        )  # Blue pen for second objetive and others after
        self.__objetive_positions += [v1, v2, v2, v3, v3, v4, v4, v1]

        # Red square
        center_point = Vector3(x=3.0, y=8.0, z=0.0)
        v1, v2, v3, v4 = calculate_rect_points(center_point, rect_size)
        self.__objetive_pen_color[len(self.__objetive_positions)] = (
            0,
            0,
            0,
        )  # Disable pen for first objetive
        self.__objetive_pen_color[len(self.__objetive_positions) + 1] = (
            255,
            0,
            0,
        )  # Green pen for second objetive and all after
        self.__objetive_positions += [v1, v2, v2, v3, v3, v4, v4, v1]

        # Yellow square
        center_point = Vector3(x=8.0, y=3.0, z=0.0)
        v1, v2, v3, v4 = calculate_rect_points(center_point, rect_size)
        self.__objetive_pen_color[len(self.__objetive_positions)] = (
            0,
            0,
            0,
        )  # Disable pen for first objetive
        self.__objetive_pen_color[len(self.__objetive_positions) + 1] = (
            255,
            255,
            0,
        )  # Yellow pen for second objetive and all after
        self.__objetive_positions += [v1, v2, v2, v3, v3, v4, v4, v1]

        # Green square
        center_point = Vector3(x=8.0, y=8.0, z=0.0)
        v1, v2, v3, v4 = calculate_rect_points(center_point, rect_size)
        self.__objetive_pen_color[len(self.__objetive_positions)] = (
            0,
            0,
            0,
        )  # Disable pen for first objetive
        self.__objetive_pen_color[len(self.__objetive_positions) + 1] = (
            0,
            255,
            0,
        )  # Red pen for second objetive and all after
        self.__objetive_positions += [v1, v2, v2, v3, v3, v4, v4, v1]

        self.runtime_timer = self.create_timer(0.01, self.runtime)

    def runtime(self):
        linear, angular, is_close = calculate_to(
            self.__current_turtle1_pose,
            self.__objetive_positions[self.__objetives_cursor],
        )

        self.get_logger().info(
            f"Current position: {self.__current_turtle1_pose.x}, {self.__current_turtle1_pose.y}"
        )

        if is_close:
            if self.__objetives_cursor == len(self.__objetive_positions) - 1:
                self.__objetives_cursor = 0
            else:
                self.__objetives_cursor += 1

        if self.__objetive_pen_color.get(self.__objetives_cursor, None) is not None:
            r, g, b = self.__objetive_pen_color[self.__objetives_cursor]
            self.__modules_manager.access("set_pen").set_rgb(r, g, b)  # Set pen color

        self.__modules_manager.access("velocity").apply(linear, angular)

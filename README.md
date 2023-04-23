## Description
A simple but complete implementation of [TurtleSim](http://wiki.ros.org/turtlesim) in [ROS2](https://index.ros.org/doc/ros2/) using python. The project is mainly oriented by modules, on each module part is a pipeline comunication with turtlesim node. Currently has support for all services, topics and actions of turtlesim node by the [documentation](http://wiki.ros.org/turtlesim).

### Modules folders:
- `clients`: Contains the clients of turtles entitys and simulator services.
- `parameters`: Contains the parameters setter and getter of turtlesim.
- `publishers`: Contains the publishers of turtlesim topics.
- `subscribers`: Contains the subscribers of turtlesim.

The main controller is named `TurtleController` and receive a instance of `ModulesManager` for manage all modules, adding and accessing them, with this practice is possible to add new modules without change the main controller, or call a module from another module... A very flexible and scalable architecture!

### Demo controller code:
The project examples has a windows logo, with colors as demo runtime, the code are hard-tested for better visual, and many numbers are finded on calculous for better visual too, for example, rects sizes and positions...
For manage turtle position and color on each edge, are implemented a array of position and dict of colors for runtime, the structure of runtime function are:
1. Calculate and get the next position ( and get if is close enough to the position )
2. If is close enough, increment the position cursor index and get the next position
3. get the next color of pencil and set on turtle
4. Apply velocity and angular velocity on turtle

### Additional infos:
-  The turtlesim workspace is a 11x11 square, with the origin (0, 0) at the bottom left corner. 11x11 considering the turtle's radius for visualization.
- Turtle init in (5.5, 5.5), on center.
- The code change background color for black, and control turtle pencil color for each windows logo rect.
- This demo is based in only one turtle, turtle default named: `turtle1` for turtlesim.
- The turtlesim workspace reset on each run, using the `reset` client.


### Nodes:
- The turtle receive the main info from `cmd_vel` topic, on `publishers` module, for move the turtle with angular velocity.
- Code receive from `pose` topic, on `subscribers` module, the turtle position and orientation, for calculate the next position and orientation.
- Background color is changed by `turtlesim/set_parameters` service, on `parameters` module, passing the parameters and value from pipeline. The parameters are: `background_r`, `background_g` and `background_b`, all with range from 0 to 255.
- The turtle color is changed by `turtlesim/set_pen` service, on `parameters` module, passing the parameters and value from pipeline. The parameters are: `r`, `g`, `b`, `width` and `off`, all with range from 0 to 255, except `off` that is a boolean.


## Demo of project running:


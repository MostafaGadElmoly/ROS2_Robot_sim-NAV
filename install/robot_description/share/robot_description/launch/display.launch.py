from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameters_type import ParameterValue
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # Get the path to the URDF file using ament_index_python
    urdf_path = os.path.join(get_package_share_directory('robot_description'), 'urdf', 'Robot.urdf')

    # Define the parameter for robot_description using a Command substitution
    robot_description = ParameterValue(
        Command(['xacro', urdf_path]),
        value_type='str'
    )

    # Create nodes for robot_state_publisher, joint_state_publisher, and rviz2
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[robot_description]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2'
    )

    # Return the LaunchDescription object containing all nodes
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz2_node
    ])

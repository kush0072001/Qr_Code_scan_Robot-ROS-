from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_share_dir = get_package_share_directory("vision_rpi_bot")
    urdf_file_path = os.path.join(package_share_dir, "urdf", "vision_rpi_bot.urdf")

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='rsp_node',
            output='screen',  # Add this line to see the output in the terminal
            arguments=[urdf_file_path]
        ),
        Node(
            package='joint_state_publisher_gui',  # Fix the package name here
            executable='joint_state_publisher_gui',
            name='jst_gui',
            output='screen'  # Add this line to see the output in the terminal
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='simulation_in_rviz',
            output='screen'  # Add this line to see the output in the terminal
        ),
    ])

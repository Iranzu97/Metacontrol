import os
from launch import LaunchDescription
from launch_ros.actions import Node
 
 
def generate_launch_description():
  return LaunchDescription([
    Node(
    	package='first_pkg',
    	namespace='publisher',
    	executable='talker',
    	name='talker'
    ),
    Node(
    	package='first_pkg',
    	namespace='subscriber',
    	executable='listener',
    	name='listener'
    ),
  ])

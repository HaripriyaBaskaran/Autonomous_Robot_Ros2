# Autonomous_Robot_Ros2
I have created a robot with automated navigation with Lidar sensors and camera which avoids the obstacle in its path

# Installation: (Requires a ROS2 distribution)
sudo apt install ros-humble-twist-mux

# Launching the files:
Launch the simulation (ros2 launch articubot_one launch_sim.launch.py)
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/articubot_one/config/mapper_params_online_async.yaml use_sim_time:=true
ros2 launch nav2_bringup navigation_launc.py use_sim_time:=true

# Running the nodes:
ros2 run twist_mux twist_mux --ros-args --params_file ./src/articubot_one/config/twist_mux.yaml -r cmd_vel_out=diff_cont/cmd_vel_unstamped
run Rviz2 (rviz2)
running obstacle avoidance (./obstacle_avoidace.py)

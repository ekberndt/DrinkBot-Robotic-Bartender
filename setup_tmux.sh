#!/bin/sh

dir="~/DrinkBot-Robotic-Bartender"
robot="ada"
tmux new -d -s ros_view
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
tmux send "roscore" Enter


tmux split-window -v
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
sleep 3
tmux send "roslaunch realsense2_camera rs_camera.launch" Enter


tmux split-window -h -t 0
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "./intera.sh $robot.local" Enter
tmux send "roslaunch sawyer_moveit_config sawyer_moveit.launch electric_gripper:=true" Enter

tmux split-window -h -t 2
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "./intera.sh $robot.local" Enter
tmux send "roslaunch intera_examples sawyer_tuck.launch"

tmux split-window -v -t 3
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "./intera.sh $robot.local" Enter
tmux send "rosrun rosserial_python serial_node.py /dev/ttyACM0" Enter

tmux split-window -v -t 2
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "rosrun planning ar_tag_client.py"

tmux split-window -v -t 1
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "roslaunch lab4_cam ar_track.launch" Enter

tmux split-window -v -t 0
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "./intera.sh $robot.local" Enter
tmux send "rosrun planning forward_kinematics_server.py" Enter

tmux split-window -h -t 7
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "Hello (っ◕‿◕)っ"

tmux split-window -h -t 6
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "rosrun rviz rviz" Enter

tmux split-window -h -t 5
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "rosrun planning sawyer_server.py" Enter

tmux split-window -h -t 4
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "source devel/setup.bash" Enter
tmux send "rosrun intera_interface joint_trajectory_action_server.py" Enter

# tmux split-window -h -t 3
# tmux send "source ~/.bashrc" Enter
# tmux send "cd $dir" Enter
# tmux send "source devel/setup.bash" Enter
# tmux send "" Enter

# Evenly split all panes
tmux select-layout tiled

tmux a -t ros_view

#!/bin/sh

dir="~/DrinkBot-Robotic-Bartender"
tmux new -d -s ros_view
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
tmux send "roscore" Enter


tmux split-window -v
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
# tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
sleep 3
tmux send "roslaunch lab4_cam rs_d435_camera_with_model.launch" Enter


tmux select-layout even-vertical

tmux split-window -h -t 1
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
# tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
tmux send "roslaunch lab4_cam ar_track.launch" Enter


tmux split-window -h -t 0
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
# tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
tmux send "rosrun rviz rviz" Enter


tmux a -t ros_view

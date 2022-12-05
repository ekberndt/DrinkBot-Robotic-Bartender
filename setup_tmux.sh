#!/bin/sh

dir="~/DrinkBot-Robotic-Bartender"
tmux new -d -s ros_view
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
tmux send "source setup_workspace.sh" Enter


tmux split-window -v
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
tmux send "source setup_workspace.sh" Enter


tmux select-layout even-vertical

tmux split-window -h -t 1
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
tmux send "source setup_workspace.sh" Enter


tmux split-window -h -t 0
tmux send "source ~/.bashrc" Enter
tmux send "cd $dir" Enter
tmux send "catkin_make" Enter
tmux send "source devel/setup.bash" Enter
tmux send "source setup_workspace.sh" Enter


tmux a -t ros_view
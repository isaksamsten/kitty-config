#!/bin/bash

# Check if there are any existing tmux sessions
if tmux ls &>/dev/null; then
  SESSION=$(tmux ls | grep -v attached | head -n 1 | cut -d: -f1)
  if [ -n "$SESSION" ]; then
    # echo "$SESSION"
    tmux attach -t "$SESSION" \; new-window
  else
    # echo "All sessions attached"
    tmux new-session
  fi
else
  # echo "No sessions at all"
  tmux new-session
fi

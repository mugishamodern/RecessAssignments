# Assignment Ten: Train RL agent to cross the road with actions right, left
# Name: ______________________
# Date: ______________________

import numpy as np

# Environment setup
GRID_SIZE = 5  # Road has 5 positions: 0 (start) to 4 (goal)
ACTIONS = ['left', 'right']
ACTION_IDX = {'left': 0, 'right': 1}

# Q-learning parameters
alpha = 0.1      # Learning rate
gamma = 0.9      # Discount factor
epsilon = 0.2    # Exploration rate
num_episodes = 200

# Initialize Q-table
Q = np.zeros((GRID_SIZE, len(ACTIONS)))

for episode in range(num_episodes):
    state = 0  # Start position
    done = False
    while not done:
        # Epsilon-greedy action selection
        if np.random.rand() < epsilon:
            action = np.random.choice(ACTIONS)
        else:
            action = ACTIONS[np.argmax(Q[state, :])]
        # Take action
        if action == 'right':
            next_state = min(state + 1, GRID_SIZE - 1)
        else:  # 'left'
            next_state = max(state - 1, 0)
        # Reward
        if next_state == GRID_SIZE - 1:
            reward = 10  # Goal reached
            done = True
        else:
            reward = -1  # Step penalty
        # Q-learning update
        Q[state, ACTION_IDX[action]] = Q[state, ACTION_IDX[action]] + alpha * (
            reward + gamma * np.max(Q[next_state, :]) - Q[state, ACTION_IDX[action]]
        )
        state = next_state

# Print learned policy
print("\nLearned Policy (best action at each position):")
for pos in range(GRID_SIZE):
    best_action = ACTIONS[np.argmax(Q[pos, :])]
    print(f"Position {pos}: {best_action}") 
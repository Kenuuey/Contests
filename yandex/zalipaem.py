import numpy as np

# The observations (activity levels)
observations = ['L', 'M', 'M', 'H', 'M', 'L', 'M', 'M', 'L', 'L', 'H', 'M', 'M', 'H', 'L']

# Define the states (moods)
states = ['G', 'B']

# Emission probabilities: P(Observation | Mood)
emission_probs = {
    'L': {'G': 0.6, 'B': 0.2},
    'M': {'G': 0.3, 'B': 0.3},
    'H': {'G': 0.1, 'B': 0.5}
}

# Transition probabilities: P(Mood_t | Mood_(t-1))
transition_probs = {
    'G': {'G': 0.6, 'B': 0.4},
    'B': {'G': 0.3, 'B': 0.7}
}

# Number of days (15 days in total)
n = len(observations)

# Initialize the Viterbi DP table and backtracking table
dp = np.zeros((n, 2))  # dp[i, j] holds the log probability for the best path until day i with mood j
backtrack = np.zeros((n, 2), dtype=int)  # backtrack[i, j] holds the state that led to the best path at day i

# Initialization for the first day (first observation)
for mood_idx, mood in enumerate(states):
    dp[0, mood_idx] = np.log(emission_probs[observations[0]][mood])  # log of the emission probability for the first day

# Viterbi algorithm: fill the dp table for each subsequent day
for day in range(1, n):
    for cur_mood_idx, cur_mood in enumerate(states):
        max_prob = -np.inf
        max_state = -1
        for prev_mood_idx, prev_mood in enumerate(states):
            # Calculate transition probability from previous mood to current mood
            prob = dp[day-1, prev_mood_idx] + np.log(transition_probs[prev_mood][cur_mood]) + np.log(emission_probs[observations[day]][cur_mood])
            
            if prob > max_prob:
                max_prob = prob
                max_state = prev_mood_idx

        dp[day, cur_mood_idx] = max_prob
        backtrack[day, cur_mood_idx] = max_state

# Backtrack to find the most likely sequence of moods
best_path = []
best_last_state = np.argmax(dp[n-1])  # The best mood on the last day

best_path.append(states[best_last_state])

for day in range(n-2, -1, -1):
    best_last_state = backtrack[day+1, best_last_state]
    best_path.insert(0, states[best_last_state])

# Print the result as the sequence of moods
print(''.join(best_path))

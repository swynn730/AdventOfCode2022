# Part 1
# Answer: 13675
MAX_SHAPE_NUMS = 3
shape_values = {"rock": 1, "paper": 2, "scissors": 3}
opponent_mappings = {"A": "rock", "B": "paper", "C": "scissors"}
player_mappings = {"X": "rock", "Y": "paper", "Z": "scissors"}

with open("input.txt") as f_handle:
	f_content = f_handle.readlines()

total_player_match_score = 0
for line in f_content:
	line = line.strip()

	round_responses = line.split(" ")

	opponent_round_response = opponent_mappings[round_responses[0]]
	player_round_response = player_mappings[round_responses[1]]

	opponent_round_value = shape_values[opponent_round_response]
	player_round_value = shape_values[player_round_response]

	player_round_score = player_round_value

	match_score = (player_round_value - opponent_round_value) % MAX_SHAPE_NUMS
	if match_score == 0:
		# It was a draw.
		player_round_score += 3

	elif match_score <= 1:
		# Player won.
		player_round_score += 6

	else:
		# Player lost.
		pass

	total_player_match_score += player_round_score

print(total_player_match_score)

# Part 2
# Answer: 14184
from enum import Enum
player_mappings = {"X": "lose", "Y": "draw", "Z": "win"}

class PlayerDirectives(Enum):
	DRAW = "draw"
	WIN = "win"
	LOSE = "lose"

total_player_match_score = 0
for line in f_content:
	line = line.strip()

	round_responses = line.split(" ")

	opponent_round_response = opponent_mappings[round_responses[0]]
	player_round_state = player_mappings[round_responses[1]]
	opponent_round_value = shape_values[opponent_round_response]

	player_round_value = 0
	player_round_score = 0

	if PlayerDirectives.DRAW.value == player_round_state:
		# It was a draw.
		for shape, val in shape_values.items():
			if (val - opponent_round_value) % MAX_SHAPE_NUMS == 0:
				player_round_response = shape
				player_round_value = val
				break

		player_round_score += player_round_value
		player_round_score += 3

	elif PlayerDirectives.WIN.value == player_round_state:
		# Player won.
		for shape, val in shape_values.items():
			if (val - opponent_round_value) % MAX_SHAPE_NUMS != 0 and (val - opponent_round_value) % MAX_SHAPE_NUMS <= 1:
				player_round_response = shape
				player_round_value = val
				break

		player_round_score += player_round_value
		player_round_score += 6

	else:
		# Player lost.
		for shape, val in shape_values.items():
			if (val - opponent_round_value) % MAX_SHAPE_NUMS > 1:
				player_round_response = shape
				player_round_value = val
				break

		player_round_score += player_round_value

	total_player_match_score += player_round_score

print(total_player_match_score)
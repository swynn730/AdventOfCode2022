# Part 1
# Answer: 13675
shape_values = {"rock": 1, "paper": 2, "scissors": 3}
opponent_mappings = {"A": "rock", "B": "paper", "C": "scissors"}
player_mappings = {"X": "rock", "Y": "paper", "Z": "scissors"}

with open("input.txt") as f_handle:
	f_content = f_handle.readlines()

# Test data
# f_content = ["A Y", "B X", "C Z"]

total_player_match_score = 0
for line in f_content:
	player_round_score = 0
	line = line.strip()
	round_responses = line.split(" ")
	opponent_round_response = opponent_mappings[round_responses[0]]
	player_round_response = player_mappings[round_responses[1]]

	opponent_round_value = shape_values[opponent_round_response]
	player_round_value = shape_values[player_round_response]

	player_round_score = player_round_value

	if player_round_value == opponent_round_value:
		# It was a draw.
		player_round_score += 3

	elif (player_round_value > opponent_round_value) and (abs(player_round_value - opponent_round_value) == 1):
		# Player won (scissors beats paper beats rock).
		player_round_score += 6

	elif (player_round_value < opponent_round_value) and (abs(player_round_value - opponent_round_value) == 2):
		# Player won (rock beats scissors).
		player_round_score += 6
	else:
		# Player lost.
		pass

	# Test
	# print(round_responses)
	# print(opponent_round_response)
	# print(player_round_response)
	# print(opponent_round_value)
	# print(player_round_value)
	# print(player_round_score)

	total_player_match_score += player_round_score

print(total_player_match_score)

# Part 2
# Answer: 14539 13525
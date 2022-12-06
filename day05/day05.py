import re

# Part 1
# Answer: 
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()

# Test Data: Answer should be CMZ.
with open("test_input.txt") as f_handle:
	f_content = f_handle.readlines()

separator = f_content.index("\n")

stack_drawing = []
stack_directions = []

stack_drawing.extend(f_content[0:separator])
stack_directions.extend(f_content[separator + 1:])

def generate_clean_stack_drawing(stack_drawing):
	# Cleans up stack drawing from input file; readying it for processing.
	stack_drawing_clean = []
	for line in stack_drawing:
		line = line.strip("\n")
		line = line.replace("[", " ")
		line = line.replace("]", " ")
		line_length = len(line)

		row = []

		for row_index in range(line_length):
			row.append(list(line[row_index]))

		stack_drawing_clean.append(row)

	return stack_drawing_clean


def generate_clean_stack_directions(stack_directions):
	# Cleans up stack directions from input file; readying it for processing.
	stack_directions_clean = []
	
	for line in stack_directions:
		line = line.strip("")
		stack_directions_clean.append(re.findall(r"([0-9]+)", line))

	return stack_directions_clean

def remap_crate_indices(stack_drawing):
	"""
	Convert the crate locations (numerical values at the bottom of the map drawing) 
	into usable indices that can be used to look at the crates in each column (crate location).
	"""
	stacks = stack_drawing
	number_of_crate_locations = int(stacks[-1][-2][0])
	flattened_list = [item for sublist in stacks[-1] for item in sublist]
	remapped_crate_indices = []

	for crate_locations in range(number_of_crate_locations):
		remapped_crate_indices.append(flattened_list.index(str(crate_locations + 1)))

	return remapped_crate_indices


def move_crates(stack_drawing, stack_directions):
	# Rearrange the crates based on the directions.
	# [0] = How many to move.
	# [1] = Start location.
	# [2] = End location.
	stack_rearranged = stack_drawing.copy()
	remapped_crate_indices = remap_crate_indices(stack_rearranged)
	remapped_crate_indices_length = len(remapped_crate_indices)

	# for index in remapped_crate_indices:
	# 	for row in stack_rearranged:
	# 		print(row[int(index)])
	# 	print("")

	for stack_direction in stack_directions:
		quantity = int(stack_direction[0])
		# Have to subtract 1 in order to make this index friendly and map to our remapped indices.
		start_location = remapped_crate_indices[int(stack_direction[1]) -1]
		end_location = remapped_crate_indices[int(stack_direction[2]) - 1]
		crate_counter = 0
		crate_start_counter = 0
		crate_end_counter = 0
		non_empty_crate_start_index = 0
		non_empty_crate_end_index = 0
		crate_start = stack_rearranged[0 + non_empty_crate_start_index + crate_start_counter][start_location]
		crate_end = stack_rearranged[0 + non_empty_crate_end_index + crate_end_counter][end_location]

		while crate_start[0].strip():
			if (0 + non_empty_crate_start_index + crate_start_counter) < len(stack_rearranged):
				crate_start = stack_rearranged[0 + non_empty_crate_start_index + crate_start_counter][start_location]
				crate_start_counter += 1
			break

		while not crate_end[0].strip():
			if (0 + non_empty_crate_end_index + crate_end_counter) < len(stack_rearranged):
				crate_end = stack_rearranged[0 + non_empty_crate_end_index + crate_end_counter][end_location]
				crate_end_counter += 1
			break

		while crate_counter < quantity:
			crate_end = crate_start

			# while crate_end[0].strip():
			# 	print(crate_end)
			# 	crate_end = stack_rearranged[0 + non_empty_crate_end_index + crate_end_counter][end_location]
			# 	crate_end_counter += 1

			crate_counter += 1
		print("")


	print("===========================")

	# stack_rearranged[1][1][0] = "S"
	# print(stack_rearranged[1][1])
	# print(type(stack_rearranged[1][1]))
	# print(stack_rearranged[1])
	for index in remapped_crate_indices:
		for row in stack_rearranged:
			print(row[int(index)])
		print("")

	return stack_rearranged


stack_drawing = generate_clean_stack_drawing(stack_drawing)

# print(stack_drawing[-1])
# print(len(stack_drawing[-1]))
# print(type(stack_drawing[-1]))

stack_directions = generate_clean_stack_directions(stack_directions)

# print(stack_directions[-1])
# print(len(stack_directions[-1]))
# print(type(stack_directions[-1]))

move_crates(stack_drawing, stack_directions)
# Part 2
# Answer:
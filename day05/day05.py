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

		stack_row = []

		for stack_row_index in range(line_length):
			stack_row.append(list(line[stack_row_index]))

		stack_drawing_clean.append(stack_row)

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
	stack_row_index_length = len(stack_rearranged) - 1
	remapped_crate_indices = remap_crate_indices(stack_rearranged)
	remapped_crate_indices_length = len(remapped_crate_indices)

	for index in remapped_crate_indices:
		for row in stack_rearranged:
			print(row[int(index)])
		print("")

	for stack_direction in stack_directions:
		quantity = int(stack_direction[0])
		# Have to subtract 1 in order to make this index friendly and map to our remapped indices.
		start_location = remapped_crate_indices[int(stack_direction[1]) - 1]
		end_location = remapped_crate_indices[int(stack_direction[2]) - 1]
		crate_counter = 0
		crate_start_counter = 0
		crate_end_counter = 0
		non_empty_crate_start_index = 0
		non_empty_crate_end_index = stack_row_index_length
		crate_start = stack_rearranged[0 + non_empty_crate_start_index + crate_start_counter][start_location]
		crate_end = stack_rearranged[-2 + non_empty_crate_end_index + crate_end_counter][end_location]

		while crate_counter < quantity:
			while not crate_start[0].isalpha():
				crate_start = stack_rearranged[0 + non_empty_crate_start_index + crate_start_counter][start_location]
				crate_start_counter += 1

			while crate_end[0].isdigit() or crate_end[0].isalpha():
				# Have to negate this to get a true comparison. Right now, the first comparison value is being used as an index.
				if -(-2 + non_empty_crate_end_index + crate_end_counter) >= stack_row_index_length:
					stack_rearranged.insert(0, [[] for _ in range(2)])
					crate_end_counter = 0
					print("once")
					crate_end = stack_rearranged[-2 + non_empty_crate_end_index + crate_end_counter][end_location]


				else:
					stack_rearranged[-2 + non_empty_crate_end_index + crate_end_counter][end_location][0] = stack_rearranged[0 + non_empty_crate_start_index + crate_start_counter][start_location][0]
					stack_rearranged[0 + non_empty_crate_start_index + crate_start_counter][start_location][0] = " "
					crate_end = stack_rearranged[-2 + non_empty_crate_end_index + crate_end_counter][end_location]
	
				crate_end_counter -= 1

			crate_counter += 1

	print("===========================")


	for index in remapped_crate_indices:
		for row in stack_rearranged:
			print(row[int(index)])
		print("")

stack_drawing = generate_clean_stack_drawing(stack_drawing)

stack_directions = generate_clean_stack_directions(stack_directions)

move_crates(stack_drawing, stack_directions)
# Part 2
# Answer:
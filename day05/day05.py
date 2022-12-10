import re

# Part 1
# Answer: QNHWJVJZW
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()

# # Test Data: Answer should be CMZ.
# with open("test_input.txt") as f_handle:
# 	f_content = f_handle.readlines()

separator = f_content.index("\n")

stack_drawing = []
stack_drawing.extend(f_content[0:separator])

stack_directions = []
stack_directions.extend(f_content[separator + 1:])

stack_rearranged = []

remapped_crate_indices = []


def generate_clean_stack_drawing(stack_drawing):
	"""
	Clean up stack drawing from input file and ready it for processing.
	"""
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
	"""
	Clean up stack directions from input file and ready it for processing.
	"""
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
	stack_row_index_length = len(stack_rearranged)
	stack_column_index_length = len(stack_rearranged[-1])
	remapped_crate_indices = remap_crate_indices(stack_rearranged)

	for stack_direction in stack_directions:
		quantity = int(stack_direction[0])

		# Subtract 1 to turn into an index that can be map to the remapped indices.
		start_location = remapped_crate_indices[int(stack_direction[1]) - 1]
		end_location = remapped_crate_indices[int(stack_direction[2]) - 1]
		
		crate_counter = 0

		while crate_counter != quantity:
			# Start from the top. Do not include the last row as that does not contain any crate information.
			start_row_index = 0
			for row_index in range(0, stack_row_index_length - 1):
				if stack_rearranged[row_index][start_location][0].isalpha():
					start_row_index = row_index
					break

			# Start from the bottom. Do not include the last row as that does not contain any crate information.
			end_row_index = 0
			for row_index in range(2, stack_row_index_length + 1):
				if not stack_rearranged[-row_index][end_location][0].isalpha():
					end_row_index = -row_index
					break

				# Add new row if the column needed for the new crate is already occupied.	
				elif row_index >= stack_row_index_length:
					inverse_row_index = -row_index
					stack_rearranged.insert(inverse_row_index, [[" "] for _ in range(stack_column_index_length)])
					stack_row_index_length = len(stack_rearranged)
					end_row_index = inverse_row_index - 1
					# Because a new row was inserted the start row index needs to be incremented to account for the shifting of rows to make room for the additional crate.
					start_row_index = start_row_index + 1
					break

			# Logic for moving the crates around, one by one.
			stack_rearranged[end_row_index][end_location][0] = stack_rearranged[start_row_index][start_location][0]
			stack_rearranged[start_row_index][start_location][0] = " "

			crate_counter += 1

	# print("==========")
	# for index in remapped_crate_indices:
	# 	for row in stack_rearranged:
	# 		print(row[int(index)])
	# print("==========")

	return (stack_rearranged, remapped_crate_indices)


def reveal_message(stack_rearranged, remapped_crate_indices):
	"""
	Figures out the crate at the very top of each stack (column) and combines the result in order to reveal the message.
	"""
	top_crates = []
	for index in remapped_crate_indices:
		for row in stack_rearranged:
			if row[int(index)][0].isalpha():
				top_crates.append(row[int(index)][0])
				break

	return "".join(top_crates)

stack_drawing = generate_clean_stack_drawing(stack_drawing)

stack_directions = generate_clean_stack_directions(stack_directions)

stack_rearranged, remapped_crate_indices = move_crates(stack_drawing, stack_directions)

print(reveal_message(stack_rearranged, remapped_crate_indices))

# Part 2
# Answer:
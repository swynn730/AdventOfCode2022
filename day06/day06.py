# Part 1
# Answer: 1850
# Comment out ELVEN_PROTOCOL = 14 to print out the answer for this one.
with open("input.txt") as f_handle:
	f_content = f_handle.read()

# Test Data: 
# # Answer should be 7.
# f_content = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# # Answer should be 5.
# f_content = "bvwbjplbgvbhsrlpgdmjqwftvncz"

# # Answer should be 6.
# f_content = "nppdvjthqldpwncqszvftbrmjlhg"

# # Answer should be 10.
# f_content = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

# # Answer should be 11.
# f_content = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

# For part 1 solution (packet marker).
ELVEN_PROTOCOL = 4

# For part 2 solution (message marker).
ELVEN_PROTOCOL = 14

f_content_length = len(f_content)

marker_found = False

marker_position = 0

for char_index in range(f_content_length):
	char_count_forwards = 0
	find_marker = []

	if marker_found:
		break
	else:
		# Based on the protocol (packet OR message marker); start looking for the marker at the major indices.
		# Example: (0, 4, 8, 12, etc.) for a packet marker.
		if char_index % ELVEN_PROTOCOL == 0:
			while char_count_forwards != ELVEN_PROTOCOL:
				# Starting at that major index, search forward and then backwards based on the established protocol.
				starting_char_index = char_index + char_count_forwards
				starting_char = f_content[starting_char_index]

				# Keep track of the search results.
				for i in range(ELVEN_PROTOCOL):
					find_marker.append(f_content[abs(starting_char_index - i)])

				# If there are no duplicates in the results, the marker that follows the established protocol has been found.
				if len(set(find_marker)) == ELVEN_PROTOCOL:
					marker_found = True

					# Have to add a 1 to convert from index to... actual "number"? 
					marker_position = starting_char_index + 1
					break

				find_marker = []
				char_count_forwards += 1

			char_count_forwards = 0


print(marker_position)


# Part 2
# Answer: 2823
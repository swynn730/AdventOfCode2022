# Part 1
# Answer: 582
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()

# # Test Data: Answer should be 2.
# f_content = [
# "2-4,6-8",
# "2-3,4-5",
# "5-7,7-9",
# "2-8,3-7",
# "6-6,4-6",
# "2-6,4-8"
# ]

overlapping_shifts = 0

for line in f_content:
	line = line.strip()
	first_elf_shift_full, second_elf_shift_full = line.split(",")

	first_elf_shift_start, first_elf_shift_end = first_elf_shift_full.split("-")
	second_elf_shift_start, second_elf_shift_end = second_elf_shift_full.split("-")

	# Adding 1 so that the full range is captured.
	first_elf_shift_expanded = list(range(int(first_elf_shift_start), int(first_elf_shift_end) + 1))
	second_elf_shift_expanded = list(range(int(second_elf_shift_start), int(second_elf_shift_end) + 1))

	# Converting to throwaway sets to make finding the overlapping shifts easier and cleaner.
	fese_set = set(first_elf_shift_expanded)
	sefse_set = set(second_elf_shift_expanded)

	if set(fese_set).issubset(sefse_set) or set(sefse_set).issubset(fese_set):
		overlapping_shifts += 1

print(overlapping_shifts)

# Part 2
# Answer: 893

# # Test Data: Answer should be 4.
# f_content = [
# "2-4,6-8",
# "2-3,4-5",
# "5-7,7-9",
# "2-8,3-7",
# "6-6,4-6",
# "2-6,4-8"
# ]

overlapping_shifts = 0

for line in f_content:
	line = line.strip()
	first_elf_shift_full, second_elf_shift_full = line.split(",")

	first_elf_shift_start, first_elf_shift_end = first_elf_shift_full.split("-")
	second_elf_shift_start, second_elf_shift_end = second_elf_shift_full.split("-")

	# Adding 1 so that the full range is captured.
	first_elf_shift_expanded = list(range(int(first_elf_shift_start), int(first_elf_shift_end) + 1))
	second_elf_shift_expanded = list(range(int(second_elf_shift_start), int(second_elf_shift_end) + 1))

	# Converting to throwaway sets to make finding the intersecting shift times easier and cleaner.
	fese_set = set(first_elf_shift_expanded)
	sefse_set = set(second_elf_shift_expanded)

	if set(fese_set).intersection(sefse_set):
		overlapping_shifts += 1

print(overlapping_shifts)
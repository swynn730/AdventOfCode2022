# Part 1
# Answer: 8053
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()

# # Test Data: Answer should be 157.
# f_content = [
# "vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw"]

priority_mapping_lower = "abcdefghijklmnopqrstuvwxyz"
priority_mapping_upper = priority_mapping_lower.upper()
priority_mapping = priority_mapping_lower + priority_mapping_upper

priority_sum = 0

for line in f_content:
	line = line.strip()
	rucksack_item_size = len(line)
	rucksack_compartment_01 = line[:int(rucksack_item_size/2)]
	rucksack_compartment_02 = line[int(rucksack_item_size/2):rucksack_item_size]
	common_item = list(set(rucksack_compartment_01).intersection(set(rucksack_compartment_02)))[0]

	# Adding 1 because in programming indices start at 0 and we need to remap that to 1 for this problem.
	priority_mapping_index = priority_mapping.index(common_item) + 1

	priority_sum += priority_mapping_index

print(priority_sum)

# Part 2
# Answer: 2425

# # Test Data: Answer should be 70.
# f_content = [
# "vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw"]

MAX_ELVES_IN_GROUP = 3
elf_groups = []
elf_group = []
elf_count = 1

priority_sum = 0

for line in f_content:
	line = line.strip()

	elf_group.append(line)

	# Put 3 elves (rucksacks) in a group and keep track of all the groups.
	if (elf_count % MAX_ELVES_IN_GROUP) == 0:
		elf_groups.append(elf_group)
		elf_group = []

	elf_count += 1

for elf_group in elf_groups:
	common_group_item = []
	rucksack_group = []
	for rucksack in elf_group:
		rucksack_group.append(set(rucksack))
	common_group_item = list(set.intersection(*rucksack_group))
	common_group_item = common_group_item[0]

	# Adding 1 because in programming indices start at 0 and we need to remap that to 1 for this problem.
	priority_mapping_index = priority_mapping.index(common_group_item) + 1

	priority_sum += priority_mapping_index

print(priority_sum)
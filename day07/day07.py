# Part 1
# Answer: 
with open("input.txt") as f_handle:
	f_content = f_handle.read()

# file_system["root"].append(("file_01", 80000))
# file_system["root"].append(("file_02", 40000))
# file_system["root"].append({"a":[]})
# file_system["root"][2]["a"].append(("file_03", 160000))
# file_system["root"][2]["a"].append(("file_04", 320000))

# file_system["root"][2]["a"].append({"b":[]})

# file_system["root"][2]["a"][2]["b"].append(("file_05", 640000))

# Test Data: 
f_content = [
"$ cd /",
"$ ls",
"dir a",
"14848514 b.txt",
"8504156 c.dat",
"dir d",
"$ cd a",
"$ ls",
"dir e",
"29116 f",
"2557 g",
"62596 h.lst",
"$ cd e",
"$ ls",
"584 i",
"$ cd ..",
"$ cd ..",
"$ cd d",
"$ ls",
"4060174 j",
"8033020 d.log",
"5626152 d.ext",
"7214296 k"]

ROOT_DIRECTORY = "/"

file_system = {ROOT_DIRECTORY:[]}

current_directory_contents = file_system[ROOT_DIRECTORY]

current_directory_name = ROOT_DIRECTORY


def change_current_directory_contents(current_directory_name, current_directory_contents, directory_target_command):
	
	if directory_target_command == "..":
		# Moves out one level.
		pass
		# for i in current_directory_contents:
		#     if isinstance(i, dict):
		#     	current_directory_contents_index = current_directory_contents.index(i)
		#     	current_directory_contents = current_directory_contents[current_directory_contents_index][directory_target_command]
		#     	current_directory_name = current_directory_contents[current_directory_contents_index]


	elif directory_target_command == "/":
		# Switches the current directory to the outermost directory.
		current_directory_contents = file_system[ROOT_DIRECTORY]
		current_directory_name = ROOT_DIRECTORY
	else:
		# Moves in one level.
		for i in current_directory_contents:
			print(i)
			# if isinstance(i, dict):
			# 	current_directory_contents_index = current_directory_contents.index(i)
			# 	current_directory_contents = current_directory_contents[current_directory_contents_index][directory_target_command]
			# 	current_directory_name = current_directory_contents[current_directory_contents_index]

	# print(current_directory_name)
	# print(current_directory_contents)
	# print("======")
	# print()
	return (current_directory_name, current_directory_contents)


def walk_current_directory_contents(current_directory_contents, depth=0):
	for directories, files in current_directory_contents.items():
		print(directories.rjust(depth))
		for file in files:
			if isinstance(file, dict):
				walk_current_directory_contents(file, depth=depth + 2)
			else:
				print(str(file).rjust(depth + 18))


def make_file_system(file_system, current_directory_name, current_directory_contents):
	newly_created_directory_contents = ""
	current_directory_name = current_directory_name

	for line in f_content:
		split_line = line.split()
		if "$" in split_line:
			# User command entered.
			if "cd" in split_line:
				user_commands["cd"](current_directory_name, current_directory_contents, split_line[2])
				pass
			elif "ls" in split_line:
				pass
				# print(current_directory_contents)
				# print(current_directory_name)

		elif len(split_line) >=2:
			# It is a directory or file.
			if "dir" in split_line:
				# Create new directory.
				current_directory_contents.append({split_line[1]:[]})
				current_directory_name = split_line[1]
				newly_created_directory_contents = current_directory_contents[-1]

			else:
				# Create new file.
				newly_created_directory_contents[current_directory_name].append((split_line[1], split_line[0]))
				#current_directory_contents.append((split_line[1], split_line[0]))

	# print(current_directory_name)
	# print(current_directory_contents)
	return (current_directory_name, current_directory_contents)

user_commands = {"cd":change_current_directory_contents, "ls": walk_current_directory_contents}

current_directory_name, current_directory_contents = make_file_system(file_system, current_directory_name, current_directory_contents)

#walk_current_directory_contents(file_system)

# print(file_system["/"])
# print()
# print(file_system["/"][-1]["a"])
# print()
# print(file_system["/"][-1]["a"][-1]["e"])
# print()
# print(file_system["/"][-1]["d"])
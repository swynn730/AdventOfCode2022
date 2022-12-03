# Part 1
# Answer:
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()

for line in f_content:
	line = line.strip()
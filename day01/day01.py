# Part 1
# Answer: 66719
elven_packs = []
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()
	eleven_pack = []
	for line in f_content:
		line = line.strip()
		if len(line) == 0:
			elven_packs.append(eleven_pack)
			eleven_pack = []
		else:	
			eleven_pack.append(int(line))

highest_caloric_value = 0
for elven_pack in elven_packs:
	elven_pack_caloric_value = sum(elven_pack)
	if elven_pack_caloric_value > highest_caloric_value:
		highest_caloric_value = elven_pack_caloric_value

print(highest_caloric_value)

# Part 2
# Answer: 198551
caloric_values = []
for elven_pack in elven_packs:
	caloric_values.append(sum(elven_pack))
	caloric_values.sort()

print(sum(caloric_values[-3:]))
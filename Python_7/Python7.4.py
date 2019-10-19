#!/usr/bin/env python3
import re

with open("Python7.3input.txt") as Input:
	for line in Input:
		if re.search(r"^>\S+", str(line)):
			match = (re.match(r"(^>\S+)(.+)", str(line)))
			print(match.group(0))
			print(match.group(1))
			print(match.group(2))
		



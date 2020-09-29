#!/usr/bin/python3
import os
import sys
import re

def parse(input_file):
	# Using readline() 
	file = open(input_file, 'r') 
	count = 0
	
	# Example
	# 09:46:01	 From Luke Farmer to Mark Kwong (Privately) : Mr. Kwong im leaving the meeting to restart my camera
	# Regex expression 
	# (\d\d:\d\d:\d\d)	 From ([a-zA-Z\. \u4e00-\u9fff]+?)( to ([a-zA-Z\. ]+? )?(\(Privately\))?)? : (.+)

	# 1.	09:46:01
	# 2.	Luke Farmer
	# 3.	to Mark Kwong (Privately)
	# 4.	Mark Kwong
	# 5.	(Privately)
	# 6.	Mr. Kwong im leaving the meeting to restart my camera

	# Data structure: Dictionary (key: sender_name, value: array of messages)
	regex_expression = r'(\d\d:\d\d:\d\d)	 From ([a-zA-Z\. \u4e00-\u9fff]+?)( to ([a-zA-Z\. ]+? )?(\(Privately\))?)? : (.+)'

	dictionary = {}

	while True: 
		count += 1

		# Get next line from file 
		line = file.readline() 
		# if line is empty 
		# end of file is reached 
		if not line: 
			break
		else:
			groups = re.match(regex_expression, line)
			if groups:
				date = groups.group(1)
				sender = groups.group(2)
				message = groups.group(6)
			if sender not in dictionary:
				dictionary[sender] = [message]
			else:
				dictionary[sender].append(message)

	file.close() 
	print("Name: # of responses")
	print("--------------------")
	for key in sorted(dictionary):
		print("{}: {}".format(key, str(len(dictionary[key]))))



def main():

	parse(sys.argv[1])
	
main()

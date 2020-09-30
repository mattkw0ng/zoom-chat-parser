#!/usr/bin/python3
import os
import sys
import re

def process(database, teacher, override):
	print("Teacher: {}\n".format(teacher))
	i = 0
	dictionary = {}
	collect_data = False

	while i < len(database) :
		chat = database[i]
		message = chat['message']
		sender = chat['sender']

		if (message == 'start' and sender == teacher):
			collect_data = True
		elif (message == 'end' and sender == teacher):
			collect_data = False
		elif collect_data or override:
			if sender != teacher:
				if sender in dictionary:
					dictionary[sender].append(message)
				else:
					dictionary[sender] = [message]
		i += 1

	
	print("Name: # of responses")
	print("--------------------")
	for key in sorted(dictionary):
		print("{}: {}".format(key, str(len(dictionary[key]))))


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

	
	database = []
	# array of dictionaries with a date, sender, and message

	while True: 
		count += 1

		# Get next line from file 
		line = file.readline() 
		# if line is empty 
		# end of file is reached 
		teacher = ''
		if not line: 
			break
		else:
			groups = re.match(regex_expression, line)
			if groups:
				date = groups.group(1)
				sender = groups.group(2)
				message = groups.group(6)
				temp_dict = {'date': date, 'sender': sender, 'message': message}
				database.append(temp_dict)


	file.close() 
	if len(sys.argv) > 3 and sys.argv[3] == '-all':
		process(database, sys.argv[2], True)
	else:
		process(database, sys.argv[2], False)
	



def main():
	# python3 zoom_chat_parser.py zoom_chat.txt "Mark Kwong" (OPTION: override)
	parse(sys.argv[1])
	
main()

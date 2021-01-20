#!/usr/bin/python3
import os
import sys
import re

def combined_process(database, teacher, override):
    i = 0
    dictionary = {}
    collect_data = False

    while i < len(database) :
        chat = database[i]
        message = chat['message']
        sender = chat['sender']

        if ( re.match('start', message, re.IGNORECASE) and sender == teacher):
            collect_data = True
        elif ( re.match('end', message, re.IGNORECASE) and sender == teacher):
            collect_data = False
        elif collect_data or override:
            if sender != teacher:
                name_reformatted = reformat_name(sender)
            if name_reformatted in dictionary:
                dictionary[name_reformatted].append(message)
            else:
                dictionary[name_reformatted] = [message]
                i += 1
    return dictionary

def print_combined(dictionary):
    print("--------------------")
    print("Name: # of responses")
    print("--------------------\n")
    for key in sorted(dictionary,  key=str.casefold):
        print("{}: {}".format(key, len(dictionary[key])))
    print()


# Calculates participation during chat sessions
# Records the students and their number of participations
def calculate_participation(database, teacher):
    print("\n--------------------")
    print("Calculating participation")
    print("--------------------\n")
    i = 0

    dictionary = {}
    collect_data = False
    participation_list = []
    chat_session = 0

    while i < len(database) :
        chat = database[i]
        message = chat['message']
        sender = chat['sender']

        # Start recording chat responses
        if ( re.match('start', message, re.IGNORECASE) and sender == teacher):
            collect_data = True
            chat_session += 1
        # Stop recording | add all participants to dictionary and print to console
        elif ( re.match('end', message, re.IGNORECASE) and sender == teacher):
            collect_data = False
            print("Participants for chat session {}:".format(chat_session))
            for person in participation_list:
                # Reformat the names
                name_reformatted = reformat_name(person)
                # Print and add names to the dictionary
                print("- {} ({})".format(name_reformatted, person))
                if name_reformatted in dictionary:
                    dictionary[name_reformatted] += 1
                else:
                   dictionary[name_reformatted] = 1
            print()
            # Clear the list to restart
            participation_list.clear()
        # Add participant to list
        elif collect_data:
            if sender != teacher and sender not in participation_list:
                participation_list.append(sender)
        i += 1

    print_participation(dictionary, chat_session)
    return dictionary

# Prints each student's participation percentage based on the total chat sessions
def print_participation(dictionary, total_chat_sessions):
    print("\n--------------------")
    print("Participation percentages")
    print("--------------------\n")
    for key in sorted(dictionary,  key=str.casefold):
        participation = dictionary.get(key)
        percentage = (participation/total_chat_sessions)*100
        print("{}: {:.2f}% \t({}/{})".format(key, percentage, participation, total_chat_sessions))
    print()

# Reformats the name by placing the first name behind the last | Matthew Kwong --> Kwong, Matthew
def reformat_name(name):
    name_separated = name.split(" ", 1)
    name_reformatted = "{}, {}".format(name_separated[1], name_separated[0])
    return name_reformatted

def parse(input_file):
    # Using readline() 
    file = open(input_file, 'r') 
    count = 0

    # Example
    # 09:46:01	 From Luke Farmer to Mark Kwong (Privately) : Mr. Kwong im leaving the meeting to restart my camera
    # Regex expression 
    # (\d\d:\d\d:\d\d)	 From ([a-zA-Z\. \u4e00-\u9fff]+?)( to ([a-zA-Z\. ]+? )?(\(Privately\))?)? : (.+)

    # Data structure: Dictionary (key: sender_name, value: array of messages)
    regex_expression = r'(\d\d:\d\d:\d\d)\s+From ([a-zA-Z\. \u4e00-\u9fff]+?)( to ([a-zA-Z\. \u4e00-\u9fff]+?)(\(Direct Message\))?(\(Privately\))?)? : (.+)'


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
                message = groups.group(7)
                temp_dict = {'date': date, 'sender': sender, 'message': message}
                database.append(temp_dict)


    file.close() 


    if len(sys.argv) > 3:
        dictionary = {}
        if sys.argv[3] == '-combined':
            dictionary = combined_process(database, sys.argv[2], False)
        elif  sys.argv[3] == '-all':
            dictionary = combined_process(database, sys.argv[2], True)
        print_combined(dictionary)

    else:
        calculate_participation(database,  sys.argv[2])

    print("Teacher: {}\n".format(sys.argv[2]))



def main():
    # python3 zoom_chat_parser.py zoom_chat.txt "Mark Kwong" (OPTION: override)
    parse(sys.argv[1])

main()

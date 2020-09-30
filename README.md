# zoom-chat-parser
Takes in zoom chat .txt file and prints the name of each student found and the number of times they responded in the chat

**UPDATE (v2.0)** Parser now excluded the Teacher's name from the zoom file and allows you to specify when to record student responses
- Runs with command: 
```
python3 zoom_chat_parser.py zoom_chat_file.txt "TEACHER_NAME" (OPTIONAL FLAG -all)
```

**Notes**
- Include your name/username as it is shown in the Zoom chat text file in the place of *TEACHER_NAME* (NOTE: use quotes around the name i.e. "Johnny A.")

- To specify a certain time window to record responses, type "start" and "end" in the Zoom chat and the parser will only record the student responses within that time frame.
- If you were not able to do this during the zoom call, you can edit the raw .txt file and insert these lines where you would like to start and stop the record
- Copy and paste from below and replace *TEACHER_NAME* with your username and Make sure not to add any extra spaces
```
00:00:00	 From TEACHER_NAME : start
00:00:00	 From TEACHER_NAME : end
```

- If you do not want this feature and would like everything to be recorded, add the optional flag *-all* to the command line arguments

# zoom-chat-parser
Takes in zoom chat .txt file and prints the name of each student found and the number of times they responded in the chat

**UPDATE (v2.0)** Parser now ignores the Teacher's chats and allows you to specify when to record student responses

**UPDATE (v3.0)** Default parsing method now tracks student participation during the specified chat sessions. 
- Prints a summary of who participated in each individual chat session as well as an overall summary of each student's participation across all of the sessions. 
- The 'start' and 'end' commands are now case-insensitive to allow flexibility. 
- The previous method of parsing is no longer the default, but is still available by using the flag *-combined*.

**Terminal command**
```
python3 zoom_chat_parser.py ZOOM_CHAT_FILE.txt "TEACHER_NAME" (optional flags: -combined, -all)
```

**Notes**
- Include your name/username as it is shown in the Zoom chat text file in the place of *TEACHER_NAME* (NOTE: use quotes around the name i.e. "Johnny A.")

- To specify a certain time window to record responses, type "start" and "end" in the Zoom chat and the parser will only record the student responses within that time frame. This can be done multiple times to create numerous 'chat sessions'. 
- If you were not able to do this during the zoom call, you can edit the raw .txt file and insert these lines where you would like to start and stop the record
- Copy and paste from below and replace *TEACHER_NAME* with your username (make sure not to add any extra spaces)
```
00:00:00	 From TEACHER_NAME : start
00:00:00	 From TEACHER_NAME : end
```

- If you do not want this feature and would like everything to be recorded, add the optional flag *-all* to the command line arguments

* Task name => name of the task
* Task preparation => what preparation is necessary to perform the task? (short)
* Task implementation => what is the way you have implemented the task?
* Task troubleshooting => what were the problems encountered?
  * Requests-module wasn't installed in my conda environment. PIPped.

* Task verification => proof of the quality of the result

===



>Task name: Webex

>Task Description

Create Webex Teams API calls using a Python script

>Task Execution

1. Create or adapt an existing Python script to create a Webex Teams space with the name “netacad_devasc_skills_{{initials}}” with yourself (initials) and <yvan.rooseleer@biasc.be> as the members
2. Publish the url of your github remote repository (task 1 of the skills exam) in this new Webex Teams space
3. Create (or adapt) an existing Python script that sends a message “Here are my screenshots of netacad-devasc skills-based exam” to the new space
4. Upload one screenshot of every task to the Webex Teams Space





Oof. This was a little PITA. At the end, the script "Create WebEx Rooms.py" contains all the scripting necessary.

It is a little bit hairy though. I tried to have everything in functions, but I need to rework those. I pushed one picture with the webex-room and the script in the backend.



Most of the script came from http://infotinks.com/simple-python-script-to-find-room-by-name-and-send-message-to-it/. Debugging done: create a lot of rooms ;)
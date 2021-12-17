* Task name => name of the task
* Task preparation => what preparation is necessary to perform the task? (short)
* Task implementation => what is the way you have implemented the task?
* Task troubleshooting => what were the problems encountered?
* Task verification => proof of the quality of the result



===



>Task name: Bash

>Task Desciption

Translate the given Python script into an equivalent bash script. URL of the input file: restconf_put_get_interface.py Tip: For the REST API call it is possible to use curl.

>Task Execution 1. Preparation Explore the given Python script and run the Python script to observe the output.

Prepare a Linux environment in which you can create a bash script that is able to connect to the given host.

2. Bash script characteristics

a. Name of the bash script: restconf_api.sh

b. Make the script executable

c. The bash script needs make two API calls and output the requested information

d. After creating and testing the bash script, copy and upload the bash script to your GitHub repo, also copy and upload the output file to your GitHub repo

3. Bash script output Output needs to be redirected to a file named check_restconf_api.txt The bash script needs to create the following output

a. First line of output: today’s date

b. Next line of output: ‘START REST API CALL’

c. ============

d. Next line of output: ‘FIRST API CALL’

e. ============

f. Status Code: (realtime output)

g. ============

h. Next line of output: ‘SECOND API CALL’

i. ============

j. Status Code: (realtime output)

k. Interfaces: (realtime output)

l. Last line of output: ‘END REST API CALL’

4. Screenshot Upload a screenshot of a relevant part of the bash script output to the Webex Teams Space
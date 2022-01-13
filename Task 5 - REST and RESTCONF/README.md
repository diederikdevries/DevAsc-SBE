* Task name => name of the task
* Task preparation => what preparation is necessary to perform the task? (short)
* Task implementation => what is the way you have implemented the task?
* Task troubleshooting => what were the problems encountered?
* Task verification => proof of the quality of the result



===

**NOTE TO SELF: URL's ARE IN THE PDF!**

>Task name: restconf

>Task Description Create a Python script based on curl command examples

Virtual router: curl => Python Use your virtual DEVASC virtual machine as well as your virtual CSR1Kv router

>Task Execution

1. Test the curl instructions presented from page 7 to 9 in the URL RESTCONF Protocol below

2. It will be sufficient to transform three curl commands in to restconf.

3. Transform the curl commands into Python code. In case of errors, use a quick fix to activate “logging monitor” using the cisco ios cli of your virtual router

4. Take screenshots indicating the success of your actions

5. Save the Python code on Github

>Task source files RESTCONF Protocol & curl

URL: RESTCONF Programmable Interface

More examples of curl and python scripting RESTCONF Tutorial - Everything you need to know about RESTCONF

URL: Everything you need to know about RESTCONF





# Options



Well, that wasn't difficult. Some reading on https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request

# Post

Ok, after enabling the logging monitor, the POST.py script works :)

devasc@labvm:~/cURL$ python3 /home/devasc/cURL/post.py
/usr/lib/python3/dist-packages/urllib3/connectionpool.py:999: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.56.101'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
<Response [201]>
{'Server': 'nginx', 'Date': 'Mon, 20 Dec 2021 11:58:00 GMT', 'Content-Type': 'text/html', 'Content-Length': '0', 'Location': 'https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity', 'Connection': 'keep-alive', 'Last-Modified': 'Mon, 20 Dec 2021 11:58:00 GMT', 'Cache-Control': 'private, no-cache, must-revalidate, proxy-revalidate', 'Etag': '1640-1480-724819', 'Pragma': 'no-cache'}
devasc@labvm:~/cURL$ 




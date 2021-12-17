* Task name => Ansible
* Task preparation => what preparation is necessary to perform the task? (short)
  I needed to start my Windows PC, connect via Remote Desktop, and start the VM's
* Task implementation => what is the way you have implemented the task?
* Task troubleshooting => what were the problems encountered?
  Probably due to an update to Windows 11, I fail to start the VM's. Argh! Upgrade to 6.1.30 might help?
* Task verification => proof of the quality of the result



===



>Task name: Ansible

>Task Description Manage Ansible scripts

>Task Execution

1. Connect to your DEVASC virtual machine
2. Create an Ansible playbook to gather information about your router:
   a. Show version
   b. Show interfaces
   c. Clear counters

3. Adapt the Ansible script described in the url under task source file in such a way that it can be executed as a playbook

4. Name the playbook ios_status

5. Run the playbook in your DEVASC virtual machine

6. Three tasks (out of the five tasks) need to succeed

7. Take screenshots indicating the success of your actions, save and upload your script files
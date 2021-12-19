* Task name => Ansible
* Task preparation => what preparation is necessary to perform the task? (short)
  I needed to start my Windows PC, connect via Remote Desktop, and start the VM's
  I need credentials (cisco:cisco123!) to login with SSH

* Task implementation => what is the way you have implemented the task?
* Task troubleshooting => what were the problems encountered?

  1. Probably due to an update to Windows 11, I fail to start the VM's. Argh! Upgrade to 6.1.30 might help?
  2. Due to a BIOS-update, I suspect the BIOS to having disabled VMM.
  3. Bios-settings changed. Fixed. Back to work!
  
* Task verification => proof of the quality of the result



===



>Task name: Ansible

>Task Description Manage Ansible scripts

>Task Execution

1. Connect to your DEVASC virtual machine

Done. I'm able to ping the CSR on 192.168.56.101

2. Create an Ansible playbook to gather information about your router:
   a. Show version
   b. Show interfaces
   c. Clear counters

I need to run scripts that are available on https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_command_module.html#examples. I have written some ansible-scripts to update virtualized Linux machines. Let's add some of those. The playbook now has a CSR-group. Does the playbook have the right plugin?



*`devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ ansible-galaxy list*`
`*[WARNING]: - the configured path /home/devasc/.ansible/roles does not exist.*`
`*[WARNING]: - the configured path /usr/share/ansible/roles does not exist.*`
`*[WARNING]: - the configured path /etc/ansible/roles does not exist.*`
`*usage: ansible-galaxy [-h] [--version] [-v] TYPE ...*`

`*Perform various Role and Collection related operations.*`

`*positional arguments:*`
  `*TYPE*`
    `*collection   Manage an Ansible Galaxy collection.*`
    `*role         Manage an Ansible Galaxy role.*`

`*optional arguments:*`
  `*--version      show program's version number, config file location, configured module search path, module location, executable location and exit*`
  `*-h, --help     show this help message and exit*`
  `*-v, --verbose  verbose mode (-vvv for more, -vvvv to enable connection debugging)*`
`*ERROR! - None of the provided paths was usable. Please specify a valid path with --roles-path*`
`*devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$*` 

Doesn't seem to be installed. Lets try to install it:



```
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ ansible-galaxy collection install cisco.ios
Process install dependency map
Starting collection install process
Installing 'cisco.ios:2.6.0' to '/home/devasc/.ansible/collections/ansible_collections/cisco/ios'
Installing 'ansible.netcommon:2.5.0' to '/home/devasc/.ansible/collections/ansible_collections/ansible/netcommon'
Installing 'ansible.utils:2.4.3' to '/home/devasc/.ansible/collections/ansible_collections/ansible/utils'
```



Bingo?  With the documentation, it seems that *network_cli* is used for connecting...

The documentation is clear, but my lack of ansible-understanding shows. Eventually, I'm able to reach the CSR:



devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ ansible-playbook -i hosts facts-demo.yml 

PLAY [Demonstrate connecting to switches] **************************************************************************************************************

TASK [Gather facts (ios)] ******************************************************************************************************************************
ok: [virtual-router]

PLAY RECAP *********************************************************************************************************************************************
virtual-router             : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ ansible-playbook -i hosts facts-demo.yml 

PLAY [Demonstrate connecting to switches] **************************************************************************************************************

TASK [Gather facts (ios)] ******************************************************************************************************************************
ok: [virtual-router]

PLAY RECAP *********************************************************************************************************************************************
virtual-router             : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   



From here, I deleted a lot of swearing in this document. Saviour came from https://www.packetswitch.co.uk/ansible-with-cisco/. I had a fair share of YAML learning :)



14:30 and make that also Ansible learning ;)

Done! Happy with the script. Things that COULD be improved: password management in the vault.

Pic:

![Proof of work](/Users/diederik/Documents/DevNet/Exam/Task 2 - Ansible/Proof of work.png)

3. Adapt the Ansible script described in the url under task source file in such a way that it can be executed as a playbook

4. Name the playbook ios_status

5. Run the playbook in your DEVASC virtual machine

6. Three tasks (out of the five tasks) need to succeed

7. Take screenshots indicating the success of your actions, save and upload your script files
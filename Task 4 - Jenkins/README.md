* Task name => name of the task
* Task preparation => what preparation is necessary to perform the task? (short)
* Task implementation => what is the way you have implemented the task?
* Task troubleshooting => what were the problems encountered?
* Task verification => proof of the quality of the result

This one is going to be fun. I have a running Jenkins on my server in Amsterdam, which I want to abuse for this :)

Let's start Jenkins, and first update it with Ansible (hey, learning stuff here :))

```
(base) diederik@Mac-mini ~ % sd
Last login: Sun Dec 19 13:11:44 2021 from 2a10:3781:7e1:0:1d86:798a:3327:3f03
FreeBSD 13.0-RELEASE-p4 (GENERIC) #0: Tue Aug 24 07:33:27 UTC 2021
Welkom!
Diederik
$ sudo bash
Password:
[root@pandora /usr/home/diederik]# vm list
NAME              DATASTORE  LOADER     CPU  MEMORY  VNC  AUTOSTART  STATE
caddy             default    bhyveload  1    512M    -    No         Locked (pandora.diedx.nl)
devnet-test       default    grub       1    1024M   -    No         Stopped
freebsd           default    bhyveload  1    256M    -    No         Stopped
freebsd-template  default    bhyveload  1    256M    -    No         Stopped
gitlab            default    grub       2    4096M   -    Yes [1]    Running (29955)
jenkins           default    grub       1    1024M   -    No         Stopped
mongodb           default    bhyveload  1    1024m   -    No         Stopped
opendag1          default    bhyveload  1    1024m   -    No         Stopped
ubuntu            default    grub       1    1024M   -    No         Stopped
[root@pandora /usr/home/diederik]# vm start jenkins
Starting jenkins

  * found guest in /tweede/vms/jenkins
  * booting...
    [root@pandora /usr/home/diederik]# cd /usr/local/etc/nginx/
    [root@pandora /usr/local/etc/nginx]# ls -al
    total 242
    drwxr-xr-x   4 root  wheel    18 Dec 18 04:30 .
    drwxr-xr-x  46 root  wheel   115 Dec 19 15:16 ..
    drwxr-xr-x   3 root  wheel    19 Dec  6 17:31 VHOSTS
    drwxr-xr-x   2 root  wheel     7 Dec 22  2020 VHOSTS_OUD
    -rw-r--r--   1 root  wheel  1007 Dec  9 10:48 fastcgi_params
    -rw-r--r--   1 root  wheel  1007 Dec  9 10:48 fastcgi_params-dist
    -rw-r--r--   1 root  wheel  2837 Dec  9 10:48 koi-utf
    -rw-r--r--   1 root  wheel  2223 Dec  9 10:48 koi-win
    -rw-r--r--   1 root  wheel  5235 Oct 21  2019 mime.types
    -rw-r--r--   1 root  wheel  5349 Dec  9 10:48 mime.types-dist
    -r--r--r--   1 root  wheel   459 Nov 25 14:23 nginx.conf
    -rw-r--r--   1 root  wheel  2989 Dec  9 10:48 nginx.conf-dist
    -rw-r--r--   1 root  wheel   636 Dec  9 10:48 scgi_params
    -rw-r--r--   1 root  wheel   636 Dec  9 10:48 scgi_params-dist
    -rw-r--r--   1 root  wheel   664 Dec  9 10:48 uwsgi_params
    -rw-r--r--   1 root  wheel   664 Dec  9 10:48 uwsgi_params-dist
    -rw-r--r--   1 root  wheel  3610 Dec  9 10:48 win-utf
    -rw-r--r--   1 root  wheel   938 Mar 15  2020 ?
    [root@pandora /usr/local/etc/nginx]# cd /usr/local/etc/ansible/
    [root@pandora /usr/local/etc/ansible]# ls -al
    total 135
    drwxr-xr-x   3 root  wheel      7 Dec  2 20:41 .
    drwxr-xr-x  46 root  wheel    115 Dec 19 15:16 ..
    -rw-r--r--   1 root  wheel  20157 Jan  5  2021 ansible.cfg
    -rw-r--r--   1 root  wheel   1730 Dec  5 13:06 hosts
    -rw-r--r--   1 root  wheel    294 Jan  5  2021 playbook.yml
    -rw-r--r--   1 root  wheel    196 Dec  5 13:04 playbook_update_ubuntu.yml
    drwxr-xr-x   2 root  wheel      4 Jan  5  2021 scripts
    [root@pandora /usr/local/etc/ansible]# ansible-playbook playbook_update_ubuntu.yml

PLAY [Update all Ubuntu machines] ****************************************************************************************************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************************************************************************************************************************************************************************************************************
[WARNING]: Platform linux on host gitlab.intern.diederik.nl is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.11/reference_appendices/interpreter_discovery.html for more information.
ok: [gitlab.intern.diederik.nl]
[WARNING]: Platform linux on host jenkins.intern.diederik.nl is using the discovered Python interpreter at /usr/bin/python3.8, but future installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.11/reference_appendices/interpreter_discovery.html for more information.
ok: [jenkins.intern.diederik.nl]

TASK [Get config for VyOS devices] ***************************************************************************************************************************************************************************************************************************************************************************************************************************************
ok: [jenkins.intern.diederik.nl]
ok: [gitlab.intern.diederik.nl]

PLAY RECAP ***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
gitlab.intern.diederik.nl  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
jenkins.intern.diederik.nl : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

[root@pandora /usr/local/etc/ansible]#
```

To prevent issues (I don't use Jenkins on a daily base), I need to forward the port through a proxy. Let's enable the VHOST for Jenkins.diederik.nl



`[root@pandora /usr/local/etc/nginx/VHOSTS]# mv jenkins.diederik.nl.vhost.disabled jenkins.diederik.nl.vhost`
`[root@pandora /usr/local/etc/nginx/VHOSTS]# service nginx restart`
`Performing sanity check on nginx configuration:`
`nginx: the configuration file /usr/local/etc/nginx/nginx.conf syntax is ok`
`nginx: configuration file /usr/local/etc/nginx/nginx.conf test is successful`
`Stopping nginx.`
`Waiting for PIDS: 4026.`
`Performing sanity check on nginx configuration:`
`nginx: the configuration file /usr/local/etc/nginx/nginx.conf syntax is ok`
`nginx: configuration file /usr/local/etc/nginx/nginx.conf test is successful`
`Starting nginx.`
`[root@pandora /usr/local/etc/nginx/VHOSTS]#`

Up and running?

```
[root@pandora /usr/local/etc/nginx/VHOSTS]# ping jenkins.diederik.nl
PING6(56=40+8+8 bytes) 2a02:898:0:20::168:1 --> 2a02:898:0:20::168:1
16 bytes from 2a02:898:0:20::168:1, icmp_seq=0 hlim=64 time=0.106 ms
^C
--- jenkins.diederik.nl ping6 statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/std-dev = 0.106/0.106/0.106/0.000 ms
[root@pandora /usr/local/etc/nginx/VHOSTS]# ping jenkins.intern.diederik.nl
PING jenkins.intern.diederik.nl (10.30.0.102): 56 data bytes
64 bytes from 10.30.0.102: icmp_seq=0 ttl=64 time=0.327 ms
^C
--- jenkins.intern.diederik.nl ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.327/0.327/0.327/0.000 ms
[root@pandora /usr/local/etc/nginx/VHOSTS]#
```

I create a folder in Jenkins, and add a 'regular' project. This feels gory, but at the end: goal justify the means... Pulling works, but then I need to clean my Jenkins. Fixed by a checkbox.



3 days later I decided to look at the practices we had in the lessons. Am I able to repeat those? One hour later I had a working Jenkins pipeline, which triggers a Jenkins project. It even does work ;)







===



Task name: Jenkins

>Task Description

Create a CI/CD pipeline

>Task Execution

1. Create a Jenkins pipeline in which you download the necessary scripts and files from a GitHub repository and install the service from Task 3

-- Docker in a docker container

2. It is necessary to test the success of the deployment

3. Take screenshots indicating the success of your actions and save script files
* Task name => name of the task
* Task preparation => what preparation is necessary to perform the task? (short)
* Task implementation => what is the way you have implemented the task?
* Task troubleshooting => what were the problems encountered?
* Task verification => proof of the quality of the result

===



>Task name: Docker

>Task Description

Create a Docker microservice

This task tests your skill to interpret an Ansible playbook and to convert it into a different deployment method, i.e a Dockerfile

>Task Execution 1. Create a docker image based on the Ansible playbook shown under Task source files. Only interpret the Ansible playbook and create a Dockerfile performing

a similar configuration creating the same type of service. Afterwards write a bash script to start the container with the correct parameters.

2. It is possible to adapt configuration elements according to your context. Too specific configuration elements are out of scope

3. Take screenshots indicating the success of your actions and save script files and related docs

>Task source files Below is a the Ansible playbook that provides elements for creating the docker image.

---

- hosts: webservers

become: yes

tasks:

- name: INSTALL APACHE2

apt: name=apache2 update_cache=yes state=latest

- name: ENABLED MOD_REWRITE

apache2_module: name=rewrite state=present

notify:

- RESTART APACHE2

- name: APACHE2 LISTEN ON PORT 8081

lineinfile: dest=/etc/apache2/ports.conf regexp="^Listen 80" line="Listen 8081" state=present

notify:

- RESTART APACHE2

- name: APACHE2 VIRTUALHOST ON PORT 8081

lineinfile: dest=/etc/apache2/sites-available/000-default.conf regexp="^<VirtualHost \*:80>" line="<VirtualHost *:8081>" state=present

notify:

- RESTART APACHE2

handlers:

- name: RESTART APACHE2

service: name=apache2 state=restarted
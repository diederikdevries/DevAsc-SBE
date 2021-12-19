* Task name => name of the task
* Task preparation => what preparation is necessary to perform the task? (short)

I want to run this image on my own machine. Let's update Docker. 

* Task implementation => what is the way you have implemented the task?

Using VSCode I created a baseline for Apache under Alpine Linux. This works:

> ```
> > Executing task: docker build --pull --rm -f "Task 3 - Docker/Dockerfile" -t exam:latest "Task 3 - Docker" <
> 
> [+] Building 4.0s (8/8) FINISHED                                                                                                                                              
>  => [internal] load build definition from Dockerfile                                                                                                                     0.0s
>  => => transferring dockerfile: 105B                                                                                                                                     0.0s
>  => [internal] load .dockerignore                                                                                                                                        0.0s
>  => => transferring context: 2B                                                                                                                                          0.0s
>  => [internal] load metadata for docker.io/library/httpd:2-alpine                                                                                                        2.0s
>  => [auth] library/httpd:pull token for registry-1.docker.io                                                                                                             0.0s
>  => [internal] load build context                                                                                                                                        0.0s
>  => => transferring context: 158B                                                                                                                                        0.0s
>  => [1/2] FROM docker.io/library/httpd:2-alpine@sha256:c5f6e7bbe1576597694da12d4dd1a244a249f9b5f91c1891b349c812543a63bc                                                  1.8s
>  => => resolve docker.io/library/httpd:2-alpine@sha256:c5f6e7bbe1576597694da12d4dd1a244a249f9b5f91c1891b349c812543a63bc                                                  0.0s
>  => => sha256:7c5b35b0fcc102a97d466b8f7705771ea08975ad38305995622b2ed43a35a57b 8.75kB / 8.75kB                                                                           0.0s
>  => => sha256:5d9e1f41284186a13b72b5c042b733c4e211d6dc47532ccc08a158e2480bc02a 1.23kB / 1.23kB                                                                           0.4s
>  => => sha256:9b3977197b4f2147bdd31e1271f811319dcd5c2fc595f14e81f5351ab6275b99 2.72MB / 2.72MB                                                                           0.3s
>  => => sha256:55c32d614302454d100dbc031565bcde98b4617dd2f4f93aa70178574b03c90e 147B / 147B                                                                               0.6s
>  => => sha256:c5f6e7bbe1576597694da12d4dd1a244a249f9b5f91c1891b349c812543a63bc 1.65kB / 1.65kB                                                                           0.0s
>  => => sha256:f4362e7f363f62c8d289ed726cbbd8137232e072514bc7c0e56986b90df1db9b 1.57kB / 1.57kB                                                                           0.0s
>  => => extracting sha256:9b3977197b4f2147bdd31e1271f811319dcd5c2fc595f14e81f5351ab6275b99                                                                                0.1s
>  => => sha256:f09380cbcdb798ac55e14b28c2168e5b4aed7bb65b605d76695a8cd1453d6460 9.51MB / 9.51MB                                                                           1.2s
>  => => extracting sha256:5d9e1f41284186a13b72b5c042b733c4e211d6dc47532ccc08a158e2480bc02a                                                                                0.0s
>  => => sha256:dc68ce6a677f07520062d06867e7b8911f9d7d98c64ed0efde9ca3cafa72e7b4 4.25MB / 4.25MB                                                                           1.3s
>  => => extracting sha256:55c32d614302454d100dbc031565bcde98b4617dd2f4f93aa70178574b03c90e                                                                                0.0s
>  => => sha256:8f73371c97e3ea179a9e3cd1af130056a5d76592e232e40273a87b34bd7199aa 292B / 292B                                                                               0.8s
>  => => extracting sha256:f09380cbcdb798ac55e14b28c2168e5b4aed7bb65b605d76695a8cd1453d6460                                                                                0.3s
>  => => extracting sha256:dc68ce6a677f07520062d06867e7b8911f9d7d98c64ed0efde9ca3cafa72e7b4                                                                                0.1s
>  => => extracting sha256:8f73371c97e3ea179a9e3cd1af130056a5d76592e232e40273a87b34bd7199aa                                                                                0.0s
>  => [2/2] COPY ./index.html /usr/local/apache2/htdocs                                                                                                                    0.1s
>  => exporting to image                                                                                                                                                   0.0s
>  => => exporting layers                                                                                                                                                  0.0s
>  => => writing image sha256:217d802b18c5303752573c25ce786be747b11c87ebd355ede588e61c91198b33                                                                             0.0s
>  => => naming to docker.io/library/exam:latest                                                                                                                           0.0s
> 
> Terminal will be reused by tasks, press any key to close it.
> ```
>
> From here, We'll add some modules...

First I'll add a update for the Alpine Image:

RUN apk update

I must admit that Docker was quite a eye-opener. Does it work?

It does! (Werkende apache.png)

## Enabling mod_rewrite:

### Is it enabled?

/usr/local/apache2/conf # grep rewrite httpd.conf
#LoadModule rewrite_module modules/mod_rewrite.so

But what is the preferred method in Alpine? Seems that I wasn't the only one asking ;)

https://github.com/nimmis/docker-alpine-apache/issues/2

Does this work? Rebuilding the docker...

Nope. Path seems to be incorrect! Adjusted and working:

/usr/local/apache2/conf # grep rewrite httpd.conf
LoadModule rewrite_module modules/mod_rewrite.so


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
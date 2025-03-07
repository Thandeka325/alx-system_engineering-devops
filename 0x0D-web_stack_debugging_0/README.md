# __Project: 0x0D-web_stack_debugging_0__

This is an introduction to web stack debugging.

![image](https://github.com/user-attachments/assets/e0248361-cbc3-432d-99b2-c6528485b539)


__Background Context__

The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

Let’s start with a very simple example. My server must:

- have a copy of the `/etc/passwd` file in /tmp
- have a file named `/tmp/isworking` containing the string `OK`

Let’s pretend that without these 2 elements, my web application cannot work.

Let’s go through this example and fix the server.

```
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
Unable to find image 'ubuntu:14.04' locally
14.04: Pulling from library/ubuntu
34667c7e4631: Already exists
d18d76a881a4: Already exists
119c7358fbfc: Already exists
2aaf13f3eff0: Already exists
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:14.04
76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
76f44c0da25e        ubuntu:14.04        "/bin/bash"         13 seconds ago      Up 12 seconds                           infallible_bhabha
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK > /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/#
vagrant@vagrant:~$
```

Then my answer file would contain:

```
sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
sylvain@ubuntu:~$
```

Note that as you cannot use interactive software such as `emacs` or `vi` in your Bash script, everything needs to be done from the command line (including file edition).


__Installing Docker__

For this project you will be given a container which you can use to solve the task. If you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.

- [Mac OS](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Ubuntu 14.04](https://www.liquidweb.com/blog/how-to-install-docker-on-ubuntu-14-04-lts/)(Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing)
- [Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

# __Resources__

man or help:
- curl
- [Network basics](https://intranet.alxswe.com/concepts/33)
- [Docker](https://intranet.alxswe.com/concepts/65)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)


# __Project Task__

__Tasks__

__0. Give me a page!__

mandatory
Be sure to read the Docker concept page

In this first debugging project, you will need to get [Apache](https://en.wikipedia.org/wiki/Apache_HTTP_Server) to run on the container and to return a page containing `Hello ALX` when querying the root of it.

Example:

```
vagrant@vagrant:~$ docker run -p 8080:80 -d -it alx/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        alx/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
```

Here we can see that after starting my Docker container, I `curl` the port `8080` mapped to the Docker container port `80`, it does not return a page but an error message. Note that you might also get the error message `curl: (52) Empty reply from server.`

```
vagrant@vagrant:~$ curl 0:8080
Hello ALX
vagrant@vagrant:~$
```

After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 returns a page that contains `Hello ALX`. Paste the command(s) you used to fix the issue in your answer file.

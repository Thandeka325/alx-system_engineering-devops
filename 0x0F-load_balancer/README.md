# __Project: 0x0F. Load balancer

This is an introduction on how to add a load balancer to your servers, and automate the process of configuring your tasks when adding the load balancer.


__Background Context__
We have been given 2 additional servers:

- gc-[STUDENT_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

We had to improve our web stack so that there is [redundancy](https://en.wikipedia.org/wiki/Redundancy_%28engineering%29) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, we had to write Bash scripts to automate our work. All scripts were designed to configure a brand new Ubuntu server to match the task requirements.

# __Resources__

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)
- [Load balancer](https://intranet.alxswe.com/concepts/46) ALX concept psge
- [Web stack debugging](https://intranet.alxswe.com/concepts/68) ALX concept page


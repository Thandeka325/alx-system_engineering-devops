## __Project: 0x1A-application_server__

This is an introduction to application servers and how they can be used.

Background Context


Your web infrastructure is already serving web pages via `Nginx` that you installed in your [first web stack project](https://github.com/Thandeka325/alx-system_engineering-devops/tree/master/0x0C-web_server). While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your `Nginx` and make is serve your Airbnb clone project.

__Resources__

- [Application server vs web server](https://www.f5.com/glossary/application-server-vs-web-server)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
- [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
- [Be careful with the way Flask manages slash](https://werkzeug.palletsprojects.com/en/stable/) in [route](https://flask.palletsprojects.com/en/stable/api/#flask.Blueprint.route) - strict_slashes
- [Upstart documentation](https://doc.ubuntu-fr.org/upstart)
- [Web Server](https://intranet.alxswe.com/concepts/17)
- [Server](https://intranet.alxswe.com/concepts/67) ALX concept page
- [Web stack debugging](https://intranet.alxswe.com/concepts/68) ALX Concept page

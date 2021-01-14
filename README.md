## Rumour-Today 

-----

### Introduction

Rumour-Today is a simple application that renders a list of articles and give you the choice of sending an email with 
title and description of a given article provided for you.

### Tech Stack

Our tech stack will include:

* **Python3** and **Django** as our server language and server framework
* **PostgreSQL** as our database of choice
* **HTML**, **CSS**, **Bootstrap** as our website's frontend
* **Amazon SES** email sending and receiving service
* **Docker** , **Docker Compose** Application containerization 


### Main Files: Project Structure
```sh
├── articles
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── management
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   └── seed_articles.py
│   │   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   ├── articles
│   │   │   ├── 404.html
│   │   │   ├── articles_list.html
│   │   │   ├── email.html
│   │   │   ├── fail_email.html
│   │   │   └── success_email.html
│   │   └── base.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── admin.json
├── README.md
└── requirements.txt
```

## Quick start

To run the project locally,

1. Open a terminal:
  ```shell
  git clone https://github.com/HamdyTawfeek/rumour-today.git
  cd rumour-today
  docker-compose up
  ```

2. Navigate to Home page [http://localhost:8000](http://localhost:8000)


## Future enhancements

1. Moving Out of the Amazon SES Sandbox: I will open a ticket on Amazon to change my account SES service limit to enable any mail recipient without verifying the mail first, but for now I have to verify all the mails that will use the service. Please reach out to me if you need to verify any additional email than the provided emails.

2. Adding authentication to the application.
3. Sync the database with `nousdigital endpoint`. But, for now the application calls the endpoint only one time at the start of the application.
4. Adding test cases for the views.
5. Adding API endpoints to enable CRUD operations on the application.
6. Improving UI
7. Using a production server for master branch and setting `Debug = False`. For now I'm usieng `Debug = True` so the admin view loads it's static files.

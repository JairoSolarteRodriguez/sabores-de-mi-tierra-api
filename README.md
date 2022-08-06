
# Sabores de mi tierra - Backend

## Description:
The project "Sabores de mi tierra" is a social network where we can share recipes,
the recipes shared here are like a treasure or a legacy that will be left for future generations.
In this repository you can find the backend of the REST API that will supply this application
the functionalities to store and manipulate this data.

## Front Repo

https://github.com/ourainbows/Sabores-de-mi-tierra-
## Installation

Install my-project with pip

```bash
  $ git clone https://github.com/JairoSolarteRodriguez/Sabores-de-mi-tierra--back.git
  $ py || python || python3 -m venv venv (create virtual env)
  
  # Activate virtual env
  $ source venv\bin\activate	   #For Unix & mac
  $ .\venv\Scripts\activate		   #For Windows
  $ source venv/Scripts/activate   #For Windows using git bash

  # Install packages
  $ pip install -r requirements.txt

  # Migrate models to database
  $ cd sabores_de_mi_tierra
  $ py || python || python3 manage.py makemigrations
  $ py || python || python3 manage.py migrate

  # Run the project in development mode
  $ py || python || python3 manage.py runserver
```
Now go to: http://127.0.0.1:8000

    
## Tech Stack

**Client:** Angular, SASS

**Server:** postgresql, django, django-rest-framework


# FlaskAPI Template

> by [Sheikh Haris Zahid](https://github.com/Sheikhharis50)

It helps to reduce the development time and code. MVC architecture and basic functionality is implemented in this template to give your development a boost.

## Dependencies

- Python v3
- Pip v3

## Getting Started

- Clone **FlaskApi-Template Project** in your workspace.

        # rename project name.
        $ mv flaskapi-template project_name
        $ cd project_name

- Remove **Migrations Directory** from project.

        $ sudo rm -r migrations && sudo rm -r .git

- Setup **virtual enviorment**.

        $ python3 -m venv venv

- Setup **.env** file

  - copy **.env.example** file from template.
  - provide **Database Credentials** and save file as **.env** in root directory.

- Install **Dependencies**

        $ pip install -r requirements.txt 

- setup **Server Database**

        # create the migrations folder with a version subfolder.
        $ flask db init
        
        # detect the model changes with an upgrade and downgrade logic set up.
        $ flask db migrate
        
        # apply the model changes you have implemented.
        $ flask db upgrade
        
        # if something goes wrong, you can use this command to unapply changes you have done on your model file.
        $ flask db downgrade

- **Run Server**

        $ chmod +x scripts/run_server
        $ ./scripts/run_server 

## Folder Structure

### 1) controllers

- write your **Business Logic** here.
- all the APIs can be implemented here.

### 2) forms

- write your **Form Validations and API Validations** here.
- it is an validation layer.

### 3) models

- model your **Database Tables** here.
- you can write serializers here as well.
- implement model's related all methods here.

### 4) routes

- define your **API Endpoints** here with its REST API method.
- attach corresponding controller with it.

### 5) scripts

- write your **Scripts** here.
- initially following script is available:

        # it runs API server.
        $ ./scripts/run_server

### 6) static

- it contains all the **Static Files**.
- initially following files are available:
  - css
    - styles.css
  - img
    - favicon.co
  - js
    - scripts.js
  
### 7) templates

- it contains all **Templates**.
- pages which will render from you server.

### 7) utils

- utils are used for convenience in development which are used in our whole app, it contains following files:
  - decorators - concept of this is like middlewares such as (token_required).
  - helpers - which are reusable methods which are easy to debug and efficent to use.
  - response - custom response classes such as (APIResponse)

### 8) root files

- app.py - where you attach configurations with flask app.
- config.py - contains all the configurations of flask app.
- .env - environment file which contains environment variables to configure flask app.
- requirements.txt - it has all the python packages requirenements and app dependencies stored in it.

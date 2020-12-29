# Django Demo Contact

## Setup

The setup is straightforward. Clone the project, install the packages, and you are ready.
Please consider using a virtual environment to keep clean your local environment.

```shell
pip install -r requirements.txt
```

## Usage

Create the initial database, and if you want you can create a superuser to access admin dashboard.

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Run the project using:

```shell
python manage.py runserver
```

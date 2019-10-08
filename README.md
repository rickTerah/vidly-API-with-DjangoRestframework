# vidly-API-with-DjangoRestframework

> ### Django-Restframework Project (CRUD, auth) API. In this project you can register as a user and login, get a movie or list of movies, get a rental or list of rentals, get a customer or a list of customers, get movies in a genre. You can also create new genres, movies and rentals. Anyone can retrieve all genres or movies or authenticated users are allowed to make some changes to existing genres, or movies.

## Installation

1. Clone this repository: `git clone https://github.com/Terahpatrick/vidly-API-with-DjangoRestframework.git`.
2. `cd` into `cd vidly-API-with-DjangoRestframework`.
3. Install [pyenv](https://github.com/yyuu/pyenv#installation).
4. Install [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
5. Install Python 3.7.4: `pyenv install 3.7.4`.
6. Create a new virtualenv called `venv`: `pyenv virtualenv 3.7.4 venv`.
7. Set the local virtualenv to `venv`: `pyenv local venv`.
8. Reload the `pyenv` environment: `pyenv rehash`.

If all went well then your command line prompt should now start with `(venv)`.

If your command line prompt does not start with `(venv)` at this point, try running `pyenv activate venv`. 

If pyenv is still not working, try running `python manage.py runserver`.

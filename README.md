# Project Instructions

## 1. clone the project and cd to the project folder

## 2. add settings.toml in the root of the project, you can find the template in docs folder

## 3. To install all packages with poetry that is documented in `poetry.lock` do bellow command

```bash
poetry install
```

## 4. activate the python environment

```bash
poetry shell
```

or

```bash
source .venv/bin/activate
```

## 4. make sure that you have installed mongodb-community and have it running

## 5. run the application with the command below

```bash
python main.py
```

## 6. open up [https://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in the browser

### there are 4 endpoints in the project

1. create_user: to create users
2. get_users: to show all the users
3. create_team: to create a team which works with already made users as members
4. get_teams (task): get all tasks

## that's it, thanks for checking out the program

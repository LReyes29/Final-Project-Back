# Backend Proyecto Final De 4Geeks Academy

### Creadores:
- Luis Reyes Segner
- Joaquin Nuñez
- Andrés Dumas

### Requirements:
- Make sure you are using python 3.6.x

##### Install the packages:
- Make sure yo have installed pipenv

```
$ pipenv shell
```
```
$ pipenv install
```
```
$ pipenv python app.py runserver
```

#### For problems:
- Delete migrations folder and database.db
- Then:
```
$ pipenv python app.py db init
```
```
$ pipenv python app.py db migrate
```
```
$ pipenv python app.py db upgrade
```
```
$ pipenv python app.py runserver
```

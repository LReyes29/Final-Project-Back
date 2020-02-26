# Backend Proyecto Final De 4Geeks Academy

### Creadores:
- [Luis Reyes Segner](https://github.com/LReyes29)
- [Joaquin Nuñez](https://github.com/joaquin16602)
- [Andrés Dumas](https://github.com/VR46KS34)

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
## License
[MIT](https://choosealicense.com/licenses/agpl-3.0/)

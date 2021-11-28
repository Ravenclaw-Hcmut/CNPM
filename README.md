# Restuarant project
## Install dependencies for backend
```
cd backend
pip install pipenv
pipenv shell
pipenv sync
```

Go to src/settings.py and change the database, user and password

## Run backend
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Bootstrap for databases
Use [Postman](https://www.postman.com/downloads/) or vscode [Thunder client extension](https://www.thunderclient.io/)
to send POST request to the server using the following files:
- http://localhost:8000/api/foods/ <- [bootstrap-foods.json](./bootstrap-foods.json)
- http://localhost:8000/api/type/ <- [bootstrap-types.json](./bootstrap-types.json)
- http://localhost:8000/api/side/ <- [bootstrap-sides.json](./bootstrap-sides.json)

## Project setup
```
cd ..
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

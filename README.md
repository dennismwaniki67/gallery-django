Gallery
===================
## Description
[Gallery](https://github.com/dennismwaniki67/gallery-django) A personal gallery application that displays photos for viewing, based on category

------------------------------------------------------------------------

## User Requirements

1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
3. Search for different categories of photos.
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

## Features

+ [x] Create and display photos based on categories
+ [x] Django admin dashboard for adding & managing images, categories and location
+ [x] Bootstrap image model and copy link button.
+ [x] Filter images based on location.
+ [x] search functionality based on image category.


## Setup

### Requirements
* Python3

### Cloning the repository
```bash
git clone https://github.com/dennismwaniki67/gallery-django.git && cd gallery-django
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
Create a .env file and add the following configutions to it
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running Tests
```bash
python manage.py test 
```

### Running the server 
```bash
python manage.py runserver
```

### Deploying to heroku
Refer to this guide: [deploying to heroku](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)

Set the configuration to production mode


## Live Demo

The web app can be accessed from the following link: 


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)


## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Dennis](https://github.com/dennismwaniki67)
# PARIVESH for Educational Institutions

![Logo](parivesh-logo.png?raw=true)

PARIVESH (**P**ro **A**ctive and **R**esponsive facilitation by **I**nteractive and **V**irtuous **E**nvironmental **S**ingle-window **H**ub) is a web-based application that has been developed for the online submission and monitoring of proposals submitted by proposers from educational institutions (batch/branch wise) seeking environmental improvements to the suggested areas by respected authorities from the government.

![Screenshot](parivesh-1.gif?raw=true)

![Badge](badges/badge-01.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-02.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-03.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-04.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-05.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-06.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-07.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-08.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-09.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-10.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-11.svg?raw=true&sanitize=true)&emsp;![Badge](badges/badge-12.svg?raw=true&sanitize=true)

> **Note:** Change the tab size from **8 (default)** to **4** by visiting `GitHub > Settings > Appearance > Tab Size Preference` to see the code in the GitHub repository in good formatting. <br> As of **September 1, 2022**, this project has been updated with its ***latest dependencies***.

An adaptive web application is responsive to different screen sizes.

![Screenshot](parivesh-2.gif?raw=true)

One of the most powerful parts of Django is the automatic admin interface. It reads metadata from project models to provide a quick, model-centric interface where trusted users can manage content on the project site. 

![Screenshot](parivesh-3.gif?raw=true)

> **Note:** If the proposal is rejected (deleted) by the admin, the uploaded files are still saved in the media folder specified in the project `media/proposals` and `media/proposer_images` and need to be deleted using the package `django-unused-media` which information is provided in the following section.

## Run the Project
After downloading and extracting this repository, the project folder named `parivesh` will have a hierarchy of sub-folders and files as shown below:
```
parivesh/
│
├── media/ (uploaded files)
│   ├── proposals/
│   └── proposer_images/
│
├── parivesh/ (django project)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── submitproposals/ (django application)
│   │
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │     
│   ├── static/
│   │   │
│   │   ├── images/
│   │   │   ├── email.png
│   │   │   ├── favicon.png
│   │   │   ├── information.png
│   │   │   ├── location.png
│   │   │   ├── logo.png
│   │   │   ├── phone.png
│   │   │   ├── point.png
│   │   │   └── warning.png
│   │   │
│   │   └── styles/
│   │       └── style.css
│   │  
│   ├── templates/
│   │   └── submitproposals/
│   │       ├── home.html
│   │       ├── message.html
│   │       └── proposal.html
│   │
│   ├── templatetags/ 
│   │   ├── __init__.py
│   │   └── rm_special_chars.py (custom template filter)
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt
Here, ignoring __pycache__
```
**Set up a virtual environment**
```bash
python3 -m venv env
```
**Activate the virtual environment**
```bash
source env/bin/activate
```
**Install the dependencies**
```bash
python3 -m pip install -r requirements.txt
```
**Start the development server**
```bash
python3 manage.py runserver
```
> **Note:** It will start the development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**Drop the database**
```bash
python3 manage.py flush
``` 
**Logging in and using the site** 

To login to the site, open the `/admin` URL [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and enter the superuser username and password credentials (user will be redirected to the login page and then back to the `/admin` URL after entering the details).

The following is the username and password of the Django administration for this project:
>**Username:** admin \
**Password:** admin

This part of the site displays the project model of the `submitproposals` application. Click on a model name `Proposals` to go to a screen that lists all its associated records and further click on those records to edit them.

**Delete unused media files**

It is easy to remove all not used media files (files without references from any Django model with FileField or ImageField fields or their inheritances) using the django-unused-media package.

![Screenshot](django-unused-media-1.png?raw=true)

> **Note:** This markdown file contains a third number graphical interchange format image file `parivesh-3.gif` that illustrates the procedure.

```bash
python3 ./manage.py cleanup_unused_media
 ```
| Before | After |
|:-----:|:-----:|
|![Screenshot](django-unused-media-2.png?raw=true)|![Screenshot](django-unused-media-3.png?raw=true)|

## License
See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
> **Note:** This is an old repository that has been organized and uploaded again. Its first commit was made on **November 5, 2021.**

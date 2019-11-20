# Budget Application Authentication Example

## Getting Started

This is a fork from a testing budget tutorial. 
 If you want to do that tutorial, then ignore 
 this repo and follow the links below.  It's 
 a good tutorial, and worth your time.
 
 Otherwise, this is a demonstration of different Auth 
 setups in Django.  If that is what you are here for, 
 then you are in the right place.
 
 A lot of this is just a practical example of the presentation
 from [Julia Looney](https://youtu.be/sXZ3ntGp_Xc) at pycharm.
 I also swapped the sqlite3 database for postgres because that 
 is the one typically used in production. If you are having 
 trouble with it, then please [read this tutorial.](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
 
 Don't forget to `python manage.py makemigration` and `python manage.py migrate` after you assign a database user.
 
 
 
### Budget Application Testing Tutorial
 - [Youtube Playlist](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)
 - [Github Repo](https://github.com/polkapolka/budget-application-tutorial)
 
### Requirements
 - Postgres
 - Psycopg2
 - Selenium

### The Premise

There are three types of users.
1. Admins
   1. Can create new users
   2. Can create new expenses
   3. Can see budget
2. Managers
   1. Can create new expenses
   2. Can see budget
3. Readers
   1. Can see budget
 

### Master

This is a setup with no authentication.  This is to enable me to create clean branches.

### default-django-auth - **YOU ARE HERE**

This is a version created with default django User models.


### one-to-one profile model

This has a separate profile class in a one-to-one relationship with the django User model.

### custom-abstractbaseuser model

This is an extension of the abstract base user class used to create a custom base user and base user manager.

### Okta Single Sign On

This takes the default-django-auth and implements okta single sign on with it.

### Vinta role-based-permissions

This takes the default-django-auth and uses role-based permissions to enable or disable access to pages.



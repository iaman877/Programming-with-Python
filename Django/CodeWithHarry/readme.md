
# Intoduction to Django 

Code with Harry Django Tutorials Notes

## Steps to Setup the Code

-  python3 -m venv myenv
-  source venv/bin/activate
-  pip3 install django
-  django-admin startproject Hello
-  python3 manage.py startapp home
- Basic file Structure of Project 
    - Inside Hello -> urls.py 
    ```
      urlpatterns = [
      path('', include('home.urls'))  #add this routes
      ]
    ```
    - Inside home -> urls.py
    ```
      urlpatterns = [
      path("", views.index, name='home'),
      path("about", views.about, name='about'),
      path("services", views.services, name='services'),
      path("contact", views.contact, name='contact'), 
      ]
    ```
    - Inside home -> views.py 
    ```
      from django.shortcuts import render, HttpResponse
      def index(request):
          context = {
              "variable1":"Harry is great",
              "variable2":"Rohan is great"
          } 
          return render(request, 'index.html', context)
    ```
- python3 manage.py runserver


## Access static file and template 

- Inside Hello -> settings.py 
    - Added below querry manually for static file
    ```
      STATICFILES_DIRS = [
          os.path.join(BASE_DIR, "static") 
      ]
    ```

    - Edit the value of DIRS in TEMPLATES 
    ```
      'DIRS': [os.path.join(BASE_DIR, "templates")]
    ```

## Create superuser for authenficiation/admin panel

~$ python3 manage.py createsuperuser

Inside Hello -> urls.py, add below lines to change the Admin Portal 
```
  admin.site.site_header = "Ice Cream Admin"
  admin.site.site_title = " Ice Cream Admin Portal"
  admin.site.index_title = "Welcome to Ice Creams"
```

## Entries in database
- Do template inheritance and create form page at conatct us route with {% csrf_token %}

- Inside home -> models.py 
```
  class Contact(models.Model):
      name = models.CharField(max_length=122)
      email = models.CharField(max_length=122)
      phone = models.CharField(max_length=12)
      desc = models.TextField()
      date = models.DateField()
  
      def __str__(self):
          return self.name
```
- Inside home -> admin.py 
    - Register the model
    ```
        from home.models import Contact
        admin.site.register(Contact)
    ```
    - Register app name: Copy app name from apps.py (HomeConfig) and add this at     INSTALLED_APPS in Hello's settings.py
    ```
      INSTALLED_APPS = [
          'home.apps.HomeConfig',
      ]
    ```
 Run below command to create database
```
  ~$ python3 manage.py makemigrations
  ~$ python3 manage.py migrate 
```

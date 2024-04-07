# Django_CRUD
CRUD_Authentication
¬¬DJANGO COMMANDS 

prerequisites >>> Python must be installed in your system

   1. Install virtual environment  
      >> pip install virtualenv  
       
   2. Create your virtual environment  
      >> python -m virtualenv venv_name 
       
   3. Activate Virtual env. 
	>> venv_name\scripts\activate 

	OR >> PSsecurityError>> in activating venv then follow below steps 
      open Powershell >> run as administrator >>
 	Set-ExecutionPolicy unrestricted


   i. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned   
      OR use this >> 
   ii.Set-ExecutionPolicy -ExecutionPolicy RemoteSigned –Scope CurrentUser 
      press >> y

   4. Now install Django 
      >> pip install django 
       
   5. Create django project 
      >> django-admin startproject project_name 
	OR 
	>> python -m django startproject project_name 

   6. Now first change the directory to start app inside your project 
      >> cd project_name 
       
   7. create App 
      >> django-admin startapp app_name 
      OR 
      >> python -m django startapp app_name 
       
   8. Now first Register your app_name in Settings.py 
      >> INSTALLED_APP = [‘app_name’] 
       
   9. Now you can start coding into Views.py >> After creating views.py >> define App_level urls >> then you can create project_level urls 
       

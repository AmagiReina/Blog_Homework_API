                                            Проект API блог на основе CRUD (Django)


Для запуска требуется:
1. Установить environment (окружение):

  pip install virtualenv
  
2. Запустить окружение:

  virtualenv venv
  
3. Активировать окружение командой:

  venv\Scripts\activate.bat
  
4. Проверить установлен ли Django:
  
  pip freeze
  
  Результат:
  asgiref==3.2.7
  Django==3.0.6
  django-cors-headers==3.3.0
  djangorestframework==3.11.0
  pytz==2020.1
  sqlparse==0.3.1
  
 5. Запустить API командой:
 
  python manage.py runserver
  или
  python3 manage.py runserver

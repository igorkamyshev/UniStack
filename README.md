# UniStack README

> если на машине установлены разные версии Python, то везде следует заменить `python` на `python3` 

## Развертывание на локальной машине
+ `git clone git@bitbucket.org:GarikNovel/unistack.git`
+ `cd unistack`
+ `npm install`
+ `pip install django`
+ `pip install djangorestframework`
+ `pip install markdown`
+ `pip install django-filter`
+ `python manage.py migrate`

## Работа с проектом локально
+ `git pull`
+ `npm install`
+ `python manage.py migrate`
+ запустить сервер `python manage.py runserver 6340`
+ проект доступен в браузере [http://127.0.0.1:6340/](http://127.0.0.1:6340/)
+ выключить сервер – **control+C**

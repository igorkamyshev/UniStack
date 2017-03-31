# UniStack README

> если на машине установлены разные версии Python, то везде следует заменить `python/pip` на `python3/pip3` 

## Развертывание на локальной машине
+ `git clone git@bitbucket.org:GarikNovel/unistack.git`
+ `cd unistack`
+ `npm install`
+ `pip install django`
+ `pip install djangorestframework`
+ `pip install markdown`
+ `pip install django-filter`
+ `pip install lxml`
+ `pip install requests`
+ `python manage.py migrate`

## Работа с проектом локально
+ `git pull`
+ `npm install`
+ `python manage.py migrate`
+ запустить сервер `python manage.py runserver 6340`
+ проект доступен в браузере [http://127.0.0.1:6340/](http://127.0.0.1:6340/)
+ выключить сервер – **control+C**

## Команды
### Получение данных из внешнего источника 
Команда загружает все полученные данные в базу данных. 
> `python manage.py parse [source]`

Доступные параметры для [source]
1. `fgos` – **направления подготовки** по группам с сайта [Федеральный портал: Российское образование](http://www.edu.ru/abitur/act.6/index.php)

# mailing_project
- **Сервис управления рассылками, администрирования и получения статистики.**

### 1. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:
        1- python -m venv venv
        2- venv\Scripts\activate
        3- pip install -r requirement.txt


### 2. Для запуска redis:
        1- sudo apt-get update
        2- sudo service redis-server start
        3- redis-cli

### 3. Для работы с переменными окружениями необходимо создать и заполнить файл `.env`
        Введите туда свои настройки как указано в файле `.env.sample`
        
        CACHE_ENABLED=
        CACHE_LOCATION=
        
        EMAIL_HOST_USER=
        EMAIL_HOST_PASSWORD=
        
        DB_NAME=
        DB_USER=
        DB_PASSWORD=
        DB_HOST=
        DB_PORT=

        ADMIN_PASSWORD =
        

### 4. Выполните `migrate`
        
        python manage.py migrate

### 4. Для создания администратора (createsuperuser)
    - заполните поля email, PASSWORD. users/management/commands/csu.py

    1- python manage.py csu

### 5. Для запуска приложения: 

    - python manage.py runserver

### 6. Для отправки рассылки из командной строки:
    - python manage.py services

### 7. Автоматическая рассылка реализована с помощью библиотеки django-crontab. По умолчанию система проверяет наличие новых рассылок и отправляет их с периодичностью 5 минут (настройку можно изменить в config/settings.py -> CRONJOBS).
    - Добавление автоматической рассылки
  
        python manage.py crontab add

   
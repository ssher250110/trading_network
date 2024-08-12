# MVP онлайн платформы-торговой сети электроники.

## Задание

- Создайте веб-приложение с API-интерфейсом и админ-панелью.
- Создайте базу данных, используя миграции Django.

## Технические требования

- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+

## Инструкция для запуска проекта

1. Клонируйте данный репозиторий к себе на локальную машину:

```bash
    git clone https://github.com/ssher250110/trading_network.git
```

2. В файле .env_example подставьте свои переменные окружения и переименуйте файл в .env
3. Запустите Docker
4. Введите команду в терминале(выполнение команды осуществляется из папки проекта):
    * Для Compose V1:
    ```bash
    docker-compose up -d --build 
    ```
    * Для Compose V2:
    ```bash
    docker compose up -d --build 
    ```

- Команда для создания суперпользователя
```bash
docker ps
```
```bash
docker exec -it <id_container_trading_network> bash
```

```bash
python3 manage.py createsuperuser
```

- Пути документации

```bash
http://127.0.0.1:8000/swagger/
```

```bash
http://127.0.0.1:8000/redoc/
```

### Автор проекта:

https://github.com/ssher250110
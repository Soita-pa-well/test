# wb_tech_test
Тестовый проект WB-Tech: Реализованы сущности комнады, ее участников и админ зона по адресу http://127.0.0.1:8000/admin/
### как запустить проект:
Из корневой директории запустить docker-compose
```bash
docker compose up -d
```
Выполнить миграции 
```bash
docker compose exec backend python manage.py migrate
```
Собрать статику
```bash
docker compose exec backend python manage.py collectstatic
```
Копировать статику в на volume
```bash
docker compose exec backend cp -r /app/static/. /backend_static/static/
```
Создать Суперпользователя
```bash
docker compose exec backend python manage.py createsuperuser
```

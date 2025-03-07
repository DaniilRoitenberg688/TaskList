*Для запуска:

**docker-compose up --build**

*Проверить работу можно на порту 8080

*Запуск бэкенда
- alembic upgrade head
- uvicorn app:app --host 0.0.0.0 --port 5000

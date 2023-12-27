Онлайн сервис бронирования туров с использованием Fast Api
   - Модели: Пользователи, Туры, Бронирования
   - Идея проекта: Разработка онлайн сервиса для бронирования туров с возможностью просмотра доступных туров, выбора даты, оформления бронирования и авторизации пользователей.

Требования к проекту:
- Упаковка проекта в докер-компоуз и запуск через docker compose up без дополнительной настройки
- прохождение flake8 + mypy в соответствии с конфигурациями проекта
- Кеширование всего, что возможно закешировать через redis
- Orm:  sqlalchemy2.0
- Migration: alembic
- Тесты - pytest + mock на redis и rollback транзакций фикстур вместо удаления.
- Минимальные данные при разворачивании проекта (фикстуры)
- Метрики: 
  - На кол-во полученных запросов в разрезе каждой ручки.
  - На кол-во ошибок по каждой ручке
  - На кол-во отправленных запросов
  - Время выполнения каждой ручки в среднем (гистограмма)
  -Время выполнения всех интеграционных методов (запросы в бд, редис и тп (гистограмма)
- Валидация входящих данных (pydantic)
- Настройки в env
- Без дублирования кода
- poetry как сборщик пакетов
- Обработка ошибок и соответствующие статусы ответов
- В README.md ожидается увидеть как что работает, чтобы можно было ознакомиться проще с проектов
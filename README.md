# 🚗 GG-Car — Backend API на Django

**GG-Car** — это backend-платформа для автосалонов, разработанная на Django. В проекте реализована авторизация по JWT, расширенная модель пользователя, справочники автомобилей (бренд, модель, тип кузова), контактные данные, а также CRUD для управления объявлениями и автосалонами.

---

## 🚧 Статус проекта

> ⚠️ **Проект находится в разработке. Новые функции и улучшения добавляются по мере времени.**

---

## 🧰 Технологии

- Python 3.11+
- Django 4.x
- Django REST Framework
- PostgreSQL
- JWT (SimpleJWT)
- python-decouple (`.env`)


## Быстрый запуск через Docker

1. Запустите команду в корне проекта:

```bash
docker-compose up --build
```

### Данные суперпользователя (Django Admin)

- Email: admin@admin.com  
- Пароль: admin123  
- Полное имя: Admin


### Полезные URL

- Django Admin: `http://localhost:8000/admin/`  
- Swagger API docs: `http://localhost:8000/swagger/`

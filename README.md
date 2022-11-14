# magnit-service

### Что на борту:
- **Python 3.10**
- **FastAPI** + **Celery** + **Uvicorn**
- Управление зависимостями: **Poetry**
- Валидация входных и выходных данных: **Pydantic**
- Деплой/запуск: **docker-compose**
- Тесты и codecoverage: **Pytest** с прогоном на CI ([https://github.com/rmilovanov/magnit-service/actions](https://github.com/rmilovanov/magnit-service/actions))
- Качество и форматирование кода: **Black**, **Flake8**, **Pylint** с прогоном на CI
- Observability: **Grafana** + **Prometheus**
- Документация для API: генерируется автоматически c использованием **Swagger UI** и **Redoc**
- Дашборд **Flower** для **Celery**

### Чтобы развернуть решение:
```shell-script
git clone https://github.com/rmilovanov/magnit-service.git
cd magnit-service
docker-compose up -d
```

Приложение будет развёрнуто по адресу [http://0.0.0.0:8008](http://0.0.0.0:8008)

C главной переадресует на интерактивную документацию - там же можно поотправлять запросы с помощью кнопки `try it out`

Список всех задач: [http://0.0.0.0:5556/tasks](http://0.0.0.0:5556/tasks)

Документация: [http://0.0.0.0:8008/docs](http://0.0.0.0:8008/docs) и [http://0.0.0.0:8008/redoc](http://0.0.0.0:8008/redoc)

Дашборд для *Celery*: [http://0.0.0.0:5556](http://0.0.0.0:5556)

Grafana: [http://0.0.0.0:3000](http://0.0.0.0:3000) - admin/admin

Статус ресурсов мониторинга: [http://0.0.0.0:9090/targets](http://0.0.0.0:9090/targets)

### Чтобы прогнать тесты:
`docker-compose up tests`


## Решение развёрнуто в облаке:

[Документация](http://77.222.42.195:8008/docs) 

[Flower](http://77.222.42.195:5556)

[App Metrics](http://77.222.42.195:3000/d/_eX4mpl3/fastapi-dashboard?orgId=1&refresh=5s)

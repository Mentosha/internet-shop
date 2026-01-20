# Система сбора и анализа данных для интернет-магазина

## Описание проекта

Этот проект представляет собой простую end-to-end систему для генерации, хранения и анализа данных интернет-магазина.  
Система автоматически создаёт заказы с реалистичными данными, сохраняет их в PostgreSQL, а затем предоставляет возможность анализа через **Redash** и **Jupyter Notebook**.
Работу выполнил: Луцук Иван Дмитриевич

### Компоненты

1. **Генератор данных**  
   - Скрипт на Python (`generate_orders.py`), который создаёт заказы с интервалом 1 секунда.  
   - Каждая запись содержит:
     - `product_name` — название товара  
     - `category` — категория товара  
     - `price` — цена  
     - `quantity` — количество  
     - `city` — город покупки  
     - `created_at` — дата и время создания заказа  

2. **База данных PostgreSQL**  
   - Хранит все сгенерированные заказы.  

3. **Redash**  
   - Используется для визуализации данных и построения дашбордов.  
   - Подключается к PostgreSQL.  
   - В проекте создан дашборд с 3+ визуализациями:
     - Выручка по городам 
     - Заказы по категориям
     - Количество заказов по времени

4. **Jupyter Notebook**  
   - Для интерактивного анализа данных.  
   - Используются библиотеки: `pandas`, `matplotlib`, `psycopg2`.  
   - Примеры аналитики:
     - Общая выручка по категориям
     - Построение графиков и диаграмм
     - Создание новых метрик (например, `total_price = price * quantity`)

---

# Быстрый старт
## Предварительные требования
- Docker и Docker Compose
- Windows / macOS / Linux  
- Браузер для работы с Redash и Jupyter Notebook 

## Установка и запуск
```
# 1. Клонируйте репозиторий
git clone https://github.com/Mentosha/internet-shop
cd internet-shop

# 2. Настройка .env на свои данные 
POSTGRES_PASSWORD=yourpassword
REDASH_DATABASE_URL=postgres://analytics:yourpassword@postgres:5432/redash
REDASH_SECRET_KEY=supersecretkey
JUPYTER_TOKEN=mytoken123

# 3. Инициализировать базу Redash:
docker-compose run --rm redash create_db

# 4. Запустите все сервисы
docker-compose up -d

# 5. Откройте Redash в браузере
http://localhost:5000
```
# Первоначальная настройка
## При первом входе в Redash:

- Зарегистрируйте первого пользователя (он станет администратором)

- Настройка источника данных в Redash:

  - Перейдите в Settings → Data Sources

  - Нажмите + New Data Source

  - Выберите PostgreSQL

  - Заполните настройки:
    - Type: PostgreSQL
    - Host: postgres
    - Port: 5432
    - Database: analytics
    - User: analytics
    - Password: mytoken123

## Структура проекта

internet-shop/
│
├─ .gitignore                  # Файлы и папки, которые не коммитить в Git
├─ generate/
│   ├─ generate_orders.py      # Скрипт генерации заказов
│   ├─ requirements.txt        # Зависимости для генератора
│   └─ Dockerfile              # Docker образ генератора
├─ notebooks/
│   └─ analysis.ipynb           # Jupyter Notebook для анализа
├─ db/
│   └─ init.sql                # Начальная инициализация базы данных
├─ docker-compose.yml           # Конфигурация всех сервисов
├─ .env                         # Переменные окружения
└─ README.md                    # Подробное описание проекта

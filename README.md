# Описание проекта

Проект представляет собой веб-сервис для предсказания дефолта клиента по кредитной карте.

Сервис принимает данные клиента в формате JSON, передаёт их в обученную модель машинного обучения и возвращает результат предсказания:

- 0 - дефолт не прогнозируется
- 1 - прогнозируется риск дефолта.

В качестве модели используется логистическая регрессия.
Модель сохранена в файл: models/model.pkl


## Структура проекта


credit-default-project/

|

|-- app.py

|-- Dockerfile

|-- requirements.txt

|-- ARCHITECTURE.md

|-- A\B-тестирование.md

|-- .gitignore

|-- .dockerignore

|-- data/

|   |-- UCI_Credit_Card.csv

|-- models/

|   |-- model.pkl

|-- notebook/

|   |-- файл с обучением модели

|-- src/

|   |-- predict.py

В проекте используются:
- Python
- Flask
- pandas
- scikit-learn
- joblib
- Docker
- GitHub
- Docker Hub



## Описание модели

Для решения задачи была обучена модель логистической регрессии.

- Целевая переменная: default.payment.next.month
- Значения целевой переменной: 
  0 - клиент не допустит дефолт 
  1 - клиент допустит дефолт

Перед обучением из данных был удалён столбец "ID", так как он является техническим идентификатором и не должен использоваться для обучения модели.

Модель сохранена в формате .pkl с помощью библиотеки joblib.


## Метрики модели

На тестовой выборке были получены следующие метрики:

- Accuracy: 0.8077
- Precision: 0.6868
- Recall: 0.2396
- F1-score: 0.3553

Модель показывает хорошую общую точность, но recall для класса дефолта невысокий.


## Установка зависимостей

1. Для запуска проекта локально нужно создать виртуальное окружение.

  bash
  
  python3 -m venv venv

3. Активировать виртуальное окружение:

bash

source venv/bin/activate

4. Установить зависимости:

bash

pip install -r requirements.txt

5. Файл requirements.txt содержит необходимые библиотеки:

- flask==3.0.3
- pandas==2.2.2
- scikit-learn==1.6.1
- joblib==1.4.2

## Локальный запуск сервиса

Для запуска Flask API локально выполните команду:

bash

python app.py

После запуска сервис будет доступен по адресу:
http://localhost:5000

## Проверка работоспособности API
Для проверки работы сервиса используется endpoint /health.

Пример запроса:

bash

curl http://localhost:5000/health

Пример ответа:

json

{"status":"ok"}

Если возвращается такой ответ, значит сервис успешно запущен.


## Пример запроса к API

Для получения предсказания используется endpoint /predict.

Пример curl-запроса:

bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "LIMIT_BAL": 20000,
  "SEX": 2,
  "EDUCATION": 2,
  "MARRIAGE": 1,
  "AGE": 24,
  "PAY_0": 2,
  "PAY_2": 2,
  "PAY_3": -1,
  "PAY_4": -1,
  "PAY_5": -2,
  "PAY_6": -2,
  "BILL_AMT1": 3913,
  "BILL_AMT2": 3102,
  "BILL_AMT3": 689,
  "BILL_AMT4": 0,
  "BILL_AMT5": 0,
  "BILL_AMT6": 0,
  "PAY_AMT1": 0,
  "PAY_AMT2": 689,
  "PAY_AMT3": 0,
  "PAY_AMT4": 0,
  "PAY_AMT5": 0,
  "PAY_AMT6": 0
}'


Пример ответа API:

json
{
  "prediction": 1,
  "prediction_": "default",
  "probability_default": 0.5112286582743187,
  "probability_no_default": 0.48877134172568126
}


Расшифровка ответа:

- prediction - числовой класс предсказания
- prediction_ - текстовое описание класса
- probability_default - вероятность дефолта
- probability_no_default - вероятность отсутствия дефолта.


## Запуск через Docker

Проект можно запустить в Docker-контейнере.

### Сборка Docker-образа

bash

docker build -t credit-default-project .



### Запуск контейнера

bash

docker run -p 5000:5000 credit-default-project

После запуска контейнера сервис будет доступен по адресу:


http://localhost:5000


Проверка:

bash

curl http://localhost:5000/health


Ожидаемый ответ:

json

{"status":"ok"}


---

## Docker Hub

Docker-образ проекта опубликован в Docker Hub:

https://hub.docker.com/repository/docker/ivalena/credit-default-project/general

Скачать образ можно командой:

bash
docker pull ivalena/credit-default-project:latest


Запустить образ из Docker Hub:

bash
docker run -p 5000:5000 ivalena/credit-default-project:latest


После запуска сервис будет доступен по адресу:


http://localhost:5000

<img width="820" height="192" alt="image" src="https://github.com/user-attachments/assets/316d90fc-a64d-48ce-b0c0-e4036eb66cd1" />


## Документация проекта

В проекте дополнительно представлены:


ARCHITECTURE.md


Файл содержит описание архитектуры ML-сервиса, выбранного подхода, возможного использования RabbitMQ, логирования, мониторинга, DVC, MLflow и бизнес-метрик.


A\B-тестирование.md


Файл содержит план A/B-тестирования двух версий модели: текущей модели v1 и новой модели v2.

---

## Демонстрация работы

Работоспособность API была проверена локально.

Проверялись endpoints:


GET /health
POST /predict


Пример успешной проверки /health:

bash

curl http://localhost:5000/health

Ответ:

json
{"status":"ok"}
<img width="925" height="317" alt="image" src="https://github.com/user-attachments/assets/733a9d14-a82d-47af-939d-ee495cce4cdd" />

Пример успешной проверки /predict:

json
{
  "prediction": 1,
  "prediction_": "default",
  "probability_default": 0.5112286582743187,
  "probability_no_default": 0.48877134172568126
}


Также проект был собран в Docker-образ, контейнер был запущен локально и проверен через curl-запросы.
<img width="1366" height="768" alt="Screenshot_20260531_142225" src="https://github.com/user-attachments/assets/49758b94-65af-4f6d-b8ab-232d6d2ac892" />

---

## Итог

В рамках проекта был создан ML-сервис для предсказания дефолта клиента по кредитной карте.

Были выполнены основные этапы:

- подготовка данных
- обучение модели
- сохранение модели в .pkl
- создание Flask API
- запуск сервиса локально
- контейнеризация через Docker
- публикация образа в Docker Hub
- подготовка архитектурного описания
- подготовка плана A/B-тестирования.

Проект можно запускать как локально через Python, так и через Docker-контейнер.

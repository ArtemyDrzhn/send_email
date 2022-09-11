### Написать на Python 2.7 / Django небольшой сервис отправки имейл рассылок.
#### Возможности сервиса:
 1. Отправка рассылок с использованием html макета и списка подписчиков.
 2. Отправка отложенных рассылок.
 3. Использование переменных в макете рассылки. (Пример: имя, фамилия, день рождения из списка подписчиков)
 4. Отслеживание открытий писем.
Отложенные отправки реализовать при помощи Celery.

#### Комментарии к решению работы:
Данные списка подписчиков было решено хранить в БД. Решение было упаковано в контейнеры докера. 
В качестве брокера использовался redis. Для отслеживания открытий писем использовались логи Mailgun.
Для поддержания чистоты кода - flake8. Написаны тесты (pytest)
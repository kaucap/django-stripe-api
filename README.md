<h1 align="center">Django + Stripe API</h1>
<p align="center">
<img src="./static/images/Stripe_Logo,_revised_2016.png">
</p>

## Описание
Сайт, разработанный на джанго, который взаимодействует с платежной системой Stripe.

## Запуск
- Создать виртуальное окружение. python3 -m venv venv
- Установить нужные библиотеки. pip install -r requirements.txt
- В качестве бд используется Postgres. Нужно установить его.
- Создать файл .env и внести в него нужные параметры, которые указаны в env.example

## Страницы
- admin/ - Админка
- shop/ - Страница с товарами
- shop/item/pk - Детальная страница с товаром
- shop/buy/pk - Покупка товара
- shop/success - Успешная попытка оплаты товара
- shop/cancel - Неудачная попытка оплаты товара
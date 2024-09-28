# Дипломный проект. Задание 2: API

## Автотесты для проверки end points, которые помогают заказать бургер в Stellar Burgers

### test_create_order - Проверяем "Создание заказа"
#### 1) test_create_order_with_login - Создание заказа с авторизацией
#### 2) test_create_order_without_login - Создание заказа без авторизации
#### 3) test_create_order_with_ing - Создание заказа с ингредиентами
#### 4) test_create_order_without_ing - Создание заказа без ингредиентов
#### 5) test_create_order_with_incorrect_hash_ing - Создание заказа с неверным хэшем

### test_create_user - Проверяем "Создание пользователя"
#### 1) test_create_new_unique_user - Создание нового уникального пользователя
#### 2) test_create_new_user_with_out_password - Создание пользователя без обязательного поля
#### 3) test_create_exist_user - Создание существующего пользователя

### test_get_orders - Проверяем получение заказов конкретного пользователя
#### 1) test_get_orders_user_with_auth - Получение заказов с авторизацией
#### 2) test_get_orders_user_without_auth - Получение заказов без авторизации

### test_login_user - Проверяем авторизацию пользователя
#### 1) test_login_exist_user - Авторизация под существующим пользователем
#### 2) test_login_with_incorrect_password - Авторизация с неверным логином и паролем

### test_update_userdata - Проверяем изменение данных пользователя
#### 1) test_update_user_data_name_with_auth, test_update_user_data_email_with_auth, test_update_user_data_password_with_auth - Изменение данных с авторизацией
#### 2) test_update_user_data_name_without_auth, test_update_email_data_name_without_auth, test_update_user_data_password_without_auth - Изменение данных без авторизации

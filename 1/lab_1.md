Проблеми методу process_order:

    1. Метод відповідає за занадто багато різних завдань, що порушує принцип єдиної відповідальності (SRP).
    2. Логіка застосування знижок змішана з обчисленням загальної вартості, що ускладнює розуміння та тестування коду.
    3. Оновлення складських залишків та надсилання підтвердження електронною поштою тісно пов'язані з обробкою замовлення, але ці дії могли б бути винесені в окремі методи або класи.

Під час рефакторінгу було зроблено:

    1. Створено окремий клас Order, який містить дані про замовлення та методи для обчислення загальної вартості та застосування знижок. Це дозволило відокремити логіку обчислення від логіки обробки замовлення.
    2. Було перенесено логіку оновлення складських залишків та надсилання підтвердження електронною поштою в окремі методи update_inventory та send_confirmation_email класу OrderProcessor. Це покращило структуру коду та дотримання принципу єдиної відповідальності.
    3. Метод process_order() був зроблений більш лаконічним, делегуючи обчислення та застосування знижок до методів Order.


Після рефакторингу код став більш модульним, зрозумілим та легшим для тестування. Метод process_order тепер відповідає за координацію обробки замовлення, а деталі реалізації винесені в окремі методи та класи. Рефакторинг покращив архітектуру системи, зробивши її більш гнучкою та масштабованою. Тепер легше вносити зміни або додавати нові функціональні можливості, не порушуючи існуючу структуру.
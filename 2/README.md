1. Рефакторинг функції calculate_score:

    Замість великої кількості параметрів, був створений клас UserProfile, який інкапсулює всю інформацію про користувача. Це дозволяє:

    1) Зменшити кількість параметрів в методах, зробивши їх більш читабельними.
    2) Групувати пов'язані дані в одному об'єкті, що полегшує супровід коду.
    3) Додавати або змінювати методи, пов'язані з профілем користувача, не змінюючи підпис методів.

2. Рефакторинг класу User:

    У цьому випадку було видалено непотрібне поле phone_code та буои об'єднані phone і phone_code в одне поле phone_number.
    Замість використання числових кодів для типів користувачів, були створені константи ENGINEER і MANAGER, які роблять код більш самодокументованим.
    Був доданий метод get_user_type_name, який повертає рядкове представлення типу користувача, що також робить код більш читабельним.
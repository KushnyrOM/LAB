При першому рефакторінгу для усунення дублювання логіка застосування знижки була відокремлена в окрему функцію apply_discount. Функція calculate_total_price тепер використовує генератор для застосування знижки до кожної ціни в списку, а потім підсумовує результати за допомогою sum. Функція calculate_total_price_with_tax викликає calculate_total_price для обчислення загальної ціни зі знижкою, а потім застосовує податок.


У другому рефакторінгу для усунення дублювання коду в класі DataAnalyzer було створено допоміжний метод _calculate_total_and_count, який обчислює суму елементів та кількість елементів у списку self.data. Цей метод використовується іншими методами класу, що потребують цих значень У методах calculate_total та calculate_average використовується _calculate_total_and_count замість повторного розрахунку суми та кількості елементів. У методах calculate_minimum та calculate_maximum було додано перевірку на порожній список self.data. Якщо список порожній, метод повертає None, інакше повертає мінімальне/максимальне значення відповідно. Таким чином, код став більш компактним, зрозумілим та легшим для підтримки. Дублювання коду було усунено, а функціональність класу залишилася незмінною.
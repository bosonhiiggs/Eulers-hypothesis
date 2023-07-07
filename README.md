# Гипотеза Эйлера о сумме степеней
## Условие:
В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой 
теоремы Ферма, предполагая, что по крайней мере `n` энных степеней 
необходимо для получения суммы, которая сама является энной 
степенью для `n > 2`. Напишите программу для опровержения гипотезы 
Эйлера (продержавшейся до 1967 года), и найдите четыре 
положительных целых числа, сумма 5-х степеней которых равна 
5-й степени другого положительного целого числа.

Таким образом, найдите пять натуральных чисел `a, b, c, d, e` 
удовлетворяющих условию:

`a ** 5 + b ** 5 + c ** 5 + d ** 5 = e ** 5.`

В ответе укажите сумму `a + b + c + d + e`.
## Решение:
1. Отдельный подсчет двух частей уравнения.
2. Проверяем равны они друг другу или нет.
3. Если условие соблюдается, то вывод ответа.

### Примечание 1. Отдельный подсчет двух частей уравнения.
Это решение позволяет не делать еще один вложенный цикл, 
поэтому сокращает перебор всех чисел, потому что 
решает проблему с большим количеством вложенных циклов.

Правая часть уравнения равна `e ** 5 = y -> e == y ** (1 / 5)`
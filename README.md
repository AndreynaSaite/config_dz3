# Конфигурационное управление дз №3
## Общее описание
Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений. Входной текст на учебном конфигурационном языке принимается из
файла, путь к которому задан ключом командной строки. Выходной текст на
языке json попадает в файл, путь к которому задан ключом командной строки.
##  Описание всех функций и настроек
Многострочные комментарии:
<!--
Это многострочный
комментарий
-->
Массивы:
#( значение значение значение ... )
Имена:
[_A-Z][_a-zA-Z0-9]*
Значения:
• Числа.
• Массивы.
Объявление константы на этапе трансляции:
имя = значение
Вычисление константного выражения на этапе трансляции (префиксная
форма), пример:
120
|+ имя 1|
Результатом вычисления константного выражения является значение.
Для константных вычислений определены операции и функции:
1. Сложение.
2. Вычитание.
3. Умножение.
4. mod().
Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 3
примера описания конфигураций из разных предметных областей.
##  Описание команд для сборки проекта.
1. Клонирование репозитория 

```https://github.com/AndreynaSaite/config_dz3```

2. Переход в директорию Homework_config

```cd config_dz3```

3. Запуск скрипта для демонстрации возможностей Cli

```python3 homework3.py config.txt output.json```
## Примеры использования
![Screen](https://github.com/AndreynaSaite/config_dz3/blob/main/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png)
<!--описание коммитов-->
## Описание коммитов
| Название | Описание                                                                             |
|------------------|----------------------------------------------------------------------------- |
| first_commit    | Готовый проект                                                               |

# Python interface scripts
### Запуск скриптов
Добавлен функционал определения позиционности аргумента **-t**, Привет запуска скрипта:
```
python3 task1.py -t 2000 Example Text
```
или
```
python3 task1.py Example Text -t 2000
```

### Запуск скрипта по крону
Запустить скрипт в указанное время **2020-05-06 21:11:25**

```
11 21 6 5 *     /usr/bin/python3 task1.py -t 4000 Запуск 1-ой задачи по крону
11 21 6 5 *     /usr/bin/python3 task2.py -t 4000 Запуск 2-ой задачи по крону
```
![Cron](https://adminvps.ru/blog/wp-content/uploads/2017/05/cron.png)

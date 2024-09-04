```
 _   _    _       _            _                           
| | | |  (_)     | |          | |                          
| |_| | ___ _ __ | |_ ___ _ __| | ___  ___ ___  ___  _ __  
| __| |/ / | '_ \| __/ _ \ '__| |/ _ \/ __/ __|/ _ \| '_ \ 
| |_|   <| | | | | ||  __/ |  | |  __/\__ \__ \ (_) | | | |
 \__|_|\_\_|_| |_|\__\___|_|  |_|\___||___/___/\___/|_| |_|
                         ______                            
                        |______|                           
```
# Запуск
### Требования
 - Python 3.12.2
 - os: MacOS (Не тестировал на windows и linux)
 - установить зависимости из requirements.txt

Запускать `main.py`

# Описание
Программа содержит анимацию движения красного круга вокруг белого. 

Кнопкой `Change direction` можно изменить направление движения красного круга.

Слайдер отвечает за скорость движения красного круга в диапазоне от 1 до 10.

Анимация происходит на канвасе, кнопки и слайдер прикреплены к отдельному фрейму. Метод `update_position` реализует анимацию, 
высчитывает новую позицию для красного круга и перемещает его на эту позицию. Также обновляет информацию о скорости, считывая значение слайдера.

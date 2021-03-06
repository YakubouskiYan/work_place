#!/usr/bin/env python
# coding: utf-8

# ## Skillactory Project №1
#   
# **Угадать загаданное компьютером число за минимальное число попыток.**
# 
# Итак, компьютер загадывает целое число от **1** до **100**, и нам его нужно угадать.
# Под «угадать», конечно, подразумевается «написать программу, которая угадывает число».

# **Варинты решений Skillfactory**

# In[60]:


import numpy as np # импортируем библиотеку numpy 


# In[61]:


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[62]:


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали


# In[63]:


# Проверяем
score_game(game_core_v1)


# In[64]:


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали


# In[65]:


# Проверяем
score_game(game_core_v2)


# **Мое решение №1**

# In[66]:


def game_core_v3(number):
    
    '''Создаем переменную "count" - счетчик, и две переменные "low" и "high" как нижний и верхний предел "random.randit".
    Создем бесконечный цикл, в котором исользуем конструкцию "try/exept", которая озволяет основной код зпписать в try,
    а при оявления исключения вывести на экануведомление об ошибки. В "try" ппомещаем наш random.randit 
    с верхним и нижним пределем в виде аргументов "low" "high". С помощью "if/elif" отрабатывем условия, 
    если "загананное число" больше "отгадывемого" изменяем присваеваем "low" значение "отгадывемого" - 1,
    загананное число" меньше "отгадывемого" изменяем присваеваем "high" значение "отгадывемого", 
    при угадывании числа нас с помощью "break" мы остнавливаем бесконечный цикл.''' 

    count = 0 # Счетчик. Подсчет количества попыток до отгадывания загаданного целого числа.
    low = 0 # Начало дипазона функции random.randint
    high = 101 # Конец дипазона функции random.randint

    while True: # Бесконечный цикл
        
        try: # Основной код омещаем в try, чтобы ловить исключения в except
            predict = np.random.randint(low, high) 
            count += 1 

            if predict < number:
                low = predict - 1 # уменьшаем диапзон подбора числа 

            elif predict > number:
                high = predict # уменьшаем диапзон подбора числа 

            elif predict == number:
                break 
        except: # Отработка исключений
            print("Ошибка! Обртитесь в службу поддежки!" )
            
    return count


# In[67]:


# Проверяем
score_game(game_core_v3)


# **Мое решение №2**

# In[68]:


def game_core_v4(number):

    '''Создаем переменную "count" - счетчик, и две переменные "low" и "high" как нижний и верхний предел "random.randit".
    Создем бесконечный цикл, в котором исользуем конструкцию "try/exept", которая озволяет основной код зпписать в try,
    а при оявления исключения вывести на экануведомление об ошибки. В "try" ппомещаем наш random.randit 
    с верхним и нижним пределем в виде аргументов "low" "high". С помощью "if/elif" отрабатывем условия, 
    если "загананное число" больше "отгадывемого" изменяем присваеваем "low" значение "отгадывемого" + 1,
    загананное число" меньше "отгадывемого" изменяем присваеваем "high" значение "отгадывемого",
    при угадывании числа нас с помощью "break" мы остнавливаем бесконечный цикл.''' 

    count = 0 # Счетчик. Подсчет количества попыток до отгадывания загаданного целого числа.
    low = 0 # Начало дипазона функции random.randint
    high = 101 # Конец дипазона функции random.randint

    while True: # Бесконечный цикл
        
        try: # Основной код омещаем в try, чтобы ловить исключения в except
            predict = np.random.randint(low, high) 
            count += 1 

            if predict < number:
                low = predict + 1 # уменьшаем диапзон подбора числа 

            elif predict > number:
                high = predict # уменьшаем диапзон подбора числа 

            elif predict == number:
                break 
        except: # Отработка исключений
            print("Ошибка! Обртитесь в службу поддежки!" )
            
    return count


# In[69]:


# Проверяем
score_game(game_core_v4) 


# In[ ]:





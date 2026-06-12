#Добавлять доходы и расходы с указанием суммы и категории
#(например, «Еда», «Транспорт»). Просматривать текущий баланс.
#Видеть историю всех транзакций.
import csv
import os
import pandas as pd
print("""
      Добро пожаловать!
      1 - Чтобы добавить расходы
      2 - чтобы добавить дохода
      3 - чтобы просмотреть свой текущий баланс
      ex - в поле суммы чтобы выйти
      """)
columns = ['summ','category','date']
if not os.path.exists('base.csv'):
    with open('base.csv','w', newline= '', encoding= 'utf-8') as file:
        write = csv.DictWriter(file, fieldnames= columns)
        write.writeheader()
    print('вонючая псина база данных для тебя готова')

if not os.path.exists('base1.csv'):
    with open('base1.csv','w', newline= '', encoding= 'utf-8') as file:
        write = csv.DictWriter(file, fieldnames= columns)
        write.writeheader()
    print('вонючая псина база данных для тебя готова')
df = pd.read_csv("base.csv")
df1 = pd.read_csv('base1.csv')
uschoice = input("Выбериите операцию: ")
if uschoice == "1":
    while True:
        ussum = input("Введите потраченную сумму: ")
        if ussum == 'ex':
            print('мы сольем твои данные урод не возвращайся')
            break
        uscat = input('Введите категорию расхода: ')
        usdate = input('Введите дату расхода ')
        a = {"summ" : ussum,
            'category' : uscat,
            'date' : usdate }
        with open('base.csv', 'a',newline='',encoding= 'utf-8') as file:
            write = csv.DictWriter(file,fieldnames= columns)
            write.writerow(a)
elif uschoice == '2':
   while True:
        ussum = input("Введите заработанную сумму: ")
        if ussum == 'ex':
            print('мы сольем твои данные урод не возвращайся')
            break
        uscat = input('Введите категорию дохода: ')
        usdate = input('Введите дату дохода ')
        a = {"summ" : ussum,
            'category' : uscat,
            'date' : usdate }
        with open('base1.csv', 'a',newline='',encoding= 'utf-8') as file:
            write = csv.DictWriter(file,fieldnames= columns)
            write.writerow(a)

elif uschoice == "3":
    print(f'ваш текущий баланс: {df1['summ'].sum() - df['summ'].sum()}')
    print(f'расходы: {df['summ'].sum()}\nдоходы: {df1['summ'].sum()}')


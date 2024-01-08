import time
import pandas as pd
import os

def add_record():
    Cat = str(input("Enter a name of Category"))
    Prod = str(input("Enter a name of Product"))
    Cost = float(input("Enter cost fo Product"))
    Date = input('Enter Date (dd-mm-yyyy): ')
    try:
        valid_date = time.strptime(Date, '%d-%m-%Y')
    except ValueError:
        print('Invalid date!')
    df = pd.read_csv("Shop_list.csv", sep=',')
    df2 = pd.DataFrame({'Category': [Cat], 'Product': [Prod], 'Cost': [Cost], 'Date': [Date]})
    df2.to_csv('Shop_list.csv', mode='a', header=False, index=False)
    print(f'Category: {Cat} \n Product: {Prod} \n Cost: {Cost} \n Date: {Date} \n Thanks! Have a good day!)')


#add_record()


def show_all():
    df = pd.read_csv("Shop_list.csv", sep=',')
    print(df[['Category', 'Product', 'Cost', 'Date']])

#show_all()

def show_for_date():
    df = pd.read_csv("Shop_list.csv", sep=',')
    print(df['Date'])
    Date = input('Enter Date (dd-mm-yyyy): ')
    try:
        valid_date = time.strptime(Date, '%d-%m-%Y')
    except ValueError:
        print('Invalid date!')
    df_print = pd.DataFrame(df.loc[df['Date'] == Date])
    res = df_print.values
    print(res)

#show_for_date()

def  show_by_category():
    df = pd.read_csv("Shop_list.csv", sep=',')
    print(df['Category'])
    Cat = str(input('Enter Category: '))
    #try:
    #    valid_date = time.strptime(Date, '%d-%m-%Y')
    #except ValueError:
    #    print('Invalid date!')
    df_print = pd.DataFrame(df.loc[df['Category'] == Cat])
    res = df_print.values
    print(res)

#show_by_category()

def show_by_min_max():
    df = pd.read_csv("Shop_list.csv", sep=',')
    df_sort = df.sort_values(by='Category', ascending=True)
    print(df_sort)

# show_by_min_max()

def delete_row():
    df = pd.read_csv("Shop_list.csv", sep=',')
    print(df)
    del_row = int(input("Enter index of row you want to delete: "))
    new_df = df.drop(index=[del_row])
    new_df.to_csv("Shop_list.csv", sep=',', index=False)
    print(new_df)

# delete_row()
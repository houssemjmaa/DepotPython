from openpyxl import Workbook, load_workbook
import logging
import pandas as pd
import re;


def OPEN_FILE():
    try:

        fichiers = ['/Users/USER/Desktop/FILE/FILE.xlsx']

        fichier_combine = pd.DataFrame()

        #  print (fichier_combine)

        return fichiers

    except:

        print('Fichier introuvable')


def READ_FILE(FILE, val):
    try:

        for fichier in FILE:
            df = pd.read_excel(fichier, skiprows=val)
            print(df)
            #    print(df)
            return df
    except:

        print('Problème lecture Fichier')


def Extract_File():
    data = pd.read_excel("FILE.xlsx");
    # print("NAME")
    # print(data)

    data['MATH'] = None
    #  print(data)
    index_set = data.columns.get_loc('ENGLISH')
    index_time = data.columns.get_loc('MATH')
    print('index_set', '=', index_set)
    print('index_time', '=', index_time)

    #  print(index_set, index_time)
    a = data['NAME']
    Table = data['GYM']
    for i in range(len(a)):
        Table1 = Table[i]
        c = a[i]
        # print(c)
        pos1 = c.find('*')
        pos2 = c.find(':') + 1
        d = c[pos2:len(c)]
        print(d, '=', Table1)


a = OPEN_FILE()
Result = READ_FILE(a, 0)
Extract_File()
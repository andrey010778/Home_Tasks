import glob
import pandas as pd
import datetime
import logging

timestring = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
today = 0

logfile = 'log_concat_csv' + '.log'
logging.basicConfig(filename=logfile, level=logging.DEBUG)




'''Рабочая функция записи чтения, формирования DataFrame и записи,
 перехвата ошибки наличия файла'''

def concat_csv(filenames):
    dfs = []
    try:
        for filename in filenames:
            dfs.append(pd.read_csv(filename))
            big_frame = pd.concat(dfs, ignore_index=True)
            c = 'C:\\Data\\P16B\\{}_bigdata.csv'.format(datetime.datetime.now().strftime("%d%m%Y_%H%M"))
            logging.info(c)
            big_frame.to_csv(c, encoding='utf-8')

    except Exception as e:
            e = f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M")}, {e}'
            logging.error(e)


path = "C:\\Data\\P16B\\"
filenames = (path + "orderdata_sample_1.csv", path + "orderdata_sample_2.csv")
concat_csv(filenames)
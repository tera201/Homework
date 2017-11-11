trades = {'V': [], 'D': [], 'X': [], 'Y': [], 'B': [], 'J': [], 'Q': [], 'Z': [], 'K': [], 'P': [], 'All': []}
max = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}
times = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}
from decimal import *

def Second(time):
    time_list = time.split(':')
    return float(time_list.pop()) + int(time_list.pop()) * 60 + int(time_list.pop()) * 3600


def cell(line_table):
    list_line = line_table.split(',')
    time = Second(list_line[0])
    exchange = list_line[3][0]
    append_trade(time, exchange)


def append_trade(time, exchange):
    trades[exchange].append(time)
    while time - trades[exchange][0] >= 1:
        trades[exchange].pop(0)
    if len(trades[exchange]) > max[exchange]:
        max[exchange] = len(trades[exchange])
        times[exchange] = trades[exchange][0]
    if exchange != 'All':
        exchange = 'All'
        append_trade(time, exchange)


def str_time(time):
    str_min,str_hours,str_sec = '','',''
    hour = int(time // 3600)
    time -= hour * 3600
    min = int(time // 60)
    sec = Decimal(time - min * 60).quantize(Decimal('.000'))
    if min < 10: str_min = '0'
    if sec < 10: str_sec = '0'
    return str_hours + str(hour) + ':' + str_min + str(min) + ':' + str_sec + str(sec)


with open("TRD2.csv") as f:
    f.readline()
    for line in f.readlines():
        cell(line)

for i in max:
    print(i,':','  ',str(max[i]), '    ',str_time(times[i]))

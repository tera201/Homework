def get_time(line):
    return int(line[3:-7]) * 60 * 1000 + int(line[6:-4]) * 1000 + int(line[-3:])


class Exchange:
    def __init__(self, name):
        self.name=name
        self.db = []
        self.i = 0
        self.max_num = 0
        self.max_second_start = 0
        self.max_second_start_str = 0
        self.left_bound_time_str = next(x for x in db if x[3][0] == name)[0]
        self.left_bound_time = get_time(self.left_bound_time_str)
        self.left_bound_index = 0
        self.curr_num = 1
        self.curr_time_str = ''


def count_overall():
    i = 0
    max_num = 0
    max_second_start_str = ''
    left_bound_time_str = db[0][0]
    left_bound_time = get_time(left_bound_time_str)
    left_bound_index = 0
    curr_num = 1

    for row in db:
        if i > 0:
            curr_time_str = row[0]
            curr_time = get_time(curr_time_str)
            if curr_time - left_bound_time <= 1000:
                curr_num += 1
            else:
                if curr_num > max_num:
                    max_num = curr_num
                    max_second_start_str = left_bound_time_str
                while curr_time - left_bound_time > 1000 and left_bound_index != i:
                    left_bound_index += 1
                    left_bound_time_str = db[left_bound_index][0]
                    left_bound_time = get_time(left_bound_time_str)
                    curr_num -= 1
                curr_num += 1
        i+=1
    print('Overall', max_second_start_str, max_num)


def count_exchange(e):
    i=0
    for row in e.db:
        if i > 0:
            e.curr_time_str = row[0]
            e.curr_time = get_time(e.curr_time_str)

            if e.curr_time - e.left_bound_time <= 1000:
                e.curr_num += 1
            else:
                if e.curr_num > e.max_num:
                    e.max_num = e.curr_num
                    e.max_second_start_str = e.left_bound_time_str
                while e.curr_time - e.left_bound_time > 1000 and e.left_bound_index != i:
                    e.left_bound_index += 1
                    e.left_bound_time_str = e.db[e.left_bound_index][0]
                    e.left_bound_time = get_time(e.left_bound_time_str)
                    e.curr_num -= 1
                e.curr_num += 1
        i+=1
    print(e.name, e.max_second_start_str, e.max_num)


es = {'V': None, 'D': None, 'X': None, 'Y': None, 'B': None, 'J': None, 'Q': None, 'Z': None, 'K': None, 'P': None}
with open('TRD2.csv') as f:
    db = f.readlines()
    del(db[0])
    for i in range(0, db.__len__()):
        db[i] = db[i].split(',')
    for e in es:
        es[e] = Exchange(e)
    for i in range(0, db.__len__()):
        es[db[i][3][0]].db.append(db[i])

    count_overall()

    for e in es:
        count_exchange(es[e])

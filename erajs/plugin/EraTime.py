import sys


class Plugin:
    pass


class EraTime:
    '''时/日/周/月/季/年
    日of周/日of月/日of年/月of年/季of年
    默认值：1年 = 4季 = 8月 = 16周 = 112日 = 224昼/夜
    年：
    季：太阳：温度
    月：月亮：湿度（潮汐）
    周：星星：月火水木金土日
    日：地球
    '''
    WEEKDAY_ORDER = ['月', '火', '水', '木', '金', '土', '日']
    TIME_ORDER = ['昼', '夜']
    SEASON_ORDER = ['春', '夏', '秋', '冬']
    MONTH_ORDER = ['乾', '坤', '震', '巽', '坎', '离', '艮', '兑']
    WEEKS_IN_A_MONTH = 2
    MONTHS_IN_A_SEASON = 2
    # 1...
    CURRENT_DAY = 0
    # 第1天 日之周 日曜日 春昼
    days_in_a_month = len(WEEKDAY_ORDER) * WEEKS_IN_A_MONTH
    days_in_a_season = days_in_a_month * MONTHS_IN_A_SEASON
    days_in_a_year = days_in_a_season * len(SEASON_ORDER)

    def __init__(self):
        pass

    def get_time(self, isText=False):
        '''昼夜'''
        if self.CURRENT_DAY % 1 == 0:
            if isText:
                return '昼'
            return 0
        elif self.CURRENT_DAY % 1 == 0.5:
            if isText:
                return '夜'
            return 1

    def get_day(self, isText=False):
        '''第几天（绝对）'''
        if isText:
            return str(int(self.CURRENT_DAY)+1)
        return int(self.CURRENT_DAY) + 1

    def get_week(self, isText=False):
        '''第几周（绝对）'''
        if isText:
            return str(int(self.CURRENT_DAY/len(self.WEEKDAY_ORDER)) + 1)
        return int(self.CURRENT_DAY/len(self.WEEKDAY_ORDER)) + 1

    def get_month(self, isText=False):
        '''第几月（绝对）'''
        if isText:
            return str(int(self.CURRENT_DAY/self.days_in_a_month)+1)
        return int(self.CURRENT_DAY/self.days_in_a_month) + 1

    def get_season(self, isText=False):
        '''第几季（绝对）'''
        if isText:
            return str(int(self.CURRENT_DAY/self.days_in_a_season)+1)
        return int(self.CURRENT_DAY/self.days_in_a_season) + 1

    def get_year(self, isText=False):
        '''第几年（绝对）'''
        if isText:
            return str(int(self.CURRENT_DAY / self.days_in_a_year)+1)
        return int(self.CURRENT_DAY / self.days_in_a_year) + 1

    def get_day_in_week(self, isText=False):
        '''第几天（周内）（星期几）：日/月/火/水/木/金/土'''
        if isText:
            return self.WEEKDAY_ORDER[int(self.CURRENT_DAY % len(self.WEEKDAY_ORDER))]
        return int(self.CURRENT_DAY % len(self.WEEKDAY_ORDER)) + 1

    def get_day_in_month(self, isText=False):
        '''第几天（月内）'''
        return int(self.CURRENT_DAY % self.days_in_a_month) + 1

    def get_day_in_year(self, isText=False):
        '''第几天（年内）'''
        pass

    def get_month_in_year(self):
        '''第几月（年内）'''
        return int(self.CURRENT_DAY/self.WEEKS_IN_A_MONTH/len(self.WEEKDAY_ORDER)) + 1

    def get_season_in_year(self, isText=False):
        '''第几季（年内）：春/夏/秋/冬'''
        if isText:
            return self.SEASON_ORDER[int(self.CURRENT_DAY % self.days_in_a_year / self.days_in_a_season)]
        return int(self.CURRENT_DAY % self.days_in_a_year / self.days_in_a_season) + 1

    def get_sys_time(self):
        '''获取时间原始值'''
        return self.CURRENT_DAY

    def set_sys_time(self, value):
        '''设定时间原始值'''
        self.CURRENT_DAY = value

    def get_full_time(self):
        '''获取全文本时间'''
        # 1年1月1日 日之周 日曜日 春昼
        temp = '第{0}年 {1}月{2}日 第{3}周 {4}耀日 {5}{6}'
        text_list = [
            self.get_year(),
            self.get_month_in_year(),
            self.get_day_in_month(),
            self.get_week(),
            self.get_day_in_week(True),
            self.get_season_in_year(True),
            self.get_time(True)
        ]
        return temp.format(*text_list)

    def tick(self):
        '''时间流逝一个单位'''
        print(self.CURRENT_DAY)
        self.CURRENT_DAY += 0.5


def register(data):
    global EraTime
    data['plugin']['time'] = EraTime
    data['entity']['time'] = EraTime()
    if not 'time' in data['db'].keys():
        data['db']['time'] = {
            'CURRENT_DAY': 0
        }
    # data['entity']['time'].load(data['db']['time'])
    func_list = [
        data['entity']['time'].get_time,
        data['entity']['time'].get_day,
        data['entity']['time'].get_week,
        data['entity']['time'].get_month,
        data['entity']['time'].get_season,
        data['entity']['time'].get_year,
        data['entity']['time'].get_day_in_week,
        data['entity']['time'].get_day_in_month,
        data['entity']['time'].get_day_in_year,
        data['entity']['time'].get_month_in_year,
        data['entity']['time'].get_season_in_year,
        data['entity']['time'].get_sys_time,
        data['entity']['time'].set_sys_time,
        data['entity']['time'].get_full_time,
        data['entity']['time'].tick
    ]
    for each in func_list:
        data['api'][each.__name__] = each


register(sys.argv[0])
# import math

# ORDER = ['日', '月', '火', '水', '木', '金', '土']
# TIME_ORDER = ['昼', '夜']
# SEASON_ORDER = ['春', '夏', '秋', '冬']
# DAYS_IN_A_MONTH = 30
# # 1...
# CURRENT_DAY = 1
# # 昼/夜
# CURRENT_TIME = '昼'
# # 第1天 日之周 日曜日 春昼


# def tick():
#     global CURRENT_TIME, CURRENT_DAY
#     if CURRENT_TIME == TIME_ORDER[0]:
#         CURRENT_TIME = TIME_ORDER[1]
#     elif CURRENT_TIME == TIME_ORDER[1]:
#         CURRENT_TIME = TIME_ORDER[0]
#         CURRENT_DAY += 1


# def get_full_time():
#     full_time_list = []
#     full_time_list.append('第{}日'.format(get_day()))
#     full_time_list.append('{}之周'.format(get_week()))
#     full_time_list.append('{}曜日'.format(get_weekday()))
#     full_time_list.append('{}{}'.format(get_season(), get_time()))
#     return ' '.join(full_time_list)


# def get_time():
#     return CURRENT_TIME


# def get_day():
#     return CURRENT_DAY


# def get_weekday():
#     index = ()
#     return ORDER[(CURRENT_DAY - 1) % 7]


# def get_week():
#     i = int(math.floor((CURRENT_DAY - 1) / 7))
#     i = i % 7
#     return ORDER[i]


# def get_season():
#     i = int(math.floor((CURRENT_DAY - 1) / DAYS_IN_A_MONTH))
#     i = i % 4
#     return SEASON_ORDER[i]

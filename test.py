import requests
import sys
import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
import openpyxl
mpl.rcParams['font.sans-serif'] = ['SimHei']

list1 = []  #日数据
list2 = []  #日期(日)
list3 = []  #月数据
list4 = []  #日期(月)
list5 = []  #年数据
list6 = []  #日期(年)
list7 = []  #日数据2
list8 = []  #日数据3
list9 = []  #日数据4
list10 = []  #日数据5
list11 = []  #日数据6

dict1 = {}  #日
dict2 = {}  #月
dict3 = {}  #年
dict4 = {}  #日2
dict5 = {}  #日3

word_url = 'http://index.baidu.com/api/SearchApi/thumbnail?area=0&word={}'
COOKIES = 'BIDUPSID=0F419F4317FCAFBECF4987E39A8BBE49; PSTM=1636079487; BAIDUID=0F419F4317FCAFBE6DA5B6D78DAB8E6B:FG=1; __yjs_duid=1_e52d05c6f29311313252eff5b863c2791636094005643; ab_jid=7b7ee9a0cfd4c318dd5594b04e56eca4275d; ab_jid_BFESS=7b7ee9a0cfd4c318dd5594b04e56eca4275d; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=hUTG9ISU13ajFqNnA1blZQa1J0eUY5fnFYYm5lVmw1SEZ4WkJodHgybUVYaFJpRVFBQUFBJCQAAAAAAAAAAAEAAAAH~GxNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAITR7GGE0exhVU; BDUSS_BFESS=hUTG9ISU13ajFqNnA1blZQa1J0eUY5fnFYYm5lVmw1SEZ4WkJodHgybUVYaFJpRVFBQUFBJCQAAAAAAAAAAAEAAAAH~GxNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAITR7GGE0exhVU; BAIDUID_BFESS=0F419F4317FCAFBE6DA5B6D78DAB8E6B:FG=1; H_PS_PSSID=35414_35785_35105_31253_35488_35774_34584_35490_35797_35319_26350; delPer=0; PSINO=5; BA_HECTOR=0g84al8la1a10l8hpu1guuk4k0r; bdindexid=ctpb23eblqa304q6u5ra6avvn0; ab_bid=94b04e56eca4275dd8dc46fe2d3220763ab2; ab_sr=1.0.1_YTM0NzViZWYzYWRlZmYxMzEzMTgwYmY5NmQ0MjhhNjZkYmVmNjRjMDQzZDU5OGRhZjMxMDA0OWY2YjQzZDE2Mzg4ZDA5YjI5NDU0NWIwYTAzMTA3Mjg0YjgzY2Q4MjJl; __yjs_st=2_NzRkY2UzNTBmYzA3MWFiMzRmZDBmNGNhNzc4N2JmZGZmOGNmMGM5ZDM3ZmM0MWM0ZjZkOWI1ZDBlMTkwYTE2MDlhZDYyYjMwMmIxZjI1MDk0MTQ1MGRmMGJmMGZiZjQ1ZDY2MTZkOWMyMTkxNTFjMzlmOTc0ODRkMTk3Yzc0NmE5MjNhNDk2NjA2MjEwNjQ3ZTkwMDQ0Njk1MTg4NjcwZTAyMjI2YmY2MzZiM2M5NWE3MTI5OWJhNmU5ZjU2ZGZiXzdfYmI3M2RkZGM=; RT="z=1&dm=baidu.com&si=6kiy366iwbh&ss=kytfnfwi&sl=a&tt=94o&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=cr59"'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Cookie': COOKIES,
    'DNT': '1',
    'Host': 'index.baidu.com',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://index.baidu.com/v2/main/index.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# 解密
def decrypt(t, e):
    n = list(t)
    i = list(e)
    a = {}
    result = []
    ln = int(len(n) / 2)
    start = n[ln:]
    end = n[:ln]
    for j, k in zip(start, end):
        a.update({k: j})
    for j in e:
        result.append(a.get(j))
    return ''.join(result)

# 定位到date数据
def get_ptbk(uniqid):
    url = 'http://index.baidu.com/Interface/ptbk?uniqid={}'
    resp = requests.get(url.format(uniqid), headers=headers)
    if resp.status_code != 200:
        print('获取uniqid失败')
        sys.exit(1)
    return resp.json().get('data')

# 根据关键词，日期取对应数据
def get_index_data(keyword, start, end, level):
    keyword = str(keyword).replace("'", '"')
    url = f'http://index.baidu.com/api/SearchApi/index?area=0&word={keyword}&area=0&startDate={start}&endDate={end}'
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print('获取指数失败')
        sys.exit(1)
    content = resp.json()
    data = content.get('data')
    user_indexes = data.get('userIndexes')[0]
    uniqid = data.get('uniqid')
    ptbk = get_ptbk(uniqid)
    while ptbk is None or ptbk == '':
        ptbk = get_ptbk(uniqid)

    # 取date数据
    if level==1:
        all_data = user_indexes.get('all').get('data')
        result = decrypt(ptbk, all_data)
        list = result.split(',')
        for i in list:
            if i == "":
                list1.append(0)
            else:
                list1.append(eval(i))

        # 自动补全日期并存入列表list2
        dateend = user_indexes.get('all').get('startDate')
        datestart = user_indexes.get('all').get('endDate')
        datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
        dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
        list2.append(datestart.strftime('%Y-%m-%d'))
        while datestart < dateend:
            datestart += datetime.timedelta(days=1)
            list2.append(datestart.strftime('%Y-%m-%d'))
    elif level==2:
        all_data = user_indexes.get('all').get('data')
        result = decrypt(ptbk, all_data)
        list = result.split(',')
        for i in list:
            if i == "":
                list7.append(0)
            else:
                list7.append(eval(i))
    elif level == 3:
        all_data = user_indexes.get('all').get('data')
        result = decrypt(ptbk, all_data)
        list = result.split(',')
        for i in list:
            if i == "":
                list8.append(0)
            else:
                list8.append(eval(i))
    elif level == 4:
        all_data = user_indexes.get('all').get('data')
        result = decrypt(ptbk, all_data)
        list = result.split(',')
        for i in list:
            if i == "":
                list9.append(0)
            else:
                list9.append(eval(i))
    elif level == 5:
        all_data = user_indexes.get('all').get('data')
        result = decrypt(ptbk, all_data)
        list = result.split(',')
        for i in list:
            if i == "":
                list10.append(0)
            else:
                list10.append(eval(i))
    else:
        all_data = user_indexes.get('all').get('data')
        result = decrypt(ptbk, all_data)
        list = result.split(',')
        for i in list:
            if i == "":
                list11.append(0)
            else:
                list11.append(eval(i))

    dict11 = dict(zip(list2,list1))      # 该处使用zip必须先定义一个dict(局部变量)
    dict1.update(dict11)                 # 把局部变量赋值给全局变量(克隆没用!!!)
    dict12 = dict(zip(list2,list7))
    dict4.update(dict12)

    # 统计月数据
    b = 1                               # 表示月
    for i in dict1.keys():
        sum = 0
        a = i[:7]
        if a == b:
            continue
        b = a
        for j,k in dict1.items():
            if j[:7] == b:
                sum += k
        dict2[b] = sum
    for key,value in dict2.items():
        list4.append(key)
        list3.append(value)

    # 统计年数据
    for i in dict2.keys():
        sum = 0
        a = i[:4]
        if a == b:
            continue
        b = a
        for j,k in dict2.items():
            if j[:4] == b:
                sum += k
        dict3[b] = sum
    for key,value in dict3.items():
        list6.append(key)
        list5.append(value)

def DrawDay():
    plt.style.use('seaborn')
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.figure(figsize=(16, 9))
    plt.title("全国网民对“困境儿童”的百度搜索频次及趋势",size=30)
    plt.xlabel("日期",size=20)
    plt.ylabel("百度搜索频次",size=20)
    plt.plot(list2, list1, linewidth='2.0', marker='o', markerfacecolor='blue', markersize='5', label='困境儿童')

    ax = plt.gca()                             # 获取图的坐标信息
    # xlocator = mpl.ticker.LinearLocator(10)    # 设置x轴显示多少个刻度
    xlocator = mpl.ticker.MultipleLocator(14)  # 设置x轴每个刻度的间隔数
    ax.xaxis.set_major_locator(xlocator)

    plt.xticks(rotation=0, fontsize=11)      # 设置x轴label
    plt.yticks(fontsize=15)                  # 设置y轴label
    plt.legend(fontsize=20)                  # 设置图例
    plt.savefig('day.png')
    plt.show()

def DrawMonth():
    plt.title("七月",size=24)
    plt.xlabel("日期",size=20)
    plt.ylabel("频数",size=20)
    plt.xticks(rotation=20, fontsize=9)
    plt.plot(list4,list3,linewidth='2.5', marker='o',markerfacecolor='blue',markersize='5',label='')
    plt.show()

def DrawYear():
    plt.title("2020年",size=24)
    plt.xlabel("日期",size=20)
    plt.ylabel("频数",size=20)
    plt.xticks(rotation=20, fontsize=9)
    plt.plot(list6,list5,linewidth='2.5',marker='o',markerfacecolor='blue',markersize='5',label='')
    plt.show()

def DrawTwo():
    plt.style.use('ggplot')
    plt.figure(figsize=(16, 9))
    plt.grid(1)                        # 是否显示网格线
    plt.title("困境儿童与心理救助百度指数的变化趋势",size=30)
    plt.xlabel("日期",size=20)
    plt.ylabel("百度搜索频次",size=20)
    plt.plot(list2, list1, linestyle='-', linewidth='2.0', marker='o', markerfacecolor='blue', markersize='5', label='困境儿童')
    plt.plot(list2, list7, linestyle='--', linewidth='2.0', marker='o', markerfacecolor='blue', markersize='5', label='心理救助')

    ax = plt.gca()                             # 获取图的坐标信息
    # xlocator = mpl.ticker.LinearLocator(10)    # 设置x轴显示多少个刻度
    xlocator = mpl.ticker.MultipleLocator(14)  # 设置x轴每个刻度的间隔数
    ax.xaxis.set_major_locator(xlocator)

    plt.xticks(rotation=0, fontsize=11)      # 设置x轴label
    plt.yticks(fontsize=15)                  # 设置y轴label
    plt.legend(fontsize=20)                  # 设置图例
    plt.savefig('困境儿童与心理救助.png')
    plt.show()

def DrawThree():
    plt.style.use('ggplot')
    plt.figure(figsize=(16, 9))
    plt.grid(1)                        # 是否显示网格线
    plt.title("困境儿童心理救助与社会工作百度指数的变化趋势",size=30)
    plt.xlabel("日期",size=20)
    plt.ylabel("百度搜索频次",size=20)
    plt.plot(list2, list1, linestyle='-', linewidth='1.0', marker='o', markerfacecolor='blue', markersize='3', label='困境儿童')
    plt.plot(list2, list7, linestyle='-', linewidth='1.0', marker='o', markerfacecolor='blue', markersize='3', label='心理救助')
    plt.plot(list2, list8, linestyle='-.', linewidth='1.0', marker='o', markerfacecolor='red', markersize='3', label='社会工作')

    ax = plt.gca()                             # 获取图的坐标信息
    # xlocator = mpl.ticker.LinearLocator(10)    # 设置x轴显示多少个刻度
    xlocator = mpl.ticker.MultipleLocator(14)  # 设置x轴每个刻度的间隔数
    ax.xaxis.set_major_locator(xlocator)

    plt.xticks(rotation=0, fontsize=11)      # 设置x轴label
    plt.yticks(fontsize=15)                  # 设置y轴label
    plt.legend(fontsize=20)                  # 设置图例
    plt.savefig('困境儿童心理救助与社会工作.png')
    plt.show()

def DrawMore():
    plt.style.use('ggplot')
    plt.figure(figsize=(16, 9))
    plt.grid(1)                        # 是否显示网格线
    plt.title("网民对不同困境类别的困境儿童的整体关注度",size=30)
    plt.xlabel("日期",size=20)
    plt.ylabel("百度搜索频次",size=20)
    plt.plot(list2, list1, linestyle='-', linewidth='1.0', marker='o', markerfacecolor='blue', markersize='2', label='留守儿童')
    plt.plot(list2, list7, linestyle='-', linewidth='1.0', marker='o', markerfacecolor='blue', markersize='2', label='贫困儿童')
    plt.plot(list2, list8, linestyle='-', linewidth='1.0', marker='o', markerfacecolor='red', markersize='2', label='流动儿童')
    plt.plot(list2, list9, linestyle='-', linewidth='1.0', marker='o', markerfacecolor='red', markersize='2', label='孤儿')
    plt.plot(list2, list10, linestyle='-', linewidth='1.0', marker='o', markerfacecolor='red', markersize='2', label='流浪儿童')
    plt.plot(list2, list11, linestyle='-', linewidth='1.0', marker='o', markerfacecolor='red', markersize='2', label='受虐儿童')
    ax = plt.gca()                             # 获取图的坐标信息
    # xlocator = mpl.ticker.LinearLocator(10)    # 设置x轴显示多少个刻度
    xlocator = mpl.ticker.MultipleLocator(14)  # 设置x轴每个刻度的间隔数
    ax.xaxis.set_major_locator(xlocator)

    plt.xticks(rotation=0, fontsize=11)      # 设置x轴label
    plt.yticks(fontsize=15)                  # 设置y轴label
    plt.legend(fontsize=20)                  # 设置图例
    plt.savefig('网民对不同困境类别的困境儿童的整体关注度1.png')
    plt.show()

def SaveDay():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '关键字\"虐童\"的百度指数'
    sheet.append(['日期','百度指数'])
    for key,value in dict1.items():
        sheet.append([key,value])
    wb.save('困境儿童(按日).xlsx')

def SaveMonth():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '关键字\"虐童\"的百度指数'
    sheet.append(['日期','百度指数'])
    for key,value in dict2.items():
        sheet.append([key,value])
    wb.save('困境儿童(按月).xlsx')

if __name__ == '__main__':
    words = [[{"name": "留守儿童", "wordType": 1}]]
    get_index_data(words,'2021-02-28','2022-02-28',1)
    words1 = [[{"name": "贫困儿童", "wordType": 1}]]
    get_index_data(words1,'2021-02-28','2022-02-28',2)
    words2 = [[{"name": "流动儿童", "wordType": 1}]]
    get_index_data(words2,'2021-02-28','2022-02-28',3)
    words3 = [[{"name": "孤儿", "wordType": 1}]]
    get_index_data(words3,'2021-02-28','2022-02-28',4)
    words4 = [[{"name": "流浪儿童", "wordType": 1}]]
    get_index_data(words4,'2021-02-28','2022-02-28',5)
    words5 = [[{"name": "受虐儿童", "wordType": 1}]]
    get_index_data(words5,'2021-02-28','2022-02-28',6)
    print(list1)
    print(list2)
    print(list7)
    print(list8)
    # print(list7)
    # DrawDay()
    # DrawMonth()
    # DrawYear()
    # DrawTwo()
    # DrawThree()
    DrawMore()
    # SaveDay()
    # SaveMonth()
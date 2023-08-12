# -*- coding:utf-8 -*-
import gopup as gp
import matplotlib.pyplot as plt


# 微博指数
# df_index1 = gp.weibo_index(word="儿童", time_type="3month")
# df_index2 = gp.weibo_index(word="困境未成年人", time_type="3month")
# df_index3 = gp.weibo_index(word="受虐儿童", time_type="3month")
# df_index4 = gp.weibo_index(word="受虐未成年人", time_type="3month")
# df_index5 = gp.weibo_index(word="受欺凌儿童", time_type="3month")
# df_index6 = gp.weibo_index(word="受欺凌未成年人", time_type="3month")
# df_index7 = gp.weibo_index(word="受性侵儿童", time_type="3month")
# df_index8 = gp.weibo_index(word="受性侵未成年人", time_type="3month")
# df_index9 = gp.weibo_index(word="受忽视儿童", time_type="3month")

# print(df_index1)
# print("---------------------------------")
# plt.figure(figsize=(15, 5))
# plt.title("微博「疫情」热度走势图")
# plt.xlabel("时间")
# plt.ylabel("指数")
# plt.plot(df_index1.index, df_index1['儿童'], '-', label="指数")
# plt.legend()
# plt.grid()
# plt.show()

# print(df_index2)
# print("---------------------------------")
# print(df_index3)
# print("---------------------------------")
# print(df_index4)
# print("---------------------------------")
# print(df_index5)
# print("---------------------------------")
# print(df_index6)
# print("---------------------------------")
# print(df_index7)
# print("---------------------------------")
# print(df_index8)
# print("---------------------------------")
# print(df_index9)
# print("---------------------------------")

# 算数指数
# index_df = gp.toutiao_index(keyword="口罩", start_date='20201016', end_date='20201022', app_name='aweme')
# print(index_df)
# print("---------------------------------")

# # 谷歌数据
# index_df = gp.google_index(keyword="困境儿童", start_date='2021-09-01T10', end_date='2022-10-20T23')
# print(index_df)
# print("---------------------------------")
#
# # 搜狗指数
# df_index = gp.sogou_index(keyword="困境儿童", start_date="20210901", end_date="20221020", data_type="SEARCH_ALL")
# print(df_index)
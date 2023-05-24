import math
import pandas as pd

# 读取原有的Excel文件
try:
    result_df = pd.read_excel('C:\\Users\\25428\Desktop\\0.1s_data.xlsx')
except FileNotFoundError:
    # 如果文件不存在，则创建一个新的空DataFrame
    result_df = pd.DataFrame(columns=['time', 'difference'])

# 读取数据
df = pd.read_excel('C:\\Users\\25428\Desktop\\第二段视频数据.xlsx')

# 初始化上一个时刻和x值
last_t = df.loc[0, 't']
last_x = df.loc[0, 'x']
slide =False
# 遍历数据，找出每隔秒的x的差
#for j in range(0,len(df)):
for i in range(0, len(df)):
    current_t = df.loc[i, 't']
    current_x = df.loc[i, 'x']
    if 0.09999<=current_t-last_t<=0.10001:#判断差是否满足时间间隔条件
        diff_x = current_x - last_x
        result_df = result_df.append({'time': current_t, 'difference': diff_x}, ignore_index=True)
        last_t = current_t
        last_x = current_x
    if current_t-last_t>0.10001:
        last_t = df.loc[i+1, 't']
        last_x = df.loc[i+1, 'x']
# 保存结果到Excel文件
result_df.to_excel("C:\\Users\\25428\Desktop\\0.1s_data.xlsx", index=False)


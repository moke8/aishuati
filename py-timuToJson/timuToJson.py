import tkinter as tk
from tkinter import filedialog
import re,time,random,json

root = tk.Tk()
root.withdraw()

# 获取选择好的文件  读取文件
filePath = filedialog.askopenfilename(filetypes=[('txt', '*.txt')])
f = open(filePath, 'r', encoding='UTF-8')
data = f.read()
data=data.replace('．','.')
f.close()
# 不同题目分割
pattern = re.compile(r'(?:^|\n\s*)\d+?[\.\。]')
data = pattern.split(data)
# 将每个题目分为题目、选项、答案
result = []
for i in data:
    pattern = re.compile(r'\n')
    # 题目
    title = pattern.split(i)[0]
    # 选项
    option = re.findall(r'[A-E][\.\。]?(.+?)\s+[\n]?', i)
    # 答案
    daan = re.findall(r'答案[:：]([A-E]+)[\n]?', i)
    analysis = ''
    if len(daan) == 0:
        daan = re.findall(r'答案[:：]([\s\S]+)', i)
        if len(daan):
            pattern = re.compile(r'解析[:：]')
            daanList=pattern.split(daan[0])
            if len(daanList)>1:
                analysis=daanList[1]
                daan=[daanList[0]]
    else:
        # 选择题获取解析
        jiexi = re.findall(r'解析[:：]([\s\S]+)', i)
        analysis = jiexi[0] if len(jiexi) else ''
    daan = daan[0] if len(daan) else ''

# 格式化成2016-03-20 11:45:39形式
    result.append({
        'id': time.strftime("%Y%m%d%H%M", time.localtime())+str(random.randint(0,1000000)),
        'title': title,
        'option': option,
        'answer': daan,
        'analysis': analysis
    })

del(result[0])
f = open(time.strftime("%Y%m%d%H%M%S", time.localtime())+'.json', 'w',encoding = 'utf-8')
f.write(json.dumps(result,ensure_ascii=False,indent = 4))
f.close()
print("执行完成")
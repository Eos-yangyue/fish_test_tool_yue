"""zidian = {}


zidian['user_name'] = input("请输入名字：")
zidian['user_age'] = input("请输入年龄：")

fout = open('allusers', 'w', encoding='utf8')
fout.write(zidian)
fout.close()

print(zidian)
"""


"""# 打开「detail_content」文件
fout = open('detail_content', 'w', encoding='utf8')
# 写入文件内容
fout.write(content)
关闭文件
fout.close()"""

import json
dictObj = {}

dictObj['user_name'] = input("请输入名字：")
dictObj['user_age'] = input("请输入年龄：")

# 将 Python 对象编码成 JSON 字符串
jsObj = json.dumps(dictObj)

# 打开json文件，w为模式
fileObject = open('jsonFile.txt', 'a+')
fileObject.write(jsObj)

# 关闭文件
fileObject.close()
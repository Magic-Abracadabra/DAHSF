操作成功与否 = False
print('【渐得如意】请继续输入。')
长输入 = input()
while not 长输入.endswith('\n”的标签改为“'):
	长输入 += '\n'
	长输入 += input()
命令对象 = 长输入[:-8]
print('【渐得如意】请继续输入。')
长输入 = input()
while not 长输入.endswith('\n”'):
	长输入 += '\n'
	长输入 += input()
新标签 = 长输入[:-2]
del 长输入
try:
	命令对象 = 执行(命令对象, 第一层感受器)[0][0]
	老标签 = 命令对象[1]
	with open(安装目录+f'/数据库/1/{老标签}.txt', 'r', encoding='utf-8') as 文件:
		文件内容 = 文件.read().split('\n')
		临时命令库 = list(map(lambda x: x.split('\t'), 文件内容))
		命令对象 = 命令对象[-1]
		for 命令序号, 命令库的一行 in enumerate(临时命令库):
			if 命令对象==命令库的一行[0]:
				操作成功与否 = True
				移动的行 = 文件内容[命令序号]
				del 文件内容[命令序号]
				break
		del 临时命令库
		文件.close()
		if 操作成功与否:
			with open(安装目录+f'/数据库/1/{老标签}.txt', 'w', encoding='utf-8') as 文件:
				文件.write('\n'.join(文件内容))
			文件.close()
			文件地址 = 安装目录+f'/数据库/1/{新标签}.txt'
			新标签存在 = os.path.exists(文件地址)
			with open(文件地址, 'a', encoding='utf-8') as 文件:
				文件.write(int(新标签存在)*'\n'+移动的行)
			del 文件内容
			文件.close()
			for 文件 in os.listdir(安装目录+'/数据库/2'):
				文件地址 = 安装目录+'/数据库/2/'+文件
				with open(文件地址, 'r', encoding='utf-8') as 文件:
					文件内容 = 文件.read().replace(str([1, 老标签, 命令对象]), str([1, 新标签, 命令对象]))
				文件.close()
				with open(文件地址, 'w', encoding='utf-8') as 文件:
					文件.write(文件内容)
				文件.close()
			print('【渐得如意】修改成功！')
		else:
			print('【渐得如意】该命令原先并不存在，或者不是这种类型。')
	文件.close()
except:
	print('【渐得如意】您的输入有误。')
del 操作成功与否

for 文件 in os.listdir(安装目录+'/数据库/2'):
	if os.path.getsize(安装目录+'/数据库/2/'+文件)==0:
		os.remove(安装目录+'/数据库/2/'+文件)
for 文件 in os.listdir(安装目录+'/数据库/1'):
	if os.path.getsize(安装目录+'/数据库/1/'+文件)==0:
		os.remove(安装目录+'/数据库/1/'+文件)
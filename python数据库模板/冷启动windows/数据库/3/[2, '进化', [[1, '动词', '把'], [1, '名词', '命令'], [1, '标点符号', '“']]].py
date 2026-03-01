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
	命令对象 = NSS.W0(执行(命令对象, 第一层感受器)[0])
	计数数据 = dict(zip(map(lambda x: '计数_'+x, 数据类型),[0]*len(数据类型)))
	for _ in 命令对象:
		if _[1] in 数据类型:
			计数数据['计数_'+_[1]] += 1
			_[2] = f"【数据{计数数据['计数_'+_[1]]}】"
	老标签 = NSS.get_tag(命令对象)
	with open(安装目录+f'/数据库/2/{老标签}.txt', 'r', encoding='utf-8') as 文件:
		文件内容 = 文件.read().split('\n')
		临时命令库 = list(map(lambda x: x.split('\t'), 文件内容))
		命令对象 = str(命令对象)
		for 命令序号, 命令库的一行 in enumerate(临时命令库):
			if 命令对象==命令库的一行[0]:
				操作成功与否 = True
				移动的行 = 文件内容[命令序号]
				del 文件内容[命令序号]
				break
		del 临时命令库
		文件.close()
		if 操作成功与否:
			with open(安装目录+f'/数据库/2/{老标签}.txt', 'w', encoding='utf-8') as 文件:
				文件.write('\n'.join(文件内容))
			文件.close()
			新标签 = 安装目录+f'/数据库/2/{新标签}.txt'
			新标签存在 = os.path.exists(新标签)
			with open(新标签, 'a', encoding='utf-8') as 文件:
				文件.write(int(新标签存在)*'\n'+移动的行)
			del 文件内容
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
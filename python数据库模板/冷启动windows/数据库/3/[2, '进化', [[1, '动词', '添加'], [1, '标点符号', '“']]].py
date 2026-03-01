print('【渐得如意】请继续输入。')
长输入 = input('')
while not 长输入.endswith('\n”的生成规则“'):
	长输入 += '\n'
	长输入 += input('')
try:
	assert list(长输入).count('\n')==1
except:
	print('【渐得如意】您的输入格式有误。')
print('【渐得如意】请继续输入。')
生成规则 = input('')
while not 生成规则.endswith('\n”'):
	生成规则 += '\n'
	生成规则 += input('')
try:
	assert list(生成规则).count('\n')==1
	生成规则 = 生成规则[:-2]
	长输入= 执行(长输入[:-6], 第一层感受器)[0][0]
	标签 = 长输入[1]
	with open(安装目录+f'/数据库/1/{标签}.txt', 'r', encoding='utf-8') as 文件:
		临时命令库 = list(map(lambda x: x.split('\t'), 文件.read().split('\n')))
		for 等价类序号, 等价类 in enumerate(临时命令库):
			if 等价类[0]==长输入[-1]:
				等价类.append(生成规则)
				break
	文件.close()
	with open(安装目录+f'/数据库/1/{标签}.txt', 'w', encoding='utf-8') as 文件:
		文件.write('\n'.join(list(map(lambda x: '\t'.join(x), 临时命令库))))
		print('【渐得如意】添加成功！')
except:
	print('【渐得如意】您的输入格式有误。')
文件.close()
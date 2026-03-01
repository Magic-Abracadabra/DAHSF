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
	长输入= 执行(长输入[:-6], 第一层感受器)[0]
	计数数据 = dict(zip(map(lambda x: '计数_'+x, 数据类型),[0]*len(数据类型)))
	for _ in 长输入:
		if _[1] in 数据类型:
			计数数据['计数_'+_[1]] += 1
			_[2] = f"【数据{计数数据['计数_'+_[1]]}】"
	长输入 = NSS.W0(长输入)
	生成规则 = 执行(生成规则[:-2], 第一层感受器)[0]
	计数数据 = dict(zip(map(lambda x: '计数_'+x, 数据类型),[0]*len(数据类型)))
	for _ in 生成规则:
		if _[1] in 数据类型:
			计数数据['计数_'+_[1]] += 1
			_[2] = f"【数据{计数数据['计数_'+_[1]]}】"
	标签 = NSS.get_tag(长输入)
	with open(安装目录+f'/数据库/2/{标签}.txt', 'r', encoding='utf-8') as 文件:
		临时命令库 = list(map(lambda x: x.split('\t'), 文件.read().split('\n')))
		for 等价类序号, 等价类 in enumerate(临时命令库):
			if 等价类[0]==str(长输入):
				等价类.append(str(生成规则))
				break
	文件.close()
	with open(安装目录+f'/数据库/2/{标签}.txt', 'w', encoding='utf-8') as 文件:
		文件.write('\n'.join(list(map(lambda x: '\t'.join(x), 临时命令库))))
		print('【渐得如意】添加成功！')
except:
	print('【渐得如意】您的输入格式有误。')
文件.close()
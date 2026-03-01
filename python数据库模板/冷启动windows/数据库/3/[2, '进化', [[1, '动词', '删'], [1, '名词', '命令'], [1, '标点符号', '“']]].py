print('【渐得如意】请继续输入。')
操作成功与否 = False
长输入 = input('')
删除状态空间 = 长输入.endswith('\n”')
删除生成规则 = 长输入.endswith('\n”的生成规则“')
while not 删除状态空间 and not 删除生成规则:
	长输入 += '\n'
	长输入 += input('')
	删除状态空间 = 长输入.endswith('\n”')
	删除生成规则 = 长输入.endswith('\n”的生成规则“')
if 删除状态空间:
	try:
		assert list(长输入).count('\n')==1
		长输入= 执行(长输入[:-2], 第一层感受器)[0]
		计数数据 = dict(zip(map(lambda x: '计数_'+x, 数据类型),[0]*len(数据类型)))
		for _ in 长输入:
			if _[1] in 数据类型:
				计数数据['计数_'+_[1]] += 1
				_[2] = f"【数据{计数数据['计数_'+_[1]]}】"
		长输入 = NSS.W0(长输入)
		标签 = NSS.get_tag(长输入)
		with open(安装目录+f'/数据库/2/{标签}.txt', 'r', encoding='utf-8') as 文件:
			文件内容 = 文件.read().split('\n')
			临时命令库 = list(map(lambda x: x.split('\t'), 文件内容))
			长输入 = str(长输入)
			for 命令序号, 命令库的一行 in enumerate(临时命令库):
				if 长输入==命令库的一行[0]:
					操作成功与否 = True
					del 文件内容[命令序号]
					break
			del 临时命令库
			文件.close()
			if 操作成功与否:
				with open(安装目录+f'/数据库/2/{标签}.txt', 'w', encoding='utf-8') as 文件:
					文件.write('\n'.join(文件内容))
				del 文件内容
				print('【渐得如意】删除成功！')
			else:
				print('【渐得如意】该命令原先并不存在，或者不是这种类型。')
	except:
		print('【渐得如意】您的输入有误。')
elif 删除生成规则:
	print('【渐得如意】请继续输入。')
	生成规则 = input()
	while not 删除状态空间:
		生成规则 += '\n'
		生成规则 += input('')
		删除状态空间 = 生成规则.endswith('\n”')
	try:
		生成规则 = 执行(生成规则[:-2], 第一层感受器)[0]
		计数数据 = dict(zip(map(lambda x: '计数_'+x, 数据类型),[0]*len(数据类型)))
		for _ in 生成规则:
			if _[1] in 数据类型:
				计数数据['计数_'+_[1]] += 1
				_[2] = f"【数据{计数数据['计数_'+_[1]]}】"
		长输入 = 执行(长输入[:-8], 第一层感受器)[0]
		计数数据 = dict(zip(map(lambda x: '计数_'+x, 数据类型),[0]*len(数据类型)))
		for _ in 长输入:
			if _[1] in 数据类型:
				计数数据['计数_'+_[1]] += 1
				_[2] = f"【数据{计数数据['计数_'+_[1]]}】"
		长输入 = NSS.W0(长输入)
		标签 = NSS.get_tag(长输入)
		生成规则 = str(生成规则)
		长输入 = str(长输入)
		with open(安装目录+f'/数据库/2/{标签}.txt', 'r', encoding='utf-8') as 文件:
			临时命令库 = list(map(lambda x: x.split('\t'), 文件.read().split('\n')))
			for 等价类序号, 等价类 in enumerate(临时命令库):
				if 等价类[0]==长输入:
					等价类.remove(生成规则)
					break
		文件.close()
		with open(安装目录+f'/数据库/2/{标签}.txt', 'w', encoding='utf-8') as 文件:
			文件.write('\n'.join(list(map(lambda x: '\t'.join(x), 临时命令库))))
		文件.close()
		print('【渐得如意】删除成功！')
	except:
		print('【渐得如意】您的输入有误。')
else:
	class 文件():
		def __init__(self):
			pass
		def close(self):
			pass
	文件 = 文件()
	print('【渐得如意】您的输入有误。')
文件.close()
del 操作成功与否, 长输入

for 文件 in os.listdir(安装目录+'/数据库/2'):
	if os.path.getsize(安装目录+'/数据库/2/'+文件)==0:
		os.remove(安装目录+'/数据库/2/'+文件)
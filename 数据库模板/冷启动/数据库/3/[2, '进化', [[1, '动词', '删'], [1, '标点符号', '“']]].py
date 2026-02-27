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
		长输入 = 长输入[:-2]
		长输入 = NSS.W0(长输入)
		标签 = NSS.get_tag(长输入)
		with open(安装目录+f'/数据库/1/{标签}.txt', 'r', encoding='utf-8') as 文件:
			# 根据NSS的内容进行判断
			文件内容 = 文件.read().split('\n')
			临时词库 = list(map(lambda x: x.split('\t'), 文件内容))
			for 词序号, 词库的一行 in enumerate(临时词库):
				if 长输入==词库的一行[0]:
					被删的词语 = 词库的一行
					操作成功与否 = True
					del 文件内容[词序号]
					break
			del 临时词库
			文件.close()
			if 操作成功与否:
				with open(安装目录+f'/数据库/1/{标签}.txt', 'w', encoding='utf-8') as 文件:
					文件.write('\n'.join(文件内容))
				for 临时命令 in os.listdir(安装目录+'/数据库/2'):
					# 这里使用NSS架构的第二层
					临时词库 = []
					with open(安装目录+'/数据库/2/'+临时命令, encoding='utf-8') as 临时文件:
						for 临时 in 临时文件.read().split('\n'):
							if f'[1, \'{标签}\', \'{长输入}\']' not in 临时:
								临时词库.append(临时)
					with open(安装目录+f'/数据库/2/'+临时命令, 'w', encoding='utf-8') as 文件:
						文件.write('\n'.join(临时词库))
				print('【渐得如意】删除成功！')
			else:
				print('【渐得如意】该命令原先并不存在，或者不是这种类型。')
	except:
		print('【渐得如意】您的输入有误。')
		文件.close()
elif 删除生成规则:
	print('【渐得如意】请继续输入。')
	生成规则 = input()
	while not 删除状态空间:
		生成规则 += '\n'
		生成规则 += input('')
		删除状态空间 = 生成规则.endswith('\n”')
	try:
		长输入 = 执行(长输入[:-8], 第一层感受器)[0][0]
		标签 = 长输入[1]
		长输入 = 长输入[2]
		with open(安装目录+f'/数据库/1/{标签}.txt', 'r', encoding='utf-8') as 文件:
			临时命令库 = list(map(lambda x: x.split('\t'), 文件.read().split('\n')))
			for 等价类序号, 等价类 in enumerate(临时命令库):
				if 等价类[0]==长输入:
					等价类.remove(生成规则[:-2])
					break
		文件.close()
		with open(安装目录+f'/数据库/1/{标签}.txt', 'w', encoding='utf-8') as 文件:
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

del 操作成功与否

for 文件 in os.listdir(安装目录+'/数据库/2'):
	if os.path.getsize(安装目录+'/数据库/2/'+文件)==0:
		os.remove(安装目录+'/数据库/2/'+文件)
for 文件 in os.listdir(安装目录+'/数据库/1'):
	if os.path.getsize(安装目录+'/数据库/1/'+文件)==0:
		os.remove(安装目录+'/数据库/1/'+文件)
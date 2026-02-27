try:
	with open(安装目录+f'/数据库/本地数据/程序地址.txt', 'r', encoding='utf-8') as 文件:
		临时数据库 = list(map(lambda x: x.split('\t'), 文件.read().split('\n')))
		for 临时程序 in 临时数据库:
			assert 临时程序[0]!=第三层数据[0]
	文件.close()
	print('【渐得如意】请继续输入。')
	长输入 = input()
	while not 长输入.endswith('\n”'):
		长输入 += '\n'
		长输入 += input()
	assert list(长输入).count('\n')==1
	临时数据库.append([第三层数据[0], 长输入[:-2]])
	with open(安装目录+f'/数据库/本地数据/程序地址.txt', 'w', encoding='utf-8') as 文件:
		文件.write('\n'.join(list(map(lambda x: '\t'.join(x), 临时数据库))))
	print('【渐得如意】添加成功！')
except:
	print('【渐得如意】您的输入有误。')
文件.close()

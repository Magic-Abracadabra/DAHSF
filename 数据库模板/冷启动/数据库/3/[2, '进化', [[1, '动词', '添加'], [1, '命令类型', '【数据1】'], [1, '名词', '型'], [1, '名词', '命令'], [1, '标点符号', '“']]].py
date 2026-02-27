print('【渐得如意】请继续输入。')
长输入 = input('')
while not 长输入.endswith('\n”'):
	长输入 += '\n'
	长输入 += input('')
try:
	assert list(长输入).count('\n')==1
	with open(安装目录+f'/数据库/2/{第三层数据[0]}.txt', 'a', encoding='utf-8') as 文件:
		长输入= 执行(长输入[:-2], 第一层感受器)[0]
		计数数据 = dict(zip(map(lambda x: '计数_'+x, 数据类型),[0]*len(数据类型)))
		for _ in 长输入:
			if _[1] in 数据类型:
				计数数据['计数_'+_[1]] += 1
				_[2] = f"【数据{计数数据['计数_'+_[1]]}】"
		文件.write('\n'+str(长输入))
		print('【渐得如意】添加成功！')
		open(f'{安装目录}/数据库/3/{[2, 第三层数据[0], 长输入]}.txt', 'a').close()
		os.system(f'start notepad {安装目录}/数据库/3/{[2, 第三层数据[0], 长输入]}.py')
except:
	print('【渐得如意】您的输入格式有误。')
文件.close()
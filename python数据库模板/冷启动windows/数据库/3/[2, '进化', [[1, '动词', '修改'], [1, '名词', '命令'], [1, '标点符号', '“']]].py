print('【渐得如意】请继续输入。')
长输入 = input('')
while not 长输入.endswith('\n”'):
	长输入 += '\n'
	长输入 += input('')
try:
	assert list(长输入).count('\n')==1
	长输入 = 执行(长输入[:-2], 第一层感受器)[0]
	计数数据 = dict(zip(map(lambda x: '计数_'+x, 数据类型),[0]*len(数据类型)))
	for _ in 长输入:
		if _[1] in 数据类型:
			计数数据['计数_'+_[1]] += 1
			_[2] = f"【数据{计数数据['计数_'+_[1]]}】"
	长输入 = NSS.W0(长输入)
	assert os.path.exists(f'{安装目录}/数据库/3/{[2, NSS.get_tag(长输入), 长输入]}.py')
	os.system(f'start notepad {安装目录}/数据库/3/{[2, NSS.get_tag(长输入), 长输入]}.py')
except:
	print('【渐得如意】您的输入的不是命令。')
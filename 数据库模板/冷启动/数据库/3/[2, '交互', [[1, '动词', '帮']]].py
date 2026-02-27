全部命令 = os.listdir(f'{安装目录}/数据库/3')
全部命令 = list(map(lambda x: eval(x[:-3])[1:], 全部命令))
alert('       您好，我叫“渐得如意”，是一个接近于使用自然语言进行自动化办公的中文编程平台。我会逐渐学习您的用语习惯。当我掌握它们后，我会命令这台计算机快速、可靠地执行您的指令。您也可以主动编辑我的数据库，这样您就可以在我的帮助下完全设计这台电脑为您执行命令的方式。\n       本平台有多种模式。您可以直接在刚才的这个平台与我对话，可以事先编辑好“.秘籍”和“.机关”的中文脚本文件然后用我打开运行（比如设置为默认的打开方式）。', '渐得如意使用指南')
if confirm('请问您是否需要我向您展示本平台的全部最简命令与所有词语类别？', '渐得如意')=='OK':
	with open(f'{安装目录}/帮助.html', 'w', encoding='utf-8') as 文件:
		文件.write('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
	<meta charset="UTF-8">
	<title>全部最简命令</title>
</head>
<body>
''')
		旧的标题 = ''
		标题与内容 = []
		内容 = []
		for 预设命令 in 全部命令:
			if 旧的标题!=预设命令[0]:
				标题与内容.append(旧的标题)
				标题与内容.append(内容)
				旧的标题 = 预设命令[0]
				内容 = []
			内容.append('')
			for token in 预设命令[1]:
				if token[1] in 数据类型:
					内容[-1] += f'（{token[1]}）'
				else:
					内容[-1] += token[2]
		标题与内容.append(内容)
		for 标题或内容 in 标题与内容[2:]:
			if type(标题或内容)==str:
				文件.write(f'\t<h1>{标题或内容}</h1>\n')
			elif type(标题或内容)==list:
				文件.write(f'\t<p>{"，".join(标题或内容)}</p>\n')
		文件.write('</body>\n</html>')
	文件.close()
	os.system(f'start "" "{安装目录}/帮助.html"')
	sleep(5)
	os.remove(f"{安装目录}/帮助.html")
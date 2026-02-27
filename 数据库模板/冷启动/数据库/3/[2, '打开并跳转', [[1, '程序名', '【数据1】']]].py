站在 = os.path.abspath('')
if '\\' in 本地数据['程序地址'][第三层数据[0]]:
	os.chdir('\\'.join(本地数据['程序地址'][第三层数据[0]].split('\\')[:-1]))
os.system('start "" "'+本地数据['程序地址'][第三层数据[0]]+'"')
os.chdir(站在)
del 站在
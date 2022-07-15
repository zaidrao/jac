import platform
import os
os.system('termux-setup-storage')
try:os.system('touch .prox.txt')
except:pass
try:os.system('touch .proxy.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	print('32bit not supported')
elif 'aarch' in arc:
	__import__("Filp").ninex()
else:
	exit(f' Unknow device machine {arc}')

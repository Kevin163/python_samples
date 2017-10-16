# batchChangeFileLine.py
# Created:2017-10-13 17:28:40

'''
批量修改指定目录文件的换行符
调用示例：
将d:\temp目录下的所有文件的换行符由\n替换为\r\n
py batchChangeFileLine d:\temp
将d:\temp目录下的所有文件的换行符由\r\n替换为\n
py batchChangeFileLine d:\temp 1
'''

__author__ = "Kevin"
__version__ = "1.0"

import os
import sys

def batchChangeFileLine(workDir,win2unix=False):
	files = os.listdir(workDir)
	oldStr = b"\r"
	newStr = b""
	if not win2unix:
		oldStr = b"\n"
		newStr = b"\r\n"
	data = b''
	for f in files:		
		fold = os.path.join(workDir,f)
		fnew = os.path.join(workDir,"$"+f)
		if os.path.isfile(fold):
			try:
				print("开始处理文件:{0}".format(fold))
				with open(fold,'rb+') as fr:
					with open(fnew,'ba+') as fw:
						while(True):
							data = fr.read(200)
							newData = data.replace(oldStr,newStr)
							fw.write(newData)
							if len(data) < 200:
								break
				os.remove(fold)
				os.rename(fnew,fold)
				print("结束处理文件:{0}".format(fold))
			except IOError as e:
				print("处理文件{0}失败，原因：{1}".format(fold,e))

def main():
	workDir = ""
	win2unix = False
	argLen = len(sys.argv)
	if(argLen > 1):
		workDir = sys.argv[1]
	if(argLen > 2):
		win2unix = int(sys.argv[2]) == 1
	if(workDir != ""): 
		batchChangeFileLine(workDir,win2unix)
	else:
		print(r'''
批量修改指定目录文件的换行符
调用示例：
将d:\temp目录下的所有文件的换行符由\n替换为\r\n
py batchChangeFileLine d:\temp
将d:\temp目录下的所有文件的换行符由\r\n替换为\n
py batchChangeFileLine d:\temp 1
''')

if __name__ == '__main__':
	main()
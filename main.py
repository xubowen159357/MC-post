import os
import sys
import OPTION
import os.path as op
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning
import pyperclip
from alive_progress import alive_bar
import time
import random
import logging
print('''From xu.bw.
Use logging.''')
_________=False
__________=False
______ = None
_____ = './log/late-log.log'
class log:
	def save():
		print('These log will seve in "./log/late-log.log"')
		if not os.path.exists('./log'):
			os.system('md .\log')
		if os.path.exists(_____):
			__ = open(_____, 'r')
			_ = __.readlines()
			______ = _[0]
			__.close()
			________ = ['：' if i == ':' else i for i in ______]
			________.pop(________.index('\n'))
			_______ = ''
			for i in ________:
				_______ += i
			os.system('ren ".\log\late-log.log" "'+_______+'.log"')
		if not os.path.exists(_____):
			__ = open(_____, 'w')
			___ = time.asctime(time.localtime())
			____ = [___, '\n']
			__.writelines(____)
			__.close()
		logging.basicConfig(filename=_____, level=logging.NOTSET, filemode='a',format='%(asctime)s : %(levelname)s level:%(levelno)s Log:%(message)s', datefmt='%m/%d/%Y %I:%M:%S world.tiem=%p')
	def _DELOLDLOG(*Any):
		print('不用管XXX\log\late-log.log因为他是当前的日志!')
		time.sleep(0.5)
		os.system('DEL /Q /S ".\log\*.*"')
	def DEBUGANDHAIGHSHOW(bool_int:int)->bool:
		global _________
		_________=bool(bool_int)
	def INFOANDHAIGHSHOW(bool_int:int)->bool:
		global __________
		__________=bool(bool_int)
	def debug(orj: str, *args, **kwargs):
		logging.debug(orj, *args, **kwargs)
		if _________:
			print('\033[32mDEBUG:root:\033[0m%s'%orj)
	def info(orj: str, *args, **kwargs):
		logging.info(orj, *args, **kwargs)
		if __________ or _________:
			print('\033[34mINFO:root:\033[0m%s'%orj)
	def error(orj: str, *args, **kwargs):
		logging.error(orj, *args, **kwargs)
	def critical(orj: str, *args, **kwargs):
		logging.critical(orj, *args, **kwargs)
	def HELP():
		print('''%_ _DELOLDLOG_%._DELOLDLOG(*any) the *%v%* is a None *%v%* you can input any things!
%_DEBUGANDHAIGHSHOW_%.DEBUGANDHAIGHSHOW(int_or_bool) the *%v%* is a bool or int you must input a int or True or False! and it be True or int>1 the DEBUG AND HAIGH WILL SHOW!
%_INFOANDHAIGHSHOW_%.INFOANDHAIGHSHOW like DEBUGANDHAIGHSHOW but it will olny show INFO AND HAIGH
%_debug_%.debug will show debug log and put in the log txt!
%_info_%.like debug but will show info log!
%_error_%.like debug and info but it def. show a error log!
%_critical_%.like error and than but it is very dangerous of exe!
%_seve_%.recording log''')
	def help(self):
		self.HELP()
	def 帮助(self):
		self.help()
print('\033[34mfrom Xu Bowen')
log.debug('init... complete!')
log.info('into complete!')
print('\033[34mResource check...\033[33m')
log.debug('debug is not open... DEBUG is stop.')
log.info('Resource check is start.')
if2=[]
file=open("./time_things.out","w")
to_test_lset=['./__mine_icon-32x32-__','./__mine_icon-16x16-__','world_post.map.post','world_post.map.name','./Opti','./Opti/option.txt','./Opti/log.save.txt','PUS']
with alive_bar(len(to_test_lset)) as bar:
	for i in to_test_lset:
		if i =='world_post.map.name':
			print('\r\033[32m')
		if1=op.exists(i)
		if if1:
			if2+='t'
		else:
			if2+='f'
		bar()
		time.sleep(random.randint(0,1)/10)
if if2[0]=='f':
	log.critical('Failed to find storage table "__mine_icon-32x32-__"')
	print('\033[1;31mFailed to find storage table "__mine_icon-32x32-__"')
	print('\033[1;31m⚠︎ __Catastrophic error!')
	print('\033[1;31mCannot continue!\033[0m')
	sys.exit(1)
if if2[1]=='f':
	log.critical('Failed to find storage table "__mine_icon-16x16-__"')
	print('\033[1;31mFailed to find storage table "__mine_icon-16x16-__"')
	print('\033[1;31m⚠︎ __Catastrophic error!')
	print('\033[1;31mCannot continue!\033[0m')
	os._exit(1)
if if2[3]=='f':
	log.error('Failed to find storage table "world_ Post.map.name"')
	os.system('DEL .\world_post.map.name')
	os.system('DEL .\world_post.map.post')
	print('\033[33mFailed to find storage table "world_ Post.map.name", creating now...')
	file=open('world_post.map.name','w')
	file=open('world_post.map.post','w')
	log.info('Repair complete!')
	print('\033[32mcomplete.')
if if2[2]=='f':
	log.error('Failed to find storage table "world_post.map.post"')
	os.system('DEL .\world_post.map.name')
	os.system('DEL .\world_post.map.post')
	print('\033[33mFailed to find storage table "world_post.map.post", creating now...')
	file=open('world_post.map.post','w')
	file=open('world_post.map.name','w')
if if2[4]=='f':
	log.error('Failed to find storage table "Opti", creating now...')
	os.system('md .\Opti')
	file=open('.\Opti\option.txt','w')
	file.write('''option.type=TRUE
Log.SHW_D=FALSE
Log.SHW_I=TRUE
USE_PUS=FALSE''')
	file=open('./Opti/log.save.txt','w')
	file.write('''log.seve.type=TRUE
Log.seve=TRUE''')
if if2[5]=='f' and if2[4]=='t':
	log.error('Failed to find storage table ".\Opti\option.txt", creating now...')
	file=open('.\Opti\option.txt','w')
	file.write('''option.type=TRUE
Log.SHW_D=FALSE
Log.SHW_I=TRUE
USE_PUS=FALSE''')
if if2[6]=='f' and if2[4]=='t':
	log.error('Failed to find storage table "./Opti/log.save.txt", creating now...')
	file=open('./Opti/log.save.txt','w')
	file.write('''log.seve.type=TRUE
Log.seve=TRUE''')
if if2[7]=='f':
	log.error('Failed to find storage table "./PUS", creating now...')
	os.system('md .\PUS')
log.info('Repair complete!')
print('\033[32mcomplete.')
file=open('./Opti/log.save.txt','r')
dksakfls=OPTION.main_log(file.readlines())
if dksakfls=='1':
	log.save()
file=open('.\Opti\option.txt','r')
dksakfls=OPTION.main_opti(file.readlines())
if dksakfls=='SD':
	log.DEBUGANDHAIGHSHOW(1)
elif dksakfls=='SI':
	log.INFOANDHAIGHSHOW(1)
log.info('Resource check is stop.')
print('\033[34mLoading...\033[33m')
log.info('Loading start.')
to_test_lset=range(100)
with alive_bar(len(to_test_lset)) as bar:
	for i in to_test_lset:
		if i == 99:
			print('\r\033[32m')
		bar()
		time.sleep(random.randint(1,2)/500)
log.info('Loading is stop.')
log.info('Resource check is stop.')
print('\033[34mPus loading...\033[33m')
log.info('Pus loading start.')
to_test_lset=range(100)
with alive_bar(len(to_test_lset)) as bar:
	for i in to_test_lset:
		if i == 99:
			print('\r\033[32m')
		bar()
log.info('Pus loading is stop.')
log.info('Run now!')
file.close()
__ico32x32__='./__mine_icon-32x32-__'
__ico16x16__='./__mine_icon-16x16-__'
ico=''
mine = tk.Tk()
mine.title('Minecraft coordinate recorder')
mine.geometry('1000x600')
window_size=str(mine.winfo_screenwidth())+'x'+str(mine.winfo_screenheight())
if window_size=='1920x1080':
	mine.tk.call('wm', 'iconphoto', mine._w, tk.PhotoImage(file=__ico32x32__))
	ico='32x32'
else:
	mine.tk.call('wm', 'iconphoto', mine._w, tk.PhotoImage(file=__ico16x16__))
	ico='16x16'
log.info('Your resolving power is '+window_size+',select icon is '+ico+' pixel.')
print('\033[33mYour resolving power is %s,select icon is %s pixel.\033[0m'%(window_size,ico))
var = tk.StringVar()
l = tk.Label(mine, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
l.pack()
list = []
list_for = []
on_hit = False
def input_x_y_z():
	log.info('Mark pos.')
	def ok():
		name=mc.get()
		log.info('get name end.')
		xyz=mc1.get()
		log.info('get pos end.')
		if ' ' in xyz:
			list_for.append(name+': '+xyz)
			list.append(xyz)
			lb.insert('end', name+': '+xyz)
			var.set('Marked!')
			log.info('Mark pos ok.')
		else:
			tk.Message(showwarning('Wrong','Wrong coordinates!'))
			log.info('Pos is wrong!')
	mc = tk.Spinbox(mine, values= ("Outline"))
	mc.pack()
	mc1 = tk.Spinbox(mine, values= ("Coordinate"))
	mc1.pack()
	b = tk.Button(mine, text='Record coordinates', font=('Arial', 12), width=10, height=1, command=ok)
	b.pack()
def ctrl_and_c():
	log.info('start copy.def')
	value = lb.get(lb.curselection())
	for i in list_for:
		if i == value:
			pyperclip.copy(list[list_for.index(i)])
			tk.Message(showinfo('提示','已复制!'))
			log.info('copy done.')
			break
def in_end():
	log.info('Start save')
	file=open('world_post.map.name','w')
	for i in list_for:
		file.write(i)
		file.write('\r')
		file.close()
	log.info('Save world_post.map.name')
	file=open('world_post.map.post','w')
	for i in list:
		file.write(i)
		file.write('\r')
		file.close()
	log.info('Save world_post.map.post')
def clean():
	value = lb.get(lb.curselection())
	for i in list_for:
		if i == value:
			del list[list_for.index(i)]
			lb.delete(list_for.index(i))
			del list_for[list_for.index(i)]
			log.info('DEL '+i)
			var.set('will del:'+i)
			break
def del_all():
	log.info('DEL ALL')
	os.system('DEL .\world_post.map.name')
	log.info('DEL world_post.map.name')
	os.system('DEL .\world_post.map.post')
	log.info('DEL world_post.map.post')
var2 = tk.StringVar()
var2.set(())
lb=tk.Listbox(mine, listvariable=var2,width=60)
lb.pack()
file=open('world_post.map.name')
k=file.readlines()
for i in k:
	lb.insert('end',i)
	list_for.append(i)
file=open('world_post.map.post')
n=file.readlines()
for i in n:
	list.append(i)
file.close()
input_x_y_z()
w = tk.Button(mine, text='copy', font=('Arial', 12), width=10, height=1, command=ctrl_and_c)
w.pack()
end = tk.Button(mine, text='save', font=('Arial', 12), width=10, height=1, command=in_end)
end.pack()
end = tk.Button(mine, text='clean', font=('Arial', 12), width=10, height=1, command=clean)
end.pack()
end = tk.Button(mine, text='del_pos', font=('Arial', 12), width=10, height=1, command=del_all)
end.pack()
end = tk.Button(mine, text='del_log', font=('Arial', 12), width=10, height=1, command=log._DELOLDLOG)
end.pack()
mine.mainloop()

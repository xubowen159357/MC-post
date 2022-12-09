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
import log

main = tk.Tk()
__=True
_=True
class Tk_menu:
	def __init__(self) -> None:
		self.mebubar = tk.Menu(main)
		self.meun_lsit = tk.Menu(main, tearoff=1)
	def list_abb(self,abb_th:str,cmd:function) -> None:
		self.meun_lsit.add_command(label=abb_th,command=cmd)
		self.meun_lsit.add_separator()
	def Num_meun(self,Name,meun={},cmd={}):
		self.mebubar.add_command(label=Name,meun=meun,command=cmd)

def save():
	log.save()
if os.path.exists('./Opti/log.save.txt'):
	file=open('./Opti/log.save.txt','r')
	if OPTION.main_log(file.readlines())=='1':
		save()
		_=False
if os.path.exists('./Opti/option.txt'):
	__=False
	file=open('.\Opti\option.txt','r')
	if OPTION.main_opti(file.readlines())=='SD':
		log.DEBUGANDHAIGHSHOW(1)
	elif OPTION.main_opti(file.readlines())=='SI':
		log.INFOANDHAIGHSHOW(1)
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
if OPTION.main_log(file.readlines())=='1' and _:
	save()
file=open('.\Opti\option.txt','r')
dksakfls=OPTION.main_opti(file.readlines())
if dksakfls=='SD' and __:
	log.DEBUGANDHAIGHSHOW(1)
elif dksakfls=='SI' and __:
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
main.title('Minecraft coordinate recorder')
main.geometry('1000x600')
window_size=str(main.winfo_screenwidth())+'x'+str(main.winfo_screenheight())
if window_size=='1920x1080':
	main.tk.call('wm', 'iconphoto', main._w, tk.PhotoImage(file=__ico32x32__))
	ico='32x32'
else:
	main.tk.call('wm', 'iconphoto', main._w, tk.PhotoImage(file=__ico16x16__))
	ico='16x16'
log.info('Your resolving power is '+window_size+',select icon is '+ico+' pixel.')
print('\033[33mYour resolving power is %s,select icon is %s pixel.\033[0m'%(window_size,ico))
var = tk.StringVar()
l = tk.Label(main, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
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
	mc = tk.Spinbox(main, values= ("Outline"))
	mc.pack()
	mc1 = tk.Spinbox(main, values= ("Coordinate"))
	mc1.pack()
	b = tk.Button(main, text='Record coordinates', font=('Arial', 12), width=10, height=1, command=ok)
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
if __name__ == '__main__':
	try:
		var2 = tk.StringVar()
		var2.set(())
		lb=tk.Listbox(main, listvariable=var2,width=60)
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
		w = tk.Button(main, text='copy', font=('Arial', 12), width=10, height=1, command=ctrl_and_c)
		w.pack()
		end = tk.Button(main, text='save', font=('Arial', 12), width=10, height=1, command=in_end)
		end.pack()
		end = tk.Button(main, text='clean', font=('Arial', 12), width=10, height=1, command=clean)
		end.pack()
		end = tk.Button(main, text='del_pos', font=('Arial', 12), width=10, height=1, command=del_all)
		end.pack()
		end = tk.Button(main, text='del_log', font=('Arial', 12), width=10, height=1, command=log._DELOLDLOG)
		end.pack()
		main.mainloop()
	except:
		log.critical('The app out notdef!')

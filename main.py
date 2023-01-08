import os
import sys
import log
import OPTION
import os.path as op
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning
import pyperclip
import get_info as gi

main = tk.Tk()
__=True
_=True
option=OPTION
def save():
	log.save()
if os.path.exists('./Opti/log.save.txt'):
	file=open('./Opti/log.save.txt','r')
	if option.main_log(file.readlines())=='1':
		save()
		_=False
if os.path.exists('./Opti/option.txt'):
	__=False
	file=open('.\Opti\option.txt','r')
	if option.main_opti(file.readlines())=='SD':
		log.DEBUGANDHAIGHSHOW(1)
	elif option.main_opti(file.readlines())=='SI':
		log.INFOANDHAIGHSHOW(1)
print('\033[34mfrom Xu Bowen')
log.debug('init... complete!')
log.info('into complete!')
print('\033[34mResource check...\033[33m')
log.debug('debug is not open... DEBUG is stop.')
log.info('Resource check is start.')
if2=[]
file=open("./time_things.out","w")
to_test_lset=['./__mine_icon-32x32-__','./__mine_icon-16x16-__','data\world_post.map-post','data\world_post.map-name','./Opti','./Opti/option.txt','./Opti/log.save.txt','data']
for i in to_test_lset:
	if i =='data\world_post.map-name':
		print('\033[32m')
	if1=op.exists(i)
	if if1:
		if2+='t'
	else:
		if2+='f'
try:
	if len(open('data\world_post.map-name').readlines()) != len(open('data\world_post.map-post').readlines()):
		print('\033[1;31m"data\world_post.map-name"or"data\world_post.map-post" is damaged!')
		print('\033[1;31mRe build!\033[0m')
		file=open('data\world_post.map-post','w')
		file=open('data\world_post.map-name','w')
except:
    pass
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
	log.error('Failed to find storage table "world_ Post.map-name"')
	os.system('DEL .\data\world_post.map-name')
	os.system('DEL .\data\world_post.map-post')
	print('\033[33mFailed to find storage table "world_ Post.map-name", creating now...')
	file=open('data\world_post.map-name','w')
	file=open('data\world_post.map-post','w')
	log.info('Repair complete!')
	print('\033[32mcomplete.')
if if2[2]=='f':
	log.error('Failed to find storage table "data\world_post.map-post"')
	os.system('DEL .\data\world_post.map-name')
	os.system('DEL .\data\world_post.map-post')
	print('\033[33mFailed to find storage table "data\world_post.map-post", creating now...')
	file=open('data\world_post.map-post','w')
	file=open('data\world_post.map-name','w')
if if2[4]=='f':
	log.error('Failed to find storage table "Opti", creating now...')
	os.system('md .\Opti')
	file=open('.\Opti\option.txt','w')
	file.write('''option.type=TRUE
Log.SHW_D=FALSE
Log.SHW_I=TRUE
USE_data=FALSE''')
	file=open('./Opti/log.save.txt','w')
	file.write('''log.seve.type=TRUE
Log.seve=TRUE''')
if if2[5]=='f' and if2[4]=='t':
	log.error('Failed to find storage table ".\Opti\option.txt", creating now...')
	file=open('.\Opti\option.txt','w')
	file.write('''option.type=TRUE
Log.SHW_D=FALSE
Log.SHW_I=TRUE
USE_data=FALSE''')
if if2[6]=='f' and if2[4]=='t':
	log.error('Failed to find storage table "./Opti/log.save.txt", creating now...')
	file=open('./Opti/log.save.txt','w')
	file.write('''log.seve.type=TRUE
Log.seve=TRUE''')
if if2[7]=='f':
	log.error('Failed to find storage table "./data", creating now...')
	os.system('md .\data')
log.info('Repair complete!')
print('\033[32mcomplete.')
file=open('./Opti/log.save.txt','r')
if option.main_log(file.readlines())=='1' and _:
	save()
file=open('.\Opti\option.txt','r')
dksakfls=option.main_opti(file.readlines())
if dksakfls=='SD' and __:
	log.DEBUGANDHAIGHSHOW(1)
elif dksakfls=='SI' and __:
	log.INFOANDHAIGHSHOW(1)
log.info('Resource check is stop.')
print('\033[34mLoading...\033[33m')
log.info('Loading start.')
log.info('Loading is stop.')
log.info('Resource check is stop.')
print('\033[34mPus loading...\033[33m')
log.info('Pus loading start.')
print('\033[32m')
log.info('Pus loading is stop.')
log.info('Run now!')
file.close()
__ico32x32__='./__mine_icon-32x32-__'
__ico16x16__='./__mine_icon-16x16-__'
ico=''
main.title('Minecraft 坐标记录仪')
main.geometry('1000x600')
window_size=str(main.winfo_screenwidth())+'x'+str(main.winfo_screenheight())
if window_size=='1920x1080':
	main.tk.call('wm', 'iconphoto', main._w, tk.PhotoImage(file=__ico32x32__)) # type: ignore
	ico='32x32'
else:
	main.tk.call('wm', 'iconphoto', main._w, tk.PhotoImage(file=__ico16x16__)) # type: ignore
	ico='16x16'
log.info('Your resolving power is '+window_size+',select icon is '+ico+' pixel.')
print('\033[33mYour resolving power is %s,select icon is %s pixel.\033[0m'%(window_size,ico))
var = tk.StringVar()
l = tk.Label(main, textvariable=var, bg='black', fg='white', font=('Arial', 12), width=110, height=2)
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
			var.set('已标记！')
			log.info('Mark pos ok.')
		else:
			showwarning('错误','错误的坐标!')
			log.info('Pos is wrong!')
	mc = tk.Spinbox(main, values=("标记")) # type: ignore
	mc.pack()
	mc1 = tk.Spinbox(main, values=("坐标")) # type: ignore
	mc1.pack()
	b = tk.Button(main, text='标记坐标', font=('Arial', 12), width=10, height=1, command=ok)
	b.pack()
def ctrl_and_c():
	log.info('start copy.def')
	value = lb.get(lb.curselection())
	for i in list_for:
		if i == value:
			pyperclip.copy(list[list_for.index(i)])
			showinfo('提示','已复制!')
			log.info('copy done.')
			break
def in_end():
	log.info('Start save')
	file=open('data\world_post.map-name','w')
	for i in list_for:
		file.write(i)
		file.write('\r')
		file.close()
	log.info('Save data\world_post.map-name')
	file=open('data\world_post.map-post','w')
	for i in list:
		file.write(i)
		file.write('\r')
		file.close()
	log.info('Save data\world_post.map-post')
def clean():
	value = lb.get(lb.curselection())
	for i in list_for:
		if i == value:
			del list[list_for.index(i)]
			lb.delete(list_for.index(i))
			del list_for[list_for.index(i)]
			log.info('DEL '+i)
			var.set('将会清除的标记："'+i.replace(':','坐标：')+'"')
			break
def del_all():
	log.info('DEL ALL')
	os.system('DEL .\data\world_post.map-name')
	log.info('DEL data\world_post.map-name')
	os.system('DEL .\data\world_post.map-post')
	log.info('DEL data\world_post.map-post')
def _lb1():
	gi1=gi.get_window(0)
	buit1=tk.Toplevel()
	text1=f'''About you os(computer or system)
	{gi1.processor}
	{gi1.pyversion}
	{gi1.os}
			{gi1.getos('name')},{gi.pf.architecture()[0]}
name:{gi.pf.node()}
坐标记录仪版本：1.2
主窗口大小：{main.winfo_width()}*{main.winfo_height()+20}'''
	buit1.geometry('550x200')
	buit1.tk.call('wm', 'iconphoto', buit1._w, tk.PhotoImage(file=__ico16x16__))
	lb1 = tk.Label(buit1, text=text1,# 设置文本内容
				 width=60,# 设置label的宽度：30
				 height=10,# 设置label的高度：10
				 justify='left',# 设置文本对齐方式：左对齐
				 anchor='nw',# 设置文本在label的方位：西北方位
				 font=('微软雅黑',10),# 设置字体：微软雅黑，字号：18
				 fg='black',# 设置前景色：白色
				 padx=0,# 设置x方向内边距：20
				 pady=0)# 设置y方向内边距：10
	lb1.pack()
	buit1.mainloop()
class menu:
	def __init__(self) -> None:
		self.menu=tk.Menu(main,tearoff=0)
		self.menu.add_command(label='help',command=self.help)
		self.menu.add_command(label='About os',command=_lb1)
	def help(self):
		showinfo('Hlep','version 1.2')
m=menu()
if __name__ == '__main__':
	try:
		mebubar=tk.Menu(main)
		mebubar.add_command(label='quit|退出',command=main.quit)
		mebubar.add_cascade(label='help|帮助',menu=m.menu)
		var2 = tk.StringVar()
		var2.set((''))
		lb=tk.Listbox(main, listvariable=var2,width=143)
		lb.pack()
		file=open('data\world_post.map-name')
		k=file.readlines()
		for i in k:
			lb.insert('end',i)
			list_for.append(i)
		file=open('data\world_post.map-post')
		n=file.readlines()
		for i in n:
			list.append(i)
		file.close()
		input_x_y_z()
		w = tk.Button(main, text='复制', font=('Arial', 12), width=10, height=1, command=ctrl_and_c)
		w.pack()
		end = tk.Button(main, text='保存', font=('Arial', 12), width=10, height=1, command=in_end)
		end.pack()
		end = tk.Button(main, text='清除标记', font=('Arial', 12), width=10, height=1, command=clean)
		end.pack()
		end = tk.Button(main, text='删除保存文件', font=('Arial', 12), width=10, height=1, command=del_all)
		end.pack()
		end = tk.Button(main, text='删除日志', font=('Arial', 12), width=10, height=1, command=log._DELOLDLOG)
		end.pack()
		main.config(menu=mebubar)
		main.mainloop()
	except:
		log.critical('The app out notdef!')

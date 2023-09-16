verion = '1.10'
try:
	import os
	import os.path as op
	import sys
	import tkinter as tk
	from tkinter.messagebox import showinfo, showwarning
	import pyperclip
	from ping3 import ping
	import get_info as gi
	import log
	import OPTION
	from mcpi import minecraft as mc
except BaseException as e:
	file=open('#FATAL-logging.log','w',encoding='utf-8')
	file.write(str(e)+'\nNot find the MODULE. Most of these errors come from insecure sources, confirming that you are using official compilations.\
\n无法找到模块。大部分出现这种错误来自于不安全的来源，确认使用的是官方编译。')
	file.close()
	exit()

try:
	main = tk.Tk()
	main.withdraw()
	showwarning('info','本程序完全开源免费：https://github.com/xubowen159357/mcpost \n本产品不能用于商业用途！')
	main.deiconify()
	__=True
	_=True
	option=OPTION
	def gethost(host):
		ttl=os.popen('ping -n 1 -w 1 %s'%host).read()
		if '的 Ping 统计信息' in ttl:return 'online'
		else:return 'offline'
	def save():
		log.save()
	if os.path.exists('./Opti/log.save.txt'):
		file=open('./Opti/log.save.txt','r')
		if option.main_log(file.readlines())=='1':
			save()
			_=False
	if os.path.exists('./Opti/option.txt'):
		__=False
		file=open('Opti\option.txt','r').readlines()
		if option.main_opti(file)=='SD':
			log.DEBUGANDHAIGHSHOW(1)
		elif option.main_opti(file)=='SI':
			log.INFOANDHAIGHSHOW(1)
		timeout=option.Test_timeout(file)
	print('\033[34mfrom Xu Bowen')
	log.debug('init... complete!')
	log.info('into complete!')
	print('\033[34mResource check..033[33m')
	log.debug('debug is not open... DEBUG is stop.')
	log.info('Resource check is start.')
	if2=[]
	file=open("./time_things.out","w")
	to_test_lset=['data/__mine_icon__','data','data\world_post.map-post','data\world_post.map-name'\
					,'./Opti','./Opti/option.txt', './Opti/log.save.txt','data']
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
		log.critical('Failed to find storage table "data\__mine_icon__"')
		print('\033[1;31mFailed to find storage table "data\__mine_icon__"')
		print('\033[1;31m⚠︎ __Catastrophic error!')
		print('\033[1;31mCannot continue!\033[0m')
		sys.exit(1)
	if if2[3]=='f':
		log.error('Failed to find storage table "world_ Post.map-name"')
		os.system('DEL data\world_post.map-name')
		os.system('DEL data\world_post.map-post')
		print('\033[33mFailed to find storage table "world_ Post.map-name", creating now...')
		file=open('data\world_post.map-name','w')
		file=open('data\world_post.map-post','w')
		log.info('Repair complete!')
		print('\033[32mcomplete.')
	if if2[2]=='f':
		log.error('Failed to find storage table "data\world_post.map-post"')
		os.system('DEL data\world_post.map-name')
		os.system('DEL data\world_post.map-post')
		print('\033[33mFailed to find storage table "data\world_post.map-post", creating now...')
		file=open('data\world_post.map-post','w')
		file=open('data\world_post.map-name','w')
	if if2[4]=='f':
		log.error('Failed to find storage table "Opti", creating now...')
		os.system('md Opti')
		file=open('Opti\option.txt','w')
		file.write('''option.type=TRUE
Log.SHW_D=FALSE
Log.SHW_I=TRUE
USE_data=FALSE
Test-ip.timeout=0.5''')
		file=open('./Opti/log.save.txt','w')
		file.write('''log.seve.type=TRUE
Log.seve=TRUE''')
	if if2[5]=='f' and if2[4]=='t':
		log.error('Failed to find storage table "Opti\option.txt", creating now...')
		file=open('Opti\option.txt','w')
		file.write('''option.type=TRUE
Log.SHW_D=FALSE
Log.SHW_I=TRUE
USE_data=FALSE
Test-ip.timeout=0.5''')
	if if2[6]=='f' and if2[4]=='t':
		log.error('Failed to find storage table "./Opti/log.save.txt", creating now...')
		file=open('./Opti/log.save.txt','w')
		file.write('''log.seve.type=TRUE
Log.seve=TRUE''')
	if if2[7]=='f':
		log.critical('Failed to find storage table "./data", stop.')
	log.info('Repair complete!')
	print('\033[32mcomplete.')
	if os.path.exists('./Opti/log.save.txt'):
		file=open('./Opti/log.save.txt','r')
		if option.main_log(file.readlines())=='1':
			save()
			_=False
	file.close()
	if os.path.exists('./Opti/option.txt'):
		__=False
		file=open('Opti\option.txt','r')
		ai=file.readlines()
		if option.main_opti(file.readlines())=='SD':
			log.DEBUGANDHAIGHSHOW(1)
		elif option.main_opti(file.readlines())=='SI':
			log.INFOANDHAIGHSHOW(1)
		timeout=option.Test_timeout(ai)
	file.close()
	def ping_host(ip):
		"""
		获取节点的延迟的作用\n
		__odj[0] the time_max
		:param node:
		:return:
		"""
		response=ping(ip,timeout=timeout)
		if response is not None:
			delay = int(response * 1000)
			return delay
		else:
			return 'time out'
	log.info('Resource check is stop.')
	print('\033[34mLoading..\033[33m')
	log.info('Loading start.')
	log.info('Loading is stop.')
	log.info('Resource check is stop.')
	print('\033[34mPus loading..\033[33m')
	log.info('Pus loading start.')
	print('\033[32m')
	log.info('Pus loading is stop.')
	log.info('Run now!')
	file.close()
	__ico__='data\__mine_icon__'
	main.title('Minecraft 坐标记录仪')
	main.geometry('1000x600')
	window_size=str(main.winfo_screenwidth())+'x'+str(main.winfo_screenheight())
	main.tk.call('wm', 'iconphoto', main._w, tk.PhotoImage(file=__ico__)) # type: ignore
	log.info('Your resolving power is '+window_size+',select icon is 128x128 pxel.')
	print('\033[33mYour resolving power is %s,select icon is %s pxel\033[0m'%(window_size,'128x128'))
	var = tk.StringVar()
	var.set('PS>')
	l = tk.Label(main, textvariable=var, bg='black', fg='white', font=('Arial', 12), width=60, height=2, padx=0)
	l.place(x=4,y=0)
	list = []
	list_for = []
	on_hit = False
	class Ai:
		def __init__(self) -> None:
			self.AI_save=False
			self.AI_c=False
			if os.path.exists('Opti\AI'):
				print('AI is open')
				opens=open('Opti\AI','r')
				self.AI_save_time=opens.read()
				opens.close()
				self.AI_save=True
		def setAi(self, Bool:bool):
			self.AI_save=Bool
			self.AI_c=True
	HC=Ai()
	def mcpi_():
		tk2=tk.Toplevel()
		tk2.minsize(400,400)
		tk2.title('Use mcpi')
		tk2.tk.call('wm', 'iconphoto', tk2._w, tk.PhotoImage(file=__ico__))
		showinfo('info','如要使用mcpi确保已安装raspberryjammod!')
		tk2.deiconify()
		GetIp=tk.Spinbox(tk2, values='ip')
		GetIp.pack(side='top')
		Getport=tk.Spinbox(tk2, values='port:int')
		Getport.pack()
		def Got():
			global post
			try:
				mc_sever_fand_error=[]
				mc_sever_fand_error+=str(GetIp.get())
				if mc_sever_fand_error.count('.')<2:
					showwarning('错误','ip错误')
					tk2.deiconify()
				else:
					mc_sever=mc.Minecraft.create(GetIp.get(),int(Getport.get()))
					x,y,z=mc_sever.player.getPos()
					list_for.append(x+y+z)
					list.append(x+' '+y+' '+z)
					lb.insert('end', x+' '+y+' '+z)
			except OSError as es:
				showwarning('错误','ip错误:%s'%es)
				tk2.deiconify()
			except:
				showwarning('错误','Num errer')
				tk2.deiconify()
			try:
				post=[x,y,z]
			except:pass
		Get=tk.Button(tk2, text='ok',command=Got)
		Get.pack()
		tk2.mainloop()
	def test():
		tk2=tk.Toplevel()
		tk2.title('Test ip')
		tk2.tk.call('wm', 'iconphoto', tk2._w, tk.PhotoImage(file=__ico__))
		tk2.minsize(400,400)
		Var = tk.StringVar()
		lboftry=tk.Label(tk2,width=20)
		GetIp=tk.Spinbox(tk2, values='ip')
		GetIp.pack(side='top')
		lb2=tk.Label(tk2,bg='black',fg='white',width=50,textvariable=Var)
		lb2.pack()
		lboftry.place(x=20)
		numIdx = 5
		aa33=tk.PhotoImage(file='data/png/33.png')
		aa32=tk.PhotoImage(file='data/png/32.png')
		aa31=tk.PhotoImage(file='data/png/31.png')
		aa30=tk.PhotoImage(file='data/png/30.png')
		aa29=tk.PhotoImage(file='data/png/29.png')
		aa34=tk.PhotoImage(file='data/png/34.png')
		frames = [tk.PhotoImage(file=(f'data/png/28-{i}.png')) for i in range(numIdx)]
		def Got():
			add=''
			ip=GetIp.get()
			cip=[]
			cip+=ip
			if cip.count('.')>0:
				print('start')
				if gethost(ip)=='online':
					a=ping_host(ip)
					if not a=='time out':add='ms'
				else:a='Error ip'
			else:a='Error ip'
			Var.set(str(a)+add)
			return a
		def update(idx,s,s2,fand,*tick_ms):
			string=None
			tick=91
			try:tick_ms[0]+1;string='int'
			except:string='str'
			frame = frames[idx]
			s+=1
			idx += 1
			if s==int(1000/tick):
				s=0
				s2+=1
			if s2==1:
				if string=='int' and tick_ms[0]<400:
					lboftry.configure(image=aa29)
				if string=='int' and tick_ms[0]<200:
					lboftry.configure(image=aa30)
				if string=='int' and tick_ms[0]<100:
					lboftry.configure(image=aa31)
				if string=='int' and tick_ms[0]<50:
					lboftry.configure(image=aa32)
				if string=='int' and tick_ms[0]<10:
					lboftry.configure(image=aa33)
				if string=='str':
					lboftry.configure(image=aa34)
				return
			else:
				lboftry.configure(image=frame)
			tk2.after(tick, update, idx%numIdx, s,s2,fand,tick_ms[0])
		def run():
			update(0, 0, 0,True,Got())
		b=tk.Button(tk2,text='test',command=run)
		b.pack()
		tk2.mainloop()
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
				var.set('PS>已标记！')
				log.info('Mark pos ok.')
			else:
				showwarning('错误','错误的坐标!')
				log.info('Pos is wrong!')
		mc = tk.Spinbox(main, values=("标记"))
		mc.place(x=550+100,y=0)
		mc1 = tk.Spinbox(main, values=("坐标"))
		mc1.place(x=550+100,y=22)
		b = tk.Button(main, text='标记坐标', font=('Arial', 12), width=10, height=1, command=ok)
		b.place(x=550+100,y=22*2)
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
		file=open('data\world_post.map-name','w')
		for i in list_for:
			print(i)
			file.write(i)
			file.write('\n')
		file.close()
		file=open('data\world_post.map-post','w')
		for i in list:
			file.write(i)
			file.write('\n')
		file.close()
		if HC.AI_save:
			main.after(HC.AI_save_time,in_end)
	def clean():
		value = lb.get(lb.curselection())
		for i in list_for:
			if i == value:
				del list[list_for.index(i)]
				lb.delete(list_for.index(i))
				del list_for[list_for.index(i)]
				log.info('DEL '+i)
				var.set('PS>将会清除的标记："'+i.replace(':','坐标：')+'"')
				break
	def del_all():
		log.info('DEL ALL')
		os.system('DEL data\world_post.map-name')
		log.info('DEL data\world_post.map-name')
		os.system('DEL data\world_post.map-post')
		log.info('DEL data\world_post.map-post')
	def _lb1():
		longging=tk.PhotoImage(file='data/python-logo.png')
		gi1=gi.get_window(0)
		buit1=tk.Toplevel()
		long=tk.Label(buit1,image=longging)
		text1=f'''About you os(computer or system)
		{gi1.processor}
		{gi1.pyversion}
		{gi1.os}
				{gi1.getos('name')},{gi.pf.architecture()[0]}
	name:{gi.pf.node()}
	坐标记录仪版本：{verion}
	主窗口大小：{main.winfo_width()}*{main.winfo_height()+20}
	使用的语言：'''
		buit1.geometry('550x300')
		buit1.tk.call('wm', 'iconphoto', buit1._w, tk.PhotoImage(file=__ico__))
		lb1 = tk.Label(buit1, text=text1,
						width=60,
						height=10,
						justify='left',
						anchor='nw',
						font=('微软雅黑',10),
						fg='black',
						padx=0,
						pady=0)
		lb1.pack()
		long.pack()
		buit1.mainloop()
	def about_save():
		showinfo('info','所有的更改将会在重启后生效')
		if os.path.exists('Opti\AI'):
			opens=open('Opti\AI','r')
			opens.close()
		def set():
			if HC.AI_save:
				HC.setAi(False)
				on.config(text='目前关闭')
				os.popen('DEL /Q /S "Opti\AI"')
			else:
				HC.setAi(True)
				on.config(text='目前打开')
				new=open("Opti\AI",'w')
				new.write('1000')
				new.close()
		def diclose():
			win.destroy()
			if HC.AI_c == True:
				win2=tk.Toplevel()
				win2.geometry('550x300')
				win2.tk.call('wm', 'iconphoto', win2._w, tk.PhotoImage(file=__ico__))
				def boff1():
					win2.destroy()
				def bon1():
					main.destroy()
				lib=tk.Label(win2,text='是否重启以启用？')
				boff=tk.Button(win2,text='否',command=boff1)
				bon=tk.Button(win2,text='是',command=bon1)
				lib.pack()
				boff.pack()
				bon.pack()
		win=tk.Toplevel()
		win.geometry('550x300')
		win.tk.call('wm', 'iconphoto', win._w, tk.PhotoImage(file=__ico__))
		on=tk.Label(win)
		one=tk.Button(win,text='打开或关闭自动保存',command=set)
		if HC.AI_save:
			on.config(text='目前打开')
		else:
			on.config(text='目前关闭')
		on.pack()
		one.pack()
		win.protocol("WM_DELETE_WINDOW", diclose)
	class menu:
		def __init__(self) -> None:
			self.menu=tk.Menu(main,tearoff=0)
			self.menu.add_command(label='help',command=self.help)
			self.menu.add_command(label='About os',command=_lb1)
		def help(self):
			showinfo('Hlep','version '+verion)
	class menu2:
		def __init__(self) -> None:
			self.menu=tk.Menu(main,tearoff=0)
			self.menu.add_command(label='Use mcpi',command=mcpi_)
			self.menu.add_command(label='Test ip',command=test)
			self.menu.add_command(label='自动保存',command=about_save)
	if __name__ == '__main__':
			mebubar=tk.Menu(main)
			mebubar.add_cascade(label='other|选项',menu=menu2().menu)
			mebubar.add_cascade(label='help|帮助',menu=menu().menu)
			mebubar.add_command(label='quit|退出',command=main.quit)
			var2 = tk.StringVar()
			var2.set((''))
			lb=tk.Listbox(main, listvariable=var2,width=78)
			lb.place(x=0,y=42)
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
			end = tk.Button(main, text='复制', font=('Arial', 12), width=10, height=1, command=ctrl_and_c)
			end.place(x=0,y=225)
			end = tk.Button(main, text='清除标记', font=('Arial', 12), width=10, height=1, command=clean)
			end.place(x=550)
			end = tk.Button(main, text='删除保存文件', font=('Arial', 12), width=10, height=1, command=del_all)
			end.place(x=550,y=31)
			end = tk.Button(main, text='删除日志', font=('Arial', 12), width=10, height=1, command=log._DELOLDLOG)
			end.place(x=550,y=31*2)
			if not HC.AI_save:
				end = tk.Button(main, text='保存', font=('Arial', 12), width=10, height=1, command=in_end)
				end.place(x=100,y=225)
			main.config(menu=mebubar)
			main.after(0,in_end)
			main.mainloop()
except BaseException as e:
    showwarning('CRITICAL',f'错误始程序无法运行：{e}')
import logging
import os
import time
print('''From xu.bw.
Use logging.''')
Log_v_main9=False
Log_v_main10=False
Log_v_main6 = None
Log_v_main5 = './log/late-log.log'
def save():
    print('These log will seve in "./log/late-log.log"')
    if not os.path.exists('./log'):
        os.system('md .\log')
        Log_v_main2 = open(Log_v_main5, 'w')
        Log_v_main3 = time.asctime(time.localtime())
        Log_v_main4 = [Log_v_main3, '\n']
        Log_v_main2.writelines(Log_v_main4)
        Log_v_main2.close()
    if os.path.exists(Log_v_main5):
        Log_v_main2 = open(Log_v_main5, 'r')
        Log_v_main1 = Log_v_main2.readlines()
        Log_v_main6 = Log_v_main1[0]
        Log_v_main2.close()
        Log_v_main8 = ['：' if i == ':' else i for i in Log_v_main6]
        Log_v_main8.pop(Log_v_main8.index('\n'))
        Log_v_main7 = ''
        for i in Log_v_main8:
            Log_v_main7 += i
        os.system('ren ".\log\late-log.log" "'+Log_v_main7+'.log"')
    if not os.path.exists(Log_v_main5):
        Log_v_main2 = open(Log_v_main5, 'w')
        Log_v_main3 = time.asctime(time.localtime())
        Log_v_main4 = [Log_v_main3, '\n']
        Log_v_main2.writelines(Log_v_main4)
        Log_v_main2.close()
    logging.basicConfig(filename=Log_v_main5, level=logging.NOTSET, filemode='a',format='%(asctime)s : %(levelname)s level:%(levelno)s Log:%(message)s', datefmt='%m/%d/%Y %I:%M:%S world.tiem=%p')
def _DELOLDLOG(*Any):
    print('不用管XXX\log\late-log.log因为他是当前的日志!')
    time.sleep(0.5)
    os.system('DEL /Q /S ".\log\*.*"')
def DEBUGANDHAIGHSHOW(bool_int:int)->bool: # type: ignore
    global Log_v_main9
    Log_v_main9=bool(bool_int)
def INFOANDHAIGHSHOW(bool_int:int)->bool: # type: ignore
    global Log_v_main10
    Log_v_main10=bool(bool_int)
def debug(orj: str, *args, **kwargs):
    logging.debug(orj, *args, **kwargs)
    if Log_v_main9:
        print('\033[32mDEBUG:root:\033[0m%s'%orj)
def info(orj: str, *args, **kwargs):
    logging.info(orj, *args, **kwargs)
    if Log_v_main10 or Log_v_main9:
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
def help():
    HELP()
def 帮助():
    help()

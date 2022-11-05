import logging
import os
import time
print('''From xu.bw.
Use logging.''')
_________=False
__________=False
______ = None
_____ = './log/late-log.log'
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
def help():
    HELP()
def 帮助():
    help()

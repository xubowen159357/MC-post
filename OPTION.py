import log

get_False_line=['log.seve.type=FALSE\n','Log.seve=FALSE','option.type=FALSE\n','Log.SHW_D=FALSE\n','Log.SHW_I=FALSE\n','USE_PUS=FALSE']
get_True_line=['log.seve.type=TRUE\n','Log.seve=TRUE','option.type=TRUE\n','Log.SHW_D=TRUE\n','Log.SHW_I=TRUE\n','USE_PUS=TRUE']

def get(bool):
    if bool:
        return get_True_line
    else:
        return get_False_line
def main_opti(option:list):
    gg=None
    gg2=None
    if get_True_line[2] in option:
        option_type=1
    else:
        option_type=0
    if option_type:
        for i in option:
            if i == get_True_line[3]:
                gg=1
            elif i == get_True_line[4]:
                gg2=1
            elif i == get_True_line[5]:
                print('开发中！')
        if gg and gg2:
            return 'SD'
        elif gg:
            return 'SD'
        elif gg2:
            return 'SI'
    if not option_type:
        print('option.type=FALSE or Can not catch! wll use def!')
        log.info('option.type=FALSE or Can not catch! wll use def!')
def main_log(log_line:list):
    if get_True_line[0] in log_line:
        log_line_type=1
    else:
        log_line_type=0
    if log_line_type:
        for i in log_line:
            if i == get_True_line[1]:  
                return '1'
    elif not log_line_type:
        print('log.save=FALSE or Can not catch! wll use def!')
        log.info('log.save=FALSE or Can not catch! wll use def!')
        return '1'
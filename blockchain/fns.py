# -*- coding: utf-8 -*-
'''
some useful function
'''

def getsys():
    '''
    windows, macos or linux
    '''
    import platform
    if platform.system().lower() == 'windows':
        return 'windows'
    elif platform.system().lower() == 'linux':
        return 'linux'
    else:
        return 'macos'

def runNewCmd(cmd):
    '''
    根据操作系统的不同采用不同的执行方式在新的终端中执行命令
    '''
    import subprocess
    cmds = cmd.split()
    linux = ['gnome-terminal', '-x']
    for i in cmds:
        linux.append(i)
    system_ = getsys()
    if system_ == 'windows':
        subprocess.call('start /wait '+cmd, shell=True)
    elif system_ == 'linux':
        subprocess.call(linux)
    else:
        import appscript
        appscript.app('Terminal').do_script(cmd)

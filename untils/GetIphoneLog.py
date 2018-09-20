'''
@author: lileilei
@file: GetIphoneLog.py
@time: 2018/9/20 16:56
'''
import  subprocess,os,time
path=os.getcwd()
logPath = os.path.join(path,'testlog')
def getLOg(devices):

    clear_cmd = 'adb -s ' + devices + ' logcat -c'
    subprocess.run(clear_cmd, shell=True)
    logcat_log = os.path.join(logPath, "logcat.log")
    cmd_logcat = "adb -s " + devices + " logcat > %s" % (logcat_log)
    os.popen(cmd_logcat)
def Count_crash():
    # 分析logcat日志
    count = 0
    count_line = 0
    word_list = ['ANR', 'FATAL']
    with open(logPath + '/logcat.log', 'rt') as f:
        for line in f:
            count_line += 1
            for word in word_list:
                if word in line:
                    text = f.readlines(count_line)
                    with open(logPath + "/crashInfo.txt", "a") as w:
                        w.write('=========================crash=========================\n')
                        w.writelines(text)
                        count += 1
                        w.close()
    f.close()
    return count
from django.shortcuts import render
import os
import glob
import re
from crontab import CronTab
from datetime import datetime, timedelta
import logging
import math
from multiprocessing import Pool
import time

class JobConfig(object):
    def __init__(self, crontab, job):
        """
        :type crontab: crontab.CronTab
        :param crontab: 実行時間設定
        :type job: function
        :param job: 実行する関数
        """
        self._crontab=crontab
        self.job=job
    def schedule(self):
        """
        次回実行日時を取得する。
        :rtype: datetime.datetime
        :return: 次回実行日時を
        """
        crontab=self._crontab
        return datetime.now() + timedelta(seconds=math.ceil(crontab.next()))
    
    def next(self):
        """
        次回実行時刻まで待機する時間を取得する。
        :rtype: long
        :retuen: 待機時間（秒）
        """
        crontab=self._crontab
        return math.ceil(crontab.next())
def job_controller(jobConfig):
    """
    処理コントローラ
    :type crontab: crontab.CronTab
    :param crontab: 実行設定
    """
    
    logging.info("->- 処理を開始しました。")
    while True:
        try:
            #次実行日時を表示
            logging.info("-?- 次回実行日時\tschedule:%s"% jobConfig.schedule().strftime("%Y-%m-%d %H:%M:%S"))
            
            #次実行時刻まで待機
            time.sleep(jobConfig.next())
            logging.info("-!> 処理を実行します。")
            
            #処理を実行する。
            jobConfig.job()
            logging.info("-!< 処理を実行しました。")
        except KeyboardInterrupt:
            break
    logging.info("-<- 処理を終了しました。")
    
def file_eraser():
    # if os.path.isfile('testsite2/media/*.xlsx'):
    xlsx_list=glob.glob('testsite2/media/*.xlsx')
    print(xlsx_list)
    for file_xlsx in xlsx_list:
        os.remove(file_xlsx)
    # if os.path.isfile('testsite2/*.txt'):
    txt_list=glob.glob('testsite2/*.txt')
    print(txt_list)
    for file_txt in txt_list:
        os.remove(file_txt)
    # if os.path.isfile('testsite2/*.log'):
    log_list=glob.glob('testsite2/*.log')
    print(log_list)
    for file_log in log_list:
        os.remove(file_log)
    logging.debug("処理1 -file_eraser-")

def main():
    """
    """
    
    #ログ設定
    logging.basicConfig(level=logging.DEBUG,
        format="time:%(asctime)s.%(msecs)03d\tprocess:%(process)d" + "\tmessage: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    
    #毎分実行設定
    jobConfigs=[
        #処理1を1分毎に実行する
        JobConfig(CronTab("* * * * *"), file_eraser)
    ]
    
    #処理を並列に実行
    p=Pool(len(jobConfigs))
    try:
        p.map(job_controller, jobConfigs)
    except KeyboardInterrupt:
        pass
    
# if __name__=="__main__":
#     main()
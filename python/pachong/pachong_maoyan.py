import pandas as pd
import numpy as np
import time
import inspect
import sys
import logging,requests
from comtools import printException, printInfo
import json

reload(sys)
sys.setdefaultencoding( "utf-8" )

play_data = pd.DataFrame(columns=['date','name','play_num','type','platform','monopoly'])

# with open('/data/mxl/pachong/result.csv','w') as f:
for i in range(0, 3):
    for j in range(0,7):
        for date in pd.date_range('2018-08-01','2018-08-24',freq='D'):
            try:
                time.sleep(0.5)
                url= 'http://box.maoyan.com/proseries/api/seriesTopRank.json?platformType='+str(j)+'&seriesType='+str(i)+'&dateRange=0&date='+str(date)[0:10]
                html = requests.get(url=url).content
                data = json.loads(html.decode('utf-8'))['data']['seriesDailyRankList']
                for item in data:
                    play_data = play_data.append({'date':str(date)[0:10],
                                                  'name':item['name'],
                                                  'play_num':float(item['playCountDesc']),
                                                  'type':i,
                                                  'platform':j,
                                                  'monopoly':item['platformInfoDescV2']},
                                                 ignore_index=True)
                # print(str(i)+' '+str(j)+' '+str(date)[0:10])
                # f.write(str(i)+' '+str(j)+' '+str(date)[0:10]+"\n")
                # f.write(play_data)
                # print(play_data)

            except:
                printException()

play_data.to_csv('/data/mxl/pachong/result.csv', sep=',', header=True, index=True)
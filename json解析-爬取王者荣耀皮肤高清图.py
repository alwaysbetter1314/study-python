
import os
import requests
import json
import urllib.request as ur

r=requests.get("http://pvp.qq.com/web201605/js/herolist.json").text
herojson= json.loads(r)
# 英雄数量
heronum = len(herojson)
# 存放目录
save_dir="wzry-skin\\"
# 没文件夹则创建
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
for i in range(heronum):
    skin_names = (herojson[i]['skin_name']).split('|')
    for n in range(len(skin_names)):
        savefile = save_dir+str(herojson[i]['ename'])+herojson[i]['cname']+skin_names[n]+".jpg"
        # 官方网页大图 background: url('//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/505/505-bigskin-1.jpg')
        skinurl="https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"+str(herojson[i]['ename'])+'/'+str(herojson[i]['ename'])+"-bigskin-"+str(n+1)+".jpg"
        print(skinurl)
        if not os.path.exists(savefile):
            ur.urlretrieve(skinurl,savefile)

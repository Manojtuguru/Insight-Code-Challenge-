import os
import json
import re
import time
import datetime

output = open('output.txt', 'wb')

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)


class ConcatJSONDecoder(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        s_len = len(s)

        objs = []
        end = 0
        while end != s_len:
            obj, end = self.raw_decode(s, idx=_w(s, end).end())
            end = _w(s, end).end()
            objs.append(obj)
        return objs
TempVar1=0
TempVar2=0
tweetmap= {}
TempArray=[]
file = open(os.path.expanduser("~/Documents/tweets.txt"))
data = json.load(file, cls=ConcatJSONDecoder)
for y in range (0, len(data)):
 try:
  test= data[y]["entities"]["hashtags"]
  test2= data[y]["created_at"]
  UT=time.mktime(datetime.datetime.strptime(test2, "%a %b %d %H:%M:%S +0000 %Y").timetuple())
  
  UT2=time.mktime(datetime.datetime.strptime(data[y+1]["created_at"], "%a %b %d %H:%M:%S +0000 %Y").timetuple())-UT
  if UT2>=0 and UT2<=60:    
      if len(test)>0:
       TempVar2=TempVar2+1    
       for x in range (0, len(test)):
      
        TempArray.append(test[x]["text"])
        TempVar1=TempVar1+1
       
       tweetmap[y]=TempArray
       TempArray=[]
      
 except:
  pass
hashtagmap={}
arraymap=[]
      
for key in tweetmap:
       
    for y in range(0, len(tweetmap[key])):
        if(hashtagmap.has_key(tweetmap[key][y])==False):
            hashtagmap[tweetmap[key][y]]=len(tweetmap[key])-1
        else:
             t=hashtagmap[tweetmap[key][y]]
             hashtagmap[tweetmap[key][y]]=t+len(tweetmap[key])-1
            
    sum=0;
    for key in hashtagmap:
        sum=sum+hashtagmap[key]
    sum1=sum//len(hashtagmap)
    output.write("%.2f" %sum1+"\n")

output.close()
        

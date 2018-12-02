# -*- coding: utf-8 -*-
#copied and modified from TPS repo.

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!flip'):
      args = info.content.split(' ')
      if len(args) == 1:
        server.tell(random.randint(0,1))
      elif (len(args) == 2) and (args[1]=='help'):
        server.tell(info.player, '使用 !!flip (上限，默认0) (<下限>，默认1) 进行一次[上限,下限]范围内的随机')
      elif (len(args) == 2) and (args[1].isdigit()) and (int(float(args[1])) > 0):
        server.tell(random.randint(0,int(float(args[1]))))
      elif (len(args) == 3) and (args[1].isdigit()) and (args[2].isdigit()) and (int(float(args[1])) > int(float(args[2]))):
        server.tell(random.randint(int(float(args[2])),int(float(args[1]))))
      else:
        server.tell('输入无效')

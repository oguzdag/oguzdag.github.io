from collections import defaultdict

class FilterModule(object):
     def filters(self):
         return { 
           'createmylist': self.createlistfunction
         }
     
     def createlistfunction(self, instancelist, clustervars, hostvars_tmp,playhost_tmp, startindex, endindex):
         retval = []
         clusterinfo = defaultdict(list)
         myserverlist = []
         for i in range(int(startindex),int(endindex)+1):
           clusterinfo = {
#             "index": instance["index"],
             "name": clustervars["startstr"]+clustervars["envname"]+clustervars["middlestr"]+str(i)+clustervars["endstr"],
             "multicastEnabled": "false",
             "servers":[]
           }
           for item in playhost_tmp:
             serverid=0
             for item2 in hostvars_tmp[item]['muleserverids']: 
               if item2['index'] == i :
                 serverid= item2['serverId']
             serverIp=hostvars_tmp[item]['serverIp']
             serverlist={ "serverId": serverid, "serverIp": serverIp }
             clusterinfo["servers"].append(serverlist)
           #clusterinfo["servers"].append(myserverlist)
           myserverlist = []
           retval.append(clusterinfo)
     
         return retval 

from wxpy import *
from chatwith.friends.friends import Friends


class Groups(Friends):
    @staticmethod
    def getInstance():
        return Groups()

    def getAllGroups(self):
        try:
            return self.groups()
        except Exception as e:
            logging.warning("获取全部群组失败", e)
            return False

    def getSomeGroups(self, names):
        somegroups = []
        try:
            for name in names:
                somegroups.extend(self.getOneGroup(name))
            return somegroups
        except Exception as e:
            logging.warning("获取部分群组失败", e)
            return False

    def getOneGroup(self, name):
        onegroup = []
        try:
            groups = self.groups()
            for group in groups:
                if name == group.nick_name:
                    onegroup.append((group,group.nick_name))
            return onegroup
        except Exception as e:
            logging.info("获取一个群组失败", e)
            raise

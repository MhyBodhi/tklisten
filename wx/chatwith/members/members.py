from wxpy import *
from chatwith.groups.groups import Groups


class Members(Groups):

    @staticmethod
    def getInstance():
        return Members()

    def getAllMembers(self,group):
        try:
            group = ensure_one(self.groups().search(group))
            return group.members
        except Exception as e:
            logging.warning("获取全部群友失败", e)
            return False

    def getSomeMembers(self, group,names):
        listMembers = []
        try:
            group = ensure_one(self.groups().search(group))
            for name in names:
                listMembers.extend(self.getOneMember(name))
            return listMembers
        except Exception as e:
            logging.warning("获取部分群友失败", e)
            return False

    def getOneMember(self, group,name):
        onemember = []
        try:
            group = ensure_one(self.groups().search(group))
            for member in group.members:
                if name==member.nick_name:
                    onemember.append((member,member.nick_name))
            return onemember
        except Exception as e:
            logging.info("获取一个群友失败", e)
            raise
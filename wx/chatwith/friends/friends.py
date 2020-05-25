from wxpy import *
from wx.bases.bots import Bots
class Friends(Bots):

    @staticmethod
    def getInstance():
        return Friends()

    def getAllFriends(self):
        try:
            return self.friends()
        except Exception as e:
            logging.warning("获取全部好友失败",e)
            return False

    def getSomeFriends(self,names):
        somefriend = []
        try:
            for name in names:
                somefriend.extend(self.getOneFriend(name))
            return somefriend
        except Exception as e:
            logging.warning("获取部分好友失败",e)
            return False


    def getOneFriend(self,name):
        onefriend = []
        try:
            friends = self.friends()
            for friend in friends:
                if friend.nick_name == name:
                    onefriend.append((friend,friend.nick_name))
            return onefriend
        except Exception as e:
            logging.info("获取一个好友失败", e)
            raise

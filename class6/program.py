import md5


# User 用户类
# EngineRoom 机房类
# Cabinet 机柜类
# NetDevice 网络设备类
# Hosts 主机类
# Salt_Hosts 被Salt 监控的主机类
# Salt_Master Salt Master 类, 管理minion包括Syndic的minion
# Salt_Syndic Syndic类 管理自己的minion 但被master 管理

class User:
    def __init__(self, username, password, permission=0):
        self.username = username
        self.password = md5(password)
        self.permission = permission

    def login(self, username, password):
        # 检查输入的用户名密码是否对应数据库的用户密码
        return self

    @classmethod
    def register(self, username, password, permission=0):
        pass

    def logout(self, username):
        pass


class EngineRoom:
    cabinet_number = 0

    def __init__(self, position, area):
        self.position = position
        self.area = area

    def put(self, cabinet):
        # 将机柜放到机房
        self.cabinet_number += 1
        pass

    def remove(self, cabinet):
        # 将机柜移出机房
        pass

    def show(self):
        return all_cabinet


class Cabinet:
    server_number = 0

    def __init__(self, position, height='42U'):
        self.position = position
        self.height = height

    def put(self, server):
        # 将服务器存放到机架上
        self.server_number += 0
        pass

    def remove(self, server):
        # 将服务器从机架移走
        pass

    def show(self):
        return all_server


class Hosts:
    def __init__(self, brand, price, buy_date, position, hostname=None, ip=None):
        self.brand = brand
        self.price = price
        self.buy_date = buy_date
        self.position = position
        self.hostname = hostname
        self.ip = ip

    def is_alive(self):
        pass


class SaltHosts(Hosts):
    def __init__(self, hostname, ip, salt_id):
        super().__init__(hostname, ip)

    def salt_run(self):
        # 在本机执行salt命令 所有salt客户端都可执行
        pass

    def is_master(self):
        # 判断机器是否为master
        pass

    def is_syndic(self):
        # 判断机器是否为Syndic
        pass


class SaltMaster(SaltHosts):

    def keys_manager(self, target=None, action='list-all'):
        # 秘钥管理 根据action 与target 作出相关操作
        pass

    def excute_cmd(self, target, cmd):
        # 对指定target 执行命令  salt target cmd.run cmd
        # 常用
        pass

    def excute_sls(self, target, sls):
        # 对指定target 执行命令 salt target state.sls sls
        pass

    def excute_salt_cmd(self, target, cmd):
        #  执行自定义的salt 命令
        #  target = '*'
        #  cmd = 'pillar.get os'
        #  salt '*' pillar.get os
        pass

    def install_minions(self, target):
        # 使用salt-ssh 对target 安装salt-minion客户端
        pass


class SaltSyndic(SaltMaster):

    def __init__(self, hostname, ip, salt_id, master):
        self.salt_id = salt_id
        self.master = master
        super().__init__(hostname, ip)


class NetDevice(Hosts):
    pass

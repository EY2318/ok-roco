import re

from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class AutoDayAlter(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "自动切换白天"
        # self.group_name = "任务列表"
        self.group_icon = FluentIcon.SYNC
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            '运行轮数': 999,
            '间隔时间(分)': 20,
            '启用动作': True,
            '动作类型': 3,
            '动作间隔': 7.9,
            '携带奇丽花队伍': True,
            '使用须知': "需要提前对着魔力之源传送点,弹出能够交互的选项即可,不要有周围人干扰,不要有回顾选项",
        })

    def dropAll(self):
        # 初始投掷奇丽花    
        for i in range(6):
            self.send_key(f'{i+1}')
            self.sleep(0.3)
            self.mouse_down()
            self.sleep(0.5)
            self.mouse_up()
            self.sleep(0.8)
        
        while True:
            tmp = 0
            prepare1_btn = self.find_one('prepare1',threshold=0.75)
            prepare2_btn = self.find_one('prepare2',threshold=0.75)
            prepare3_btn = self.find_one('prepare3',threshold=0.75)
            prepare4_btn = self.find_one('prepare4',threshold=0.75)
            prepare5_btn = self.find_one('prepare5',threshold=0.75)
            prepare6_btn = self.find_one('prepare6',threshold=0.7)

            if prepare1_btn == None:
                self.send_key('1')
                self.sleep(0.3)
                self.mouse_down()
                self.sleep(0.5)
                self.mouse_up()
                self.sleep(0.8)
                tmp += 1
            if prepare2_btn == None:
                self.send_key('2')
                self.sleep(0.3)
                self.mouse_down()
                self.sleep(0.5)
                self.mouse_up()
                self.sleep(0.8)
                tmp += 1
            if prepare3_btn == None:
                self.send_key('3')
                self.sleep(0.3)
                self.mouse_down()
                self.sleep(0.5)
                self.mouse_up()
                self.sleep(0.8)
                tmp += 1
            if prepare4_btn == None:
                self.send_key('4')
                self.sleep(0.3)
                self.mouse_down()
                self.sleep(0.5)
                self.mouse_up()
                self.sleep(0.8)
                tmp += 1
            if prepare5_btn == None:
                self.send_key('5')
                self.sleep(0.3)
                self.mouse_down()
                self.sleep(0.5)
                self.mouse_up()
                self.sleep(0.8)
                tmp += 1
            if prepare6_btn == None:
                self.send_key('6')
                self.sleep(0.3)
                self.mouse_down()
                self.sleep(0.5)
                self.mouse_up()
                self.sleep(0.8)
                tmp += 1
            if tmp == 0:
                break


    def run(self):
        self.log_info("开始运行")
        onesDelay = self.config.get('间隔时间(分)') * 60
        action_interval = self.config.get('动作间隔')

        times = 0
        run_times = self.config.get('运行轮数')
        while times < run_times:
            times += 1
            self.log_info("切换白天")

            # 切换白天
            self.send_key_down('f')
            self.sleep(0.3)
            self.send_key_up('f')
            self.sleep(7)
            self.send_key_down('1')
            self.sleep(0.3)
            self.send_key_up('1')
            self.sleep(4)
            self.send_key_down('1')
            self.sleep(0.3)
            self.send_key_up('1')
            self.sleep(8)
            self.send_key_down('2')
            self.sleep(0.3)
            self.send_key_up('2')
            self.sleep(5)

            if self.config.get('携带奇丽花队伍'):
                # 投掷奇丽花    
                self.log_info("开始投掷奇丽花")
                self.dropAll()
                self.log_info("投掷奇丽花完成")
            self.sleep(1)
            if self.config.get('启用动作'):
                tmptime = 0
                self.log_info("开始执行动作")
                self.send_key('Tab')
                while True:
                    self.sleep(1)
                    emotion = self.find_one('Tab_Esc',threshold=0.7)
                    if emotion is None:
                        self.send_key('Tab')
                    else:
                        break
                self.sleep(1)
                while tmptime < onesDelay:
                    emotion = self.find_one('Tab_Esc',threshold=0.7)
                    if emotion is None:
                        self.send_key('Tab')
                        self.sleep(1)
                    self.send_key(str(self.config.get('动作类型')))
                    self.sleep(0.1)
                    self.send_key(str(self.config.get('动作类型')))
                    self.sleep(0.1)
                    self.send_key(str(self.config.get('动作类型')))
                    self.send_key('x')
                    self.sleep(action_interval)
                    tmptime += action_interval
                while True:
                    self.sleep(1)
                    emotion = self.find_one('Tab_Esc',threshold=0.7)
                    if emotion is not None:
                        self.send_key('Esc')
                    else:
                        break
                self.sleep(1)
                self.log_info("动作执行完成")
            else:
                self.sleep(onesDelay)









import re

from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class AutoTab(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "自动动作"
        # self.group_name = "任务列表"
        self.group_icon = FluentIcon.SYNC
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            # '是否选项默认支持': False,
            '运行轮数': 9999,
            '间隔': 8.0,
            '动作类型': 3,
            '使用须知': "自动鞠躬",
        })


    def run(self):
        self.middle_click()
        self.sleep(0.5)

        delay = self.config.get('间隔')
        times = self.config.get('运行轮数')
        action_interval = self.config.get('动作间隔')

        for i in range(times):
            while True:
                self.sleep(1)
                emotion = self.find_one('Tab_Esc',threshold=0.7)
                if emotion is None:
                    self.send_key('Tab')
                else:
                    break
            self.send_key(str(action_interval))
            self.sleep(0.1)
            self.send_key(str(action_interval))
            self.sleep(0.1)
            self.send_key(str(action_interval))
            self.send_key('x')

            self.sleep(delay)

                








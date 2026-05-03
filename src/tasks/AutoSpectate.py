import re

from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class AutoSpectate(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "自动观战"
        # self.group_name = "任务列表"
        self.group_icon = FluentIcon.SYNC
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            # '是否选项默认支持': False,
            '使用须知': "站在人堆里",
        })


    def run(self):
        while True:
            qiecuo = self.find_one('qiecuo')
            guanzhan = self.find_one('guanzhan')
            guan = self.find_one('guan')

            if guanzhan is not None:
                self.click_box_with_move(guanzhan)
                self.guanzhan_count = getattr(self, 'guanzhan_count', 0) + 1
                if self.guanzhan_count > 3:
                    self.send_key('Esc')
                    self.guanzhan_count = 0
            elif qiecuo is not None:
                self.send_key('Esc')
                self.guanzhan_count = 0
            elif guan is not None:
                self.click_box_with_move(guan)
                self.guanzhan_count = 0
            else :
                self.send_key('f')
                self.guanzhan_count = 0

            self.sleep(1)








import re

from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class AutoQILIHUA(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "自动刷奇丽花2"
        self.description = "需要至少5只奇丽花"
        # self.group_name = "任务列表"
        self.group_icon = FluentIcon.SYNC
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            # '是否选项默认支持': False,
            '运行轮数': 999,
            '是否六只奇丽花': False,
            '使用须知': "需要预先切换到奇丽花配队,配队中2号位带坐骑用于采花,组队的话可以带同乘坐骑。去艾普鲁庄园的大型眼枭庇护所,传送过去后开启脚本即可,传送过去什么都不要做",
        })

    def pressEmotion(self):
        self.send_key('Tab')
        self.sleep(0.8)
        self.send_key('2')
        self.sleep(0.8)
        self.send_key('Esc')

    def run(self):
        self.middle_click()
        self.sleep(0.5)

        use_six = self.config.get('是否六只奇丽花')

        times = 0
        run_times = self.config.get('运行轮数')
        while times < run_times:
            times += 1
            self.log_info(f'第{times}次召唤奇丽花')

            # self.move_relative(0, 0.5)
            # self.move_relative(0, 0.5)
            # self.move_relative(0, 0.5)
            # self.move_relative(0, 0.5)
            # self.move_relative(0, 0.5)
            # self.move_relative(0, 0.5)

            self.send_key('1')
            self.sleep(0.3)
            self.mouse_down()
            self.sleep(0.1)
            self.mouse_up()
            self.sleep(1)

            if use_six:
                self.send_key('2')
                self.sleep(0.3)
                self.mouse_down()
                self.sleep(0.1)
                self.mouse_up()
                self.sleep(1)

            self.send_key('3')
            self.sleep(0.3)
            self.mouse_down()
            self.sleep(0.1)
            self.mouse_up()
            self.sleep(1)

            self.send_key('4')
            self.sleep(0.3)
            self.mouse_down()
            self.sleep(0.1)
            self.mouse_up()
            self.sleep(1)

            self.send_key('5')
            self.sleep(0.3)
            self.mouse_down()
            self.sleep(0.1)
            self.mouse_up()
            self.sleep(1)

            self.send_key('6')
            self.sleep(0.3)
            self.mouse_down()
            self.sleep(0.1)
            self.mouse_up()
            self.sleep(0.3)

            for i in range(15):
                self.pressEmotion()
                self.sleep(15)
                self.send_key('2')
                self.sleep(1)
                self.send_key('r')
                self.sleep(1)
                self.send_key('x')
                self.sleep(0.5)
                self.mouse_down()
                self.sleep(0.1)
                self.mouse_up()
                self.sleep(1)
            
            self.sleep(0.3)
            self.send_key('m')
            self.sleep(2) 
            self.click_box_with_move()
            self.sleep(0.5)
            cs_button = self.find_one('cs_button')
            if cs_button:
                self.click_box_with_move(cs_button, relative_x=0.5, relative_y=0.5, down_time=0.3, move_back=True)
                self.log_info("点击传送")
            else:
                self.log_info("未找到cs_button，跳过点击")
            
            self.sleep(2)
            
            loading = self.wait_feature('loading', time_out=10)
            if loading:
                self.log_info("检测到加载中...")
                while self.find_one('loading'):
                    self.sleep(1)
                self.log_info("加载完成")
                self.sleep(2)
                








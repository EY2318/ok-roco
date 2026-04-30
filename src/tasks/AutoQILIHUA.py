import re

from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class AutoQILIHUA(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "自动刷奇丽花"
        # self.group_name = "任务列表"
        self.group_icon = FluentIcon.SYNC
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            # '是否选项默认支持': False,
            '运行轮数': 999,
            '是否使用收割队伍': False,
            '使用须知': "需要预先切换到奇丽花配队,收割队伍放在奇丽花队的上一队,去月兔暗港的魔力之源传送点,传送过去后开启脚本即",
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

            # 传送后修正位置
            self.send_key_down('a')
            self.sleep(0.6)
            self.send_key_up('a')
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
            self.send_key_down('a')
            self.send_key_down('s')
            self.sleep(0.5)
            self.send_key_up('a')
            self.send_key_up('s')

            for i in range(6):
                
                self.mouse_down()
                self.sleep(1.2)
                if i > 0 or times > 1:
                    self.scroll_relative(0.5, 0.5, -1)
                    
                self.sleep(0.8)
                self.send_key('1')
                self.sleep(0.6)
                self.mouse_up()
                self.sleep(2)

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

            
                # self.pressEmotion()
                self.sleep(15)
                # self.send_key('2')
                # self.sleep(1)
                # self.send_key('r')
                # self.sleep(1)
                # self.send_key('x')
                # self.sleep(0.5)
                # self.mouse_down()
                # self.sleep(0.1)
                # self.mouse_up()
                # self.sleep(1)
                self.mouse_down()
                self.sleep(1.2)
                self.scroll_relative(0.5, 0.5, 1)
                self.sleep(0.8)
                self.send_key('1')
                self.sleep(0.6)
                self.mouse_up()
                self.sleep(0.3)
                self.mouse_down()
                self.sleep(0.3)
                self.mouse_up()
                self.sleep(1)
                self.send_key('r')
                self.sleep(1)
                self.send_key('x')
                self.sleep(2)
            
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
                








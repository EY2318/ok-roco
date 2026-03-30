import re

from qfluentwidgets import FluentIcon

from src.tasks.MyBaseTask import MyBaseTask


class MyOneTimeWithAGroup(MyBaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "自动刷奇丽花"
        self.description = "需要6只奇丽花"
        # self.group_name = "任务列表"
        self.group_icon = FluentIcon.SYNC
        self.icon = FluentIcon.SYNC
        self.default_config.update({
            # '是否选项默认支持': False,
            '运行轮数': 999,
            '标题': "务必查看使用须知和设置队伍顺序",
            '使用须知': "需要预先切换到奇丽花配队,找一块草地不要有野生精灵在附近游荡的,脚本会自动投掷收割队的第一位来收割花朵,如果有巧手特性的可以放在第一位来增加收割范围",
            '是否使用表情动作': True,
            '是否使用收割队伍收割花朵(不开的话你得先自己骑乘精灵,注意不要骑乘1号位精灵)': True,
            '队伍顺序设置': ['其他队伍', '收割队', '奇丽花队'],
            '目前正在使用的队伍': "其他队伍",
        })
        self.config_type["目前正在使用的队伍"] = {'type': "drop_down",
                                      'options': ['其他队伍', '收割队', '奇丽花队']}

    def switch_to_team(self, target_team_name):
        team_order = self.config.get('队伍顺序设置')
        current_team = self.config.get('目前正在使用的队伍')
        
        if current_team == target_team_name:
            self.log_info(f'已在目标队伍: {target_team_name}')
            return True
        
        current_index = team_order.index(current_team)
        target_index = team_order.index(target_team_name)
        total_teams = len(team_order)
        
        self.log_info(f'当前队伍: {current_team}({current_index + 1}队), 目标: {target_team_name}({target_index + 1}队)')
        
        scroll_up_count = (current_index - target_index + total_teams) % total_teams
        scroll_down_count = (target_index - current_index + total_teams) % total_teams
        
        if scroll_up_count <= scroll_down_count:
            scroll_count = scroll_up_count
            scroll_direction = 1
            self.log_info(f'向上滚动{scroll_count}次')
        else:
            scroll_count = scroll_down_count
            scroll_direction = -1
            self.log_info(f'向下滚动{scroll_count}次')
        
        for i in range(scroll_count):
            self.scroll_relative(0.5, 0.5, scroll_direction)
            self.sleep(0.5)
        
        self.config.update({'目前正在使用的队伍': target_team_name})
        self.log_info(f'已切换到队伍: {target_team_name}')
        return True

    def run(self):
        self.middle_click() # 用于刷新窗口状态
        self.sleep(0.5)

        use_emotion = self.config.get('是否使用表情动作')
        use_harvest = self.config.get('是否使用收割队伍收割花朵')

        times = 0
        run_times = self.config.get('运行轮数')
        while times < run_times:
            times += 1
            self.log_info(f'第{times}次召唤奇丽花')
            self.send_key('1')
            self.sleep(0.3)
            self.mouse_down()
            self.sleep(1.3)
            self.switch_to_team('奇丽花队')
            self.send_key('1')
            self.sleep(0.3)
            self.mouse_up()
            self.sleep(1)

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
            
            if use_emotion and use_harvest:
                self.send_key('Tab')
                self.sleep(0.8)
                self.send_key('2')
                self.sleep(0.8)
                self.send_key('Esc')

            self.sleep(15) # 等待花生成

            self.mouse_down()
            self.sleep(1.2)
            self.switch_to_team('收割队')
            self.send_key('1')
            self.sleep(0.3)
            self.mouse_up()
            self.sleep(1)






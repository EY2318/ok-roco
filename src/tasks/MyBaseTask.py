import re
import win32gui
import win32api
import win32con

from ok import BaseTask

class MyBaseTask(BaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def operate(self, func):
        self.executor.interaction.operate(func, block=True)

    def do_mouse_down(self, key):
        self.executor.interaction.do_mouse_down(key=key)

    def do_mouse_up(self, key):
        self.executor.interaction.do_mouse_up(key=key)

    def do_send_key_down(self, key):
        self.executor.interaction.do_send_key_down(key)

    def do_send_key_up(self, key):
        self.executor.interaction.do_send_key_up(key)

    def get_window_rect(self):
        try:
            interaction = self.executor.interaction
            if hasattr(interaction, 'hwnd'):
                return win32gui.GetWindowRect(interaction.hwnd)
            if hasattr(interaction, 'window') and hasattr(interaction.window, 'hwnd'):
                return win32gui.GetWindowRect(interaction.window.hwnd)
        except Exception as e:
            pass
        
        try:
            hwnd = win32gui.FindWindow('UnrealWindow', None)
            if hwnd:
                return win32gui.GetWindowRect(hwnd)
        except Exception as e:
            pass
        
        return None

    def click_box_with_move(self, box=None, relative_x=0.5, relative_y=0.5, down_time=0.1, move_back=True):
        rect = self.get_window_rect()
        if not rect:
            self.log_warning("无法获取窗口位置")
            return False
        
        left, top, right, bottom = rect
        
        border_left = 0
        border_top = 0
        try:
            client_rect = win32gui.GetClientRect(win32gui.FindWindow('UnrealWindow', None))
            border_left = (right - left - client_rect[2]) // 2
            border_top = (bottom - top - client_rect[3]) - border_left
        except:
            pass
        
        window_x = left + border_left
        window_y = top + border_top
        window_width = right - left - 2 * border_left
        window_height = bottom - top - border_top - border_left
        
        if box is None:
            target_x = window_x + window_width * relative_x
            target_y = window_y + window_height * relative_y
            self.log_info(f"点击窗口相对位置: ({relative_x}, {relative_y})")
        else:
            target_x = window_x + box.x + box.width * relative_x
            target_y = window_y + box.y + box.height * relative_y
            self.log_info(f"点击Box: {box.name if box.name else 'unnamed'}")
        
        current_pos = win32api.GetCursorPos()
        
        self.log_info(f"窗口位置: ({window_x}, {window_y}), 边框偏移: ({border_left}, {border_top})")
        self.log_info(f"目标坐标: ({int(target_x)}, {int(target_y)})")
        
        win32api.SetCursorPos((int(target_x), int(target_y)))
        self.sleep(0.05)
        
        self.mouse_down()
        self.sleep(down_time)
        self.mouse_up()
        
        if move_back:
            self.sleep(0.05)
            win32api.SetCursorPos(current_pos)
        
        return True

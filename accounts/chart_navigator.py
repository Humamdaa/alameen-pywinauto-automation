from pywinauto import Application, Desktop
from pywinauto.keyboard import send_keys
import pandas as pd
import time

# ===============================
# مدير التنقّل داخل دليل الحسابات
# ===============================
class ChartNavigator:
    def __init__(self, main_window):
        self.main = main_window

    def expand_path(self, steps):
        current = None
        for step in steps:
            print(f"move to {step}")
            # find the text in window
            items = self.main.descendants(control_type="TreeItem")
            target = next((i for i in items if i.window_text() == step), None)
            if not target:
                raise Exception(f"لم أجد العنصر: {step}")

            try:
                if not target.is_expanded():
                    target.expand()
            except:
                pass

            current = target
            time.sleep(0.2)

        return current

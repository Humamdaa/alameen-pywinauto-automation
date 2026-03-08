from pywinauto import Application
from pywinauto.keyboard import send_keys
import time
import re


# ===============================
# مدير الاتصال ببرنامج الأمين
# ===============================
class AlAmeenApp:
    def __init__(self):
        self.app = Application(backend="uia").connect(title_re=".*الأمين.*")
        self.main = self.app.top_window()
        self.main.set_focus()

    def click_menu_path(self, steps):
        materials = self.main.child_window(title=steps[0], control_type="MenuItem")

        materials.click_input()
        time.sleep(0.3)

        for step in steps[1:]:
            item = next(
                (i for i in self.main.descendants(control_type="MenuItem")
                if step in i.window_text()),
                None
            )

            if not item:
                raise Exception(f" not found {step} in menu")
            
            item.click_input()

            time.sleep(0.5)

    def open_context_menu(self, tree_item):
        tree_item.click_input()
        time.sleep(0.3)
        tree_item.right_click_input()
        menu = self.app.window(control_type="Menu")
        menu.wait('visible', timeout=5)
        return menu

    def press_enter(self):
        send_keys("{ENTER}")


  
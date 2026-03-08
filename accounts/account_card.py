from pywinauto.keyboard import send_keys
import time

# ===============================
# مدير نافذة بطاقة الحساب
# ===============================


class AccountCard:
    def __init__(self, main_window):
        self.window = main_window.child_window(
            title="بطاقة حساب", control_type="Window")
        self.window.wait('exists ready', timeout=10)
        self.desc = self.window.descendants()

        self.account_code = self._find_edit("رمز الحساب")  # , index=6
        self.account_name = self._find_edit("اسم الحساب")  # , index=7
        self.add_button = self._find_add_button()


    def _find_edit(self, label):
        statics = [s for s in self.desc if s.friendly_class_name() == "Static"]
        for s in statics:
            if s.window_text().strip() == label:
                parent = s.parent()
                # ابحث عن أول Edit بعد الـ Static داخل نفس الـ parent
                siblings = parent.children()
                start = siblings.index(s)
                for sibling in siblings[start + 1:]:
                    if sibling.friendly_class_name() == "Edit":
                        return sibling
        raise Exception(f"لم أجد الحقل المرتبط بالعنوان: {label}")

    def _find_add_button(self):
        btns = [b for b in self.desc if b.friendly_class_name(
        ) == "Pane" and b.window_text().strip() == "إضافة"]
        if not btns:
            raise Exception("لم أجد زر إضافة")
        return btns[0]

    def fill_fields(self, code, name):
        if code:
            self.account_code.set_edit_text(code)
            time.sleep(0.2)

        self.account_name.set_edit_text(name)
        time.sleep(0.2)

    def click_add(self):
        self.add_button.click_input()
        time.sleep(0.5)

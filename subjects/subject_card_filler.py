import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class SubjectCardFiller:
    """
    كلاس مسؤول عن:
    - إيجاد بطاقة المادة المفتوحة مسبقًا
    - إيجاد الحقول
    - تعبئة البيانات
    - الضغط على زر إضافة
    """

    def __init__(self, app):
        self.app = app
        self.main = app.main

        # نافذة بطاقة المادة (يجب أن تكون مفتوحة مسبقًا)
        self.window = self.main.child_window(
            title="بطاقة مادة", control_type="Window"
        )
        self.window.wait("exists ready", timeout=10)

        # الحقول
        self.code = self._find_edit("رمز المادة")
        self.name = self._find_edit("اسم المادة")
        self.group = self._find_edit("المجموعة")

        self.add_button = self._find_add_button()

    # ----------------------------------------------------
    # أدوات داخلية
    # ----------------------------------------------------
    def _find_edit(self, label_text):
        elements = self.window.descendants()

        for i, el in enumerate(elements):
            if el.element_info.control_type == "Text" and label_text in el.window_text():
                for next_el in elements[i+1:]:
                    if next_el.element_info.control_type == "Edit":
                        return next_el

        raise Exception(f"❌ لم أجد الحقل المرتبط بـ: {label_text}")

    def _find_add_button(self):
        for el in self.window.descendants():
            if el.element_info.control_type == "Pane" and "إضافة" in el.window_text():
                return el
        raise Exception("❌ لم أجد زر 'إضافة'")

    # ----------------------------------------------------
    # تعبئة البطاقة
    # ----------------------------------------------------
    def fill_card(self, code, name, group):
        print(f"➡ تعبئة مادة: {code} - {name}")

        self.name.set_edit_text(name)

        if code:
            self.code.set_edit_text(code)

        self.group.set_edit_text(group)

    def click_add(self):
        self.add_button.click_input()
        time.sleep(0.4)
        self.app.press_enter()

    # ----------------------------------------------------
    # معالجة CSV كامل
    # ----------------------------------------------------
    def process_csv(self, csv_loader):
        print(csv_loader.df.head())

        for _, row in csv_loader.df.iterrows():
            code = str(row["subject symbol"]).strip() if "subject symbol" in row else ""
            name = str(row["subject name"]).strip()
            group = str(row["group"]).strip()

            self.fill_card(code, name, group)
            self.click_add()

        self.window.close()
        print("✔ تم إدخال جميع مواد CSV بنجاح")

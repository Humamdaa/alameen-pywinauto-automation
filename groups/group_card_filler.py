import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class GroupCardFiller:
    """
    كلاس واحد مسؤول عن:
    - فتح بطاقة مجموعة
    - إيجاد الحقول
    - تعبئة البيانات
    - الضغط على زر إضافة
    """

    def __init__(self, app):
        self.app = app
        self.main = app.main
        self.window = self.main.child_window(
            title="بطاقة مجموعة", control_type="Window")
        self.window.wait("exists ready", timeout=10)

        self.code = self._find_edit("الرمز")
        self.name = self._find_edit("الاسم")
        self.main_group = self._find_edit("المجموعة الرئيسية")
        self.add_button = self._find_add_button()
    # ----------------------------------------------------
    # فتح بطاقة مجموعة
    # ----------------------------------------------------

    def open_group_card(self):
        materials = self.main.child_window(
            title="مواد", control_type="MenuItem")
        materials.click_input()
        time.sleep(0.3)

        items = self.main.descendants(control_type="MenuItem")
        target = next(
            (i for i in items if "بطاقة مجموعة" in i.window_text()), None)

        if not target:
            raise Exception("❌ لم أجد 'بطاقة مجموعة'")

        target.click_input()
        time.sleep(0.5)

        # نافذة بطاقة المجموعة

        # تجهيز الحقول

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
    def fill_card(self, code, name, main_group=None):
        print(f"➡ تعبئة: {code} - {name}")

        self.name.set_edit_text(name)
        if code :
            self.code.set_edit_text(code)

        if main_group:
            self.main_group.set_edit_text(main_group)

    def click_add(self):
        self.add_button.click_input()
        time.sleep(0.4)
        self.app.press_enter()

    # ----------------------------------------------------
    # معالجة CSV كامل
    # ----------------------------------------------------
    def process_csv(self, csv_loader):
        has_main_group = "main group" in csv_loader.df.columns
        print(f"has main group? {has_main_group}")
        print(csv_loader.df.head())

        # self.open_group_card()

        for _, row in csv_loader.df.iterrows():
            code = str(row["subject symbol"]).strip()
            name = str(row["subject name"]).strip()
            main_group = str(row["main group"]).strip(
            ) if has_main_group else None

            self.fill_card(code, name, main_group)
            self.click_add()

        self.window.close()
        print("✔ تم إدخال جميع البيانات بنجاح")

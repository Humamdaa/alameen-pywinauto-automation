import sys
import os 
# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from load_file.csv_loader import CSVLoader
from account_card import AccountCard
from chart_navigator import ChartNavigator
from app.alameen_app import AlAmeenApp
import re
import sys
import os


def build_fuzzy_pattern(text):
    """
    يحوّل النص إلى تعبير منتظم مرن:
    - يتجاهل النقاط
    - يسمح بفراغات مرنة
    - يطابق أي نص يحتوي على هذا النص
    """
    pattern = re.escape(text)
    pattern = pattern.replace(r"\ ", ".*")
    return f".*{pattern}.*"

# ===============================
# البرنامج الرئيسي
# ===============================

def main():
    app = AlAmeenApp()

    # فتح دليل الحسابات
    steps = [line.strip() for line in open(
        "accounts-data/Car-Types-Steps.txt", encoding="utf-8") if line.strip()]

    # open the menus
    app.click_menu_path(steps[1:3])

    # to expand the tree to arrive to the target node
    navigator = ChartNavigator(app.main)
    last_item = navigator.expand_path(steps[3:])

    # open context menu (the chioces from the target)
    menu = app.open_context_menu(last_item)

    fuzzy_title_pattern = build_fuzzy_pattern('إضافة حساب فرعي')

    add_sub = menu.child_window(
        title_re=fuzzy_title_pattern, control_type="MenuItem")
    add_sub.wait('visible', timeout=5)
    add_sub.click_input()

    # بطاقة الحساب
    card = AccountCard(app.main)
    print(steps[0])
    csv = CSVLoader(f"{steps[0]}")

    for code, name in csv.rows():
        print(f"إضافة: {name} ({code})")
        card.fill_fields(code, name)
        card.click_add()
        app.press_enter()

    # close the window
    card.window.close()

    print("✅ تم إدخال جميع الحسابات بنجاح")


if __name__ == "__main__":
    main()

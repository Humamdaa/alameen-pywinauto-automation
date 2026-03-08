import time

def deep_debug(app, duration=5):
    print("\n🔎 START DEBUGGING WINDOWS 🔎\n")
    start = time.time()

    while time.time() - start < duration:
        print("\n⏱️ Snapshot @", round(time.time() - start, 2), "seconds")

        for w in app.windows():
            try:
                print("\n==============================")
                print("WINDOW TEXT :", repr(w.window_text()))
                print("CONTROL TYPE:", w.element_info.control_type)
                print("CLASS NAME  :", w.element_info.class_name)
                print("AUTOMATIONID:", w.element_info.automation_id)
                print("==============================")

                for c in w.descendants():
                    print(
                        "  ->",
                        repr(c.window_text()),
                        "| type:", c.element_info.control_type,
                        "| class:", c.element_info.class_name,
                        "| auto_id:", c.element_info.automation_id
                    )
            except Exception as e:
                print("❌ Error reading window:", e)

        time.sleep(0.3)

    print("\n🛑 DEBUG FINISHED 🛑\n")

def debug_windows(app):
    for w in app.windows():
        print("\n==============================")
        print("WINDOW TEXT:", w.window_text())
        print("WINDOW TYPE:", w.element_info.control_type)
        print("WINDOW CLASS:", w.element_info.class_name)
        print("==============================")

        try:
            for c in w.descendants():
                print("  ->", c.window_text(), "|",
                      c.element_info.control_type, "|", c.element_info.class_name)
        except:
            pass

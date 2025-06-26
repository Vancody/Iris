# ─────────────────────────────────────────────────────────────
# Iris — генератор цветовых палитр
# (c) 2025 Mitori Vancody Firelight
#
# Разработка и код: Mitori Vancody Firelight
# Связаться со мной:
#   VK:        https://vk.com/mitori_territory
#   Telegram:  https://t.me/Vancody_Firelight
#   GitHub:    https://github.com/Vancody
#   Discord:   @vancodyfirelight
#
# Этот код распространяется без лицензии, но с сохранением авторства.
# Копирование и использование разрешено при указании автора.
# ─────────────────────────────────────────────────────────────

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from iris.interface.tkinter_app.app import main

if __name__ == "__main__":
    main()

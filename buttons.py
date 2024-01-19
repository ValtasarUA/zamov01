from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton("💰 Заробити")
kb2 = KeyboardButton("👣 Реферальна система")
kb3 = KeyboardButton("👤 Профіль")
kb_ch = KeyboardButton('💬 Чат')
menu_kb.add(kb1, kb2)
menu_kb.add(kb3,kb_ch)


menu_kb02 = ReplyKeyboardMarkup(resize_keyboard=True)
kb102 = KeyboardButton("💰 Заробити")
kb202 = KeyboardButton("👣 Реферальна система")
adminkb01 = KeyboardButton("Адміністрація")
kb302 = KeyboardButton("👤 Профіль")
kb_ch02 = KeyboardButton('💬 Чат')
menu_kb02.add(kb102, kb202)
menu_kb02.add(adminkb01)
menu_kb02.add(kb302,kb_ch02)

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
kb106 = KeyboardButton("➕ Баланс")
kb109 = KeyboardButton("🗯 Розсилка")
kb115468 = KeyboardButton("♦ Інфоюзер")
kbstatis = KeyboardButton("📊 Статистика")
kb108 = KeyboardButton("⬅ Назад")
admin_panel.add(kb106)
admin_panel.add(kb109)
admin_panel.add(kb115468)
admin_panel.add(kbstatis)
admin_panel.add(kb108)

c_kb = ReplyKeyboardMarkup(resize_keyboard=True)
c1 = KeyboardButton("❌ Скасувати")
c_kb.add(c1)

widhart = ReplyKeyboardMarkup(resize_keyboard=True)
widhart01 = KeyboardButton("💳 Вивести")
back = KeyboardButton("⬅ Назад")
widhart.add(widhart01)
widhart.add(back)


ikb48 = InlineKeyboardMarkup(row_width=1)
ik148 = InlineKeyboardButton(text="Долучіться до чату користувачів!", url=f"https://t.me/GorilaChat")
ikb48.insert(ik148)

veref_kb = ReplyKeyboardMarkup(resize_keyboard=True)
veref1 = KeyboardButton('🛑 Верифікація', request_contact=True)
veref_kb.add(veref1)


ikb = InlineKeyboardMarkup(row_width=1)
ik1 = InlineKeyboardButton(text="📋 Правила та політика конфідеційності.", url=f"https://telegra.ph/Mat--ban-01-14")
ikb.insert(ik1)
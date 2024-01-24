from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice
from sqlite import *
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from random import choice
from buttons import *
from config import *
from asyncio import sleep
import emoji
from aiogram.utils.exceptions import Throttled
from datetime import datetime
from decimal import Decimal
import os.path
import os
import base64
import re
# If modifying these scopes, delete the file token.json.
#blocki = [6124970105]
async def delete_message_by_id(message_id: int, chat_id: int):
  try:
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
  except:
    pass





async def checking():
  hour_to = datetime.now().hour
  minute_to = datetime.now().minute
  if str(hour_to) in ['0', '00']:
    if str(minute_to) in ['0', '1', '2']:
      await edit_towidhart('0.0')
      await edit_todeposit('0.0')
      await edit_reftod_all()

class Rosa(StatesGroup):
  text_rosa = State()

class AddPromo1(StatesGroup):
  promo1 = State()
  suma1 = State()
class AddChannel(StatesGroup):
  channel = State()
  lim = State()
class AddPromo2(StatesGroup):
  promo2 = State()
  suma2 = State()

list_baza = []

bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def anti_flood(*args, **kwargs):
  message = args[0]
  #await bot.send_message(message.from_user.id, 'Не флудити! 😡')

class DuelGra(StatesGroup):
  suma_stavok = State()
  id_1 = State()

class ZminBal(StatesGroup):
  id_z = State()
  suma_z = State()

class Promo(StatesGroup):
  promocode = State()

class perekaz(StatesGroup):
  id_o = State()
  suma_p = State()

mats2 = ["🧸"]

class InfoUser(StatesGroup):
  id_user = State()


class OrelStorage(StatesGroup):
  suma_stavka = State()
  orel_or = State()


class Odno(StatesGroup):
  stavka_odno = State()


class Widwart(StatesGroup):
  suma_w = State()
  karta_w = State()

async def check_verif(user):
  ver = await get_veref(user)

  if ver[2] != 'False':
    return True
  else:
    return False

ikb52563 = InlineKeyboardMarkup(row_width=1)
ik152563 = InlineKeyboardButton(text="Lucky Star - Казино", url=f"https://t.me/Lucky_Star2_bot")
ikb52563.insert(ik152563)

async def on_startup(_):
  await db_start()
  await db_start3()

  await db_start5()
  await db_start6()
  await db_start7()
  await db_start8()
  await db_start9()
  #await speak("Бот успешно запущен!")
  print("On")

bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'], state=None)
#@dp.throttled(anti_flood, rate=1)
async def start(message: types.Message):
  user = message.from_user.id
  await create_veref(message.from_user.id)
  await create_reftod(message.from_user.id)
  await checking()
  await create_balances(message.from_user.id)
  await create_profile(message.from_user.id, message.from_user.username)
  await create_bonus(message.from_user.id, 0)
  await message.delete()
  referrer_id = str(message.text[7:])
  if referrer_id != "":
    if str(referrer_id) != str(message.from_user.id):
      ref = await add_refer(referrer_id, message.from_user.id)

  verres = await check_verif(user)

  if verres == True:

    if 1==1:


        result = await bot.get_chat_member('@GorilaChat',
                                           int(message.from_user.id))
        #print(result.status)
        if result.status in ['member', 'administrator', 'creator', 'restricted']:

          if message.from_user.id in admins:
            keyb = menu_kb02
          else:
            keyb = menu_kb

          #print("Klick start")
          #await speak("присоединился новый пользователь!")         

          await bot.send_message(message.from_user.id,
                                 "Вітаємо в нашому боті!",
                                 reply_markup=keyb)
          await bot.send_message(
              message.from_user.id,
              "Перед користуванням ознайомтесь з правилами та політикою конфідеційності!",
              reply_markup=ikb)
          await create_profile(message.from_user.id, message.from_user.username)
          await create_balances(message.from_user.id)
          await create_bonus(message.from_user.id, 0)
        if result.status not in ['member', 'administrator', 'creator', 'restricted']:
          await bot.send_message(message.from_user.id, "Вітаємо в нашому боті!", reply_markup=menu_kb)
          await bot.send_message(message.from_user.id,
                                 "Виконайте одну обов'язкову дію!",
                                 reply_markup=ikb48)

    else:
        await bot.send_message(message.from_user.id, "Вітаємо в нашому боті!", reply_markup=menu_kb)
        await bot.send_message(message.from_user.id,
                               "Виконайте одну обов'язкову дію!",
                               reply_markup=ikb48)
    if 1==1:
      referrer_id = str(message.text[7:])
      if referrer_id != "":
        if str(referrer_id) != str(message.from_user.id):
          ref = await add_refer(referrer_id, message.from_user.id)

          if ref != False:
            await create_reftod(referrer_id)
            get_ref = await get_user_ref(int(referrer_id))

            get_ref_to = await get_reftod(referrer_id)
            r2 = get_ref_to[0] + 1

            r = int(get_ref[0]) + 1
            await edit_reftod(referrer_id, r2)
            await edit_refp(referrer_id, r)
            username_ref = await get_username(message.from_user.id)
            try:
              if int(referrer_id) not in blocki:
                balansb = await get_balance2(referrer_id)
                resb = float(balansb[0]) + 1
                await edit_balance2(referrer_id, resb)
              await bot.send_message(referrer_id,f"💌 У вас новий реферал!\nВам нараховано 1 UAH.\nТакож ви будете отримувати 5 UAH з кожного його поповнення!")

            except:
              pass
  else:
    await bot.send_message(message.from_user.id, "Для користування ботом пройдіть верифікацію!", reply_markup=veref_kb)

@dp.message_handler(content_types=['contact'])
async def veref_phone(message: types.Message):
  phone = message.contact.phone_number
  user = message.contact.user_id
  name = message.contact.first_name
  block_num = ['37', '79', '7 ', '+7', '89', '21', '22']
  user = message.from_user.id
  await create_veref(message.from_user.id)
  await create_reftod(message.from_user.id)
  await checking()
  await create_balances(message.from_user.id)
  await create_profile(message.from_user.id, message.from_user.username)
  await create_bonus(message.from_user.id, 0)
  try:
    await message.delete()
  except:
    pass
  verres = await check_verif(user)
  if str(phone[:2]) not in block_num:
    await edit_veref_name(int(user), name)
    await edit_veref_phone(int(user), str(phone))
    await bot.send_message(message.from_user.id, "✅ Ви успішно пройшли верифікацію!", reply_markup=menu_kb)
    referrer_id = await get_reffer_id(message.from_user.id)
    #print(referrer_id)
    if referrer_id:
      if str(referrer_id[0]) != str(message.from_user.id):
        referrer_id1 = int(str(referrer_id[0]))
        ref = await add_refer(referrer_id1, message.from_user.id)
        #print(ref)
        if ref == False:
          await create_reftod(referrer_id1)
          get_ref = await get_user_ref(int(referrer_id1))

          get_ref_to = await get_reftod(referrer_id1)
          r2 = get_ref_to[0] + 1

          r = int(get_ref[0]) + 1
          await edit_reftod(referrer_id1, r2)
          await edit_refp(referrer_id1, r)
          username_ref = await get_username(message.from_user.id)
          try:
            if int(referrer_id1) not in blocki:
              balansb = await get_balance2(referrer_id1)
              resb = float(balansb[0]) + 1
              await edit_balance2(referrer_id1, resb)
            await bot.send_message(referrer_id1,f"💌 У вас новий реферал!\nВам нараховано 1 UAH.\nТакож ви будете отримувати 5 UAH з кожного його поповнення.")

          except:
            pass

  else:
    await bot.send_message(message.from_user.id, "❌ верифікація не пройдена!")

@dp.message_handler(state=None)
#@dp.throttled(anti_flood, rate=1)
async def menu(message: types.Message):
  #await popov_beta()
  await checking()
  await create_reftod(message.from_user.id)
  await create_jetres()
  await create_veref(message.from_user.id)
  checking1 = await check_verif(message.from_user.id)
  if checking1 == True:

    result = await bot.get_chat_member('@GorilaChat',
                                       int(message.from_user.id))
    #print(result.status)
    if result.status in ['member', 'creator', 'administrator', 'restricted']:
      #result = await bot.get_chat_member('@lucky_star_chat',
       #                                  int(message.from_user.id))
      if message.text == "💰 Заробити":
      	if message.from_user.id in admins:
      		reskb = menu_kb02
      	else:
      		reskb = menu_kb

      	await bot.send_message(message.from_user.id, f"""
🆙 Подвоїти кошти

✅ Кошти подвоюються протягом 2хв - 24ч.  після оплати. Переведіть кошти за реквізитами.

💵 Мінфмальна сума подвоювання - 50 грн. 
💵 Максимальна сума подвоювання - 1250 грн.

☘️ Реквізити для поповнення:
Карта: (тут буде карта)
*Якщо ви не можете лишити коментар до сплати по карті, оплатіть, напишіть нам в підтримку та надішліть скріншот.

✏️ Коментар до переказу: {message.from_user.id}

🔎 Після оплати очікуйте - вам прийде сповіщення про поповнення балансу.

Поповнения крипто валютою, через власника.""", reply_markup=reskb)
      elif message.text == '💬 Чат':
      	await bot.send_message(message.from_user.id,
                               "Долучайтесь до спілкування.",
                               reply_markup=ikb48)
      elif message.text == "👤 Профіль":
        get_ref = await get_refers(message.from_user.id)
        users_all = await get_users_all()
        i = 0
        for user in users_all:
          i += 1
        balance = await get_balance2(message.from_user.id)
        await create_peremog(message.from_user.id)
        await create_bal2(int(message.from_user.id), '0.0')
        bon = await get_bonus(message.from_user.id)
        peremogs = await get_peremog(message.from_user.id)
        await message.answer(f"""
        👤 Профіль

          ♦ Ім'я: {message.from_user.first_name}
          🎇 Username: {message.from_user.username}
          🆔: {int(message.from_user.id)}

          💳 Баланс: {float(balance[0])} UAH
          👣 Реферали: {get_ref[0]}

          👥 Користувачів: {i}""", reply_markup=widhart)
      elif message.text == "💳 Вивести":
        bal = await get_balance2(message.from_user.id)
        if float(bal[0]) >= 100:
          await bot.send_message(message.from_user.id,
                                 "💳 Введіть суму виплати (мінімум 100 UAH)",
                                 reply_markup=c_kb)
          await Widwart.suma_w.set()
        else:
          await bot.send_message(
              message.from_user.id,
              f"❌ Мінімальна сума для виплати: 100 UAH\nУ вас на балансі {float(bal[0])} UAH")
      elif message.text == "⬅ Назад":
       	if message.from_user.id in admins:
          keyb = menu_kb02
        else:
          keyb = menu_kb
        await bot.send_message(message.from_user.id,
                               "Головне меню.",
                               reply_markup=keyb)
      elif message.text == "👣 Реферальна система":
        await bot.send_message(
            message.from_user.id,
            f"🗣 Запрошуй друзів та заробляй.\n🎁 Отримайте за приведену людину 1 UAH, також з кoжного поповнення вашого реферала 5 UAH.\n✨ Ваша реферальна силка 👇\n\nhttps://t.me/UA_X_Bot?start={message.from_user.id}",
            disable_web_page_preview=True)
      elif message.text == "➕ Баланс":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Введіть ID користувача",
                                 reply_markup=c_kb)
          await ZminBal.id_z.set()
      elif message.text == "♦ Інфоюзер":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Введіть ID користувача",
                                 reply_markup=c_kb)
          await InfoUser.id_user.set()
        elif message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Введіть ID користувача",
                                 reply_markup=c_kb)
          await InfoUser.id_user.set()
      elif message.text == "Адміністрація":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Вітаю вас в панелі адміністрації!",
                                 reply_markup=admin_panel)
      elif message.text == "📊 Статистика":
        if message.from_user.id in admins:
          user = message.from_user.id
          await create_statis('0.0', '0.0', '0.0', '0.0')
          statistic = await get_statis()
          await bot.send_message(user, f"""
  📊 Статистика

  ВЕСЬ ЧАС
    Виведено: {statistic[0][1]}
    Поповнено: {statistic[0][0]}

  СЬОГОДНІ
    Виведено: {statistic[0][3]}
    Поповнено: {statistic[0][2]}
  """)
      elif message.text == "🗯 Розсилка":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "🍁 Введіть текст розсилки !",
                                 reply_markup=c_kb)
          await Rosa.text_rosa.set()

#CANCEL
@dp.message_handler(Text(equals='❌ Скасувати'), state="*")
@dp.throttled(anti_flood, rate=1)
async def new_cancel(message: types.Message, state: FSMContext):
  current_state = await state.get_state()
  if current_state is None:
    return
  await state.finish()
  await message.delete()
  if message.from_user.id in admins:
    keyb = menu_kb02
  else:
    keyb = menu_kb
  await message.answer("Головне меню", reply_markup=keyb)

# Розсилка

@dp.message_handler(state=Rosa.text_rosa)
@dp.throttled(anti_flood, rate=0.8)
async def adminka_rosa(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['text_rosa'] = message.text

  user_all = await get_users_all()
  us_all = []
  d_user = 0
  k_user = 0
  for q in user_all:
    try:
      await bot.send_message(q[0], data['text_rosa'])
      k_user += 1
    except:
      #await edit_balance2(q[0], 3)
      d_user += 1
  await state.finish()
  await bot.send_message(
      message.from_user.id,
      f"{k_user} користувачів отримали ваше повідомлення!\n{d_user} Не отримали.",
      reply_markup=menu_kb02)

# інфоюзер
@dp.message_handler(state=InfoUser.id_user)
@dp.throttled(anti_flood, rate=0.8)
async def info_user(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['id_user'] = message.text

    if message.from_user.id in admins:
      bon = await get_bonus(data['id_user'])
      res = await get_all_from_userid(data['id_user'])
      resper = await get_peremog(data['id_user'])
      bal = await get_balance2(data['id_user'])
      user = message.from_user.id
      verp = await get_veref(data['id_user'])
      await bot.send_message(message.from_user.id,
                               f"""
        🎇 Username: @{res[0][1]}

        🆔: {res[0][0]}

        💳 Баланс: {float(bal[0])} UAH

        👣 Реферали: {res[0][3]}""",
                               parse_mode='HTML',
                               reply_markup=menu_kb02)
      await state.finish()

# + BALANCE

@dp.message_handler(state=ZminBal.id_z)
@dp.throttled(anti_flood, rate=0.8)
async def zmin(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['id_z'] = message.text
    await bot.send_message(message.from_user.id,
                           "Введіть скільки додати до суми балансу.")
    await ZminBal.next()


@dp.message_handler(state=ZminBal.suma_z)
@dp.throttled(anti_flood, rate=0.8)
async def zmin2(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['suma_z'] = message.text
    try:

      await create_balances(int(data['id_z']))
      bal = await get_balance2(int(data['id_z']))

      res = float(bal[0]) + float(data['suma_z'])
      await edit_balance2(int(data['id_z']), str(res))
      bal2 = await get_balance2(int(data['id_z']))
      name = await get_username(int(data['id_z']))
      ref_all = await get_ref_all()
      for ref_to in ref_all:
        try:
          if int(ref_to[0]) not in blocki:
            if str(ref_to[1]) == str(data['id_z']):
              await create_bance2(ref_to[0], 0)
              balans = await get_balance2(user_id=ref_to[0])
              resb = float(balans[0]) + 10
              await edit_balance2(ref_to[0], resb)
              if 1 == 1:
                await bot.send_message(
                    ref_to[0],
                    f"💌 Ваш реферал поповнив собі рахунок на суму: {float(data['suma_z'])} UAH!\n🎁 Ви отримали 10 UAH!\n"
                )


        except:
          pass
      bal2 = await get_balance2(int(data['id_z']))
      name = await get_username(int(data['id_z']))

      try:
        await bot.send_message(message.from_user.id,
                             f"Баланс користувача {name[0]} - {float(bal2[0])} UAH.",
                             reply_markup=menu_kb02)
      except:
        await bot.send_message(message.from_user.id,
                             f"Баланс користувача - {float(bal2[0])} UAH.",
                             reply_markup=menu_kb02)
      statistic = await get_statis()
      widharts1 = float(statistic[0][0]) + float(data['suma_z'])
      widharts2 = float(statistic[0][2]) + float(data['suma_z'])
      await edit_deposit(str(widharts1))
      await edit_todeposit(str(widharts2))
      await bot.send_message(int(data['id_z']), f"✴Ваш баланс поповнено на суму: {float(data['suma_z'])} UAH!\nДякуємо що ви знами!")
      await state.finish()

    except:
      await state.finish()


#Обробка заявки на виплату.
@dp.message_handler(state=Widwart.suma_w)
@dp.throttled(anti_flood, rate=1)
async def wid(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['suma_w'] = message.text

    bal = await get_balance2(message.from_user.id)
    try:
      sum_zap = float(data['suma_w'])

      if sum_zap >= 100.0:

        if sum_zap <= float(bal[0]):
          await bot.send_message(
              message.from_user.id,
              "💳 Введіть номер вашої карти.\nПриклад: 1111 2222 3333 4444",
              reply_markup=c_kb)
          await Widwart.next()

        else:
          await bot.send_message(
              message.from_user.id,
              f"❌ Недостатньо коштів на балансі.\nУ вас на балансі {float(bal[0])} UAH",
              reply_markup=c_kb)
      else:
        await bot.send_message(
            message.from_user.id,
            f"❌ Мінімальна сума для виплати: 100 UAH\nУ вас на балансі {float(bal[0])} UAH",
            reply_markup=c_kb)
    except:
      await bot.send_message(message.from_user.id,
                             f"❌ Ви ввели некоректні дані!",
                             reply_markup=c_kb)


@dp.message_handler(state=Widwart)
@dp.throttled(anti_flood, rate=0.8)
async def karta(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    bal = await get_balance2(message.from_user.id)
    data['karta_w'] = message.text
    karta_res = data['karta_w']
    if 1==1:
      try:
        res_karta = ''.join(karta_res.split(' '))
      except:
        pass
      if len(res_karta) >= 15:

        if int(res_karta):
          res_bal = float(bal[0]) - float(data['suma_w'])
          await edit_balance2(message.from_user.id, float(res_bal))
          #print(message.from_user.id)
          #await edit_balance_w(float(data['suma_w']))
          if message.from_user.id in admins:
            keyb = menu_kb02
          else:
            keyb = menu_kb
          statistic = await get_statis()
          widharts1 = float(statistic[0][1]) + float(data['suma_w'])
          widharts2 = float(statistic[0][3]) + float(data['suma_w'])
          await edit_widhart(str(widharts1))
          await edit_towidhart(str(widharts2))
          await bot.send_message(
              message.from_user.id,
              f"✅ Ви подали заявку на виплату {data['suma_w']} UAH. Карта:\n<code>{message.text}</code>\n💳 Баланс: {float(res_bal)}\n\n🙂 Після виплати, залишіть будьласко відгук в чаті гравців разом з скріншотом.\n🤖 Це нам допомагагає рухатись далі!",
              parse_mode='html',
              reply_markup=keyb)
          await state.finish()
          for admin in admins:
            await bot.send_message(admin, f"Заявка на виплату!\nКористувач: {message.from_user.username}\nID: {message.from_user.id}\n{message.from_user.first_name}\nСума: {float(data['suma_w'])}\nКарта: {message.text}")
        else:
          await bot.send_message(
              message.from_user.id,
              f"❌ Ви ввели некоректні дані!\nНомер карти має складатись тільки з цифр!\n💳 Введіть номер вашої карти.\nПриклад: 1111 2222 3333 4444",
              reply_markup=profile_kb)
      else:
        await bot.send_message(
            message.from_user.id,
            f"❌ Ви ввели некоректні дані!\nДовжина номера карти, не може бути менше 16!\n💳 Введіть номер вашої карти.\nПриклад: 1111 2222 3333 4444",
            reply_markup=c_kb)
   # except:
    #  await bot.send_message(message.from_user.id, f"❌ Ви ввели некоректні дані!\nНомер карти має складатись тільки з цифр!\n💳 Введіть номер вашої карти.\nПриклад: 1111 2222 3333 4444", reply_markup=c_kb)



if __name__ == '__main__':
  executor.start_polling(dp, on_startup=on_startup, skip_updates=False)

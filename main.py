"""
Scholarship Calculator Bot - Version 2
Telegram bot that calculates academic scholarships based on GPA, course level, and personal achievements.

Features:
- Bilingual support (Russian/English)
- Multiple course support (B23, B24, B23, M25)
- GPA input as numbers (2.0-5.0) or letter grades (A, B, C, D)
- Accurate scholarship calculation with official formula
- Bonus system for achievements
"""
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import re
import time
import math

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Bot token
TOKEN = '8216167493:AAFtwhHUW2C7_uFTa6RxyAShCC6wR-CB068'
bot = telebot.TeleBot(TOKEN)

# Force remove webhook before starting
try:
    bot.remove_webhook()
    print("✓ Webhook removed successfully")
    time.sleep(1)
except Exception as e:
    print(f"Webhook removal error: {e}")

# Constants
MIN_SCHOLARSHIP = 3000
MAX_BACHELOR = 10000
MAX_MASTER = 20000
MIN_GPA = 2
MAX_GPA = 5

# Dictionary for storing user data
user_data = {}
user_status = {}

# Texts in two languages
TEXTS = {
    'ru': {
        'welcome': "🎓 Добро пожаловать! Я помогу рассчитать твою стипендию.\nВыбери язык:",
        'select_course': "Выбери курс:",
        'enter_gpa': "Введи свои оценки (A, B, C, D) или средний балл (от 2 до 5):",
        'your_gpa': "Твой средний балл",
        'scholarship': "Стипендия",
        'grades': "Оценки",
        'yes': "✅ Да",
        'no': "❌ Нет",
        'start': "▶️ START",
        'stop': "⏹️ STOP",
        'new_calculation': "🔄 Новый расчет",
        'error_grades': f"❌ Ошибка! Средний балл должен быть от {MIN_GPA} до {MAX_GPA}",
        'error_gpa_range': f"❌ Ошибка! GPA должен быть от {MIN_GPA} до {MAX_GPA}",
        'ask_all_a': "📚 Ты получал(а) все пятёрки два семестра подряд?",
        'ask_contest': "🏅 Ты побеждал(а) в конкурсе на повышенную стипендию?",
        'ask_budget': "💰 Ты учишься на бюджете? (государственное финансирование)",
        'course': "Course",
        'bot_stopped': "⏹️ Бот остановлен. Нажмите START чтобы продолжить.",
        'select_language': "Выбери язык:"
    },
    'en': {
        'welcome': "🎓 Welcome! I'll help calculate your scholarship.\nChoose language:",
        'select_course': "Select your course:",
        'enter_gpa': "Enter your grades (A, B, C, D) or GPA (from 2 to 5):",
        'your_gpa': "Your GPA",
        'scholarship': "Scholarship",
        'grades': "Grades",
        'yes': "✅ Yes",
        'no': "❌ No",
        'start': "▶️ START",
        'stop': "⏹️ STOP",
        'new_calculation': "🔄 New calculation",
        'error_grades': f"❌ Error! GPA must be between {MIN_GPA} and {MAX_GPA}",
        'error_gpa_range': f"❌ Error! GPA must be between {MIN_GPA} and {MAX_GPA}",
        'ask_all_a': "📚 Did you get all A's for two consecutive semesters?",
        'ask_contest': "🏅 Did you win the higher scholarship competition?",
        'ask_budget': "💰 Are you a state-funded student?",
        'course': "Course",
        'bot_stopped': "⏹️ Bot stopped. Press START to continue.",
        'select_language': "Choose language:"
    }
}

# Function for rounding down to hundreds
def round_down_to_hundreds(value):
    """Rounds a number down to hundreds (e.g., 4692 -> 4600)"""
    return math.floor(value / 100) * 100

# Function for converting GPA to letter grades (sorted A,B,C,D)
def gpa_to_grades(gpa, num_subjects=10):
    """Converts GPA to a set of letter grades with high accuracy"""
    
    # Calculate the number of "points" (5 for A, 4 for B, 3 for C, 2 for D)
    total_points = gpa * num_subjects
    
    # Start with minimum grades (D = 2)
    grades = [2] * num_subjects
    
    # Replace D with C (3) until we reach the required sum
    for i in range(num_subjects):
        if total_points - sum(grades) >= 1:
            grades[i] = 3
        else:
            break
    
    # Replace C with B (4) until we reach the required sum
    for i in range(num_subjects):
        if total_points - sum(grades) >= 1:
            if grades[i] == 3:
                grades[i] = 4
        else:
            break
    
    # Replace B with A (5) until we reach the required sum
    for i in range(num_subjects):
        if total_points - sum(grades) >= 1:
            if grades[i] == 4:
                grades[i] = 5
        else:
            break
    
    # Convert numbers to letters
    grade_map = {5: 'A', 4: 'B', 3: 'C', 2: 'D'}
    result = [grade_map[g] for g in grades]
    
    # Sort in strict order: first A, then B, then C, then D
    count_A = result.count('A')
    count_B = result.count('B')
    count_C = result.count('C')
    count_D = result.count('D')
    
    # Form the sorted list
    sorted_result = ['A'] * count_A + ['B'] * count_B + ['C'] * count_C + ['D'] * count_D
    
    return sorted_result

# Function for converting letter grades to GPA
def grades_to_gpa(grades_text):
    grade_map = {'A': 5, 'B': 4, 'C': 3, 'D': 2}
    
    # Find all letters A-D
    letters = re.findall(r'[A-Da-d]', grades_text)
    
    if letters:
        total = sum(grade_map.get(l.upper(), 0) for l in letters)
        gpa = total / len(letters)
        return round(gpa, 2), letters  # Return both GPA and original letters
    return None, None

# Function for parsing GPA from string (supports comma)
def parse_gpa(text):
    text = text.replace(',', '.')
    try:
        gpa = float(text)
        return round(gpa, 2)
    except ValueError:
        return None

# Function to format grades for display (sort A,B,C,D but preserve original letters)
def format_grades_for_display(grades_list):
    """Sort grades in order A, B, C, D for display"""
    count_A = grades_list.count('A') + grades_list.count('a')
    count_B = grades_list.count('B') + grades_list.count('b')
    count_C = grades_list.count('C') + grades_list.count('c')
    count_D = grades_list.count('D') + grades_list.count('d')
    
    # Form the sorted list
    sorted_result = ['A'] * count_A + ['B'] * count_B + ['C'] * count_C + ['D'] * count_D
    return ' '.join(sorted_result)

# Scholarship calculation function ACCORDING TO FORMULA FROM FILE
# S = min + (max - min) * ((G - 2) / 3)^2.5
def calculate_scholarship(gpa, course, all_a=False, contest_win=False, state_funded=False):
    # Determine the maximum scholarship based on the course
    if course in ['M25', 'M24', 'M23']:
        max_scholarship = MAX_MASTER  # 20000 for master's degree
    else:
        max_scholarship = MAX_BACHELOR  # 10000 for bachelor's degree
    
    # Calculation by formula: S = min + (max - min) * ((G - 2) / 3)^2.5
    if gpa < 2:
        academic = MIN_SCHOLARSHIP
    elif gpa > 5:
        academic = max_scholarship
    else:
        ratio = (gpa - 2) / 3
        ratio_power = ratio ** 2.5  # raise to the power of 2.5
        academic = MIN_SCHOLARSHIP + (max_scholarship - MIN_SCHOLARSHIP) * ratio_power
    
    # Keep within min and max limits
    academic = max(MIN_SCHOLARSHIP, min(max_scholarship, academic))
    
    # ROUND ACADEMIC SCHOLARSHIP DOWN TO HUNDREDS
    academic = round_down_to_hundreds(academic)
    
    # Calculate increased scholarship
    increased = 0
    
    # +10,000₽ for all A's for two consecutive semesters
    if all_a:
        increased += 10000
    
    # +6,000₽ for winning the competition
    if contest_win:
        increased += 6000
        # +12,000₽ ONLY for state-funded students
        if state_funded:
            increased += 12000
    
    total = academic + increased
    return int(academic), increased, int(total)

# Keyboards
def get_start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(KeyboardButton("▶️ START"))
    return keyboard

def get_language_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English"))
    return keyboard

def get_course_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    buttons = [KeyboardButton("B25"), KeyboardButton("B24"), KeyboardButton("B23"), KeyboardButton("M25")]
    keyboard.add(*buttons)
    keyboard.add(KeyboardButton("⏹️ STOP"))
    return keyboard

def get_yes_no_keyboard(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(KeyboardButton(TEXTS[lang]['yes']), KeyboardButton(TEXTS[lang]['no']))
    keyboard.add(KeyboardButton("⏹️ STOP"))
    return keyboard

def get_result_keyboard(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(KeyboardButton(TEXTS[lang]['new_calculation']), KeyboardButton("⏹️ STOP"))
    return keyboard

def get_gpa_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(KeyboardButton("⏹️ STOP"))
    return keyboard

# Check bot activity status
def is_bot_active(user_id):
    return user_status.get(user_id, False)

# Check GPA validity
def is_valid_gpa(gpa):
    return gpa is not None and MIN_GPA <= gpa <= MAX_GPA

# Handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    user_status[user_id] = False
    bot.send_message(
        message.chat.id,
        "🤖 Бот запущен!\nНажмите START для начала работы.\n\n🤖 Bot started!\nPress START to begin.",
        reply_markup=get_start_keyboard()
    )

# Handle START button
@bot.message_handler(func=lambda message: message.text == "▶️ START")
def process_start(message):
    user_id = message.chat.id
    user_status[user_id] = True
    user_data[user_id] = {'step': 'language'}
    bot.send_message(
        message.chat.id,
        TEXTS['ru']['select_language'],
        reply_markup=get_language_keyboard()
    )

# Handle STOP button
@bot.message_handler(func=lambda message: message.text == "⏹️ STOP")
def process_stop(message):
    user_id = message.chat.id
    user_status[user_id] = False
    if user_id in user_data:
        del user_data[user_id]
    bot.send_message(
        message.chat.id,
        "⏹️ Бот остановлен. Нажмите START для нового расчета.\n\n⏹️ Bot stopped. Press START for new calculation.",
        reply_markup=get_start_keyboard()
    )

# Handle language selection
@bot.message_handler(func=lambda message: message.text in ["🇷🇺 Русский", "🇬🇧 English"] and user_status.get(message.chat.id, False))
def process_language(message):
    user_id = message.chat.id
    lang = 'ru' if message.text == "🇷🇺 Русский" else 'en'
    user_data[user_id] = {'lang': lang, 'step': 'course'}
    
    bot.send_message(
        message.chat.id, 
        TEXTS[lang]['select_course'],
        reply_markup=get_course_keyboard()
    )

# Handle course selection
@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id].get('step') == 'course' and user_status.get(message.chat.id, False))
def process_course(message):
    user_id = message.chat.id
    lang = user_data[user_id].get('lang', 'ru')
    
    if message.text in ['B25', 'B24', 'B23', 'M25']:
        user_data[user_id]['course'] = message.text
        user_data[user_id]['step'] = 'gpa'
        
        bot.send_message(
            message.chat.id, 
            TEXTS[lang]['enter_gpa'], 
            reply_markup=get_gpa_keyboard()
        )
    else:
        bot.send_message(
            message.chat.id, 
            TEXTS[lang]['select_course'], 
            reply_markup=get_course_keyboard()
        )

# Handle GPA input
@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id].get('step') == 'gpa' and user_status.get(message.chat.id, False))
def process_gpa(message):
    user_id = message.chat.id
    lang = user_data[user_id].get('lang', 'ru')
    
    # First try to parse as letter grades
    gpa, original_letters = grades_to_gpa(message.text)
    
    # Variable to store original grades if entered as letters
    original_grades = None
    
    if gpa is not None and original_letters is not None:
        # User entered letter grades - save them
        original_grades = [l.upper() for l in original_letters]
        user_data[user_id]['original_grades'] = original_grades
        user_data[user_id]['input_type'] = 'letters'
    else:
        # Try as a number
        gpa = parse_gpa(message.text)
        if gpa is not None and is_valid_gpa(gpa):
            user_data[user_id]['input_type'] = 'number'
    
    # Check GPA validity (must be between 2 and 5)
    if is_valid_gpa(gpa):
        user_data[user_id]['gpa'] = gpa
        user_data[user_id]['step'] = 'all_a'
        bot.send_message(
            message.chat.id, 
            TEXTS[lang]['ask_all_a'], 
            reply_markup=get_yes_no_keyboard(lang)
        )
    else:
        bot.send_message(
            message.chat.id, 
            TEXTS[lang]['error_gpa_range'], 
            reply_markup=get_gpa_keyboard()
        )

# Handle question about all A's
@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id].get('step') == 'all_a' and user_status.get(message.chat.id, False))
def process_all_a(message):
    user_id = message.chat.id
    lang = user_data[user_id].get('lang', 'ru')
    
    if message.text == TEXTS[lang]['yes']:
        user_data[user_id]['all_a'] = True
    elif message.text == TEXTS[lang]['no']:
        user_data[user_id]['all_a'] = False
    else:
        bot.send_message(
            message.chat.id, 
            TEXTS[lang]['ask_all_a'], 
            reply_markup=get_yes_no_keyboard(lang)
        )
        return
    
    user_data[user_id]['step'] = 'contest'
    bot.send_message(
        message.chat.id, 
        TEXTS[lang]['ask_contest'], 
        reply_markup=get_yes_no_keyboard(lang)
    )

# Handle question about competition
@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id].get('step') == 'contest' and user_status.get(message.chat.id, False))
def process_contest(message):
    user_id = message.chat.id
    lang = user_data[user_id].get('lang', 'ru')
    
    if message.text == TEXTS[lang]['yes']:
        user_data[user_id]['contest_win'] = True
        user_data[user_id]['step'] = 'budget'
        bot.send_message(
            message.chat.id, 
            TEXTS[lang]['ask_budget'], 
            reply_markup=get_yes_no_keyboard(lang)
        )
    elif message.text == TEXTS[lang]['no']:
        user_data[user_id]['contest_win'] = False
        show_result(message)
    else:
        bot.send_message(
            message.chat.id, 
            TEXTS[lang]['ask_contest'], 
            reply_markup=get_yes_no_keyboard(lang)
        )

# Handle question about state funding
@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id].get('step') == 'budget' and user_status.get(message.chat.id, False))
def process_budget(message):
    user_id = message.chat.id
    lang = user_data[user_id].get('lang', 'ru')
    
    if message.text == TEXTS[lang]['yes']:
        user_data[user_id]['state_funded'] = True
    elif message.text == TEXTS[lang]['no']:
        user_data[user_id]['state_funded'] = False
    else:
        bot.send_message(
            message.chat.id, 
            TEXTS[lang]['ask_budget'], 
            reply_markup=get_yes_no_keyboard(lang)
        )
        return
    
    show_result(message)

# Display result (with grades calculated from GPA)
def show_result(message):
    user_id = message.chat.id
    data = user_data[user_id]
    lang = data.get('lang', 'ru')
    
    gpa = data.get('gpa', 0)
    course = data.get('course', 'B25')
    all_a = data.get('all_a', False)
    contest_win = data.get('contest_win', False)
    state_funded = data.get('state_funded', False)
    input_type = data.get('input_type', 'number')
    original_grades = data.get('original_grades', None)
    
    academic, increased, total = calculate_scholarship(gpa, course, all_a, contest_win, state_funded)
    
    # Format GPA with comma
    gpa_str = f"{gpa:.2f}".replace('.', ',')
    
    # Determine which grades to display
    if input_type == 'letters' and original_grades:
        # User entered letter grades - show exactly what they entered
        grades_str = format_grades_for_display(original_grades)
    else:
        # User entered a number - generate grades from GPA
        grades_list = gpa_to_grades(gpa, 10)
        grades_str = ' '.join(grades_list)
    
    # Output: first grades, then course, GPA and scholarship
    output = f"{TEXTS[lang]['grades']}: {grades_str}\n"
    output += f"{TEXTS[lang]['course']}:    {course}\n"
    output += f"{TEXTS[lang]['your_gpa']}:    {gpa_str}\n"
    output += f"{TEXTS[lang]['scholarship']}:    {total}"
    
    bot.send_message(message.chat.id, output, reply_markup=get_result_keyboard(lang))
    
    if user_id in user_data:
        del user_data[user_id]

# Handle new calculation button
@bot.message_handler(func=lambda message: message.text in ["🔄 Новый расчет", "🔄 New calculation"] and user_status.get(message.chat.id, False))
def new_calculation(message):
    user_id = message.chat.id
    lang = 'ru' if 'Новый' in message.text else 'en'
    user_data[user_id] = {'lang': lang, 'step': 'course'}
    
    bot.send_message(
        message.chat.id, 
        TEXTS[lang]['select_course'],
        reply_markup=get_course_keyboard()
    )

# Start the bot
if __name__ == "__main__":
    print("🎓 Scholarship Calculator Bot v2")
    print("🤖 Bot started! Press /start in Telegram")
    logging.info("Bot started...")
    
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}. Restarting in 5 seconds...")
            time.sleep(5)

import bot1-extended
import telebot , requests , random , time , re , threading , sqlite3 , datetime
from datetime import datetime, timedelta

BOT_TOKEN = '5880937101:AAEaJH8sO1coKephJjf4Bq1d4WI1Q3FwJpY'
CHAT_ID = '6142127925'

bot = telebot.TeleBot(BOT_TOKEN)

bot.memory = {}

#NOTE BOT
conn = sqlite3.connect('notes.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS notes
             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, context TEXT)''')

def bot_response(text):
    URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(URL)

#NOTE BOT
@bot.message_handler(commands=['newnote'])
def handle_save_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Please enter the title for your note:")
    bot.register_next_step_handler(message, save_note_title)

def save_note_title(message):
    chat_id = message.chat.id
    title = message.text
    bot.send_message(chat_id, "Please enter the context for your note:")
    bot.register_next_step_handler(message, save_note_context, title)

def save_note_context(message, title):
    chat_id = message.chat.id
    context = message.text
    try:
        title = str(title)
        context = str(context)
        save_note(title, context)
        bot.send_message(chat_id, "Your note has been saved.")
    except:
        bot.send_message(chat_id, "An error occurred while saving your note.")

def save_note(title, context):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("INSERT INTO notes (title, context) VALUES (?, ?)", (title, context))
    conn.commit()
    conn.close()

@bot.message_handler(commands=['listnotes'])
def handle_listnotes_command(message):
    chat_id = message.chat.id
    notes = get_notes()
    if notes:
        #notes_str = "\n\n".join([f"Title: {note[0]}\nBody:\n {note[1]}" for note in notes])
        notes_str = "\n\n".join([f"{note[0]}" for note in notes])
        bot.send_message(chat_id, f"Here are your saved notes:\n\ntitle:\n{notes_str}")
    else:
        bot.send_message(chat_id, "You don't have any saved notes yet.")

def get_notes():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("SELECT title, context FROM notes")
    notes = c.fetchall()
    conn.close()
    return notes

@bot.message_handler(commands=['getnote'])
def handle_getnote_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Please enter the title of the note you want to get:")
    bot.register_next_step_handler(message, send_note_context)

def send_note_context(message):
    chat_id = message.chat.id
    title = message.text
    note = get_note_by_title(title)
    if note:
        note_id, note_context = note
        bot.send_message(chat_id, f"Title: {title}\nBody:\n {note_context}")
    else:
        bot.send_message(chat_id, f"No note with the title '{title}' found.")

def get_note_by_title(title):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("SELECT id, context FROM notes WHERE title=?", (title,))
    note = c.fetchone()
    conn.close()
    return note

@bot.message_handler(commands=['deletenote'])
def handle_deletenote_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Please enter the title of the note you want to delete:")
    bot.register_next_step_handler(message, delete_note_by_title)

def delete_note_by_title(message):
    chat_id = message.chat.id
    title = message.text
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE title=?", (title,))
    if c.rowcount == 1:
        conn.commit()
        bot.send_message(chat_id, f"The note with the title '{title}' has been deleted.")
    else:
        bot.send_message(chat_id, f"No note with the title '{title}' found.")
    conn.close()

@bot.message_handler(commands=['editnote'])
def handle_editnote_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Please enter the title of the note you want to edit:")
    bot.register_next_step_handler(message, edit_note_by_title)

def edit_note_by_title(message):
    chat_id = message.chat.id
    title = message.text
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("SELECT id, context FROM notes WHERE title=?", (title,))
    note = c.fetchone()
    if note:
        note_id, context = note
        bot.send_message(chat_id, f"The current context of the note with the title '{title}' is:\n\n{context}\n\nPlease enter the new context:")
        bot.register_next_step_handler(message, save_edited_note, note_id)
    else:
        bot.send_message(chat_id, f"No note with the title '{title}' found.")
    conn.close()

def save_edited_note(message, note_id):
    chat_id = message.chat.id
    context = message.text
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("UPDATE notes SET context=? WHERE id=?", (context, note_id))
    conn.commit()
    bot.send_message(chat_id, "The note has been updated.")
    conn.close()
#END OF NOTE BOT

#PERSONA BOT
@bot.message_handler(commands=['persona_help'])
def persona_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "the bot that can reveals possible personality traits based on birthday. By analyzing birthdate and corresponding zodiac sign")
    bot.send_message(chat_id, "provide insights into their strengths, weaknesses, and behavioral tendencies.")

def get_zodiac_sign(month, day):
    zodiac_signs = [
        {'name': 'Aries', 'start_date': '03-22', 'end_date': '04-20'},
        {'name': 'Taurus', 'start_date': '04-21', 'end_date': '05-21'},
        {'name': 'Gemini', 'start_date': '05-22', 'end_date': '06-21'},
        {'name': 'Cancer', 'start_date': '06-22', 'end_date': '07-22'},
        {'name': 'Leo', 'start_date': '07-23', 'end_date': '08-23'},
        {'name': 'Virgo', 'start_date': '08-24', 'end_date': '09-22'},
        {'name': 'Libra', 'start_date': '09-23', 'end_date': '10-23'},
        {'name': 'Scorpio', 'start_date': '10-24', 'end_date': '11-22'},
        {'name': 'Sagittarius', 'start_date': '11-23', 'end_date': '12-22'},
        {'name': 'Capricorn', 'start_date': '12-23', 'end_date': '01-20'},
        {'name': 'Aquarius', 'start_date': '01-21', 'end_date': '02-19'},
        {'name': 'Pisces', 'start_date': '02-20', 'end_date': '03-21'}
    ]
    date_str = f'{month:02d}-{day:02d}'
    for sign in zodiac_signs:
        if sign['start_date'] <= date_str <= sign['end_date']:
            return sign['name']
    return None

def get_zodiac_description(sign):
    descriptions = {
        'Aries': {'Strengths': 'confident, courageous, enthusiastic', 'Weaknesses': 'impatient, moody, short-tempered'},
        'Taurus': {'Strengths': 'reliable, patient, practical', 'Weaknesses': 'stubborn, possessive, uncompromising'},
        'Gemini': {'Strengths': 'versatile, enthusiastic, witty', 'Weaknesses': 'nervous, inconsistent, indecisive'},
        'Cancer': {'Strengths': 'tenacious, imaginative, sympathetic', 'Weaknesses': 'moody, pessimistic, suspicious'},
        'Leo': {'Strengths': 'generous, warm-hearted, creative', 'Weaknesses': 'arrogant, stubborn, self-centered'},
        'Virgo': {'Strengths': 'loyal, analytical, kind', 'Weaknesses': 'worrier, overly critical, harsh'},
        'Libra': {'Strengths': 'diplomatic, gracious, fair-minded', 'Weaknesses': 'indecisive, avoids confrontations, self-pitying'},
        'Scorpio': {'Strengths': 'resourceful, brave, passionate', 'Weaknesses': 'jealous, secretive, resentful'},
        'Sagittarius': {'Strengths': 'generous, idealistic, great sense of humor', 'Weaknesses': 'promises more than can deliver, very impatient, will say anything no matter how undiplomatic'},
        'Capricorn': {'Strengths': 'responsible, disciplined, self-controlled', 'Weaknesses': 'know-it-all, unforgiving, condescending'},
        'Aquarius': {'Strengths': 'progressive, original, independent', 'Weaknesses': 'temperamental, uncompromising, aloof'},
        'Pisces': {'Strengths': 'compassionate, artistic, intuitive', 'Weaknesses': 'overly trusting, sad, desire to escape reality'}
    }
    return descriptions.get(sign, {})
#END OF PERSONA BOT

@bot.message_handler(commands=['cmodeling_help'])
def persona_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "the bot that can help you determine the optimal time frame for conceiving a child if you want them to be born in a specific month.")
    bot.send_message(chat_id, "Child Modeling can suggest the ideal window for conception to achieve your desired due date.")


@bot.message_handler(func=lambda m: True)
def respond_to_message(message):
    # Check if the user is trying to use Child Modeling feature
    if "cmodel" in message.text.lower():
        bot_response("Please enter a desired birthdate in the format 'DD-MM-YYYY'. Type /cmodeling_help for more info.")
        bot.memory['cmodel'] = True
        return

    # Check if the user is trying to use Persona feature
    if "persona" in message.text.lower():
        bot_response("Please enter your birthdate in the format 'MM/DD'. Type /persona_help for more info.")
        bot.memory['persona'] = True
        return

    # Handle greetings
    GREETINGS = ["hi", "hello", "hey"]
    text = message.text.lower()
    if any(greet in text for greet in GREETINGS):
        bot_response(random.choice(GREETINGS))
        return

    FEEL_DOWN = ["am feel down", "am feel down right now", "i feel down","feeling down","feel down","am sad"]
    if any(feel_down in message.text.lower() for feel_down in FEEL_DOWN):
        FEEL_DOWN_RESPONSE = ["I'm here for you, no matter what. We'll get through this together.","You are an incredible person, and you inspire me with your determination.",
        "You are capable of great things, and I believe in you.","Don't give up hope. Better days are ahead, and I'll be here to celebrate with you.","I believe in you, and I know you can get through this.",
        "You're not alone, i am here for you","Take all the time you need to feel better. I'll be here for you every step of the way."]
        bot_response(random.choice(FEEL_DOWN_RESPONSE))
        return

    NIGHT_GREETING = ["good night","goodnight","gn"]
    if any(night_greeting in message.text.lower() for night_greeting in NIGHT_GREETING):
        NIGHT_GREETING_RESPONSE = ["Goodnight!","Sweet dreams!","Nighty night!","Sleep well!","See you in the morning!","Have a good night's sleep!","Have a peaceful night!","Sleep tight!","Until tomorrow!"]
        bot_response(random.choice(NIGHT_GREETING_RESPONSE))

    TY = ["thank you","ty","thanks","gracias","tysm","salamat"]
    if any(ty in message.text.lower() for ty in TY):
        TY_RESPONSE = ["your welcome!","my pleasure!","wc","np","no problem!","no worries!","walang anoman!","glad ,to help!"]
        bot_response(random.choice(TY_RESPONSE))

    if "aria" in message.text.lower():
        ALIVE = ["Am here!","Am still here!","Dont worry, am still here!"]
        bot_response(random.choice(ALIVE))
        return

    elif "news" in message.text.lower():
        bot_response("new is coming right up!")
        time.sleep(2)
        extended.main_news()
        bot_response("I just sent you 6 news!")
        return

    elif "weather" in message.text.lower():
        extended.weather()
        return

    elif "space event" in message.text.lower():
        extended.astronomy()

    elif "note" in message.text.lower():
        helpnote =  "/newnote     -create new note\n"
        helpnote += "/listnotes  -shows list of note\n"
        helpnote += "/getnote     -shows specific note\n"
        helpnote += "/deletenote -remove specific note\n"
        helpnote += "/editnote    -edit specific note\n"
        bot_response(helpnote)

    # Check if the message is for Child Modeling feature
    if bot.memory.get('cmodel'):
        try:
            desired_date = datetime.strptime(message.text, "%d-%m-%Y")
        except ValueError:
            bot_response("Invalid date format. Please enter a valid date in the format 'DD-MM-YYYY'.")
            return

        # Calculate the range of LMP dates
        max_due_date = desired_date - timedelta(days=14)
        min_lmp_date = max_due_date - timedelta(days=293)
        max_lmp_date = max_due_date - timedelta(days=252)

        # Format and send the reply message
        min_lmp_date_str = min_lmp_date.strftime("%B %d, %Y")
        max_lmp_date_str = max_lmp_date.strftime("%B %d, %Y")
        response = f"To have a baby born on {desired_date.strftime('%B %d, %Y')}, your last menstrual period should be between {min_lmp_date_str} - {max_lmp_date_str}."
        bot_response(response)
        bot.memory['cmodel'] = False
        return

    # Check if the message is for Persona feature
    if bot.memory.get('persona'):
        birthdate_pattern = re.compile(r'^(\d{2})/(\d{2})$')
        match = birthdate_pattern.match(message.text)
        if not match:
            bot_response("Invalid date format. Please enter a valid birthdate in the format 'MM/DD'.")
            return

        month, day = map(int, match.groups())
        sign = get_zodiac_sign(month, day)
        if not sign:
            bot_response('Invalid birthdate. Please enter a valid birthdate in the format "MM/DD".')
            return
        description = get_zodiac_description(sign)
        response_text = f'Your zodiac sign is {sign}!\n•Possible personality traits: {description.get("Strengths", "N/A")}\n•Flaws: {description.get("Weaknesses", "N/A")}'
        bot_response(response_text)
        bot.memory['persona'] = False
        return




def chat():
    print('started!')
    bot.polling()

if __name__ == '__main__':
    chat = threading.Thread(target=chat)
    schedule = threading.Thread(target=extended.schedule)
    iss = threading.Thread(target=extended.iss_alert)

    chat.start()
    schedule.start()
    iss.start()

    chat.join()
    schedule.join()
    iss.join()



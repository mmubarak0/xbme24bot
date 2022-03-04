#!/usr/bin/env python
# pylint: disable=C0116,W0613


import logging
import random
import os
import Messages
import media
import keyboards


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


fortunes = Messages.fortunes
content_types = ["message",
                 "photo",
                 "audio",
                 "document",
                 "video",
                 ]

subset = ["mecha", "anatomy", "elec", "bme", "chem", "code", "integral", "comp"]

ADMIN = "coruten"


lisa = []
lisaid = []
stuff = {}
users = []

# lisaid[0] == sub name inside course && lisaid[1:] == content of new sub (if the add button pressed from inside a course)

def cout(update: Update, context: CallbackContext, course, sub, key):
    query = update.callback_query
    if len(lisaid) > 0:
        if lisaid[0] == sub:
            if lisaid[1] == "text" and lisaid[-1] != "d":
                media.course[course][lisaid[0]]["message"] += lisaid[2:]
            elif lisaid[1] == "video":
                media.course[course][lisaid[0]]["vid"] += lisaid[2:]
            elif lisaid[1] == "document":
                media.course[course][lisaid[0]]["doc"] += lisaid[2:]
            elif lisaid[1] == "photo":
                media.course[course][lisaid[0]]["photo"] += lisaid[2:]
            context.bot.send_message(query.message.chat.id, "added new stuff press r to clean your input or d to delete them")
        if lisaid[0] == sub and lisaid[-1] == "d":
            st = media.course[course][lisaid[0]]
            try:
                if lisaid[1] == "text":
                    for i in lisaid[2:-1]:
                        st["message"].remove(i)
                elif lisaid[1] == "video":
                    for i in lisaid[2:-1]:
                        st["vid"].remove(i)
                elif lisaid[1] == "document":
                    for i in lisaid[2:-1]:
                        st["doc"].remove(i)
                elif lisaid[1] == "photo":
                    for i in lisaid[2:-1]:
                        st["photo"].remove(i)
            except Exception:
                context.bot.send_message(query.message.chat.id, "already removed press r to clean input")


    if len(media.course[course][sub]["message"]) > 0:
        for i in range(len(media.course[course][sub]["message"])):
            context.bot.send_message(query.message.chat.id, str(media.course[course][sub]["message"][i]))
    if len(media.course[course][sub]["vid"]) > 0:
        for i in range(len(media.course[course][sub]["vid"])):
            context.bot.send_video(query.message.chat.id, str(media.course[course][sub]["vid"][i]))
    if len(media.course[course][sub]["doc"]) > 0:
        for i in range(len(media.course[course][sub]["doc"])):
            context.bot.send_document(query.message.chat.id, str(media.course[course][sub]["doc"][i]))
    if len(media.course[course][sub]["photo"]) > 0:
        for i in range(len(media.course[course][sub]["photo"])):
            context.bot.send_photo(query.message.chat.id, str(media.course[course][sub]["photo"][i]))

    if query.message.chat.username == ADMIN:
        context.bot.send_message(chat_id=update.effective_chat.id, text="sub name is : "+sub)


def addlist(update: Update, context: CallbackContext, key):
    keyboard = keyboards.keyboard[key]
#    if update.callback_query.message.chat.username == ADMIN:
#        if not ([InlineKeyboardButton("add stuff", callback_data="add_to")]) in keyboard:
#            keyboard.append([InlineKeyboardButton(
#                "add stuff", callback_data="add_to")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    # here we used the `edit_message_test` to overwrite the previous
    # message and replace it with the new one instead of
    # having multiple replys
    query = update.callback_query
    query.edit_message_text(text='Please choose :',
                            reply_markup=reply_markup)


# ----------------------
def echo(update: Update, context: CallbackContext):
    """ text handler
        it also return the message id for me
        if i need it
        & it handles query send too
    """

    ranma = random.randint(0, len(media.course["mecha"]["main_sheet"]["sticker"]))
    try:
        if not update.message.chat.username in users:
            users.append(update.message.chat.username)
    except Exception:
        if not update.callback_query.message.chat.username in users:
            users.append(update.callback_query.message.chat.username)

    # send a fortune message when this function is called
    # here i used BSD fortune
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=os.popen('fortune fortune').read())

    # At first it checks for the text type
    # if it's coming from query it or not
    # and handle the error if it was not
    try:
        # Well here I used my username to show command as an admin
        # or somthing like nobody else than me can see it
        if update.callback_query.message.chat.username == ADMIN:
            # context.bot.send_message(update.message.chat.id, "file_id: " + str(update.callback_query.message.message_id))
            # lisaid.append(update.callback_query.message.text)
            pass
    except Exception:
        if update.message.chat.username == ADMIN:
            context.bot.send_message(update.message.chat.id, "file_id: " + str(update.message.message_id))
            lisaid.append(update.message.text)
            context.bot.send_message(update.message.chat.id, "file_type: " + "Text")
            if update.message.text == "s" or update.message.text == "r":
                context.bot.send_message(update.message.chat.id, '"'+'",\n"'.join(lisaid)+'"')
            # print('"'+'",\n"'.join(lisaid))
            if update.message.text == "r":
                lisaid.clear()
            print(users)
    try:
        context.bot.send_sticker(update.message.chat.id, media.course["mecha"]["main_sheet"]["sticker"][ranma])
    except Exception:
        pass




def voice_handler(update: Update, context: CallbackContext):
    """ voice handler it also return the voice message id for me if i need it """
    # file = context.bot.getFile(update.message.voice.file_id)
    if update.message.chat.username == ADMIN:
        context.bot.send_message(update.message.chat.id, "file_id: " + str(update.message.voice.file_id))
        context.bot.send_message(update.message.chat.id, "file_type: " + "voice")
        lisaid.append(update.message.voice.file_id)
        # file.download('voice.ogg')


def document_handler(update: Update, context: CallbackContext):
    """ Documents handler it also return the document message id for me if i need it """
    if update.message.chat.username == ADMIN:
        context.bot.send_message(update.message.chat.id, "file_id: " + str(update.message.document.file_id))
        context.bot.send_message(update.message.chat.id, "file_type: " + "document")
        lisaid.append(update.message.document.file_id)


def video_handler(update: Update, context: CallbackContext):
    """ Video handler it also return the video id for me if i need it """
    if update.message.chat.username == ADMIN:
        context.bot.send_message(update.message.chat.id, "file_id: " + str(update.message.video.file_id))
        context.bot.send_message(update.message.chat.id, "file_type: " + "video")
        lisaid.append(update.message.video.file_id)

def photo_handler(update: Update, context: CallbackContext):
    """ Photo handler it also return the photo id for me if i need it """
    if update.message.chat.username == ADMIN:
        context.bot.send_message(update.message.chat.id, "file_id: " + str(update.message.photo[0]['file_id']))
        context.bot.send_message(update.message.chat.id, "file_type: " + "photo")
        lisaid.append(update.message.photo[0]['file_id'])

        # context.bot.send_photo(update.message.chat.id,
        #                       update.message.photo[0]['file_id'])

def sticker_handler(update: Update, context: CallbackContext):
    """ Sticker handler it also return the sticker id for me if i need it """
    if update.message.chat.username == ADMIN:
        context.bot.send_message(update.message.chat.id, "file_id: " + str(update.message.sticker.file_id))
        context.bot.send_message(update.message.chat.id, "file_type: " + "sticker")
        lisaid.append(update.message.sticker.file_id)
# ---------------


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with inline buttons attached."""
    key = "main"
    keyboard = keyboards.keyboard[key]

    # I didn't completed the adding stuff from the bot
    # mechanism but at least I will try to complete this
    # later so now I will Just Hard coded stuff .

    # adding button for the admin to add stuff {{// This Will be Depreceated in the next versions//}}
    # if update.message.chat.username == "coruten":
    #     if not ([InlineKeyboardButton("add stuff", callback_data="add")]) in keyboard:
    #         keyboard.append([InlineKeyboardButton(
    #             "add stuff", callback_data="add")])

    # define the keyboards button handler
    reply_markup = InlineKeyboardMarkup(keyboard)

    # reply to user with the button under the message after sending /start
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    # query.edit_message_text(text=f"{query.data}")

    # `query.data` just return the key given from the query answer
    # and it's equall to `callback_data` parameter in keyboard buttons
    """ Mechanics of materials stuff """
    if query.data == '1':
        key = "mecha"
        addlist(update, context, key)

    """ Anatomy stuff """
    if query.data == '2':
        key = "anatomy"
        addlist(update, context, key)

    """ Circuit theory stuff """
    if query.data == '3':
        key = "elec"
        addlist(update, context, key)

    """ BME principles stuff """
    if query.data == '4':
        key = "bme"
        addlist(update, context, key)

    """ Organic chemistry stuff """
    if query.data == '5':
        key = "chem"
        addlist(update, context, key)

    """ Programming language stuff """
    if query.data == '6':
        key = "code"
        addlist(update, context, key)

    """ Special integral stuff """
    if query.data == '7':
        key = "integral"
        addlist(update, context, key)

    """ Complex number stuff """
    if query.data == '8':
        key = "comp"
        addlist(update, context, key)

    """ references stuff """
    if query.data == '9':
        key = "ref"
        addlist(update, context, key)

    """ Apps stuff """
    if query.data == '10':
        key = "app"
        addlist(update, context, key)


    if query.data == 'back':
        key = "main"
        keyboard = keyboards.keyboard[key]
        # if update.effective_chat.username == "coruten":
        #     if not ([InlineKeyboardButton("add stuff", callback_data="add")]) in keyboard:
        #         keyboard.append([InlineKeyboardButton(
        #             "add stuff", callback_data="add")])

        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)

# -----------------------------------------------------------------------------------------------
    """ answering & sending files """

    """ Mechanic Answers """
    if query.data == 'mecha1':
        # echo is just a place holder for now
        # echo(update, context)
        sub = "main_sheet"
        course = "mecha"
        cout(update, context, course, sub, course)

    elif query.data == 'mecha2':
        # echo(update, context)
        sub = "Exams"
        course = "mecha"
        cout(update, context, course, sub, course)

    elif query.data == 'mecha3':
        # echo(update, context)
        sub = "yt_tutor"
        course = "mecha"
        cout(update, context, course, sub, course)

    elif query.data == 'mecha4':
        # echo(update, context)
        sub = "hand"
        course = "mecha"
        cout(update, context, course, sub, course)

    elif query.data == 'mecha5':
        # echo(update, context)
        sub = "lec_old"
        course = "mecha"
        cout(update, context, course, sub, course)



    """ Anatomy Answers """
    if query.data == 'anatomy1':
        # echo(update, context)
        sub = "lectures"
        course = "anatomy"
        cout(update, context, course, sub, course)

    elif query.data == 'anatomy2':
        # echo(update, context)
        sub = "pdf"
        course = "anatomy"
        cout(update, context, course, sub, course)

    elif query.data == 'anatomy3':
        # echo(update, context)
        sub = "yt_tutor"
        course = "anatomy"
        cout(update, context, course, sub, course)

    elif query.data == 'anatomy4':
        # echo(update, context)
        sub = "lab"
        course = "anatomy"
        cout(update, context, course, sub, course)

    elif query.data == 'anatomy5':
        # echo(update, context)
        sub = "exam"
        course = "anatomy"
        cout(update, context, course, sub, course)



    """ Circuit theory stuff """
    if query.data == 'elec1':
        # echo(update, context)
        sub = "introduction"
        course = "elec"
        cout(update, context, course, sub, course)

    elif query.data == 'elec2':
        # echo(update, context)
        sub = "lab"
        course = "elec"
        cout(update, context, course, sub, course)

    elif query.data == 'elec3':
        echo(update, context)
        sub = "lectures"
        course = "elec"
        cout(update, context, course, sub, course)



    """ BME principles stuff """
    if query.data == 'bme1':
        # echo(update, context)
        sub = "Videos"
        course = "bme"
        cout(update, context, course, sub, course)

    elif query.data == 'bme2':
        # echo(update, context)
        sub = "pdf"
        course = "bme"
        cout(update, context, course, sub, course)

    elif query.data == 'bme3':
        # echo(update, context)
        sub = "ppt"
        course = "bme"
        cout(update, context, course, sub, course)

    elif query.data == 'bme4':
        # echo(update, context)
        sub = "yt_tutor"
        course = "bme"
        cout(update, context, course, sub, course)

    elif query.data == 'bme5':
        # echo(update, context)
        sub = "summary"
        course = "bme"
        cout(update, context, course, sub, course)



    """ Organic chemistry stuff """
    if query.data == 'chem1':
        # echo(update, context)
        sub = "ppt"
        course = "chem"
        cout(update, context, course, sub, course)

    elif query.data == 'chem2':
        # echo(update, context)
        sub = "pdf"
        course = "chem"
        cout(update, context, course, sub, course)

    elif query.data == 'chem3':
        # echo(update, context)
        sub = "old_lec"
        course = "chem"
        cout(update, context, course, sub, course)

    elif query.data == 'chem4':
        # echo(update, context)
        sub = "exams"
        course = "chem"
        cout(update, context, course, sub, course)



    """ Programming language stuff """
    if query.data == 'code1':
        echo(update, context)
        sub = "lectures"
        course = "code"
        cout(update, context, course, sub, course)

    elif query.data == 'code2':
        # echo(update, context)
        sub = "lab"
        course = "code"
        cout(update, context, course, sub, course)

    elif query.data == 'code3':
        # echo(update, context)
        sub = "exam"
        course = "code"
        cout(update, context, course, sub, course)



    """ Special integral stuff """
    if query.data == 'integral1':
        # echo(update, context)
        sub = "lectures"
        course = "integral"
        cout(update, context, course, sub, course)

    if query.data == 'integral2':
        # echo(update, context)
        sub = "master_sheet"
        course = "integral"
        cout(update, context, course, sub, course)

    if query.data == 'integral3':
        # echo(update, context)
        sub = "taras"
        course = "integral"
        cout(update, context, course, sub, course)



    """ Complex number stuff """
    if query.data == 'comp1':
        # echo(update, context)
        sub = "master_sheet"
        course = "comp"
        cout(update, context, course, sub, course)

    elif query.data == 'comp2':
        # echo(update, context)
        sub = "Exams"
        course = "comp"
        cout(update, context, course, sub, course)

    elif query.data == 'comp3':
        # echo(update, context)
        sub = "hand"
        course = "comp"
        cout(update, context, course, sub, course)

    elif query.data == 'comp4':
        # echo(update, context)
        sub = "yt_tutor"
        course = "comp"
        cout(update, context, course, sub, course)



    """ references stuff """
    if query.data == 'mecharef':
        echo(update, context)
        sub = "mecharef"
        course = "ref"
        cout(update, context, course, sub, course)

    elif query.data == 'anatomyref':
        echo(update, context)
        sub = "anatomyref"
        course = "ref"
        cout(update, context, course, sub, course)

    elif query.data == 'elecref':
        # echo(update, context)
        sub = "elecref"
        course = "ref"
        cout(update, context, course, sub, course)

    elif query.data == 'bmeref':
        echo(update, context)
        sub = "bmeref"
        course = "ref"
        cout(update, context, course, sub, course)

    elif query.data == 'chemref':
        # echo(update, context)
        sub = "chemref"
        course = "ref"
        cout(update, context, course, sub, course)

    elif query.data == 'coderef':
        # echo(update, context)
        sub = "coderef"
        course = "ref"
        cout(update, context, course, sub, course)

    elif query.data == 'integralref':
        # echo(update, context)
        sub = "integralref"
        course = "ref"
        cout(update, context, course, sub, course)

    elif query.data == 'refref':
        # echo(update, context)
        sub = "compref"
        course = "ref"
        cout(update, context, course, sub, course)



    """ Apps stuff """
    if query.data == 'app1':
        echo(update, context)
        sub = subset[0]
        course = "app"
        cout(update, context, course, sub, course)

    elif query.data == 'app2':
        echo(update, context)
        sub = subset[1]
        course = "app"
        cout(update, context, course, sub, course)

    elif query.data == 'app1':
        echo(update, context)
        sub = subset[2]
        course = "app"
        cout(update, context, course, sub, course)

    elif query.data == 'app1':
        echo(update, context)
        sub = subset[3]
        course = "app"
        cout(update, context, course, sub, course)

    elif query.data == 'app1':
        echo(update, context)
        sub = subset[4]
        course = "app"
        cout(update, context, course, sub, course)

    elif query.data == 'app1':
        echo(update, context)
        sub = subset[5]
        course = "app"
        cout(update, context, course, sub, course)

    elif query.data == 'app1':
        echo(update, context)
        sub = subset[6]
        course = "app"
        cout(update, context, course, sub, course)

    elif query.data == 'app1':
        echo(update, context)
        sub = subset[7]
        course = "app"
        cout(update, context, course, sub, course)




# --------------------------------------------------------------------------------------------END of Answer section
    answers = ["amecha1", "amecha2", "amecha3", "amecha4", "amecha5",
               "aanatomy1", "aanatomy2", "aanatomy3", "aanatomy4",
               "aelec1", "aelec2", "aelec3",
               "abme1", "abme2", "abme3", "abme4",
               "achem1", "achem2", "achem3", "achem4",
               "acode1", "acode2",
               "aintegral1",
               "acomp1", "acomp2", "acomp3", "acomp4",
               ]
    if query.data == 'add':
        keyboard = keyboards.keyboard["add"]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query = update.callback_query
        query.edit_message_text(text='Please choose:',
                                reply_markup=reply_markup)

    if query.data in answers:
        context.bot.send_message(query.message.chat.id, "do you want to add stuff to : " + str(query.data))
        lisa.append(query.data)
    # print(lisa)
    # print(lisaid)
    # stuff[lisa[-1]] = lisaid[-1]
    # if not stuff["amecha1"] in amecha1:
    #     amecha1.append(stuff["amecha1"])
    # if not stuff["amecha2"] in amecha2:
    #     amecha1.append(stuff["amecha2"])
    # if not stuff["amecha3"] in amecha3:
    #     amecha1.append(stuff["amecha3"])
    # print(amecha1)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2043698404:AAFAH3MJwMnD48qliUF76-ROl7c4KKqqQg0")
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(echo_handler)
    updater.dispatcher.add_handler(
        MessageHandler(Filters.voice, voice_handler))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.document, document_handler))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.video, video_handler))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.photo, photo_handler))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.sticker, sticker_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

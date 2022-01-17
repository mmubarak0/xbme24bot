from telegram import InlineKeyboardButton

answers = ["amecha1", "amecha2", "amecha3", "amecha4", "amecha5",
               "aanatomy1", "aanatomy2", "aanatomy3", "aanatomy4",
               "aelec1", "aelec2", "aelec3",
               "abme1", "abme2", "abme3", "abme4",
               "achem1", "achem2", "achem3", "achem4",
               "acode1", "acode2",
               "aintegral1",
               "acomp1", "acomp2", "acomp3", "acomp4",
               ]

keyboard = {
    "main": [
        [
            InlineKeyboardButton("♦️ ميكانيكا المواد", callback_data='1'),
            InlineKeyboardButton(
                "♦️ التشريح و وظائف الأعضاء", callback_data='2'),
            InlineKeyboardButton(
                "♦️ نظرية الدوائر الكهربية", callback_data='3'),
        ],
        [InlineKeyboardButton("♥️ أساسيات الهندسة الطبية", callback_data='4')],
        [InlineKeyboardButton("🔸 الكيمياء العضوية", callback_data='5')],
        [InlineKeyboardButton("💻 لغات البرمجة", callback_data='6')],
        [
            InlineKeyboardButton(
                "🔹 الدوال التكاملية الخاصة", callback_data='7'),
            InlineKeyboardButton("🔹 الدوال المركبة", callback_data='8'),
        ],
        [InlineKeyboardButton("💡مراجع", callback_data='9')],
        [InlineKeyboardButton("🎲 Apps", callback_data='10')],
    ],


    # """ Mechanics of materials stuff """
    "mecha": [
            [
                InlineKeyboardButton("Main sheet", callback_data='mecha1'),
                InlineKeyboardButton("Exams", callback_data='mecha2'),
                InlineKeyboardButton("Youtube tutor", callback_data='mecha3'),
            ],
            [
                InlineKeyboardButton("hand summaries", callback_data='mecha4'),
                InlineKeyboardButton("Lectures old", callback_data='mecha5'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ Anatomy stuff """
    "anatomy": [
            [
                InlineKeyboardButton("Lectures", callback_data='anatomy1'),
                InlineKeyboardButton("pdf", callback_data='anatomy2'),
            ],
            [
                InlineKeyboardButton(
                    "YouTube tutor", callback_data='anatomy3'),
                InlineKeyboardButton("Lab", callback_data='anatomy4'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ Circuit theory stuff """
    "elec": [
            [
                InlineKeyboardButton("Introduction", callback_data='elec1'),
                InlineKeyboardButton("Lab", callback_data='elec2'),
            ],
            [
                InlineKeyboardButton("Lectures", callback_data='elec3'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ BME principles stuff """
    "bme": [
            [
                InlineKeyboardButton("Videos", callback_data='bme1'),
                InlineKeyboardButton("PDF", callback_data='bme2'),
                InlineKeyboardButton("PPT", callback_data='bme3'),
            ],
            [
                InlineKeyboardButton("Youtube tutor", callback_data='bme4'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ Organic chemistry stuff """
    "chem": [
            [
                InlineKeyboardButton("PPT", callback_data='chem1'),
                InlineKeyboardButton("PDF", callback_data='chem2'),
            ],
            [
                InlineKeyboardButton("Old lectures", callback_data='chem3'),
                InlineKeyboardButton("Exams", callback_data='chem4'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ Programming language stuff """
    "code": [
            [
                InlineKeyboardButton("Lectures", callback_data='code1'),
            ],
            [
                InlineKeyboardButton("Lab", callback_data='code2'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ Special integral stuff """
    "integral": [
            [
                InlineKeyboardButton("Lectures", callback_data='integral1'),
            ],
            [
                InlineKeyboardButton("Main sheet", callback_data='integral2'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ Complex number stuff """
    "comp": [
            [
                InlineKeyboardButton("Master sheet", callback_data='comp1'),
                InlineKeyboardButton("Exams", callback_data='comp2'),
            ],
            [
                InlineKeyboardButton("hand summaries", callback_data='comp3'),
                InlineKeyboardButton("YouTube tutor", callback_data='comp4'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ references stuff """
    "ref": [
            [
                InlineKeyboardButton(
                    "Electrical Circuit theory", callback_data='elecref'),
            ],
            [
                InlineKeyboardButton(
                    "Mechanics of materials", callback_data='mecharef'),
            ],
            [
                InlineKeyboardButton("Anatomy & physiology",
                                     callback_data='anatomyref'),
            ],
            [
                InlineKeyboardButton(
                    "Biomedical Engineering principles", callback_data='bmeref'),
            ],
            [
                InlineKeyboardButton("Organic chemistry",
                                     callback_data='chemref'),
            ],
            [
                InlineKeyboardButton("Programming language",
                                     callback_data='coderef'),
            ],
            [
                InlineKeyboardButton("Special integral",
                                     callback_data='integralref'),
            ],
            [
                InlineKeyboardButton(
                    "Complex number", callback_data='compref'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    # """ Apps stuff """
    "app": [
            [
                InlineKeyboardButton("Anatomy ", callback_data='app1'),
            ],
            [InlineKeyboardButton("Back to menu", callback_data='back')],
        ],


    "add": [
            [InlineKeyboardButton("m1(Main sheet)", callback_data=answers[0]),
             InlineKeyboardButton(
                 "m2(exam)", callback_data=answers[1]),
             InlineKeyboardButton(
                 "m3(yt tutor)", callback_data=answers[2]),
             InlineKeyboardButton(
                 "m4(hand summary)", callback_data=answers[3]),
             InlineKeyboardButton(
                 "m5(lectures old)", callback_data=answers[4])
             ],
            [InlineKeyboardButton("a6(lecture)", callback_data=answers[5]),
            InlineKeyboardButton(
                "a2(pdf)", callback_data=answers[6]),
            InlineKeyboardButton(
                "a3(yt tutor)", callback_data=answers[7]),
            InlineKeyboardButton(
                "a4(lab)", callback_data=answers[8])
             ],
            [InlineKeyboardButton("e1(intro)", callback_data=answers[9]),
            InlineKeyboardButton(
                "e2(lab)", callback_data=answers[10]),
            InlineKeyboardButton(
                "e3(lectures)", callback_data=answers[11])
             ],
            [InlineKeyboardButton("b1(video)", callback_data=answers[12]),
            InlineKeyboardButton(
                "b2(pdf)", callback_data=answers[13]),
            InlineKeyboardButton(
                "b3(ppt)", callback_data=answers[14]),
            InlineKeyboardButton(
                "b4(yt tutor)", callback_data=answers[15])
             ],
            [InlineKeyboardButton("ch1(ppt)", callback_data=answers[16]),
            InlineKeyboardButton(
                "ch2(pdf)", callback_data=answers[17]),
            InlineKeyboardButton(
                "ch3(old lec)", callback_data=answers[18]),
            InlineKeyboardButton(
                "ch4(exam)", callback_data=answers[19])
             ],
            [InlineKeyboardButton("co1(lectuer)", callback_data=answers[20]),
            InlineKeyboardButton(
                "co2(lab)", callback_data=answers[21])
             ],
            [InlineKeyboardButton("i1(lectures)", callback_data=answers[22])
             ],
            [InlineKeyboardButton("c1(master sheet)", callback_data=answers[23]),
            InlineKeyboardButton(
                "c2(exams)", callback_data=answers[24]),
            InlineKeyboardButton(
                "c3(hand summ)", callback_data=answers[25]),
            InlineKeyboardButton(
                "c4(yt tutor)", callback_data=answers[26])
             ],
        ]
}

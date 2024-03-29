BUILD_NUMBER = 52
LAST_UPDATE_DATE = "September/17/2020"


def combine_multiple_lines(lines):
    value = ""
    for line in lines:
        value = value + line + "\n"
    return value


# SESSIONS SHIT
MAX_NUMBER_OF_AVAILABLE_SESSIONS = 3

AVAILABLE_CATEGORY_ID = 667256540864053269
OCCUPIED_CATEGORY_ID = 630899948841336842
DORMANT_CATEGORY_ID = 722493688688934972

SESSION_CHANNELS = [
    630209704894791691,
    705712718681735218,
    705712937645637643,
    630209625966379023,
    630209791255642112,
    630209742106656779,
    722512874735665185,
    722512938619109407,
    722512998933069884,
    722513045967994902,
    722513107905151076,
    722513186590556260,
]

IN_SESSION_ROLE = 722498396220293150
MAIN_TUTOR_ROLE = 630183885623525424
TUTOR_ROLES = {
    "MATH": 724158494072111175,
    "SCIENCE": 724158499524968488,
    "SOCIALSTUDIES": 724159960627281931,
    "ENGLISH": 724158482286379092,
}
BANNED_ASSIGN_TUTOR_ROLE = 703965433816023110


def tsc_ongoing_session(user):
    return f'__**How to ask for help:**__\n:question: | Post your question! *Don\'t just say "help".*\n:eye: | Add any images, sources, or texts that will help the tutors.\n:school_satchel: | Inform the tutor of what level the question is. *(e.g. python3.8, geometry, us history)*\n\n**Once the above is complete, ping the respective tutor role once!**\n\n{user}'


# AUTOJOIN
JOIN_MSG_CHANNEL = 630206335085969418

PUBLIC_WELCOMER_MSG = combine_multiple_lines(
    [
        "Hey, <@&671220549283741708>! {mention} has joined **The Study Corner**.",
        "Please give them a proper welcome!",
    ]
)

MUST_ADD_ROLES = [674245729480605716, 631013102325858305, 630185034753638429]

uni1 = "\ud83d\udd17"
uni2 = "\ud83c\udf80\u30fb"
uni3 = "\u2b50\ufe0f\u30fb"
uni4 = "\ud83c\udf0c\u30fb"
uni5 = "\ud83d\udd30\u30fb"
uni6 = "\ud83e\udd0d\u30fb"
PRIVATE_WELCOMER_MSG = combine_multiple_lines(
    [
        "**Hello & Welcome to __The Study Corner__**",
        "__Some Basic Guidelines before Entering TSC:__",
        f"> Members are not permitted to DM Staff, unless they are friends. To access help, DM the support bot.",
        "> Use **only** the Study Channels provided to ask questions about subjects.",
        "> Excessive swearing is prohibited.",
        "> Doing anything that breaks **Discord TOS** is a bannable offence.",
        "",
        f"You can assign yourself roles at `#{uni2}profile`. Please also introduce yourself at `#{uni3}introductions`.",
        "",
        "Here is a permanent invite to the server just in case you leave or you'd like to invite friends - https://discord.gg/AcFxSZP",
        "Here is a permanent invite to the **Ban Appeals** server just in case you get banned and wish to appeal - https://discord.gg/ZzKBTwy",
        "",
        f'We are currently actively looking for Moderators, Developers and Partners. If you are interested in any of theses check out `#{uni4}server-information`. If you are interested in Partnering with us, DM Lush#0001 or anyone with the "Growth & Promtion" Role.',
        "",
        "**Lush's Other Server(s):**",
        f"{uni1} - https://discord.gg/Yv6Y2bc",
        f"{uni1} - https://gph.is/g/ZywQrrn",
    ]
)

CLOSE_KEYWORDS = ["ty", "thanks", "thank", "tank", "tysm", "bye", "cya", "bai"]

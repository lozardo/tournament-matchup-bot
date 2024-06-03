import discord
from discord.ext import commands
import random

# Initialize the bot
# Define your desired intents
intents = discord.Intents.default()
intents.typing = True  # Optional: Adjust the intent settings as needed
intents.messages = True
intents.dm_messages = True
intents.reactions = True
#intents.message_content = True

# Initialize the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Create a dictionary to store replies
replies = {}
players = {'exslide': '183272527060140032',
           'lozardo': '477186481811619850',
           'aaron': '398998497514225674',
           'noob': '453609781685649419',
           'axus': '325982325118861314',
           'lucy': '343160765995286528',
           'face': '267432017019273226',
           'wind': '254825291023646720', #sui player
           'jav': '560312553331359755', #fbk ollie player
           'lud': '390525312825425942',
           'wazim': '204750438292127744',
           'logec': '114813375950749711',
           'ver': '414877069072269312',
           'mouss': '530985763979132929',
           'brewed': '776731790790098965',
           'mikko': '122141547427921920',
           'kemo': '516240528598106112'
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

def funny_text_person_pick():
    options = ["blessed you with the opportunity to play",
               "allowed you to use",
               "was nice enough to let you play",
               "decided your new main is",
               "thought it would be funny to give you",
               "wanted you to play as",
               "REALLY REALLY wanted to fight you when you're using",
               "wanted you to suffer with",
               "decided it would be best if you used",
               "wil doxx you if you dont use"]
    return random.choice(options)

def funny_text_random_char():
    options = ["play",
               "damn... seems like you need to use",
               "be happy! you get to use",
               "your new main is",
               "it would be really funny if you used",
               "you should REALLY REALLY use",
               "I want you to suffer with",
               "god decided it would be best if you used",
               "you will get doxxed if you dont use"]
    return random.choice(options)


def random_char(chemical_bool=False): #if true ret as second option which is chemical
    options = [["Ayame","aluminium manganese alloy"],
               ["Aki","aluminum potassium alloy"],
               ["Botan","aluminum titanium alloy, boron oxide"],
               ["Coco","ethylene dione"],
               ["Fubuki","potassium bromine, fluorine dioxe iodide"],
               ["Korone","krypton, neon nitrogen dioxide"],
               ["Ollie","dilithium oxide"],
               ["Sora","argon sulfate oxide"],
               ["Suisei","disulfer diiodine oxide"],
               ["Pekora","radium potassium phosphorus oxide"],
               ["Ina", "Goku"]]
    return random.choice(options)[int(chemical_bool)]


def random_assist(chemical_bool=False): #if true ret as second option which is chemical
    options = [["Kanata","aluminum titanium alloy, aluminum potassium alloy nitride"],
               ["Amelia","aluminium manganese alloy lithium iodine"],
               ["Marine","manganese argon iodine nitride"],
               ["Iroha","iridium ethyl"],
               ["Risu","NUTS"],
               ["Mio","molybdenum iodine"],
               ["Roboco","rubidium carbonate"],
               ["Miko","potassium manganate iodide"],
               ["Kaela","aluminum potassium alloy lithium"],
               ["Kiara","potassium argon iodine"],
               ["Moona","molybdenum nitrogen oxide"],
               ["AZKi","aluminum potassium alloy zinc iodide"],
               ["Fauna", "aizawa"],
               ["Subaru", "Cementoss"]]
    return random.choice(options)[int(chemical_bool)]


@bot.event
async def on_message(message):
    print(message.content)
    if message.author == bot.user:
        return

    mentioned_users = []  # Initialize the list here

    '''if message.content[0:2] == "! " and not isinstance(message.channel, discord.DMChannel):
        mentioned_user = message.mentions[0]
        sender = message.author

        # Send a direct message to both the sender and the mentioned user
        dm_sender = await sender.create_dm()
        dm_mentioned = await mentioned_user.create_dm()

        await dm_sender.send(f'You said you are playing right now, who do you want to give to your opponent? (have the char\'s name in the next message)')
        await dm_mentioned.send(f'You were pinged by {sender.mention} so I assume you two are playing, who do you give them? (have the char\'s name in the next message)')

        # Add thumbs-up reaction to the original message
        await message.add_reaction('👍')

        # Store message context for later
        replies[sender] = message
        replies[mentioned_user] = message
'''

    if message.content[0:7] == "!random":
        print(f"rolling for {message.author}")
        reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
        '''
        if players['exslide'] in f'{message.author.mention}':
            while "Korone" in reply or "Risu" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['lozardo'] in f'{message.author.mention}':
            reply = f"{message.author.mention} {funny_text_random_char()} Coco Moona"
            pass

        if players['aaron'] in f'{message.author.mention}':
            while "Coco" in reply or "Aki" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['noob'] in f'{message.author.mention}':
            while "Ayame" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['axus'] in f'{message.author.mention}':
            while "Aki" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['lucy'] in f'{message.author.mention}':
            while "Coco" in reply:
                reply = f"you now play poker with your opponent"
            pass

        if players['face'] in f'{message.author.mention}':
            while "Sora" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['wind'] in f'{message.author.mention}':
            while "Suisei" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['jav'] in f'{message.author.mention}':
            while "Fubuki" in reply or 'Ollie' in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['lud'] in f'{message.author.mention}':
            while "Pekora" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['wazim'] in f'{message.author.mention}':
            while "Fubuki" in reply or 'Pekora' in reply or 'Korone' in reply:
                reply = "shut up"
            pass

        if players['logec'] in f'{message.author.mention}':
            while "Ayame" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['ver'] in f'{message.author.mention}':
            while "Suisei" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['mouss'] in f'{message.author.mention}':
            while "Botan" in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['brewed'] in f'{message.author.mention}':
            while "Ayame" in reply or 'Korone' in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            pass

        if players['mikko'] in f'{message.author.mention}':
            while "Ollie" in reply or 'Aki' in reply:
                reply = f"{message.author.mention} {funny_text_random_char()} {random_char()} {random_assist()}"
            reply = "you and the opponent now play on beta build"
            pass'''

        if random.randint(0, 99) == 0:
            reply = f"you now play poker with your opponent"

    await message.channel.send(reply)
    await message.delete()
'''
    if message.content[0:9] == "!exrandom" and players['kemo'] in f'{message.author.mention}':
        print(f"EXrolling for {message.author}")
        reply = f"{message.author.mention} {funny_text_random_char()} {random_char(True)} - {random_assist(True)}"
        #while '114813375950749711' in f'{message.author.mention}' and "aluminium manganese alloy" in reply: for logec
        #    reply = f"{message.author.mention} {funny_text_random_char()} {random_char(True)} - {random_assist(True)} (you originally got ayame)"
        await message.channel.send(reply)
'''

'''
    # Check if the message is in a direct message with the bot
    if isinstance(message.channel, discord.DMChannel) and message.author in replies:
        original_message = replies[message.author]
        if original_message.author != message.author:
            mentioned_users = [original_message.mentions[0]]
            print(mentioned_users)


        # Check if the message is from either the sender or the mentioned user
        if message.author == original_message.author or message.author in mentioned_users:
            # Store the reply in the replies dictionary
            if original_message not in replies:
                replies[original_message] = []


            replies[original_message].append((message.author, message.content))
            print(replies)

            # If both the sender and mentioned user have replied, send a combined message to the original channel
            if len(replies[original_message]) == 2:
                original_channel = original_message.channel
                combined_reply = "\n".join([f'{user.mention} {funny_text_person_pick()} {reply}' for user, reply in replies[original_message]])

                # Send the combined message to the original channel
                sent_message = await original_channel.send(combined_reply)

                # Add thumbs-up reaction to the combined message
                await sent_message.add_reaction('👍')
'''

bot_token = ''
bot.run(bot_token)

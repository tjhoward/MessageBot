#from flask import Flask 
#from threading import Thread
#from main import start
import random
from nextcord.ext import commands##
import os #to get environment variable from AWS
#import asyncio##

api_key = os.environ['API_KEY']
bot = commands.Bot(command_prefix = '.') ##


class messages():
    def __init__(self, user_name):
        self.user_name = user_name
        self.templates = ["* ahead", "likely *", "if only I had a *...", "*, O *", "ahh, *...", "no * ahead", "first off, *", "didn't expect *...", "behold, *!", "*", "* required ahead", "seek *", "visions of *...", "offer *", "*!", "be wary of *", "still no *...", "could this be a *?", "praise the *!", "*?","try *", "why is it always *?", "time for *", "let there be *", "*..."]
        self.conjuctions = [" and then ", " or ", " but ", " therefore ", " in short ", " except ", " by the way ", " so to speak ", " all the more ", "," ]
        self.enemies = ['enemy', 'weak foe', 'strong foe', 'monster', 'dragon', 'boss', 'sentry', 'group', 'pack', 'decoy', 'undead', 'soldier', 'knight', 'cavalier', 'archer', 'sniper', 'mage', 'ordnance', 'monarch', 'lord', 'demi-human', 'outsider', 'giant', 'horse', 'dog', 'wolf', 'rat', 'beast', 'bird', 'raptor', 'snake', 'crab', 'prawn', 'octopus', 'bug', 'scarab', 'slug', 'wraith', 'skeleton', 'monstrosity', 'ill-omened creature']
        self.people = ['Tarnished', 'warrior', 'swordfighter', 'knight', 'samurai', 'sorcerer', 'cleric', 'sage', 'merchant', 'teacher', 'master', 'friend', 'lover', 'old dear', 'old codger', 'angel', 'fat coinpurse', 'pauper', 'good sort', 'wicked sort', 'plump sort', 'skinny sort', 'lovable sort', 'pathetic sort', 'strange sort', 'nimble sort', 'laggardly sort', 'invisible sort', 'unfathomable sort', 'giant sort', 'sinner', 'thief', 'liar', 'dastard', 'traitor', 'pair', 'trio', 'noble', 'aristocrat', 'hero', 'champion', 'monarch', 'lord', 'god']
        self.things = [ 'item', 'necessary item', 'precious item', 'something', 'something incredible', 'treasure chest', 'corpse', 'coffin', 'trap', 'armament', 'shield', 'bow', 'projectile weapon', 'armor', 'talisman', 'skill', 'sorcery', 'incantation', 'map', 'material', 'flower', 'grass', 'tree', 'fruit', 'seed', 'mushroom', 'tear', 'crystal', 'butterfly', 'bug', 'dung', 'grace', 'door', 'key', 'ladder', 'lever', 'lift', 'spiritspring', 'sending gate', 'stone astrolabe', 'Birdseye Telescope', 'message', 'bloodstain', 'Erdtree', 'Elden Ring']
        self.battleTactics = [ 'close-quarters battle', 'ranged battle', 'horseback battle', 'luring out', 'defeating one-by-one', 'taking on all at once', 'rushing in', 'stealth', 'mimicry', 'confusion', 'pursuit', 'fleeing', 'summoning', 'circling around', 'jumping off', 'dashing through', 'brief respite'] 
        self.actions = [  'attacking', 'jump attack', 'running attack', 'critical hit', 'two-handing', 'blocking', 'parrying', 'guard counter', 'sorcery', 'incantation', 'skill', 'summoning', 'throwing', 'healing', 'running', 'rolling', 'backstepping', 'jumping', 'crouching', 'target lock', 'item crafting', 'gesturing'] 
        self.situations = [  'morning', 'noon', 'evening', 'night', 'clear sky', 'overcast', 'rain', 'storm', 'mist', 'snow', 'patrolling', 'procession', 'crowd', 'surprise attack', 'ambush', 'pincer attack', 'beating to a pulp', 'battle', 'reinforcements', 'ritual', 'explosion', 'high spot', 'defensible spot', 'climbable spot', 'bright spot', 'dark spot', 'open area', 'cramped area', 'hiding place', 'sniping spot', 'recon spot', 'safety', 'danger', 'gorgeous view', 'detour', 'hidden path', 'secret passage', 'shortcut', 'dead end', 'looking away', 'unnoticed', 'out of stamina'] 
        self.places = [  'high road', 'checkpoint', 'bridge', 'castle', 'fort', 'city', 'ruins', 'church', 'tower', 'camp site', 'house', 'cemetery', 'underground tomb', 'tunnel', 'cave', 'evergaol', 'great tree', 'cellar', 'surface', 'underground', 'forest', 'river', 'lake', 'bog', 'mountain', 'valley', 'cliff', 'waterside', 'nest', 'hole'] 
        self.directions = [  'east', 'west', 'south', 'north', 'ahead', 'behind', 'left', 'right', 'center', 'up', 'down', 'edge'] 
        self.bodyParts = [  'head', 'stomach', 'back', 'arms', 'legs', 'rump', 'tail', 'core', 'fingers']
        self.affinities = [  'physical', 'standard', 'striking', 'slashing', 'piercing', 'fire', 'lightning', 'magic', 'holy', 'poison', 'toxic', 'scarlet rot', 'blood loss', 'frost', 'sleep', 'madness', 'death'] 
        self.concepts = [  'life', 'Death', 'light', 'dark', 'stars', 'fire', 'Order', 'chaos', 'joy', 'wrath', 'suffering', 'sadness', 'comfort', 'bliss', 'misfortune', 'good fortune', 'bad luck', 'hope', 'despair', 'victory', 'defeat', 'research', 'faith', 'abundance', 'rot', 'loyalty', 'injustice', 'secret', 'opportunity', 'pickle', 'clue', 'friendship', 'love', 'bravery', 'vigor', 'fortitude', 'confidence', 'distracted', 'unguarded', 'introspection', 'regret', 'resignation', 'futility', 'on the brink', 'betrayal', 'revenge', 'destruction', 'recklessness', 'calmness', 'vigilance', 'tranquility', 'sound', 'tears', 'sleep', 'depths', 'dregs', 'fear', 'sacrifice', 'ruin'] 
        self.phrases = [  'good luck', 'look carefully', 'listen carefully', 'think carefully', 'well done', 'I did it!', "I've failed...", 'here!', 'not here!', "don't you dare!", 'do it!', "I can't take this...", "don't think", 'so lonely...', 'here again...', 'just getting started', 'stay calm', 'keep moving', 'turn back', 'give up', "don't give up", 'help me...', "I don't believe it...", 'too high up', 'I want to go home...', "it's like a dream...", 'seems familiar...', 'beautiful...', "you don't have the right", 'are you ready?']


    def getRandom(self, lists):
        max = len(lists) - 1
        randomValue = random.randint(0,max)
        return lists[randomValue]
    
    def getWord(self): #get a random word
        choice = random.randint(1, 12) #where 1 is enemies and 12 is phrases
        word = ""
        if choice == 1:
            word = self.getRandom(self.enemies)
        elif choice == 2:
            word = self.getRandom(self.people)
        elif choice == 3:
            word = self.getRandom(self.things)    
        elif choice == 4:
            word = self.getRandom(self.battleTactics)
        elif choice == 5:
            word = self.getRandom(self.actions)
        elif choice == 6:
            word = self.getRandom(self.situations)
        elif choice == 7:
            word = self.getRandom(self.places)
        elif choice == 8:
            word = self.getRandom(self.directions)
        elif choice == 9:
            word = self.getRandom(self.bodyParts)
        elif choice == 10:
            word = self.getRandom(self.affinities)
        elif choice == 11:
            word = self.getRandom(self.concepts)
        elif choice == 12:
            word = self.getRandom(self.phrases)    
        
        return word
    
    def fillTemplate(self, template_skeleton): #fill in blank spots of template
        #print("template skeleton is " + template_skeleton)
        filled_template = template_skeleton
        count = template_skeleton.count("*")
        #print("count is " + str(count))
        index = 0
        filled_template = filled_template.replace("*", self.getWord())
        
        #while index < count:
           # filled_template = filled_template.replace("*", self.getWord(), 1)
           # index += 1
        
        #print("filled template is " + filled_template)
        return filled_template

@bot.command(name="message") #.hi
async def SendMessage(ctx):
        q = messages('')
        filledTemplate = ""
        filledTemplate2 = ""
        template_skeleton = q.getRandom(q.templates)
        template_skeleton2 = ""
        conjuction = ""
        
        filledTemplate = q.fillTemplate(template_skeleton)
        
        useConjuction = random.randint(0,1) == 1
        if useConjuction == True:
            template_skeleton2 = q.getRandom(q.templates)
            filledTemplate2 = q.fillTemplate(template_skeleton2)
            conjuction = q.getRandom(q.conjuctions)
            
            if conjuction == ",":
                await ctx.send(filledTemplate + conjuction + "\n" + filledTemplate2)
            else:
                conjuction = conjuction.strip() + " "
                await ctx.send(filledTemplate + "\n" + conjuction +  filledTemplate2)
            
        elif useConjuction == False:
            await ctx.send(filledTemplate)

@bot.command(name="D") #.hi
async def deex(ctx):
    #emoji = get(bot.get_all_emojis(), name='EmojiName')
    #await bot.add_reaction(message, emoji)
    await ctx.send("Deez nuts!")

@bot.event
async def on_message(message):

    if message.author == bot.user: #ignore bot messages
        return
    
    channel = message.channel
    #await channel.send('hi')

if __name__ == "__main__":
    print("started")
    bot.run(api_key)
#loop = asyncio.get_event_loop()##
#loop.run_until_complete(bot.login(api_key))##

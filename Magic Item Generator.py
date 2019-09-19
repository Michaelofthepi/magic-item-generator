import random

bases = """sword
axe
hammer
amulet
potion
broom
orb
cloak
armor
circlet
boots
bag
shield
shackles
glasses
helmet
book
bow
ring
socks
ointment
deck
fork
cart
boat
paper
arrows
apparatus
slippers
greaves
staff
skull
head
hand
glue
quiver
token
instrument
mirror
flask
keg
javelin
dagger
maul
shuriken
spiked chain
dust
gem
gate
carpet
candle
crystal ball
fortress
figurine
hat
portable ram
trap
box
ioun stone
horn"""

enchantments = """flaming
frost
healing
adamantine
death
commanding elementals
flying
talking
awakened
teleportation
unlocking
lucky
unlucky
instant
illusion
illusionary
many things
dwarven
draconic
disguise
feindish
knowledge
toughness
serpentine
folding
theives
holding
devouring
alien
eldritch
fireball
archmage
cubic
crab
stars
wild
natural
lycanthrope (wolf)
ursanthrope (bear)
felinethrope (tiger)
smashing
horripilating
revivification
holy
unholy
gravity
paper
mechanical
electricity
sonic
endless water
cursed (make something up)
jousting
charming
swarming
swarming insects
snake
fuzzy
soft
lifestealing
vorpal
the sphere
ultimate evil
pure good
true neutral
tentacle
enemy detection
secret
wonder
vecna
fish command
sticky
creative
rulership
eyes
fire resistance
telekinesis
wishes
x-ray vision
animal influence
limitless
wild magic
the sewers
todd
love
life trapping
soul trapping
tripping
psychadelic
berserker
dry
elvenkind
displacement
winterlands
northern
levitating
arrow attraction
bat
manta ray
arachnida
drow
glamerous
free action
jumping
warmth
regeneration
annihilation
refridgeration
spherical
monkey
primal
psychic
woodlands
sharpness
smiting
bane of arthropods
fear
web
plane shift
winged
sun
son
spellguard
gaseous form
gaseous
valhalla
horned
golden lion
purple
enlargement
shrinking
slaying"""

basesList = bases.split("\n")
#print(basesList)
enchantmentsList = enchantments.split("\n")
#print(enchantmentsList)

magicItemList = []

def makeItem():
    base = getBase()
    enchantment = getEnchantment()
    magicItem = ""
    roll = random.randint(0,20) #rolls to see if it's
    if roll < 10:   #[ENCHANTMENT] [BASE] (10/21)
        magicItem += enchantment+" "+base
    elif roll == 20:#[ENCHANTMENT] [BASE] of [ENCHANTMENT 2] (1/21)
        enchantment2 = getEnchantment()
        magicItem += enchantment+" "+base+" of "+enchantment2
    else:        #or [BASE] of [ENCHANTMENT] (10/21)
        magicItem += base+" of "+enchantment
    return magicItem

def getEnchantment():
    return enchantmentsList[random.randint(0,len(enchantmentsList)-1)]

def getBase():
    return basesList[random.randint(0,len(basesList)-1)]

for i in range(100):
    magicItem = makeItem()
    magicItemList.append(str(i+1)+": "+magicItem)

for item in magicItemList:
    print(item)

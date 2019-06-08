init python:
    def rolly(event, interact=True, **kwargs):
        renpy.fix_rollback()
        

label nameentry: 

$ cardduty = False
$ cardenlightenment = False
$ cardconflict = False
$ cardgrief = False
$ cardhope = False
$ cardinception = False
$ cardleadership = False
$ cardlorem = False
$ cardloss = False
$ cardpassion = False
$ cardpride = False
$ cardsuperstition = False
$ cardtrauma = False

if persistent.endingsseen == 0:
    
    pass
    
else:

    $ remystatus = "none"
    $ annastatus = "none"
    $ adinestatus = "none"
    $ brycestatus = "none"
    $ loremstatus = "none"

    $ remydead = False
    $ annadead = False
    $ adinedead = False
    $ brycedead = False
    $ loremdead = False
    
    jump skipintro
    
label nameentryx:

$ save_name = "Prologue"

$ adjust_spacing = False

stop music fadeout 0.5

$ player_name = "Name"

scene black with fade

scene heartbg2 with fade

s "Detecting user profile.{cps=2}..{/cps}{w=2.0}{nw}"

#if mp.demoplayed == True:
    
    #play sound "fx/system.wav"
    
    #s "User Profile found."
    
    #call syscheck from _call_syscheck_2
    
    #if system == "sassy":
        
        #play sound "fx/system3.wav"
        
        #s "Wait a minute. It's you, [player_name]!"

        #play sound "fx/system3.wav"
        
        #s "How the heck did you even get to be here? You're certainly not supposed to."

        #play sound "fx/system3.wav"
        
        #s "Hmm, maybe you don't know. Or you don't remember."

        #play sound "fx/system3.wav"
        
        #s "Whatever the heck happened, you're here now and we're going to make the best of it, alright?"

        #play sound "fx/system3.wav"
        
        #s "Let's just proceed from here."
    
    #jump detected
    
#else:

play sound "fx/system.wav"

s "User profile not found."

label nameentry2:

#$ player_name = renpy.input("Please, enter your name:", default='Jayden', exclude='{%}', length=10)
$ player_name = renpy.input("Please, enter your name:", default=player_name, exclude='{%}', length=10)
$ persistent.player_name = player_name
$ mp.player_name = player_name

if player_name == "":
    $ player_name="Alex"

label colormenu1:

menu:
    s "Choose a color."
    
    "{color=#0000ff}B{/color}lue":
        $ playercolor = "#0000FF"
        $ persistent.playercolor = "#0000FF"
        $ playercolorname = "blue"
        $ persistent.playercolorname = "blue"
        $ mp.playercolorname = "blue"
        $ mp.playercolor = "#0000FF"
        jump colorend

    "{color=#ff0000}R{/color}ed":
        $ playercolor = "#ff0000"
        $ playercolorname = "red"
        $ persistent.playercolor = "#ff0000"
        $ persistent.playercolorname = "red"
        $ mp.playercolorname = "red"
        $ mp.playercolor = "#ff0000"
        jump colorend

    "{color=#ffff00}Y{/color}ellow":
        $ playercolor = "#ffff00"
        $ playercolorname = "yellow"
        $ persistent.playercolor = "#ffff00"
        $ persistent.playercolorname = "yellow"
        $ mp.playercolorname = "yellow"
        $ mp.playercolor = "#ffff00"
        jump colorend

    "{color=#008000}G{/color}reen":
        $ playercolor = "#008000"
        $ mp.playercolorname = "green"
        $ playercolorname = "green"
        $ mp.playercolor = "#008000"

        $ persistent.playercolor = "#008000"
        $ persistent.playercolorname = "green"
        jump colorend

    "{color=#d3d3d3}G{/color}ray":
        $ playercolor = "#d3d3d3"
        $ playercolorname = "gray"
        $ persistent.playercolor = "#d3d3d3"
        $ persistent.playercolorname = "gray"

        $ mp.playercolorname = "gray"
        $ mp.playercolor = "#d3d3d3"
        jump colorend

    "[[Show more colors.]":
        jump colormenu2
        
label colormenu2:

menu:
    s "Choose a color."
    
    "{color=#00ffff}C{/color}yan":
        $ playercolor = "#00ffff"
        $ playercolorname = "cyan"

        $ persistent.playercolor = "#00ffff"
        $ persistent.playercolorname = "cyan"

        $ mp.playercolorname = "cyan"
        $ mp.playercolor = "#00ffff"
        jump colorend

    "{color=#ff00ff}M{/color}agenta":
        $ playercolor = "#ff00ff"
        $ playercolorname = "magenta"

        $ persistent.playercolor = "#ff00ff"
        $ persistent.playercolorname = "magenta"

        $ mp.playercolor = "magenta"
        $ mp.playercolor = "#ff00ff"
        jump colorend

    "{color=#00ff00}L{/color}ime":
        $ playercolor = "#00ff00"
        $ playercolorname = "lime"

        $ persistent.playercolor = "#00ff00"
        $ persistent.playercolorname = "lime"

        $ mp.playercolorname = "lime"
        $ mp.playercolor = "#00ff00"
        jump colorend

    "{color=#ffa500}O{/color}range":
        $ playercolor = "#ffa500"
        $ playercolorname = "orange"

        $ persistent.playercolor = "#ffa500"
        $ persistent.playercolorname = "orange"

        $ mp.playercolorname = "orange"
        $ mp.playercolor = "#ffa500"
        jump colorend

    "{color=#ffffff}W{/color}hite":
        $ playercolor = "#ffffff"
        $ playercolorname = "white"
        
        $ persistent.playercolor = "#ffffff"
        $ persistent.playercolorname = "white"
        
        $ mp.playercolorname = "white"
        $ mp.playercolor = "#ffffff"
        jump colorend

    "[[Show more colors.]":
        jump colormenu3

label colormenu3:

menu:
    s "Choose a color."
    
    "{color=#ffd700}G{/color}old":
        $ playercolor = "#ffd700"
        $ playercolorname = "gold"
        
        $ persistent.playercolor = "#ffd700"
        $ persistent.playercolorname = "gold"
        
        $ mp.playercolorname = "gold"
        $ mp.playercolor = "#ffd700"
        jump colorend

    "{color=#c0c0c0}S{/color}ilver":
        $ playercolor = "#c0c0c0"
        $ playercolorname = "silver"
        
        $ persistent.playercolor = "#c0c0c0"
        $ persistent.playercolorname = "silver"
        
        $ mp.playercolorname = "silver"
        $ mp.playercolor = "#c0c0c0"
        jump colorend

    "{color=#b5a642}B{/color}rass":
        $ playercolor = "#b5a642"
        $ playercolorname = "brass"
        
        $ persistent.playercolor = "#b5a642"
        $ persistent.playercolorname = "brass"
        
        $ mp.playercolorname = "brass"
        $ mp.playercolor = "#b5a642"
        jump colorend

    "{color=#cd7f32}B{/color}ronze":
        $ playercolor = "#cd7f32"
        $ playercolorname = "bronze"
        
        $ persistent.playercolor = "#cd7f32"
        $ persistent.playercolorname = "bronze"
        
        $ mp.playercolorname = "bronze"
        $ mp.playercolor = "#cd7f32"
        jump colorend

    "{color=#cb6d51}C{/color}opper":
        $ playercolor = "#cb6d51"
        $ playercolorname = "copper"
        
        $ persistent.playercolor = "#cb6d51"
        $ persistent.playercolorname = "copper"
        
        $ mp.playercolorname = "copper"
        $ mp.playercolor = "#cb6d51"
        jump colorend

    "[[Show more colors.]":
        jump colormenu4

label colormenu4:

menu:
    s "Choose a color."
    
    "{color=#808000}O{/color}live":
        $ playercolor = "#808000"
        $ playercolorname = "olive"
        
        $ persistent.playercolor = "#808000"
        $ persistent.playercolorname = "olive"
        
        $ mp.playercolorname = "olive"
        $ mp.playercolor = "#808000"
        jump colorend

    "{color=#8b4513}B{/color}rown":
        $ playercolor = "#8b4513"
        $ playercolorname = "brown"
        
        $ persistent.playercolor = "#8b4513"
        $ persistent.playercolorname = "brown"
        
        $ mp.playercolorname = "brown"
        $ mp.playercolor = "#8b4513"
        jump colorend

    "{color=#008080}T{/color}eal":
        $ playercolor = "#008080"
        $ playercolorname = "teal"
        
        $ persistent.playercolor = "#008080"
        $ persistent.playercolorname = "teal"
        
        $ mp.playercolorname = "teal"
        $ mp.playercolor = "#008080"
        jump colorend

    "{color=#800080}P{/color}urple":
        $ playercolor = "#800080"
        $ playercolorname = "purple"
        
        $ persistent.playercolor = "#800080"
        $ persistent.playercolorname = "purple"
        
        $ mp.playercolorname = "purple"
        $ mp.playercolor = "#800080"
        jump colorend

    "{color=#800000}M{/color}aroon":
        $ playercolor = "#800000"
        $ playercolorname = "maroon"
        
        $ persistent.playercolor = "#800000"
        $ persistent.playercolorname = "maroon"
        
        $ mp.playercolorname = "maroon"
        $ mp.playercolor = "#800000"
        jump colorend
        
#    "{color=#808080}Gray{/color}":
#        $ playercolor = "#808080"
#        $ playercolorname = "Gray"
#        $ mp.playercolorname = "Gray"
#        $ mp.playercolor = "#808080"
#        jump colorend

    "[[Show more colors.]":
        jump colormenu1
        
label detected:
    
$ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
$ player_name = persistent.player_name

if system == "sassy":
    
    pass
    
else:

    s "Welcome back, [player_name]."

menu:
    c "(Does this look right?)"
    "No":
        jump nameentry2
        
    "Yes":
        
        play sound "fx/system.wav"
        s "User profile confirmed."
        $ mp.name = "player_name"
        $ mp.demoplayed = True
        $ mp.save()
        s "Before we start, please review the following information:"
        "Controls\nUse [[Left Click] or [[Enter] to advance text and select menu options.\nPress [[Space] to advance text only. This is useful to avoid making a selection by mistake."
        "[[ESC] or [[Right Click] brings up the menu.\n[[F] toggles fullscreen.\nUse the [[Mousewheel], or [[Page Up] and [[Page Down] to review past messages and rewind."
        "Hold [[Ctrl] or press [[Tab] to skip seen messages.\n[[S] takes a screenshot.\n[[Middle Click] or [[H] hides the text window.\nIf you wish to view this information again, you can do so from the main menu."
        s "That would be all.{cps=2}..{/cps}{w=2.0}{nw}"
        jump begingame

label colorend:
    
$ c = DynamicCharacter ("player_name", color=playercolor, callback=rolly)

menu:
    c "(Does this look right?)"
    "No":
        jump nameentry2
        
    "Yes":

        play sound "fx/system.wav"
        s "User profile confirmed."
        $ mp.name = "player_name"
        $ mp.demoplayed = True
        $ mp.save()
        s "Before we start, please review the following information:"
        "Controls\nUse [[Left Click] or [[Enter] to advance text and select menu options.\nPress [[Space] to advance text only. This is useful to avoid making a selection by mistake."
        "[[ESC] or [[Right Click] brings up the menu.\n[[F] toggles fullscreen.\nUse the [[Mousewheel], or [[Page Up] and [[Page Down] to review past messages and rewind."
        "Hold [[Ctrl] or press [[Tab] to skip seen messages.\n[[S] takes a screenshot.\n[[Middle Click] or [[H] hides the text window.\nIf you wish to view this information again, you can do so from the main menu."
        s "That would be all."

label begingame:

$ evilpoints = 0

stop music fadeout 1.0
scene black with dissolveslow
play music "mx/introtheme.ogg"
$ renpy.pause (0.5)
nvl clear
window show
n "The year is 20XX." 
n "Only recently has humanity discovered a portal that leads into a different world, populated with a race of intelligent, talking dragons. I was one of the few to travel to this world..."
n "...but, maybe, I should start at the beginning..."
n "It all began when we discovered a strange device in the middle of nowhere during one of our expeditions... a portal."

window hide
scene intro1 with dissolve
$ renpy.pause(3.0)
window show

n "I had heard about similar technology before, though that had been more on an experimental level. From what I knew, other portals had been created in the past and were under consideration for mass application. As for this one in particular, though, we did not know who had built it, nor when - or why we found it in the wilderness where we did. What was more exciting to us was the fact that it was... functional."

nvl clear

n "After our first tests, we found there was someone else on the other side who was in possession of a similar portal, and our attempts at communication through letters were successful. But in the end, the machine’s extraordinary demand for power meant we needed to act quickly as we wouldn’t be able to keep the portal open much longer. " 
n "When we made this known to the other side, we received a very unexpected reply: A letter of invitation. After some deliberation, it was decided to accept their hospitality and send a person to the other side."
n "There was an individual who took the job almost immediately." 

scene black with dissolve
window hide
scene intro2 with dissolve
$ renpy.pause(3.0)
nvl clear
window show

n "Reza Izquierdo." 
n "I knew him. Or rather, had known him. We attended the same school back then, and even had a few classes together. We never really were very close friends, but we talked to each other occasionally and hung around with the same crowd sometimes. However, we still went our separate ways in the end."
n "I wasn't sure what to think about the whole thing, but he had to have known what he was doing. He certainly was brave." 
n "Either that, or just very, very foolish." 
n "While I wasn't sure which, his courage was applauded by others. After all, he couldn't possibly have known who or what would await him at the other end of the portal, and if he did meet someone there, who knew what kinds of intentions they might have?"
n "Not that any speculation on our part would've made a difference."
nvl clear
n "When the day finally came, through he went, with applause echoing across the area - equipped only with the clothes he wore, his multi-tool, a gun and a device on his wrist that acted as a PDA."

scene black with dissolve
window hide
$ renpy.pause(1.0)
nvl clear
window show

n "Then we waited..."
n "The crowd that was applauding him slowly dispersed when the enthusiasm died down, as there was nothing for us to do but wait and speculate."
n "Approximately 8 hours later, we received our first message from him."
n "While we had assumed the portal led to another in a different country, or maybe on a different continent, the reality turned out to be much more... foreign."
n "The situation he described to us was so outlandish that we initially took it as a joke."
n "A very bad joke, maybe, with even worse timing and no punchline at all."
nvl clear
n "It soon became clear to us, though, that we may just have made one of the most important discoveries since the dawn of mankind."
n "Finding the portal had been remarkable in itself, but this took it to a completely different level."

n "From what he described about the place - or, more accurately, its inhabitants - we surmised it could not be part of Earth at all."
n "We called them {i}dragons{/i}, because according to Reza, that's what they were, or at least what they resembled most." 
n "Even though we found it hard to believe, it had been these dragons who sent us all the letters. And what Reza found on the other side of the portal was a whole civilization of them. They could talk, write books, had buildings and electricity. In many ways, their society was actually very similar to our own."
nvl clear
n "So, who were they? And where was this place? Could they be aliens?" 
n "Our speculations led us to conclude otherwise. After all, we knew about the existence of thousands of planets, millions of light-years away that may have been theoretically habitable, yet even then we had never found conclusive proof in regards to actual alien life-forms."

n "Some people brought up quantum mechanics and parallel universes, but in the end all of this was just conjecture and an ultimately fruitless endeavor, since we neither had the means nor the resources to explore these possibilities in greater detail."
nvl clear
n "I think there's just one more thing worth mentioning before I move on:"
n "The previous isolation had been mutual." 
n "They hadn't known about any other intelligent life-form beyond their own, their portal had only recently been discovered and was a technology previously unknown to them, and just as we had myths about dragons, they had myths about us."

n "That was what we knew about them so far, and as interesting as learning those things and debating their cultural significance was, we didn't really know what we should make of it all."
n "Reza apparently was sure of what he was doing, though, as he eventually let us know that they had agreed on a trade." 
nvl clear
n "We were to give them a few of our PDA devices, which contained vast amounts of knowledge, dwarfing even that of encyclopedias. In return, they would supply us with generators." 
n "Overall, they didn't seem as technologically advanced as we had been, but they did surpass us in that one aspect. Their means of generating energy seemed... sustainable." 
n "Not only that, but evidently also quite efficient. We certainly would be able to put technology like that to good use, and trading mere past knowledge of the human race for something more...  tangible... was a good call on his part." 

scene black with dissolve
window hide
$ renpy.pause(0.5)
nvl clear
window show

n "That was where I came in."
n "My prior experience in both biology and sociology made me a good fit to deliver our PDA devices for the trade. And while in the dragons' world, waiting for the prototypes of our generators to be manufactured by them, I would act as an ambassador on humanity's behalf."
n "What a way to make a first impression by a display of mutual goodwill. Everyone benefits and everyone goes home happy."
n "All is well."
n "At least, that was the plan."
nvl clear
n "Despite the images that living, talking dragons might conjure up in some people's minds, I didn't even think of bringing a weapon myself, considering that they were reportedly friendly and peaceful enough." 
n "There was no need for me to fear potential ill intentions like Reza did when he had stepped into unknown territory, and acting as humanity's ambassador, I had to do my best to uphold a high standard in fostering this diplomatic relationship."
n "When the time came for me to step through the portal, all my mental preparedness vanished. My anxiousness was fueled by all the questions lurking in my head, just as the machine started to do its work."
nvl clear

n "Would it hurt?"
n "Who would I meet on the other side?"
n "What if they really weren't so friendly and just made Reza write those letters, with the pretense of appearing friendly, only to lure us into the den of man-eating monsters and certain doom, with us ending up as nothing more than a tasty afternoon snack?"
stop music fadeout 1.0
n "Maybe I should've brought a weapon after all..."

$ _game_menu_screen = None

show screen my_scr
$ renpy.show("port1")
$ renpy.transition(Dissolve(2))
play sound "fx/tel.wav"
n "{cps=80}Suddenly, I felt a shiver coursing throughout my whole body and beyond when I disintegrated, as if every cell, every atom of my body was torn from me and pulled into a different direction.{/cps}{nw}"

$_dismiss_pause = False

scene port2 with dissolve
scene port1 with dissolve
scene port2 with dissolve
scene port1 with dissolve
scene port2 with dissolve


scene port3 with dissolvequick2
scene port4 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port5 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port6 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port7 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port8 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port9 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port10 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port11 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port12 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port13 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port14 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port15 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port16 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port17 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port18 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port19 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port20 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port21 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port22 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port23 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port24 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port25 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port26 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port27 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port28 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port29 with dissolvequick2
#$ renpy.pause(0.0, hard=True)
scene port30 with dissolve
#$ renpy.pause(0.0, hard=True)
$ renpy.pause(1.0)
scene porty with dissolveslow
#$ renpy.pause(0.0, hard=True)
scene portz with dissolveslow
#$ renpy.pause(0.0, hard=True)
scene black with dissolveslow
#$ renpy.pause(0.0, hard=True)
#window show
#$ renpy.pause(1.0)
hide screen my_scr

window hide
nvl clear
window show

$_dismiss_pause = True

stop sound fadeout 2.0

$ _game_menu_screen = "navigation"

n "{cps=80}I saw darkness and light, painting patterns in the stars as I traveled, and images rapidly flashed before me of things unseen and unspoken.{/cps}{nw}"

n "{cps=80}Both horrifying and beautiful, it was an experience unlike any other, yet over in just a split second.{/cps}"

window hide

nvl clear

window show

n "Then it was dark."
n "I could only see a patch of lighter color contrasting with its dark surroundings as my vision started to clear. Its edges got sharper as the patch of light slowly took shape, giving me the distinguished outline of a reptilian head, and an array of horns spouting from it."

$_dismiss_pause = False

window hide

label holetravel:
    
    pass

play music "mx/amb/night.ogg" fadein 5.0


show cg1xx with dissolveslow
show cg1x with dissolveslow
show cg1b with dissolveslow
show cg1 with dissolveslow
$ double_vision_on("cg1")
$ renpy.pause(1.0)
$ double_vision_off()

m "It was a dragon!{w=1.0}\nAnd as I could now see, a dragon who not only had a pair of round glasses, but also wore a burgundy tie around its neck." #testannotation
nvl clear

scene np1n dk at Pan((350, 200), (350, 200), 2.0)
show remy normal dk
with fade

#$_dismiss_pause = True

Ry "In the name of our people, I bid you welcome. If I may introduce myself, I am Remy, your guide and ambassador - a representative of our council."

$ remystatus = "none"
$ annastatus = "none"
$ adinestatus = "none"
$ brycestatus = "none"
$ loremstatus = "none"

$ remydead = False
$ annadead = False
$ adinedead = False
$ brycedead = False
$ loremdead = False

$ persistent.remymet = True

m "The dragon spoke! It was one thing to have heard and read about this, but something else entirely to have one standing in front of me, in flesh and blood... and tongue. It was good that all my mental preparedness had disappeared when I was teleported, because nothing could have prepared me for this."
Ry "Sorry, I imagine you might still feel the effects of the teleportation. Drowsiness or weakness is not unusual, as is fainting and spontaneous emptying of your bowels, bladder or stomach. How do you feel?"
m "Rendered speechless, I had totally forgotten that I was shouldering the burden of representing my people to them as well. So much for being professional, but at least he gave me a good excuse for my blunder."
c "I... think I'm alright."
show remy smile dk with dissolve
Ry "Well, I'm glad to hear that."
show remy normal dk with dissolve
Ry "Maybe we should go before it gets too dark. Come with me, please."
show np2 dk with fade
$ renpy.pause(1.0)
m "So I followed the dragon, not straying too far from him, as the sun had already departed for the day and the remaining light diminished by the minute." 
play sound "fx/steps/rough_gravel.wav"
scene np3 with dissolve
$ renpy.pause(1.0)
c "It is getting hard to see where I'm going..."

show remy normal dk with dissolve

Ry "Sorry about that, but we had a good reason to schedule your arrival like this. We did not want you to be ambushed by a crowd, so we had to keep your exact time and date of arrival secret."
c "Thanks. I suppose an event like this would make me a celebrity of sorts. It would be the same if one of you came to us."
Ry "That's quite an understatement. Some people here are rather superstitious. They might regard you or any of your kind as... divine, I suppose."
scene np4 with dissolve
$ renpy.pause(1.0)
c "Really? How so?"

show remy normal dk with dissolve

Ry "We do have certain myths that involve humans and as such... Oh, I suppose the history lesson will have to wait for another time. Here we are."
scene np5 dk with dissolve
$ renpy.pause(1.0)

m "By this point, it had gotten so dark that I could barely make out the building before us. I briefly wondered whether they might have street lights elsewhere, or if they just did not require any due to possible enhanced eyesight or night vision." 
m "I could vaguely see the dragon, his light colors still visible within the blackness that engulfed the area, rear up and manipulate the door handle with one of his forepaws."
play sound "fx/door/handle.wav"
$ renpy.pause(0.5)
play sound "fx/door/creaky.wav"
$ renpy.pause(2.5)
scene black with dissolve
$ renpy.pause(1.0)
stop music fadeout 1.0
play sound "fx/switch.wav"
$ renpy.pause(0.6)

scene o2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

m "Hinges creaking, the door opened, and with the flick of a switch, the apartment was flooded with light, blinding me after all the time we had just spent without it."

show remy normal with dissolve

Ry "This is where you will live for the time being. It is fully stocked, but in case you need anything else, I left you a note with a few phone numbers."
Ry "It is getting rather late, so I will have to take my leave now. In any case, someone will come and meet you tomorrow morning."
c "Thank you, Remy. Have a good night."
Ry "Until we meet again."

hide remy normal with dissolve
$ renpy.pause(0.6)

play sound "fx/door/doorclose3.wav"

$ renpy.pause(1.0)

window show

n "With a nod, Remy left the apartment, mindful enough to close the door behind himself. Surveying the room, I considered the events that had just transpired as my gaze met the window." 
n "I could see movement outside, and as I drew nearer, startled, I could hear footsteps in the grass, moving away quickly. Assuming it must have been the dragon I just met, I thought nothing of it as I went to bed and slowly succumbed to the sweet allure of sleep overdue."

#window hide
#nvl clear

n "I spent a few moments thinking about my role, my mission and what it meant to be here now."

window hide

menu:
    
    "I felt the responsibility placed on my shoulders.":
        nvl clear
        $ renpy.pause(0.5)
        window show
        n "Now here I was, a stranger in a strange land, as I only began to feel the weight of the burden that lay upon me, the pressure of my task and the expectations I would have to meet in representing a species, culture and civilization."
        n "So many would depend on it, yet I did not even know where the only human contact I had currently was."
        nvl clear
        n "I was alone."
        $ persistent.type = "responsible"
        $ mp.type = "responsible"
        $ mp.save()
        
    "I was eager for the adventure to come.":
        nvl clear
        $ renpy.pause(0.5)
        window show
        n "So many possibilities and prospects raced through my mind. Truth be told, the thought of being able to meet an entirely new species and civilization excited me. As I was going to be one of the first to truly experience their society with its own little quirks, differences and similarities, I couldn't help but feel like some sort of modern Vasco da Gama or Marco Polo."
        n "Maybe I would even write a book about the whole experience after it's all over. I was sure it would become a hit, all things considered."
        nvl clear
        n "At any rate, this was going to be fun."
        $ persistent.type = "adventurous"
        $ mp.type = "adventurous"
        $ mp.save()
        

window hide

if persistent.trueending:
    
    scene black with dissolveslow
    
    $ renpy.pause(2.3)

    jump sec

label skipintro:

$ cardduty = False
$ cardenlightenment = False
$ cardconflict = False
$ cardgrief = False
$ cardhope = False
$ cardinception = False
$ cardleadership = False
$ cardlorem = False
$ cardloss = False
$ cardpassion = False
$ cardpride = False
$ cardsuperstition = False
$ cardtrauma = False
    
$ secending = False

    
if persistent.endingsseen == 0:
    
    scene black with dissolveslow
    
else:
    
    stop music fadeout 0.5
    scene black with fade
    
    $ player_name = persistent.player_name
    $ playercolor = persistent.playercolor
    
    $ c = DynamicCharacter ("player_name", color=playercolor, callback=rolly)
    
    if persistent.secretending:

        s "{cps=20}You wish to glimpse the past, [player_name]? Very well.{/cps}{cps=2}..{/cps}{w=2.0}{nw}"
        
    elif persistent.trueending:
        
        s "{cps=20}You wish to return once more, [player_name]? Very well.{/cps}{cps=2}..{/cps}{w=2.0}{nw}"

    else:

        s "{cps=20}Continue your journey, [player_name].{/cps}{cps=2}..{/cps}{w=2.0}{nw}"

    #$ renpy.pause (2.0)

label seccont:

$ evilpoints = 0
$_dismiss_pause = False
#$ _skipping = False

$ trueselectable = False


$ _game_menu_screen = None

if persistent.remygoodending == True:
    if persistent.brycegoodending == True:
        if persistent.annagoodending == True:
            if persistent.adinegoodending == True:
                if persistent.loremgoodending == True:
                    $ trueselectable = True


$ renpy.pause(1.3)

play sound "fx/impact2.ogg"

$ save_name = "Chapter 1"

$ cardduty = False
$ cardenlightenment = False
$ cardconflict = False
$ cardgrief = False
$ cardhope = False
$ cardinception = False
$ cardleadership = False
$ cardlorem = False
$ cardloss = False
$ cardpassion = False
$ cardpride = False
$ cardsuperstition = False
$ cardtrauma = False

#achievements sync here
if persistent.c1blood:
    $ achievement.grant("Blood Donation")
                
if persistent.c1fish:
    $ achievement.grant("Bravery")

if persistent.c1books:
    $ achievement.grant("Bookworm")

if persistent.c1meds:
    $ achievement.grant("Prescription")
                
if persistent.c1liquid:
    $ achievement.grant("Daredevil")
                
if persistent.c1eggs:
    $ achievement.grant("Ovicide")
                
if persistent.c1fruits:
    $ achievement.grant("Fruitarian")

if persistent.c1decline:
    $ achievement.grant("Nuisance")
                
if persistent.c1invhigh:
    $ achievement.grant("Investigator 1")
                    
if persistent.c1booksort:
    $ achievement.grant("Librarian")
                
if persistent.c1boredom:
    $ achievement.grant("Patient")
                
if persistent.c1annaanswers:
    $ achievement.grant("General Knowledgist")
    
if persistent.c1teetotaler:
    $ achievement.grant("Teetotaler")
    
if persistent.c1disrobement:
    $ achievement.grant("Disrobement")

if persistent.c1bastion:
    $ achievement.grant("You are a winner!")
    
if persistent.c2interrogator:
    $ achievement.grant("Interrogator 1")

if persistent.c2bandage:
    $ achievement.grant("Finders, Keepers")

if persistent.dirttaken:
    $ achievement.grant("Archeologist")

if persistent.c2landscape:
    $ achievement.grant("Landscaper")

if persistent.orb_taken:
    $ achievement.grant("Orb Finder")
    
if persistent.c2storeaisles:
    $ achievement.grant("Window Shopper")

if persistent.c2investigation:
    $ achievement.grant("Investigator 2")
    
if persistent.c2pictures:
    $ achievement.grant("Memories")

if persistent.heardaboutcancerenvelope:
    $ achievement.grant("Snoop")

if persistent.c2legs:
    $ achievement.grant("Leg Stretcher")

if persistent.c2eau:
    $ achievement.grant("Eau de Dragon")
    
if persistent.c2magazine:
    $ achievement.grant("Research Material")

if persistent.c2music:
    $ achievement.grant("Audiophile")

if persistent.playedemera:
    $ achievement.grant("The Politician")
    
if persistent.havemapfirst:
    $ achievement.grant("Cartographer")
    
if persistent.base_taken:
    $ achievement.grant("Base Finder")

if persistent.c3prank:
    $ achievement.grant("Prankster")
    
if persistent.c3helpedkatsu:
    $ achievement.grant("Altruist")
    
if persistent.c3interrogator:
    $ achievement.grant("Interrogator 2")
    
if persistent.varasaved:
    $ achievement.grant("Stalker")
    
if persistent.c3reckless:
    $ achievement.grant("Reckless")

if persistent.c3investigator:
    $ achievement.grant("Investigator 3")

if persistent.c3flawless:
    $ achievement.grant("Flawless Run")

if persistent.seashells:
    $ achievement.grant("Souvenir")
    
if persistent.playedkatsu:
    $ achievement.grant("The Artisan")
    
if persistent.c4eggs:
    $ achievement.grant("In Loco Parentis")
    
if persistent.ixomenassembled:
    $ achievement.grant("Sphere Builder")
    
if persistent.playedkevin:
    $ achievement.grant("The Student")
    
if persistent.lazy:
    $ achievement.grant("Lazy")
    
if persistent.skip:
    $ achievement.grant("Fast Forward")
    
if persistent.popular:
    $ achievement.grant("Popular")
    
if persistent.c3pointless:
    $ achievement.grant("Utterly Pointless Achievement")
    
if persistent.izumimask:
    $ achievement.grant("Unmasking")
    
if persistent.firstending:
    $ achievement.grant("It begins")

if persistent.neutralending:
    $ achievement.grant("Detonation")

if persistent.remybadending:
    $ achievement.grant("Alone")

if persistent.remygoodending:
    $ achievement.grant("Casualties of War")

if persistent.annabadending:
    $ achievement.grant("Sacrifice")

if persistent.annagoodending:
    $ achievement.grant("Tragic Hero")

if persistent.lorembadending:
    $ achievement.grant("Remember")

if persistent.loremgoodending:
    $ achievement.grant("The Plan")

if persistent.brycebadending:
    $ achievement.grant("Catastrophy")

if persistent.brycegoodending:
    $ achievement.grant("Murderer")

if persistent.adinebadending:
    $ achievement.grant("Getaway")

if persistent.adinegoodending:
    $ achievement.grant("Decisions")

if persistent.evilending:
    $ achievement.grant("Betrayal")

if persistent.optimist:
    $ achievement.grant("Optimist")

if persistent.trueending:
    $ achievement.grant("Hope")

scene chap1 at Pan((0, 0), (0, 0), 6.0) with dissolveslow

#show card1 at Pan((100, 0), (0, 0), 2.0) with dissolveslow

if persistent.trueending == True:
 
    show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardenlightenment = True

elif trueselectable == True:

    show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardenlightenment = True

elif persistent.lastendingseen == "bad":

    show ctrauma at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardtrauma = True
    
elif persistent.lastendingseen == "good":

    show cduty at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardduty = True

else:

    show cinception at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardinception = True


show text1 with dissolveslow


if persistent.trueending == True:
 
    scene chap1 at Pan((0, 120), (0, 360), 7.0) 
    show cenlightenment at Pan((0, 0), (0, 0), 2.0) 
    show text1
    with dissolveslow

elif trueselectable == True:
    
    scene chap1 at Pan((0, 120), (0, 360), 7.0) 
    show cenlightenment at Pan((0, 0), (0, 0), 2.0) 
    show text1
    with dissolveslow

elif persistent.lastendingseen == "bad":
    
    scene chap1 at Pan((0, 120), (0, 360), 7.0) 
    show ctrauma at Pan((0, 0), (0, 0), 2.0) 
    show text1
    with dissolveslow
    
elif persistent.lastendingseen == "good":

    scene chap1 at Pan((0, 120), (0, 360), 7.0) 
    show cduty at Pan((0, 0), (0, 0), 2.0) 
    show text1
    with dissolveslow

else:

    scene chap1 at Pan((0, 120), (0, 360), 7.0) 
    show cinception at Pan((0, 0), (0, 0), 2.0) 
    show text1
    with dissolveslow




$ renpy.pause(4.0)

stop sound fadeout 2.0

scene black with dissolveslow

#$_dismiss_pause = True
#$ _skipping = True

$ renpy.pause(2.0)

nvl clear

$ _game_menu_screen = "navigation"

scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause(3.0)

if persistent.brycedies == True:
    $ persistent.brycekey1 = True
    
#insert skip menu here

play music "mx/sail.ogg"
window show

n "I awoke from uneasy dreams looking at an unfamiliar ceiling. Just for a moment, I wondered where I was before the events of last night all came back to me."
n "After a good stretch, I looked around the room illuminated by the sunlight coming in from the window. Outside, in the distance, the portal I had emerged from proudly stood on the peak of a small hill." 
n "Getting ready, I noticed something lying on the table. It was the note Remy had left for me in case I needed anything. Along with his own home phone and work number, there were also some numbers for delivery of food and other necessities, as well as emergency and even janitorial services. He had certainly thought of everything, even though I now had to wonder what a dragon plumber might look like." 

play sound "fx/door/doorbell.wav"

n "My musings were interrupted when the doorbell rang. When I opened the door, I was met by another dragon."

stop sound fadeout 0.5

window hide

play sound "fx/door/handle.wav"

$ renpy.pause (1.5)


scene black with dissolve
$ renpy.pause (0.3)
$ skipbeginning = False

if persistent.c1blood == True:
    
    if persistent.c1invhigh == True:
        
        stop music fadeout 1.0

        $ renpy.pause (0.3)

        play sound "fx/system3.wav"

        call syscheck from _call_syscheck_3
        
        $ skipplace = "1"
        
        call skiptut from _call_skiptut_2
        
        if skipbeginning == False:

            if system == "normal":
            
                s "My records indicate you have already experienced this section in a satisfactory manner. Would you like to skip to the character selection?"
            
                #play sound "fx/system3.wav"
            
                #s "Warning: In this scene, skipping ahead this way instead of using the skip buttons (CTRL and TAB) may prevent you from experiencing alternative choices and outcomes that you haven't seen before. These may only be minor, though."
            
            elif system == "advanced":

                s "It looks like you've seen this before. Skip to the character selection?"
            
                #play sound "fx/system3.wav"
            
                #s "I have to warn you, though. If you do this here instead of just using CTRL and TAB, you may end up missing some minor changes you haven't seen before."
                
            else:
                
                s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the character selection."
                
                #play sound "fx/system3.wav"
                
                #s "If you want to do things this way instead of just using the skip buttons like a civilized person, you could end up missing some choices you haven't made before. But considering how far you've come, you probably won't miss much."
            
        $ skipbeginning = False
        
        menu:
            
            "Yes. I want to skip ahead.":
                
                play sound "fx/system3.wav"
                
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                
                $ blood = True

                $ inv = "high"

                $ food = "fish"
                
                $ answers = 6

                $ persistent.skipnumber += 1
                call skipcheck from _call_skipcheck_2
                
                stop music fadeout 1.0
                
                jump sceneselect
            
            "No. Don't skip ahead.":

                play sound "fx/system3.wav"
            
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

                play music "mx/sail.ogg" fadein 1.0
                
                $ renpy.pause (0.5)

#$ renpy.fix_rollback()

show cgseb at Pan((0, 302), (0, 0), 7.0) with dissolvemed
$ renpy.pause(4.0)

scene o at Pan((0, 250), (0, 250), 0.1)
with fade

show sebastian normal b with dissolve

#play music "mx/sail.ogg"

Sb "H-Hello! You must be [player_name]. I'm Sebastian, and I'll be your escort... or s-security, I suppose. Usually I work for the police, though. Nice to meet you."

m "He seemed a lot smaller than Remy, and when he somewhat nervously extended his arm towards me, I noticed he apparently only walked on his hind legs, the two forelimbs instead having distinct arms, hands and fingers."

menu:
    
    "Shake his hand.":
        m "When I took his hand into mine to shake it gently, I could feel the individual bumps and scales on his rough skin."
        c "Nice to meet you too, Sebastian. So, where are you taking me?"
        
    "Don't shake his hand.":
        c "Nice to meet you too, Sebastian. So, where are you taking me?"

        $ evilpoints += 1
        
        
    "Kiss his hand.":
        m "When I took his hand into mine, preparing to kiss it, I could feel the individual bumps and scales on  his rough skin."
        play sound "fx/kiss.wav"
        $ renpy.pause (1.0)
        show sebastian shy b with dissolve
        c "Nice to meet you too, Sebastian. So, where are you taking me?"
        show sebastian normal b with dissolve

#$ renpy.fix_rollback()


Sb "Straight to business, eh? We're going to visit the plant where they are making your generators. They have some news for you, or so I've heard."
Sb "Reza will be there, too."
c "Sounds great."
Sb "Just follow me."
#Sb "Follow me, please."

play sound "fx/steps/clean2.wav"

scene black with fade
$ renpy.pause (0.5)
scene town2 at Pan ((0, 400), (0, 400), 0.0) with fade
nvl clear

window show
n "While we walked, I was under the impression we were purposefully avoiding the busier parts of the town, instead straying towards the edges and small alleys as to not garner too much attention." 
n "Even then, we got the occasional stare."

n "After just a couple of minutes, we arrived at our destination where we were met by Reza, as well as yet another dragon, a vicious looking beast that didn't stay too close to him."

stop music fadeout 1.0
window hide

scene black with dissolve
$ renpy.pause (0.3)
show cgarrival at Pan((0, 302), (0, 0), 10.0) with dissolvemed
$ renpy.pause(5.0)

stop music fadeout 1.0

scene fac1 with fade
#show reza normalx with dissolve
show reza normal with dissolve

play music "mx/basicguitar.ogg"

Rz "Hey."
c "Reza, long time no see."
Rz "How true that is. Good to finally see another human face around here." 
#Rz "Good to finally see another human face around here." 
Rz "What a coincidence to have you, of all people, show up."
c "Yeah, guess those degrees aren't so useless after all." 
c "By the way, who's your friend?"
Rz "Just my bodyguard, same as yours. Don't bother with him, he doesn't talk much."

menu:
    "I bet he'd win in a fight with mine, though.":
        Rz "Hah."
        $ evilpoints += 1

    "He looks grumpy.":
        $ renpy.pause (0.5)
        show reza amused with dissolve
        Rz "That's what he always looks like. And yes, that does mean he's always grumpy."
        
        
    "Just like you.":
        $ renpy.pause (0.5)
        show reza annoyed with dissolve
        Rz "Very funny."
        

hide reza with dissolve

m "The two dragons exchanged a few words and as I met the gaze of the larger, tenebrous dragon a few paces from us, Sebastian turned towards me and spoke up again."
    
show sebastian normal b at right with dissolve

show maverick normal flip at left with dissolve

Sb "Hey, [player_name], this is Maverick."
c "Nice to meet you." 
Mv "Yeah, whatever. Just don't expect me to give you any special treatment like everyone else is and we'll be good."
c "What are you talking about?"
Mv "So you're saying you haven't noticed the stares and how they all treat you like you're the next messiah or something?"
c "N-No.. I just thought..."

hide sebastian with easeoutright
show reza angry at Position(xpos = 0.8) with easeinright

Rz "We're not the ones making a big deal out of this, you are. We're just here to get what we agreed on and then we'll be gone. If anything, I'd actually prefer if you left us alone, but you're the one who insists on following me around wherever I go."

play sound "fx/growl.wav"

show maverick angry flip with dissolve

m "A growl escaped the darker dragon's trembling lips as he bared his teeth at Reza."

show sebastian normal b at right with easeinright

Sb "Alright, alright, that's quite enough. Let's just all go inside already, shall we?"
c "After you."

stop music fadeout 1.0
scene black with dissolve
scene facin2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

nvl clear
$ renpy.pause (1.3)
m "The crisis was quickly averted as we entered the building, which was characterized by its many floors, high ceilings and long, narrow hallways as Sebastian led us to our destination."
window hide

show anna normal b with dissolve

play music "mx/general.ogg"

"???" "There you are. I was waiting for you."

scene black with dissolve
$ renpy.pause (0.3)
show cganna at Pan((0, 302), (0, 0), 7.0) with dissolvemed
$ renpy.pause(5.0)
scene facin 
show anna normal b at right
with fade

show sebastian normal b flip at left with easeinleft

Sb "Wait a minute, I thought we were going to meet the guys from production. What are you doing here?"

show anna smirk b with dissolve

"???" "They're only coming in later today, so you'll just have to make do with me."

show anna normal b with dissolve

Sb "I see." 
Sb "Well, [player_name], this is Anna. She kinda manages this building, though actually she's more involved with the research wing rather than production and engineering."
c "Nice to meet you."
An "My pleasure. I have something for you, by the way. It'll take them a while to make all the generators we promised, but we've got one for you here. Feel free to send it home and give it a test."

$ persistent.annamet = True

play sound "fx/box1.wav"

show reza normal flip at Position(xpos = 0.45) with easeinleft

Rz "That's great. I'll take it."

play sound "fx/box2.wav"

c "Looks a little small, if you ask me."
An "Don't underestimate its power. Oh, and do be careful not to drop it."
Rz "Sure. I'll be waiting outside while you do your thing, [player_name]."

show reza normal 

$ renpy.pause (0.3)

hide reza with easeoutleft

Sb "I suppose I'll wait for you outside as well."

show sebastian normal b

$ renpy.pause (0.2)

hide sebastian normal b flip with easeoutleft

c "What thing?" 
An "Oh, have you brought the PDA?"
c "Of course. Here you go."

play sound "fx/pda.wav"

An "Alright, now to give this thing a test run..."

#play sound "fx/clicks.wav"

m "The PDA lit up as her hands swiftly moved around its interface in calculated motions."

An "By the way, would you consider letting me run some tests on you as well? It would only take a drop of your blood."
c "What? Why?"
An "I work in biology, so obviously this kind of thing would be very interesting to us. I'd share the results with you, of course."

$ blood = False

menu:
    "I'd rather not.":
        
        if persistent.havetestresults == True:
            
            show anna sad b with dissolve
            An "Really? I thought you wouldn't mind."
            show anna normal b with dissolve
            
            An "Well, maybe next time."
        
        else:
            
            $ renpy.pause (0.5)
            show anna sad b with dissolve
            An "That's a shame..."
            show anna normal b with dissolve

    "Sure, why not.":
        An "Great."
        m "She was quick to produce a small device from a drawer, which from a glance reminded me a lot of a test tube."
        show anna smirk b with dissolve
        An "Now, if you would give me your hand, please."
        m "As I reached out to her, she took my hand into hers before she pressed the device into the back of my hand. I winced as pain jolted through my hand. Something sharp drove itself through my skin and, shortly afterwards, a droplet of blood was sucked into the tube attached to the small needle."
        show anna normal b with dissolve
        An "Thanks."
        c "You're... welcome?"
        $ blood = True
        
        if persistent.c1blood == False:

            $ persistent.c1blood = True
            
            $ achievement.grant("Blood Donation")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_4
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You gave Anna your blood!{image=image/ui/status/havetestresults.png}"
                
            elif system == "advanced":

                s "You gave Anna your blood?{image=image/ui/status/havetestresults.png}"
                
            else:
                
                s "You gave Anna your blood? Oh, well...{image=image/ui/status/havetestresults.png}"
                
                

An "Looks like your PDA is good, by the way, so we're just about done here."
An "And since we're both in biology, it could be interesting if you want to meet me some other time as well. Here's my number."
c "Alright."

show anna smirk b with dissolve

An "See you soon."

scene fac1 with wiperight

c "Well, that was interesting."

show reza normal with dissolve

Rz "Did she ask you for your blood too?"
c "Yeah..."
Rz "Did you give it to her?"

menu:
    "No.":
        Rz "Me neither. I mean, if we're going to give them our body, let's not do it for free, right?"
        c "Sure."
        $ evilpoints += 1

    "Yes.":
         Rz "Oh... Well, it's your choice. We've got no idea what they might do with it, though."

c "I'm getting hungry. How about some breakfast?"
Rz "I'm all for it. I can't stand early mornings like this."

show sebastian normal b flip at left with easeinleft

Sb "That shouldn't be a problem. There's a café not far from here. What do you say, Mavers?"

show maverick normal at Position(xpos = 0.9) with easeinright

Mv "I wouldn't mind to grab a bite myself."

Sb "That settles it, then."
stop music fadeout 1.0
scene cafe with fade

if persistent.c1skip == True:

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_5
    
    $ skipplace = "2"
    
    call skiptut from _call_skiptut_3
    
    if skipbeginning == False:

        if system == "normal":
        
            s "My records indicate you have already experienced this section in a satisfactory manner. Would you like to skip to the investigation?"
        
            #play sound "fx/system3.wav"
        
            #s "Warning: In this scene, skipping ahead this way instead of using the skip buttons (CTRL and TAB) may prevent you from experiencing alternative choices and outcomes that you haven't seen before. These may only be minor, though."
        
        elif system == "advanced":

            s "It looks like you've seen this before. Skip to the investigation?"
        
            #play sound "fx/system3.wav"
        
            #s "I have to warn you, though. If you do this here instead of just using CTRL and TAB, you may end up missing some minor changes you haven't seen before."
            
        else:
            
            s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the investigation."
            
            #play sound "fx/system3.wav"
            
            #s "If you want to do things this way instead of just using the skip buttons like a civilized person, you could end up missing some choices you haven't made before. But considering how far you've come, you probably won't miss much."
        
    $ skipbeginning = False
    
    menu:
        
        "Yes. I want to skip ahead.":
            
            play sound "fx/system3.wav"
            
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            $ food = "fish"

            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_3

            play music "mx/threat.ogg" fadein 2.0
            
            jump investigation
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

play music "mx/jazzy.ogg"
m "Luckily for us, the café was mostly empty when we arrived, as it was still pretty early in the day. Reza was quick to lead me to a table for two, prompting the dragons to get one of their own at the other side of the restaurant."

show reza annoyed with dissolve

Rz "Eugh, finally. I can't stand that guy being on my tail all the damn time."

menu:
    "They say it's for our own security.":
        Rz "I'm very much aware that is what they're saying."
        
    "It does seem rather strange that they need someone following us everywhere.":
        Rz "Yeah, I'm not buying their shtick about how it's to keep us safe."
        $ evilpoints += 1
        
    "Maybe he just likes you a lot.":
        Rz "..."

show reza normal with dissolve

m "We were approached by an individual who appeared to be the waitress of the café. She was an interesting-looking dragon, who - unlike the others I had seen so far - was more akin to a wyvern, possessing two rather large wings as her forelimbs, which resembled those of an oversized bat."

#scene black with dissolve
#scene cgadine with dissolveslow
#$ renpy.pause(4.0)
#scene cafe
show reza normal at Position(xpos = 0.7) with ease
#with fade

show adine normal b flip at left with easeinleft

"???" "Oh, it's the humans!"

menu:
    "You were able to correctly identify our species based on what we look like, congratulations!":
        $ renpy.pause (0.5)
        show reza amused with dissolve
        $ evilpoints += 1

    "Wait, where?":
        $ renpy.pause (0.5)
        show reza annoyed with dissolve
        Rz "..."
    "Oh, it's a dragon!":
        $ renpy.pause (0.5)
        show reza annoyed with dissolve
        Rz "..."
        
        
show adine giggle b flip with dissolve
"???" "That's a good one."
show reza normal with dissolve
show adine normal b flip with dissolve
Ad "Welcome to our establishment. My name's Adine, and I'll be your waitress today. What can I bring you two?"

$ persistent.adinemet = True

menu:
    "Just a coffee for me.":
        $ food = "coffee"
        Rz "Yeah, me too. Just make it quick."
        Ad "Sure thing. Two coffees coming right up."
        
    "How about some scrambled eggs with bacon?":
        $ food = "eggs"
        Rz "Yeah, me too. Just make it quick."
        Ad "Sure thing. Two scrambled eggs with bacon coming right up."

    "Today's special.":
        $ food = "fish"
        Rz "Yeah, me too. Just make it quick."
        Ad "Sure thing. Two specials coming right up."

        $ mp.fish = True
        $ mp.save()

show adine normal b
$ renpy.pause (0.3)
hide adine with easeoutleft

show reza at center with ease

Rz "As I was saying, if you look at the big picture, don't you think there's just something... off about this whole place? Where is it, really?"
#Rz "Don't you think there's just something... off about this whole place?"
Rz "If this is supposed to be a completely separate place from Earth or even a different dimension, some things just don't add up. Don't you think so too?"

menu:
    "I'm not sure.":
        pass
        
    "Yeah, I've noticed it too.":
        pass
        
    "Let me just grab my tinfoil hat real quick.":
        $ renpy.pause (0.5)
        show reza annoyed with dissolve
        Rz "I've been here much longer than you have been. Maybe you'll see soon enough."
        $ evilpoints += 1

Rz "I can't really say much more with you-know-who over there. He's probably listening to us right now."

menu:
    "Yeah, he's a charming fellow.":
        pass
        
    "He doesn't seem so bad to me.":
        pass
        
    "What a creep.":
        $ evilpoints += 1

m "When I let my gaze wander, I saw that Maverick was looking in my direction. Our eyes met briefly, his expression not showing any discernible emotion, while I wondered whether it had just been a coincidence or if he really was able to hear us from the distance."
Rz "I do have some theories... and if I'm right, we might be in trouble."
c "What kind of trouble? What are you talking about?"
Rz "Shh, be quiet. I'll let you know more as soon as I can. But for now, let's just play along. After all, we already have one of these babies."
m "He patted the generator's box for emphasis."
Rz "God knows we need them."
c "Oh, there she comes."

show reza at Position(xpos = 0.7) with ease

show adine normal b flip at left with easeinleft

m "The female returned, astounding me with her ability to balance the dishes on the edges of her wings. She placed her forelimb on the table and proceeded to move the dishes from her wing to us with a gentle push of her snout."

play sound "fx/dishes.wav"

if food == "fish":
    Ad "There you go. Watch out, it's hot."
    
else:
    Ad "There you go. Enjoy!"

menu:
    "Thanks.":
        Ad "You're welcome."
    
    "Now shoo, scaly-face.":
        $ renpy.pause (0.5)
        show adine annoyed b flip with dissolve
        Ad "..."
        show reza amused with dissolve
        $ evilpoints += 1
        
    "[[Say nothing.]":
        $ renpy.pause (0.5)
        
show adine normal b
$ renpy.pause (0.3)
hide adine with easeoutleft
show reza at center with ease

if food == "coffee":
    play sound "fx/coffee.wav"
    m "To be honest, I was a little skeptical of the kind of coffee they might come up with in a place like this, but after a mouthful I had to admit it wasn't so bad. I've certainly had much worse before."
    
elif food == "eggs":
    m "I was wondering what kind of breakfast could be had in a place like this, but I was pleasantly surprised to find it quite as I was used to. The only real difference was that they apparently didn't use cutlery."
    
else:
    m "Apparently today's special consisted of an odd-looking fish of some sort. I was a little hesitant to try it, but considering the steam coming from it, it was probably better to wait a few minutes anyway."

m "When the waitress brought out meals to the two dragons across the café and exchanged a few words with them, Reza leaned forward and whispered something to me."
Rz "I'll send you a letter with a coded message later. You'll know what to do."
m "Reza rose from his seat before he made it known to me that he still had a few things to do and left the restaurant, followed shortly after by the larger of the two dragons."

show reza normal flip 
$ renpy.pause (0.3)
hide reza with easeoutright

if food == "fish":
    c "But you haven't even touched your... fish." 
    m "I wasn't in a hurry, so I spent a few more minutes in contemplation while I looked out the window." 
    m "Not that this whole situation was already bizarre enough, there was also now the vague sense of danger conveyed by Reza's earlier words. I did not even have an idea what kind of threat might be lurking out there."
    m "Eventually, I took a bite of my somewhat unusual breakfast. While I already thought the smell was quite peculiar, the taste had been even worse. I imagined it might be the kind of delicacy that had an acquired taste. One that I certainly hadn't acquired yet. I decided to get outside before it was too late."
    $ mp.vegetarian = False
    $ mp.save()
    
elif food == "coffee":
    c "Laters."
    m "I wasn't in a hurry, so I spent a few more minutes in contemplation while I looked out the window and finished my coffee." 
    m "Not that this whole situation was already bizarre enough, there was also now the vague sense of danger conveyed by Reza's earlier words. I did not even have an idea what kind of threat might be lurking out there."
    m "Eventually, I got up, ready to be on my way for whatever else the day might bring."

else:
    c "Laters."
    m "I wasn't in a hurry, so I spent a few more minutes in contemplation while I looked out the window and finished my breakfast." 
    m "Not that this whole situation was already bizarre enough, there was also now the vague sense of danger conveyed by Reza's earlier words. I did not even have an idea what kind of threat might be lurking out there."
    m "Eventually, I got up, ready to be on my way for whatever else the day might bring."

show sebastian normal b with dissolve

Sb "Are you done?"
c "Sure am."
Sb "How'd you like it?"

if food == "fish":
    c "I'll just say it's probably not for me."
    Sb "And you wouldn't be the only one to say that. You better wait outside just in case it decides to come up again."

    if persistent.c1fish == False:

        $ persistent.c1fish = True
        
        $ achievement.grant("Bravery")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_6
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You tried the odd-looking fish!"
            
        elif system == "advanced":

            s "You tried the odd-looking fish. How brave."
            
        else:
            
            s "You tried the odd-looking fish. But you weren't brave enough to eat it all." 
    
else:
    c "It was alright."
    Sb "Glad you enjoyed it. Just wait outside and I'll handle the rest here."

c "Sure thing."

stop music fadeout 1.0

scene town3 with dissolve

window show

play music "mx/menu.ogg" fadein 1.0

n "I stepped outside, taking in the scenery of this strangely familiar world."
n "In the short time I was here, I had already found the similarities between their world and our own utterly fascinating."
n "After all, we were talking about an unmapped place with a never-before-seen form of life."
n "As far as discoveries were concerned, even something as simple as a new unicellular organism or even bacteria would have been remarkable."
n "Yet here I was, standing in the middle of a village evidently built by this race of intelligent, talking dragons with a society not unlike our own."
n "Reza didn't seem to share the same interest and instead was more smitten with the generator, but given our reasons for coming here in the first place, I couldn't blame him for his enthusiasm being focused on something else."
stop music fadeout 1.0

window hide
nvl clear

m "My thoughts were interrupted as something suddenly zipped past me just a little too close, causing me to stumble back. It was a rather small dragon with a bag clamped in its maw who apparently had somewhere to be." 

scene black with dissolve
$ renpy.pause (0.5)
scene cgvara at Pan ((0, 326), (580, 0), 5) with dissolvemed
$ renpy.pause(3.5)

#scene black with dissolvemed
scene town3 with fade

m "I regained my footing and watched as it disappeared into the distance. Even though I'd seen enough dragons to recognize their variations in size, color, and other attributes, I guessed this one must have been a juvenile of its species.\nShortly afterwards, Sebastian joined me outside, having taken care of the tab."

#window hide
#$ renpy.pause (0.5)

show sebastian normal b with dissolve
play music "mx/sail.ogg" fadein 1.0
Sb "I gave her a generous tip on your behalf. I hope you don't mind."

menu:
    "Of course not, as long as I don't have to pay the bill.":
        Sb "Don't worry about it."

    "Actually, I do.":
        Sb "Why's that?"
        c "The whole thing where she lost it, because we were humans. How unprofessional. Besides, I don't believe in tipping."
        Sb "Well, too late for that now."
        $ evilpoints += 1
        
    "How nice of you.":
        pass

Sb "In any case, now that you've given us the PDA and Reza has the generator, you're free for today. So, if you want to go anywhere in particular, let me know, or I could show you around town."
m "I was tempted to be given a tour, but considering Reza's words, I wanted to be careful and not  stray too far without knowing more about this world first."
c "I think I'll stay home for today. I still have to get used to everything, you know?"
Sb "I'll just accompany you back, then."

play sound "fx/steps/clean2.wav"

scene black with fade
$ renpy.pause (0.5)
scene o at Pan((0, 250), (0, 250), 0.1)
with fade

show sebastian normal b with dissolve

Sb "There we are."
c "Home, sweet home. For now, at least."
Sb "Well, if you need anything, I'll be outside until my shift ends. Otherwise, I'll see you tomorrow."
c "Thanks, see you tomorrow."
Sb "See ya!"

$ renpy.pause (0.3)

hide sebastian with easeoutleft

$ renpy.pause (0.3)

play sound "fx/door/doorclose3.wav"
stop music fadeout 1.0
$ renpy.pause (1.0)

nvl clear
window show
play music "mx/basicguitar.ogg" fadein 1.0

n "I hadn't really looked at the apartment much, so I spent the rest of the day investigating it and relaxing. I considered checking out some of the phone numbers Remy had left me, but I thought it was better to keep a low profile for now."
n "I found the kitchen fully stocked with plenty of groceries, though the variety was wasted on me. I hadn't been a particularly great cook in the first place, but what was more, I didn't even recognize some of the things I found there." 
n "Whether they were edibles that we had back home that I just didn't know about, or something completely alien I wasn't sure, but I didn't want to take the risk of eating anything I didn't know."
n "After all, it was possible that some of the comestibles might be fine for them to eat, but still be poisonous to us."
nvl clear
n "I was also glad to find a shelf that was filled to the brim with a variety of books."
n "While I found the subject matter of {i}Man: Myth or Reality?{/i} to be quite intriguing, I had to give up after just a few pages due to its exceptionally dry writing style, which I wasn't inclined to enjoy at the moment." 
n "In the end, I settled for an adventure novel about a dragon archaeologist who stumbles upon the remains of a long lost human civilization, after which she is hunted by an evil organization who wants to use the found magical artifacts for its own, nefarious purposes."
n "While entertaining, I had to admit that it reminded me a little too much of the trashy novels we had at home. I certainly found it amusing that certain tropes were not really unique to us as a species, though I wondered whether this kind of literature had fallen into disfavor here as it had back where I had come from." 
nvl clear
n "I was reading a particularly exciting scene, in which the hero, Sheridan, uses one of the magical artifacts shaped like a pair of human hands holding a scepter with a globe at the top to prevent herself from being crushed and ground into a bloody pulp by an ancient human temple's moving walls, when I suddenly heard the doorbell ring."

play sound "fx/door/doorbell.wav"

$ renpy.pause(2.0)

#window hide

#n "When I opened the door, it was Sebastian again, my little follower."

#window hide

#show sebastian normal b flip at left with easeinleft

#Sb "Hey, I don't want to interrupt your afternoon and all, but I've got something for you."
#m "In the grasp of his claws was a rather plain looking envelope, which he handed to me."
#c "Oh, a letter. Who's it from?" 
#Sb "Reza."
#c "Well, thank you. See you tomorrow, then."
#Sb "See ya!"
#nvl clear

#show sebastian normal b
#$ renpy.pause (0.3)
#hide sebastian with easeoutleft

window hide

stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
#$ renpy.pause(1.0)

$ renpy.pause (1.5)

show black with dissolve
#nvl clear
#window hide
$ renpy.pause (0.5)
show meetinglorem at Pan((540, 0), (540, 608), 10.0) with fade

$ renpy.pause (8.5)

nvl clear

hide black
hide meetinglorem
show lorem happy b flip at Position (xpos = 0.35)
with fade

"???" "Hello there! Would you please sign here?"

c "I'm not signing away my rights with this, am I?"

"???" "I've got a letter for you that requires signature confirmation."

c "I see."

m "Looking over the clipboard the small dragon was holding up to me, I saw that the sender of the letter in question was Reza."

play sound "fx/signature.ogg"

c "There you go."

Lo normal b flip "I'm Lorem, by the way. Would you mind if I asked you a few questions?"

$ persistent.loremmet = True

show lorem at Position (xpos = 0.2) with ease

show sebastian normal b at right with easeinright

Sb "What is this about?"

Lo happy b flip "I'm just making small talk."

Sb disapproval b "Wait a minute... I recognize you. You tried to do the same thing with Reza! Maybe I should report you to your superiors for your inappropriate behavior toward your clients."

Lo sad b flip "But it's important! Please, just let me talk to [player_name] for a few minutes!"

Sb normal b "You know how it is. If you want an interview with one of the humans, you'll have to get permission from the proper authorities."

Lo relieved b flip "Help me out here, [player_name]. As an ambassador, you care about the accurate portrayal of humans in the media, don't you?" #he wants to ask the mc a few questions because of the game he is making and wants to portray humans accurately

Lo happy b flip "Then you should talk to me. Otherwise, someone else will fill in the blanks and who knows what they will come up with."

Lo normal b flip "Let me show you something."

play sound "fx/rummage3.ogg"

m "The small dragon opened his bag, rummaging through a number of letters and small packages."

Lo think b flip "Huh, I think I lost it." 

Lo happy b flip "Anyway, I wanted to show you some pictures of what people think humans look like. On some of them, they have like four heads and look nothing like you. It's crazy!"

c "What are you, Lorem? A reporter?"

Lo normal b flip "No, I'm just..."

Sb normal b "Do you want me to remove him, [player_name]?"

c "Is what he is saying true?"

Sb drop b "Yeah, I guess..."

c "I see. That sounds pretty interesting, though."

c "Alright, you can leave your number here and maybe I'll call you later, but that's all I can promise."

Lo happy b flip "Thank you! Thank you so much!"

play sound "fx/scribblex.ogg"

m "He quickly produced a small sheet of paper and scribbled his number on it. Afterwards, he sheepishly presented it with both hands."

Sb disapproval b "Alright, you got what you wanted. Off you go, now."

$ renpy.pause (0.3)

show lorem happy b

$ renpy.pause (0.3)

hide lorem with easeoutleft

$ renpy.pause (0.2)

show sebastian at center with ease

#$ renpy.pause (0.3)

Lo "Eeeeeeeeeeeee~!"

Sb normal b "Sorry about that."

c "Don't worry about it."

Sb "I guess that should be all. I'll see you tomorrow, then."

c "Right."

$ renpy.pause (0.3)

hide sebastian with easeoutleft

play sound "fx/door/doorclose3.wav"

$ renpy.pause(1.0)

m "With all the commotion, I almost forgot that I was also still holding Reza's letter."

window show

play sound "fx/envelope.wav"

n "Within the plain envelope was a similarly plain sheet of paper with his handwriting." 
n "When I started reading, however, I saw that his wording was so full of the pleasantries I knew he hated that I assumed every word of it was faked as to conceal its true intent."
n "He did mention I'd know what to do, but I was unsure of how I was supposed to decode the letter's secret message."
n "I didn't remember ever having a conversation about this topic with him, yet he still relied on me to remember whatever it was that I was missing. Or he thought I would just be able to figure it out on my own."
n "This is what it said:"
nvl clear
n "Hello, my dear friend."
n "I hope this letter reached you swiftly and in good condition." 
n "Unfortunately, we were not able to catch up earlier, so I wanted to write you this letter. How have you been these last few years? What have you been doing? How's the family?"
n "I feel like there is so much we should talk about, since we have not seen each other much recently. At least we have a chance to do so in this form."
n "Quite an exciting venture we are on now, right? How have you liked it here so far? Made any dragon friends yet?" 
n "Haha." 
n "Anyways, I will be looking forward to your reply soon."
n "Best regards,"
n "Reza"

window hide
nvl clear

m "Various things came to mind. Only reading certain words or letters was one that I thought of immediately, but I couldn't make out anything after trying to find a system within its array of letters and lines. Maybe I had to look more carefully."

$ wronganswers = 0
$ sebastianmurder = True
$ donothing = True
$ government = True
$ flee = True
$ pizzaparty = True
$ steallibrary = True
$ knowmaverick = True
$ breakintoplant = True
$ linesread = True
jump menu3
label menu3:

    menu:
    
        "I think I know its meaning.":
            jump menu1
            label menu1:
        
                m "After looking at it for a while, I came to the conclusion that the secret message said that Reza wanted me to:"
                jump menu2
                label menu2:
                    menu:
                
                        "Plan Sebastian's Murder." if sebastianmurder:
                            call increasing from _call_increasing
                            $ sebastianmurder = False
                            jump menu2
                
                        "Do nothing while he figures out what to do." if donothing:
                            call increasing from _call_increasing_1
                            $ donothing = False
                            jump menu2

                        "Find out more about their government." if government:
                            call increasing from _call_increasing_2
                            $ government = False
                            jump menu2
                
                        "Flee through the portal as soon as possible." if flee:
                            call increasing from _call_increasing_3
                            $ flee = False
                            jump menu2
                            
                    
                        "[[Look at the letter again.]":
                            nvl clear
                            window show

                            play sound "fx/envelope.wav"


                            n "Hello, my dear friend."
                            n "I hope this letter reached you swiftly and in good condition." 
                            n "Unfortunately, we were not able to catch up earlier, so I wanted to write you this letter. How have you been these last few years? What have you been doing? How's the family?"
                            n "I feel like there is so much we should talk about, since we have not seen each other much recently. At least we have a chance to do so in this form."
                            n "Quite an exciting venture we are on now, right? How have you liked it here so far? Made any dragon friends yet?" 
                            n "Haha." 
                            n "Anyways, I will be looking forward to your reply soon."
                            n "Best regards,"
                            n "Reza"

                            window hide
                            nvl clear
                            
                            jump menu1

                        "[[Show more options.]":
                            jump menu1x

        "Read between the lines." if linesread:
            m "Lines, of course. Maybe I was supposed to read between them? I didn't have an implement on me with which I would've been able to read fine print, though with this handwritten letter, I doubted Reza could have done anything of the sort."
            $ linesread = False
            jump menu3
            

        "Look elsewhere for hints.":
            jump elsewhere
            
label menu1x:
    menu:
        "Have a pizza party." if pizzaparty:
            call increasing from _call_increasing_4
            $ pizzaparty = False
            jump menu1x
                
        "Steal a certain book from the library." if steallibrary:
            call increasing from _call_increasing_5
            $ steallibrary = False
            jump menu1x
                
        "Find out where Maverick lives." if knowmaverick:
            call increasing from _call_increasing_6
            $ knowmaverick = False
            jump menu1x

        "Break into the manufacturing plant." if breakintoplant:
            call increasing from _call_increasing_7
            $ breakintoplant = False
            jump menu1x
                    

        "[[I am unable to decode the message.]":
            jump menu3
            
        "[[Show more options.]":
            jump menu2


label increasing:
    if wronganswers == 0:
        c "(No, that's not it.)"
        $ wronganswers += 1
        return
    elif wronganswers == 1:
        c "(That's not it, either.)"
        $ wronganswers += 1
        return
    elif wronganswers == 2:
        c "(Now I'm just guessing and hoping to get lucky.)"
        $ wronganswers += 1
        return
    elif wronganswers == 3:
        c "(I don't feel like any of these options is actually right.)"
        $ wronganswers += 1
        return        
    elif wronganswers == 4:
        c "(Why am I even still doing this?)"
        $ wronganswers += 1
        return
    elif wronganswers == 5:
        c "(I have now reached the point where, statistically speaking, I should have gotten the right one. Either I'm just exceptionally bad at guessing or I should start looking elsewhere.)"
        $ wronganswers += 1
        return
    elif wronganswers == 6:
        c "(It was a fifty-fifty chance, but then the right answer wasn't there to begin with.)"
        $ wronganswers += 1
        return
    elif wronganswers == 7:
        c "(Okay, this was the last option and it was still wrong. If that's not enough to prompt me to finally start looking elsewhere, I don't know what else will.)"
        $ wronganswers += 1
        return
            
label elsewhere:
    $ lookedbehindthebooks = True
    $ desireunread = True
    $ assaultunread = True
    $ bornunread = True
    $ priceunread = True
    $ ixomenunread = True
    $ medstaken = 0
    $ medsuntaken = True
    $ uncheckedshower = True
    $ unmeat = True
    $ unmilk = True
    $ crackedeggs = 0
    $ uneggsgone = True
    $ undrunk = True
    $ undate = True
    $ unfig = True
    $ unolive = True
    $ unplum = True
    $ unpear = True
    $ ungrape = True
    $ booksread = 0
    $ lookatindividualbook = True
    m "Or maybe he referred to the fact that we were both given an apartment. Considering the things they provided for us, maybe I just had to find the right object to decode the message. There were many everyday items here, though, and of course I still had no idea what in particular I was looking for."
    jump menu5
    label menu5:
        
        
        menu:
            
            "Look at the bookshelf.":
                m "The bookshelf was stocked with quite a variety of books on different topics."
                jump menu6
                label menu6:
                    
                    
                    menu:
                        
                        "Look at an individual book." if lookatindividualbook:
                            c "(Maybe it has something to do with the books? The shelf is full of them, but I suppose the hint could be hidden inside one of them.)"
                            jump menubooks
                            label menubooks:

                                if booksread == 5:

                                    $ lookatindividualbook = False
                
                                    if persistent.c1books == False:

                                        $ mp.bookworm = True
                                        $ mp.save()
                                        
                                        $ persistent.c1books = True
                                    
                                        $ achievement.grant("Bookworm")
                                        
                                        $ persistent.achievements += 1
                                        
                                        call syscheck from _call_syscheck_7
                                        
                                        play sound "fx/system.wav"
                                        
                                        if system == "normal":
                                        
                                            s "You read a bunch of books!"
                                            
                                        elif system == "advanced":

                                            s "You read a bunch of books. Good for you."
                                            
                                        else:
                                            
                                            s "You read a bunch of books. ...Like you expected the hint to show up in them or something."

                                menu:
                                    c "Which book should I look into?"

                                    "Draconic Desire" if desireunread:
                                        show cover1 with fade
                                        nvl clear
                                        $ renpy.pause(1.0)
                                        play sound "fx/envelope.wav"
                                        window show
                                        n "I was so young and naive back then." 
                                        n "Barely having reached the age at which the arduous process of finding a mate, settling down and starting a family became expected, yet none of my peers interested myself. They were childish and crude and uncultured." 
                                        n "I was lost in a sea of uncertainty, drifting, hoping to be found by the one, one day. And then I did. How fast time flies when you're happy, I can't believe this was just two weeks ago. Two weeks ago I found the one, my truest soulmate there ever could be." 
                                        n "Like a wrecking ball, he came out of nothing, breaking all the barriers and entered my life. Two weeks ago, I was nothing. Today, I am the happiest dragon alive. Who knew that out of all the people alive, it only took the right one to right life itself." 
                                        n "Who knew that to meet the perfect one, the only thing you needed was..."
                                        window hide
                                        hide cover1 with fade
                                        c "(I don't think there's anything in here.)"
                                        c "(And who let this mess ever get to print? Sheesh.)"
                                        $ desireunread = False
                                        $ booksread += 1
                                        jump menubooks
                                        
                                    "Assault of the Humanoids from Outer Space" if assaultunread:
                                        show cover3 with fade
                                        nvl clear
                                        $ renpy.pause(1.0)
                                        play sound "fx/envelope.wav"
                                        window show
                                        n "Arc 1"
                                        n "It was a dark and stormy night. Relentlessly pouring was the rain outside, periodically interrupted by the loud echo of thunder, again and again. So quick had its roaring staccato become that it almost seemed like someone was pounding against the door. No, someone really was pounding on the door right now. The door swiftly opened and the moment for which the house's owner had waited decades finally was here."
                                        n "\"Not on the field of battle do you meet me, human scum, but in the comforts of my own home do you seek to assassinate me? FEEL MY WRATH! MAY IT LEAD YOU TO A SLOW AND PAINFUL D-E-A-T-H!\" he screamed at the top of his lungs."
                                        n "\"Your resistance will only temper my blade, inferior creature. TASTE MY BLADE AND DIE FROM IT.\" the reply wryly came from the human invader standing within the door frame."
                                        nvl clear
                                        n "Hiro quickly stabbed him with his Magi-pen, a lethal hit which caused the human invader to slump to the ground instantly, his last words being \"D...Damn y-you... Hiro.. this... i-is... not... over... y-y... yet.\" while he melded into a red blotch, blotching up Hiro's carpet."
                                        n "Hiro looked up into the sky and realized all the thunder and rain had really been the UFOs of the invaders, numerous enough as to rival the raindrops falling from the sky."
                                        n "This was the moment when he knew it was too late. This meant WAR."
                                        window hide
                                        hide cover3 with fade
                                        c "(Really? An invasion by human aliens? Is that what they think we're like?)"
                                        $ assaultunread = False
                                        $ booksread += 1
                                        jump menubooks

                                        
                                    "Born to Serve" if bornunread:
                                        show cover2 with fade
                                        nvl clear
                                        $ renpy.pause(1.0)
                                        play sound "fx/envelope.wav"
                                        window show
                                        n "Chapter 1: Rise from the Ashes"
                                        n "From the day I was born, I knew I was destined for greatness. As a member of the Avdonian household, nothing less was expected from me."
                                        n "My father, Avdon VI made sure of that. My mother, however, was a worm. Not literally, mind you. She was not some sort of annelid squirming beneath the earth and living in filth. No, she was just what I would describe as the lowest form of life."
                                        n "Not concerning herself with matters of any importance, she instead sought to base her existence on superficialities."
                                        n "Not that it mattered much, as I grew to hate them both equally."
                                        n "For those who may want to critique me now for saying this:"
                                        n "I have no doubt of my father's political achievements, yet only those who had to live with him know that these successes came at the price of his very soul. An empty shell of a dragon driven by nothing but his performance as a politician, not as a father."
                                        window hide
                                        hide cover2 with fade
                                        c "(A politician, huh? I wonder what their actual government is like.)"
                                        $ bornunread = False
                                        $ persistent.bornread = True
                                        $ booksread += 1
                                        jump menubooks
                                        
                                    "Price and Prayer" if priceunread:
                                        show cover5 with fade
                                        nvl clear
                                        $ renpy.pause(1.0)
                                        play sound "fx/envelope.wav"
                                        window show
                                        n "Preface"
                                        n "In the 1422nd year since our ascent to sentience, a most extraordinary chain of events led to the most extraordinary of circumstances in our politics and society."
                                        n "These events have since been buried in history, until I stumbled upon the records of these tumultuous times."
                                        n "I have taken it upon myself to dramatize the events in a manner that is both accurate to history as well as entertaining to any reader who might have an interest in such stories."
                                        n "This is not just for my own personal gain, as I hope to make this story available to a larger audience than just a few who have permission to visit the archives."
                                        n "I believe the wisdom to be gained from the ensuing tale to be more relevant to us now than ever."
                                        window hide
                                        hide cover5 with fade
                                        $ priceunread = False
                                        $ booksread += 1
                                        jump menubooks


                                        
                                    "The Ixomen Sphere and How to Use it" if ixomenunread:
                                        show cover4 with fade
                                        nvl clear
                                        $ renpy.pause(1.0)
                                        play sound "fx/envelope.wav"
                                        window show
                                        n "As a manual meant for the general populace, this booklet intends to bring you, the valued reader, closer to the uses and joys an Ixomen Sphere might bring. I have taken utmost care to use simple language and instructions to remove the well-known barrier between individuals and knowledge of proper use of this most wondrous device. For interested parties, a chapter about the Ixomen Sphere's history and ideas for advanced applications can be found later in the book."
                                        n "Quick start guide:"
                                        n "Step 1."
                                        n "Place your Ixomen Sphere on a flat, stable surface. Make sure that the surface is, indeed, stable and flat."
                                        n "Expert tip: Use a spirit level in order to determine if a surface is absolutely horizontal in order to prevent the Ixomen Sphere from rolling off the table unintendedly."
                                        nvl clear
                                        n "Step 2."
                                        n "Plug your Ixomen Sphere into any fitting household outlet." 
                                        n "WARNING: Make sure the Ixomen Sphere's power switch is in the \"OFF\" position prior to plugging it in."
                                        n "Step 3."
                                        n "Locate the power switch of the Ixomen Sphere."
                                        n "This step may introduce some difficulties, as many different models of Ixomen Spheres exist, with varying methods of turning them on and off. When in doubt, please contact your Ixomen Sphere's manufacturer to help with this step, if necessary."
                                        window hide
                                        hide cover4 with fade
                                        c "(Now I know how to work an Ixomen Sphere. Whatever that is.)"
                                        $ ixomenunread = False
                                        $ persistent.ixomenbookread = True
                                        $ booksread += 1
                                        jump menubooks

                                    "[[Go back.]":
                                        jump menu6
                                        



                            
                        
                        "Look behind the books." if lookedbehindthebooks:
                        
                            c "(Maybe Reza left me another message here at some point. He could've known that I was going to live here, so I suppose it is possible that he helped with the preparations and hid something for me to find.)"
                            
                            play sound "fx/books.wav"
                            
                            $ renpy.pause(5.0)
                            
                            c "(No, even after removing every single book from the shelf, there is still no indicator of anything that would help me decode his secret message.)"
                            
                            c "(But even if Reza did leave a hint, this could've been anywhere in the apartment, and not just on this bookshelf.)"
                            
                            $ lookedbehindthebooks = False
                            stop sound fadeout 1.0
                            jump menu6
                        "[[Go back.]":
                            jump menu5

            "Look in the bathroom.":
                scene bath with dissolve
                jump menubath
                label menubath:
                    menu:
                        "Look inside the cabinet." if medsuntaken:
                            play sound "fx/slide.ogg"
                            $ renpy.pause(1.0)
                            c "(No razors. There are some pain meds, though.)"
                            jump medmenu
                            label medmenu:
                            
                                menu:
                            
                                    "Take some." if medsuntaken:
                                        if medstaken == 0:
                                            c "(I'm not sure if this is a good idea, but here we go.)"
                                            play sound "fx/meds.wav"
                                            $ renpy.pause(2.5)
                                            $ medstaken +=1
                                            jump medmenu
                                        
                                        if medstaken == 1:
                                            c "(Again? All right.)"
                                            play sound "fx/meds.wav"
                                            $ renpy.pause(2.5)
                                            $ medstaken +=1
                                            c "(I'm feeling... strange.)"
                                            jump medmenu
    
                                        if medstaken == 2:
                                            c "(I suppose one more can't hurt.)"
                                            c "(Can't hurt... because they're pain meds. Hehe.)"
                                            play sound "fx/meds.wav"
                                            $ renpy.pause(1.5)
                                            scene bath with fadequick
                                            $ renpy.pause(1.5)
                                            scene bath with fadequick
                                            stop music fadeout 1.0
                                            $ renpy.pause(2.5)
                                            scene black with dissolve
                                            play sound "fx/impact.wav"
                                            $ renpy.pause(4.5)
                                            play music "mx/basicguitar.ogg" fadein 3.0
                                            scene bath with dissolveslow
                                            c "(How long was I gone? And why did I think eating a whole bottle of pain medication would somehow help with my search?)"
                                            $ evilpoints += 3
                                            $ medsuntaken = False
                                            
                                            if persistent.c1meds == False:

                                                $ mp.prescription = True
                                                $ mp.save()

                                                $ persistent.c1meds = True
                                                
                                                $ achievement.grant("Prescription")
                                                
                                                $ persistent.achievements += 1
                                                
                                                call syscheck from _call_syscheck_8
                                                
                                                play sound "fx/system.wav"

                                                if system == "normal":
                                            
                                                    s "You took some pain medication. This was not a good idea."
                                                    
                                                elif system == "advanced":

                                                    s "You took some pain medication. You should probably have known that was a bad idea."
                                                    
                                                else:
                                                    
                                                    s "You took some pain medication. Possibly the stupidest thing I've seen you do... yet."
                                                
                                                    
                                            jump medmenu

                            
                                    "[[Go back.]":
                                        jump menubath
                            
                        
                        "Look inside the shower." if uncheckedshower:
                            c "(Hah, no shampoo to be found anywhere, of course. And no hint either, just some body wash.)"
                            $ uncheckedshower = False
                            jump menubath
                            
                        "[[Go back.]":
                            scene o at Pan((0, 250), (0, 250), 0.1) with dissolve
                            jump menu5
                
            "Look in the kitchen.":
                scene kitchen with dissolve
                jump menukitchen
                label menukitchen:
                    menu:
                        "Look in the fridge.":
                            c "(Plenty of stuff in here.)"
                            jump menufridge
                            label menufridge:
                                menu:
                                    "Look at the meat." if unmeat:
                                        c "(It is just a slab of meat. Nothing special about it.)"
                                        $ unmeat = False
                                        jump menufridge

                                    "Look at the milk." if unmilk:
                                        c "(Pasteurized. At least they've got that down.)"
                                        $ unmilk = False
                                        jump menufridge

                                    "Crack open an egg and look inside." if uneggsgone:
                                        if crackedeggs <= 6:
                                            play sound "fx/egg.ogg"
                                            $ renpy.pause (1.0)
                                            c "(Nope, just a regular egg.)"
                                            $ crackedeggs += 1
                                            $ persistent.c1eggnumber += 1
                                            $ mp.eggnumber += 1
                                            $ mp.save()
                                            jump menufridge
                                        else:
                                            play sound "fx/egg.ogg"
                                            $ renpy.pause (1.0)
                                            c "(Nope, just a regular egg.)"
                                            $ renpy.pause (0.5)
                                            c "(Huh, those were all of them.)"
                                            $ persistent.c1eggnumber += 1
                                            $ mp.eggnumber += 1
                                            $ mp.save()
                                            c "(Guess I just wasted a perfectly good batch of eggs.)"
                                            
                                            if persistent.c1eggs == False:

                                                $ persistent.c1eggs = True
                                                
                                                $ achievement.grant("Ovicide")
                                                
                                                $ persistent.achievements += 1
                                                
                                                call syscheck from _call_syscheck_9
                                                
                                                play sound "fx/system.wav"
                                                
                                                if system == "normal":
                                                
                                                    s "You just wasted a perfectly good batch of eggs!"
                                                    
                                                elif system == "advanced":

                                                    s "You just wasted a perfectly good batch of eggs. Poor eggs."
                                                    
                                                else:
                                                    
                                                    s "You just wasted a perfectly good batch of eggs. I hope you're happy now."


                                            $ uneggsgone = False
                                            jump menufridge

                                    "Examine an unlabeled container." if undrunk:
                                        c "(It's an unlabeled container with some sort of white liquid inside. Well, here goes nothing.)"
                                        play sound "fx/chug.wav"
                                        $ renpy.pause (1.0)
                                        c "(It's salty.)"
                                        $ undrunk = False

                                        if persistent.c1liquid == False:

                                            $ mp.liquid = True
                                            $ mp.save()

                                            $ persistent.c1liquid = True
                                            
                                            $ achievement.grant("Daredevil")
                                            
                                            $ persistent.achievements += 1
                                            
                                            call syscheck from _call_syscheck_10
                                            
                                            play sound "fx/system.wav"
                                            
                                            if system == "normal":
                                            
                                                s "You drank a mystery liquid!"
                                                
                                            elif system == "advanced":

                                                s "You drank a mystery liquid. Good for you."
                                                
                                            else:
                                                
                                                s "You drank a mystery liquid. I'm proud of you."
                                        
                                        jump menufridge


                                    "[[Go back.]":
                                        jump menukitchen
                                        
                            
                        "Look in the pantry.":
                            c "(Just some fruits and veggies here.)"

                            $ pantrynumber = 0

                            jump menupantry
                            label menupantry:


                                if pantrynumber == 4:
                                    
                                    if persistent.c1fruits == False:

                                        $ mp.fruitarian = True
                                        $ mp.save()

                                        $ persistent.c1fruits = True
                                        
                                        $ achievement.grant("Fruitarian")
                                        
                                        $ persistent.achievements += 1
                                        
                                        call syscheck from _call_syscheck_11
                                        
                                        play sound "fx/system.wav"
                                        
                                        if system == "normal":
                                        
                                            s "You learned a lot about fruits!"
                                            
                                        elif system == "advanced":

                                            s "You learned a lot about fruits. Kinda."
                                            
                                        else:
                                            
                                            s "You learned a lot about fruits. Could've added a few more puns, though."
                                    
                                    
                                else:

                                    pass
                                    
                                menu:

                                    c "(What should I look at?)"
                                
                                    "Date" if undate:
                                        c "(If I put it on the floor and then step on it, what would happen?)"
                                        c "(I'd be going on a date.)"
                                        c "(But, no, there's no hint here.)"
                                        $ undate = False
                                        $ pantrynumber += 1
                                        jump menupantry

                                    "Fig" if unfig:
                                        c "(What do I know about figs? Quite a bit, actually. Figs are ripe with history and still enjoy some cultural significance, especially in religious circles.)"
                                        c "(For example, they are the leaves with which Adam and Eve covered themselves up in the Bible's book of Genesis. It also happens to be the kind of tree Buddha achieved enlightenment under.)" 
                                        c "(Not only that, but it is also mentioned in Greek mythology. Isn't it fascinating?)"
                                        c "(But wait, there's more: The influence of figs also extends towards words, phrases and sayings we still use today.)"
                                        c "(Take the word \"sycophant\", for example, which comes from a Greek expression meaning \"someone who shows the fig\", which was a vulgar gesture at the time, or \"I don't give a fig\", which of course is a fig-ure of speech.)"
                                        c "(It might as well be said that the influence of figs is as far reaching as its fruit is succulent. Fig-uratively speaking, that is.)"
                                        c "(I'm afraid nothing of this actually helps with Reza's letter, though.)"
                                        $ unfig = False
                                        $ pantrynumber += 1
                                        jump menupantry
                                    
                                    "Pear" if unpear:
                                        c "(There are two of them. What a nice pear.)"
                                        $ unpear = False
                                        $ pantrynumber += 1
                                        jump menupantry
                                        
                                    "Grape" if ungrape:
                                        c "(So, daddy grape finds his kid crying and asks \"What's wrong, kid?\", but through all the tears, the kid couldn't get a single word out. Eventually, daddy had enough, so he said: \"Stop wi...\" No, I won't say it. It wasn't a good joke anyway.)"
                                        $ ungrape = False
                                        $ pantrynumber += 1
                                        jump menupantry

                                    "Lemon":
                                        stop music fadeout 1.0
                                        m "Lemons... lemons... LEMONS! Of course! Why didn't I realize it sooner?"
                                        play music "mx/slowpiano.ogg"
                                        m "Lemon juice is about the simplest way to write a hidden message using household items. We learned about that in chemistry. In the most boring detail, of course. A message written in lemon juice on paper becomes just about invisible to the naked eye when dried, but after heating it gently, oxidization occurs, making the message visible."
                                        m "I was sitting next to him in class when we learned that. He made a joke about using the method to cheat on the next test, and I replied by saying he'd have to bring an iron. Had he really expected me to remember a random chemistry class that happened years ago? But then, I did remember it after all."
                            
                                        if uneggsgone == True:
                                            m "\"Meet me at the portal, tonight, 10pm\" was all the message said. I wasted a good amount of time, but I still had some left before I'd have to go out to meet Reza, so I decided to make some lunch." 

                                        else:
                                            m "\"Meet me at the portal, tonight, 10pm\" was all the message said. I wasted a good amount of time, but I still had some left before I'd have to go out to meet Reza, so I decided to make some lunch. I could've made some scrambled eggs if I hadn't broken them all earlier."
                                        scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolve
                                        m "Afterwards, I resumed reading my book about the continuing adventures of Sheridan and her exploits in destroying cultural artifacts."
                                        m "Unsurprisingly, it came to a happy end, with the evil organization stopped in its tracks, at least for now. I thought the ending was deliberately left open for ambiguity, but when I turned the page and saw the advertisement for the next entry in this apparently long-running series of books, I realized all of this had just been a ploy to set up the inevitable sequel."
                                        jump continuation
    


                                    "[[Go back.]":
                                        jump menukitchen

                        "[[Go back.]":
                            scene o at Pan((0, 250), (0, 250), 0.1) with dissolve
                            jump menu5
            
            
label continuation:
    stop music fadeout 1.0
    m "Luckily, the disappointment didn't last long as I had to get going to meet Reza at the portal."
    scene np5e with dissolve
    play music "mx/amb/night.ogg" fadein 2.0
   
    m "When I got outside, it didn't seem quite as dark as it was when I arrived yesterday. I might have had difficulties finding my way, otherwise, but I could still see the portal in the distance."
   
    scene np4 with dissolve
    $ renpy.pause(1.0)
    scene np3 with dissolve
   
    m "As I was walking, I wondered if anyone was following me, but the land seemed oddly deserted. Was everyone already asleep?" 
    
    scene np2 dk with dissolve
    $ renpy.pause(1.0)
    scene np1 dk at Pan ((50,0), (400,200), 6.0) with dissolveslow
    
    $ renpy.pause (3.8)
   
    m "Eventually, I arrived at my destination. Reza was already standing idly by the portal, his fidgeting making it obvious that he had waited just for me."

    show reza normal dk with dissolve
    
    Rz "I was already wondering whether you'd get it at all."

    menu:
        "Guess I did.":
            Rz "..."
                        
        "What did you expect?":
            Rz "..."
                        
        "Well, you didn't make it easy.":
            Rz "..."
            
            
    Rz "What a wonderful night it is."
    
    scene stars dk at Pan((0, 200), (0, 0), 6.0) with dissolve

    Rz "Just look up at the stars. You can see them so clearly here, without all the pollution lingering in the air like back home. Almost as if we were looking right into the face of eternity itself."
    Rz "For so long, humanity thought we'd find aliens out there. Yet after all these years, we found we were still alone in the universe. Turns out we were just not looking in the right place."
    
    scene np1n dk at Pan ((350,200), (350,200), 0.0)
    show reza normal dk
    with dissolve
    
    c "What's going on, Reza? Why did you call me here, at this time?"
    Rz "For one, because we're sending the generator home."
    m "Right. Before I was sent here, they told me they would limit the use of the portal as they couldn't afford to keep it open all the time. In order to keep in contact with us and to enable us to send things over to them, the portal would be open for just a quarter of an hour each day."
    m "Sending something back home wasn't really problematic for us, since the high energy expenditure associated with sending bigger objects only affected the sender, not the receiver. However, this also meant that until all business was concluded in regards to our trade with the PDAs and the generators, we were basically stuck here."
    Rz "As for the other: Do you know what this place is?"
    c "You said something about trouble. How much danger are we in, really?"
    Rz "More than enough. I'm afraid this whole place will be gone soon. And we better not be here when it happens."
    #Rz "I'm afraid this whole place will be gone soon. And we better not be here when it happens."
    menu:
        "Yeah, I know.":
            Rz "You do? Well, then you know what we've got to do, right?"
            c "Yeah."
            Rz "How did you find out? It took me quite a while, but maybe we can compare notes and make sure we're right."
            $ evilpoints += 3
        
        "What are you talking about?":
            Rz "I hoped you'd see it too, but then it took me a while to understand, and I had a head start on you. In any case..."

        "Just spit it out already!":
            Rz "I hoped you'd see it too, but then it took me a while to understand, and I had a head start on you. In any case..." 
            
    m "While he was speaking, my gaze wandered and fixed on some movement nearby. It was hard to make out anything, but I imagined it might just have been wind blowing through the nearby shrubbery. Except for the fact that there was no wind."
    c "Reza."
    Rz "This might take a while to explain, but we've got the whole night."
    c "Reza, look."
    m "He turned around to face whatever I was seeing. He squinted hard before he called out."
    
    show reza angry dk with dissolve
    
    Rz "You! How dare you follow me even here?" with vpunch
    m "The disturbance came closer, until it became clear that it was Maverick, who had hidden nearby to listen in on our conversation."
    
    show reza angry dk at Position(xpos = 0.8) 
    show np1n dk at Position (xpos = 1.05, xanchor = "right")
    with ease
    show maverick normal flip dk at left with easeinleft

    #show reza angry dk at Position(xpos = 0.8) with ease
    #show maverick normal flip dk at left with easeinleft
    
    Mv "I knew you were up to no good. What were you talking about? What are you planning here, some kind of attack?"
    c "Wait a minute, there's no reason for-"
    Mv "Don't try to deny it. I heard you both talking about it in the café, and I saw the letter. You think I couldn't smell the lemon on it? Pathetic. You'll have to come with me to the police station now, both of you."

    c "Come on, I think you're overreacting, but we'll come with you if it'll help in any-{w=1.0}{nw}"
    
    #$ renpy.pause (1.3)
    
    #extend "{cps=7} \ \ \ \ {/cps}{nw}"

    play sound "fx/rev.ogg"
    
    show reza gunpoint dk with dissolve
    
    queue sound "fx/gunshot2.wav"

    $ renpy.pause (0.2)

    show maverick angry flip dk with dissolve

    play sound "fx/dragonpain.wav"

    $ renpy.pause (2.0)

    c "Reza, what are you doing?" 
    Rz angry dk "Come on, [player_name], let's get outta here!"
    
    show reza angry flip dk
    $ renpy.pause (0.3)
    hide reza normal flip dk with easeoutright

    m "In the dragon's side I could see the wound where the bullet had penetrated his hide, a trickle of blood staining his dark scales and the earth beneath. Reza used the opportunity to run off in some direction. I wasn't sure which."
    
    hide maverick with dissolve
    
    m "I frantically scanned my surroundings looking for Reza, though he had already vanished into the darkness. What was I supposed to do? Run away as well? Help Maverick? I was just a diplomat and I had no idea what was happening."

    play sound "fx/wooshimpact.wav"

    $ renpy.pause (0.7)
    
    scene np1n dk at Position (xpos = 1.05, xanchor = "right", ypos = 0.0, yanchor = 0.1) with vpunch
    
    #$ double_vision_on("np1 dk")
    
    m "Suddenly, the dragon whipped around, hitting me in the guts with his thick tail. I was lifted off the ground briefly before I felt the impact of my body hitting the ground hard enough that my vision blurred almost immediately."
    
    play sound "fx/dragonscream.wav"

    m "A deafening roar battered my ears. Was this his cry for help? I could barely move, but I found it better not to try, as to not startle the wounded dragon more than he already was. It certainly would've ended badly for me if he tried anything."
    
    play sound "fx/walklaydownpant.ogg"
    
    m "I heard him take a few unsure steps before he lay down on the ground, panting."

    show maverick angry dk with dissolve

    Mv "I'm still watching you, you know... and you better not move, for your own good. If I have to get up again and come after you in this condition, I can promise you I won't be nice."
    
    #play sound "fx/breathing.ogg"
    
    m "It took a few minutes of listening to his labored breathing before someone arrived. It was two dragons: The first I recognized as Sebastian, the other one I didn't know."
    m "I heard Sebastian and Maverick exchange a few words, when the stocky fellow approached me."
    
    stop sound fadeout 1.0
    
    scene black with dissolve
    $ renpy.pause (0.3)
    show cgcombat at Pan((0, 302), (0, 0), 7.0) with dissolvemed
    $ renpy.pause(5.0)
    scene np1n dk at Pan ((350,200), (350,200), 0.0) with fade
    
    show bryce stern b dk with dissolve

    "???" "Hey, kid. You alright?"
    
    menu:
        "Still feeling a little dizzy.":
            pass
            
        "I think I'm alright.":
            pass
    
    Br "I'm Bryce, the chief of police in this town. Can you tell me what happened?"

    $ persistent.brycemet = True

    menu:

        "I'm not sure.":
            pass

        "Reza shot Maverick and ran off.":
            pass
            
        "Maverick followed us here and tried to apprehend us.":
            $ evilpoints += 2
            
    $ renpy.pause (0.5)        
    show bryce brow b dk with dissolve
    
    Br "Is that so?"
    m "His face was stern and seemingly lost in thought as I overheard Sebastian's conversation."
    hide bryce with dissolve
    
    show sebastian normal b flip dk at left
    show maverick angry dk at right 
    with dissolve

    Sb "Yeah, but you're the flyer on duty. We probably won't find him now. Not here in the darkness, at any rate."
    
    Mv "Well, that's just brilliant."
    
    Sb "What do you think, Chief?"

    hide maverick with easeoutright
    
    show bryce stern b dk at right with easeinright
    
    Br "[player_name], can you walk?"
    c "Yeah, I think so."
    Br "Alright. Sebastian, take [player_name] to the apartment, get us some help here for Maverick, and then we'll look for Reza."
    Sb "Right on."
    Sb "Come on, [player_name]. I'll help you up."
    
    stop music fadeout 1.0
    scene black with fade
    scene o3 at Pan((0, 250), (0, 250), 0.1) with fade
    
    m "I was still shaken up by the events I just witnessed when I arrived at my apartment. Not knowing anything better to do, I soon fell into a deep slumber."
    
    scene black with dissolveslow

    $ renpy.pause(2.0)
    
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolveslow
    play music "mx/basicguitar.ogg"
    
    m "The next day, I awoke with many questions lingering in my head. I considered calling someone from the police department to ask about Reza and Maverick, but in the end I decided against doing so as I was sure they would contact me if they had anything to tell me." 
    m "I knew it was no use worrying about it for now, so I settled for starting another book."
    
    play sound "fx/door/doorbell.wav"

    $ renpy.pause(1.0)
    
    m "It didn't take very long, though, before the doorbell rang."

    play sound "fx/door/handle.wav"

    $ renpy.pause(1.0)

    show bryce normal b with dissolve

    m "Did Bryce, the chief of police, take it upon himself to escort me today?"
    c "Oh, it's you again."
    
    show bryce brow b with dissolve
    
    Br "Are you surprised?"
    c "No, but I guess it'll mean bad news."
    
    show bryce stern b with dissolve
    
    Br "'Fraid so. How are you holding up?"
    c "Better than yesterday, that's for sure."
    Br "Let's go for a walk then, shall we?"
    c "Sure." 
    
    scene black with dissolve
    $ renpy.pause (0.5)
    scene town2 at Pan ((0, 400), (0, 400), 0.0) with dissolvemed

    m "This time, I was taken along a different route than yesterday. And I was quite sure there was more to this than just taking a walk."
    c "I'll just go ahead and guess you didn't find Reza." 
    
    show bryce stern b with dissolve
    
    Br "Yeah, we hoped he would have come back on his own by now. Do you have any idea where he might be? Maybe he mentioned some sort of place in particular that holds some meaning to him?"
    c "No, not really. We didn't get a chance to talk much at all yesterday, before..."
    Br "There's that, too."
    
    c "I have no idea why Reza would have done anything like that. I had the impression that they weren't very fond of each other, but this... How is he, by the way?"

    Br "Oh, Maverick is doing fine, but there is plenty of blame to go around. You're right, they didn't particularly like each other."

    show bryce brow b with dissolve

    Br "In his statement, Maverick says he suspected Reza of planning some sort of attack. Do you know anything about that?"
    c "No, he only told me something was going to happen, not that he was planning anything. At least that was the impression I got." 
    
    show bryce stern b with dissolve
    
    Br "He's suspecting you too, by the way. That you both planned this all from the beginning."
    c "No, that wouldn't make sense."
    c "Actually, none of this is making any sense. Why would we go through all the lengths of our agreement only to jeopardize it by doing something like this?" 
    c "You even already have our PDAs and we don't have much to show for it yet. If we had any nefarious plans, this wouldn't have been a very good idea."
    Br "You have a good point. I believe you, but from our side we only have Maverick's word on the whole matter. After all, he was the one who spent the most time with Reza since he arrived here."
    Br "But even then, he didn't really have any reason to follow you yesterday and his behavior was completely out of line. I'm just glad you came out fine."
    Br "If he wasn't on mandatory sick leave, he would be suspended right now. We'll have to wait until this whole thing is over before we decide what to do with him. I can assure you this won't be taken lightly."

    menu:
        "Maybe they both acted in the heat of the moment.":
            Br "Maybe."
            c "We still got quite a lot on our hands now, though. We have a wounded dragon and a missing human. This could lead to a diplomatic crisis."
            
        "Where I come from, this kind of attack on a diplomat could be classified as an act of war, punishable by death.":
            $ renpy.pause (0.5)
            show bryce brow b with dissolve
            Br "Is that so?"
            c "We still got quite a lot on our hands now, though. We have a wounded dragon and a missing human. This could lead to a diplomatic crisis."
            $ evilpoints += 3
            show bryce stern b with dissolve
            
        "I hope so.":
            Br "I personally guarantee it."
            c "We still got quite a lot on our hands now, though. We have a wounded dragon and a missing human. This could lead to a diplomatic crisis."

    Br "Maybe Reza will still show up soon and we can get all of this behind us."
    c "I hope so too. I really wouldn't want to jeopardize everything over this unfortunate incident."
    Br "Yeah, how about we both just keep quiet about this whole thing for now? After all, I don't think any of us wants our people panicking about this already, right?"
    m "I merely nodded in agreement."
    
    stop music fadeout 1.0
    scene black with dissolve
    scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow
    
    $ renpy.pause (1.5)
    nvl clear
    window show
    
    n "Eventually, we arrived at the police station, where the chief took my formal statement in regards to yesterday's events." 
    n "He asked me about Reza and Maverick, too. Not that I knew much of anything that preceded yesterday's events, or the mysterious catastrophe Reza had mentioned."
    
    n "Afterwards, he thanked me and left to file my statement while I sat by his table, waiting and listening to the going-ons of this small, provincial town police department." 
    n "When he returned, he was approached by someone who seemed to have urgent news. A lot of talking between the two ensued that I couldn't make out from my position. This went on for a bit, until Bryce returned to me."

    window hide

    show bryce stern b with dissolve
    play music "mx/threat.ogg"
    
    Br "'Fraid I have more bad news for you. Reza has now officially become a murder suspect."
    c "M-Murder?"
    Br "We're headed to the crime scene and hoped you'd come with us."
    c "Me? A crime scene? I don't really know much about forensics."
    Br "It's just that you're the only link to Reza we have. Consider what he said would happen to us. It's in all of our interests that we find him as soon as possible, and if he has anything to do with it, you might be able to help us find him."
    Br "Your cooperation would certainly be appreciated, and it would be a nice gesture to show us that you're trustworthy in the eyes of those who might think otherwise after what happened yesterday." 
    $ declined = False
    $ declinenumber = 0
    jump imploreyou
    label imploreyou:
        
        if persistent.c1declinenumber == 99:
            
            if persistent.c1decline == False:

                $ mp.nuisance = True
                $ mp.save()

                $ persistent.c1decline = True
                
                $ achievement.grant("Nuisance")
                
                $ persistent.achievements += 1
                
                call syscheck from _call_syscheck_12
                
                play sound "fx/system.wav"
                
                if system == "normal":
                
                    s "You refused to help Bryce for the 99th time!"
                    
                elif system == "advanced":

                    s "You refused to help Bryce for the 99th time. Woohoo!"
                    
                else:
                    
                    s "You refused to help Bryce for the 99th time. You need more hobbies." 
        
        menu:
            Br "Will you help us?"
            
            "I respectfully decline.":
                if declined == False:
                    $ renpy.pause (0.5)
                    show bryce laugh b with dissolve
                    Br "I implore you to reconsider!"
                    show bryce stern b with dissolve
                    $ declined = True
                    $ persistent.c1declinenumber += 1
                    jump imploreyou
                    
                else:
                    $ renpy.pause (0.5)
                    show bryce smirk b with dissolve
                    Br "I suppose I'll just have to keep asking you until you change your mind." 
                    show bryce stern b with dissolve
                    $ persistent.c1declinenumber += 1
                    jump imploreyou

            "I will help you.":
                c "I suppose I don't really have much choice here, but you're right. We've got to find Reza, and if that's what it takes, then I'll do it."

    Br "Very well. Let us go, then."

    play sound "fx/steps/clean2.wav"
    
    label investigation:
    
    scene black with dissolve
    $ renpy.pause (1.0)
    scene town7 with fade

    m "On our way to the crime scene, he tried to prepare me for what would come. I had studied biology, so I was familiar with the sight of dead animals. Asking myself how similar this would be, I wondered if my reaction would be any different if it wasn't a dragon, but a human corpse I would be seeing."

    scene town6 with dissolve
    
    m "When we arrived, we were met by Sebastian, who gave us an overview of the whole situation."
    show bryce stern b at right with dissolve
    
    show sebastian normal b flip at left with dissolve

    Sb "This morning, the victim was found by a delivery flyer for a restaurant. Blood loss from multiple wounds are the likely cause of death. Forensics was already here, so feel free to poke around."
    show sebastian normal b
    $ renpy.pause (0.3)
    hide sebastian with easeoutleft
    m "A few paces in front of us, the unfortunate victim lay on the ground, covered by a sheet that concealed the body, but not the large red stain beneath. We approached, while Sebastian went off to deter any curious onlookers."
    
    Br "I know it won't be pretty, and I'm sorry for putting you through this, but you know what's at stake here. Just remember what I told you and you should be fine." 
    c "Alright."
    Br "Are you ready?"
    
    menu:
        "I guess so.":
            $ renpy.pause (0.0)

        "Just do it.":
            $ renpy.pause (0.0)
    
    stop music fadeout 1.0
    Br "..."
    
    play sound "fx/sheet.wav"
    
    scene black with dissolve
    $ renpy.pause (0.5)
    scene deadbody at Pan ((0, 1080), (0, 350), 10) with dissolveslow
    $ renpy.pause (10.0)
    
    Br "What do you think?"
    c "Well, he's definitely dead."
    Br "Yeah, RIP."
    Br "Let's just say this will be your test, and tell me what you can deduce from what you see. Give it your best shot."
    
    play sound "fx/unroll.ogg"
    show invest with wiperightquick
    
    play sound "fx/unroll.ogg"
    show start with wipeleftquick

    $ renpy.pause (0.5)
    play music "mx/investigation.ogg"
    $ renpy.pause (0.5)

    hide invest
    hide start
    with dissolvemed
    
    $ renpy.pause (0.5)
    
    m "Two wings, two legs, just like the waitress in the café. About as big as a human, length-wise, if not slightly taller. The wingspan would certainly look impressive at that size."
    
    show deadbody at Position(xpos = 0, xanchor=0, ypos=-1000, yanchor=0) with ease

    show deadbodywounds at Pan ((0, 1000), (0, 1000), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodywounds with dissolvequick
    show deadbodywounds at Pan ((0, 1000), (0, 1000), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodywounds with dissolvequick

    show deadbody at Position(xpos = 0, xanchor=0, ypos=-350, yanchor=0) with ease

    $ renpy.pause (1.0)

    show deadbodywounds at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodywounds with dissolvequick
    show deadbodywounds at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodywounds with dissolvequick
    c "The wounds are kinda hard to miss."
    $ answers = 0
    Br "True, but what are they telling you?"
    $ wrong1 = True
    $ wrong2 = True
    $ wrong3 = True
    $ wrong4 = True
    $ wrong5 = True
    $ wrong6 = True
    $ wrong7 = True
    $ wrong8 = True
    $ wrong9 = True
    $ wrong10 = True
    $ wrong11 = True
    $ wrong12 = True
    $ wrong13 = True
    $ wrong14 = True
    $ wrong15 = True
    $ wrong16 = True
    $ wrong17 = True
    $ wrong18 = True
    $ wrong19 = True
    $ wrong20 = True
    $ wrong21 = True
    $ wrong22 = True
    $ suicide = 0
    
    jump quest1
    label quest1:
        
        menu:
            "They were inflicted with a sharp implement.":
                $ answers += 1
            
            "The perpetrator was an unusually large or small person." if wrong1:
                c "The angles look a bit strange, like they were done from an unusual position. Is it possible that they were inflicted by a person who was much larger or smaller than him?"
                Br "No, I don't think that's it."
                $ answers -= 1
                $ wrong1 = False
                jump quest1

            "He was already dead when he got these wounds." if wrong2:
                Br "How so? That seems pretty unlikely."
                $ answers -= 1
                $ wrong2 = False
                jump quest1

            "It was suicide." if wrong3:
                c "Based on the number and shape of the wounds, I'd say it was a suicide."
                Br "No way."
                $ answers -= 2
                $ suicide += 1
                $ wrong3 = False
                jump quest1


        c "They are clean cuts, like from a knife or another sharp instrument."
        Br "That is true, but why does this matter?"

    jump quest2
    label quest2:
        menu:
            "It actually doesn't." if wrong4:
                Br "You don't think the murder weapon matters?"
                $ answers -= 2
                $ wrong4 = False
                jump quest2

            "Dragons don't use knives." if wrong5:
                Br "Actually, we do. Mostly by those who have the proper hands to use them, but still..." 
                $ wrong5 = False
                jump quest2

            "It couldn't have been Reza.":
                c "Reza had a gun yesterday. Why would he use a knife now?"
                Br "Right, that weapon he was using on Maverick is called a \"gun\", right?"
                c "Yeah."
                Br "What strange contraptions."
                Br "Well, he could have had a reason to use a knife over his \"gun\" if it was him. Can you think of any?"

            "It could have only been someone with hands.":
                Br "That's right. Only those of us who walk on two legs have the proper dexterity to wield a knife effectively. Most other dragons would probably just bite instead."
                $ answers +=1
                Br "Of course, this rules out most of the bigger dragons, and flyers."
                Br "But then, Reza still has his... what was it called again?"
                c "You mean his gun?"
                Br "Yeah. If it was him, why would he kill someone with a knife rather than just use this \"gun\" on him?"

            "It tells us that it was suicide." if wrong6:
                if suicide == 0:   
                    Br "Unlikely. Someone who commits suicide doesn't slash themselves multiple times. Also, some of the cuts are only superficial. No, this must have been a fight."
                if suicide == 1:
                    Br "I thought we ruled that one out already."
                $ suicide +=1
                $ answers -=2
                $ wrong6 = False
                jump quest2


    jump quest3
    label quest3:
        menu:
            "It makes him look cooler." if wrong7:
                Br "No, just no."
                $ answers -=2
                $ wrong7 = False
                jump quest3
                
            "He lost his gun." if wrong8:
                Br "That is possible, but we have already searched the perimeter and didn't find anything."
                $ wrong8 = False
                jump quest3
                
            "He did not want to make any noise.":
                c "He did not want to make any noise. After all, he ran away from Maverick, trying to hide from the police. Something as loud as a gunshot would have easily given away his position and alerted others in the area."
                $ answers += 1
                Br "Right, that could be a good reason."

            "He wouldn't, because it wasn't him." if wrong9:
                c "There clearly is no reason why he would, so it couldn't have been him at all."
                $ answers -= 1
                Br "I'll have to disagree with you on that." 
                $ wrong9 = False
                jump quest3

            "He wouldn't, because this was clearly a suicide." if wrong10:
                if suicide == 0:
                    Br "Clearly? You mean a flyer with barely usable hands stabbed himself with a knife multiple times until he died from blood loss? That just doesn't seem plausible."
                    Br "Actually, the only reason I can think of why someone would do that is if he deliberately wanted to make it look as if it wasn't a suicide."
                    Br "Even then, Haziq's procedure of logic tells us that until further evidence surfaces, the theory with the least amount of assumptions is the most likely. This one isn't it."
                if suicide == 1:
                    Br "I thought we ruled that one out already."

                if suicide == 2:
                    Br "Alright, I get it. You think it was a suicide, but I think we should explore other options." 
                    
                $ suicide += 1
                $ answers -= 2
                $ wrong10 = False
                jump quest3
    
    Br "By the way, which wound do you think was the lethal one?"
    jump quest4
    label quest4:
        
        menu:
            
            "The one on his chest." if wrong11:
                c "The gashes on his chest look rather large. I think it was them."
                Br "Actually, no. These kinds of wounds come from a slashing motion, meaning the wound may end up looking big, but the damage is comparatively superficial." 
                Br "Of course they may contribute to blood loss, but they aren't lethal so quickly."
                $ answers -= 1
                $ wrong11= False
                jump quest4

            "The ones on his wings." if wrong12:
                c "He's got quite a few there, so I think it must be them."
                Br "No, there's not really much blood loss from those. These are actually defensive wounds, usually inflicted when someone tries to defend themselves from these kinds of attacks."
                $ answers -= 1
                $ wrong12 = False
                jump quest4
                
            "The one on his neck.":
                c "I think it was the one on his neck."
                Br "That's right. If all the blood from it wasn't a giveaway, this is a stab wound. Characterized by a rather small footprint, you can tell it's also the deepest one." 
                Br "And from the location, it's pretty obvious this must have done tremendous damage."
                $ answers += 1
      
      
    Br "What else do you see?"
    show deadbodyblood at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodyblood with dissolvequick
    show deadbodyblood at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodyblood with dissolvequick
    
    c "Well, there's a lot of blood."   
    
    jump quest5
    label quest5:
                
        menu:
            "The blood splatters suggest that:"

            "He was hemophiliac." if wrong13:
                c "There's so much blood. Could he have been hemophiliac?"
                Br "It is a lot of blood, I'll give you that, but I don't think this has anything to do with hemophilia."
                $ answers -= 1
                $ wrong13 = False
                jump quest5

            "He had aids." if wrong14:
                Br "Had what?"
                c "..."
                $ wrong14 = False
                jump quest5
            
            "He died here.":    
                c "He died here, else there would have been a trail we could follow. The splatters also suggest this is where they fought."
                $ answers += 1
                
            "This isn't blood." if wrong15:
                Br "You sure?"
                play sound "fx/sniff.ogg"
                $ renpy.pause (2.5)
                Br "No, it's blood alright."
                $ answers -=1
                $ wrong15 = False
                jump quest5
                
            "He was dragged here after he died." if wrong17:
                Br "Well, there is no blood anywhere else in the vicinity that would suggest that. Unless the perpetrator had the time to clean up some of it."
                $ answers -= 1
                $ wrong17 = False
                jump quest5

            "He committed suicide." if wrong18:
                
                if suicide == 0:
                    Br "Really? You mean a flyer with barely usable hands stabbed himself with a knife multiple times until he died from blood loss? That just doesn't seem plausible."
                    Br "Actually, the only reason I can think of why someone would do that is if he deliberately wanted to make it look as if it wasn't a suicide."
                    Br "Even then, Haziq's procedure of logic tells us that, until further evidence surfaces, the theory with the least amount of assumptions is the most likely. This one isn't it."

                if suicide == 1:
                    Br "I thought we ruled that one out already."

                if suicide == 2:
                    Br "Alright, I get it. You think it was a suicide, but I think we should explore other options." 
                
                if suicide == 3:  
                    Br "Just stop it already."

                $ suicide += 1
                $ answers -= 2
                $ wrong18 = False
                jump quest5

    Br "That's true." 
    Br "Unfortunately, it doesn't help with determining who the perpetrator is."
    c "Objection!" with hpunch
    #c "Objection!" with Shake((0, 0, 0, 0), 2, dist=10)
    Br "Excuse me?"
    c "Sorry, I just always wanted to say that."
    Br "Go on, please."
    show deadbodyteeth at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodyteeth with dissolvequick
    show deadbodyteeth at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodyteeth with dissolvequick
    
    c "What about the blood on his muzzle?"
    Br "You tell me."

    jump quest6
    label quest6:

        menu:
            
            "The blood on his muzzle suggests that:"
            
            "He is a vampire." if wrong19:
                
                Br "Don't be silly."
                $ answers -= 2
                $ wrong19 = False
                jump quest6

            "He fought back.":
                c "It might be the perpetrator's blood."
                $ answers += 1

            "He had a bloody steak earlier." if wrong20:
                Br "And have the blood from it still stuck to his teeth who knows how long after? I don't think so."
                $ answers -= 1
                $ wrong20 = False
                jump quest6

            "He has gum disease." if wrong21:
                Br "Possible, but unlikely."
                $ answers -= 1
                $ wrong21 = False
                jump quest6

            "He bit his tongue during the fight." if wrong22:
                Br "That is actually a very real possibility. We probably would be seeing more blood if that were the case, though."
                $ wrong22 = False
                jump quest6
            

    Br "Yes, that is true. I expect forensics already took a sample of it, so it might actually help us determine who the perpetrator is."
    Br "Hm. I think that's about everything."

    play sound "fx/unroll.ogg"
    show invest with wiperightquick
    
    play sound "fx/unroll.ogg"
    show over with wipeleftquick

    $ renpy.pause (0.5)
    stop music fadeout 1.0
    $ renpy.pause (0.5)

    hide invest
    hide over
    with dissolvemed
    
    scene town6 with fade
    show bryce normal b with dissolve
    play music "mx/basicguitar.ogg"
    
    if answers >= 5:
        show bryce laugh b with dissolve
        Br "You know what, kid? I'm impressed. Maybe we should have you around more often."
        show bryce normal b with dissolve
        $ inv = "high"
        
        if persistent.c1invhigh == False:

            $ mp.investigator1 = True
            $ mp.save()

            $ persistent.c1invhigh = True
            
            $ achievement.grant("Investigator 1")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_13
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You did well on the first investigation!"
                
            elif system == "advanced":

                s "You did well on the first investigation. Well done."
                
            else:
                
                s "You did well on the first investigation. Achoo- I mean, achievement unlocked."


    elif answers >= 2:
        Br "For someone who says they haven't done this kind of thing before, that wasn't actually too bad. I know some recruits who did a lot worse during their first time, for sure."
        $ inv = "normal"
        
    else:
        show bryce brow b with dissolve
        Br "Maybe this isn't your strong suit."
        c "Told you so."
        show bryce stern b with dissolve
        Br "Don't worry about it. We still need your help with other things."
        show bryce normal b with dissolve
        $ inv = "low"
    
    show bryce at right with ease
    show sebastian normal b flip at left with easeinleft
    
    Sb "Hey Chief, do you still need the witness here for anything?"
    m "Sebastian approached with the dragon who had discovered the body earlier. I recognized her as Adine, the waitress from the café. She seemed distraught, which given the situation, wasn't very surprising."
    Br "I don't think so. Take her to the department, get her statement written up and that should be it."
    Sb "Sure thing."
    
    hide bryce stern b with easeoutright
    show adine disappoint b at right with easeinright
    
    Sb "Alright, Miss, we're going to have to take you to the department."
    Ad "Of course."
    m "When she spotted me, however, her composure brightened visibly."
    
    show adine normal b with dissolve

    Ad "Oh, it's the human!"

    menu:
        "Well, I'm {i}a{/i} human.":
            $ renpy.pause (0.5)
            show adine b giggle with dissolve
            Ad "Well, I'd call you by your name, but you never actually told me it."
            
        "I have a name, you know.":
            
            Ad "Actually, I don't. You never told me it."
            
        "Go away.":
            $ renpy.pause (0.5)
            show adine disappoint b with dissolve
            Ad "Sorry, I'd call you by your name, but you never actually told me it."
            $ evilpoints += 1

    c "It's [player_name]."
    
    show adine think b with dissolve

    Ad "What're you even doing here? Do you work for our police now?"
    
    menu:
        "Guess so.":
            $ renpy.pause (0.5)
            show adine normal b with dissolve
            Ad "That doesn't sound very convincing."
            c "I'm not quite convinced, either."
            
        "Looks like it.":
            $ renpy.pause (0.5)
            show adine normal b with dissolve
            Ad "Maybe I should be calling you officer, then."
            c "I don't think I'm quite there yet."

        "No, it's just a hobby.":
            $ renpy.pause (0.5)
            show adine giggle b with dissolve
            Ad "Oh, you."

    c "By the way, I didn't know you also did deliveries."
    show adine normal b with dissolve
    Ad "I do a little bit of everything, really."

    if food == "fish":
        c "That's nice. I liked my uh... fish yesterday."
        show adine giggle b with dissolve
        Ad "You don't have to hide it. I know it's quite an acquired taste." 
        show adine think b with dissolve
        Ad "To be fair, I wouldn't have recommended it to someone new like you, but you could always try something different." 
        show adine normal b with dissolve
        Ad "Here's our number if you don't want to come in and we'll deliver anything we have to you." 
        
    if food == "coffee":
        c "That's nice. I liked my coffee yesterday."
        Ad "If you like it, why don't you take our number? We could deliver something to you next time if you don't want to come in." 

    if food == "eggs":
        c "That's nice. I loved my scrambled eggs yesterday."
        Ad "If you like it so much, why don't you take our number? We could deliver something to you next time if you don't want to come in." 
        
    c "Thanks."

    show sebastian disapproval b flip with dissolve

    play sound "fx/throat_clear.ogg"
        
    Sb "..."
    Ad "Sorry, I guess we should get going. Bye!"

    show adine normal b flip
    $ renpy.pause (0.3)
    hide adine normal b flip with easeoutright
    hide sebastian disapproval b flip with easeoutright
    $ renpy.pause (0.5)
    show bryce stern b with dissolve
    
    c "What do we do now?"
    stop music fadeout 1.0
    
    
    Br "I suppose we'll head off too, unless- oh no."
    c "What is it?"

    show bryce stern b at right with ease
    show maverick normal flip at Position(xpos = 0.13) with easeinleft
    play music "mx/detective.ogg"
    
    Mv "We've got a violent homicide and of course nobody from the department tells me. I have to find out from a neighbor who wanted to ask me about it. Good thing rumors travel fast, eh?"
    
    show bryce brow b with dissolve
    
    Br "Of course nobody told you. You're on sick leave. Mandatory sick leave, I might add." 
    Mv "I'm not here in any official capacity, you see. I am merely enjoying a curative walk in the fresh air and happened to come across you by accident."
    Br "What do you want?"
    Mv "I don't want anything. I just find it interesting that no one tells me about this, but the prime suspect's buddy can mess with the investigation. I see how it is."
    Br "I know what you are thinking, but don't jump to conclusions here."
    Mv "I don't need to jump to conclusions, I think the dead body we found says it all."
    Br "You really have an attitude problem. You know, if you weren't on sick leave you'd be suspended right now for attacking [player_name] yesterday. Do you even have any idea what kind of repercussions this could have on us all?"
    Mv "Me attack [player_name]? As far as I can see, I'm the only one who's injured here. Besides, I'm so sorry for apparently being the only one who's doing his damn job." 
    Mv "Right, let's just all sit idly by while the suspect's on the loose and planning his next move."
    c "You know, whatever it was Reza was talking about, he was going to tell me just before you showed up yesterday."
    show maverick angry flip with dissolve
    Mv "I don't need to hear you, of all people, belittling me about this."
    c "What's your problem? If anything, I want to find him just as much as you do."
    Mv "Don't compare yourself to me. Your words mean nothing."
    
    show bryce stern b with dissolve
    
    Br "Enough. You shouldn't even be here, so you better go now and get some rest before I have to take disciplinary action."
    Mv "Fine, but when we find him, you'll see I was right. If I have to prove it myself, so be it."
    stop music fadeout 1.0
    
    show maverick normal at Position(xpos = 0.29)
    $ renpy.pause (0.3)
    hide maverick normal with easeoutleft
    $ renpy.pause (0.5)
    play music "mx/basicguitar.ogg" fadein 1.0
    
    c "Can he even just do his own investigation like that?"
    Br "Well, as long as he doesn't interfere with us, we can't really stop him from doing things in his own free time."
    c "I see. I suspect he won't adhere to the standards of performing an unbiased investigation, though."
    Br "He has already made up his mind. It's clear to me he won't be looking for facts, just for evidence to support his own view in order to prove it to us or himself, who knows." 
    Br "He's always been like that, always something to prove. We'll have to be careful. He'll be looking for Reza soon enough."
    menu:
        "To be fair, I might be too if I was shot.":
            Br "Yeah, and that's exactly why he wouldn't be on the case even if he wasn't on sick leave."

        "Let's hope we find Reza before he does.":
            Br "Yeah."

        "At least that means someone will find him, right?":
            $ renpy.pause (0.0)
            
    Br "Don't worry, Reza will turn up eventually."
    c "I surely hope so."
    m "All things considered, I had to admit that it remained a possibility that Maverick was right, but could the Reza I knew really be a murderer?"
    Br "You know what, if you think of something that might help with the investigation, or if you need anything else, just call me."
    c "I will."
    Br "Well, I think we're done here. Let's go."

    label sceneselect:
        pass
    
    scene black with dissolve
    $ renpy.pause (1.0)
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

    m "Bryce led me back to the apartment. I guess there wasn't really much for me to do in the meantime, as I was spared the more arduous parts of the investigation. Maybe I should have been glad about this, though now I had an afternoon to fill."

$ evilending = False

$ remy3choiceyes = False

$ adinesendawayseen = False
$ adinerequestmade = False
$ c4witnessavailable = True

$ remydead = False
$ annadead = False
$ loremdead = False
$ brycedead = False
$ adinedead = False

$ loremhavesphere = False

$ persistent.c1skip = True

$ attempts = 3
$ toolsactivated = False
$ toolsfirst = False
$ tools = False
$ buggymenu = False
$ tennisplayed = False

$ pw = "0"
$ permission = False
$ term = "0"
$ cipher = 16

$ boredom = 0

$ system = "normal"

$ gotresultsviapost = False
$ gaveadinemap = False

$ c4clues = 0

$ kevinavailable = False
$ kevinunplayed = True

$ katsuavailable = False
$ seenkatsu = False
$ katsuunplayed = True

$ chopedisplayed = False

$ c4intuition = False

$ c4displaycharacters = 0
$ c4displayloss = False
$ c4displayremy = False
$ c4displayanna = False
$ c4displaylorem = False
$ c4displaybryce = False
$ c4displayadine = False

$ carddisplayed = False
$ lastcard = "none"

$ chap3picksremy = 0
$ chap3picksanna = 0
$ chap3picksbryce = 0
$ chap3picksadine = 0
$ chap3pickslorem = 0

$ readingavailable = True
$ chapter2count = 0
$ chapter3count = 0
$ chapter4count = 0

$ emeraavailable = False
$ emeraunplayed = True
$ emeramet = False

$ zhongavailable = False
$ zhongnameavailable = False
$ zhongunplayed = True

$ nodrinks = False
$ nofood = False
$ remyapologized = False
$ nomeat = False

$ sebastianavailable = False
$ sebastianfail = True
$ sebastiansaved = False

$ metclerk = False
#$ heardaboutcancer = False
$ sebastianunplayed = True

$ mcfirst = False
$ brycefirst = False
$ c4hatcheryavailable = False

$ brycegoodending = False
$ remygoodending = False
$ annagoodending = False
$ adinegoodending = False
$ loremgoodending = False

$ anna3stopped = False
$ bryce3do = "none"
$ playmessage = False

$ remygoodending = False
$ brycegoodending = False
$ annagoodending = False
$ adinegoodending = False
$ loremgoodending = False

$ chap3inv = 0

$ c3facques1 = True
$ c3facques2 = True
$ c3facques3 = True
$ c3facques4 = True
$ c3facquesx = 0

$ c3arcquesx = 0
$ c3arcques1 = True
$ c3arcques2 = True
$ c3arcques3 = True
$ c3arcques4 = True

$ c3facd = False
$ c3arcd = False
$ c3arcprank = False
$ c3stod = False

$ varasaved = False
$ c3stay = False

$ c3clues = 0

$ metdamion2 = False
$ annasurvives = False
$ damionsurvives = False

$ chap1picka = "none"
$ chap1pickb = "none"

$ chap2picka = "none"
$ chap2pickb = "none"

$ chap3picka = "none"
$ chap3pickb = "none"

$ chap4picka = "none"
$ chap4pickb = "none"

$ bryce2legs = False
$ bryce2magazine = False

$ chap2facres2 = True

$ chapter2unplayed = True
$ chapter3unplayed = True
$ chapter4unplayed = True

$ remy1unheard = True
$ bryce1unheard = True
$ anna1unheard = True
$ adine1unheard = True
$ lorem1unheard = True

$ remy2unheard = True
$ bryce2unheard = True
$ anna2unheard = True
$ adine2unheard = True
$ lorem2unheard = True

$ remy3unheard = True
$ bryce3unheard = True
$ anna3unheard = True
$ adine3unheard = True
$ lorem3unheard = True

$ remy4unheard = True
$ bryce4unheard = True
$ anna4unheard = True
$ adine4unheard = True
$ lorem4unheard = True

$ remyavailable = True
$ bryceavailable = True
$ adineavailable = True
$ annaavailable = True
$ loremavailable = True

$ chap2clues = 0

$ chap2storewho = True
$ chap2receiptsuntaken = True
$ chap2storebrowse = True

$ chap2storebread = True
$ chap2storeproduce = True
$ chap2storemeat = True
$ chap2storehealth = True

$ chap2facreza = True
$ chap2facanna = True
$ chap2facres = True
$ chap2asked = False

$ chap2libreza = True
$ chap2libadine = True
$ chap2libmood = True
$ chap2libapologize = False
$ chap2libasked = False

$ chap2emmeet = True
$ chap2emmeet2 = False
$ chap2emvisit = True
$ chap2emjob = True
$ chap2empark = True
$ chap2park3unvisited = True
$ leftbryce = False
$ chap2bandageuntaken = True

$ emeramood = 0

$ remy1unplayed = True
$ anna1unplayed = True
$ bryce1unplayed = True
$ adine1unplayed = True
$ lorem1unplayed = True

$ remy2unplayed = True
$ anna2unplayed = True
$ bryce2unplayed = True
$ adine2unplayed = True
$ lorem2unplayed = True

$ remy3unplayed = True
$ anna3unplayed = True
$ bryce3unplayed = True
$ adine3unplayed = True
$ lorem3unplayed = True

$ remy4unplayed = True
$ anna4unplayed = True
$ bryce4unplayed = True
$ adine4unplayed = True
$ lorem4unplayed = True

$ chapter1csplayed = 0
$ chapter2csplayed = 0
$ chapter3csplayed = 0
$ chapter4csplayed = 0

$ remy1played = False
$ remy2played = False
$ remy3played = False
$ remy4played = False
$ remy5played = False
$ anna1played = False
$ anna2played = False
$ anna3played = False
$ anna4played = False
$ anna5played = False
$ bryce1played = False
$ bryce2played = False
$ bryce3played = False
$ bryce4played = False
$ bryce5played = False
$ lorem1played = False
$ lorem2played = False
$ lorem3played = False
$ lorem4played = False
$ lorem5played = False

$ remystatus = "none"
$ annastatus = "none"
$ adinestatus = "none"
$ brycestatus = "none"
$ loremstatus = "none"

$ brycebar = False


label chapter1chars:
    
    $ save_name = "Chapter 1"

    if persistent.endingsseen > 0:
    
        $ sebastianavailable = True
        
    if sebastianunplayed == False:
    
        $ sebastianavailable = False

    if chapter1csplayed == 0:


        menu:
            c "(What should I do?)"
            "Meet with Remy." if remy1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "remy"
                $ chap3picksremy += 3
                jump remy1
                
            "Meet with Anna." if anna1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "anna"
                $ chap3picksanna += 3
                jump anna1
                
            "Meet with Lorem." if lorem1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "lorem"
                $ chap3pickslorem += 3
                jump lorem1
                
            "Meet with Bryce." if bryce1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1picka = "bryce"
                $ chap3picksbryce += 3
                jump bryce1
                
            "Order some lunch." if adine1unplayed:
                stop music fadeout 1.0
                $ chap1picka = "adine"
                $ chap3picksadine += 3
                jump adine1


            "Meet with Sebastian." if sebastianavailable:
                stop music fadeout 1.0
                $ chap1picka = "sebastian"
                jump sebastian
    
    elif chapter1csplayed == 1:
        
        scene black with dissolveslow
        $ renpy.pause (1.0)
        scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

        menu:
            c "(More free time. What should I do?)"
            "Meet with Remy." if remy1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "remy"
                $ chap3picksremy += 2
                jump remy1
                
            "Meet with Anna." if anna1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "anna"
                $ chap3picksanna += 2
                jump anna1

            "Meet with Lorem." if lorem1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "lorem"
                $ chap3pickslorem += 2
                jump lorem1
                
            "Meet with Bryce." if bryce1unplayed:
                play sound "fx/steps/clean2.wav"
                stop music fadeout 1.0
                $ chap1pickb = "bryce"
                $ chap3picksbryce += 2
                jump bryce1
                
            "Order some lunch." if adine1unplayed:
                stop music fadeout 1.0
                $ chap1pickb = "adine"
                $ chap3picksadine += 2
                jump adine1

            "Meet with Sebastian." if sebastianavailable:
                stop music fadeout 1.0
                $ chap1pickb = "sebastian"
                jump sebastian

            "Get some well deserved rest.":
                
                $ chap1pickb = "none"
                m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
                $ persistent.lazynumber += 1
                call lazycheck from _call_lazycheck
                
                jump chapter2
                
    else:
        jump chapter2

return

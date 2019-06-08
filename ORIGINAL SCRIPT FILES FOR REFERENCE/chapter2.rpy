label chapter2:

#calculations here

$ evil2points = evilpoints

if remystatus == "bad":
    
    $ evil2points += 2

if annastatus == "bad":
    
    $ evil2points += 2

if brycestatus == "bad":
    
    $ evil2points += 2

if adinestatus == "bad":
    
    $ evil2points += 2

if loremstatus == "bad":
    
    $ evil2points += 2


$ chap2points = 0
$ chap2points += answers

if remystatus == "neutral":
    
    $ chap2points += 1

if annastatus == "neutral":
    
    $ chap2points += 1

if brycestatus == "neutral":
    
    $ chap2points += 1

if adinestatus == "neutral":
    
    $ chap2points += 1

if loremstatus == "neutral":
    
    $ chap2points += 1

if remystatus == "good":
    
    $ chap2points += 2

if annastatus == "good":
    
    $ chap2points += 2

if brycestatus == "good":
    
    $ chap2points += 2

if adinestatus == "good":
    
    $ chap2points += 2

if loremstatus == "good":
    
    $ chap2points += 2

scene black with dissolveslow   

$_dismiss_pause = False

$ _game_menu_screen = None

$ renpy.pause (1.3)

play sound "fx/chapter2.ogg"

$ save_name = "Chapter 2"

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

scene chap2 at Pan((0, 0), (0, 0), 6.0) with dissolveslow

#show card1 at Pan((100, 0), (0, 0), 2.0) with dissolveslow

if persistent.trueending == True:
 
    show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardenlightenment = True
    
elif trueselectable == True:
    
    show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardenlightenment = True

elif evil2points >= 12:
    
    show cpride at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardpride = True

elif chap2points >= 8:
    
    show cduty at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardduty = True

elif chap2points >= 5:
    
    show chope at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardhope = True
    
else:
    
    show ctrauma at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardtrauma = True



show text2 with dissolveslow

play soundloop "fx/fire3.ogg" fadein 1.0


if persistent.trueending == True:
 
    scene chap2 at Pan((0, 120), (0, 360), 7.0)
    show cenlightenment at Pan((00, 0), (0, 0), 2.0)
    show text2
    with dissolveslow

elif trueselectable == True:
    
    scene chap2 at Pan((0, 120), (0, 360), 7.0)
    show cenlightenment at Pan((00, 0), (0, 0), 2.0)
    show text2
    with dissolveslow

elif evil2points >= 12:
    
    scene chap2 at Pan((0, 120), (0, 360), 7.0)
    show cpride at Pan((00, 0), (0, 0), 2.0)
    show text2
    with dissolveslow

elif chap2points >= 8:
    
    scene chap2 at Pan((0, 120), (0, 360), 7.0)
    show cduty at Pan((00, 0), (0, 0), 2.0)
    show text2
    with dissolveslow

elif chap2points >= 5:
    
    scene chap2 at Pan((0, 120), (0, 360), 7.0)
    show chope at Pan((00, 0), (0, 0), 2.0)
    show text2
    with dissolveslow
    
else:
    
    scene chap2 at Pan((0, 120), (0, 360), 7.0)
    show ctrauma at Pan((00, 0), (0, 0), 2.0)
    show text2
    with dissolveslow



$ renpy.pause(2.0)

$ renpy.pause (2.0)

stop sound fadeout 2.0

stop soundloop fadeout 2.0

scene black with dissolveslow

#$_dismiss_pause = True

$ renpy.pause(2.0)

$ _game_menu_screen = "navigation"

nvl clear

scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause(3.0)

if persistent.brycedies == True:
    $ persistent.brycekey2 = True
    
if persistent.c2skip == True:

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_49

    call skiptut from _call_skiptut_11
        
    if skipbeginning == False:

        if system == "normal":
        
            s "My records indicate you have already experienced this section in a satisfactory manner. Would you like to skip to the scene selection?"
        
            #play sound "fx/system3.wav"
        
            #s "Warning: In this scene, skipping ahead this way instead of using the skip buttons (CTRL and TAB) may prevent you from experiencing alternative choices and outcomes that you haven't seen before. These may only be minor, though."
        
        elif system == "advanced":

            s "It looks like you've seen this before. Skip to the scene selection?"
        
            #play sound "fx/system3.wav"
        
            #s "I have to warn you, though. If you do this here instead of just using CTRL and TAB, you may end up missing some minor changes you haven't seen before."
            
        else:
            
            s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the scene selection."
            
            #play sound "fx/system3.wav"
            
            #s "If you want to do things this way instead of just using the skip buttons like a civilized person, you could end up missing some choices you haven't made before. But considering how far you've come, you probably won't miss much."
        
    $ skipbeginning = False
    
    menu:
        
        "Yes. I want to skip ahead.":
            
            play sound "fx/system3.wav"
            
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            
            $ chap2inv = 7
            $ chap2invt = 0
            
            $ chapter2sectionsplayed = 0
            $ chapter2libraryunplayed = True
            $ chapter2storeunplayed = True
            $ chapter2facilityunplayed = True
            $ chapter2parkunplayed = True
            $ chap2shrubberysearched = 0
            $ chap2pavsearched = 0
            $ chap2rested = 0
            
            show black with dissolvemed

            $ renpy.pause (0.5)
            
            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_11

            show town1 with dissolvemed

            play music "mx/elegant.ogg" fadein 1.0
            
            window show
            
            jump chapter2sections2
            
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

play music "mx/basicguitar2.ogg"
window show

n "Another day, another morning."
n "I awoke from dreams filled with fire and smoke. The sun shining through the window gave me a comforting feeling of familiarity, despite the portal in the distance reminding me of my purpose here."
n "I looked towards the horizon, my view undisturbed by dividing walls. The light of the morning sun was painting the sky with golden hues, a view that had become a rarity back home. It evoked a feeling of freedom and openness that was almost scary to me."
n "While I got ready for the day, my thoughts strayed to the people I knew back home. I couldn't help but wonder how they were doing."
n "But I had greater things to worry about at the moment, like Reza, murders and generators. How much danger was I in, really?"

play sound "fx/door/doorbell.wav"

$ renpy.pause (1.5)

stop sound fadeout 0.5

window hide

play sound "fx/door/handle.wav"

$ renpy.pause (1.5)

nvl clear

if brycebar == True:
    
    show bryce stern b with dissolve
    
    Br "Hey, [player_name]."
    
    c "Bryce."

    Br "We've got some work ahead of us, but before we get to that, I've got to ask you a question."

    c "Okay, go ahead."

    Br "Why'd you just leave when we were in the bar?"

    c "Getting drunk isn't really my idea of fun and you were kinda pushy about the whole thing."

    show bryce laugh b with dissolve

    Br "Is that so? That's my bad, sorry. I just wanted to have a nice evening and relax with a few beers. You know, that's kinda what bars are all about."

    show bryce normal b with dissolve
    
    Br "Anyway, how about I invite you to make up for the whole thing?"
    
    c "I'll think about it."

    Br "Sounds good."

    c "So, what else is on today's agenda?"

    Br "Just some good, old-fashioned police work. And we're counting on your help. Again."
    
    
elif brycestatus == "good":
    
    show bryce normal b with dissolve
    
    c "Hey, Bryce. Isn't it a little early for a rematch?"

    show bryce laugh b with dissolve

    Br "I'd agree with you, but that's not why I'm here."
    
    show bryce stern b with dissolve

    Br "Today's agenda isn't nearly as exciting or fun."

    c "Well, what is it?"

    show bryce normal b with dissolve

    Br "Just some good, old-fashioned police work. And we're counting on your help. Again."

elif brycestatus == "bad":
    
    show bryce stern b with dissolve
    
    Br "Hey, [player_name]. Don't worry, I'm not here to talk about last time. This is strictly business."

    c "Well, what is it?"
    
    show bryce normal b with dissolve

    Br "Just some good, old-fashioned police work. And we're counting on your help. Again."
    
    #$ brycestatus = "ex"
    
elif brycestatus == "neutral":
    
    show bryce normal b with dissolve
    
    Br "Hey, [player_name]. Good to see you again."

    c "Likewise."

    Br "I hope you're in the mood for some good, old-fashioned police work."
    
#status none    
else:
    
    show bryce stern b with dissolve
    
    Br "Hey, [player_name]."

    c "Hey, Chief. More bad news?"

    Br "Not quite, unless you count Reza still missing as bad news. But that's kinda why I'm here."

    c "Well, what is it?"

    show bryce normal b with dissolve

    Br "Just some good, old-fashioned police work. And we're counting on your help. Again."
    
    
$ chap2inv = 0
$ chap2invt = 0

menu:
    
    "I'm not really in the mood to look at corpses today.":
        
        $ renpy.pause (0.5)
        
        show bryce laugh b with dissolve
        
        Br "Don't worry, we have something else planned."
        
        $ chap2inv -= 1
        
    "Sure, sign me up.":

        $ renpy.pause (0.5)
        
        show bryce smirk b with dissolve
        
        Br "Great."
        
        $chap2inv += 1
        
    "It's not like I have anything better to do.":
        
        Br "Alright."
        
show bryce stern b with dissolve

Br "We obtained a list of places Reza visited in the days before he vanished. We'll check those out, maybe find a lead, and you might help us understand his motivations or give us some context to his actions."
    
c "I can certainly try."
    
if inv == "low":
    
    show bryce laugh b with dissolve
    
    Br "Don't worry, we don't expect too much from you."
    
elif inv == "normal":
    
    show bryce normal b with dissolve
    
    Br "That's all you have to do."
    
else:
    
    show bryce normal b with dissolve
    
    Br "I'm sure you'll do a great job."
    
    
c "That is reassuring."

Br "Are you ready to go?"

c "Sure, let's go."

play sound "fx/steps/clean2.wav"

scene black with fade
scene town2 with fade

show bryce stern b with dissolve

Br "There's a couple of places we can check out. Let's see where we should go first..."

m "While Bryce focused on his list, I saw someone approach out of the corner of my eye."

m "A closer look revealed that it was Sebastian, waving his arm in an attempt to get our attention as he ran toward us, his face grave."

stop music fadeout 2.0

show bryce at right with ease

show sebastian normal b flip at left with easeinleft

Sb "There you are, Chief. I was looking for you."

play music "mx/threat.ogg"

show bryce brow b with dissolve

Br "What are you doing here?" 

#show bryce stern b with dissolve

Br stern b "Don't tell me there's another dead person."

Sb "Sorry, Chief. There is."

Br "Damn. Guess it's going to be one of those days." 
    
Sb "Yeah, looks that way."

Br "Someone else can take care of that today, though. We've got other plans."

Sb "You'll need to sign off on a few things, at least."

Br "I know, I know. We'll go to the crime scene, sign a few forms and then we're out."

play sound "fx/steps/clean2.wav"
    
scene black with fade
$ renpy.pause (1.0)
scene town4 with dissolveslow

#play music "mx/threat.ogg"
  
m "When we arrived at the scene, I saw the poor victim next to one of the houses. The obligatory sheet that was draped over him provided a modicum of discretion, but did nothing to hide the crime that had occurred."

show bryce stern b at right with easeinright

show sebastian normal b flip at left with easeinleft

Br "Alright, give me the story."

Sb "It's an interesting one, that's for sure. The wounds match those of the last victim, so a similar - if not identical - murder weapon is likely."

Sb "The victim? Maintenance person for this area. And the electricity is out. The power goes out, maintenance guy shows up and is killed before he can fix the problem. At least that's my theory."

Br brow b "So the power for the whole block is still out?"

Sb "That is correct."

Br stern b "We should get that fixed as soon as possible. We don't need civilians showing up around here complaining about sitting in the dark."

Sb "Good point."

m "Bryce's snout wrinkled with distaste as he glanced over Sebastian's shoulder."

Br "Damn, not again."

Sb "What is it?"
    
hide sebastian with easeoutleft

show sebastian normal b at Position(xpos = 0.86) with easeinright

show maverick normal flip at Position(xpos = 0.13) with easeinleft

Br brow b "What are you doing here, Maverick?"

Mv "A second victim, huh?"

Br stern b "This is an official investigation, so you better not cross that police line."

Mv angry flip  "Shunned by my own colleagues. This is ridiculous." 

Sb "You know how it is. Rules are rules. And without rules, murders like this one would be allowed to happen and go unpunished."

Mv "Tchk. Have your fun without me, then." 

show maverick normal flip with dissolve
$ renpy.pause (0.5)
show maverick normal at Position(xpos = 0.29)
$ renpy.pause (0.3)
hide maverick normal with easeoutleft
$ renpy.pause (0.5)

hide sebastian with easeoutright

show sebastian normal b flip at left with easeinleft

Sb "What do you think he wanted here, Chief?"

Br "That one's easy: To do his own investigation, just like he said he would. I shouldn't be surprised he showed up, but I guess we're lucky we arrived before he did."

Sb "I agree."

Br "We better check out that power outage now."

Sb "Of course. I think the door to the maintenance room is right around here."

stop music fadeout 2.0

$ renpy.pause (0.5)

play sound "fx/door/door_open.wav"

scene black with fade

scene stairs at Pan((0, 0), (0, 233), 3.0)
show dark2
with dissolveslow

$ renpy.pause (2.0)

Br "You got your flashlight, Seb?"

Sb "Always, Chief."

Br "You should go first, then. I don't have my stuff here."

Br "Besides, putting on that head mount is such a hassle."

Sb "I remember. You complain about that every time it comes up."

play sound "fx/button_on.ogg"

hide dark2
show flashlight2 at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
with None

$ renpy.pause (0.4)

Sb "There, that should do the trick."

$ renpy.pause (0.6)

show flashlight2 at Position(xpos = 0.38, xanchor=0.5, ypos=0.65, yanchor=0.5) with ease

$ renpy.pause (0.6)

show flashlight2 at Position(xpos = 0.20, xanchor=0.5, ypos=0.2, yanchor=0.5) with move2

$ renpy.pause (0.6)

show flashlight2 at Position(xpos = 0.1, xanchor=0.5, ypos=0.45, yanchor=0.5) with ease

Br "You just stay behind me, [player_name], alright?"

c "Okay."

play soundloop "fx/steps/slowstepsdown.ogg"

show stairs at Pan((0, 233), (0, 0), 3.0)
#$ renpy.pause (3.0)
show flashlight2 at Position(xpos = 0.24, xanchor=0.5, ypos=0.1, yanchor=0.5) 
with move4

Br "Gah, I hate stairs. Especially those made for smaller dragons like you."

Sb "Trust me, having it the other way around isn't too great, either." 

menu:
    "[[Say nothing.]":
        pass
        
    "I don't mind stairs.":
        
        c "I don't mind stairs that much."

        Sb "I can see why. Your legs have more articulation than even mine, especially the knees. Out of us three, I think Bryce has it the worst right now."

        Br "Damn you and your articulated knees."
        
    "I dislike all kinds of stairs.":
        
        c "I just dislike all kinds of stairs, period."

        Br "That's what I'm talking about."
        
show flashlight2 at Position(xpos = 0.97, xanchor=0.5, ypos=0.15, yanchor=0.5) with move3

Sb "This kinda reminds me of when we found that underground base, or whatever it was. Remember, Chief?"

Br "How could I not? It wasn't that long ago."

show flashlight2 at Position(xpos = 0.97, xanchor=0.5, ypos=0.8, yanchor=0.5)
show stairs at Pan((0, 0), (0, 233), 3.0)
with move4

$ renpy.pause (1.0)

c "Underground base?"

Br "Yeah, the portal wasn't the only piece of ancient technology we found. There was also this whole... lab near it. Seemed to have some high-tech stuff in there."

Br "At least that place didn't have as many stairs."

show flashlight2 at Position(xpos = 0.38, xanchor=0.5, ypos=0.7, yanchor=0.5) with move3

c "Wait, so you not only found the portal, but a whole facility along with it?"

Br "Yes, but we're not sure how much the two are actually related."

show flashlight2 at Position(xpos = 0.47, xanchor=0.5, ypos=0.13, yanchor=0.5) with move3

Br "We spent all that time studying the portal and barely got anywhere with it. This stuff is just... beyond what we know."

show flashlight2 at Position(xpos = 0.85, xanchor=0.5, ypos=0.2, yanchor=0.5) with move3

stop soundloop fadeout 1.0

Sb "Here we are."

show black with fade

#scene doorc at Pan((0, 1481), (0, 533), 7.0)
scene doorc at Pan((0, 1481), (0, 1007), 3.0)
show flashlight2 at Pan((1000, 0), (1000, 100), 3.0)
with dissolveslow

show flashlight2 at Position(xpos = 0.2, xanchor=0.5, ypos=0.6, yanchor=0.5) with move3
show flashlight2 at Position(xpos = 0.2, xanchor=0.5, ypos=0.6, yanchor=0.5) with move
show flashlight2 at Position(xpos = 0.8, xanchor=0.5, ypos=0.4, yanchor=0.5) with move3
show flashlight2 at Position(xpos = 0.8, xanchor=0.5, ypos=0.4, yanchor=0.5) with move

show doorc at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
show flashlight2 at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) 
with move2

$ renpy.pause (1.0)

play sound "fx/door/opendoorslow.ogg"

show black with fade
$ renpy.pause (1.0)
play soundloop "fx/steps/slowechosteps.ogg"
scene darker at Pan((0, 0), (0, 360), 6.0)
show flashlight2 at Pan((1000, 0), (1000, 100), 3.0)
with dissolveslow

show flashlight2 at Position(xpos = 0.3, xanchor=0.5, ypos=0.6, yanchor=0.5) with move3
show flashlight2 at Position(xpos = 0.3, xanchor=0.5, ypos=0.6, yanchor=0.5) with move
show flashlight2 at Position(xpos = 0.7, xanchor=0.5, ypos=0.4, yanchor=0.5) with move3
show flashlight2 at Position(xpos = 0.7, xanchor=0.5, ypos=0.4, yanchor=0.5) with move
show flashlight2 at Position(xpos = 0.6, xanchor=0.5, ypos=0.6, yanchor=0.5) with move2

$ renpy.pause (0.5)

Sb "So, what exactly are we looking for?"

Br "Whatever's causing the power outage. If we don't find the cause, we should at least be able to get the backup running."

show flashlight2 at Position(xpos = 0.62, xanchor=0.5, ypos=0.7, yanchor=0.5) with move4
$ renpy.pause (1.0)
show flashlight2 at Position(xpos = 0.57, xanchor=0.5, ypos=0.5, yanchor=0.5) with move4
stop soundloop fadeout 1.0
$ renpy.pause (1.0)

Sb "Looks like the generator is gone."

Br "Mystery solved."

play sound "fx/creak2.ogg"

m "The sound of creaking metal penetrated the stillness of the room." 

#show darker at Position(xpos = 0.5, xanchor=0.5, ypos=-0.01, yanchor=0.0) with move4
show darker at Position(xpos = 0.5, xanchor=0.5, ypos=0.0, yanchor=0.0) 
show flashlight2 at Position(xpos = 0.6, xanchor=0.5, ypos=0.2, yanchor=0.5)
with move4

play sound "fx/creak3.ogg"

$ renpy.pause (1.5)

show darker at Position(xpos = 0.5, xanchor=0.5, ypos=0.34, yanchor=0.5)  
show flashlight2 at Position(xpos = 0.7, xanchor=0.5, ypos=0.7, yanchor=0.5)
#hide flashlight2

with vpunch

m "I looked above toward the source of the noise as it grew louder, and in the next instant I was pushed sideways and fell to the ground — just barely avoiding the giant light fixture that fell from the ceiling and shattered into countless pieces alongside me."

Br "[player_name]! Are you alright?"

m "The next thing I saw was a hooded figure standing above me, barely visible against the darkness that permeated the room."

show black with dissolve
$ renpy.pause (0.5)
show cgmeeting at Pan ((200, 608), (700, 0), 8) with dissolvemed

$ renpy.pause (7.5)

play music "mx/bells.ogg"

m "The figure crouched down next to me, its mask hovering right in front of my face. Merely a whisper reached my ears when it spoke."

"???" "Be careful, [player_name]."

hide cgmeeting 
hide black
with fade

m "Then, the figure dashed towards the stairs."

play sound "fx/quickstairs.ogg"

$ renpy.pause (0.5)

Sb "Where are you going?"

c "That... that's not me!"

Br "Don't move!"

if persistent.izumiseen == True:

    c "She's going up the stairs!"
    
else:

    c "He's going up the stairs!" #switch text in subsequent playthroughs

Sb "I'm on it!"

play sound "fx/runstumblefall.ogg"

$ renpy.pause (0.3)

show flashlight2 at Position(xpos = 0.47, xanchor=0.5, ypos=0.8, yanchor=0.5) with move

show flashlight2x at Pan((1350, 350), (1450, 1400), 0.2) 
hide flashlight2
with vpunch

$ renpy.pause (0.35)

show flashlight2x at Pan((1550, 0), (1650, 1400), 0.3) 

$ renpy.pause (0.45)

show flashlight2x at Pan((1700, 0), (1800, 1400), 0.45) 

$ renpy.pause (0.55)

show flashlight2x at Pan((1900, 0), (1950, 700), 0.3) 


Sb "I didn't see that chair coming..."

Br "I can't see a damn thing in here!"

show flashlight2x at Pan((1950, 700), (1350, 450), 0.5) 

$ renpy.pause (0.5)

show flashlight2x at Pan((1350, 450), (1350, 550), 0.3)

$ renpy.pause (0.4)

Sb "Here, Chief!"

play sound "fx/stupidstairs.ogg"

Br "I hate these stupid stairs!"

Sb "You're blocking the way!"

Br "Just go around me!"

stop music fadeout 1.0

play sound "fx/blocking.ogg"

Sb "There's no room, you're as wide as the stairs are!"

Br "I can't help it!"

$ renpy.pause (2.0)

Br "Damn it! We'll never catch him now..."

$ renpy.pause (1.0)

scene black with dissolveslow

$ renpy.pause (1.0)

scene town4 with dissolveslow

play music "mx/elegant.ogg" fadein 1.0

m "By the time we found our way back up, the mysterious figure was nowhere to be found."

show bryce stern b at right with easeinright

show sebastian normal b flip at left with easeinleft

Br "We've got a long search ahead of us... and with a head start like that, there might be no end to it."

Sb "We have to take our chances as long as we still can."

Br "Except that chance is growing smaller and smaller while we wait for the team to arrive."

Sb "What even happened down there?"

Br "Right. [player_name], tell us everything in as much detail as you can."

c "There wasn't much to it. I heard a noise, I looked up, the light fixture came down, then someone pushed me- "

Br brow b "You mean Reza."

menu:
    
    "I guess so.":
    
        Br "What do you mean? Didn't you see him?"

    "I don't think it was Reza.":

        Br "What makes you say that?"
        
        $ chap2inv -= 1

    "I'm not so sure of that.":
        
        Br "Didn't you see him?"

        $ chap2inv += 1

c "Whoever it was was wearing a mask."

Br "It bloody well can't be someone else, so let's not kid ourselves here."

if persistent.izumiseen == True:
    
    Sb disapproval b flip "Wait a minute... When we were down there, didn't you refer to him as \"she\"?"
    
    c "Did I? I don't know, maybe you just heard it wrong."
    
    Sb normal b flip "Maybe."

show bryce stern b with dissolve

Sb "Why would he wear that whole getup, though?" 

menu:
    
    "He didn't want to be recognized.":  
        
        $ renpy.pause (0.5)

        Br brow b "That's a bad excuse when there are only two humans here."

        $ chap2inv -= 1
        
        show bryce stern b with dissolve

    "As some sort of camouflage.":

        Br "Good point."

        $ chap2inv += 1

    "For protection.":
        
        $ renpy.pause (0.5)

        Br brow b "I'm not so sure about that, but who knows?"
        
        show bryce stern b with dissolve

Sb "This whole thing doesn't make any sense."

Br "Let's take a step back and look at the bigger picture."

Br "Your earlier theory about what happened was pretty sound, Sebastian. Let's go with that, and add the bit about the generator being stolen."

Br brow b "So, now the question is: Who has a motive for stealing a generator?"

menu:
    "It could be anyone, really.":

        $ renpy.pause (0.5)

        Br stern b "Technically, yes, but it's unlikely that someone who lives here would resort to stealing a generator when they could easily buy or even just request one. It's not really the kind of thing that would get stolen around here."

        Sb "How about Reza?"
        
        $ chap2inv -= 1

    "I have no idea.":

        Sb "Reza."

        Br stern b "Right. Who else would need to steal a generator, when those who live here could either buy or even simply request one? Not to mention, Reza was the one who arranged the diplomatic trade for the generators in the first place."

    "Reza.":

        $ renpy.pause (0.5)

        Br stern b "Right. Who else would need to steal a generator, when those who live here could either buy or even simply request one. Not to mention, Reza was the one who arranged the diplomatic trade for the generators in the first place."

        $ chap2inv += 1

c "I can't deny the fact that your generators are pretty important to us, but resorting to murder?"

Br brow b "We all saw the human figure running away."

$ chap2q11 = True
$ chap2q12 = True

label chap2q1:
    
menu:
    
    "Why would he have stayed here if he stole it?": 

        c "Why would he remain here if he was the one who stole it? The generator was already gone when we got here, and the person in question wasn't carrying it, either."

        $ chap2inv += 1

    "Maybe it was a dragon in disguise." if chap2q11:

        $ renpy.pause (0.5)

        Br stern b "Judging by the person's mannerisms, posture and speed, I'd say no. None of our kind moves like that." 
        
        show bryce brow b with dissolve

        $ chap2q11 = False

        jump chap2q1

    "Are we sure we saw him running away?" if chap2q12:

        Br "Now you're grasping at straws, [player_name]."

        $ chap2inv -= 1

        $ chap2q12 = False

        jump chap2q1

Sb "Perhaps this is a case where the criminal has returned to the crime scene."

Br stern b "For this kind of crime? I'd say no, but who knows? Maybe our rules just don't apply anymore."

c "What do you mean?"

Br "No offense, but ever since you two humans arrived, there have been a lot of strange things going on. This place used to be a quiet town."

menu:

    "So you think it was Reza.":

        Br "Honestly, things aren't looking great for him right now. It's still our top priority to find him, but after what we've seen here today, I'm not sure what will happen when we do. I just don't want to give you any false hope, you know?"

        c "I see."

        $ chap2inv += 1

    "You're starting to sound like Maverick.":
        
        $ renpy.pause (0.5)

        Br brow b "To be fair, we saw a human running away from the crime scene. Given what we know so far, there's only really one option."
        
        #$ evilpoints += 1
        
        show bryce stern b with dissolve

    "Maybe this whole thing is just a huge misunderstanding.":

        c "Maybe this is all a huge misunderstanding and he just needs someone to talk to him."

        Br brow b "Let's put this into perspective: We've found two corpses so far. Reza is the prime suspect, and you think all he needs is someone to talk to him? Sorry, but I'll be going with a \"no\" on that one."

        show bryce stern b with dissolve
        
        $ chap2inv -= 1
        
    "You do understand why he ran away in the first place, right?" if persistent.neutralending:

        c "You do understand why he ran away in the first place, right? Strange, alien world; a big, scary dragon coming to arrest him; and he had no idea what consequences being arrested would have here."

        Br "Are you actually defending him?"

        c "No, I'm just looking for an explanation."

        $ evilpoints += 2

Sb "Maybe we should just focus on finding him and point fingers later."

c "Agreed."

Br "The police team will be here any minute now. You don't have to get involved with the search, but that doesn't mean you can't help us."

c "What do you want me to do?"

Br normal b "We still have the list of places we were going to check out, remember? We can't go now; the search takes priority." 

Br "Of course we'll still check out those places after we're done here, but if you go on your own you can speed up the process. You could even find a lead for us, who knows?" 

menu:

    "Sure thing.":
        
        $ renpy.pause (0.5)

        Br smirk b "Great."

        Br "Here's the list."

        $ chap2inv += 1

    "You must be really understaffed if you need to rely on me.":

        Br "It has less to do with my staff and more with what I told you last time. You know him, and that gives you experience that can help us understand how he thinks. That's the kind of help we really need."

        Br smirk b "In any case, here's the list."

    "How about no?":

        $ renpy.pause (0.5)

        Br brow b "I figured you'd want to help find Reza, but I suppose I can't make you."

        Br "Here's the list in case you change your mind."

        $ evilpoints += 1

        $ chap2inv -= 1

Br normal b "Considering your status, you shouldn't have any trouble in these places, but if anything happens, call me and I'll check up on you later."

c "Wait a minute. You mean I'm going all by myself?" 

Br "All of us are going to be busy with the search, and we can't really afford to spare someone right now. You'll be fine."

c "Aren't you worried I'll do something fishy? I mean, isn't that why Reza and I were assigned police escorts in the first place?"

Br smirk b "That policy was mostly Maverick's fault, and he's out of the picture. With my authority as chief, I say you can go alone."

Br normal b "I already know where you're going, and besides, I trust you. If you were in cahoots with Reza, you would have run off with him when you had the chance."

c "Good point."

Br stern b "Ah, I see the team approaching. Guess you should get going."

c "Alright. I'll see you later, then."

Br "Good luck."

label chap2testx:

show black with dissolveslow

$ renpy.pause (1.0)

show town1 with dissolveslow

nvl clear

window show

label chapter2sections2:

n "It was a relief to leave the crime scene, considering all that had happened. When I reached into my pocket to take a look at the list, however, I found something unexpected."

n "It was a small piece of paper with the word \"Tatsu\" written on it. How did it get there?"

window hide

scene cgmeeting2 gray at Pan ((700, 0), (700, 0), 0) with fade

$ renpy.pause (2.0)

scene town1 with fade

#nvl clear

window show

n "My earlier encounter with the masked person was the only time today someone was close enough to smuggle something into my pocket. I figured if someone like Bryce tried to do something like that, I definitely would have noticed."

n "As for \"Tatsu\"... The only related thing I could think of was Tatsu Park, which I had come across when I went to the police station the other day."

n "Even if that park was the place the mysterious paper referred to, I didn't know if it was actually a good idea to visit. The masked person may have saved me from the falling light fixture, but if it was Reza, it would mean following someone who was also the prime suspect of two murders."

nvl clear

n "I also had to consider the list of places Reza had been to: A local grocery store, the production facility we had visited and the library were the three places closest to here."

n "It certainly was going to be a busy day, and I knew I wouldn't have the time to visit all of them."

window hide

$ chapter2sectionsplayed = 0
$ chapter2libraryunplayed = True
$ chapter2storeunplayed = True
$ chapter2facilityunplayed = True
$ chapter2parkunplayed = True
$ chap2shrubberysearched = 0
$ chap2pavsearched = 0
$ chap2rested = 0

label chapter2sections:
    
    if chapter2sectionsplayed == 0:
        
        menu:
            
            c "What should I do?"
            
            "Visit the grocery store.":
                
                play sound "fx/steps/clean2.wav"
                scene black with fade
                jump chap2store
                
            "Visit the production facility.":

                play sound "fx/steps/clean2.wav"
                scene black with fade
                jump chap2facility
                
            "Visit the library.":
                
                play sound "fx/steps/clean2.wav"
                scene black with fade
                jump chap2library
                
            "Visit Tatsu Park.":
                
                play sound "fx/steps/clean2.wav"
                scene black with fade
                jump chap2park        
            
    elif chapter2sectionsplayed == 1:
        
        menu:
        
            c "I've got some more time left. What should I do?"
            
            "Visit the grocery store." if chapter2storeunplayed:
                
                play sound "fx/steps/clean2.wav"
                scene black with fade
                jump chap2store
                
            "Visit the production facility." if chapter2facilityunplayed:

                play sound "fx/steps/clean2.wav"
                scene black with fade
                jump chap2facility
                
            "Visit the library." if chapter2libraryunplayed:

                play sound "fx/steps/clean2.wav"
                scene black with fade
                jump chap2library
                
            "Visit Tatsu Park." if chapter2parkunplayed:

                play sound "fx/steps/clean2.wav"
                scene black with fade
                jump chap2park        
                
            "Get some well deserved rest.":
                
                m "I decided I had done enough for today and went to my apartment to relax for a few hours until the afternoon sun hung low in the sky and I decided it was time to report my findings to the police. A brief call to the department, and I was on my way to an appointment with Sebastian."
                
                $ persistent.lazynumber += 1
                call lazycheck from _call_lazycheck_4
                
                jump chap2cont2
    
        
    else:
        
        jump chap2cont
        
        
label chap2store:

$ metclerk = True
$ chapter2sectionsplayed += 1
$ chapter2storeunplayed = False
$ persistent.seenvarain2 = True

if persistent.playedzhong == True:
    define St = Character("Zhong", color="#7e9147", image="zhong")

scene store at Pan ((0, 360), (0, 150), 4.0) with fade

play sound "fx/door/bell.ogg"

m "I entered the store, the sound of a bell alerting the staff to my arrival. Seeing the patrons browsing the shelves - neatly stocked with wares of all kinds - evoked some feelings of nostalgia and normalcy in me." 

c "(This must be the store Reza's been shopping at.)"

#show cgclerk at Pan ( (0, 0), (100, 327), 6.0) with fade
show cgclerk at Pan ( (0, 0), (0, 327), 6.0) with fade


$ renpy.pause (4.5)

hide cgclerk with fade

c "(Who's he talking to?)"

c "(Hey, I think I've seen her before.)"

show vara normal flip at left with easeinleft

show zhong normal c at right with easeinright

St "I'm sorry, but this prescription has expired."

show vara none flip with dissolve

if persistent.varasaved == True:

    Vr "..."
    
else:
    
    "???" "..."

St "I can't fill it like this. You'll need to tell your parents to visit the doctor so he can write you a new one."

if persistent.varasaved == True:

    Vr "..."
    
else:
    
    "???" "..."

show vara none

$ renpy.pause (0.3)

hide vara with easeoutleft

play sound "fx/door/bell.ogg"

m "She turned around, nearly running into me when she suddenly bolted toward the door."

#play sound "fx/door/bell.ogg"

#$ renpy.pause (0.5)

if brycebar == True:
    
    St "Hello, [player_name]. How can I help you?"

    c "Wait, aren't you the bartender from the other day?"

    St "That I am. Did you have fun that evening?"

    c "Not really. I'm not much of a fan of drinking contests."

    St "That's Bryce for you."
    
    c "He apologized for it, though, so I guess it's all good now."
        
    St "He did? What did you do to him?"
    
    c "Nothing. At least not that I know."
    
    St "Interesting. I guess he realized getting you drunk might not be such a good idea, or he just really likes you."
    
    St "You know, you can do more in the bar than just getting drunk."
    
    c "Oh, really?"
    
    St "I could show you some time, if you want to."
    
    c "Is that an invitation?"
    
    St "Well, if you put it that way, it kind of is."

    if persistent.playedzhong == True:
        
        $ zhongnameavailable = True
        
    else:
    
        $ zhongavailable = True
    
elif leftbryce == True:
    
    St "Hello, [player_name]. How can I help you?"

    c "Wait, aren't you the bartender from the other day?"

    St "That I am. You just leaving Bryce behind caused quite a bit of trouble for me. That was awfully nice of you. Emphasis on \"awful\"."
    
    menu:
        
        "Sorry about that.":

            c "I'm very sorry about that. I was drunk out of my mind."

            St "I suppose that's the downside of working in a bar. Everybody's there to get drunk."

            c "I imagine Bryce didn't take it well, either."

            St "He did not."

            c "I bet he's angry with me..."

            St "He isn't the kind of person to stay mad about something like that. I think if you call him and explain things, it should be fine. If you want to, that is."

            c "I'll keep that in mind, thanks."

            St "If you want to come by some time, I could tell you more."
    
            c "Oh, really?"
            
            St "And even though it's a bar, the alcohol is always optional."
            
            c "Good to know. I'll think about it."
            
            if persistent.playedzhong == True:
                
                $ zhongnameavailable = True
                
            else:
            
                $ zhongavailable = True
            
        "I regret nothing.":
            
            pass

elif brycestatus == "bad":
    
    St "Hello, [player_name]. How can I help you?"

    c "Wait, aren't you the bartender from the other day?"

    St "That I am. Did you have fun that evening?"

    c "Sort of. I think Bryce isn't too fond of me."

    St "I know he can be a little rough around the edges, but if you call him and talk about what happened, it should be fine. If you want to, that is."

    c "I'll keep that in mind, thanks."
    
    St "If you want to come by some time, I could tell you more."
    
    c "Oh, really?"
    
    St "And even though it's a bar, the alcohol is always optional."
    
    c "Good to know. I'll think about it."
    
    $ brycestatus = "neutral"
    
    if persistent.playedzhong == True:
        
        $ zhongnameavailable = True
        
    else:
    
        $ zhongavailable = True
    
elif brycestatus == "good":
    
    St "Hello, [player_name]. How can I help you?"

    c "Wait, aren't you the bartender from the other day?"

    St "That I am. Did you have fun that evening?"

    c "Yeah. You've got some interesting drinks, if I do say so myself."

    St "Did you enjoy what you tried? You haven't even experienced a fraction of what I have to offer."

    c "Is that a challenge?"

    St "More of an invitation, really. You can come by any time if you are interested in seeing what else I have in store."

    c "Thanks, I'll keep that in mind."

    if persistent.playedzhong == True:
        
        $ zhongnameavailable = True
        
    else:
    
        $ zhongavailable = True

elif brycestatus == "neutral":

    St "Hello, [player_name]. How can I help you?"

    c "Wait, aren't you the bartender from the other day?"

    St "That I am. Did you have fun that evening?"
    
    c "Yeah, it was alright."
    
    St "You know, you can do more in the bar than just getting drunk."
    
    c "Oh, really?"
    
    St "I could show you some time, if you want to."
    
    c "Is that an invitation?"
    
    St "Well, if you put it that way, it kind of is."
    
    if persistent.playedzhong == True:
        
        $ zhongnameavailable = True
        
    else:
    
        $ zhongavailable = True

else:
    
    St "Hello, [player_name]. How can I help you?"

    c "You know who I am?"

    St "How could I not? Everyone knows about you."

St "Anyway, how can I help you?"

$ chap2storewho = True
$ chap2receiptsuntaken = True
$ chap2storebrowse = True

$ chap2storebread = True
$ chap2storeproduce = True
$ chap2storemeat = True
$ chap2storehealth = True

$ chap2storenumber = 0

label chap2storeques:

menu:
    
    "Who was that?" if chap2storewho:

        St "You mean the girl? That's Vara."

        St "She comes here occasionally to pick up her mother's prescription."
        
        $ persistent.seenvara = True

        $ chap2storewho = False
        
        jump chap2storeques
        
    "Do you remember Reza coming here?" if chap2receiptsuntaken:

        St "Of course I do. It's only been a few days since he was last here."

        c "This will sound a little unusual, but can you tell me what he bought?"

        St "Are you just talking about last time or every time he came here?"

        c "Both, I suppose. He came here more than once?"

        St "He's been visiting pretty regularly, now that I think about it."

        c "Interesting."

        St "I can look up his purchases if you like."

        c "That would be really helpful."

        St "Shouldn't be too hard, just give me a second."

        play sound "fx/register.ogg"
        
        $ renpy.pause (5.0)
        
        m "I watched him carefully navigate the register's buttons, soon followed by the sound of the attached printer."

        St "Here you go. Receipts from all his purchases."

        c "Well, that was easy."

        St "Since our government takes care of all his purchases, they're filed separately. It was simple to pull them up."

        play sound "fx/receipts.ogg"

        c "Looks like he bought mostly food and snacks. Sometimes magazines. But why was he buying lemons every single time?"

        St "I can't say that I didn't notice, but I figured it was just a human thing."

        c "Strange. In any case, that was more information than I expected. You have my thanks."

        St "You're welcome."
        
        stop sound fadeout 2.0

        $ chap2clues += 1
        
        $ chap2receiptsuntaken = False
        
        jump chap2storeques

    "Just browsing for now." if chap2storebrowse:
        
        St "Let me know if you need anything."
        
        show zhong normal c flip
        
        $ renpy.pause (0.3)
        
        hide zhong with easeoutright

        $ chap2storebrowse = False

        c "(What am I even looking for?)"
        
        label chap2storebrowsemenu:
        
        menu:
            
            "Look at the bread selection." if chap2storebread:

                c "(They have a surprisingly big selection.)"

                c "(Since when do dragons eat bread, anyway?)"

                c "(I guess at least I'm covered in case I want any melon bread.)"

                Op "Hey, you!"
                
                show ophinia normal with dissolve

                c "Are you talking to me?"

                Op "Yes! What do you say, melon or lemon bread? I mean, the only difference between the two is, like, one letter - so how am I supposed to choose?"

                c "(I don't think that's how it works...)"

                c "Why don't you just go with the one you think you'll like more?"

                Op "..."

                Op "That's a good idea. Why didn't I think of that?"

                $ renpy.pause (0.2)
                
                show ophinia normal flip

                $ renpy.pause (0.3)
                
                hide ophinia with easeoutright

                $ renpy.pause (0.5)

                c "(Was that a cardboard box on her head?)"

                $ chap2storebread = False

                $ chap2storenumber += 1
                
                jump chap2storebrowsemenu
            
            "Look at the produce." if chap2storeproduce:

                c "(Who would've thought that dragons are big on produce?)"

                c "(I don't even recognize some of these.)"

                $ chap2storeproduce = False

                $ chap2storenumber += 1

                jump chap2storebrowsemenu
            
            "Look at the meat." if chap2storemeat:
                
                c "(Meat, of course. Lots and lots of meat.)"

                c "(Fresh meat, smoked meat, cured meat, dried meat, pre-packaged meat, prepared meat, ready-to-eat meat, meat snacks, burgers, kebab, nuggets, whole hams, bacon, meat loaf, sausages.)"

                c "(And that's not even all of it. Needless to say, they have that area covered.)"

                $ chap2storemeat = False

                $ chap2storenumber += 1

                jump chap2storebrowsemenu

            "Look at the health aisle." if chap2storehealth:
                
                c "(Everything from food supplements to skin care and even birth control.)"

                c "(The variance in product sizes is astounding, especially when talking about the birth control.)"

                c "(I think these ones could fit on my arm.)"

                $ chap2storehealth = False

                $ chap2storenumber += 1

                jump chap2storebrowsemenu
                
            "Go back.":
                
                c "(Enough browsing, I should go back to what I came here for.)"

                if chap2storenumber == 4:
                    
                    if persistent.c2storeaisles == False:

                        $ persistent.c2storeaisles = True
                        
                        $ achievement.grant("Window Shopper")
                        
                        $ persistent.achievements += 1
                        
                        call syscheck from _call_syscheck_50
                        
                        play sound "fx/system.wav"
                        
                        if system == "normal":
                        
                            s "You looked at everything the store has to offer!"
                            
                        elif system == "advanced":

                            s "You looked at everything the store has to offer. Isn't that great?" 
                            
                        else:
                            
                            s "You looked at everything the store has to offer. Of course, you're not planning to buy anything."
                
                show zhong normal c at right with easeinright
                
                jump chap2storeques

            
        
    "[[Leave.]":
        
        c "(I suppose that's all I can do here.)"
        
        show black with dissolvemed

        $ renpy.pause (0.5)

        show town1 with dissolvemed
        
        jump chapter2sections
    
        
label chap2facility:
    
$ chapter2sectionsplayed += 1
$ chapter2facilityunplayed = False
scene facin2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

c "(Reza was allegedly here at some point. Maybe I should ask Anna.)"    

play sound "fx/knocking1.ogg"

$ renpy.pause (2.0)

c "Hello?"

play sound "fx/knocking2.ogg"

$ renpy.pause (2.5)

c "Anybody here?"

play sound "fx/door/door_open.wav"
#$ renpy.pause (0.3)
scene black with dissolve
$ renpy.pause (0.5)
#$ renpy.pause (0.3)
show cgdamion at Pan((0, 0), (0, 302), 5.0) with dissolvemed
$ renpy.pause(3.0)

hide cgdamion 
scene facin2 at Pan ((128, 250), (128, 250), 0.0)
show damion arrogant
with fade

$ metdamion2 = True
$ persistent.metdamion = True

"???" "Can I help you?"

c "I was just looking for Anna. This is her lab, right?"

show damion face with dissolve

"???" "Why don't I ever get any recognition? This is my lab as much as it is hers."

show damion normal with dissolve

"???" "Either way, Anna is not here. Would that be all?"

c "Since you work here, maybe you can help me instead."

show damion arrogant with dissolve

"???" "Oh, of course. Your precious Anna isn't here, so you'll have to settle for me. I see how it is."

if annastatus == "bad":
    
    c "Maybe it's not so bad that she isn't here at the moment. I met with her the other day, and it didn't go too well."
    
    show damion face with dissolve

    "???" "She's a bitch, isn't she? Now imagine having to share a lab with someone who still throws temper tantrums like a toddler."

    show damion normal with dissolve

    "???" "Anyway, how can I help you?"
        
else:
    
    c "That's not what I meant."
    
    show damion normal with dissolve

    "???" "Of course, of course. Let's just get this over with."

c "You could start by telling me who you are."

"???" "Here's the short version: My name is Damion. I work in this facility, and I'm unfortunate enough to live the nightmare of having to deal with Anna on a daily basis. Nice to meet you."

c "Nice to meet you, too."

Dm "And you are?"

c "You don't know who I am?"

Dm arrogant "Tchk, of course I know who you are, but your assumption validated the point I was going to make. You see, this whole thing about you coming here has been blown out of proportion, like it's some huge event that everyone should be celebrating."

Dm "Newsflash: Not everyone cares. Once both of you are gone, life will return to normal and we can all go back to what we actually should be doing."

c "I imagine a lot of it has to do with those human myths you have."

Dm normal "I can only reiterate: Not everyone cares."

Dm "What exactly did you want, again?"

$ chap2facreza = True
$ chap2facanna = True
$ chap2facres = True
$ chap2facres2 = True
$ chap2asked = False
$ chap2damionquestions = 0

label chap2facques:

menu:
    
    "Has Reza been here recently?" if chap2facreza:
        
        c "Do you know anything about Reza's visits to this facility?"

        Dm arrogant "I've seen him a few times. He would come by to ask about the progress of the generators."

        Dm face "Heh, there was this one time when Anna told him she'd have news, but when he came over, she just wanted to run some tests on him."
        
        c "Did he go through with it?"

        Dm arrogant "No, he wanted some... compensation, I suppose. Nothing she could offer satisfied him, however, and that was that."

        $ chap2asked = True
        
        $ chap2facreza = False

        $ chap2clues += 1
        
        show damion normal with dissolve
    
        $ chap2damionquestions += 1

        jump chap2facques
        
    "How long have you known Anna?" if chap2facanna:
        
        $ renpy.pause (0.5)

        Dm arrogant "Why do you care about that?"

        c "Maybe I want to find out what kind of person she is. You might have an idea."

        Dm face "I'll put it this way: I've known her far too long."
        
        show damion normal with dissolve

        $ chap2facanna = False

        $ chap2asked = True

        $ chap2damionquestions += 1
        
        jump chap2facques
        
    "What kind of research is Anna doing?" if chap2facres:
        
        $ renpy.pause (0.5)
        
        Dm arrogant "Cancer research. She thinks she can cure it, but she's out of her mind."

        c "Is that such a bad thing?"

        Dm face "The way she does it? Yes. She's wasting resources that could be better spent on projects with an actual chance of success."
        
        $ chap2facres = False

        $ chap2asked = True
        
        show damion normal with dissolve

        $ chap2damionquestions += 1
        
        jump chap2facques
        
    "What kind of research are you doing?" if chap2facres2:
        
        $ renpy.pause (0.5)

        $ chap2damionquestions += 1

        if blood == True:

            Dm face "Right now? Guess who got tasked with running all those tests on your blood."

            c "You did?"

            Dm arrogant "That's right. While she goes out and does whatever the heck she wants, I get to keep an eye on the experiment."

            c "Any interesting results?"

            Dm "Not just yet, but soon we'll know more about your body than you do."
            
        else:
            
            Dm arrogant "Nothing special, unless you care a lot about genetics. And we're not talking about the basics here, but the deep stuff."
            
        show damion normal with dissolve

        $ chap2asked = True
            
        $ chap2facres2 = False
        
        jump chap2facques
        
        
    "That's all." if chap2asked:

        c "Thanks for your help."

        Dm face "Yeah, yeah."
        
        hide damion with dissolve
        
        play sound "fx/door/doorclose.ogg"
        
        $ renpy.pause (0.5)
        
        show black with dissolvemed
        
        if chap2damionquestions == 4:
            
            if persistent.c2interrogator == False:
                
                $ renpy.pause (0.5)

                $ persistent.c2interrogator = True
                
                $ achievement.grant("Interrogator 1")
                
                $ persistent.achievements += 1
                
                call syscheck from _call_syscheck_51
                
                play sound "fx/system.wav"
                
                if system == "normal":
                
                    s "You interrogated Damion!"
                    
                elif system == "advanced":

                    s "You interrogated Damion. Fun times."
                    
                else:
                    
                    s "You interrogated Damion. Makes you feel important, eh?"  

        $ renpy.pause (0.5)

        show town1 with dissolvemed
        
        jump chapter2sections
    
label chap2library:

$ chapter2sectionsplayed += 1
$ chapter2libraryunplayed = False   
$ persistent.chapter2libraryvisited = True 

scene black with dissolve
scene library at Pan ((240, 228), (0,228), 3.0) with dissolveslow

c "(Alright, Reza. What did you want here?)"

c "(Hey, it's Remy.)"

show remy look flip at left with easeinleft

Ry "I already told you, it's not here."

c "(Who's he talking to? Adine?)"

show adine disappoint b at right with easeinright

Ad "Won't you help out an old friend?"

Ry sad flip "F-Friend?! This is the first time you've spoken to me in years."

Ad annoyed b  "And whose fault is that? For you, I didn't even exist these last few years. At least I tried to reach out to you."

Ry angry flip "No, you're just here because you want something."

Ad disappoint b "I'm right here, right now and you still continue to act like that. She was my friend too, you know."

Ry sad flip "..."

Ry "I think you should leave."

Ad "..."

show adine disappoint b flip

$ renpy.pause (1.0)

show adine disappoint b

$ renpy.pause (1.0)

Ad "For what it's worth, I'm sorry. For everything."

Ry "It's a little late for apologies."

Ad annoyed b "Have it your way, then."

show adine annoyed b flip

$ renpy.pause (0.3)

hide adine with easeoutright

$ renpy.pause (1.0)

show remy sad

$ renpy.pause (0.3)

hide remy with easeoutleft

m "Adine stormed out so quickly that she didn't even notice me."

m "I waited a few moments and wondered if it was a good time to talk to Remy. In the end, I decided that my task was too pressing to come back at another time. I shuffled through books and tried to look busy until I noticed he resumed his work so I could approach him."

if remystatus == "good":
    
    show remy smile with dissolve

    Ry "Oh, hello [player_name]! Good to see you again."

    c "You too, Remy."

    Ry normal "Sorry, I didn't get a chance to call you about the dinner yet, but there should be an opening soon. Anyways, do you need anything from me?"

elif remystatus == "neutral":
    
    show remy normal with dissolve
    
    Ry "Oh, hello [player_name]! Good to see you. Do you need anything?"

elif remystatus == "bad":
    
    show remy normal with dissolve
    
    Ry "Can I help you?"
    
else: 

    show remy normal with dissolve
    
    Ry "Hello [player_name]. How can I help you?"


$ chap2libreza = True
$ chap2libadine = True
$ chap2libmood = True
$ chap2libapologize = False
$ chap2libasked = False

label chap2libmenu:
menu:
    
    "Has Reza been here recently?" if chap2libreza:

        $ chap2libasked = True
        
        Ry "Reza? He's visited quite often since he arrived, actually. Until a few days ago, that is."

        c "Do you know what he was reading?"

        Ry "Not particularly. I thought he just wanted to learn about our world."

        c "Did you notice anything unusual about him while he was here?"

        Ry "Can't say I did, though he did ask me for a map once."
    
        c "A map?"

        Ry "Yes. I showed him a few, but none of them seemed to be what he was looking for."

        c "Did he talk to you about anything strange while he was here?"

        Ry "Besides the maps, nothing else worth mentioning comes to mind. Only the usual pleasantries."

        $ chap2clues += 1
    
        $ chap2libreza = False
        
        jump chap2libmenu
    
    
    "What did Adine want from you?" if chap2libadine:

        $ chap2libasked = True
    
        if remystatus == "bad":
            
            Ry look "Were you eavesdropping?"

            c "I can't exactly shut my ears off if I'm nearby."

            Ry "Whatever your reason, it isn't any of your business."
            
            show remy normal with dissolve
            
            $ chap2libadine = False
            
            jump chap2libmenu
                        
        else:
            
            Ry shy "Wait, you were here that whole time?"

            c "Not the whole time, just long enough to know that something's up."

            Ry "It's nothing that concerns you."

            c "Come on. It does concern me. I know you, and I know Adine."

            Ry normal "It's really nothing of great importance. Are you aware of a certain prehistoric underground building we recently discovered?"

            c "I've heard of it."
                
            Ry "She wanted a blueprint of it, which was one of the things found inside the building during an investigation."

            c "Why would you have it?"

            Ry "We're not just a library, you know, but a whole archive that stores all sorts of information and objects."
        
            if remy1unplayed == False:

                Ry "Do you remember the box you dropped last time you came here?"

                c "Yeah."

                Ry "It was filled with artifacts. We have them here for safekeeping."
                
            else:
                
                pass
                
            Ry "In any case, a blueprint is the kind of thing that would be placed in our care eventually."

            c "So she thinks you have it."

            Ry "Even if we did, it wouldn't be something we could just give out to anyone."

            c "Of course."
            
            $ chap2libadine = False
            
            jump chap2libmenu
            
    "How are you doing?" if chap2libmood:

        $ chap2libasked = True
        
        if remystatus == "bad":
            
            Ry "I'm fine, thank you."

            c "Somehow, I don't believe you."

            Ry look "Why would how I'm doing concern you?"

            c "Because I care."

            Ry sad "I... reject that notion. The last time you came here you acted in a manner that was unacceptable, and unless you need my assistance with something, this conversation is over."
                 
            $ chap2libmood = False
            $ chap2libapologize = True
            
            show remy normal with dissolve
            
            jump chap2libmenu
                 
        elif remystatus == "none":
            
            Ry "I'm doing fine, thank you."
            
            $ chap2libmood = False
            jump chap2libmenu
            
        else:
            
            Ry "I'm not sure, to be honest. There are a lot of things on my mind right now."

            c "Like what?"

            Ry shy "I'm not at liberty to discuss them at the moment. I'm supposed to be working, you know."
            
            show remy normal with dissolve
            
            $ chap2libmood = False
            jump chap2libmenu
    
    "[[Apologize.]" if chap2libapologize:

        c "I do have to apologize for last time."

        Ry look "Is that so?"

        c "I don't even know why I acted the way I did." 
        
        c "I guess it's not easy coming to another world with a different society and different standards."

        Ry "I'm listening."

        c "Is it really fair to judge me by your own standards when this place is completely alien to me? I just came from a totally different world, and I don't know anything about your standards yet."

        Ry "I suppose everyone deserves a second chance."

        c "Maybe if you took the time to get to know me, you wouldn't find me that bad. Besides, you said you were interested in humans, what with all the myths you were telling me about..."

        Ry "Alright, alright. I get it."
        
        c "So you are giving me another chance?"

        Ry "You have a few good points, so I guess it's only fair. Hopefully with less things being broken this time around, though."

        Ry normal "Seeing how you were talking about standards and such, what is a typical activity in your world that is used to get to know someone else?"

        c "We share meals together. Usually dinner."

        Ry "Then that shall be it." 
        
        $ remystatus = "good"
        
        $ chap2libapologize = False
        
        $ remyapologized = True
        
        jump chap2libmenu


    "That's all." if chap2libasked:

        c "Thanks for your help."

        Ry "You're welcome."
        
        hide remy with dissolve
        
        $ renpy.pause (0.5)

        show black with dissolvemed

        $ renpy.pause (0.5)

        show town1 with dissolvemed

        
        jump chapter2sections

    
    
label chap2park:

$ chapter2sectionsplayed += 1
$ chapter2parkunplayed = False
scene town2 at Pan ((300, 400), (150, 400), 3.0) with dissolveslow

#$ renpy.pause (2.0)

c "(Tatsu Park, here I am. I don't know what I'm even looking for, though.)"

label chap2park1choice:

menu:

    "Read the sign.":
        
        "\"This park is dedicated to our creator, to whom we owe our sentience and existence. As it is our duty to remember, this place honors them every day with its beauty and grants a place of recreation and contemplation to all of us.\""

        jump chap2park1choice
        
    "Look at the map.":
        
        c "(This park is bigger than I thought. I could go north, towards Tatsu Avenue, which apparently is a nice spot to look at the landscape, or south to the political district. Where should I go?)"

        menu:
            
            "North, towards Tatsu Avenue.":
                jump chap2park2

            "South, toward the political district." if chap2park3unvisited:

                $ chap2park3unvisited = False
                
                jump chap2park3
                
            "Stay in the central area.":
                jump chap2park1choice
                
    "Search the shrubbery.":
        
        if chap2shrubberysearched == 0:
            
            c "(Yeah, this totally won't look strange or suspicious. Here we go.)"
            
            play sound "fx/bushes.ogg"
            
            $ renpy.pause (4.0)

            c "(I found some dirt. There doesn't seem to be anything else here.)"
            
            if persistent.dirttaken == False:
            
                $ persistent.dirttaken = True
                
                $ achievement.grant("Archeologist")
                
                $ persistent.achievements += 1
                
                call syscheck from _call_syscheck_52
                
                play sound "fx/system.wav"
            
                if system == "normal":
                
                    s "You found a handful of dirt!"
                    
                elif system == "advanced":

                    s "You found a handful of dirt. How quaint."
                    
                else:
                    
                    s "You found a handful of dirt. That should come in handy somewhere. Or maybe not."

                $ chap2shrubberysearched += 1
                
                jump chap2park1choice
                
            else:
                
                $ chap2shrubberysearched += 1
                
                jump chap2park1choice
            
        else: 
            
            c "(Again? I guess I should look harder this time.)"

            play sound "fx/bushes.ogg"

            $ renpy.pause (4.0)

            c "(No, it seems there's still just dirt to be found here, and I don't think I'll need more than what I already have.)"

            jump chap2park1choice
            
            
    "Search the pavilion.":
        
        if chap2pavsearched == 0:
        
            c "(You never know what you'll find around a pavillion. Let's do this.)"
            
            play sound "fx/searchpav.ogg"

            $ renpy.pause (4.0)

            c "(There doesn't seem to be anything important here, but at least it provides excellent shade.)"
            
            $ chap2pavsearched += 1
            
            jump chap2park1choice

        elif chap2pavsearched == 1:
            
            label chap2findnothing:
            
            c "(Again? I guess I should look harder this time.)"
            
            play sound "fx/searchpav.ogg"

            $ renpy.pause (4.0)
            
            c "(No, nothing here.)"
            
            $ chap2pavsearched += 1
            
            jump chap2park1choice
            
        else:
            
            if persistent.orb_taken == False:
            
                c "(Again? I guess I should look harder this time.)"
                
                play sound "fx/searchpav.ogg"

                $ renpy.pause (4.0)

                c "(I found something!)"

                c "(It's a round, smooth orb about the size of a bowling ball.)"
                
                if persistent.ixomenbookread == True:
                    
                    c "(Wait a minute... I recognize this. It looks like something I saw in one of the books the other day.)"

                    c "(Might as well take it with me.)"

                    $ persistent.orb_taken = True
                    
                    $ achievement.grant("Orb Finder")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_53
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You acquired an Ixomen Sphere part (Orb)! {image=image/ui/status/orb_taken.png}"
                        
                    elif system == "advanced":

                        s "You acquired an Ixomen Sphere part (Orb). Orbsome!{image=image/ui/status/orb_taken.png}"
                        
                    else:
                        
                        s "You acquired an Ixomen Sphere part (Orb). I hope you have big pockets to carry this thing around in. {image=image/ui/status/orb_taken.png}"

                    jump chap2park1choice
                    
                else:
                    
                    c "(Not sure what it is, but I'll take it with me, just in case.)"

                    $ persistent.orb_taken = True
                    
                    $ achievement.grant("Orb Finder")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_54
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You acquired a mysterious orb! {image=image/ui/status/orb_taken.png}" 
                        
                    elif system == "advanced":

                        s "You acquired a mysterious orb. How mysterious. {image=image/ui/status/orb_taken.png}"
                        
                    else:
                        
                        s "You acquired a mysterious orb. Do you think it can float? {image=image/ui/status/orb_taken.png}"



                    jump chap2park1choice
            
            else:
                
                jump chap2findnothing

    "Stop searching the park.":
        
        c "(I don't think I'll find anything else here.)"

        show black with dissolvemed

        $ renpy.pause (0.5)

        show town1 with dissolvemed

        
        jump chapter2sections
            

label chap2park2:
    
    scene park2 with fade
    
    $ renpy.pause (0.5)
    
    label chap2park2choice:
    
    menu:
        
        "Rest on the bench.":
            
            if chap2rested == 0:
                
                c "(Finally, a place to sit down.)"

                c "(The view of the scenery is perfect.)"
                
                if persistent.c2landscape == False:

                    $ persistent.c2landscape = True
                    
                    $ achievement.grant("Landscaper")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_55
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You appreciated the landscape for a bit!"
                        
                    elif system == "advanced":

                        s "You appreciated the landscape for a bit. How relaxing."
                        
                    else:
                        
                        s "You appreciated the landscape for a bit. Now you feel like everything is going to be fine."


                c "(That was nice.)"

                m "I was just about to get up when I noticed someone sitting next to me."
                
                show dramavian normal at Position (xpos = 0.6) with dissolve

                c "Whoa, I didn't see you there. I thought you were a statue or something."

                Dr "..."

                c "Hello?"

                Dr "..."

                c "(Well, maybe it {i}is{/i} a statue. Or I just turned invisible.)"

                c "(I hope it's not the latter.)"

                hide dramavian normal with dissolve
                
                $ renpy.pause (0.3)
                
                $ chap2rested += 1
                
                jump chap2park2choice
                
            else:

                c "(I'm already well-rested. I shouldn't waste any more time.)"
                
                jump chap2park2choice

        "Open the hatch." if chap2bandageuntaken:
            
            show closed
            show handle at Position (xpos = 982, ypos = 648)
            with fade
            
            $ chap2button1 = 0
            $ chap2button2 = 0
            $ chap2lever = 1
            
            c "(On the metal covering of the hatch, there are two buttons which are situated to the left and the right of a central, circular lever. The arrow on the lever is pointing up.)" 

            label chap2hatch:
                
            if chap2button1 == 1:
                if chap2button2 == 1:
                    if chap2lever == 0:
                        
                        show black with dissolvemed

                        play sound "fx/hatchopen.ogg"
                        
                        stop music fadeout 2.0
                        
                        $ renpy.pause (2.0)
                        
                        if persistent.trueending:
                            
                            show open 
                            show hole
                            with dissolvemed
                            
                            play soundloop "fx/calloftheunearthly.ogg" fadein 2.0

                            m "Beneath the hatch, a strange-looking orb of darkness was floating in the shaft that leads down to the maintenance tunnels."

                            m "As I looked into the pitch black center of the orb, I felt strangely drawn to it, its low hum beckoning me to come closer."
                            
                            menu:
                                
                                "Touch it.":
                                    
                                    $ renpy.pause (2.0)
                                    
                                    stop music
                                    
                                    show glitch
                                    
                                    $ renpy.pause (1.0)
                                    
                                    scene black
                                    
                                    stop soundloop
                                    
                                    $ renpy.pause (2.0)
                                    
                                    $ save_name = "Prologue"
                                    
                                    jump holetravel
                                    
                                "Close the hatch.":
                                    
                                    scene black with dissolvemed
                                    
                                    stop soundloop fadeout 2.0

                                    play sound "fx/hatchclose.ogg"
                                    
                                    $ renpy.pause (2.0)

                                    play music "mx/elegant.ogg" fadein 2.0

                                    scene park2 with dissolvemed
                                    
                                    jump chap2park2choice
                                    
                                    
                            
                        else:
                        
                            show open 
                            show cloth
                            with dissolvemed
                            
                            m "I looked down to see the maintenance tunnels for the underground drain system. A pale object starkly contrasted against the pitch-black backdrop."
                            
                            play sound "fx/ladder1.ogg"
                            
                            $ renpy.pause (5.0)
                            
                            hide cloth with dissolvemed
                            
                            c "(It's a cloth with suspicious red markings all over it.)"
                            
                            if persistent.c2bandage == False:

                                $ persistent.c2bandage = True
                                
                                $ achievement.grant("Finders, Keepers")
                                
                                $ persistent.achievements += 1
                                
                                call syscheck from _call_syscheck_56
                                
                                play sound "fx/system.wav"
                                
                                if system == "normal":
                                
                                    s "You acquired a bloody bandage!"
                                    
                                elif system == "advanced":

                                    s "You acquired a bloody bandage. Gross."
                                    
                                else:
                                    
                                    s "You acquired a bloody bandage. Why you would want to pick up something like that is beyond me, though."

                            c "(I guess that's all to be found down here.)"
                            
                            play sound "fx/ladder2.ogg"

                            $ renpy.pause (5.0)

                            scene black with dissolvemed

                            play sound "fx/hatchclose.ogg"
                            
                            $ renpy.pause (2.0)
                            
                            #hide open
                            #show closed
                            #show button1
                            #show button2
                            #show handle at Position (xpos = 982, ypos = 648)
                            #hide black
                            #with dissolvemed

                            $ chap2clues += 1
                            
                            $ chap2bandageuntaken = False

                            $ evilpoints += 5
                            
                            #$ renpy.pause (1.0)
                            
                            #scene black with dissolve
                            
                            $ renpy.pause (0.5)
                            
                            scene park2 with dissolvemed
                            
                            play music "mx/elegant.ogg" fadein 2.0
                            
                            jump chap2park2choice
                        
                    else:
                        pass
                else:
                    pass
            else:
                pass
            
            menu:
                
                "Press the first button.":
                    
                    $ renpy.pause (0.5)
                    
                    if chap2button1 == 0:
                        
                        play sound "fx/button_press.ogg"

                        $ renpy.pause (0.2)
                        
                        show button1
                        
                        $ chap2button1 = 1
                        
                        c "(The first button is now pressed and sits flush with the metal covering of the hatch.)"
                        
                        jump chap2hatch
                        
                    else:

                        $ renpy.pause (0.2)
                        
                        play sound "fx/button_unpress.ogg"
                        
                        hide button1
                        
                        $ chap2button1 = 0
                        
                        c "(After pressing the first the button again, it has returned to its original position, sticking out slightly against the metal covering of the hatch.)"
                    
                        jump chap2hatch
                    
                "Press the second button.":

                    $ renpy.pause (0.5)

                    if chap2button2 == 0:
                        
                        play sound "fx/button_press.ogg"

                        $ renpy.pause (0.2)

                        show button2
                        
                        $ chap2button2 = 1
                        
                        c "(The second button is now pressed and sits flush with the metal covering of the hatch.)"
                        
                        jump chap2hatch
                        
                    else:
                        
                        $ renpy.pause (0.2)
                        
                        play sound "fx/button_unpress.ogg"
                        
                        hide button2
                        
                        $ chap2button2 = 0
                        
                        c "(After pressing the second button again, it has returned to its original position, sticking out slightly against the metal covering of the hatch.)"
                    
                        jump chap2hatch
                    
                "Turn the lever clockwise.":
                    
                    $ renpy.pause (0.5)
                    
                    if chap2lever == 0:
                        
                        show handle:
                            xpos 983 
                            ypos 680
                            rotate 270
                        
                        show handle:
                            
                            linear 1.5 rotate 360
                    
                    if chap2lever == 1:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate 0
                        
                        show handle:
                            
                            linear 1.5 rotate 90

                    if chap2lever == 2:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate 90
                        
                        show handle:
                            
                            linear 1.5 rotate 180


                    if chap2lever == 3:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate 180
                        
                        show handle:
                            
                            linear 1.5 rotate 270


                    if chap2lever == 4:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate 270
                        
                        show handle:
                            
                            linear 1.5 rotate 360
                    
                    play sound "fx/lever_turn.ogg"

                    $ renpy.pause (1.0)

                    $ chap2lever += 1
                    
                    label chap2leverresult:
                    
                    if chap2lever == 0:
                        
                        c "(The arrow on the lever is now pointing left.)"

                        jump chap2hatch
                        
                    elif chap2lever == 1:

                        c "(The arrow on the lever is now pointing up.)" 

                        jump chap2hatch
                        
                    elif chap2lever == 2:

                        c "(The arrow on the lever is now pointing right.)"

                        jump chap2hatch
                        
                    elif chap2lever == 3:

                        c "(The arrow on the lever is now pointing down.)"

                        jump chap2hatch
                        
                    elif chap2lever == 4:
                        
                        $ chap2lever = 0

                        c "(The arrow on the lever is pointing left.)"

                        jump chap2hatch
                        
                    else: #-1
                        
                        $ chap2lever = 3

                        c "(The arrow on the lever is pointing down.)"

                        jump chap2hatch

                "Turn the lever counter-clockwise.":

                    #show handle at Position (xpos = 983, ypos = 650)

                    $ renpy.pause (0.5)

                    if chap2lever == 0:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate -90
                        
                        show handle:
                            
                            linear 1.5 rotate -180
                    
                    if chap2lever == 1:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate 0
                        
                        show handle:
                            
                            linear 1.5 rotate -90

                    if chap2lever == 2:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate 90
                        
                        show handle:
                            
                            linear 1.5 rotate 0


                    if chap2lever == 3:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate 180
                        
                        show handle:
                            
                            linear 1.5 rotate 90


                    if chap2lever == 4:

                        show handle:
                            xpos 983 
                            ypos 680
                            rotate -90
                        
                        show handle:
                            
                            linear 1.5 rotate -180
                    
                    play sound "fx/lever_turn.ogg"

                    $ renpy.pause (1.0)

                    $ chap2lever -= 1
                    
                    jump chap2leverresult

                    
                "Give up.":

                    hide open
                    hide closed
                    hide button1
                    hide button2
                    hide handle
                    with fade
                    
                    jump chap2park2choice
            
        "Examine the fallen leaves.":
            
            c "(I don't recognize this species of tree.)" 

            jump chap2park2choice
            
        "Go back.":
            
            scene town2 at Pan ((300, 400), (150, 400), 3.0) with dissolveslow
            
            jump chap2park1choice
            
            
    
label chap2park3:
    
    scene park3 at Pan ((100, 0), (100, 0), 0.0) with fade
    
    $ renpy.pause (0.5)

    m "Just as I entered the southern part of the park, I found myself tumbling to the ground when someone suddenly bumped into me."

    play sound "fx/impact3.ogg"
    
    c "Ouch!" with vpunch
    
    show lucius normal with dissolve

    Lu "Sorry about that. Are you alright?"

    c "Besides being a little dirtier than before, I think so."

    Lu "I should really look where I'm going. Sometimes, I just get lost in my thoughts."

    play sound "fx/book.ogg"

    c "Hey, I think you dropped this."

    Lu "Oh, thank you."

    c "Ghost stories, huh?"

    Lu "Yep! Oh, I should probably go before the bookstore closes. Bye!"
    
    $ renpy.pause (0.2)
    
    show lucius normal flip
    
    $ renpy.pause (0.3)
    
    hide lucius with easeoutright

    $ renpy.pause (0.3)

    c "Bye."
    
    $ renpy.pause (0.5)
        
    c "(There's someone sitting on the benches.)"
    
    label chap2park3choice:
    
    menu:
        
        "Approach the dragon." if chap2emmeet:

            $ chap2park3unvisited = False
            $ chap2emmeet2 = True
            $ emeramet = True

            scene black with dissolve
            $ renpy.pause (0.3)
            show cgemera at Pan((0, 0), (0, 302), 7.0) with dissolvemed
            $ renpy.pause(5.0)
            
            scene park3 at Pan ((100, 0), (100, 0), 0.0)
            show emera normal
            
            with fade
            
            if persistent.remy1played == True:
                
                Em "What a most pleasant surprise to be meeting you here, [player_name]." 
                
                Em ques "Do you know who I am?"
                
                menu:
                    
                    "I have no idea.":
                        
                        c "I'm afraid I don't."

                        Em mean "Then let me fill that gap in your knowledge. My name is Emera and I am the Minister of Culture and Arts."

                        c "I see."
                        
                    "I do.":
                        
                        $ renpy.pause (0.5)
                
            else:
                
                "???" "What a most pleasant surprise to be meeting you here, [player_name]." 
                
                show emera ques with dissolve
                
                "???" "Do you know who I am?"

                c "I'm afraid I don't."

                show emera mean with dissolve

                "???" "Then let me fill that gap in your knowledge. My name is Emera and I am the Minister of Culture and Arts."

                c "I see."
                                
            Em normal "And what brings you here today, [player_name]?"

            c "I'm not quite sure of that myself."

            Em mean "Ah, the park does have an appeal that naturally draws people in. I would know, since I'm partly responsible for creating it. Have you seen the north side yet? If not, you totally should. It's just so pretty this time of year."

            c "You created this park?"

            Em normal "Well, some of it." 
            
            Em "Do you see the building behind me? That's where I work."

            Em mean "Do you want to know a secret? The park was built here so I could enjoy going outside on my breaks - like right now, for example."
                
            if persistent.remy1played == True:
                
                c "Speaking of your work: Remy works for you, right? I just met him the other day."

                Em "Oh, Remy? Quite the little nerd, isn't he?"
                
                Em "Have you seen his malformed ears? I want to laugh every single time I see him."

                menu: 
                
                    "I haven't noticed.":
                        
                        #$ renpy.pause (0.5)

                        Em "Oh, then you're missing out on some quality entertainment. You have to look at them next time you see him."

                        show emera normal with dissolve

                    "I have to admit, they are pretty funny.":

                        Em "Right? Now just imagine what it must be like working with him. He's always running back and forth on my command, like some sort of well-trained, ugly, yappy dog."
                        
                        $ emeramood += 1

                        $ evilpoints += 1

                        show emera normal with dissolve

                    "That's not very nice.": 

                        $ renpy.pause (0.5)

                        Em ques "Be that as it may, I just can't help it."

                        $ emeramood -= 1
                        
                        show emera normal with dissolve
        
            else:
                
                pass
                
            c "Can I ask you a question?"

            Em ques "You can ask, for sure, but whether I can answer or not is another question."

            Em normal "What would you like to know?"
            
            label chap2emselection:
            
            menu:
                
                "Ask about your visit." if chap2emvisit:

                    c "What do you think about us visiting this world?"

                    Em ques "You and Reza?"

                    Em normal "Well, I think it is about the most exciting thing that has happened here in the last few years."

                    Em mean "It certainly has been a nice distraction from the other boring things I have to do at work."

                    c "How so?"

                    Em ques "Arranging your arrival was partly my responsibility. In fact, I would have been at the portal to welcome you myself if something didn't come up at the last second."
                                        
                    $ chap2emvisit = False
                    
                    show emera normal with dissolve
                    
                    jump chap2emselection
                    
                "Ask about her job." if chap2emjob:
                    
                    c "Can you tell me more about your job?"

                    Em ques "I could, but I think overall it's a very boring affair."

                    Em frown "It involves a lot of reading, and talking, and approving or rejecting forms and projects."

                    Em normal "It has its perks, but in some ways I'll certainly be happy when my term is over."

                    Em ques "If you've been minister once, that's something people will remember you for - even if those times are long past. No one can ever take that away from you again."

                    c "You mentioned your \"term\" ending. How does that work here?"

                    Em normal "We, the ministers, serve our term, and then someone else takes our place. Only one minister changes at a time, though."
                    
                    Em "Technically speaking, any person can become a minister, though there are certain standards and requirements that must be met in order to apply for office."

                    Em frown "I don't want to bore you with the details, as that too would be a long and tedious affair."
                    
                    show emera normal with dissolve
                    
                    $ chap2emjob = False

                    jump chap2emselection

                "Ask about Tatsu Park." if chap2empark:
                    
                    c "Can you tell me more about Tatsu Park?"

                    Em ques "Well, I'm not so sure there is that much to say about it."

                    Em normal "It just opened recently. I think the initial request was for more open spaces, like a dedicated place for people to gather and such."

                    Em ques "If you read the plaque, you would know that the park was dedicated to our so-called \"creator\". I say \"creator\" like that because I think that word is a bit of a misnomer, but I suppose people still use it regardless."

                    show emera normal with dissolve
                    
                    $ chap2empark = False
                    
                    jump chap2emselection
                    
                "That's all.":
                    
                    $ renpy.pause (0.5)
                    
                    $ chap2emmeet = False
                    
                    Em ques "I suppose I should be getting back to work anyway."

                    Em mean "Well, thank you for this most pleasant conversation, [player_name]."

            if emeramood >= 0:
                
                Em "You know, if you wanted to continue talking at a later time, you should have no difficulty contacting me."

                c "I'll keep that in mind."

                if persistent.remygoodending == True:
                    
                    $ emeraavailable = True
                    
                elif persistent.remybadending == True:

                    $ emeraavailable = True
                    
                else:
                    
                    pass
                
                hide emera with dissolve
                
                jump chap2park3choice
                
            else:
                
                hide emera with dissolve
                
                jump chap2park3choice
                
        "Go back.":
            
            scene town2 at Pan ((300, 400), (150, 400), 3.0) with dissolveslow
            
            jump chap2park1choice

        
label chap2cont:

#skippy here


    
m "The afternoon sun hung low in the sky, and I decided it was time to report my findings to the police. A brief call to the department, and I was on my way to an appointment with Sebastian."

    
label chap2cont2:
    
if persistent.c2skip == True:

    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_57

    call skiptut from _call_skiptut_12
        
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
            
            $ c2mav = "understand"
            
            scene black with dissolvemed

            $ renpy.pause (1.0)
            
            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_12

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow
            
            $ renpy.pause (1.0)

            nvl clear

            show sebastian normal b with dissolve

            play music "mx/barren.ogg" fadein 1.0
            
            jump chap2skip3
            
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/elegant.ogg" fadein 1.0

c "(I'm not sure how my findings will help, but at least I have something.)"

stop music fadeout 1.0

"???" "Look who we have here."

play music "mx/mysteryambience.ogg"

show maverick normal with dissolve

m "I turned around to see Maverick. His intense gaze confirmed that there was no one else his words could have been directed at. Even with the civilians passing by in the background, I suddenly felt very alone."

c "What do you want from me?"

Mv "Answers."

menu:
    
    "What if I don't have any for you?":
        
        Mv angry "Then you will listen."

        $ evilpoints += 1
        
        show maverick normal with dissolve
        
    "Okay. Then start talking.":
        
        pass
        
Mv "Just tell me one thing: Why?"

Mv "What is your goal in all of this?"

Mv "Why even come here?"
        
menu:

    "You know why. We came as ambassadors for humanity and to oversee the trade we agreed on.":
        
        Mv "No, no, no. That won't do."

        Mv "That's simply not true. You know it, and I know it. I just don't get why you can't be honest with me, even when you know no one else is listening."
        
        $ c2mav = "ambassador"
        
    "You wouldn't understand.":
        
        Mv "What would I not understand?"

        Mv "I just don't get why you can't be honest with me, even when you know no one else is listening."
        
        $ c2mav = "understand"

Mv "You know I can't touch you. If I did, it would be over for me. At least, as long as I don't have any proof."

Mv "In the end, what difference does it make if I know? No one is going to believe me, anyway."

Mv "Do you wish to kill me, too? Like Reza?"

menu:
    
    "[[Say nothing.]":
        
        $ renpy.pause (0.5)
         
        Mv angry "Tell me, why would an ambassador need such a dangerous tool in the first place?"
        
        show maverick normal with dissolve
        
    "I would never do such a thing.":
        
        Mv "Is that so?"

        Mv angry "Tell me, why would an ambassador need such a dangerous tool in the first place?"
        
        show maverick normal with dissolve
        
    "If I have to." if persistent.neutralending:
        
        Mv "I appreciate the honesty."

        Mv angry "Of course, why else would an ambassador need such a dangerous tool?"
        
        $ evilpoints += 3
        
        show maverick normal with dissolve
         

Mv "I know you claimed not to have one of these things Reza injured me with, and you didn't have any when they searched you, but I guess it's way too late for safety precautions at this point. You could have hidden one anywhere."

Mv "That damn hurt, you know." 

Mv "But even worse than that was getting thrown aside by Bryce."

Mv "I trust him, but after what happened, he doesn't trust me anymore."

Mv "Now, there's only you. The mythical, the special, the new."

Mv "How much I wish I could make him see what I see."

Mv "I could've saved the world with what I did that day and it still wouldn't matter when no one believes me. Just because I don't have any proof."

Mv angry "But I won't stop until I find some."

Mv normal "And when I do, I'm gonna be a damn hero." 

hide maverick with dissolve

stop music fadeout 2.0

nvl clear

$ renpy.pause (1.0)

window show

n "And with that, he was gone."

n "On the way to the police station, Maverick's words kept finding their way back into my mind. I couldn't decide how to feel about them."

n "I wasn't even sure if it was worth mentioning to the police, since all he did was make vague accusations. It wasn't anything substantial enough to be considered a threat."

n "However, his actions were growing more calculated, and he seemed very sure of himself. I wondered about what this could amount to..."

n "But that wasn't the problem at hand."

window hide

scene black with dissolveslow

$ renpy.pause (1.0)

scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow

$ renpy.pause (1.0)

nvl clear

show sebastian normal b with dissolve

play music "mx/barren.ogg" fadein 1.0

Sb "Hey, [player_name]!"

c "Hey, Sebastian! I thought I'd meet you at the front desk. What are we doing in Bryce's office?"

Sb smile b "He does have a nice office, doesn't he? And the chairs are comfy."

c "Is that the only reason we're in here?"

m "The dragon gave a brief chuckle."

Sb "Let's just say that any information pertaining to this case is important enough to warrant some privacy."

c "I see."

c "Will Bryce be here anytime soon?"

Sb normal b "I don't think so. He's still outside, looking for Reza. He's not the kind of person who gives up easily."

menu:
    
    "That sounds like him.":
        
        Sb "That's Bryce for you. Once he sets his mind on something, he sees it through to the end."

        Sb "That's why he's our chief. He gets things done."

    "He should've given up hours ago.":

        Sb "That's just how he is. Once he sets his mind on something, he sees it through to the end."

        Sb "That's why he's our chief. He gets things done."

        $ evilpoints += 1
        
    "Can't we help?":

        Sb "There's only so much we can do. I was out searching too until I came to meet you."


Sb "At this rate, it doesn't look like we'll find him today."

Sb "He could be anywhere. Long gone, beyond our reach. What do you think?"

menu:
    
    "To be honest, I don't know.":

        c "To be honest, I don't know."

        c "I have no idea what he's doing, or what his plan is, really."

    "I don't think he's going anywhere.":

        c "I don't think he's going anywhere."

        c "He can't flee to another place. No matter where he goes, he'd be recognized immediately."

        c "In the end, his only way out is the same way he got in: The portal."

        c "And he can't use that without someone noticing."

        Sb smile b "Very astute observation."
        
        show sebastian normal b with dissolve

    "We'll never find him.":

        Sb "What makes you think so?"

        c "He's escaped twice now. Each time, he managed to get away without any trouble. I just feel like if we haven't found him by now, we won't do so anytime soon, either. Reza knows what he's doing."

        Sb "I wouldn't give up just yet."

        c "I don't think you quite understand what you're dealing with."

        Sb "But you do. That's why we asked for your help."

        c "I know, but to be honest, I'm not sure if I can be much help to you at all."

        Sb "You just have to keep trying." 
        
        Sb "At least, that's what they told me in the police academy."

        Sb "In our line of work, there can be a lot of situations that seem hopeless, but the one thing you can't do is to just give up."

        Sb "You can go over the same facts and evidence dozens of times and still miss something. Focus and keep trying, and you'll eventually find something new."

        Sb "Even if you're sure there's nothing else to be found, or you feel like it's not worth it, or you just think it's hopeless, there's always something you can do to help."

        Sb "As long as you don't give up, there's still a chance to solve the case - however small it may be."

        Sb "And you know, maybe it's that small chance that makes the difference in the end."

        Sb "Don't give up, [player_name], because quite frankly, you're the best chance we have."
        
c "I wonder what will happen to our trade agreement now, considering Reza's still missing, the murders, and the stolen generator."

c "If Reza really is the murderer, then..."

Sb "Don't do that."

c "What?"

Sb "Worry."

c "You don't know what's at stake here."

Sb "People are dead, [player_name]. Do you think I don't know that?"

Sb "Reza may be our prime suspect, but he's also a missing person. For all we know, he could be a victim. Maybe someone is making him do this."

Sb "My point is, we don't know the facts yet. What we need to do is find him and find the murderer."

Sb "We'll find Reza and go from there. We'll figure it out."

menu:
    
    "[[Say nothing.]":

        $ evilpoints += 1
        
        
    "Thanks, Sebastian.":
        
        pass

label chap2skip3:

Sb "Anyway, you said you had some information for us. So, what did you find?"

show black with dissolve

$ renpy.pause (1.0)

hide black with dissolvemed

if chap2bandageuntaken == False:
    
    Sb "The bandage you found is something, alright. Of course, it could be anyone's, but why would someone discard theirs in a place like that? It seems suspicious to me, and is certainly worth checking out."

    Sb "I'll make sure it gets to the right place."
    
else:
    
    pass
    
if chap2receiptsuntaken == False:
    
    Sb "The receipts you got are interesting. There might be something more to them, or they could just be a useless record of his eating habits. You never know what you might find out about a person, their habits, or their plans this way."
    
    
else:
    
    pass

if chap2facreza == False:
    
    Sb "I'm not sure if there's anything special about Anna wanting Reza's blood. I mean, she's a scientist, so it's natural that she'd be interested in something like that."

    Sb "We'll have to talk to her about it, though. Maybe she has some more details for us."
    
else:
    
    pass

if chap2libreza == False:
    
    Sb "The map in the library... I don't know what to think about that." 
    
    Sb "He could've needed a map to plan something, I suppose, but who knows what he really wanted to do with it. It's the kind of detail that - on its own - might not tell us much, but could be crucial later on."
    
else:
    
    pass

if chap2clues == 2:
    
    Sb smile b "Well done, [player_name]. That gives us some solid points from which we can continue our investigation."

    if persistent.c2investigation == False:

        $ persistent.c2investigation = True
        
        $ achievement.grant("Investigator 2")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_58
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You did well on the second investigation!"
            
        elif system == "advanced":

            s "You did well on the second investigation. My compliments to you."
            
        else:
            
            s "You did well on the second investigation. If it was Zhong, would that make him an investi-gator?"

    show sebastian normal b with dissolve
    
    $ chap2inv2 = 3
    
elif chap2clues == 1:
    
    Sb smile b "Good work, [player_name]. It's not much to go on, but it's something. It'll keep us busy, at least."
    
    show sebastian normal b with dissolve
    
    $ chap2inv2 = 2
    
else:
    
    Sb "There isn't much information to glean from what you told me. The rest of the police force and I will have to check things out ourselves to see if we can find more details."

    $ chap2inv2 = 1

if inv == "high":
    
    $ chap1inv = 5
    
elif inv == "med" :
    
    $ chap1inv = 3
    
else:
    
    $ chap1inv = 1
    


Sb "In any case, thanks for your help. We really do appreciate it."

c "You're welcome."

Sb "That should be all, then. Since Bryce still hasn't come back, I assume the search is still going on, and I better get out there and help him. Guess it's going to be a long day."

Sb "Can you find your way back to your apartment?"

c "Of course."

Sb "Alright. I'll see you later."

c "Good luck."

scene black with dissolve
$ renpy.pause (1.0)

scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

label chap2skip2:

c "(Finally, some free time. Whatever am I going to do?)"

$ popularnumber = 0

$ chap2inv1 = 0

if chap2inv > 5 :
    
    $ chap2inv1 = 2
    
elif chap2inv > 2 :
    
    $ chap2inv1 = 1
    
else:
    
    $ chap2inv1 = 0

$ chap2invt += chap2inv1
$ chap2invt += chap2inv2

if inv == "high":
    $ totalinv = 5
    
elif inv == "med":
    $ totalinv = 3
    
else:
    $ totalinv = 1

$ totalinv += chap2invt
#now we have a total inv value based on the first two chapter that can be between 2 and 10

#if chap2invt >= 4:
#    $ persistent.c2skip = True

$ persistent.c2skip = True

$ chapter2csplayed = 0
$ chapter2unplayed = False

label chapter2chars:

$ save_name = "Chapter 2"

if zhongunplayed == False:
    
    $ zhongavailable = False
    $ zhongnameavailable = False

if emeraunplayed == False:
    
    $ emeraavailable = False

if chapter2csplayed == 1:
        
    scene black with dissolveslow
    $ renpy.pause (1.0)
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

elif chapter2csplayed == 0:
    
    pass
    
else:
    
    jump chapter3

$ playmessage = False

if remystatus == "good":
    
    if remy3unplayed == False:
        
        if remy3unheard == True:
            
            pass
            
        else:
            
            pass
        
    elif remy2unplayed == False:

        if remy2unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            pass
            
        else:
            
            pass
        
    else:

        if remy1unheard == True:
    
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            $ playmessage = True

        else:
            
            pass
        

if brycestatus == "good":
    
    if bryce3unplayed == False:
        
        if bryce3unheard == True:
            
            pass
            
        else:
            
            pass
        
    elif bryce2unplayed == False:

        if bryce2unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            pass
            
        else:
            
            pass
        
    else:

        if bryce1unheard == True:
    
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            $ playmessage = True

        else:
            
            pass


if adinestatus == "good":
    
    if adine3unplayed == False:
        
        if adine3unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            
            pass
            
        else:
            
            pass
        
    elif adine2unplayed == False:

        if adine2unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            pass
            
        else:
            
            pass
        
    else:

        if adine1unheard == True:
    
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            $ playmessage = True

        else:
            
            pass

if annastatus == "good":
    
    if anna3unplayed == False:
        
        if anna3unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            pass
            
        else:
            
            pass
        
    elif anna2unplayed == False:

        if anna2unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            pass
            
        else:
            
            pass
        
    else:

        if anna1unheard == True:
    
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            $ playmessage = True


        else:
            
            pass

if loremstatus == "good":
    
    if lorem3unplayed == False:
        
        if lorem3unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            
            pass
            
        else:
            
            pass
        
    elif lorem2unplayed == False:

        if lorem2unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            pass
            
        else:
            
            pass
        
    else:

        if lorem1unheard == True:
    
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            $ playmessage = True


        else:
            
            pass

else:
    
    pass
    
if playmessage == True:
    
    c "(Looks like there are some messages on the answering machine. Let's see...)"
    
else:
    pass

if remystatus == "good":

    if remy3unplayed == False:
        
        if remy3unheard == True:
            
            #answeringmachine
            
            pass
            
        else:
            
            pass
            
    elif remy2unplayed == False:
        
        pass

    else:
        
        if remy1unheard == True:
            
            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)

            Ry "Hello, this is Remy speaking. I'm calling in regard to the dinner we talked about. I'll have an opening soon and was wondering if you also had the time."

            Ry "Let me know if you are interested."

            Ry "Have a good day."

            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)

            c "(I guess that's my official invitation. Now the question is if I want to go or not.)"

            $ remy1unheard = False
            
            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_10
            
        else:
            
            pass
else:
    
    pass
            

if brycestatus == "good":

    if bryce3unplayed == False:
        
        if bryce3unheard == True:
            
            #answeringmachine
            
            pass
            
        else:
            
            pass
            
    elif bryce2unplayed == False:
        
        pass


    else:
        
        if bryce1unheard == True:
            
            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)

            Br "Hey. I was just thinking about last time. I know we got a little blackout drunk, but I still thought that was kinda fun."

            Br "I think you had some fun too, but I also wanted to show you there's more to me than that."

            Br "So, I was just wondering if you wanted to come over just to hang out and relax, you know."

            Br "We only get to see each other when things are all serious, and I bet it's rough for you with everything that's going on. I figured you might want to get away from that a little."

            Br "Anyway, if you want to drop by at any time - my door's open, buddy."

            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)

            c "(Considering what happened last time, entering the literal dragon's den could either turn out really well, or not so much.)"
            
            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_11
            
            $ bryce1unheard = False
            
        else:
            
            pass
else:
    
    pass
            
if adinestatus == "good":

    if adine3unplayed == False:
        
        if adine3unheard == True:
            
            #answeringmachine
            
            pass
            
        else:
            
            pass
            
    elif adine2unplayed == False:
        
        pass


    else:
        
        if adine1unheard == True:
            
            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)
            
            Ad "Please leave a message after the beep."

            Ad "Gotcha! You thought that was your answering machine, but it was me, Adine!"

            Ad "I know we talked about me coming over again, but I thought, why not mix it up and you come to me instead?"

            Ad "I mean, it's not like I can use your excuse and pretend to order something from you."

            Ad "After all, you don't even have anything to sell or deliver. Unless..."

            Ad "Well, I don't think you're that kind of person."

            Ad "Oh, I do hope this is the right number, or someone is going to be very confused."
            
            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)

            c "(Well, she did get the right number and I'm still confused.)"
            
            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_12
            
            $ adine1unheard = False   
            
            
        else:
            
            pass
else:
    
    pass

if annastatus == "good":

    if anna3unplayed == False:
        
        if anna3unheard == True:
            
            #answeringmachine
            
            pass
            
        else:
            
            pass
            
    elif anna2unplayed == False:
        
        pass


    else:
        
        if anna1unheard == True:
            
            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)
            
            An "I just wanted to update you. I still don't have an open spot in the facility for your tests, but I'll be free if you want to cash in your reward."

            An "You know I'm busy, so this is your chance for your date if you even still want to go through with it. Take it or leave it. I don't care much either way."

            An "In any case, you know where to find me."

            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)

            c "(I guess the choice is mine.)"

            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_13
            
            $ anna1unheard = False
            
            
        else:
            
            pass
else:
    
    pass


if loremstatus == "good":

    if lorem3unplayed == False:
        
        if lorem3unheard == True:
            
            #answeringmachine
            
            pass
            
        else:
            
            pass
            
    elif lorem2unplayed == False:
        
        pass

    else:
        
        if lorem1unheard == True:
            
            play sound "fx/answeringmachine.ogg"

            $ renpy.pause (0.5)
            
            Lo "Hello! I had some time to work through the stuff you told me, and now would be the perfect time to get some pictures of you."

            Lo "If you're not busy with anything else, it would be great if you could come over sometime."

            Lo "So, see you soon? Maybe."

            play sound "fx/answeringmachine.ogg"
            
            $ renpy.pause (0.5)

            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_14
            
            $ lorem1unheard = False
                
            
        else:
            
            pass
else:
    
    pass

$ remyavailable = True
$ bryceavailable = True
$ annaavailable = True
$ loremavailable = True

$ adineavailable = False

if adine1unplayed == False:

    if adinestatus == "bad":
        
        $ adineavailable = False
        
    elif adine2unplayed == False:
        
        $ adineavailable = False
        
    else:
        
        $ adineavailable = True
    
else:
    
    pass
    
if remystatus == "bad":
    
    $ remyavailable = False
    
else:
    
    pass
    
if remy2unplayed == False:
    
    $ remyavailable = False
    
else:
    
    pass

if brycestatus == "bad":
    
    $ bryceavailable = False
    
else:
    
    pass

if bryce2unplayed == False:
    
    $ bryceavailable = False
    
else:
    
    pass

if annastatus == "bad":
    
    $ annaavailable = False
    
else:
    
    pass
    
if anna2unplayed == False:
    
    $ annaavailable = False
    
else:
    
    pass
    
if loremstatus == "bad":
    
    $ loremavailable = False

if lorem2unplayed == False:
    
    $ loremavailable = False
    

if chapter2csplayed == 0:

    if remyavailable == True:
        
        $ chapter2count +=1
        
    if annaavailable == True:
        
        $ chapter2count +=1

    if loremavailable == True:
        
        $ chapter2count +=1
        
    if bryceavailable == True:
        
        $ chapter2count +=1

    if adine1unplayed == True:
        
        $ chapter2count +=1
        
    if adineavailable == True:
        
        $ chapter2count +=1
        
    if zhongavailable == True:
        
        $ chapter2count +=1

    if zhongnameavailable == True:
        
        $ chapter2count +=1

    if emeraavailable == True:
        
        $ chapter2count +=1


    if chapter2count >= 7:
        
        jump chap2altmenua1


    menu:
        
        "Meet with Remy." if remyavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "remy"
            $ chap3picksremy += 3
            
            if remy1unplayed == True:
                
                jump remy1
                
            else:
                
                jump remy2
            
        "Meet with Anna." if annaavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "anna"
            $ chap3picksanna += 3

            if anna1unplayed == True:
                
                jump anna1
                
            else:
                
                jump anna2


        "Meet with Lorem." if loremavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "lorem"
            $ chap3pickslorem += 3

            if lorem1unplayed == True:
                
                jump lorem1
                
            else:
                
                jump lorem2

            
        "Meet with Bryce." if bryceavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "bryce"
            $ chap3picksbryce += 3

            if bryce1unplayed == True:
                
                jump bryce1
                
            else:
                
                jump bryce2
            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "adine"
            $ chap3picksadine += 3

            jump adine1
            
        "Meet with Adine." if adineavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "adine"
            $ chap3picksadine += 3

            jump adine2

        "Meet with the store clerk." if zhongavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "zhong"
            jump zhong
            
        "Meet with Zhong." if zhongnameavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "zhong"
            jump zhong
            
        "Meet with Emera." if emeraavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "emera"
            jump emera
        
                
elif chapter2csplayed == 1:
    
    c "(Nothing going on today. Guess I can do whatever.)"
    
    $ chapter2count = 0

    $ chapter2count += 1

    if remyavailable == True:
        
        $ chapter2count +=1
        
    if annaavailable == True:
        
        $ chapter2count +=1

    if loremavailable == True:
        
        $ chapter2count +=1
        
    if bryceavailable == True:
        
        $ chapter2count +=1

    if adine1unplayed == True:
        
        $ chapter2count +=1
        
    if adineavailable == True:
        
        $ chapter2count +=1
        
    if zhongavailable == True:
        
        $ chapter2count +=1

    if zhongnameavailable == True:
        
        $ chapter2count +=1

    if emeraavailable == True:
        
        $ chapter2count +=1
        
    if chapter2count >= 7:
        
        jump chap2altmenub1
    

    menu:
        
        "Meet with Remy." if remyavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "remy"
            $ chap3picksremy += 2

            if remy1unplayed == True:
                
                jump remy1
                
            else:
                
                jump remy2
            
        "Meet with Anna." if annaavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "anna"
            $ chap3picksanna += 2

            if anna1unplayed == True:
                
                jump anna1
                
            else:
                
                jump anna2


        "Meet with Lorem." if loremavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "lorem"
            $ chap3pickslorem += 2

            if lorem1unplayed == True:
                
                jump lorem1
                
            else:
                
                jump lorem2


            
        "Meet with Bryce." if bryceavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "bryce"
            $ chap3picksbryce += 2

            if bryce1unplayed == True:
                
                jump bryce1
                
            else:
                
                jump bryce2
            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "adine"
            $ chap3picksadine += 2

            jump adine1
            
        "Meet with Adine." if adineavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "adine"
            $ chap3picksadine += 2

            jump adine2

        "Meet with the store clerk." if zhongavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "zhong"
            jump zhong
            
        "Meet with Zhong." if zhongnameavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "zhong"
            jump zhong

        "Meet with Emera." if emeraavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "emera"
            jump emera

        "Spend the day reading.":
                
            m "In the end, I decided to spend the day reading in my apartment. I wasn't really in the mood for anything complex, so I settled for reading the next entry in the \"Sheridan's Adventures\" series." 
            m "By the time I had finished the book, in which the Scepter of Sovereignty from the preceding novel is first stolen, then reclaimed by the novels' titular hero, only to be stolen again in another cliffhanger ending ploy setting up the series' next entry, I wished I had spent the time doing something more productive."
            m "I figured I might still be able to go out or do something else, but when I looked at the time, I regretfully had to realize that the day was already over and it was too late."
            
            $ persistent.lazynumber += 1
            call lazycheck from _call_lazycheck_5
            
            jump chapter3

else:
    jump chapter3




label chap2altmenua1:

    menu:
        
        "Meet with Remy." if remyavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "remy"
            $ chap3picksremy += 3
            
            if remy1unplayed == True:
                
                jump remy1
                
            else:
                
                jump remy2
            
        "Meet with Anna." if annaavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "anna"
            $ chap3picksanna += 3

            if anna1unplayed == True:
                
                jump anna1
                
            else:
                
                jump anna2


        "Meet with Lorem." if loremavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "lorem"
            $ chap3pickslorem += 3

            if lorem1unplayed == True:
                
                jump lorem1
                
            else:
                
                jump lorem2

            
        "Meet with Bryce." if bryceavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "bryce"
            $ chap3picksbryce += 3

            if bryce1unplayed == True:
                
                jump bryce1
                
            else:
                
                jump bryce2
                
        "[[Show more options.]":
            
            jump chap2altmenua2
            

label chap2altmenua2:

    menu:
    
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "adine"
            $ chap3picksadine += 3

            jump adine1
            
        "Meet with Adine." if adineavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "adine"
            $ chap3picksadine += 3

            jump adine2

        "Meet with the store clerk." if zhongavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "zhong"
            jump zhong
            
        "Meet with Zhong." if zhongnameavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "zhong"
            jump zhong
            
        "Meet with Emera." if emeraavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2picka = "emera"
            jump emera


        "[[Show more options.]":
            
            jump chap2altmenua1

label chap2altmenub1:

    menu:
        
        "Meet with Remy." if remyavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "remy"
            $ chap3picksremy += 2

            if remy1unplayed == True:
                
                jump remy1
                
            else:
                
                jump remy2
            
        "Meet with Anna." if annaavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "anna"
            $ chap3picksanna += 2

            if anna1unplayed == True:
                
                jump anna1
                
            else:
                
                jump anna2


        "Meet with Lorem." if loremavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "lorem"
            $ chap3pickslorem += 2

            if lorem1unplayed == True:
                
                jump lorem1
                
            else:
                
                jump lorem2


            
        "Meet with Bryce." if bryceavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "bryce"
            $ chap3picksbryce += 2

            if bryce1unplayed == True:
                
                jump bryce1
                
            else:
                
                jump bryce2
            

        "[[Show more options.]":
            
            jump chap2altmenub2
    
    

label chap2altmenub2:

    menu:
            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "adine"
            $ chap3picksadine += 2

            jump adine1
            
        "Meet with Adine." if adineavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "adine"
            $ chap3picksadine += 2

            jump adine2

        "Meet with the store clerk." if zhongavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "zhong"
            jump zhong
            
        "Meet with Zhong." if zhongnameavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "zhong"
            jump zhong

        "Meet with Emera." if emeraavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ chapter2csplayed += 1
            $ chap2pickb = "emera"
            jump emera

        "Spend the day reading.":
                
            m "In the end, I decided to spend the day reading in my apartment. I wasn't really in the mood for anything complex, so I settled for reading the next entry in the \"Sheridan's Adventures\" series." 
            m "By the time I had finished the book, in which the Scepter of Sovereignty from the preceding novel is first stolen, then reclaimed by the novels' titular hero, only to be stolen again in another cliffhanger ending ploy setting up the series' next entry, I wished I had spent the time doing something more productive."
            m "I figured I might still be able to go out or do something else, but when I looked at the time, I regretfully had to realize that the day was already over and it was too late."
            
            $ persistent.lazynumber += 1
            call lazycheck from _call_lazycheck_6
            
            jump chapter3

        "[[Show more options.]":
            
            jump chap2altmenub1
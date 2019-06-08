label bryce5:
    
show black with dissolvemed
$ renpy.pause (0.5)
scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow

$ save_name = "Chapter 5 - Bryce"

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(That must be him.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

show bryce normal with dissolve

Br smirk "I hope you're ready to see the fireworks, because I brought everything we need."

m "In front of him, there was a woven basket that was closed at the top. It reminded me a lot of a typical picnic basket."

c "What are you talking about?"

Br laugh "Snacks, and other things... You'll see."

if brycestatus == "neutral":
    
    Br normal "I kinda wanted to apologize for last time, so maybe I can make up for that."

    c "Don't mention it."

    Br laugh "I'm glad you're even willing to see me again after what happened."

    c "I'm serious. Let's just forget it and focus on today."

    Br "Alright."
    
else:
    
    pass
    
c "Let's go, then."

scene black with dissolvemed
$ renpy.pause (0.5)
scene viewingspot with dissolvemed

play music "mx/amb/night.ogg" fadein 5.0

m "After a few minutes of walking, we arrived at a rather empty looking area near the edge of town."

c "Where is everyone else? I thought the whole population was watching the fireworks."

show bryce laugh with dissolve

Br "Well, there are more public spaces, but someone like you would get pushed around a lot in the crowds. Besides, I think you'll appreciate the solitude."

c "If you say so."

Br normal "The fireworks should start any minute now."

Br smirk "If you're hungry, you can grab something from the fun basket."

c "Fun basket?"

Br laugh "That's what I call it."

c "I didn't know snacks were that much fun for you."

Br smirk "They certainly can be. Besides, there are other things inside as well."

Br normal "Oh, I think it's starting."

play soundloop "fx/fireworks3.ogg"

m "We waited quietly as the stillness of the night enveloped us. Soon, I heard the sound of the first rocket making its way into the night sky after which it exploded in a pattern of colors."

m "More rockets followed, their thunderous noise echoing throughout the land."

show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow
$ renpy.pause (6)
#hide fireworks with dissolveslow


stop music fadeout 2.0

hide fireworks with dissolveslow

#stop music fadeout 2.0

#hide fireworks with fade

if brycestatus == "good":
    
    Br flirty "You remember what happened last time there were fireworks?"

    c "Is that what the fun basket is for?"

    Br smirk "Actually, no. Not unless you feel adventurous."

    c "We're already outside. That's pretty adventurous, I'd say."

    Br laugh "Suit yourself."

    m "Bryce opened the basket, feeling around in it with one of his claws. Meanwhile, my gaze wandered to the illuminated night sky."
    
else:
    
    pass

m "Suddenly, a terrible realization hit me."

play music "mx/judgement.ogg" fadein 0.5

m "Considering how public of an event this was and how everyone would be watching the fireworks, now would be the best time for Reza to make his move."

m "Not only was the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever have."

m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."

c "Bryce, I think we need to go. Now."

Br smirk "What? Do you want to take this somewhere else?"

c "I know where Reza is."

Br brow "What are you talking about? Are you sure?"

c "I'd bet my life on it."

Br stern "Then we have no time to lose. Let's go."

#copied passage

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow

m "We arrived at the portal just a few minutes later. While I checked out the portal itself, Bryce looked around the area. I was glad to see it was still turned off. Had it been used recently, it would either still be running or in the process of recharging. Reza was still here, somewhere."

#stop music fadeout 2.0

if sebastianunplayed == True:

    show bryce stern with dissolve

    Br "Damn it."

    c "What is it, Bryce?"
    
    m "Hesitating, I drew nearer."

    show sebastiandead at Pan((1080, 608), (300, 150), 10.0) with fade
    
    $ renpy.pause (8.0)
    
    Br "He's dead, but still warm."
    
    hide sebastiandead with fade
    
    Br "That bastard."

    c "Reza hasn't used the portal yet."
    
else:

    show bryce brow with dissolve
    
    Br "Just look at this."

    c "What is it?"

    play sound "fx/suitcase.ogg"

    Br stern "Eggs, a suitcase full of them."

    c "So he broke into the hatchery again."

    Br "Looks like it."
    
    c "He hasn't used the portal yet, though."
    

Br brow "How could he? Isn't it broken?"

c "Not anymore. Looks like someone repaired it."

Br stern "Then he must be close, but where is he? What is so important that he won't leave without it?"

c "The underground building."

m "The Administrator had told me all about the prowess of the generators within. It probably hadn't been hard for Reza to guess the same, or to try stealing it from a place he knew would be even more deserted than the rest of the village was right now."

Br "That must be it."

c "So, what do we do now?"

Br brow "We could wait for him here, but I think I've got an even better plan."

c "What is it?"

Br stern "Let's just do it like last time. You go in first, and I'll stay behind and out of sight. If you meet him, you can confront him and maybe talk him down, but if he tries to flee, he'll still have to get through me first."

c "Alright. Let's go."

hide bryce with dissolve

m "Bryce led me to the dig site where they had unearthed the building's entry. Once we got nearer, he stayed behind and motioned for me to go forward."

m "He slowly followed me, trying to stay in cover as I entered the building."

stop soundloop fadeout 3.0

stop music fadeout 2.0

scene black with dissolvemed

$ renpy.pause (0.5)

scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed

m "Inside, I was met with a long, illuminated hallway that was lined with doors on both sides."

#call secondary function here

call sincethelightswerealreadyon from _call_sincethelightswerealreadyon

if brycegoodending == True:
    
    jump mainmenu

Br "Maybe I can."

play music "mx/fervor.ogg" fadein 0.5

m "Suddenly, Bryce was standing next to me."

show reza at Position (xpos= 0.9) with ease

show bryce stern flip at left with easeinleft

Rz angry "Now you're showing your true colors, [player_name]."

c "No, Reza. You did. I was willing to talk this out."

Rz annoyed "Alright. Game's over."

play sound "fx/rev.ogg"

show reza gunself with dissolve

show reza gunpoint with dissolve

m "He pulled out his gun, not sure which one of us he should be aiming at."

Rz "The six bullets I have in here should be more than enough for you two."

Br "I wouldn't be so sure of that."

c "Do you think you can really do that, Reza? Do you think this is worth risking your life for?"

Rz angry "I've been risking my life for this every day for the last two weeks. What did you do during that time, sip champagne in your nice apartment?"

Rz "Besides, this generator and the whole building came from our time."

show izumi normal behind reza at Position(xpos=1.25, xanchor='center')

Rz "They belong to humanity!" with Shake((0, 0, 0, 0), 2, dist=10)

show reza at Position(xpos=0.45, xanchor='center')
show bryce at Position(xpos=-0.3, xanchor='center')
with ease

m "Suddenly, the Administrator came out of the shadows in the hallway behind Reza."

show izumi normal at right with ease

As "No, they belong to me."

play sound "fx/rev.ogg"

show reza angry flip

m "Confused, Reza spun around, aiming his gun at the newcomer who was slowly walking towards him."

Rz "Who the fuck are you? Freeze! I said freeze!"

show izumi at Position(xpos=0.8, xanchor='center') with ease

As "Want to waste your bullets on me? Feel free. You can't stop all of us."

play sound "fx/rev.ogg"

Rz gunpoint flip "If you say so."

play sound "fx/gunshot2.wav"

$ renpy.pause (0.5)

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/impact3.ogg"

hide izumi with easeoutbottom

m "He pulled the trigger, and the Administrator fell to the ground with a dull thud that knocked her mask off."

$ persistent.izumiseen = True

show izumiinjured3 at Pan((300, 0), (600, 608), 7.0) with fade

$ renpy.pause (5.0)

hide izumiinjured3 
show bryce at Position (xpos = 0.0)
show reza at Position (xpos = 0.9)
with fade

m "My first instinct was to run away, but as Bryce started charging, so did I."

show reza gunpoint

play sound "fx/gunshots5.ogg"

show bryce at Position (xpos = 0.2)  with ease
$ renpy.pause (0.2)
show bryce at Position (xpos = 0.4)  with ease
$ renpy.pause (0.5)
hide bryce with easeoutbottom

m "Reza aimed at Bryce. It took four shots before he stumbled and fell. Then, Reza aimed at me."

play sound "fx/rev.ogg"

show reza gunself with dissolve

play sound2 "fx/boxdive.ogg"

m "I quickly dove behind the box with the generator for cover, just as Reza pulled the trigger multiple times."

play sound "fx/gunshot2.wav"

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger2.ogg"
#queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger2.ogg"
#queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger1.ogg"

$ renpy.pause (1.0)

play soundloop "fx/hiss.ogg" fadein 1.0

m "Only a single shot came out and lodged itself in the box. Though I was seemingly unharmed, a loud hiss began to emanate from my cover."

Br "Run, [player_name]! It's going to explode!"

show reza angry with dissolve

hide reza with easeoutleft

m "Immediately, Reza and I ran towards the exit." 

play sound "fx/impact3.ogg"

#$ renpy.pause (0.3)

m "Gaining speed, he pushed me and I fell to the ground as he ran outside." with vpunch

m "As I got up again, I saw Bryce still lying in the same spot."

c "What about you?"

#show bryce sad with dissolve

Br "I can't move. Just go. It'll be any second now."

m "I ran as fast as I could. As I was about to reach the outside, I looked back over my shoulder just in time to see Bryce throwing himself on the box before it exploded."

stop music fadeout 1.0

scene np2y at Pan ((0, 100), (0, 100), 0.0) with fade

#explosion

play sound "fx/explosion.ogg"

$ brycedead = True

play soundloop "fx/fireworks.ogg" fadein 10

m "There was a rain of small debris as I heard the walls of the building shaking in their foundation." with Shake((0, 0, 0, 0), 3.0, dist=30)

show reza annoyed at Position (xpos = 0.9) with dissolve

show maverick angry flip at Position(xpos=0.2, xanchor='center') with dissolve

queue sound "fx/reload.ogg"

m "As I made my way to the portal, I saw Reza fumbling with his gun as Maverick pounced on him."

play sound "fx/rev.ogg"

show reza gunpoint with dissolve

show maverick at Position(xpos=0.65, xanchor='center') with move6

play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top") 
show reza at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top") 
with move9

#show maverick at Position(xpos=0.6, xanchor='center') with move6
#hide reza
#hide maverick
#with dissolve

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/bite.ogg"

m "He bit into Reza's neck and strained for a second before ripping a large chunk out of it."

m "Reza wasn't moving when Maverick walked off and came towards me."

show maverick at Position (xpos=0.5, xanchor='center', ypos=1.0, yanchor="top") 
show maverick normal c at center with dissolve

Mv "Where is Bryce?"

c "He was inside. Threw himself on the generator before it exploded."

m "His face contorted into an expression of pain and anger I hadn't seen before."

Mv angry c "I greatly admired him, you know."

Mv "I knew I couldn't trust you lot when you came here."

Mv "His blood is on your hands, because he got involved in your matters, your pointless struggles."

Mv "You never were on our side. It was your fight that you brought here, that he... all of us got involved in. Our world your battlefield, our people the casualties."

Mv "And you still pretend that you were just trying to help us?"

c "It was Bryce himself who asked me for help. He would have wanted to..."

show maverick rage c with dissolve

Mv "Don't tell me what he would have wanted. He is the only reason you are still breathing." with Shake((0, 0, 0, 0), 3.0, dist=30)

Mv angry c "The portal is over here. I'm giving you this one chance to leave. If you refuse, I will kill you."

c "Alright."

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r at Pan((500, 150), (500, 150), 6.0) with dissolvemed

m "He accompanied me to the portal, never leaving my side."

m "When we arrived, I remembered there was something they needed to know before I left."

c "Wait... The comet. You need to listen."

play sound "fx/hit1.ogg"

#play sound2 "fx/silence.ogg"
play sound2 "fx/leather.ogg"

m "Suddenly, one of his claws wrapped around my neck and tightened its grip until it was cutting off my airways."

show maverick angry c with dissolve

Mv "I said you had one chance. One more word, human, and you're dead."

show maverick rage c with dissolve

Mv "Do you hear me?" with Shake((0, 0, 0, 0), 2, dist=10)

show maverick normal c with dissolve

m "He let me go and shoved me towards the portal's controls. As I tried to figure out its interface, only one set of coordinates presented themselves to me, which I confirmed."

m "Wordlessly, I took my place in the middle of the portal."

scene black with dissolveslow

stop music fadeout 2.0

stop soundloop fadeout 2.0

$ renpy.pause (2.0)

nvl clear

window show

n "Maverick's gaze never left me as the portal did its startup routine and I thought about what would happen now."

n "I was going to be the one who would have to tell humanity what happened, that Reza was dead and I escaped with nothing but my own life."

n "I was sure the welcome I was to receive would not be a warm one. This mission had been a last ditch effort on humanity's part to save our slowly dying city."

n "For all my efforts, not only had I gained nothing, but I also lost the PDAs I had given to the dragons."

window hide
nvl clear
window show

n "Considering our city's failure, I could only guess that whatever other cities remained had limited time as well. At this rate, humanity was doomed."

n "On the other hand, all of those who knew about the danger of the comet in the dragon's world were either gone or dead. Maverick would no doubt tell his own side of the story of how he stopped both Reza and I, who he held accountable for the deaths that had occured."

n "Maybe he would be hailed as a hero for having stopped Reza, only to be proven wrong when a few weeks later, the comet would strike."

$ _game_menu_screen = None

window hide 

$ renpy.pause (2.0)

$ renpy.block_rollback()

play sound "mx/clocks.ogg"

#$ renpy.pause (2.0)

#2,1 rezadeadexplosion
#explosion 4,3
#6,5 sun
#meeting otomo, 8, 7
#10, 9 portal left
#logo at the end
#at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='bottom')
show izumiinjured3 at Pan((-450, 400), (400, 508), 25.0)
show credits1 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show explosion at Position(xpos=0.25, xanchor='center')
show credits3 at right 
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show bryceback at Pan((50, 900), (-600, 208), 25.0)
show credits5 at left 
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed
#stop movie

#

show pad at Pan((750, 360), (250, 360), 25.0)
show credits7 at right 
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

#

show cgcombat at Pan((-450, 302), (-450, 0), 25.0)
show credits9 at left 
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

stop music fadeout 4.0

stop sound fadeout 2.0

$ renpy.pause (2.0)

play sound "fx/telstart.ogg"

$ renpy.pause (7.0)

scene np1r at Pan((500, 150), (500, 150), 6.0) with dissolveslow

$ renpy.pause (0.5)

show izumi normal with dissolve

play music "mx/amb/night.ogg" fadein 5.0

$ renpy.pause (0.5)

As "Welcome back." #I entered those coordinates for you so you could return to this moment in case anything went wrong."

#As "Apparently, it did, but don't worry, we'll just try again."

As "If you haven't realized it yet, this is the day of your arrival in this world."

c "Who are you? I... can't remember anything..."

As "It's fine if you don't. Actually, this may be better for both of us." 

As "I don't even know if we've met before, or if this is just the effect of the teleportation." 

As "Either way, it doesn't matter."

As "Come on, Remy will pick you up soon, and there's something else we need to take care of first."

stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolveslow

$ renpy.pause (4.0)

$ persistent.lastendingseen = "bad"

$ persistent.endingsseen += 1

call izumimask from _call_izumimask_5

if persistent.brycebadending == False:

    $ persistent.brycebadending = True
    
    $ achievement.grant("Catastrophy")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_87

    $ mp.brycebadending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Bryce's bad ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "bryce"
    
    jump tut
    
else:

    jump mainmenu


label brycegoodending:
    
Rz "There you are, [player_name]. You don't know how glad I am to see you.  I've wanted to talk with you for so long. I even tried to contact you, but that didn't work with one of them on your tail the whole time."

Rz "But talking can wait. Now that you're here, we've got everything. Come on, help me with this and let's get out of here."

#removed

#call no function here

call no from _call_no

Rz annoyed "What are you talking about? I didn't kill anyone."

c "Don't lie to me. You did it! I remember it now."

Rz "What do you mean? That doesn't make any sense."

c "Are you telling me you weren't the one who stole the generators and those other things these past two weeks?"

Rz normal "No, I was in hiding. After what happened at the portal, I didn't dare to do anything that could jeopardize our mission."

c "Why didn't you just come back?"

Rz annoyed "How could I? They wanted to arrest me. I was a fugitive." 

Rz normal "I was surprised they didn't apprehend you, but then you weren't the one who shot at one of their police officers."

c "Come on, Reza. The murders only started happening after you were gone, and the police have gathered plenty of evidence. You're the only one with a motive."

Rz annoyed "All I did this whole time was try to find ways to contact you so you could talk to our people and figure something out for me. Why would I escalate the situation like that?"

Rz "Besides, how did you know so much about what the police were doing?"

c "I've been helping them, because you were going about this the wrong way."

Rz angry "I didn't kill anyone, I'm telling you!"

c "They have proof, Reza. I've seen it myself. Just turn yourself in and we'll go from there. Nobody can help you if you don't do that."

Rz annoyed "No, I'm not going to turn myself in for something I didn't do. Not for these... beasts. Who knows what they'll do to someone like me in captivity?"

c "How else do you expect this to end?"

Rz normal "I'm not doing anything until I've got free passage back home. Actually, I could just leave this place right now. The portal's fixed, after all."

c "That's not going to happen."

Rz amused "Let me ask you one thing: How exactly are you planning to stop me? I'm the one with the gun here."

c "You would shoot me to save your own hide?"

Rz annoyed "Only if you insist on standing in my way."

c "You're not going to get away that easily."

stop music fadeout 2.0

Rz "What are you going to do, huh? I'll be long gone by the time you call the cops."

c "I don't need to, Reza. They're already here."

play music "mx/termination.ogg" #fadein 0.5

m "Suddenly, Bryce and Maverick were standing next to me."

show reza at Position (xpos = 0.9) with ease #Position(xpos=0.75, xanchor='center') with ease

show maverick normal flip at Position(xpos=0.2, xanchor='center') with easeinleft

show bryce stern flip at Position(xpos=0.1, xanchor='center') with easeinleft

Rz angry "You planned this, didn't you, [player_name]?"

#Rz "Traitor!" with Shake((0, 0, 0, 0), 2, dist=10)

Rz "Traitor!" with hpunch

Rz "And to think I let you distract me with such a cheap trick! Just because I thought there was still a shred of humanity within you..."

play sound "fx/rev.ogg"

show reza gunself with dissolve

show reza gunpoint with dissolve

m "He pulled out his gun, not sure which one of us he should be aiming at."

Rz "Just let me go, and I'll forget this thing ever happened."

c "You've got six bullets for three people. Do you think you can really do that, Reza? Do you think this is worth risking your life for?"

Rz angry "I've been risking my life for this every day for the last two weeks. What did you do during that time? Sip champagne in your nice apartment?"

Rz "Besides, this generator and the whole building came from our time."

Rz "They belong to humanity!" with Shake((0, 0, 0, 0), 2, dist=10)

#Rz "They belong to humanity!" with hpunch
show reza at Position(xpos=0.45, xanchor='center')
#show izumi normal at right 
show bryce at Position(xpos=-0.3, xanchor='center')
show maverick at Position(xpos=-0.3, xanchor='center')
with ease

show izumi normal behind reza at Position(xpos=1.25, xanchor='center')
m "Suddenly, the Administrator came out of the shadows in the hallway behind Reza."

show izumi at right with ease


As "No, they belong to me."

#$ renpy.pause (0.3)

play sound "fx/rev.ogg"

show reza angry flip

m "Confused, Reza spun around, aiming his gun at the newcomer who was slowly walking towards him."

Rz "Who the fuck are you? Freeze! I said freeze!"

show izumi at Position(xpos=0.8, xanchor='center') with ease

As "Want to waste your bullets on me? Feel free. You can't stop all of us."

play sound "fx/rev.ogg"

Rz gunpoint flip "If you say so."

play sound "fx/gunshot2.wav"

$ renpy.pause (0.5)

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/impact3.ogg"

hide izumi with easeoutbottom

m "He pulled the trigger, and the Administrator fell to the ground with a dull thud that knocked her mask off."

$ persistent.izumiseen = True

show izumiinjured3 at Pan((300, 0), (600, 608), 7.0) with fade

$ renpy.pause (5.0)

hide izumiinjured3 
show maverick at Position(xpos=0.2, xanchor='center')
show bryce at Position(xpos=0.1, xanchor='center')
show reza at Position (xpos = 0.9)
with fade

m "My first instinct was to run away, but as Bryce and Maverick started charging, so did I."

show reza gunpoint

play sound "fx/gunshots4.ogg"

show bryce at Position (xpos = 0.30)  
show maverick at Position (xpos = 0.35)
with ease
$ renpy.pause (0.5)
hide bryce with easeoutbottom

play sound "fx/gunshots4.ogg"

show maverick at Position (xpos = 0.6) with ease
$ renpy.pause (0.5)
hide maverick with easeoutbottom

m "Reza was quick with his aim, shooting both Maverick and Bryce twice before pointing his gun in my direction."

play sound "fx/rev.ogg"

show reza gunself with dissolve

play sound2 "fx/boxdive.ogg"

m "I quickly dove behind the box with the generator for cover, just as Reza pulled the trigger multiple times."

play sound "fx/gunshot2.wav"

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger2.ogg"
#queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger2.ogg"
#queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger1.ogg"

$ renpy.pause (1.0)

play soundloop "fx/hiss.ogg" fadein 1.0

m "Only a single shot came out and lodged itself in the box. Though I was seemingly unharmed, a loud hiss began to emanate from my cover."

Br "Everybody, run! It's going to explode!"

show reza angry with dissolve

hide reza with easeoutleft

m "I started running towards the exit and was soon overtaken by both Reza and Maverick. I looked back over my shoulder to see Bryce grab the Administrator before he started running as well."

#m "Just as I reached the outside, the explosion knocked me off my feet."

stop music fadeout 1.0

scene np2y at Pan ((0, 100), (0, 100), 0.0) with fade

#explosion

play sound "fx/explosion.ogg"

play soundloop "fx/fireworks.ogg" fadein 10

m "Just as I reached the outside, the explosion knocked me off my feet." with Shake((0, 0, 0, 0), 3.0, dist=30)

m "There was a rain of small debris as I heard the walls of the building shaking in their foundation."

show reza annoyed at Position (xpos = 0.9) with dissolve

show maverick angry flip at Position(xpos=0.2, xanchor='center') with dissolve

play sound "fx/reload.ogg"

m "As I looked up, I saw Reza fumbling with his gun as Maverick pounced on him."

play sound "fx/rev.ogg"

show reza gunpoint with dissolve

show maverick at Position(xpos=0.65, xanchor='center') with move6

play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top") 
show reza at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top") 
with move9

#show maverick at Position(xpos=0.6, xanchor='center') with move6
#hide reza
#hide maverick
#with dissolve

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/bite.ogg"

#show maverick at Position(xpos=0.6, xanchor='center') with move6
#hide reza
#hide maverick
#with dissolve

#play sound "fx/bite.ogg"

m "He bit into Reza's neck and strained for a second before ripping a large chunk out of it."

m "Reza wasn't moving when Maverick walked off and came towards me."

show maverick normal c at center with dissolve

Mv "Where is Bryce?"

m "I looked towards the entry which was now mostly blocked by debris."

c "He must still be inside."

show maverick rage c with dissolve

Mv "Then what are you still waiting for? Come on!" with Shake((0, 0, 0, 0), 2, dist=10)

hide maverick with dissolve

play sound "fx/rocks1.ogg"

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/undress.ogg"

m "We ran towards the rubble, only to see the Administrator crawling through a small hole as she removed the last bits of debris that separated her from the outside world."

m "Afterwards, she laid down, panting heavily. Water began to trickle from the new opening."

c "It's the water pockets. The building must be flooded."

show maverick angry c with dissolve

Mv "And he's still inside. I'll clear away the rubble, and you try to find him."

hide maverick with dissolve

play sound "fx/rocks2.ogg"

queue sound "fx/water1.ogg"

m "We both set to work as I stuck my head into the hole that the Administrator had crawled out of."

play sound "fx/underwater.ogg"

m "The place was flooded completely, but luckily, even through the water I could see Bryce as he also tried to clear away the rubble from the other side."

stop sound fadeout 0.5

play sound2 "fx/water2.ogg"

m "Quickly, I pulled my head back out of the hole."

play sound "fx/rocks3.ogg"

c "He's on the other side, trying to get through."

show maverick rage c with dissolve

Mv "Who knows how long he's been underwater. Give him some air!" with Shake((0, 0, 0, 0), 2, dist=10)

stop sound fadeout 0.5

hide maverick with dissolve

play sound2 "fx/water1.ogg"

play sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/underwater.ogg"

m "I took a deep breath before I went in again. I extended my arm to grab Bryce's muzzle. Luckily, he seemed to understand what I was going for as he moved into my reach."

play sound2 "fx/bubbles.ogg"

m "I pressed my lips to his muzzle, giving him some much-needed air."

stop sound fadeout 0.5

play sound2 "fx/water2.ogg"

m "I drew back, repeating the same process a few times while Maverick cleared away the rubble, until eventually, Bryce surfaced, panting heavily."

play sound "fx/rocks4.ogg"

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/watersurface.ogg"

$ renpy.pause (1.5)

show bryce angry with easeinbottom
show bryce brow with dissolve

c "Are you alright?"

Br stern "Yes. Let's get away from here before the empty water pockets cave in or something."

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1n at Pan((500, 320), (500, 150), 6.0) with dissolvemed

m "Maverick carried the Administrator while we went uphill towards the portal." 

show rezadeadneck at Pan ((0, 326), (580, 126), 10.0) with fade

$ renpy.pause (5.0)

m "When I came across Reza's corpse, I took the time to strip him of his gun and ammo, not wanting the dragons to find them."

hide rezadeadneck with fade

m "Meanwhile, the Administrator was set on the ground, and Bryce checked out everyone's injuries. Luckily, it seemed both Bryce's and Maverick's were comparatively minor and didn't need any immediate attention."

play sound "fx/undress.ogg"

m "The Administrator was not so lucky, however. She squirmed as Bryce moved her clothes out of the way to get a good look at her bullet wound." 

As "No, don't."

m "As I returned to them, I heard Bryce audibly gasping."

show bryce stern with dissolve

Br "Damn it."

c "Is it bad?"

Br brow "[player_name], do you remember the first victim? The blood on his muzzle from fighting back was neither yours nor Reza's, but still distinctly human. I thought it was an error, or that our DNA tests weren't compatible."

Br stern "But Reza doesn't have a matching bite wound from him. She does."

m "I considered the implications of Bryce's words. Whereas Reza usually didn't hesitate to admit the killings to reach a goal he thought noble, he had denied any such actions this time."

m "Of course, there was no use ignoring the evidence before us. This could only mean one thing."

c "Why did you do it, Izumi? Why did you kill them?"

hide bryce with dissolve

if persistent.annabadending == True:

    show izumi normal 3 d with dissolve
    
else:
    
    show izumi normal 3 c with dissolve

Iz "He did kill them, you know. Just not in this timeline."

Iz "If you can even remember my name now, then you should also rememeber what else he would have done. How he would enslave them to use as weapons back in the future and how he doesn't care what happens to this world."

Iz "I had to do it in order to put you on the same trail he would have."

Iz "If I had come to you during the first night and tried to explain to you that I am a time traveller who had to kill in order to prevent a suffering that is magnitudes greater - genocide, slavery - would you have believed me?"

Iz "Who could've known that, sometimes, even Reza can change?" 

Iz "If he didn't kill anyone, there would have been no investigation, and you wouldn't have known how dangerous he is when he shows his true colors."

Iz "You just saw that even in this scenario he wouldn't shy away from shooting others to get what he wants."

Iz "Besides, I didn't want to risk jeopardizing our experience by changing things. It could erase all the progress we have made and the things we learned over the many times we've done this now. "

Iz "If I didn't shove you out of the way in the cellar when the light fixture came down, you would've died then and there. That's what happened the first few times." 

Iz "There was a lot of trial and error involved to get where we are now. You wouldn't believe the lengths I have to go to every single time and the consequences if I don't."

Iz "You could not have followed the same path and arrived here if I didn't kill them. The fact that you remembered that it was originally Reza who did it only proves just how important this is." 

Iz "Only if the events stay the same long enough will you be able to learn from them and remember, despite the effects the repeated teleportations have on your memory."

Iz "This only tells me that I made the right call."

c "If Reza had nothing to do with it, then what was he doing when he was trying to take the generator?"

Iz "I slipped him a note he thought came from you. It said to meet here and take the generator before you'd leave together. He played his part well enough so you couldn't tell the difference."

c "So, he really did think that I planned all of this, that I lured him here to have him arrested by Bryce and Maverick."

Iz "For all he's done, I think he deserves to know what betrayal feels like."


show np1n at Position (xpos = 1.07, xanchor = "right")
show izumi at Position (xpos = 0.8) 
with ease

show maverick angry c flip at Position (xpos = 0.0) with easeinleft

play sound "fx/growl.ogg"

Mv "I've listened to this long enough now. It was you, and that's all that matters to me."

show bryce stern at Position (xpos = 0.5) with easeinbottom

Br "No, Maverick! Don't do it!"

show maverick rage c flip with dissolve

Mv "I'll tear you apart!" with Shake((0, 0, 0, 0), 2, dist=10)

play sound "fx/wooshimpact3.ogg"

show maverick at Position (xpos = 0.30) with move6

#show bryce at center with Shake((0, 0, 0, 0), 2, dist=10)

hide bryce with easeoutbottom


show maverick at Position (xpos = 0.6) with move6

#play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top") 
show izumi at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top") 
with move9

#hide maverick
#hide izumi
#with dissolve

play sound2 "fx/bite.ogg"

m "Bryce tried to go between them, but Maverick aimed his shoulder squarely into Bryce's bullet wound. Bryce collapsed, convulsing in pain as Maverick pounced on Izumi and tore into her."

play sound "fx/rev.ogg"

queue sound "fx/gunshots2.ogg"

m "Meanwhile, I put a few bullets into the gun I took from Reza before I aimed at Maverick and pulled the trigger several times."

m "Maverick collapsed instantly and looked at me with a pained expression. Beneath him lay Izumi, dead."

show maverick angry c at center with dissolve

Mv "Why?"

m "He was trembling and took a few slow steps towards me, only stopping when I aimed the gun at him."

c "Stop right there."

Mv "She killed them, and you protect her?"

c "We needed her."

Mv normal c "I told you I'd show no mercy if I found the killer."

Mv angry c "Just when I thought I could trust you. I should have known you'd shoot me, just like Reza did."

c "No, it's not like that."

Mv "Then, why?"

c "I don't think I can explain."

m "He shook his head weakly."

Mv nice c "Thanks for proving me right, [player_name]."

Mv "Do you remember when I confronted you a while back and asked you to explain your reasons?"

if c2mav == "ambassador":
    
    Mv "You told me you both just came as ambassadors and nothing more."

    m "He gave a weak chuckle as a trail of blood slowly ran down from the corner of his muzzle."

    Mv "What an interesting kind of ambassador you turned out to be."
    
else:

    Mv "You told me I wouldn't understand." 

    Mv "You're right... I don't..."
    

hide maverick with dissolve

m "His head slumped as he closed his eyes. He was dead."

show brycemav at Pan ((580,0), (0, 326), 12.0) with fade

$ renpy.pause (9.5)

stop soundloop fadeout 2.0
stop music fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow

$ renpy.pause(3.3)

play sound "fx/door/doorbell.wav"
$ renpy.pause(2.0)

stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

play music "mx/prophecy.ogg" fadein 2.0

show bryce stern with dissolve

c "Hey, Bryce."

Br brow "I'm afraid I've got some pretty bad news for you."

c "What is it?"

Br stern "We were able to power the portal again even without the generators from the lab, but we still couldn't re-establish contact with humanity."

c "Why not?"

#Br brow "They don't even think it has anything to do with the new power source, as everything else works like it did before." 

Br brow "Ever since the portal got sabotaged and was repaired, the coordinates – the connection to humanity's portal… It just isn’t there anymore."

c "Can't you locate it again?"

Br "We don't know how."

Br stern "We found a different set of coordinates in there, but for some reason, we aren't able to use them."

c "I know, only I can. They are for travelling back in time to the day of my arrival."

Br smirk "I guess you really are a time traveller, huh?"

c "Now that you know everything, that really shouldn't surprise you."

Br brow "What are you going to do now?"

c "Well, I guess returning to humanity is out of the picture."

Br "So, it's either staying here, or using the portal to return to the day you arrived here."

Br laugh "All that time travel business is too complicated for me."

c "Izumi had it all figured out."

c "I'm wondering what she would think about this outcome. All she ever wanted was to save you dragons, just like Reza only wanted to save humanity."

Br stern "Neither shied away from killing people, so maybe you shouldn't look to them as pillars of morality."

Br brow "Either way, I'm not sure if you really have much of a choice here. They don't actually know if they can stop the comet. Of course they'll try, but without the generators from the lab, it's not looking great for us."

c "I initially came here to help humanity, but if I go back with what I know now, maybe I can help you too."

Br normal "At any rate, it was nice while it lasted."

c "Hey, no need for melancholy now. It's not as if we're not going to see each other again."

#stop music fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

nvl clear

window show

n "Soon, I was preparing to return to the day of my arrival."

n "Despite her actions, Izumi had made a good point."

n "Thinking about the knowledge I had now, I realized just how important it was to remember and how it would help me during my next attempt."

n "No doubt, the teleportation would erase some of my memory again, but I could think of a few ways to retain some knowledge."

n "Not only did I take my own written account of what had happened with me, but there were also physical reminders I could bring to remember, such as Izumi's mask and cloak."

n "With her gone, I was now the one with the most experience."

n "As I made my way to the portal, I realized that in order to make this mission a success - to save everyone - this time I would just have to save myself."

window hide

stop music fadeout 2.0

$ renpy.pause (2.0)

$ _game_menu_screen = None

stop sound fadeout 2.0

#scene black with dissolveslow

$ renpy.pause (2.0)

$ renpy.block_rollback()

play sound "mx/sweetmemories.ogg"

$ renpy.pause (1.5)

show fireworks at Pan ((-960, 545), (-200, 350), 20)
show credits1 at left
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

show tripwire at Pan ( (800, 0), (1000, 608), 20.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show bryceback at Pan((50, 900), (-600, 208), 25.0)
show credits5 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed
#stop movie

#

show cgmeeting at Pan ((740, 608), (1240, 0), 24)
show credits7 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#

show cgbryce
show credits9 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (8.5)

scene black with dissolvemed

stop sound fadeout 1.4

$ renpy.pause (4.0)

$ persistent.anygoodending = True

$ persistent.lastendingseen = "good"

$ persistent.endingsseen += 1

call izumimask from _call_izumimask_6

call optimistcheck from _call_optimistcheck_2

if persistent.brycegoodending == False:

    $ persistent.brycegoodending = True
    
    $ achievement.grant("Murderer")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_88

    $ mp.brycegoodending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Bryce's good ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "bryce"
    
    jump tut
    
else:

    jump mainmenu







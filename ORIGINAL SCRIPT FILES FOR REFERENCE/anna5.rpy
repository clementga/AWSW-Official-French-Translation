label anna5:

show black with dissolvemed
$ renpy.pause (0.5)
scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow

$ save_name = "Chapter 5 - Anna"

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(That must be her.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

show anna normal with dissolve

An smirk "Hey, [player_name]. Looks like you're ready to go."

c "I didn't think you'd want to go to a community event like this one."

An normal "Anything can be fun with the right company."

c "With that argument, we could just stay here."

An sad "I haven't seen the fireworks in years. With all the crazy shit that's happened to me recently, maybe they'll be a reminder of better days."

c "Better days? You don't usually talk about yourself like that..."

An normal "It's because I just don't give a damn anymore. Who cares if you know that about me? Who cares if the entire town knows? I certainly don't."

An "These days, I'm just trying to make the most of whatever is left."

c "Alright. Let's go, then."

scene black with dissolvemed
$ renpy.pause (0.5)
scene viewingspot with dissolvemed

play music "mx/amb/night.ogg" fadein 5.0

m "After a few minutes of walking, we arrived at a rather empty looking area near the edge of town."

show anna normal with dissolve

c "So much for the whole town being out to watch the fireworks."

An face "Yeah, I'm not going to those places. I'm kind of a celebrity, you know."

c "Really?"

An sad "For better or worse, people know about me. Of course they would, given my intellectual status."

c "Or maybe you just don't want to be seen with me."

An normal "No, that's not it. Actually, that could be quite fun. It would only be another reason for people to be jealous of me."

c "Oh, I think it's starting."

play soundloop "fx/fireworks3.ogg"

m "We waited quietly as the stillness of the night enveloped us. Soon, I heard the sound of the first rocket making its way into the night sky after which it exploded in a pattern of colors."

m "More rockets followed, their thunderous noise echoing throughout the land."

show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow
$ renpy.pause (6)
#hide fireworks with dissolveslow


stop music fadeout 2.0

hide fireworks with dissolveslow

#stop music fadeout 2.0

m "Suddenly, a terrible realization hit me."

play music "mx/judgement.ogg" fadein 0.5

m "Considering how public of an event this was and how everyone would be watching the fireworks, now would be the best time for Reza to make his move."

m "Not only was the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever need."

m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."

c "Anna, I think we need to go. Now."

An face "Really? The fireworks just started."

c "I know where Reza is. We need to stop him."

An disgust "Speak for yourself. This isn't my responsibility."

c "This is much bigger than you. Are you going to help me or not?"

An sad "Alright, just for you. What do you want me to do, fight him?"

c "I'm not sure if that would be such a good idea. I want to try talking to him first."

An "If you can buy us some time, maybe I could get some help."

c "That would be perfect. He'll be at the portal. Let's go!"

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow

$ renpy.pause (3.5)

#call function here

call endingjustafewminuteslater from _call_endingjustafewminuteslater_1

Mv "Maybe I can."

play music "mx/disturbance.ogg" fadein 0.5

m "Suddenly, Maverick and Anna appeared next to me."

show reza at Position (xpos = 0.9) with ease #Position(xpos=0.75, xanchor='center') with ease

show maverick normal flip at Position(xpos=0.2, xanchor='center') with easeinleft

show anna sad flip at Position(xpos=0.05, xanchor='center') with easeinleft


Rz angry "You planned this, didn't you, [player_name]?"

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

show izumi normal behind reza at Position(xpos=1.25, xanchor='center')
Rz "They belong to humanity!" with Shake((0, 0, 0, 0), 2, dist=10)

#Rz "They belong to humanity!" with hpunch
show reza at Position(xpos=0.45, xanchor='center')
#show izumi normal at right 
show anna at Position(xpos=-0.3, xanchor='center')
show maverick at Position(xpos=-0.3, xanchor='center')
with ease

m "Suddenly, the Administrator came out of the shadows in the hallway behind Reza."

show izumi normal at right with ease


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

m "He pulled the trigger and the Administrator fell to the ground with a dull thud that knocked her mask off."

$ persistent.izumiseen = True

show izumiinjured2 at Pan((300, 0), (600, 608), 7.0) with fade

$ renpy.pause (5.0)

hide izumiinjured2
show maverick at Position(xpos=0.2, xanchor='center')
show anna at Position(xpos=0.1, xanchor='center')
show reza at Position (xpos = 0.9)
with fade

m "My first instinct was to run away, but as Maverick started charging, so did Anna and I."

play sound "fx/snarl.ogg"
show maverick angry flip with dissolve

$ renpy.pause (1.0)


#show maverick at Position(xpos=0.6, xanchor='center') with move6
#hide reza with easeoutbottom
#hide reza
#hide maverick
#with dissolve

show maverick at Position(xpos=0.65, xanchor='center') with move6

play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top") 
show reza at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top") 
with move9


#$ renpy.pause (2.0)

queue sound "fx/bite.ogg"

m "Maverick was fast, pouncing on Reza before he had a chance to aim at any of us."

m "He was knocked to the ground and Maverick embedded his teeth into the body before him."

play sound "fx/gunshots4.ogg"

m "Reza was screaming. He aimed at Maverick's head and frantically pulled the trigger twice."

if annagoodending == True:
    
    jump annagoodending
    
else:
    
    pass

play sound "fx/rev.ogg"

show reza gunself b at center behind anna with dissolve

#show anna at center with ease
show anna at Position (xpos = 0.4) with ease

play sound "fx/gunshots2.ogg"

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
queue sound2 "fx/trigger2.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger2.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger1.ogg"

show anna rage flip with dissolve

$ renpy.pause (2.0)

hide anna with easeoutbottom

m "The jaws dislodged and Reza aimed his gun in my direction. Suddenly, Anna jumped in front of me as the deafening bangs of several more shots rang out through the hallway."
hide reza with dissolve

play sound "fx/reload.ogg"

m "While I was unharmed, Anna was hit multiple times and fell to the ground. While I watched Reza's hand dive into his pocket for more ammo, Anna's harsh breathing filled my ears."

play sound "fx/boxdive.ogg"

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/spray.ogg"

m "Quickly, I dove behind the generator's box for cover and saw Anna opening her muzzle, spraying some liquid in Reza's direction."

play sound "fx/firex.ogg"

m "Reza looked at her in bewilderment before he suddenly burst into flames."

m "He started flailing his arms around wildly, trying to put out the fire." 

m "But the flames didn't stop. He tried to get up, but failed as he fell once more and squirmed around the floor shrieking in agony."

m "A short time later, his body slumped and his cries stopped as he lay on the ground, motionless. I watched for a while as the flames continued burning the now lifeless body."

m "I went over to Anna, only to realize she was covered in blood from her bullet wounds. She was breathing heavily, but was still alive."

c "This looks bad. I have to do something to stop the bleeding."

show anna cry e with dissolve

An "Don't bother. Based on where he got me, I'll be gone soon." 

c "Don't say that."

An "I've done autopsies before. I know how this goes. No one can help me now."

c "You jumped in front of me, Anna. Why? Why did you do it?"

An "I only had a few months left to live. If I was lucky, that is. Anything past that wouldn't even be a life worth living." 

An "Would you want to spend your last days strapped to a hospital bed, slowly wasting away until nothing is left but a mere shell - a shadow of your former self?" 

An "They can prolong my life, but they can't save me. But by doing this, I could save you - so I did." 

An "I know you have it in you, to achieve and succeed at what you set out to do. Even if I couldn't."

An "Even if they'd have me rot and die in prison rather than finding a cure for myself and who knows how many others. Just...  make it count, [player_name]."

hide anna with dissolve

m "Before I could answer, her head slumped. She was dead."

$ annadead = True

m "I looked around the room. The fire had stopped and it had become eerily quiet as I checked on the others."

show maverickdead2 at Pan ((0, 0), (200,400), 10.0) with fade

$ renpy.pause (8.5)

show rezaburned at Pan ((0, 326), (580,0), 10.0) with fade

$ renpy.pause (8.5)

hide rezaburned 
hide maverickdead2
with fade

m "While I confirmed that Maverick and Reza were dead, I was glad to discover that the Administrator was still alive."

m "I found a first aid kit in one of the rooms and used it to dress her wound."

m "After a bit of rest, she was able to get up and we walked outside."

stop music fadeout 2.0

scene black with dissolveslow

$ renpy.pause (0.5)

scene np2y at Pan ((0, 100), (0, 100), 0.0)

if persistent.annabadending == True:

    show izumi normal 2 d
    
else:

    show izumi normal 2 c

with dissolveslow

play music "fx/fireworks.ogg" fadein 10.0

#$ renpy.pause (0.3)

As "What are you planning to do now?"

c "I don't know, Izumi. What do you think we should do? We have to stop the comet, after all."

Iz "So you remember my name. What else do you remember?"

c "I know we can stop the comet, but I also want to help humanity. I'd be just like Reza if I didn't try, you know. Just helping one world and disregarding the suffering of the other."

Iz "That's why I was asking for your plan."

c "Sending generators now would be out of the question, since we'll need all we can gather in order to stop the comet."

Iz "That is correct."

c "Unfortunately, I also know that by the time we've stopped the comet, humanity will have given up on the portal and disconnected its power source, so we won't be able to help them afterwards."

Iz "You remember well."

c "The solution to this would be rather simple: We'd just need to let them know to wait a while longer while the dragons recover from expending all their power sources to stop the comet."

c "We could just send them a letter."

Iz "I'm afraid that won't be possible."

c "And why is that?"

Iz "After what happened during some of our other attempts, I decided to delete the coordinates to humanity's portal when I repaired this one a few days ago."

c "But the portal has ways to locate other functional portals, right? We could re-establish the connection."

Iz "Unfortunately, looking for other portals through time and space would be a significant energy expenditure that we can't afford right now. Not if we want to stop the comet."

c "I... reject this outcome. If there is no way to send them help, I will go back to the day of my arrival and try again. That's why you put those coordinates in, after all."

Iz "No, that's not your call to make. These coordinates were only to be used in emergencies, or if we failed."

c "As far as I am concerned, we did fail."

Iz "Look at this world and what they have achieved under my guidance. You want to jeopardize this for a chance – just a chance - to save your city as well?"

c "It's what I came here for. Reza too, but he's dead now, so I'm the only one they have left to fight for their survival."

c "I can't just leave them now. As nice as it would be, a life here would be a life built on the suffering of others. I wouldn't be able to live with myself knowing that I could've helped them but didn't because I took the easy way out."

c "As far as I am concerned, this isn't over yet."

#Iz "Who do you really want to save, those who sent Reza? Those who supported him?"

Iz "You want to save those who sent Reza, and his supporters?"

Iz "Is this really about humanity, or about Anna?"

Iz "She sacrificed herself for you, not for you to undo it all again."

Iz "It is her sacrifice that makes it possible to save this world now. Is that not enough for you?"

c "No, I'm going."

Iz "If that is your final decision, you leave me no other choice."


m "Suddenly, I saw her reaching for something in one of her pockets." 

#play sound "fx/silence.ogg"
#queue sound "fx/silence.ogg"
#queue sound "fx/silence.ogg"
#queue sound "fx/silence.ogg"
queue sound "fx/rev.ogg"
queue sound "fx/hit1.ogg"
queue sound "fx/gunshot2.wav"

$ renpy.pause (0.3)

show izumi at Position (xpos = 0.525, xanchor = "center", ypos = 1.025, yanchor = "bottom") with ease



m "When it parted to reveal Reza's gun, I quickly grabbed it and pointed it out of the way before Izumi pulled the trigger."

#play sound "fx/hit2.ogg"
#$ renpy.pause (0.2)
#play sound "fx/hit1.ogg"
#$ renpy.pause (0.2)
#play sound "fx/gunhit.ogg"
#$ renpy.pause (0.6)
#hide izumi with easeoutbottom

play sound "fx/hit2.ogg"
queue sound "fx/hit1.ogg"

show izumi at Position (xpos = 0.55, xanchor = "center", ypos = 1.05, yanchor = "bottom") with ease

#show izumi at Position (xpos = 0.575, xanchor = "center", ypos = 1.075, yanchor = "bottom") with ease

play sound "fx/gunhit.ogg"

$ renpy.pause (0.5)

#hide izumi with easeoutbottom

show izumi at Position (xpos = 0.6, xanchor = "center", ypos = 1.0, yanchor = "top") with ease


m "In the ensuing scuffle, I managed to wrest it away from her and hit her in the face with its blunt end."

m "She collapsed in pain as blood started to run down her cheek where the impact had opened a gash."

m "As she squirmed on the ground, I turned to her before I took my leave."

c "You know what? For all Reza has done, you sure don't seem that different from him when it comes down to it. Goodbye."

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1n at Pan((500, 320), (500, 150), 6.0) with dissolveslow

m "As I made my way to the portal to return to the day of my arrival, I thought about what had just happened and what I would do now." 

m "If anything, Izumi's actions had only strengthened my resolve to make things right. Just right. After all, I had all the time in the world to try."

stop music fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

#window hide

#$ renpy.pause (2.0)

$ _game_menu_screen = None

stop sound fadeout 2.0

#scene black with dissolveslow

#$ renpy.pause (2.0)

$ renpy.block_rollback()

play sound "mx/mindstream.ogg" fadein 0.5

#$ renpy.pause (1.5)

show izumiinjured2 at Pan((-450, 400), (400, 508), 20.0)
show credits1 at left
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

show testingroom at Pan ((960,0), (0,233), 20.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show cgcampfire at Pan ((0, 500), (1500, 100), 30.0) #Position(xpos=0.75, xanchor='center')
show credits5 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed
#stop movie

#

show cgdamion at Pan ((500, 0), (400, 302), 20) #at Position(xpos=0.25, xanchor='center') at Pan((0, 0), (0, 302), 5.0)
show credits7 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#

show cganna at Pan((-600, 302), (-600, 0), 20.0)
show credits9 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

stop sound fadeout 2.5

$ renpy.pause (4.0)

#$ persistent.anygoodending = True
$ persistent.lastendingseen = "bad"

$ persistent.endingsseen += 1

call izumimask from _call_izumimask

if persistent.annabadending == False:

    $ persistent.annabadending = True
    
    $ achievement.grant("Sacrifice")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_42

    $ mp.annabadending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Anna's bad ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "anna"
    
    jump tut
    
else:

    jump mainmenu
    


label annagoodending:

play sound "fx/rev.ogg"

show reza gunself b at center behind anna with dissolve

show anna at center with ease

play sound "fx/impact3.ogg"

show anna at center with vpunch

#$ renpy.pause (2.0)

hide anna 
hide reza
with dissolve

play sound "fx/gunshots2.ogg"

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
queue sound2 "fx/trigger2.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger2.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger1.ogg"

#$ renpy.pause (2.0)

#hide anna with easeoutbottom
    
m "The jaws dislodged and Reza aimed his gun in my direction. Out of nowhere, Anna tackled me – shoving us both out of the way just before Reza unloaded the weapon in our direction."

show anna rage flip at Position (xpos = 0.2) 
show reza angry b at Position (xpos = 0.9)
with dissolve

play sound "fx/reload.ogg"

m "Both of us were seemingly unharmed, and by the time Reza was reloading his gun, Anna was already up again and running towards him."

play sound "fx/rev.ogg"

show reza gunpoint b with dissolve

show anna at Position (xpos = 0.65) with move6

play sound "fx/impact3.ogg"

show anna at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top") 
show reza at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top") 
with move9

#hide reza
#hide anna
#with dissolve

play sound2 "fx/gunshot2.wav"

m "Just as he raised his arm to aim at her, she jumped and collided with him, causing him to miss his target wildly."

play sound "fx/slice.ogg"

m "She was on top of him now, raising a hind leg before slitting his throat with one of the large claws at the end of it."

m "Immediately he slumped. Blood gushed from his wound as he helplessly squirmed on the ground and horrible, distorted noises left his severed windpipe."

m "After a few seconds, his movements stopped and Anna returned to me."

show rezathroatslit at Pan ((0, 326), (1280,0), 12.0) with fade

$ renpy.pause (10.5)

hide rezathroatslit

show anna sad at center

with fade

An "Are you alright?"

c "Yeah."

m "We went to check on the others, but both Maverick and the Administrator were dead."

show maverickdead3 at Pan((300, 900), (600, 758), 7.0) with fade

$ renpy.pause (5.0)

show izumidead2 at Pan((800, 608), (1000, 750), 8.0) with fade

$ renpy.pause (5.0)


stop music fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

nvl clear

window show

play music "mx/schizophrenia.ogg"

n "In the weeks that followed, the dragons prepared for the comet."

n "I, on the other hand, spent more time with Anna as she opened up about her condition."

n "When the time came, the dragons executed their plan, and by utilizing the underground building's generators, the comet was ultimately diverted and never hit Earth."

n "Even after they recovered and power was restored to the portal, I knew that I wouldn't be able to return to my own time as the Administrator, Izumi, had deleted the coordinates I needed to return home when she repaired the portal a while ago."

n "While she had her own reasons for doing this, it meant that now my only options were to stay here, or to use the portal and the coordinates she had entered to travel back in time and return to the day of my arrival in this world."

window hide
nvl clear
window show

n "However, I wasn't very concerned about this at the moment, as I spent my time in this world accompanying Anna on her journey."

n "For her help in stopping Reza, she was awarded the highest honor the council could bestow on her, citing her bravery and exceptional service to the community."

n "As a result, the case against her was dropped and she was cleared of all charges."

n "In the months that followed, I was with her during her cancer treatments and could only watch as her condition worsened by the day."

n "By this point, she was living in a hospice and had become thin and weak as her disease had eroded her both physically and mentally."

window hide

nvl clear

show testingroom at Pan ((0, 233), (0, 233), 0.0) 

show anna sad

with dissolveslow

c "What did the doctor say?"

An "Who cares what the doctor says? I know he sugarcoats everything. It's not going to be long now, or else I wouldn't even be here."

c "I'm not sure if there is any sensible way to ask this, but..."

An "We're talking about less than a week." 

An "Besides, I'm the one who's dying here, not you. No reason for you to be so upset."

m "She looked away from me as I saw tears welling up in her eyes."

An cry "And to think that in your world you already had a cure for cancer."

An "How pointlessly tragic."

An "Yet here I am, being what I never wanted to become."

show annasick at Pan((300, 169), (0, 0), 12.0) with fade

$ renpy.pause (7.0)

An "But at least I'm not alone."

scene black with dissolveslow

$ renpy.pause (2.0)

nvl clear

window show

n "A few days later, she passed away quietly in her sleep."

$ annadead = True

n "The council held a funeral in her honor, which I didn't attend."

n "Now that I had been with Anna until the end, I had a decision to make."

n "I could either stay here, accept this outcome and all its consequences, or - by using the portal and Izumi's coordinates - travel back in time and return to the day of my arrival in this world."

n "This way, I could get the chance to try again."

n "No doubt, it would be a risk to relive this rollercoaster of emotions. After all, I would have to go through all the events and their dangers again, but maybe it would be worth it..."

stop music fadeout 2.0

window hide

#scene black with dissolveslow

$ renpy.pause (2.0)

#window hide

$ renpy.pause (1.0)

$ _game_menu_screen = None

stop sound fadeout 2.0

#scene black with dissolveslow

#$ renpy.pause (2.0)
#$ renpy.block_rollback()

play sound "mx/fragilemind.ogg" fadein 0.5

#$ renpy.pause (1.5)

show rezathroatslit at Pan ((500, 326), (1280,0), 20.0)
show credits1 at left
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

show testingroom at Pan ((960,0), (0,233), 20.0)
#show annasick at Pan((700, 169), (0, 0), 20.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show cgcampfire at Pan ((0, 500), (1500, 100), 30.0) #Position(xpos=0.75, xanchor='center')
show credits5 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed
#stop movie

#

show cgdamion at Pan ((600, 0), (400, 302), 23) #at Position(xpos=0.25, xanchor='center') at Pan((0, 0), (0, 302), 5.0)
show credits7 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#

show cganna at Pan((-600, 302), (-600, 0), 22.0)
show credits9 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (3.0)

stop sound fadeout 2.5

$ renpy.pause (7.0)

scene black with dissolvemed

stop sound fadeout 2.5

$ renpy.pause (4.0)

$ persistent.anygoodending = True
$ persistent.lastendingseen = "good"

$ persistent.endingsseen += 1

call izumimask from _call_izumimask_1

call optimistcheck from _call_optimistcheck

if persistent.annagoodending == False:

    $ persistent.annagoodending = True
    
    $ achievement.grant("Tragic Hero")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_43

    $ mp.annagoodending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Anna's good ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "anna"
    
    jump tut
    
else:

    jump mainmenu







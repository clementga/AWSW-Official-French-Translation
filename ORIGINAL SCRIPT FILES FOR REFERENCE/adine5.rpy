label adine5:

show black with dissolvemed
$ renpy.pause (0.5)
scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow

$ save_name = "Chapter 5 - Adine"

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(I guess she's here.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

show adine normal b with dissolve

Ad "Are you ready?"

c "Ready for what?"

Ad giggle b "The fireworks, silly."

c "Oh, of course. Let's go."

scene black with dissolvemed
$ renpy.pause (0.5)
scene viewingspot with dissolvemed

play music "mx/amb/night.ogg" fadein 5.0

m "After a few minutes of walking, we arrived at a rather empty looking area near the edge of town."

show adine normal b with dissolve

Ad "Here we are."

c "If this is everyone, I'm disappointed. I thought it would be crowded here."

Ad giggle b "This is actually one of my training spots, and it turns out you can see the fireworks pretty well from here too."

c "So this is your secret spot, then?"

Ad think b "I guess you could say so."

c "Well, now that I know of it, I suppose it's not so secret anymore."

Ad normal b "Not if you keep it to yourself. We could make it {i}our{/i} secret."

c "If you say so."

Ad giggle b "Hey, looks like it's starting. Now, take a good look."

show adine normal b with dissolve

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

m "Not only was the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever have."

m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."

c "Adine, I think we need to go. Now."

Ad giggle b "Stop joking around, [player_name]. You still haven't seen the best part."

c "I know where Reza is. We need to stop him."

Ad think b "Are you serious?"

c "Yes, I am."

Ad disappoint b "What should we do, then?"

c "Maybe you could fly and get us some help. I'll try to buy us some time by confronting him."

Ad think b "Alright, where should I meet you?"

c "Somewhere near the portal. He'll be there. Let's go!"

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow

$ renpy.pause (3.5)

#call function here

call endingjustafewminuteslater from _call_endingjustafewminuteslater_4

if adinegoodending == True:
    
    jump mainmenu

Mv "Maybe I can."

play music "mx/martyr.ogg" fadein 0.5

m "Suddenly, Maverick and Adine appeared next to me."

show reza at Position (xpos = 0.9) with ease #Position(xpos=0.75, xanchor='center') with ease

show maverick normal flip at Position(xpos=0.2, xanchor='center') with easeinleft

show adine think b flip at Position(xpos=0.05, xanchor='center') with easeinleft


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
show adine at Position(xpos=-0.3, xanchor='center')
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

m "He pulled the trigger, and the Administrator fell to the ground with a dull thud that knocked her mask off."

$ persistent.izumiseen = True

show izumiinjured6 at Pan((300, 0), (600, 608), 7.0) with fade

$ renpy.pause (5.0)

hide izumiinjured6
show maverick normal flip at Position(xpos=0.2, xanchor='center')
show adine at Position(xpos=0.1, xanchor='center')
show reza at Position (xpos = 0.9)
with fade

show reza gunpoint

play sound "fx/gunshot2.wav"

$ renpy.pause (0.5)

hide adine with easeoutbottom

m "Reza was quick with his gun and shot Adine once before Maverick even had a chance to charge."

play sound "fx/snarl.ogg"
show maverick angry flip with dissolve

$ renpy.pause (1.0)

play sound "fx/gunshots2.ogg"


show maverick at Position (xpos = 0.35)  with ease
$ renpy.pause (0.5)
show maverick at Position (xpos = 0.5)  with ease
$ renpy.pause (0.5)
hide maverick with easeoutbottom

m "As Maverick ran towards him, Reza adjusted his aim before shooting at Maverick multiple times."

show reza annoyed with dissolve
show reza at Position (xpos = 0.8) with ease

play sound "fx/gunshot2.wav"

m "Maverick stumbled and fell before Reza walked up to him and shot him in the head."

Rz angry "What now, [player_name]? Are you going to let me through, or do I have to finish the job with you?"

m "Adine was lying on the ground next to me, injured."

show adinewounded at Pan((0, 0), (780, 300), 10.0) with fade

$ renpy.pause (8.5)

hide adinewounded with fade

m "I looked over to Maverick and the Administrator. Both lay dead in a pool of their own blood."

show maverickdead1 at Pan((500, 500), (250, 400), 7.0) with fade

$ renpy.pause (5.0)

show izumidead6 at Pan((0, 0), (140,79), 7.0) with fade

#show izumidead6 at Pan((800, 608), (1000, 750), 7.0) with fade

$ renpy.pause (5.0)

hide izumidead6
hide maverickdead1
show reza at center
with fade

c "Now you hesitate to kill, after doing all this?"

play sound "fx/rev.ogg"

Rz gunself "It's your choice."

Ad "Please..."

c "Just... go." 

Rz angry "If you told me that just a few minutes ago, I wouldn't have had to do all this. Heck, you could've come with me, you stupid idiot. But if you want to die here with everyone else, feel free."

Rz annoyed "Alright, step over there and lie on the ground. If I see either of you moving before I'm gone, I'll shoot."

m "I did as he said and could only watch as he took the generator and left."

show reza annoyed flip at Position (xpos = 0.8) with ease

play sound "fx/box2.wav"

$ renpy.pause (2.0)

show reza annoyed

$ renpy.pause (0.3)

show reza at Position (xpos = 0.5) with ease

$ renpy.pause (0.3)

show reza at Position (xpos = 0.2) with ease

$ renpy.pause (0.3)

hide reza with easeoutleft

#stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolveslow

$ renpy.pause (2.0)

nvl clear

window show

n "While both Maverick and the Administrator were dead, it turned out that Adine's injury was fairly minor and she soon got the medical attention she needed."

n "When I attempted to use the portal to follow Reza, however, I had to realize that humanity's portal was not accessible."

n "After Reza had arrived on the other side, he or humanity must have quickly deactivated the portal in order to prevent anyone from connecting with it again."

n "I warned the dragons about the comet, but without the generators from the underground building, they failed at diverting the comet enough to make a difference."

window hide
nvl clear
window show

n "As such, the only remaining option for me was to use the portal with the Administrator's coordinates, which would enable me to travel back in time to the day of my arrival in this world."

n "I met with Adine for one last time to tell her about my plan: I would use the portal to try again, hoping for a better outcome."

stop music fadeout 2.0

window hide

nvl clear

$ renpy.pause (3.0)

#scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow

$ renpy.pause (0.3)

#show adine normal b with dissolve

scene adineapt at Pan ((128, 300), (128,300), 0.0)
show adine normal b
with dissolveslow

play music "mx/prophecy.ogg" fadein 2.0

$ renpy.pause (0.3)

Ad "There will always be another year, huh?"

c "What are you talking about?"

Ad disappoint b "That's what you told me during the summer festival when you talked me out of flying in the contest. There will always be another year, so I didn't have to fly in this one."

c "I'm sorry."

Ad normal b "Don't be. You did what you could. Even if it has to end like this, I enjoyed my time with you. Let's not have any regrets now."

c "Thank you."

Ad disappoint b "Remember when I asked you what you were going to do if you knew the world was going to end?"

if adine1choice == "fullest":
    
    Ad "You told me you would enjoy life to the fullest until the last moment. I guess you won't have to do that if you go back."

    c "And you won't have to either if I get to have any say in this."
    
elif adine1choice == "goodbyes":
    
    Ad "You told me you would say your last goodbyes and hope for the best. Is that what this is, your last goodbyes?"

    c "It's not a goodbye. It's an \"I'll see you in a better future.\""

elif adine1choice == "outside":
    
    Ad normal b "You told me you would stay outside and watch it all unfold before your eyes. Maybe that's what I'll do."

    c "You won't have to see it. Not if I get to have any say in this."
    
else:
    
    Ad "You told me you'd hide in a bunker deep underground, but I'm not sure if I can do that. Maybe I'll just stay outside and watch it all go down. At least then I'll know the moment when it comes."

    c "You won't have to see it. Not if I get to have any say in this."


Ad sad b "Can't I just come with you?"

c "Unfortunately, no. These coordinates are tied to my biometric data. Only I can use them."

Ad disappoint b "Oh, well."

c "Don't worry, I'll be back before you realize it and nothing will have happened."

Ad normal b "I'll wait for you."

stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolveslow

$ renpy.pause (2.0)

#window hide

#$ renpy.pause (2.0)

$ _game_menu_screen = None

stop sound fadeout 2.0

#scene black with dissolveslow

#$ renpy.pause (2.0)

$ renpy.block_rollback()

play sound "mx/sleepingcity.ogg"

#$ renpy.pause (1.5)

show izumidead6 at Pan((-850, 0), (-350, 80), 20.0)
#show adinewounded at Pan((-540, 0), (780, 300), 20.0)
#show adinewounded at Pan((0, 0), (780, 300), 20.0)
show credits1 at left
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

show beach at Pan ((500, 0), (1100, 0), 20.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show map at Pan ((-500, 0), (0, 0), 23) #Position(xpos=0.75, xanchor='center')
show credits5 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed
#stop movie

#

show cgamely at Pan ((400, 0), (980, 326), 23) #at Position(xpos=0.25, xanchor='center')
show credits7 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#

show cgadine2 at Pan((-600, 302), (-600, 0), 22.0)
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

call izumimask from _call_izumimask_9

if persistent.adinebadending == False:

    $ persistent.adinebadending = True
    
    $ achievement.grant("Getaway")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_92

    $ mp.adinebadending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Adine's bad ending!"
    

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "adine"
    
    jump tut
    
else:

    jump mainmenu



label adinegoodending:

Rz "I mean, what are you going to do? You can't stop me now, anyway."

play sound "fx/rev.ogg"

show reza gunself with dissolve

m "He pulled out his gun and pointed it at me."

c "Reza, wait! Why can't we just talk about this?"

Rz "We just did."

c "No! What about -"

Rz annoyed "Wait, you're just trying to distract me, aren't you?"

c "No, I'm just -"

show reza angry with dissolve

#Rz "Shut up!" with Shake((0, 0, 0, 0), 2, dist=10)

Rz "Shut up!" with hpunch

Rz annoyed "They're probably already on their way."

play sound "fx/rev.ogg"

show reza gunself with dissolve

queue sound "fx/gunshot3.ogg"

queue sound "fx/impact3.ogg"

$ renpy.pause (0.5)

m "Suddenly, Reza shot me in the leg, causing me to fall over and squirm in pain." with vpunch

show reza annoyed flip with dissolve

$ renpy.pause (0.3)

show reza at Position (xpos = 0.8) with ease

play sound "fx/box2.wav"

$ renpy.pause (2.0)

show reza annoyed

$ renpy.pause (0.3)

show reza at Position (xpos = 0.5) with ease

$ renpy.pause (0.3)

show reza at Position (xpos = 0.2) with ease

$ renpy.pause (0.3)

hide reza with easeoutleft

m "I saw Reza running to the box containing the generator. He lifted it up using both of his hands before making his way towards the exit as fast as he could."

show maverick angry at Position (xpos = 1.3)

show maverick at Position (xpos = -0.4) with ease

m "When Reza got close to the entrance, I saw a flurry of grey zipping past me with a thunderous gallop." 

show reza normal at Position (xpos = 0.2) with dissolve

show reza normal flip

$ renpy.pause (0.3)

show reza angry flip with dissolve

play sound "fx/box1.wav"

#show reza gunpoint flip with dissolve

#queue sound "fx/rev.ogg"

m "I looked towards Reza who turned around, dropped the box, and grabbed his pistol." 

show maverick angry at Position (xpos = 1.4)

play sound "fx/rev.ogg"

show reza gunpoint flip behind maverick with dissolve

show maverick at Position(xpos=0.45, xanchor='center') with move9

play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.2, xanchor='center', ypos=1.0, yanchor="top") 
show reza at Position(xpos=0.0, xanchor='center', ypos=1.0, yanchor="top") 
with move9

#$ renpy.pause (2.0)

queue sound "fx/bite.ogg"

#show maverick at Position (xpos = 0.5) with move

#play sound "fx/bite.ogg"

#hide maverick
#hide reza
#with dissolve

m "It was Maverick, who pounced immediately. Reza fell to the ground, and before he could so much as react, Maverick buried his teeth in Reza's neck and bit down."

m "Reza slumped instantly and didn't move again."

show rezabitten2 at Pan ((0, 326), (580,0), 10.0) with fade

$ renpy.pause (8.5)

hide rezabitten2 
show maverick normal c at left
with fade

m "Then, Adine appeared and called out to Maverick."

show adine disappoint b at right with dissolve

Ad "Why did you have to kill him?"

$ renpy.pause (0.3)

show maverick normal c flip

$ renpy.pause (0.3)

Mv "Because I'm not taking chances anymore."

c "What took you so long?"

Ad "[player_name]! Are you alright?"

c "He got me in the leg. Maybe there's a first aid kit in one of these rooms."

hide maverick
hide adine
with dissolve

m "Adine went into one of the adjoining rooms, only to reappear with a first aid kit shortly afterwards."

show adine disappoint b with dissolve

Ad "Can I do anything else? I'm not sure if I can apply the bandage."

c "You could tell me what took you so long."

Ad normal b "Well, at first, Maverick wanted to storm the place head-on, but then I remembered the map you gave me and the other entrance. We heard you two talking and figured we could surprise him if we went in the other way."

c "I guess I shouldn't be complaining then, because this could have turned out so much worse. Well done, Adine."
#show maverick at Position (xpos = -0.4)
Ad disappoint b "We probably should be getting you some real help."

show maverick normal c at Position (xpos = -0.4)

$ renpy.pause (0.0)

show adine at right

show maverick at Position (xpos = 0.1)
with ease


m "She turned to Maverick."

Ad annoyed b "Come on, what are you waiting for?"

c "Maybe he thinks I'm going to take the generator while you're gone."

Mv "..."

$ renpy.pause (0.3)

show maverick normal c flip

$ renpy.pause (0.3)

Mv "Guess you really wanted to stop Reza. My apologies."

$ renpy.pause (0.3)

show maverick normal c 

$ renpy.pause (0.3)

hide maverick with easeoutleft

hide adine with easeoutleft

stop music fadeout 2.0

m "He turned and they both left."

m "Shortly thereafter, the Administrator appeared and came towards me."

show izumi normal with dissolve

play music "mx/clocks.ogg" fadein 2.0

c "Izumi, you're kinda late this time, too."

As "How ironic that you would remember her name now."

As "Besides, it didn't seem like you really needed me. Good job."

c "Her name? What are you talking about?"

As "I'm not Izumi."

hide izumi with dissolve

play sound "fx/undress.ogg"

$ renpy.pause (0.3)

m "The person I thought was the Administrator took off the mask, only to reveal a strangely familiar face underneath."

m "The person before me had a face that looked exactly like mine, down to the tiniest detail. It was like looking into a mirror or at a twin. It was me."

play sound "fx/undress.ogg"

$ renpy.pause (0.5)

show izumi normal with dissolve

As "You understand why I'm wearing the mask now?"

c "How is this possible?"

As "It's complicated. By now, I guess you know that this always ends with you travelling back in time when something goes wrong."

As "When I was in your position, Izumi died during our confrontation with Reza, and as all the experience from all the different attempts vanished with her, I decided I had to become the person who would oversee the next one."

As "I didn't know just how complicated it would be."

As "Luckily, she left a lot behind to help me, and I executed her plan just as she would."

#As "And now, here we are."

c "So, what do we do now?"

As "Well, with the generators still intact, we will have no trouble diverting the comet and saving this world, but I also know that you feel very strongly about executing the mission you were sent here for."

As "Unfortunately, I'm starting to realize now that this won't be possible."

c "What are you talking about?"

As "As outlined in Izumi's plan, I deleted the coordinates that would lead back to humanity's portal when I repaired this one, replacing them with coordinates to travel back in time to the day of your arrival in this world."

As "Unfortunately, this means that our connection to humanity's portal is lost."

c "Are you saying we could've saved humanity if you just didn't remove those coordinates?"

As "I'm afraid so."

c "Then why did you do it?"

As "I didn't realize it would come to this. I just executed her plan as she would have. I can understand her reasoning for it, though."

As "It presents an extraordinary risk. Eliminating these coordinates also eliminates the possibility of Reza getting away through the portal and taking the generator we need with him."

c "Why not just tie them to my biometric data like the coordinates we need to travel back in time?"

As "That wouldn't be much help, because in scenarios where Reza escapes with the generator, he wouldn't hesitate to kill you to take what he needs to bypass the biometrics scan and use the portal anyway."

c "Then the only way to achieve what we want is to not delete those coordinates."

As "Can we really take that risk? You know that if we fail badly enough even once - if the portal gets destroyed, or if both the Administrator and you die - there won't be any more chances."

c "If you have seen what goes on from the Administrator's side during my stay here, I suppose you should be the one to decide that."

c "That still doesn't address the question of what we should do now, though."

As "If we want to make this happen, one of us will have to go back and do this all over again."

c "And what happens to the other?"

As "They could stay here and live their life however they wanted."

c "What about Adine?"

As "I wish I could stay with her. All she does for the orphans... I wish I could be part of that."

As "I wish I could be done with this already and settle down, but someone has to go back and ensure we can reach the outcome both of us want. No matter if it's you or me, one of us has to do it." 

As "Otherwise, all those we know back home, they... I don't think I need to tell you."

c "Why are you making me think of those who suffer?"

As "You'll never forget them, and if you don't do this, it will haunt you. I know."

c "What do you want me to do? Go back in time and do it all over again?"

As "It's what we've been trying to do all this time, you know. No compromise."

c "And of course you want me to do it so you can stay here, huh?"

As "I will do it myself if that's what it takes. I just hoped it wouldn't have to be me."

c "Don't we both?"

As "If we wanted to settle for an outcome where we just stop the comet and stay here, we could have done so a long time ago."

c "That doesn't mean that we're both not tired of this."

As "Maybe forgetting everything again by stepping through the portal would be a boon, then."

c "Don't try to make this more palatable for me. How many times have we done this now?"

As "..."

As "I don't know."

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

play sound "mx/aquavitae.ogg"

$ renpy.pause (1.0)

show rezabitten2 at Pan ((-500, 326), (80,0), 20.0)
show credits1 at left
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

show adineshower at Pan ((300, 608), (880,0), 20.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show adineflying at Pan ((-500, 200), (0, 0), 23)
show credits5 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed
#stop movie

#

show cgamely at Pan ((400, 0), (980, 326), 23) #at Position(xpos=0.25, xanchor='center')
show credits7 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#

show cgadine2 at Pan((-600, 302), (-600, 0), 22.0)
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


scene adineapt at Pan ((128, 300), (128,300), 0.0)
show adine normal b
with dissolveslow

play music "mx/hopefulAMELY.ogg" fadein 2.0

$ renpy.pause (0.3)

Ad think b "What will you do now?"

c "For the time being, I suppose I'll be stuck in this world."

Ad disappoint b "Just losing the connection to humanity's portal... How is that even possible?"

c "I don't know. Maybe we'll never be able to re-establish contact."

Ad normal b "No matter what happens, you'll always be welcome here."

Ad disappoint b "You put your life on the line to save us, and it cost your colleague his life."

c "Reza was never my colleague."

Ad think b "Then what was he, exactly?"

c "You know, maybe it's better if humanity never finds out what happened."

Ad disappoint b "Oh, well..."

Ad normal b "Either way, I'm glad you're here now. And I think Amely will appreciate it, too."

c "You think so?"

Ad "I'm sure of it! The people from the orphanage should be here any minute now."

c "I'm a bit nervous, to be honest."

Ad think b "Have you ever babysat before?"

c "Not a dragon, that's for sure."

Ad normal b "Don't worry, I'll be here with you the whole time. But you'll have to be very careful, alright?"

c "Of course."

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

Ad "I guess it's time. Are you ready?"

c "..."

c "I think so."

stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolveslow

$ renpy.pause (4.0)

$ persistent.anygoodending = True
$ persistent.lastendingseen = "good"

$ persistent.endingsseen += 1

call optimistcheck from _call_optimistcheck_3

if persistent.adinegoodending == False:

    $ persistent.adinegoodending = True
    
    $ achievement.grant("Decisions")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_93

    $ mp.adinegoodending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Adine's good ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "adine"
    
    jump tut
    
else:

    jump mainmenu



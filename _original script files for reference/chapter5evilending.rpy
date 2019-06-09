label evilending:

$ save_name = "Chapter 5 - Evil"
    
c "Sure."

m "I approached Reza. Both of us took a side of the cardboard box and lifted it up. It wasn't heavy enough that he couldn't have carried it on his own, but I was sure he appreciated the help."

m "Slowly, we made our way through the long hallway towards the exit."

Rz amused "We've made it, [player_name]. We really did. With this, we can save our city - and we can have something for ourselves too."

c "Can you hold the box for a minute? I want to show you something."

Rz "Sure."

m "I watched as Reza adjusted his grip on the box before I let it go. I dug into my pocket as he resumed talking."

Rz laugh "All the glory and riches that come from this - they're ours. And we earned it."

c "Yes, Reza. We did."

Rz amused "What do you think about that?"
 
c "I only have one question: Why would I share it with you?"

show reza angry with dissolve

play sound "fx/box2.wav"

m "Immediately, his expression changed to one of horror as he let the box fall to the ground and reached for his gun."

m "Having distracted him by letting him hold the box, I already had my finger on the trigger of my own gun - or rather, a copy of Reza's gun."

m "I had acquired it in a previous attempt. I wasn't sure how long ago that was, but I vaguely remembered taking it from Reza's corpse after he had tried to kill me one time."

play sound "fx/rev.ogg"

queue sound "fx/gungore.ogg"

$ renpy.pause (0.7)

show reza at Position (ypos = 1.0, yanchor = 0.9) with ease

m "While he still fumbled to get a grip on his own weapon, I shot him in the arm and kicked his gun far away after it fell to the ground. He contorted in pain and slouched against the wall behind him."

m "When he realized I was still aiming at him, he threw up his other arm in defeat."

Rz "Wait..."

c "You were willing to kill to get here, so you shouldn't complain about me doing the same thing."

Rz "Can't we talk about this?"

c "Do you think this was a spontaneous decision, Reza? You have no idea for how long I've been planning to do this."

Rz "Why, [player_name]? You have nothing to gain from killing me."

c "You think so? Think again. We both know that humanity would have had so much more to gain if we actually cooperated with the dragons."

c "Just look at all their technology. You were willing to waste it all, and for what? Just so you and I could profit most from this and be hailed as heroes when at large our world wouldn't change."

c "A token victory over what could have been possible."

Rz "That's not what this was about. It was the better plan. Better than taking the risk of cooperating with them and waiting for the comet to pass."

c "You always hid behind your idealism, Reza, but it just so happens that it's always you who stands the most to gain in the end."

Rz "So what? I thought we had an agreement there."

c "We did - but in the end, someone like you just isn't trustworthy. We both know what we did, Reza."

c "If humanity found out we'd rather forego our trade agreement and just let a potential long-term trade partner be eradicated by the meteorite for our own profit, they surely would not be pleased."

c "I think we both know that it would fall under treason, the only crime heinous enough to our leaders to warrant immediate execution."

c "Shutting off communication with the dragons for a few weeks would have been easy, and after they were gone, they wouldn't present a risk for us to be found out. So the only ones who would know about what we did are you and me."

c "I know you don't shy away from murder, so I was sure that one day, you would try to silence me to eliminate the last risk of being found out."

c "Now you're just jealous that I thought of it before you did."

Rz "I could've gotten rid of you a long time ago if I wanted." 

Rz "I could've ditched you and left you behind, but I trusted you."

Rz "I didn't even need you in the first place. I did all of this on my own, and now you just came here to take everything for yourself. You don't deserve any of it."

c "You've got a good point, you know, but it won't save you." 

Rz "It doesn't have to. I'd rather die trying to do what is right than sit around, living my life doing nothing and watching our world go down in ashes." 

hide reza with dissolve

c "And die, you will."

play sound "fx/gunshots3.ogg"

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
queue sound2 "fx/trigger2.ogg"
#queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger2.ogg"
#queue sound2 "fx/silence.ogg"
queue sound2 "fx/trigger1.ogg"

m "I pulled the trigger, firing the remaining bullets into him until no more were left."

m "His body sunk, like a puppet cut from its strings. He was dead."

show rezashotsixtimes at Pan ((1000, 626), (1280,0), 10.0) with fade

$ renpy.pause (8.5)

hide rezashotsixtimes with fade

m "I put away the gun and grabbed the box that contained the generator and a few other things Reza had taken from the lab."

scene black with dissolvemed

$ renpy.pause (0.5)

scene np1r at Pan((500, 150), (500, 150), 6.0) with dissolvemed

m "Soon, I was outside, and after a bit of walking while carrying the heavy box, I arrived at the portal."

m "After activating the controls, I took my place, ready to return to humanity as a hero."

#stop music fadeout 2.0

m "Not the time of dragons or man, but the time of [player_name] had come."

$ _game_menu_screen = None

stop music fadeout 2.0

#scene black with dissolvemed

#nvl clear

#window show

#$ renpy.show("port1")
#$ renpy.transition(Dissolve(2))

#play sound "fx/telstart.ogg"
#play sound "fx/tel.wav"

#n "{cps=40}Not the time of dragons or man, but the time of [player_name] had come.{/cps}{nw}"

#scene port2 with dissolveslow
#scene port1 with dissolve
#scene port2 with dissolve
#scene port1 with dissolve
#scene port2 with dissolve
#scene port1 with dissolve
#scene port2 with dissolve
#scene port1 with dissolve


#$ renpy.pause (2.0)

stop sound fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

$ renpy.block_rollback()

play sound "mx/darkrock.ogg"

$ renpy.pause (0.8)

show rezashotsixtimes at Pan ((700, 626), (970,0), 16.0)
show credits1 at left
with dissolvemed

$ renpy.pause (6.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (6.0)

scene black with dissolvemed

show sebastiandead at Pan((1080, 308), (300, 0), 16.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (6.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (6.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show explosion at Position(xpos=0.75, xanchor='center')
show credits5 at left 
with dissolvemed

$ renpy.pause (6.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (6.0)

scene black with dissolvemed
#stop movie

#

show cgmeeting at Pan ((740, 608), (1240, 0), 16)
show credits7 at right 
with dissolvemed

$ renpy.pause (6.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (6.0)

scene black with dissolvemed

#

show deadbody at Pan ((0, 0), (-500, 1000), 16)
show credits9 at left 
with dissolvemed

$ renpy.pause (6.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (6.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (7.0)

scene black with dissolvemed

stop sound fadeout 2.0

$ renpy.pause (4.0)

$ persistent.lastendingseen = "bad"

$ persistent.endingsseen += 1

if persistent.evilending == False:

    $ persistent.evilending = True
    
    $ achievement.grant("Betrayal")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_96
    
    $ mp.evilending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen the evil ending!"


if persistent.endingsseen == 1:

    $ persistent.firstending = "alone"
    
    jump tut
    
else:

    jump mainmenu


label endingjustafewminuteslater:
    
m "I arrived at the portal just a few minutes later. I couldn’t help but be glad that it was still turned off and didn’t appear to have been used recently... But it meant Reza was still here, somewhere."

label endingjustafewminuteslaterx:
#stop music fadeout 2.0

m "I looked around, thinking about where he could be or if it was worth waiting for him here when I saw something out of the corner of my eye."

if sebastiansaved == False:
    
    m "Hesitating, I drew nearer."

    show sebastiandead at Pan((1080, 608), (300, 150), 10.0) with fade
    
    $ renpy.pause (8.0)
    
    m "I checked Sebastian for any signs of life and found nothing. However, his body was still warm."
    
    hide sebastiandead with fade

    m "Reza was here very recently, but he hadn't used the portal just yet. Why?"

    m "Sebastian's guard post was not just for the portal itself, but also the surrounding area. Since Reza was already here, he probably had some unfinished business very close by."
    
else:
    
    m "There was a suitcase leaning against the portal."
    
    play sound "fx/suitcase.ogg"

    m "When I opened it to check on its contents, I was surprised to find a few eggs inside. I had no doubt that this was Reza's doing."

    m "Apparently, he had broken into the hatchery again, stashing the eggs here. But he hadn't used the portal just yet. Why?"

    m "Given that he hadn't left yet, he clearly still had unfinished business in the area."
    
    
m "The underground building. The Administrator had told me all about the prowess of the generators within. It probably hadn't been hard for Reza to guess the same, or to try stealing them from a place he knew would be even more deserted than the rest of the village was right now."

m "He also didn't have far to go from the portal. All things considered, it was the only option that made sense to me."

m "I could've waited for Reza here, but in the end I decided it would be better to meet him underground. If there was going to be a confrontation, I was sure I would have the advantage in a more crowded space."

stop soundloop fadeout 3.0

stop music fadeout 2.0

m "Even in the darkness, it was easy for me to spot the site where they had unearthed the building's entry as it was in a roped off area that I had seen from afar before."

scene black with dissolvemed

$ renpy.pause (0.5)

scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed

$ renpy.pause (2.0)

m "When I entered the building, I was met by a long, illuminated hallway that was lined with doors on both sides."

label sincethelightswerealreadyon:

m "Since the lights were already on, Reza had to be very close. I wasn't surprised at the building still having electricity, since its generators were also powering the portal."

play sound "fx/door/hallwaydoor.ogg"

m "Suddenly, one of the doors opened, and out came Reza, carrying a large cardboard box."

m "When he spotted me, he set it on the ground."

play sound "fx/box1.wav"

$ renpy.pause (1.0)

show reza normal with dissolve

play music "mx/path.ogg" fadein 0.5

if endingselect == "bryce":

    if brycegoodending == True:

        if persistent.endingsseen == 0:
            
            pass
        
        else: 
        
            jump brycegoodending
        
else:
    
    pass

Rz "[player_name]! You're here? You don't know how glad I am to see you.  I've wanted to talk with you for so long. I even tried to contact you, but I couldn't with someone tailing you the whole time."

Rz "But talking can wait. Now that you're here, we've got everything. Come on, help me with this and let's get out of here."

#total evil points 40
    
if persistent.neutralending:

    if endingselect == "alone":
    
        if evilpoints >= 30:

            $ evilending = True
        
            jump evilending
        
    else:
        
        pass
        
elif persistent.brycegoodending:

    if endingselect == "alone":
    
        if evilpoints >= 30:

            $ evilending = True
        
            jump evilending
        
    else:
        
        pass

else:
    
    pass

label no:

c "No."

Rz annoyed "No? What are you talking about?"

c "I'm not doing anything until you answer a few questions."

Rz amused "You want to talk now? Sure, why not? We've probably got a few hours if we wanted to. None of them will disturb us here. We could even get the backup generator as well after we send this one over."

if loremgoodending == True:
    
    return

c "When did you realize we were in the past? How did you know about the comet?"

Rz normal "I've known for a while. It's what I wanted to talk with you about when we met at the portal. How about you?"

c "I only recently found out."

Rz annoyed "Looking back, it just seems so obvious to me now. I'm not sure how exactly you figured it out, but there are so many damn clues when you think about it."

Rz normal "I mean, how could a supposedly completely different, independent civilization speak the same language as us? What was this supposed to be? An alternate reality? No, it was just a different time."

Rz annoyed "When was there ever anything resembling these ... creatures on Earth? It's not hard to make the jump from dragons to dinosaurs when some of them here look pretty damn near identical to dinosaurs we knew about."

Rz "And then, there are also the prehistoric fruits, the plants and the fact that their technological level is nearly exactly the same as our own past society."

Rz normal "But we don't even have to think that abstract. You just needed to look at the sky."

Rz annoyed "The sun, the moon, even the stars are the same. Constellations change over time, of course, but you know we could account for that stuff." 

Rz "You could've just pointed your PDA at the sky and it would've told you the time period - including the imminent threat of being eradicated."

Rz "You could even see the meteorite in the sky, and how it would change its position day after day."

c "Are you done being condescending?"

Rz normal "I guess so."

c "You killed those dragons, Reza."

if endingselect == "bryce":

    if brycegoodending == True:

        if persistent.endingsseen > 0:
            
            return
        
        else: 
        
            pass
        
else:
    
    pass

Rz amused "What a brilliant deduction, Sherlock."

c "Why did you do it?"

Rz annoyed "Do you really need me to spell it out? I thought better of you."

Rz "After I found out the truth about this place, I knew just waiting for the generators we were owed was not an option anymore."

Rz normal "It would have taken who knows how long, but I didn't intend to stay a day longer than necessary."

Rz annoyed "You wouldn't believe how hard it was for me to acquire some generators. Some of the dragons didn't go down easily."

Rz amused "But who cares that they got back the generators I stole? With just this one, we won't need any of the others."

c "How could you do this?"

Rz annoyed "{i}How could I do this?{/i}"

Rz amused "Let me ask you this: What harm is there really in taking their generators when their whole civilization will be gone in a few weeks, anyway? The ones I killed just died a little earlier than scheduled."

Rz annoyed "Even if that creep hadn't shown up and interrupted our meeting, we wouldn't have had the time for them to make the generators for us."

c "How about we don't let them all die?"

Rz amused "They aren't going to be extinct any time soon, if that's what you're concerned about. I paid the hatchery another visit before I came here."

Rz normal "With the right... persuasion, I think we'll have plenty of reasons to keep at least some of them around. Bodyguards, border patrols, weapons. Even as pets or companions, as long as we make the necessary changes."

Rz amused "See, it's not as bad as you might think."

c "I'm not going to just abandon them like that, only for their whole civilization to be wiped out."

Rz angry "Get your priorties straight, [player_name]."

Rz "Next you'd rather starve, because you suddenly empathize with a steak. And you're not satisfied just starving by yourself. No, you're going to let all of us starve, because you want to impose your morals on everyone."

Rz annoyed "Since when do you think that you get to have any say in this? You know why you're here. What you're proposing is treason, and you know the consequences."

Rz amused "Personally, I don't mind if you want to stay here. You know I don't care about corporal punishment."

Rz normal "Just let me through and you can do whatever you wish."

c "I can't do that, Reza."

Rz annoyed "I see how it is. They've told you they need this generator to stop the comet, huh? And now you've become their lackey."

Rz "Don't tell me you've been drinking up what they've been telling you. You know they have as much of a vested interest in this whole thing as humanity does - that I and you do, or at least used to."

Rz "Do you think they wouldn't do the same thing if it was their families on the line instead of ours?"

c "Their entire world is on the line here."

Rz "They live in perfect harmony, with their perfect green energy source and no reason for wars or conflicts, yadda yadda yadda. We had that too, and you know what happened then? Of course you do." 

Rz "This is such an idiotic trope, you know. Random person meets weird natives, learns their ways and then ends up saving them."

Rz "What do they need you for, huh? Maybe they're going to be extinct for a reason if they can't even save themselves."

c "You know of our suffering, yet will let them have it?"

Rz angry "I don't care what happens to them, but unlike you, I was at least trying to save humanity."

c "At any cost."

Rz "We have the solution right here, and you want to get philosophical now? Don't you think we deserve it?" 

Rz "They've had it for who knows how long. Now it's time for us."

c "Not like this."

Rz "Do you think I like it? If there was a different way, I wouldn't have spent the last few weeks doing what you didn't."

Rz "We don't live in this fairy tale world of yours where there is a perfect solution to everything. You should know that. Just being here for a few weeks must have messed you up."

Rz annoyed "I think I know why."

Rz "You got too used to all the comforts they have here. You actually don't care if they all die back home, do you?" 

Rz "As long as you can stay here, in this perfect little world of yours. You have discarded everything and everyone back home, and replaced it with this."

Rz "Maybe it is because you just don't have a life back home."

Rz normal "I can even understand that a little. Of course it would be nice to just stay here where they have everything that we don't, but being here also reminded me of everything I hated about our world as it used to be."

Rz angry "The pettiness and the politics. Say about the solar flare what you want, but it leveled the playing field and gave people like us a chance to make a difference." 

Rz "For all of our efforts, what did we get? A vote that was meaningless in a sea of stupidty and lies. Now everyone has to pull their own weight. We make the rules."

Rz "You, of all people, should understand."

Rz "Of course they wouldn't. They haven't experienced how it is, to live like we do now. To see the world burn and everyone you know die around you."

c "And because I have, I won't let the same thing happen to them."

Rz "How many do you think died back home just in the two weeks you've been here because we don't have power for the hospital, huh? Do you think those victims aren't worth mentioning, or do you just care about the few dragons I killed?"

Rz "Our city is the last bastion of a civilized society in a world where nothing else is left."

Rz annoyed "Maybe you have forgotten about them, but I haven't."

Rz "How many of us do you think will still be there in a month? A year? Or are they just a statistic to you?"

c "The same could be said for the dragons."

Rz "What do you want to do? Talk me down from doing this? And then what?"

Rz "It's too late, anyway. You think they're just going to let us go after what I've done? Fat chance."

Rz normal "Whatever you may think, you'll find that our leaders back home agree with my course of action."

c "Why are you telling me this?"

Rz "Because I expect you to join me."

c "That's not going to happen."

Rz angry "And you call yourself an ambassador? This generator is the only thing we need for our city to survive. How can you even argue about this?"

#Rz "Who told you that this generator in particular would be so important that they can't make it without it, huh?"


c "The dragons also need that generator and I'll do what is necessary to stop you if I have to."

Rz annoyed "So, that makes you judge, jury and executioner. What a wonderful set of morals you have there, [player_name]."


c "We only need to wait until the comet has passed safely."

Rz "You think you can stop the comet? And you need this generator to do that?"

Rz "Sure, and if your plan fails, then not only is this world gone, but we also lose any and all hope to save our own."

Rz angry "We are so close now. We can't risk anything by waiting for your crazy plan when back home they are dying by the minute. I will not let you."

c "You only want to save your own two-faced hide, because you don't want to face the consequences of what you did."

Rz "..."

Rz normal "..."

Rz laugh "Hahahahahahahahahahaha!"

c "Why are you laughing about this?"

Rz "Because it's a joke. It must be. I'm the one with the gun, and you thought you could just waltz in here and lecture me."

Rz amused "Listening to you was fun and all, but the grownups must get back to work now."

if endingselect == "adine":
    
    if adinegoodending == True:
    
        jump adinegoodending
    
else:
    
    pass

stop music fadeout 2.0

Rz "I mean, what are you going to do? You can't stop me now, anyway."

return

#label saveentry:
    
#$ save_name = renpy.input("Choose a name for your save file:", default=save_name, exclude='{%}', length=20)
    
#return

label syscheck:
    
    if persistent.achievements < 21:
        
        $ system = "normal"
        
    elif persistent.achievements < 41:
        
        $ system = "advanced"
        
    else:
        
        $ system = "sassy"
        
    return
    
label lazycheck:
    
    if persistent.lazynumber >= 10:
        
        if persistent.lazy == False:

            $ persistent.lazy = True
            
            $ achievement.grant("Lazy")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_97
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You decided not to meet anyone or investigate for the tenth time!"
                
            elif system == "advanced":

                s "You decided not to meet anyone or investigate for the tenth time. Who cares?"
                
            else:
                
                s "You decided not to meet anyone or investigate for the tenth time. Being exceptionally good at doing nothing apparently is a skill, too."
                
    return
    
label skipcheck:
    
    if persistent.skipnumber >= 10:
        
        if persistent.skip == False:

            $ persistent.skip = True
            
            $ achievement.grant("Fast Forward")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_98
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You used the skip function 10 times!"
                
            elif system == "advanced":

                s "You used the skip function 10 times. You skipper."
                
            else:
                
                s "You used the skip function 10 times. If you could, you'd probably skip this text too, wouldn't you?"
                
    return
    
label popularcheck:
    
    if popularnumber >= 2:
        
        if persistent.popular == False:

            $ persistent.popular = True
            
            $ achievement.grant("Popular")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_99
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You had two messages waiting for you!"
                
            elif system == "advanced":

                s "You had two messages waiting for you. I wonder why..."
                
            else:
                
                s "You had two messages waiting for you. You sure are getting around, aren't you?"
                
    return
    
label izumimask:
    
    if persistent.izumimask == False:

        $ persistent.izumimask = True
        
        $ achievement.grant("Unmasking")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_100
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You have seen what lies beneath the mask!"
            
        elif system == "advanced":

            s "You have seen what lies beneath the mask. Quite revealing, isn't it?"
            
        else:
            
            s "You have seen what lies beneath the mask. Unsurprisingly, it was a face."
                
    return
    
label optimistcheck:
    
    if persistent.optimist == False:

        $ persistent.optimist = True
        
        $ achievement.grant("Optimist")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_101
        
        play sound "fx/system.wav"
        
        s "You have seen your first good ending!"
                
    return
    
label mainmenu2:
    
    return

label skiptut:
    
    if persistent.skiptut == False:

        s "My records indicate you have already experienced this section in a satisfactory manner."

        play sound "fx/system3.wav"

        s "If you wish, we could skip sections like these which you have already cleared before."

        play sound "fx/system3.wav"

        s "No need to read everything again! Isn't that great?"

        play sound "fx/system3.wav"

        s "{i}How is this different from just using the skip buttons like [[Ctrl] and [[Tab]?{/i}, you might ask."

        play sound "fx/system3.wav"

        s "Well, here's the deal: Using the skip buttons can be tedious, especially when encountering puzzles you've already solved before or when faced with long dialogue trees."

        play sound "fx/system3.wav"

        s "Sometimes, it's just easier to jump over a whole section than speeding it up, y'know?" 

        play sound "fx/system3.wav"

        s "So, during relevant sections, I will come in and ask if you don't want to just outright jump ahead. Sound good so far?"

        play sound "fx/system3.wav"

        s "Anyway, there are times when you might still want to choose not to jump ahead like this and use the skip buttons as usual. That's totally fine."

        play sound "fx/system3.wav"

        s "Both methods have their own advantages and disadvantages."

        play sound "fx/system3.wav"

        s "Jumping ahead will often skip minor choices that can be made, especially during character sections with lots of dialogue options. This can include parts that would unlock new achievements."

        play sound "fx/system3.wav"

        s "However, jumping ahead will never skip important choices that you have to make, such as those that could result in good endings or the choices you make during your investigations." 

        play sound "fx/system3.wav"

        s "It's up to you whether you want to use it or not, but it might save you some time."

        play sound "fx/system3.wav"

        s "Either way, the choice is yours."

        play sound "fx/system3.wav"
        


        s "Would you like to skip ahead?"
        
        #only at the ending of stretch is the variable changed
        
        $ persistent.skiptut = True
        $ skipbeginning = True
        
    return

label resetall:
    $ persistent._clear(progress=True)

    $ persistent.set_volumes = True
       
    $ _preferences.volumes['music'] *= .80
            
    $ persistent.orb_taken = False

    $ persistent.remy1played = False

    $ persistent.dirttaken = False

    $ persistent.metdamion = False
    
    $ persistent.havemap = False

    $ persistent.base_taken = False

    $ persistent.ixomenbookread = False

    $ persistent.seenvarain2 = False

    $ persistent.playedadine2 = False
    
    $ persistent.chapter2libraryvisited = False

    $ persistent.varasaved = False
    
    $ persistent.playedanna1 = False
    
    $ persistent.seashells = False
    
    $ persistent.playedremy3 = False
    
    $ persistent.havetestresults = False

    $ persistent.ixomenassembled = False
    
    $ persistent.heardaboutcancer = False

    $ persistent.endingsseen = 0

    $ persistent.firstending = "none"

    $ persistent.neutralending = False

    $ persistent.evilending = False

    $ persistent.remygoodending = False

    $ persistent.remybadending = False

    $ persistent.brycebadending = False
    
    $ persistent.brycegoodending = False

    $ persistent.annabadending = False

    $ persistent.annagoodending = False

    $ persistent.adinebadending = False

    $ persistent.adinegoodending = False

    $ persistent.lorembadending = False

    $ persistent.loremgoodending = False

    $ persistent.anygoodending = False
    
    $ persistent.trueending = False

    $ persistent.secretending = False

    $ persistent.sebastianplayed = False

    $ persistent.minor2played = False

    $ persistent.minor3played = False

    $ persistent.minor4played = False

    $ persistent.minor5played = False

    $ persistent.brycedies = False
    
    $ persistent.brycediesnumber = 0

    $ persistent.brycesurvives = False

    $ persistent.brycekey1 = False
    
    $ persistent.brycekey2 = False
    
    $ persistent.brycekey3 = False
    
    $ persistent.brycekey4 = False

    $ persistent.brycesolvedonce = False
    
    $ persistent.brycefinished = False
    
    $ persistent.sebastianfail = True
    
    $ persistent.seenvara = False
    
    $ persistent.zhongname = False
    
    $ persistent.playedzhong = False

    $ persistent.bornread = False

    $ persistent.playedemera = False
    
    $ persistent.lastendingseen = "none"

    $ persistent.playedkatsu = False

    $ persistent.playedkevin = False

    $ persistent.c1blood = False
    
    $ persistent.c1invhigh = False
    
    $ persistent.c2skip = False

    $ persistent.c3skip = False

    $ persistent.c4skip = False
    
    $ persistent.adine1skip = False
    
    $ persistent.adine2skip = False
    
    $ persistent.adine3skip = False
    
    $ persistent.adine4skip = False

    $ persistent.adine1choice = "none"
    
    $ persistent.headgear = True

    $ persistent.anna1skip = False
    
    $ persistent.anna2skip = False
    
    $ persistent.anna3skip = False
    
    $ persistent.anna4skip = False

    $ persistent.bryce1skip = False
    
    $ persistent.bryce2skip = False
    
    $ persistent.bryce3skip = False
    
    $ persistent.bryce4skip = False

    $ persistent.remy1skip = False
    
    $ persistent.remy2skip = False
    
    $ persistent.remy3skip = False
    
    $ persistent.remy4skip = False

    $ persistent.lorem1skip = False
    
    $ persistent.lorem2skip = False
    
    $ persistent.lorem3skip = False
    
    $ persistent.lorem4skip = False
    
    $ persistent.bryce3do = "nothing"

    $ persistent.remy2picturesseen = False
    
    $ persistent.heardaboutcancerremy = False
    
    $ persistent.heardaboutcancerenvelope = False

    $ persistent.gotresultsviapost = False
    
    $ persistent.havetestresultsfromanna = False
    
    $ persistent.showautoforwardbutton = True
    
    $ persistent.izumiseen = False
    
    $ persistent.achievements = 0
    
    $ persistent.c1fish = False

    $ persistent.c1books = False
    
    $ persistent.c1meds = False
    
    $ persistent.c1liquid = False
    
    $ persistent.c1eggs = False
    
    $ persistent.c1eggnumber = 0
    
    $ persistent.c1fruits = False

    $ persistent.c1decline = False
    
    $ persistent.c1declinenumber = 0
    
    $ persistent.c1booksort = False

    $ persistent.c1boredom = False

    $ persistent.c1annaanswers = False

    $ persistent.c1teetotaler = False
    
    $ persistent.c1disrobement = False
    
    $ persistent.c1bastion = False
    
    $ persistent.c2interrogator = False
    
    $ persistent.c2bandage = False
    
    $ persistent.c2landscape = False            
    
    $ persistent.c2storeaisles = False
    
    $ persistent.c2investigation = False
    
    $ persistent.c2pictures = False
    
    $ persistent.c2legs = False            
    
    $ persistent.c2eau = False             
    
    $ persistent.c2magazine = False           
    
    $ persistent.c2music = False               
    
    $ persistent.havemapfirst = False               
    
    $ persistent.c3prank = False          
    
    $ persistent.c3helpedkatsu = False              
    
    $ persistent.c3interrogator = False               
    
    $ persistent.c3reckless = False             
    
    $ persistent.c3investigator = False     
    
    $ persistent.c3flawless = False             
    
    $ persistent.c4eggs = False            
    
    $ persistent.lazynumber = 0            
    
    $ persistent.lazy = False             
    
    $ persistent.skipnumber = 0            
    
    $ persistent.skip = False             
                
    $ persistent.popular = False
       
    $ persistent.c3pointless = False
    
    $ persistent.izumimask = False            
    
    $ persistent.firstending = False    
    
    $ persistent.optimist = False
    
    $ persistent.secactivated = False
    
    $ persistent.c1skip = False

    $ persistent.skiptut = False
    
    $ persistent.remymet = False

    $ persistent.annamet = False
    
    $ persistent.loremmet = False

    $ persistent.brycemet = False
    
    $ persistent.adinemet = False
    
    $ persistent.player_name = "Alex"

    $ persistent.playercolor = "#ffffff"

    $ persistent.playercolorname = "white"
     
    #$ renpy.reload_script
    call screen main_menu
    
label resetlevels:
    
    $ persistent.set_volumes = True
       
    $ _preferences.volumes['music'] = .80

    $ _preferences.volumes['sfx'] = 1.0
    
    return
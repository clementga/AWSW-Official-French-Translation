label lorem5:

show black with dissolvemed
$ renpy.pause (0.5)

$ save_name = "Chapter 5 - Lorem"

if loremhavesphere == True:

    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow

    c "(It's time to go.)"

    c "(Oh, I still have Ipsum's Ixomen Sphere. I could give it to Lorem when I meet with them.)"
    
    menu:
        
        "Take the sphere. {image=image/ui/status/base_taken.png}{image=image/ui/status/orb_taken2.png}":

            c "(The sooner Ipsum gets it, the better.)"

            m "I took the sphere and put it in one of my pockets before I headed out to meet Lorem."
            
            $ loremgoodending = True

        "Leave it.":

            c "(It's probably not the best time to take it with me. I'll give it to Ipsum some other time.)"

            m "Having gathered my things, I headed out to meet Lorem."



    show black with dissolvemed
    $ renpy.pause (0.5)
    
    
scene viewingspot with dissolvemed

play music "mx/amb/night.ogg" fadein 5.0

m "After a few minutes of walking, I arrived at a rather empty looking area near the edge of town."

show lorem normal with dissolve

c "Hey, Lorem!"

Lo happy "Hey, [player_name]."

c "You were right. This will be much better than mingling with the crowds. I can do without all the extra noise and screaming."

Lo normal "Yeah."

if lorem4pick == "whattosay":

    Lo relieved "Listen, after what happened last time, why'd you decide to come and meet me again?"

    c "You know, I had some time to think things over. When you first told me, that came as a shock - but now, I don't think it's that big of a deal anymore. At least, it's not enough to just ignore everything else that's happened."

    Lo normal "Thank you, [player_name]."

    c "Don't worry about it."


c "So, what are we going to do now?"

Lo "Wait."

if loremgoodending == True:
    
    c "Oh, I also brought Ipsum's sphere. Maybe it can finally find its way home."

    Lo happy "Great! Would you mind holding on to it, though? I don't really have a bag or anything to put it in right now."

    c "That's alright. Just remind me to give it to you later."

    Lo normal "Sure."


Lo think "I think it's starting. Look!"

play soundloop "fx/fireworks3.ogg"

m "We were quiet as we waited and the stillness of the night enveloped us. Soon, I heard the sound of the first rocket making its way into the night sky after which it exploded in a pattern of colors."

m "More rockets followed, their thunderous noise echoing throughout the land."

show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow
$ renpy.pause (6)
#hide fireworks with dissolveslow


stop music fadeout 2.0

hide fireworks with dissolveslow

#stop music fadeout 2.0

#hide fireworks with fade

m "Suddenly, a terrible realization hit me."

play music "mx/judgement.ogg" fadein 0.5

m "Considering how public of an event this was and how I was told multiple times that everyone would be watching the fireworks, now would be the best time for Reza to do anything he planned to do."

m "Not only was the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever have."

m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."

c "Lorem, I think we need to go. Now."

Lo relieved "What's going on?"

c "I know where Reza is."

Lo think "Really?"

c "We need to stop him."

Lo relieved "We? What do you think I can do? He's twice as big as I am, and let's not forget about his weapon."

c "I can try to hold him off. You go and get help."

Lo think "Alright."

if loremgoodending == True:
    
    Lo "Wait a minute. Give me the sphere."

    c "There you go."
    
    play sound "fx/spheretake.ogg"

    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/sphereboot.ogg"

    m "I watched as Lorem took the sphere from my hands and slid their fingers over its interface in a peculiar way. After a few seconds, they were done and the sphere was back in my hands."

    Lo "It might not help you much, but if something goes wrong, just throw it at him."

    c "Alright."

    
    
Lo "Where is he, anyway?"

c "The underground building."

c "Let's go!"

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow

$ renpy.pause (3.5)

call endingjustafewminuteslater from _call_endingjustafewminuteslater_3

if loremgoodending == True:
    
    jump loremgoodending

Mv "Maybe I can."

label loremgoodending2:

play music "mx/ashes.ogg" fadein 1.0

m "Suddenly, Maverick and Lorem appeared next to me."

show reza at Position(xpos=0.9, xanchor='center') with ease

show maverick normal flip at Position(xpos=0.2, xanchor='center') with easeinleft

show lorem think flip at Position(xpos=0.1, xanchor='center') with easeinleft

Rz angry "You planned this, didn't you, [player_name]?"

#Rz "Traitor!" with Shake((0, 0, 0, 0), 2, dist=10)

Rz "Traitor!" with hpunch

if loremgoodending == False:

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
show lorem at Position(xpos=-0.3, xanchor='center')
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

show izumiinjured5 at Pan((300, 0), (600, 608), 7.0) with fade

$ renpy.pause (5.0)

hide izumiinjured5 
show maverick at Position(xpos=0.2, xanchor='center')
show lorem at Position(xpos=0.1, xanchor='center')
show reza at Position (xpos = 0.9, xanchor = 'center')
with fade

m "My first instinct was to run away, but as Maverick and Lorem started charging, so did I."

play sound "fx/snarl.ogg"
show maverick angry flip with dissolve

$ renpy.pause (1.0)

show reza gunpoint

play sound "fx/gunshots2.ogg"


show maverick at Position (xpos = 0.35)  with ease
$ renpy.pause (0.5)
show maverick at Position (xpos = 0.5)  with ease
$ renpy.pause (0.5)
hide maverick with easeoutbottom

m "Reza was quick with his aim and shot at Maverick until he went down."

play sound "fx/flapx.ogg"

show lorem at Position (xpos = 0.3, xanchor = 'center') with ease

$ renpy.pause (0.5)

play sound2 "fx/gunshot.wav"

show lorem at Position (xpos = 0.78, xanchor = 'center') with move7

play sound "fx/loremkick.ogg"

show reza gunself

$ renpy.pause (0.3)

show reza angry

hide lorem with easeoutbottom

m "Lorem took flight with a few beats of their wings and was about to collide with Reza, but at the last moment, Reza got out of the way and hit Lorem with a well-aimed kick."

show loremwounded at Pan((1080, 0), (500, 350), 6) with fade

$ renpy.pause (4.5)

hide loremwounded with fade

if loremgoodending == True:
    
    jump loremgoodending3

#m "Lorem collided roughly with the wall and fell to the ground."

play sound "fx/rev.ogg"

show reza gunself with dissolve

play sound2 "fx/boxdive.ogg"


m "In an instant, Reza was aiming at me. I quickly dove behind the box with the generator for cover - just before he pulled the trigger."

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

m "While I was unharmed, a loud hiss suddenly started emanating from the box."

m "I knew what was going to happen and quickly started running towards the exit."

stop music fadeout 1.0

scene np2y at Pan ((0, 100), (0, 100), 0.0) with fade

#explosion

play sound "fx/explosion.ogg"

$ loremdead = True

play soundloop "fx/fireworks.ogg" fadein 10

m "Just as I reached the outside, the explosion battered my ears. The shockwave sent me flying briefly before I roughly collided with the ground." with Shake((0, 0, 0, 0), 3.0, dist=30)

show np2z at Pan ((0, 100), (0, 100), 0.0) with dissolve

m "My vision blurred instantly and all control left my body as I slowly closed my eyes."

stop soundloop fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

play soundloop "fx/fireworks.ogg" fadein 10

scene np2y at Pan ((0, 100), (0, 100), 0.0) 

show reza gunself

with dissolvemed

m "I awoke to the sight of Reza aiming his gun at me."

Rz "What the heck did you do to the portal?"

c "What are you talking about? I didn't do anything."

Rz angry "Why can't I use it then? And what happened to the coordinates?"

Rz annoyed "The dragons don't know that much about the portal, so it must've been you or that girl."

play sound "fx/rev.ogg"

Rz gunself "You better give me something, or else I have no reason to let you live."

c "It was her."

Rz angry "Who is she?"

c "I don't know."

Rz annoyed "They must've sent her through after you. The only question is why."

c "You were the one who suddenly vanished. Maybe that's why they sent her."

Rz angry "I had my plan and humanity was fine with it. You must have told them something that changed their minds."

c "I haven't been in contact with them since the day I arrived here."

c "I've got nothing to do with her. I just wanted a diplomatic solution."

Rz annoyed "That was the fucking plan. You weren't supposed to know anything about what I was doing."

c "If humanity knew, why would they send her, then?"

Rz "That's what I've been asking myself. It doesn't make any sense."

c "It doesn't really matter, anyway. She is the only one who knows how to use the portal again, and now that you've killed her, we're both stuck here."

Rz "You..."

Rz "You've got something to do with this, or else you wouldn't be so fucking smug about it."

c "No, I just like seeing you fail."

Rz angry "Stop denying it!" with hpunch

Rz "You're going to fix this right now, or I'll find ways to make you talk."

c "Nothing you can do or say will change what's coming now."

Rz annoyed "What's that?"

c "Turn around."

m "Reza glanced back over his shoulder just in time to see Maverick running towards him."

play sound "fx/rev.ogg"

show reza gunpoint flip

m "He turned around, aiming his gun in Maverick's direction."


play sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/hit1.ogg"
queue sound "fx/gunshot2.wav"
#queue sound "fx/impact3.ogg"

show reza angry flip with dissolve

m "Before he could fire, I grabbed his hand in an attempt to disarm him, but in the scuffle, a shot went off and I suddenly found myself in a world of pain. I collapsed to the ground still holding the gun."

show maverick angry at Position (xpos = 1.3)

show maverick at Position(xpos=0.65, xanchor='center') with move7

play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.5, xanchor='center', ypos=1.0, yanchor="top") 
show reza at Position(xpos=0.25, xanchor='center', ypos=1.0, yanchor="top") 
with move9

m "Maverick pounced and pinned Reza to the ground with all his weight."

show maverick rage at center with dissolve

Mv "What are you going to do now, Reza?"

Mv angry "Not so strong anymore without your weapon, huh?"

scene starsrx at Pan((0, 200), (0, 0), 20.0) 
#show starsr2 at Pan((0, 200), (0, 0), 20.0) 
show starsr at Pan((0, 200), (0, 0), 20.0)
show stars at Pan((0, 200), (0, 0), 20.0) 

with dissolve

$ renpy.pause (0.5)

m "The voices faded as I watched the sky." 

hide stars with dissolveslow3

m "My vision turned red, making it look as if the stars were bathing in a sea of blood."

#hide starsr with dissolveslow

m "I resigned to my fate as I closed my eyes."

stop soundloop fadeout 4.5


hide starsr with dissolveslow

$ renpy.pause (0.5)

scene black with dissolveslow

$ renpy.pause (2.0)

nvl clear

window show

n "Reza was apprehended and taken to jail."

n "As communication between our worlds was no longer possible, humanity never learned of our fate in this timeline."

n "They had decided that if our visit did not yield any results, they would no longer try their luck with the portal and instead use their remaining energy to hold on as long as they still could."

n "It was an uphill battle that was eventually lost when the city ran out of resources and fell."

n "Reza warned the dragons of the comet and its danger, but without the generators from the underground building, their plan to redirect it ultimately failed."

stop music fadeout 2.0

#$ renpy.pause (0.3)

window hide

#scene black with dissolveslow

$ renpy.pause (2.0)

#window hide

$ renpy.pause (1.0)

$ _game_menu_screen = None

stop sound fadeout 2.0

#scene black with dissolveslow

#$ renpy.pause (2.0)

$ renpy.block_rollback()

play sound "mx/fragments.ogg" fadein 0.5

#$ renpy.pause (1.5)

show loremwounded at Pan((500, 0), (-150, 350), 20)
show credits1 at left
with dissolvemed

$ renpy.pause (7.4)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (7.4)

scene black with dissolvemed

show storex at Pan ((0,183), (960,0), 40.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (7.4)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (7.4)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show meetingipsum at Pan ((-200, 0), (-100,324), 20.0) #Position(xpos=0.75, xanchor='center')
show credits5 at left 
with dissolvemed

$ renpy.pause (7.4)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (7.4)

scene black with dissolvemed
#stop movie

#

show school at Pan ((200, 252), (700, 302), 23) #at Position(xpos=0.25, xanchor='center') at Pan((0, 0), (0, 302), 5.0)
show credits7 at right 
with dissolvemed

$ renpy.pause (7.4)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (7.4)

scene black with dissolvemed

#

show meetinglorem at Pan((90, 0), (90, 408), 20.0)
show credits9 at left 
with dissolvemed

$ renpy.pause (7.4)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (7.4)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (2.5)

stop sound fadeout 2.0

$ renpy.pause (5.0)

scene black with dissolvemed

stop sound fadeout 2.5

$ renpy.pause (4.0)

#$ persistent.anygoodending = True
$ persistent.lastendingseen = "bad"

$ persistent.endingsseen += 1

call izumimask from _call_izumimask_7

#call optimistcheck

if persistent.lorembadending == False:

    $ persistent.lorembadending = True
    
    $ achievement.grant("Remember")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_90

    $ mp.lorembadending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Lorem's bad ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "lorem"
    
    jump tut
    
else:

    jump mainmenu



label loremgoodending:
    
c "You know what? I'm not having this conversation with you again."

Rz annoyed "What are you talking about?"

c "Your plan, Reza. I know all about it."

Rz amused "Great. Then stop wasting time and help me with this."

c "I'm not here to help you. This is where it ends."

Rz annoyed "What is your problem, [player_name]? You know about the comet, so we can't stay here."

c "Just shut up, Reza. I'm not in the mood to talk with you anymore."

stop music fadeout 2.0

c "I don't need to, because your friend has just arrived."

jump loremgoodending2

label loremgoodending3:

#search for throw sound effect
    
m "Lorem collided roughly with the wall and fell to the ground. Remembering Lorem's words, I took the sphere and threw it towards Reza as hard as I could."

play sound "fx/blop.ogg"

m "At first it looked as though it was going to miss, but the sphere adjusted its path and flew straight towards him."

play sound "fx/rev.ogg"

show reza gunself with dissolve

queue sound "fx/glassimpact2.ogg"

$ renpy.pause (0.1)

queue sound "fx/impact3.ogg"

$ renpy.pause (0.4)

hide reza with easeoutbottom

m "Reza aimed at me, but the sphere hit him before he could pull the trigger. He lost his balance and stumbled backwards before he fell to the ground."

show reza angry with dissolve

m "As he got up, I saw that the barrel of his gun was now bent out of shape."

m "When he realized this, he bolted towards the exit."

play sound "fx/gunhit2.ogg"

queue sound "fx/impact3.ogg"

hide reza with easeoutleft


#$ renpy.pause (0.4)

m "I tried to stop him, but he hit me in the face with the gun's blunt end and ran past me." with vpunch

m "It took a few seconds until I composed myself and ran after him."

stop music fadeout 2.0

scene black with dissolvemed

$ renpy.pause (0.5)

scene np1r at Pan((500, 350), (500, 200), 6.0) with dissolveslow

play soundloop "fx/fireworks.ogg" fadein 10

play sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/telstart.ogg"

play music "fx/silence.ogg"
queue music "fx/silence.ogg"
queue music "fx/silence.ogg"
queue music "fx/silence.ogg"
queue music "fx/silence.ogg"
queue music "fx/silence.ogg"
queue music "fx/silence.ogg"
queue music "fx/silence.ogg"
queue music "fx/silence.ogg"
queue music "fx/wooshes.ogg"

m "As I went up the hill, I saw that Reza was already taking his place while the Portal did its starting routine."

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/telbuttons.ogg"

m "I ran up to the console and entered a few commands. Reza turned around and saw me."

show reza angry with dissolve

Rz "What are you doing?" with vpunch

play sound "fx/run.ogg"

$ renpy.pause (1.5)

queue sound "fx/impact3.ogg"

show remy normal at Position (xpos = -1.0) with vpunch

hide reza with easeoutbottom

m "Reza walked off the platform, but I quickly ran around the console and threw my weight against him, just in time for the portal to start teleporting us." #with vpunch

play sound "fx/telstart.ogg"

stop music fadeout 2.0

$ renpy.pause (3.0)

stop soundloop fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

nvl clear

window show

n "Lorem lived to tell the police what had transpired in the underground building."

n "The conversation they had overheard was enough for the dragons to find out about the comet, and with the help of the portal's power source, they were able to divert it."

n "As neither humanity nor the dragons knew where Reza and I ended up, our visit was considered a failure."

n "Humanity had decided that if our visit did not yield any results, they would no longer try their luck with the portal and instead use their remaining energy to hold on as long as they still could."

n "For the dragons, life went on as usual - but for our city, this outcome meant they had to continue their fight on their own."

n "It was an uphill battle that was eventually lost when the city ran out of resources and fell."

stop music fadeout 2.0

window hide

#scene black with dissolveslow

$ renpy.pause (2.0)

#window hide

$ renpy.pause (1.0)

$ _game_menu_screen = None

stop sound fadeout 2.0

$ renpy.block_rollback()

#scene black with dissolveslow

#play sound "fx/silence.ogg"
#queue sound "fx/silence.ogg"
play sound "mx/nostalgia.ogg" #fadein 0.2

#$ renpy.pause (1.5)

show izumidead5 at Pan((-450, 400), (400, 508), 25.0) #lorem cg
show credits1 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show loremsphere at Pan ((250, 326), (750,0), 24.0) #lorem with orb cg
show credits3 at right 
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show meetingipsum at Pan ((-200, 0), (-100,324), 25) #Position(xpos=0.75, xanchor='center')
show credits5 at left 
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed
#stop movie

#

show school at Pan ((200, 252), (700, 302), 25) #at Position(xpos=0.25, xanchor='center') at Pan((0, 0), (0, 302), 5.0)
show credits7 at right 
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

#

show meetinglorem at Pan((90, 0), (90, 408), 25.0)
show credits9 at left 
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (9.5)

stop sound fadeout 1.5

$ renpy.pause (1.0)

scene black with dissolvemed

stop sound fadeout 2.5

$ renpy.pause (5.0)

play sound "fx/telstart.ogg"

$ renpy.pause (7.0)

scene np1r at Pan((500, 150), (500, 150), 6.0) with dissolveslow

$ renpy.pause (0.5)

play music "mx/amb/night.ogg" fadein 5.0

$ renpy.pause (0.5)

m "We reappeared on the other side and collapsed to the ground. It was the day of my arrival in the dragons' world, just as I had planned."

show reza annoyed flip at Position (xpos = 0.2) with easeinbottom 

Rz "What the fuck is going on here?"

show izumi normal 3 at Position (xpos = 0.8) with easeinright

Iz "Oh, look at what the cat dragged in."

Rz angry flip "You're supposed to be dead."

Iz "Am I, now?"

Iz "You're right. But today is not the day."

show izumi at Position (xpos = 0.63) with ease

$ renpy.pause (0.2)

show izumi at Position (xpos = 0.46) with ease

$ renpy.pause (0.2)

show izumi at Position (xpos = 0.3) with ease

$ renpy.pause (0.2)

play sound "fx/gnarlypunch.ogg"

$ renpy.pause (0.5)

hide reza with easeoutbottom

m "She held up Reza's head and punched him. His body instantly went limp as he fell unconscious."

$ renpy.pause (0.3)

show izumi normal 3 flip

$ renpy.pause (0.3)

Iz "Good job, [player_name]."

Iz "Oh, is that yours?"

m "She pointed at an object on the ground behind me."

m "When I turned around, I realized that it was the Ixomen Sphere. Whatever setting Lorem activated had apparently prompted it to follow us, even through the portal."

c "Not exactly."

Iz "You better hold on to it regardless. Those things are expensive."

show izumi at Position (xpos = 0.40) with ease

$ renpy.pause (0.3)

show izumi normal 3

$ renpy.pause (0.3)

play sound "fx/liftbody.ogg"

m "She walked over to Reza's lower half and started lifting him by the legs."

Iz "Come on and help me with this. We've got a long night ahead of us."

stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolveslow

$ renpy.pause (4.0)


$ persistent.anygoodending = True
$ persistent.lastendingseen = "good"

$ persistent.endingsseen += 1

call izumimask from _call_izumimask_8

#call optimistcheck

if persistent.loremgoodending == False:

    $ persistent.loremgoodending = True
    
    $ achievement.grant("The Plan")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_91

    $ mp.loremgoodending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Lorem's good ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "lorem"
    
    jump tut
    
else:

    jump mainmenu

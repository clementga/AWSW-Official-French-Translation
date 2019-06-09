label chapter5:

if persistent.loremgoodending == False:
    if lorem3unplayed == True:
        $ loremdead = True
        
if persistent.adinegoodending == False:
    if adine4unplayed == True:
        if remygoodending == False:
            $ adinedead = True

if persistent.remygoodending == False:
    if remystatus == "bad":
        $ remydead = True
        
    elif remystatus == "abandoned":
        $ remydead = True

scene black with dissolveslow

$_dismiss_pause = False

$ _game_menu_screen = None

$ renpy.pause(1.3)

play sound "fx/chapter5.ogg"

$ save_name = "Chapter 5"

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

if persistent.sebastianfail == True:
    
    scene chap5 at Pan((0, 0), (0, 0), 6.0) with dissolveslow

else:
    
    scene chap5x at Pan((0, 0), (0, 0), 6.0) with dissolveslow

$ carddisplayed = False

if persistent.trueending:

    show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardenlightenment = True
    $ lastcard = "cenlightenment"
    $ carddisplayed = True

elif trueselectable == True:
    
    show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardenlightenment = True
    $ lastcard = "cenlightenment"
    $ carddisplayed = True
    
elif persistent.endingsseen == 0:
    
    show cconflict at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardconflict = True
    $ lastcard = "cconflict"
    $ carddisplayed = True


if carddisplayed == False:
    
    if remygoodending == True:
        
        if remy4unplayed == False:
    
            show chope at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardhope = True
            
            $ renpy.pause (0.5)
            
            show cgrief at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardgrief = True
            $ lastcard = "cgrief"
            $ carddisplayed = True
            $ chopedisplayed = True
        
    if annagoodending == True:

        if remy4unplayed == False:
        
            if chopedisplayed == True:

                $ renpy.pause (0.5)
                
                show cpassion at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardpassion = True
                $ lastcard = "cpassion"
                $ carddisplayed = True
                $ chopedisplayed = True
                
            else:
                
                show chope at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardhope = True

                $ renpy.pause (0.5)

                show cpassion at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardpassion = True
                $ lastcard = "cpassion"
                $ carddisplayed = True
                $ chopedisplayed = True
            
    if loremhavesphere == True:
        
        if lorem4unplayed == False:
        
            if chopedisplayed == True:

                $ renpy.pause (0.5)
                
                show clorem at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardlorem = True
                $ lastcard = "clorem"
                $ carddisplayed = True
                $ chopedisplayed = True
                
            else:
                
                show chope at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardhope = True

                $ renpy.pause (0.5)

                show clorem at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardlorem = True
                $ lastcard = "clorem"
                $ carddisplayed = True
                $ chopedisplayed = True

    if brycegoodending == True:

        if bryce4unplayed == False:
        
            if chopedisplayed == True:

                $ renpy.pause (0.5)
                
                show cleadership at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardleadership = True
                $ lastcard = "cleadership"
                $ carddisplayed = True
                $ chopedisplayed = True
                
            else:
                
                show chope at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardhope = True

                $ renpy.pause (0.5)

                show cleadership at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardleadership = True
                $ lastcard = "cleadership"
                $ carddisplayed = True
                $ chopedisplayed = True

    if adinegoodending == True:

        if adine4unplayed == False:
        
            if chopedisplayed == True:

                $ renpy.pause (0.5)
                
                show csuperstition at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardsuperstition = True
                $ lastcard = "csuperstition"
                $ carddisplayed = True
                $ chopedisplayed = True
                
            else:
                
                show chope at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardhope = True

                $ renpy.pause (0.5)

                show csuperstition at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                $ cardsuperstition = True
                $ lastcard = "csuperstition"
                $ carddisplayed = True
                $ chopedisplayed = True
    

$ evilpoints += 15
$ evilpoints -= totalinv

if remystatus == "bad":
    
    $ evilpoints += 2

if annastatus == "bad":
    
    $ evilpoints += 2

if brycestatus == "bad":
    
    $ evilpoints += 2

if adinestatus == "bad":
    
    $ evilpoints += 2

if loremstatus == "bad":
    
    $ evilpoints += 2


if carddisplayed == False:

    if evilpoints >= 30:
        
        show cpride at Pan((100, 0), (0, 0), 2.0) with dissolveslow
        $ cardpride = True
        $ lastcard = "cpride"
        $ carddisplayed = True
            

if carddisplayed == False:
    
    show cduty at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardduty = True
    $ lastcard = "cduty"
    $ carddisplayed = True


show text5 with dissolveslow


if sebastiansaved == False:
    scene chap5 at Pan((0, 120), (0, 360), 7.0) 
    
else:
    scene chap5x at Pan((0, 120), (0, 360), 7.0) 
    

    
    
#show card1 at Pan((0, 0), (0, 0), 0.1)

if lastcard == "cenlightenment":

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show cenlightenment at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show cenlightenment at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow


elif lastcard == "cconflict":

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show cconflict at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show cconflict at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow

elif lastcard == "cgrief":

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show cgrief at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show cgrief at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow


elif lastcard == "cpassion":

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show cpassion at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show cpassion at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
        
        
elif lastcard == "clorem":

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show clorem at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show clorem at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
        
        
elif lastcard == "cleadership":

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show cleadership at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show cleadership at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow


elif lastcard == "csuperstition":

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show csuperstition at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show csuperstition at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
        

elif lastcard == "cpride":

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show cpride at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show cpride at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow


else:

    if sebastiansaved == False:
        
        scene chap5 at Pan((0, 120), (0, 360), 7.0) 
        show cduty at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow
    
    else:
        
        scene chap5x at Pan((0, 120), (0, 360), 7.0) 
        show cduty at Pan((0, 0), (0, 0), 0.1)
        show text5
        with dissolveslow



play soundloop "fx/fireworks2.ogg"

$ renpy.pause(4.0)

stop sound fadeout 2.0

scene black with dissolveslow

#$_dismiss_pause = True

$ renpy.pause(2.0)

stop soundloop fadeout 2.0

$ renpy.pause(2.0)

$ _game_menu_screen = "navigation"

nvl clear

scene o4 at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause(3.0)

$ save_name = "Chapter 5"

$ chapter5unplayed = False

m "After a night of turbulent dreams, my consciousness returned to the shores of the waking world."

c "(Today is the day of the big fireworks. Who shall I bring?)"

$ loremavailable = False

if lorem4unplayed == False:
    
    if loremstatus == "neutral":
        
        $ loremavailable = True
    
    if loremstatus == "good":

        $ loremavailable = True
                
#insert script to make selectable here

menu:
    
    "Remy." if remy4unplayed == False:

        $ endingselect = "remy"

        jump remy5

    "Anna." if anna4unplayed == False:

        $ endingselect = "anna"

        jump anna5
        
    "Lorem." if loremavailable:

        $ endingselect = "lorem"

        jump lorem5

    "Bryce." if bryce4unplayed == False:

        $ endingselect = "bryce"

        jump bryce5

    "Adine." if adine4unplayed == False:

        $ endingselect = "adine"

        jump adine5


    "Go alone.":

        $ endingselect = "alone"

        jump aloneendings
        
    "Everyone." if trueselectable:

        jump trueendings

label aloneendings:

$ save_name = "Chapter 5 - Alone"

m "While I was sure any of those I knew would agree to watch the fireworks with me if I asked, I ultimately decided to go alone, not wanting to impose on anyone if they hadn't asked me first."

m "After making some preparations for the day, I set out to experience these fireworks I had heard so much about."

scene black with dissolvemed
$ renpy.pause (0.5)
scene np5e with dissolvemed

play music "mx/amb/night.ogg" fadein 5.0

m "When I left my apartment, I realized just how eerily deserted the rest of the place felt. They really weren't kidding when they said {i}everyone{/i} would watch the fireworks. I imagined there were a couple of designated places people gathered for this purpose. I had no doubt they were crowded beyond belief."

m "While I waited for the fireworks to start, I looked at the area around me. With no soul in sight, I realized I hadn't actually spent many nights outside and was reminded of the day I had arrived here at my apartment in total darkness, with only Remy by my side."

play soundloop "fx/fireworks3.ogg"

m "Soon, the total stillness was broken with the sound of the first rocket ascending, its explosion painting a circular pattern in the sky."

m "More rockets followed, their quantity and frequency steadily increasing."

show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow
$ renpy.pause (6)
#hide fireworks with dissolveslow


stop music fadeout 2.0

hide fireworks with dissolveslow

m "As the explosions battered my ears, a terrible realization hit me."

play music "mx/judgement.ogg" fadein 0.5

m "Considering how public of an event this was and how everyone would be watching the fireworks, now would be the best time for Reza to make his move."

m "Not only was the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever have."

m "As the portal had been repaired by the Administrator, Reza would have no trouble making his getaway, and I was the only one who knew."

m "I ran to my apartment and briefly considered calling the police as I grabbed a few things. However, I soon remembered that they were not only already understaffed, but that I might waste precious time if I tried to do so."

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow

$ renpy.pause (3.5)

#call function here

call endingjustafewminuteslater from _call_endingjustafewminuteslater

#end function here

if evilending == True:
    jump mainmenu

c "Actually, I can."

play music "mx/confrontation.ogg" fadein 0.5

m "I opened the cloak I was wearing to reveal an improvised bomb I had made from a generator."

Rz angry "What is this?"

c "You showed me how to do it, with the little trap you set at the farmhouse."

Rz "That... wasn't intended for you."

c "It doesn't matter. You set it for someone. You set it to kill."

Rz annoyed "Where'd you even get a generator?"

c "After the police reclaimed the generators you stole, it was easy for me to take one when I was alone in the department, just in case."

m "I set the bomb on the ground between us. With it and me between Reza and the exit, he would have to listen now."

Rz "So, what's the plan?"

c "I'll tell you what's going to happen. You leave the generator and turn yourself in."

Rz angry "You know what? I think you're bluffing. If you set off that bomb, not only do we both die, but you destroy the generators as well - and with them, any chance of saving either world. You would never do that."

play sound "fx/rev.ogg"

show reza gunself with dissolve

m "He pulled out his gun and pointed it at me as he slowly started closing the distance between us."

Rz "What is it going to be, [player_name]? Killing all of us, or just this world?"

m "Reza was right. In reality, the bomb provided no real leverage against him. If his goal was truly to save our city back home at any costs, he would not turn himself in. Even if the threat of setting off the bomb was a real one, his best chance would be to at least try to kill me now."

m "I turned around and started running."

hide reza with dissolve

Rz "No!" with hpunch

play sound "fx/gunshots2.ogg"

m "I heard gunshots. Immediately I felt the most excruciating pain I’ve ever experienced resonate through my arm. As I kept sprinting as fast as I could, I heard a beeping sound that made me realize I had inadvertently activated the bomb when I was hit."

play sound "fx/beeps.ogg"

m "Out of bullets, Reza was not far behind me as we both scrambled towards the exit." 

stop music fadeout 1.0

scene np2y at Pan ((0, 100), (0, 100), 0.0) with fade

play sound "fx/beeps2.ogg"

$ renpy.pause (1.0)

#explosion

queue sound "fx/explosion.ogg"

m "Just as I reached the outside, the bomb went off. The explosion battered my ears as the shockwave sent me flying."

m "I collided with the ground and immediately felt a hail of debris. I cowered, waiting for it to die down."

play soundloop "fx/fireworks3.ogg" fadein 3

m "After a few seconds, I turned around and looked at the sky where the fireworks still painted patterns in the stars. With one hand, I reached toward my injured arm only to find it wet with blood from my bullet wound. My whole body was numb."

m "But I could not give up now. I slowly got up, looking around the area to get some perspective of the situation. Not far from where I was, I saw Reza lying on the ground. He wasn't moving."

show rezadeadexplosion at Pan ((0, 326), (580, 126), 10.0) with fade

$ renpy.pause (5.0)

m "As I got closer, I spotted the gun next to him."

c "I won't let them find this."

hide rezadeadexplosion with fade

m "I took it with me, hiding it in one of my pockets as I started making my way towards the portal with slow and uneasy steps."

show np2z at Pan ((0, 100), (0, 100), 0.0) with dissolveslow

m "I was shaking and my vision was blurry. Every inch of movement felt like a new and harder chore than the last."

play sound "fx/impact.wav"

m "Eventually, my legs gave in and I collapsed to the ground."# with vpunch

show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow
$ renpy.pause (3)
#hide fireworks with dissolveslow


#stop music fadeout 2.0

#hide fireworks with dissolveslow

m "I resigned to my fate as I watched the night sky, illuminated by the colorful explosions of the fireworks."

#$ renpy.pause (3)

show black with dissolveslow

$ renpy.pause (1.0)

scene np2y at Pan ((0, 100), (0, 100), 0.0) with dissolvemed

m "Suddenly, I was lifted off the ground and as I opened my eyes, I saw the masked face of the Administrator."

show izumi normal with dissolve

c "I just could not let it happen. I had to stop him. I had to try... somehow."

m "The Administrator started moving, carrying me."

As "Unfortunately, it seems like the generators were destroyed as well."

c "So this is how it ends? With humanity doomed to fade into history, and the dragons facing extinction?"

As "All hope is not lost. It never was."

c "What are you going to do?"

As "I'm going to send you back in time. We'll just try again, and maybe we'll do better next time."

scene np1r at Pan((500, 150), (500, 150), 6.0) with dissolvemed

m "By now, we had arrived at the portal. The Administrator gently set me down before moving towards the portal's controls."

show izumi normal with dissolve

#As "I'm glad you didn't try to put the bomb at the portal to stop Reza, or else we'd be in real trouble."

#c "You told me the portal was our greatest asset. That's why I didn't do it."

#As "I know."

#c "What's going to happen now?"

As "You will probably forget most of what happened. The teleportation tends to do that sometimes, especially when someone is transported several times in quick succession."

As "Maybe you'll remember a thing or two, and maybe they'll help you do better next time."

c "Maybe."

stop soundloop fadeout 2.0

As "I'll see you on the other side."

$ _game_menu_screen = None

scene black with dissolveslow

nvl clear

window show

$ renpy.show("port1")
$ renpy.transition(Dissolve(2))

#play sound "fx/telstart.ogg"
play sound "fx/tel.wav"

n "{cps=40}I heard the sound of the portal starting to do its work as the numbness and pain suddenly left my body.{/cps}{nw}"

scene port2 with dissolve
scene port1 with dissolve
scene port2 with dissolve
scene port1 with dissolve

n "{cps=46}Things I had experienced and things I hadn't flashed across my mind as I was teleported.{/cps}{nw}"

scene port2 with dissolve
scene port1 with dissolve
scene port2 with dissolve
scene port1 with dissolve

n "{cps=40}I felt free.{/cps}{nw}"

$ renpy.pause (1.3)

scene port2 with dissolve
scene port1 with dissolve
scene port2 with dissolve
scene port1 with dissolve
#scene port2 with dissolve

$ renpy.pause (2.0)

stop sound fadeout 2.0

scene black with dissolveslow

window hide# with dissolveslow

$ renpy.pause (2.0)

$ renpy.block_rollback()

play music "mx/confrontation.ogg"

$ renpy.pause (2.0)

#2,1 rezadeadexplosion
#explosion 4,3
#6,5 sun
#meeting otomo, 8, 7
#10, 9 portal left
#logo at the end
#at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='bottom')
show rezadeadexplosion at Pan ((580, 0), (-580, 326), 24.0)
show credits1 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show portalb at Pan ((540, 0), (1400, 380), 24.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

play movie "cg/chap3/sun2.ogv" loop

show movie at Position(xpos=0.75, xanchor='center')
show credits5 at left 
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed
stop movie

#

show cgmeeting at Pan ((740, 608), (1240, 0), 24)
show credits7 at right 
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

#

show np1r at Pan((0, 350), (350, 100), 24.0)
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

$ renpy.pause (4.0)

$ persistent.lastendingseen = "bad"

$ persistent.endingsseen += 1

if persistent.neutralending == False:

    $ persistent.neutralending = True
    
    $ achievement.grant("Detonation")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_27
    
    $ mp.neutralending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen the neutral ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "alone"
    
    jump tut
    
else:

    jump mainmenu


label tut:

    play sound "fx/system3.wav"

    s "You experienced just one of the many different endings of {i}Angels with Scaly Wings{/i}."

    play sound "fx/system3.wav"

    s "In order to see the story's conclusion, you will have to play through the game a number of times."

    play sound "fx/system3.wav"

    s "During the next playthrough, you may want to make different choices. You may even find the information you've gained this time to be helpful!" 
    
    play sound "fx/system3.wav"
    
    s "Sometimes, you might even notice that prior choices have changed a character or aspect of the game's world permanently."

    play sound "fx/system3.wav"

    s "At any rate, feel free to employ the game's skip buttons (CTRL and TAB) generously, as - by default - they will only skip text that you have already seen, making subsequent playthroughs much more palatable."

    play sound "fx/system3.wav"

    s "Can you find all the different endings?"
    
    $ persistent.playercolor = playercolor
    $ persistent.player_name = player_name
    
    $ persistent.firstending = True
            
    $ achievement.grant("It begins")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_28
    
    play sound "fx/system.wav"
    
    s "You have seen your first ending!"

    $ renpy.pause (2.0)

    jump mainmenu
    
label mainmenu:

    #$ persistent.brycesurvives = False

    $ mp.achievements = persistent.achievemenets
    $ mp.save()
    
    $ _game_menu_screen = "navigation"
        
#After knowing of their origins, is a dragon like Adine a dinosaur? Technically, no. The word Dinosaur only describes species of the clade "Dinosauria", which is further divided into groups like Ornithischia and Saurischia, which only describes certain land-dwelling species. For example, the Pteranodon is not a Dinosaur, but actually a Pterosaur, which is a different order. Most interestingly, though, birds are actually descended from dinosaurs, and not pterosaurs, which evolved flight much earlier.

#Though we often think mammals are the most successful animals on earth, more than 97 percent of animals are invertebrates, those without backbones.
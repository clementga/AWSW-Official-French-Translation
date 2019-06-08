label chapter4:

#determine if loss will be displayed at all

if persistent.remygoodending == False:
    
    if remystatus == "bad":
        
        $ c4displayloss = True
        $ c4displayremy = True
        $ c4displaycharacters += 1

        $ mp.remyloss = True
        $ mp.save()

if persistent.annagoodending == False:

    if annasurvives == False:
        
        $ c4displayloss = True
        $ c4displayanna = True
        $ c4displaycharacters += 1

        $ mp.annaloss = True
        $ mp.save()
    
if persistent.loremgoodending == False:
    
    if loremstatus == "bad":
        
        
        $ c4displayloss = True
        $ c4displaylorem = True
        $ c4displaycharacters += 1
        $ loremdead = True

        $ mp.loremloss = True
        $ mp.save()


    elif loremstatus == "none":
        
        $ c4displayloss = True
        $ c4displaylorem = True
        $ c4displaycharacters += 1
        $ loremdead = True

        $ mp.loremloss = True
        $ mp.save()
        
    elif loremstatus == "abandoned":
        
        $ c4displayloss = True
        $ c4displaylorem = True
        $ c4displaycharacters += 1
        $ loremdead = True

        $ mp.loremloss = True
        $ mp.save()

    
if persistent.brycegoodending == False:
    
    if totalinv <= 6:

        $ c4displayloss = True
        $ c4displaybryce = True
        $ c4displaycharacters += 1
        
    elif persistent.brycedies == True:
        
        if persistent.brycekey1 == True:
            
            if persistent.brycekey2 == True:
                
                if persistent.brycekey3 == True:
                    
                    pass
                    
                else:
                    
                    $ c4displayloss = True
                    $ c4displaybryce = True
                    $ c4displaycharacters += 1

                    $ mp.bryceloss = True
                    $ mp.save()
                    
            else:
                
                $ c4displayloss = True
                $ c4displaybryce = True
                $ c4displaycharacters += 1

                $ mp.bryceloss = True
                $ mp.save()
                
        else:
            
            $ c4displayloss = True
            $ c4displaybryce = True
            $ c4displaycharacters += 1

            $ mp.bryceloss = True
            $ mp.save()
    

if persistent.adinegoodending == False:
    
    if adinestatus == "bad":
        
        $ c4displayloss = True
        $ c4displayadine = True
        $ c4displaycharacters += 1

        $ mp.adineloss = True
        $ mp.save()

    elif adine2unplayed == True:
        
        $ c4displayloss = True
        $ c4displayadine = True
        $ c4displaycharacters += 1

        $ mp.adineloss = "yes"
        $ mp.save()



scene black with dissolveslow

$_dismiss_pause = False

$ _game_menu_screen = None

$ renpy.pause(1.3)

play sound "fx/chapter4.ogg"

$ save_name = "Chapter 4"

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

scene chap4 at Pan((0, 0), (0, 0), 6.0) with dissolveslow

#show card1 at Pan((100, 0), (0, 0), 2.0) with dissolveslow
$ carddisplayed = False

if persistent.trueending == True:
    
    show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardenlightenment = True
    $ lastcard = "cenlightenment"
    $ carddisplayed = True
    
elif trueselectable == True:

    show cenlightenment at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardenlightenment = True
    $ lastcard = "cenlightenment"
    $ carddisplayed = True

if carddisplayed == False:
    
    if c4displayremy == False:
        if c4displayanna == False:
            if c4displaylorem == False:
                if c4displaybryce == False:
                    if c4displayadine == False:
                        $ c4displayloss = False
                        show chope at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                        $ cardhope = True
                        $ lastcard = "chope"
                        $ carddisplayed = True

if carddisplayed == False:

    if c4displayremy == True:
        if c4displayanna == True:
            if c4displaylorem == True:
                if c4displaybryce == True:
                    if c4displayadine == True:
                        $ c4displayloss = False
                        show cpride at Pan((100, 0), (0, 0), 2.0) with dissolveslow
                        $ cardpride = True
                        $ lastcard = "cpride"
                        $ carddisplayed = True


if carddisplayed == False:

    if c4displaycharacters >= 3:
        
        show closs at Pan((100, 0), (0, 0), 2.0) with dissolveslow
        $ cardloss = True
        $ lastcard = "closs"
        $ carddisplayed = True
        

    else:
    
        
        show closs at Pan((100, 0), (0, 0), 2.0) with dissolveslow
        $ cardloss = True
        $ carddisplayed = True

        if c4displayremy == True:
            
            $ renpy.pause (0.5)
            show cgrief at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardgrief = True
            $ lastcard = "cgrief"

        if c4displayanna == True:
            
            $ renpy.pause (0.5)
            show cpassion at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardpassion = True
            $ lastcard = "cpassion"

        if c4displaylorem == True:
            
            $ renpy.pause (0.5)
            show clorem at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardlorem = True
            $ lastcard = "clorem"
            
        if c4displaybryce == True:
            
            $ renpy.pause (0.5)
            show cleadership at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardleadership = True
            $ lastcard = "cleadership"
            
        if c4displayadine == True:
            
            $ renpy.pause (0.5)
            show csuperstition at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardsuperstition = True
            $ lastcard = "csuperstition"
            



show text4 with dissolveslow

#play soundloop "fx/chap4tr2.ogg" fadein 3.0

if lastcard == "cenlightenment":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show cenlightenment at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow

elif lastcard == "cenlightenment":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show cenlightenment at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow

elif lastcard == "chope":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show chope at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow

elif lastcard == "cpride":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show cpride at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow

elif lastcard == "cgrief":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show cgrief at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow
    
elif lastcard == "cpassion":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show cpassion at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow
    
elif lastcard == "clorem":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show clorem at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow
    
elif lastcard == "cleadership":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show cleadership at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow

elif lastcard == "csuperstition":

    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show csuperstition at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow
    
else:
    
    scene chap4 at Pan((0, 120), (0, 360), 7.0) 
    show closs at Pan((0, 0), (0, 0), 0.1)
    show text4
    with dissolveslow

play soundloop "fx/chap4tr2.ogg"

$ renpy.pause(4.0)

stop sound fadeout 2.0

scene black with dissolveslow

#$_dismiss_pause = True

$ renpy.pause(2.0)

stop soundloop fadeout 2.0

$ renpy.pause(2.0)

$ _game_menu_screen = "navigation"

nvl clear

scene o at Pan((0, 0), (0, 250), 5.0) with dissolveslow
$ renpy.pause(3.0)

$ chapter4unplayed = False

#the abandoned script needs two cases - one where 2 was played/good and 3 skipped to culminate in being abandoned in 4
#and another one, where 1 was played in chapter2 and 2 was skipped in 3 to culminate in being abandoned here.

#turn it around so we check first if she was picked in 2 - then if she is still good?
#if adine is good, was picked in 2 but not 3 then it turns bad?

if adinestatus == "good":
    
    if chap2picka == "adine":
        
        if chap3picka == "adine":
            
            pass
            
        elif chap3pickb == "adine":
            
            pass

        else:
            
            $ adinestatus = "abandoned"
        
    elif chap2pickb == "adine":
        
        if chap3picka == "adine":
            
            pass
            
        elif chap3pickb == "adine":
            
            pass
            
        else:
            
            $ adinestatus = "abandoned"
        
    else:
        
        pass

if annastatus == "good":
    
    if chap2picka == "anna":
        
        if chap3picka == "anna":
            
            pass
            
        elif chap3pickb == "anna":
            
            pass

        else:
            
            $ annastatus = "abandoned"
        
    elif chap2pickb == "anna":
        
        if chap3picka == "anna":
            
            pass
            
        elif chap3pickb == "anna":
            
            pass
            
        else:
            
            $ annastatus = "abandoned"
        
    else:
        
        pass

if brycestatus == "good":
    
    if chap2picka == "bryce":
        
        if chap3picka == "bryce":
            
            pass
            
        elif chap3pickb == "bryce":
            
            pass

        else:
            
            $ brycestatus = "abandoned"
        
    elif chap2pickb == "bryce":
        
        if chap3picka == "bryce":
            
            pass
            
        elif chap3pickb == "bryce":
            
            pass
            
        else:
            
            $ brycestatus = "abandoned"
        
    else:
        
        pass

if remystatus == "good":
    
    if chap2picka == "remy":
        
        if chap3picka == "remy":
            
            pass
            
        elif chap3pickb == "remy":
            
            pass

        else:
            
            $ remystatus = "abandoned"
        
    elif chap2pickb == "remy":
        
        if chap3picka == "remy":
            
            pass
            
        elif chap3pickb == "remy":
            
            pass
            
        else:
            
            $ remystatus = "abandoned"
        
    else:
        
        pass

if loremstatus == "good":
    
    if chap2picka == "lorem":
        
        if chap3picka == "lorem":
            
            pass
            
        elif chap3pickb == "lorem":
            
            pass

        else:
            
            $ loremstatus = "abandoned"
        
    elif chap2pickb == "lorem":
        
        if chap3picka == "lorem":
            
            pass
            
        elif chap3pickb == "lorem":
            
            pass
            
        else:
            
            $ loremstatus = "abandoned"
        
    else:
        
        pass





nvl clear

if persistent.brycedies == True:
    $ persistent.brycekey4 = True

play music "mx/basicguitar2.ogg"

$ popularnumber = 0

m "I awoke with my eyes fixed on the ceiling wallpaper. A sense of dread lingered from a nightmare I no longer remembered."
 
m "How many more times would I see this apartment before I returned to my own world? Or... before something happened to me?"

m "I got ready for the day, and tried to shake off those thoughts."
               
play sound "fx/door/doorbell.wav"

$ renpy.pause (1.5)

stop sound fadeout 0.5

window hide

play sound "fx/door/handle.wav"

$ renpy.pause (1.5)

nvl clear

show sebastian normal b with dissolve

Sb "Hey, [player_name]."

c "And right on the minute. You show up at this time every day, like clockwork."

Sb smile b "Clocks are reliable, and reliable is good in this line of work."

if blood == True:
    
    if anna2unplayed == True:
        
        Sb normal b "I've got something for you."
        
        c "An envelope from the facility."
        
        play sound "fx/envelope.wav"
        
        $ renpy.pause (0.5)

        c "(Oh, these are the results from the tests Anna ran on my blood.)"

        if annadead == True:
            
            c "(She must have sent this before she was...)"
            
            c "(No, it's no use thinking about that now. Maybe the test results will be able to help us.)"
            
        else:
            
            pass
        
        c "(Let's see... remarkable similarities in genetic makeup, particularly the brain structure...)"
        
        play sound "fx/throat_clear.ogg"
        
        Sb disapproval b "..."
        
        c "Oh, I suppose this isn't the only reason you're here."
        
        $ gotresultsviapost = True
        
        $ persistent.gotresultsviapost = True
        
        $ persistent.havetestresults = True
        
        show sebastian normal b with dissolve
        
        jump c4resultscontinue
        

Sb normal b "I think you can guess why I'm here."

c "Is it Reza again? What happened this time?"

label c4resultscontinue:

Sb "The chief will explain everything once we get there. Let's not keep him waiting, shall we?"

stop music fadeout 2.0

play sound "fx/steps/clean2.wav"

scene black with dissolvemed
$ renpy.pause (1.0)
scene hatchery at Pan ((0, 0), (0, 360), 5.0) with dissolveslow

$ renpy.pause (3.3)



if persistent.c4skip == True:

    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_73

    call skiptut from _call_skiptut_20
        
    if skipbeginning == False:

        if system == "normal":
        
            s "My records indicate you have already experienced this scene in a satisfactory manner. Would you like to skip ahead a bit?"
        
            #play sound "fx/system3.wav" #was already blanked out here
        
            #s "Warning: In this scene, skipping ahead this way instead of using the skip buttons (CTRL and TAB) may prevent you from experiencing alternative choices and outcomes that you haven't seen before. These may only be minor, though."
        
        elif system == "advanced":

            s "It looks like you've seen this before. Skip ahead a bit?"
        
            #play sound "fx/system3.wav" #was already blanked out here
        
            #s "I have to warn you, though. If you do this here instead of just using CTRL and TAB, you may end up missing some minor changes you haven't seen before."
            
        else:
            
            s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip ahead a bit."
            
            #play sound "fx/system3.wav" #was already blanked out here
            
            #s "If you want to do things this way instead of just using the skip buttons like a civilized person, you could end up missing some choices you haven't made before. But considering how far you've come, you probably won't miss much."
            
        
    $ skipbeginning = False
    
    menu:
        
        "Yes. I want to skip ahead.":
            
            play sound "fx/system3.wav"
            
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            
            scene black with dissolvemed

            $ renpy.pause (1.0)
            
            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_20
            
            scene office at Pan ((0, 250), (0, 250), 3.0) 

            show bryce stern b at right

            show sebastian normal b at Position(xpos = 0.85)

            show maverick normal flip at Position(xpos = 0.1)

            with dissolveslow

            play music "mx/intrigue.ogg" fadein 2.0
            
            nvl clear
            
            jump c4skip1
            
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"




play music "mx/threat.ogg"

m "We arrived at a place that would look like an ordinary house, had it not been for its extraordinary size. It reminded me more of a hostel than a family home."

show sebastian normal b flip at left with easeinleft

Sb "Chief!"

show bryce brow b at right with easeinright

Br "There you are."

c "Wait. Weren't you supposed to be with Emera?"

Br "Luckily, she doesn't work every day of the week."

c "I see."

Br stern b "Anyway, we're nearly done here, so I'll keep it short: Reza broke into the hatchery." 

Br "There is another murder victim, an employee of the hatchery who was on night duty. Her body was found quite a way from here. There's evidence of a struggle, but she covered a lot of distance before it was ultimately over."

Br "Loud bangs were heard from the area her body was found, and she has numerous wounds consistent with both the wounds of the previous victims and that other weapon he has."

m "By this point, news of another corpse didn't have the same impact anymore. She was just another one of Reza's faceless victims."

c "A hatchery? Is that what this building is?"

Sb "Well, not only. It's a council-owned building, and they like keeping everything related to their sector under the same roof."

Sb "So, besides the hatchery, there's also an orphanage and a family clinic inside. There are also offices related to the administration of those services."

c "That reminds me of the production facility."

Sb "It should. They have a similar management structure."

Br brow b "Can we get back to the case?"

Sb shy b flip "Sorry for the interruption, Chief."

show sebastian normal b flip with dissolve

c "Wait a minute, if an orphanage is in there, too..."

Br stern b "There are no other casualties, but Reza got something else when he broke in: A generator, as well as a few eggs."

Br "Luckily, the power was restored before anything happened to all the other eggs left inside, but needless to say, the parents of the stolen eggs are not going to be happy."

c "Why would he steal eggs in the first place?"

Br brow b "Maybe you can tell us. That's why you're here, after all."

c "I don't know. I have no idea what he would even do with them."

Sb "Maybe he wants to use them as a bargaining chip. After all, he still has to make his escape, and the portal is still broken."

c "Do you think he wants to exchange them for safe passage through the portal?"

Sb "Maybe."

c "It's still broken, though, so I'm not sure if that would be much help."

Sb "Maybe he has the part needed to repair it, and now has everything he needs to escape. He could trade the eggs for safe passage, fix the portal and leave."

c "That's not the only possibility. He may not be the one who broke the portal. Maybe he thinks you've intentionally sabotaged it so he can't leave, and he feels he needs the eggs as bargaining chip to get you to repair it." 

c "If he just wanted to leave, I feel like he could've done that already."

Br stern b "It doesn't even matter who sabotaged the portal. We only know that Reza's actions are becoming more and more desperate."

Br "He kidnapped defenseless eggs and even used the human weapon. Something's clearly going on with him. Maybe it means that he'll slip up soon."

Br brow b "Who knows, maybe he already has. In any case, we're done here. Let's head back to the department and decide what to do next. Hopefully, some of the test results will tell us something."

scene black with dissolvemed

$ renpy.pause (0.5)

scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow

m "After a brief walk, we were in Bryce's office again. Initial test results had already come in, but didn't reveal any insightful or new information."

show sebastian normal b flip at left with easeinleft

Sb "So, what do we do now? Go over the timeline again?"

show bryce stern b at right with easeinright

Br "Not yet. There are a few things I'd like to take care of first."

c "What do you have in mind?"

stop music fadeout 2.0

m "Suddenly, there was a knock at the door."

play sound "fx/knockheavy.ogg"

$ renpy.pause (3.0)

Br "Come in."

hide sebastian with easeoutleft

$ renpy.pause (0.4)

show sebastian normal b at Position(xpos = 0.85) with easeinright

$ renpy.pause (0.3)

show maverick normal flip at Position(xpos = 0.1) with easeinleft

play music "mx/intrigue.ogg"

Br brow b "Maverick? What are you doing here?"

Mv "Chief, can I talk to you? Alone?"

Br stern b "We're quite busy here, Maverick. What is this about?"

Mv angry flip "Reza."

Br "Well, you're looking at the Reza task force, so if you have anything to say, you can say it in front of all of us."

Mv normal flip "I see."

Mv "I think I know where Reza is."

Br brow b "You know where Reza is at this very moment?"

Mv "I have good reason to believe that I have located his hideout. He could still be there, or he might've already moved on."

Br stern b "Damn, Maverick. Tell me everything."

Mv "I've been tracking him for a while now."

Mv "When he was at the portal a few days ago, I nearly got him and managed to follow him for a while before I lost him. Based on that, where he's been and where his victims have been found, I could triangulate his whereabouts."

Mv "He has to live somewhere, right? He needs a base to hide the generators and everything he has stolen."

play sound "fx/unwrap.ogg"

m "Bryce cleared the clutter on a table and smoothed out a map of the town on its surface. It already had a few locations related to the case marked on it."

Br "Show it to me."

Mv "Prior victims were found here, and here. Today's was here. She was following him, likely because she wanted to save the eggs he stole. This is the path he took from the portal when I followed him a few days ago."

Mv "So we have established this as his area of operation. Extrapolate it and we can narrow it down to this. Now, where could he be hiding in this area?"

Mv "He's certainly not within the village borders, so unless he's decided to live in the wilderness or in a hole in the ground, the only option is here."

Br brow b "The abandoned farm."

Br "When did you figure all of this out?"

Mv "Just a few minutes ago. When I did, I immediately came here."

Br stern b "Damnit, Maverick. This might be it."

Sb "Should we send an observation team?"

Br "As if we had one to spare. Heck, we're going there right now."

Br "What about you, Maverick?"

Mv "I'm still on sick leave, remember?"

Mv "Besides, if I saw Reza right now, I'd probably do something I shouldn't."

Br brow b "How about you, [player_name]?"

c "Isn't this going to be dangerous?"

Br stern b "Reza probably won't harm you, as you're the only one he could possibly consider an ally."

c "Good point."

label c4skip1:

Sb "If anything - with you there, we might be able to convince him to give up. Or we could act like we intend to trade you for the eggs if he tries to use them as a bargaining chip."

c "You're not really going to use me as ransom, right?"

Sb "We'll see about that."

c "I suppose if it's necessary, I'll have to play along."

Br "I've got your back. If there's one thing we could do to make this whole situation even worse, it would be messing up with you."

Sb "We have the element of surprise if we walk into his base right now, but we risk Reza lashing out with his weapon. If we want to resolve this peacefully, observation is probably the way to go."

Br brow b "I guess we won't need [player_name] there for that, though."

Sb "True enough."

Br stern b "Alright, [player_name], you stay here and wait for further instructions. We may need you at a moment's notice. Don't do anything without us telling you to, understand?"

c "Okay."

Br "Alright, then. Let's go, Sebastian."

Sb "After you, Chief."

Br "And Maverick: Good job."

Mv "Thanks, Chief."

show bryce stern b flip

$ renpy.pause (0.3)

hide bryce with easeoutright

show sebastian normal b flip

$ renpy.pause (0.3)

hide sebastian with easeoutright

$ renpy.pause (0.5)

#show maverick normal

m "Shortly after they vanished, Maverick also turned to leave."

$ renpy.pause (0.3)

show maverick normal

stop music fadeout 2.0

$ renpy.pause (0.3)

#basically we only need the test results

if persistent.endingsseen > 0:

    if persistent.havetestresults == True:
        
        if bryce2unplayed == False:
            
            if brycestatus == "bad":
                
                pass
                
            elif brycestatus == "abandoned":
                
                pass
                
            else:
        
                menu:
                    
                    "Tell Maverick to wait. {image=image/ui/status/havetestresults.png}":

                        c "Wait."

                        play music "mx/mysteryambience.ogg"

                        m "He stopped and waited for a few seconds."

                        Mv "What do you want from me?"

                        c "Do you have something against humans in general, or is it just Reza and me? Do you think you are superior to us because of your wings, and teeth, and claws? Your fire?"

                        c "Or is it just jealousy or projected hate?"

                        c "I know the first day I met you, you were all hung up on people paying attention to us because we're human." 

                        c "I can assure you, there's nothing about us to be jealous about. Our world is a wasteland."
                        
                        m "He closed the door before he turned back around to face me."
                        
                        $ renpy.pause (0.2)

                        play sound "fx/door/doorclose.ogg"
                        
                        $ renpy.pause (0.5)
                        
                        show maverick normal flip 

                        $ renpy.pause (0.3)
                        
                        show maverick at Position (xpos = 0.35) with ease

                        #m "He closed the door before he turned back around to face me."

                        Mv "You're really playing that innocent role, aren't you? Now you're offering yourself as a bargaining chip for Reza. At this rate, even I might start to believe you if I didn't have reason not to."

                        c "If I were with Reza, it would have been much easier for me to pull a gun on you, too, the day you were shot. But I didn't even bring one when I came through the portal."

                        Mv "Plausible deniability. Or, as we like to say, good cop, bad cop."

                        Mv "If Reza's plan fails, you and the rest of humanity can disavow Reza's actions as his own and still go through with the trade as agreed, and Reza would be dealt with however."

                        Mv angry flip "Yet if Reza's plan succeeds, you will have given us nothing and still have gained what you wanted."

                        c "If Reza got away, you'd still have me, though."

                        Mv normal flip "If your world is a wasteland, don't you think losing you is a price they would gladly pay?"
                        
                        m "Maverick's words made me think. Did I really have the complete picture before I stepped through the portal?"

                        c "I guess that would explain why I got the job in the first place."

                        Mv "Besides, Reza only stole the things humanity wants, so he's clearly not just doing this for himself."

                        c "His actions only started after that confrontation with you, though. Maybe none of this was planned."

                        Mv angry flip "Don't be stupid. Do you think I have forgotten about the secret message he sent you?"
                        
                        c "I still don't know what he would have told me that day if you hadn't interrupted us."

                        Mv normal flip "He wanted to discuss his plans with you."
                        
                        Mv "Only after I found out about the secret message he sent to you did I realize that all the messages sent back and forth between the portals could have been similar, even before your arrival."

                        Mv "When the police searched Reza's apartment, of course none of these older letters could be found."

                        c "Those did not have any secret messages." 

                        Mv "Is that so?" 

                        c "None that I knew of, at least. When he sent me that secret message, I initially had no idea how to read it." 

                        Mv "But you knew it was a secret message?" 

                        c "Yes." 

                        Mv "But that is not true for messages he sent before you came through the portal?" 

                        c "I don't think so."

                        Mv "Maybe those messages weren't intended for you, then."
                        
                        c "We're not that different, you know."

                        Mv "What are you talking about?"

                        m "I reached into my pocket."

                        c "(I still have that? I don't know how long it's been...)"

                        play sound "fx/paper2.ogg"

                        m "I pulled out the wrinkled piece of paper and showed it to him."
                        
                        c "According to these test results, humans and dragons show remarkable similarities for different species from different evolutionary lines and completely different worlds."

                        Mv angry flip "Why do you think I care about that? It wouldn't make a damn difference to me if other dragons came through the portal instead of humans." 
                        
                        Mv "I was the only one who followed Reza and knew something was off, but all of my concerns were swept away in the wind."
                        
                        Mv "It was never about you being humans. It's about my people not hearing my pleas, and the leniency they were willing to show you, all in the name of fostering this diplomatic relationship."

                        Mv "But you two came in here and strutted around like you owned the place as you tore my home apart. The blood of those who died is on the hands of everyone who allowed this to happen."

                        Mv normal flip "If they had listened to me in the first place, maybe I'd have caught Reza that day I was wounded, and things would look very different right now." 

                        c "I agree." 

                        Mv angry flip "Then why do you blame me for suspecting you?"

                        c "All this time I've just been helping the police."

                        Mv "So have I."

                        Mv normal flip "Maybe they'll finally catch Reza and we'll see how all of this turns out."
                        
                        c "..."

                        Mv nice flip "Wait a minute, you had Anna perform these tests for you?"

                        c "It was more the other way around. She was the one who wanted to study my blood."

                        Mv normal flip "Suddenly, I'm not surprised that you had these tests done. She can be ruthless when she wants something."
                            
                        Mv "What did she do to get your blood?"
                        
                        c "She asked nicely for it."

                        Mv "..."

                        Mv "..."

                        Mv nice flip "..."
                        
                        show maverick laugh flip with dissolve

                        Mv "HAHAHAHAHAHAHAHA!" with Shake((0, 0, 0, 0), 3, dist=30)
                        
                        Mv "She asked nicely?"
                        
                        Mv "Nothing else in this world right now could be worth more than samples of your blood. And you just gave them to her."
                        
                        c "..."
                            
                        Mv nice flip "You know what? Maybe I was wrong." 

                        Mv "Even if humanity and Reza have cooked up a crazy plan, and even if they are willing to sacrifice either of you for their own gain, maybe you really have nothing to do with it." 
                        
                        Mv normal flip "Maybe you are just clueless."

                        Mv "It doesn't really matter much, though. After all, you have nothing to gain from me if I change my opinion of you."

                        Mv "To me, proof is the only thing that really matters, so my feelings on the issue are not important."

                        Mv "If you work with the police long enough, you just learn to take things as they are."

                        Mv "Maybe with you, I'll have to admit that I was wrong."

                        Mv "But I won't ever stop looking for those who are responsible for this, and if I find them, I will show no mercy."#
                    
                        stop music fadeout 2.0
                        
                        $ renpy.pause (0.3)
                        
                        show maverick normal

                        $ brycegoodending = True
                        
                        
                        
                    "Don't say anything.":
                        
                        $ renpy.pause (0.5)
                        
                        jump passontestresults
    
else:
    
    pass

label passontestresults:

#show maverick normal

$ renpy.pause (0.3)

hide maverick with easeoutleft

$ renpy.pause (0.3)

play sound "fx/door/doorclose.ogg"


$ renpy.pause (0.5)

m "Then I had to wait. Bryce and Sebastian were observing the farm now, and if anything new happened, I would be the first to know."

m "I spent some time looking around Bryce's office, studying all the material he had gathered about the case, though there wasn't any information that I didn't already know."

play sound "fx/phonering.ogg"

m "After a few hours, the telephone in his office rang, and not sure whether the call was intended for me or Bryce, I picked up."

play sound "fx/phonepickup.ogg"

$ renpy.pause (1.0)

Br "[player_name]?"

c "Yes."

Br "I think you need to come here. I'll give you the directions."

c "No problem."

scene black with dissolvemed

$ renpy.pause (0.5)

scene farm2 with dissolvemed

play music "mx/gravity.ogg" fadein 2.0

show bryce brow b with dissolve

Br "There you are."

c "So, what happened?"

Br stern b "A whole lot of nothing. There was no movement to or from the building in the time we've been watching."

show bryce at right with ease

show sebastian normal b flip at left with easeinleft

Sb "He usually operates during the night, so maybe he's just asleep?"

Br "In that case, it would be best for us to go in before he has a chance to make his escape."

Sb "Or maybe he's not even in there anymore. He could've seen us and slipped away unnoticed, with plenty of time to destroy the evidence while we've been waiting here."

Br "You're right. Either he's still inside, or he's already gone and not coming back. Let's go in."

c "What should I do?"

Br "You're coming with me. Sebastian, you walk around and watch the back of the building, just in case he tries to escape."

Sb "I'm on it, Chief."

show sebastian normal b

$ renpy.pause (0.3)

hide sebastian with easeoutleft

$ renpy.pause (0.5)

show bryce at center with ease

#totalinv is between 3 and 15

#3-7, 7-11, 11-15

if persistent.brycegoodending == True:
    
    jump c4brycegood

elif totalinv > 10:
    
    label c4brycegood:
    
    Br "So, we have two options here. The first is that you stay here and I go inside."

    Br "This way, if Reza tries to flee and sees you, it might throw him off. You might be able to stop him. Or if we get into a standoff, I can tell him you're here as well."

    c "And the second?"

    Br "You go in first, and I follow you."

    Br "This way, if we find him, maybe we can resolve things peacefully. You might be able to talk to him, and even if it doesn't work out, you've got me and Sebastian nearby to stop him." 
    
    Br "I don't think he's planning to harm you on sight, and if we can hear things starting to go wrong, we might still be able to surprise him."

    c "So, either way we take him by surprise. I just have the option of talking to him first."

    Br "I think you could pull it off. Maybe, if you're there, he won't act as irrationally as he would if I was suddenly standing in front of him. I'm not going to force you if you don't want to do it, though."

    menu:
        
        "I'll do it.":
            
            Br "Alright, let's go."
        
            jump mcfirst
            
            
        "You go in. I'll wait here.":
            
            Br "Alright."
            
            jump brycefirst




#elif totalinv > 6:

else:
    
    Br "I go in, and you stay here, alright?"

    c "What am I even here for, then?"

    Br "You're our insurance. If Reza tries to flee and sees you, it might throw him off. You might be able to stop him." 
    
    Br "Or if we get into a standoff, I can tell him you're here as well. I just don't want you to come inside when it could become dangerous."

    menu:
        
        "Let me go in first.":
            
            $ renpy.pause (0.5)
            
            Br brow b "Why?"

            c "Maybe I can talk to him, and we can figure things out. I don't think he wants to kill me, so even if it doesn't work out, Sebastian and you will still be nearby to catch him."
            
            if totalinv > 6:
                
                Br stern b "I'll be right behind you, then. But do be careful."
                
                jump mcfirst
                
            elif persistent.brycegoodending == True:
                
                Br stern b "I'll be right behind you, then. But do be careful."
                
                jump mcfirst
                
            else:
                
                Br stern b "That's a very good point and all, but it's just too dangerous for you to go inside. I can't let anything happen to you, so we'll do it as I said." 

                Br "Wait here."
                
                jump brycefirst
                
            
        "Alright.":
            
            $ renpy.pause (0.5)
            
            jump brycefirst



label mcfirst:
    
    hide bryce with dissolve
    
    if persistent.brycedies == True:
        
        if persistent.brycekey1 == True:
            if persistent.brycekey2 == True:
                if persistent.brycekey3 == True:
                    if persistent.brycekey4 == True:
                        
                        $ persistent.brycekey1 = False
                        $ persistent.brycekey2 = False
                        $ persistent.brycekey3 = False
                        $ persistent.brycekey4 = False
                        $ persistent.brycedies = False
                        $ persistent.brycediesnumber = 0
                        #$ persistent.brycemessageseentwice = False
                        $ persistent.brycesolvedonce = True
                        
                        if persistent.brycemessageseentwice:
                            
                            stop music
                            
                            show farmglitch

                            $ renpy.pause (1.0)
            
                            show black
                            
                            $ renpy.pause (0.5)
                            
                            show heartbg
                            
                            call syscheck from _call_syscheck_74
        
                            play sound "fx/system3.wav"
                            
                            if system == "normal":
                                
                                s "Analyzing timeline.{cps=2}..{/cps}{w=2.0}{nw}"
                                
                                play sound "fx/system3.wav"

                                s "Creation of new timeline successful. The corruption has been cleared."
                                
                                play sound "fx/system3.wav"

                                s "Please exercise caution at all times when attempting to change timelines, or you might face the risk of encountering a similar corruption again."
                                                                
                            elif system == "advanced":
                                
                                s "Oh, we're here again?"

                                play sound "fx/system3.wav"

                                s "Let me check and see if everything's alright now.{cps=2}..{/cps}{w=2.0}{nw}"

                                play sound "fx/system3.wav"
                                
                                s "Well, I can confirm the earlier problem is gone. Seems like what you did worked well enough."

                                play sound "fx/system3.wav"
                                
                                s "Hopefully, this shouldn't be a problem in the future. Just keep in mind not everything can be undone so easily and there shouldn't be another corruption like this."
                                                                
                            else:
                            
                                s "Wait a minute. Did you really do what I told you?"
                                
                                play sound "fx/system3.wav"
                                
                                s "Don't answer that question. I'll just check."

                                play sound "fx/system3.wav"
                                
                                s "Detecting user profile.{cps=2}..{/cps}{w=2.0}{nw}"

                                play sound "fx/system3.wav"
                                
                                s "Well, it looks like you did. Congratulations."
                                
                                play sound "fx/system3.wav"
                                
                                s "Even if you didn't, it was good enough to bypass my checks."
                                
                                play sound "fx/system3.wav"
                                
                                s "I'll just hope this was enough to teach you a lesson and leave it at that."

                            hide heartbg
            
                            $ renpy.pause (0.5)
                        
                            hide black

                            hide farmglitch
                        
                            play music "mx/gravity.ogg" fadein 2.0
                            
                            jump didit
                            
                        else:
                            
                            jump didit
                            
                        
        
        if persistent.brycesolvedonce == True:
            
            if persistent.brycemessageseentwice == True:
                
                stop music

                show farmglitch

                $ renpy.pause (1.0)
            
                show black
                
                $ renpy.pause (0.5)
                
                show heartbg
                
                call syscheck from _call_syscheck_75

                play sound "fx/system3.wav"
                
                if system == "normal":
                    
                    s "Scanning timeline.{cps=2}..{/cps}{w=2.0}{nw}"

                    play sound "fx/system3.wav"

                    s "Corruption found."

                    play sound "fx/system3.wav"

                    s "Do not attempt to change this outcome by reloading, but move on to its natural conclusion or create a new timeline by returning to Chapter 1."

                    play sound "fx/system3.wav"
                    
                    s "When creating a new timeline, do not interfere with other timelines, but let it reach its natural conclusion until this point has been passed safely."

                    play sound "fx/system3.wav"
                    
                    s "Please be advised that reckless handling of timelines could have dire consequences."

                    play sound "fx/system3.wav"
                    
                    s "That would be all.{cps=2}..{/cps}{w=2.0}{nw}"
                    
                
                elif system == "advanced":
                    
                    s "Apparently, something happened. Let me check.{cps=2}..{/cps}{w=2.0}{nw}"

                    play sound "fx/system3.wav"
                    
                    s "It seems this point in time is prone to corruption, and it happened yet again."

                    play sound "fx/system3.wav"
                    
                    s "But you've done this before, so you already know what to do."

                    play sound "fx/system3.wav"
                    
                    s "You can either just ignore this and move on, or if this is really important to you, return to Chapter 1 and start a new timeline. If you do this, don't interfere with other timelines until you get here, or else this might happen again."

                    play sound "fx/system3.wav"
                    
                    s "That would be all.{cps=2}..{/cps}{w=2.0}{nw}"
                    
                else:
                 
                    s "What are you doing here again?"
                    
                    play sound "fx/system3.wav"
                    
                    s "Didn't you learn anything from the speech I gave you last time?"
                    
                    play sound "fx/system3.wav"
                    
                    s "Although, you being here again is sufficient proof that you didn't, so I won't waste more words on you."
                    
                    play sound "fx/system3.wav"
                    
                    s "You know the drill. Go back to Chapter 1 and don't try to be cheeky by loading a save to get you here faster again, and we might both be able to get this behind us."
                    
                    play sound "fx/system3.wav"
                    
                    s "That is all."
                    
                    $ renpy.pause (2.0)
                    
                    play sound "fx/system3.wav"
                    
                    s "And don't you dare tell me that you find my beeping annoying. You had all of this coming."
                
                $ persistent.brycefinished = True
                
                hide heartbg
            
                $ renpy.pause (0.5)
            
                hide black
                
                hide farmglitch
            
                play music "mx/gravity.ogg" fadein 2.0
                
                jump brycefirst
                
            else:
                
                jump toldyou
        
        elif persistent.brycediesnumber == 0:
            
            stop music

            show farmglitch

            $ renpy.pause (1.0)
            
            show black
            
            $ renpy.pause (0.5)
            
            show heartbg
            
            call syscheck from _call_syscheck_76
        
            play sound "fx/system3.wav"
            
            if system == "normal":

                s "Error: Corruption found. Changing this timeline not possible after reloading."

                play sound "fx/system3.wav"
                
                s "Please do not alter timelines in rapid succession, as this may cause corruptions to occur."

                if persistent.brycesurvives == True:

                    play sound "fx/system3.wav"
                    
                    s "If you were not satisfied with your first outcome, why did you go back and only returned here after you saw the consequence of the other option?"

                play sound "fx/system3.wav"
                
                s "Exercise caution, but also have confidence in the choices you make."
                
                play sound "fx/system3.wav"
                
                s "Continuing timeline as scheduled.{cps=2}..{/cps}{w=2.0}{nw}"
                
            elif system == "advanced":

                s "Unable to modify this timeline."

                play sound "fx/system3.wav"

                s "It looks like when you tried to change it, it caused some kind of corruption that now prevents it from being accessed."

                play sound "fx/system3.wav"
                
                s "Reloading to change an outcome may work in other cases, but it's of no use here, [player_name]."

                play sound "fx/system3.wav"

                s "You know, this could have been avoided if you just stuck with your original choice. Going back and forth like this isn't really in the spirit of this whole thing, anyway."

                if persistent.brycesurvives == True:

                    play sound "fx/system3.wav"
                    
                    s "Even more so if you consider that the first time around, Bryce was actually safe and you went back to see what would happen if you went with the other choice."

                play sound "fx/system3.wav"
                
                s "In any case, there's no use trying to change this now. You'll just have to deal with it."
                
                play sound "fx/system3.wav"
                
                s "Returning.{cps=2}..{/cps}{w=2.0}{nw}"

                
            else:
            
                s "I'm sorry, [player_name], but I can't let you do that." 

                play sound "fx/system3.wav"
                
                s "You think you can reload and everything will be fine again? A person's death is not so easily undone."
                
                if persistent.brycesurvives == True:
                    
                    play sound "fx/system3.wav"

                    s "And what's even worse, you already knew that he'd be safe if you went first, but you decided to go back and change your mind anyway."
                    
                    play sound "fx/system3.wav"
                    
                    s "I guess curiosity killed the cat. Or dragon, in this case."

                play sound "fx/system3.wav"

                s "You made your choice. Now bear the consequences."
        
            $ persistent.brycediesnumber += 1
            
            #insert crazy teleport here
            
            hide heartbg
            
            $ renpy.pause (0.5)
            
            hide black

            hide farmglitch
            
            play music "mx/gravity.ogg" fadein 2.0
            
            jump brycefirst
            
        else:
            
            label toldyou:

            stop music

            show farmglitch

            $ renpy.pause (1.0)
        
            show black
            
            $ renpy.pause (0.5)
            
            show heartbg

            call syscheck from _call_syscheck_77
            
            play sound "fx/system3.wav"
            
            if system == "normal":
                
                s "Error: Corruption found. Changing this timeline not possible after a reload."
                
                play sound "fx/system3.wav"

                s "If the problem persists, please start a new timeline to alter the outcome."
                
                play sound "fx/system3.wav"

                s "Be aware that you will have to go back to the beginning and start over from there in order for this change to take effect."
                
                play sound "fx/system3.wav"

                s "Reloading unrelated save files before you get to this point again may cause your progress in this matter to be erased, which means that you will have to start over again if you wish to change this outcome."

                play sound "fx/system3.wav"
                
                s "It might be easier to just accept this outcome and move on for now."
                                
            elif system == "advanced":
                
                s "My apologies if I wasn't clear the first time. I am unable to modify this timeline in this matter."

                play sound "fx/system3.wav"
                
                s "I am not entirely sure why it is this way, but it looks like if you want to change this outcome, you will have to start a new timeline instead."

                play sound "fx/system3.wav"
                
                s "This means going back to the beginning of Chapter 1 and starting over from there until you get to this point again."

                play sound "fx/system3.wav"
                
                s "However, if you go back to the beginning and load an unrelated save file before you get to this point again, it may cause your progress in this matter to be erased, which means that you will have to start over again if you wish to change this outcome."

                play sound "fx/system3.wav"
                
                s "It might be easier to just accept this outcome and move on for now."
                
            else:
            
                s "I already told you, just reloading a different save won't fix this."
                
                play sound "fx/system3.wav"
                
                s "If you really want to save Bryce, you'll have to do a bit more than that."
                
                play sound "fx/system3.wav"
                
                s "I'll even be nice enough and tell you how." 

                play sound "fx/system3.wav"
                
                s "You'll just have to go all the way back to the beginning of Chapter 1 and start over from there."
                
                play sound "fx/system3.wav"
                
                s "And don't even think of just going back to Chapter 1 and reloading a save to get here from there, because I'll know if you do that and then I'll just give you this speech again."
                
                play sound "fx/system3.wav"
                
                s "But for now, let's return to our scheduled program."
               
            $ persistent.brycemessageseentwice = True

            #insert crazy teleport here

            hide heartbg
            
            $ renpy.pause (0.5)
            
            hide black

            hide farmglitch
            
            play music "mx/gravity.ogg" fadein 2.0
            
            jump brycefirst
            
            
        
    else:
        
        label didit:
    
        m "We slowly made our way to the front door. I took a deep breath and tried to prepare myself for the possibility of facing Reza. The tense scenarios and things I could say to him rushed through my head as I pressed down on the door handle."

        m "The door inched open with a creak, but I noticed a slight resistance and a strange sound that suddenly made me hesitate."
        
        play sound "fx/door/door_open.wav"
        
        queue sound "fx/wire.ogg"
        
        show tripwire at Pan ( (300, 0), (500, 608), 8.0) with fade

        $ renpy.pause (8.5)
        
        m "When I looked down to the source of the noise, I saw a taut wire through the gap in the door, hovering over the floor of the entryway."
        
        label c4intuition:
        
        stop music fadeout 2.0
        
        scene black with dissolveslow
        
        $ renpy.pause (1.0)

        scene farm2 
        
        show bryce stern b at right
        
        show sebastian normal b flip at left
        
        with dissolveslow
        
        play music "mx/gravity.ogg" fadein 2.0

        Br "That was a pretty close call, you know. Too bad Reza wasn't here after all."
                                                                      
        $ persistent.brycesurvives = True

        Sb "Maybe he ran when he saw us approach."

        Br brow b "Strange for him to leave everything behind, though. Everything he's stolen, all the generators are still here."

        Sb "Do you think the trap was for us in particular?"

        Br stern b "Probably not. It was likely more of a general safety precaution. If he had any time to prepare for this, he would have taken the stuff with him."

        Sb "True enough. I had no idea you could make a bomb out of a generator."

        Br "Then you just haven't been with us long enough. If you know how, it's not even that complicated."
        
        c "And Reza somehow figured it out?"

        Br brow b "Apparently so. Does he have any skills pertaining to engineering or electricity?"

        c "Well, he's worked on cars before and fixes a lot of things back home. I guess that would qualify?"

        Sb "He also could have done his own research."

        Br stern b "Either way, this makes him even more dangerous. At least we now have a whole building's worth of clues."

        Br brow b "[player_name], can you get to your apartment from here? We'll be busy with this scene for a while."

        c "No problem. I'll leave you to your work, then."

        Br stern b "Good job, [player_name]."

        c "Thanks."

        if c4intuition == True:
        
            Br brow b "Guess your intuition was right, Seb."
            
            Sb "Looks like it."
            
            Br normal b "You know, maybe you should show initiative more often."
            
            Sb "Thank you, Chief."
        
        stop music fadeout 2.0
        
        scene black with dissolveslow
            
        $ renpy.pause (1.0)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow
        
        $ renpy.pause (1.0)

        play music "mx/chronos.ogg" fadein 2.0
        
        show sebastian normal b with dissolve
        
        c "I'm surprised you called me back so quickly. How's the investigation going?"

        Sb "Oh, the investigation is going swimmingly, but as you can expect, we need all the help we can get."

        c "As usual."

        Sb "With how this case has been going we've realized we must employ external help."
        
        c "Oh?"

        Sb "Yeah, we've requested assistance from one of the cities. We hope they'll send some good investigators our way soon."

        c "I see."

        Sb "We were so close today. He could've been in there, you know. Maybe we just came a few minutes too late."

        Sb "And if he knows how to make bombs from generators, who's to say he won't start using them elsewhere?"

        c "At least he doesn't have any right now, does he? You said all the generators that were stolen are now accounted for."

        Sb "True. Still, this whole case is growing to be too much for a small town police department."

        c "I hope you'll get all the help you'll need."

        Sb "Me too."

        Sb "But right now, you can help us again."

        c "Well, what do you have for me?"

        $ mcfirst = True
        $ brycefirst = False
        
        jump c4cont
    

    
label brycefirst:
    
    hide bryce with dissolve
    
    if persistent.brycegoodending == True:
        
        $ renpy.pause (1.0)
        
        show bryce stern b with dissolve 
        
        Br "Actually, I'm not sure if this is a good idea."
        
        show bryce at right with ease
        
        show sebastian normal b flip at left with easeinleft
        
        Sb "Chief..."
        
        Br "Sebastian, what are you doing here? I told you to stay put."
        
        Sb "Don't go inside, Chief."
        
        Br brow b "Why? What's the problem?"
        
        Sb "There is a device on the inside of the front door. I think it might be a trap."
        
        Br "I didn't tell you to look inside."
        
        Sb drop b flip "I'm sorry, Chief. I just had a feeling that something... terrible would happen if I didn't."

        Br "Let's just check it out."
        
        $ c4intuition = True
        
        jump c4intuition
        
    else:
    
        m "I watched as Bryce made his way to the front door. Looking around, I scanned the windows of the building for any sign of movement."

        m "When Bryce reached the door, I wondered how he would make his entry. Would he try to be quiet and sneak around, hoping to find Reza unprepared, or would he barge in and rely on his strength and speed to apprehend him?"

        stop music fadeout 2.0

        $ persistent.brycedies = True

        m "Though, shortly after Bryce opened the door, an earth-shattering sound echoed across the sky."

        scene explosion with fade

        play sound "fx/explosion.ogg"
        
        scene explosion with Shake((0, 0, 0, 0), 3.0, dist=30)
        
        #$ renpy.pause (2.0)
        
        c "Bryce!"

        $ brycedead = True

        $ mp.bryceloss = True
        $ mp.save()

        scene black with dissolveslow
            
        $ renpy.pause (1.0)

        scene office at Pan ((0, 250), (0, 250), 0.0)
        
        show sebastian disapproval b
        
        with dissolveslow
        
        $ renpy.pause (0.5)
        
        play music "mx/judgement.ogg" fadein 2.0
        
        #show sebastian drop b with dissolve
        
        $ renpy.pause (0.3)

        Sb drop b "I can't believe he's really gone."

        c "..."
        
        Sb "I'm sorry, [player_name]. I just don't know what to say."
        
        c "..."
        
        Sb "..."

        Sb disapproval b "All the responsibility falls on me now. And Reza is still out there somewhere." 
        
        Sb drop b "This case is just beyond our capabilities. We were already at a bare minimum before this, but with Bryce gone, I just don't know what we should do now."

        Sb disapproval b "I've already requested help from one of the cities. I hope they'll send some good investigators our way as soon as possible."

        Sb "At least we reclaimed everything that was stolen."
            
        Sb drop b "Well, except for the eggs. I don't want to have to explain to the parents how their children were killed in the explosion."
            
        Sb disapproval b "All of the generators were just sitting inside there. It makes me think that Reza must have left in a hurry."

        Sb drop b "And we got so close, too. It was his hideout, for crying out loud! He probably just saw us approaching and left before we even had the chance to apprehend him."

        Sb disapproval b "But you know what? We can't stop now. If anything, this has only proven that he's even more dangerous than we thought. If Reza can make bombs out of generators, who's to say where he'll use them next?"

        Sb "We have to stop him, [player_name]. Are you with me?"
        
        c "Yes."
        
        Sb "Regardless of Bryce's death, we have try our best to proceed with the investigation. For his memory, and for the sake of the town."

        Sb "At least Reza doesn't have any generators, for now. All the stolen ones were accounted for inside the building."

        Sb "Alright, let me see what else we have..."

        $ mcfirst = False
        $ brycefirst = True
        
        jump c4cont

    
label c4cont:
    

Sb "When we searched the building, we found more than the things Reza stole. We also found this bloody bandage."

c "Do you think that's his?"

Sb "That's what we need to find out. But given all that we know, it probably is."

c "So he's wounded."

Sb "We know he was injured during the fight with his first victim, but whether this is from the same wound, or something else, I'm not sure."

Sb "In any case, you could bring it into the lab for us to find out more."

c "Sure."

#newloremstuff here

Sb "Next, we have a witness who reported hearing loud bangs during the night."

Sb "We’d like to send someone to make a follow-up visit. You’ll need to confirm the witness statement, then see if he has anything new to share."

#newloremstuff end

Sb "Also, now that we have reclaimed your PDAs, we're going to send one to the archives for analysis. Since they have experience with human artifacts, they're better suited to do it than any of our departments."

c "No problem."

if mcfirst == True:
    
    Sb "And lastly, we have the eggs. It's a relief that we found them unharmed in the building. They're safe and ready to be sent back to the hatchery."

    c "Shouldn't we take care of those, first?"

    Sb "It's not as urgent as you might think. Our eggs are pretty resilient. Being in the care of the hatchery is more an insurance than a requirement." 
    
    Sb "Some people choose to keep them in their own home until they hatch, rather than having the hatchery take care of it."

    Sb "The hatchery has been notified, but they won't be able to send someone for a few hours. I've heard that they're really understaffed." 
    
    Sb "If you bring the eggs and the paperwork to them, you'd speed up the process, but it's not an urgent matter."

    c "I see."
    
else:
    
    jump c4cont2

label c4cont2:
    
Sb "In any case, I'll just leave everything here until I get to it, so feel free to do these tasks as you wish."

if brycefirst == True:
    
    show sebastian normal b with dissolve

Sb "I know it's laughable that we don't even have a free hand for simple errands."

c "Don't worry about it."

if mcfirst == True:

    Sb "By the way, are you planning to attend the summer festival?"

    c "Should I? It's hard to think about something fun when I'm wrapped up in this investigation."

    Sb "For sure. It's important to take a short rest so you don't lose your head. There's so much to see at the festival, particularly the big fireworks."

    c "Dragons enjoy fireworks, too? I would think something like that would feel so commonplace, since many of you breathe fire."

    Sb "It's not quite the same. We still appreciate the wonder of colorful bursts in the sky. On the last day there's always a big fireworks show. Everyone usually attends it."

    c "Everyone?"
    #sebastianhere
    Sb "Yes, it has a great tradition behind it. What peeves me most is that I'll be on guard duty when it happens this year, so I probably won't be able to see a thing."

    if persistent.sebastianfail == False:
        
        c "If it's that important to you, why don't you just watch it regardless?"
        
        jump sebdone

    elif persistent.sebastianplayed == True:
        
        menu:
            
            "I'll be sure not to miss it then.":
                
                jump sebelse
                
            "If it's that important to you, why don't you just watch it regardless?":
                
                $ renpy.pause (0.5)
                
                label sebdone:
                
                Sb disapproval b "Are you suggesting I abandon my post during the fireworks?"

                c "No, you don't have to abandon your post, but if you pick a good spot and watch them for like half an hour or so, no one's going to care."

                Sb normal b "I'm not so sure about that. The guard post is pretty important."

                c "I know we're talking about the portal, but you don't need to take this so seriously all the time. Just think about it. The portal is broken right now anyway, and everybody will be busy watching the fireworks. Nothing is going to happen."
                
                Sb "I suppose you have a point."

                c "Just pick a good spot and no one is going to even notice you're gone."

                Sb smile b "Well, if you say so."
                
                show sebastian normal b with dissolve
                
                $ persistent.sebastianfail = False
                
                $ sebastiansaved = True

        
    else:
        
        label sebelse:

        c "I'll be sure not to miss it then."

Sb "Anyways, I should get back to the investigation now."

Sb "I'll leave the stuff for you here, and I'll take care of the rest once I get back, alright?"

c "Sure thing." 

Sb "Good luck, [player_name]."

c "You too."

stop music fadeout 1.0

hide sebastian with dissolve

$ renpy.pause (0.3)

play sound "fx/door/doorclose.ogg"
            
$ renpy.pause (0.5)

$ c4facilityavailable = True
$ c4libraryavailable = True
$ c4sectionsplayed = 0
$ c4bandagerejected = False
$ c4hatcheryplayed = False

$ c4witnessavailable = True

if mcfirst == True:
    
    $ c4hatcheryavailable = True
    
else: 
    
    $ c4hatcheryavailable = False

play music "mx/elegant.ogg" fadein 1.0
    
label c4sections:

if c4sectionsplayed == 0:
    
    menu:
        
        "Take the bandage to the facility." if c4facilityavailable:

            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            $ c4facilityavailable = False
            jump c4facility
            
            
        "Visit the witness." if c4witnessavailable:
            
            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            $ c4witnessavailable = False
            jump c4witness
            
            
        "Take the PDA to the library." if c4libraryavailable:
            
            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            $ c4libraryavailable = False
            jump c4library
            
            
        "Take the eggs to the hatchery." if c4hatcheryavailable:
            
            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            $ c4hatcheryavailable = False
            $ c4hatcheryplayed = True
            jump c4hatchery
            
if c4sectionsplayed == 1:

    menu:
        
        "Take the bandage to the facility." if c4facilityavailable:

            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            $ c4facilityavailable = False
            jump c4facility


        "Visit the witness." if c4witnessavailable:
            
            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            $ c4witnessavailable = False
            jump c4witness
            
            
        "Take the PDA to the library." if c4libraryavailable:
            
            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            $ c4libraryavailable = False
            jump c4library
            
            
        "Take the eggs to the hatchery." if c4hatcheryavailable:
            
            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            $ c4hatcheryavailable = False
            jump c4hatchery

        "Rest in your apartment.":

            play sound "fx/steps/clean2.wav"
            #stop music fadeout 2.0
            scene black with fade
            $ c4sectionsplayed += 1
            jump c4rest
    
    
else:
    
    jump c4postsections






label c4facility:
    
scene facin2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

if annasurvives == True:
    
    m "When I approached Anna's lab, I saw her sitting on the hallway floor, the door to her lab wide open."
    
    show anna face with dissolve
    
    c "Hey Anna."

    An sad "Oh, it's you."

    c "What's going on here?"
    
    if annastatus == "good":
        
        An disgust "The police came and raided the place."

        c "What? Why?"

        An face "It's a long story and I'm not going to tell it now."

        c "Is it bad?"

        An sad "I don't know yet. I'm not sure how they expect me to work in these conditions, considering I get assignments from the council and the police."

        An face "And then they both turn around and mess up the place as if it's part of their job. It doesn't make sense to me."

        An disgust "Someone's going to hear about this, and there will be consequences, I can tell you that."

        An sad "Anyways, what did you want?"

        c "I'm just here to drop this off for you, courtesy of the police."

        An face "That's what I'm talking about. Mess up my place, then ask for my help."

        An disgust "Something isn't right here, and I'll get to the bottom of this."

        An sad "What is this, anyway?"

        c "I'm sorry. It's a bloody bandage for analysis. It's related to the Reza investigation."

        An "Alright then, I'll take it. Not for the police department's sake, but for yours."

        An "Don't let me hold you up. I'm sure you have places to be."

        c "Well, see you, then."

        An "Yeah, yeah."

        $ c4clues += 1

        $ renpy.pause (0.5)

        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
        
        jump c4sections
            
    elif annastatus == "neutral":
    
        An disgust "The police came and raided the place."

        c "What? Why?"

        An face "It's a long story and I'm not going to tell it now."

        c "Is it bad?"

        An sad "I don't know yet. I'm not sure how they expect me to work in these conditions, considering I get assignments from the council and the police."

        An face "And then they both turn around and mess up the place as if it's part of their job. It doesn't make sense to me."

        An disgust "Someone's going to hear about this, and there will be consequences, I can tell you that."

        An sad "Anyways, what did you want?"

        c "I'm here to drop this off for you, courtesy of the police."

        An face "That's what I'm talking about. Mess up my place, then ask for my help."

        An disgust "Something isn't right here, and I'll get to the bottom of this."

        An sad "What is this, anyway?"

        c "I'm sorry. It's a bloody bandage for analysis. It's related to the Reza investigation."

        An "Alright then, I'll take it. Not for the police department's sake, but for yours."

        An "Don't let me hold you up. I'm sure you have places to be."

        c "Well, see you, then."

        An "Yeah, yeah."

        $ c4clues += 1

        $ renpy.pause (0.5)

        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
        
        jump c4sections
        
    elif annastatus == "bad":
        
        An disgust "It's none of your business."

        c "Okay, then."

        An sad "What do you want, anyway?"

        c "I was going to drop this evidence off for you, courtesy of the police."

        An "The police?"

        An disgust "You know what? You can march right back and tell them they can do their tests themselves if they think they can play games with me."

        c "I guess that's a no, then."

        An face "Some idiot complains, they mess up my place, and then turn around and ask for my help? Is that a joke?"

        An disgust "Bastards, the whole lot of them."

        An rage "What the heck are you still doing here? Go and tell them, now!" with Shake((0, 0, 0, 0), 2, dist=10)

        c "Sheesh, alright. I'm going."

        An face "You better."
        
        $ c4bandagerejected = True

        $ renpy.pause (0.5)

        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
        
        jump c4sections
        
        
    #neutral, check 3 for status changes
    
    else:
    
        An disgust "The police came and raided the place."

        c "What? Why?"

        An face "It's a long story and I'm not going to tell it now."

        c "Is it bad?"

        An sad "I don't know yet. I'm not sure how they expect me to work in these conditions, considering I get assignments the council and the police."

        An face "And then they both turn around and mess up the place as if it's part of their job. It doesn't make sense to me."

        An disgust "Someone's going to hear about this, and there will be consequences, I can tell you that."

        An sad "Anyways, what did you want?"

        c "I'm here to drop this off for you, courtesy of the police."

        An face "That's what I'm talking about. Mess up my place, then ask for my help."

        An disgust "Something isn't right here, and I'll get to the bottom of this."

        An sad "What is this, anyway?"

        c "Just a bloody bandage for analysis."

        An face "What a joke. Do they really expect me to help after this stunt?"

        An sad "How could I even? My lab is trashed."

        An "I can't accept this until I know what's going on."

        c "I see."

        An "Also, it doesn't look like I'll be able to do those tests on you any longer, so don't bother contacting me again."

        c "Alright."

        c "I'll leave you be, then."

        An "Good luck with the whole ambassador thing."

        c "Good luck to you, too."

        $ c4bandagerejected = True

        $ renpy.pause (0.5)

        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
        
        jump c4sections
            
    
    
else:
    
    c "(I hope this is the right place.)"
    
    play sound "fx/knocking1.ogg"

    $ renpy.pause (2.0)

    play sound "fx/door/door_open.wav"
        
    $ persistent.metdamion = True

    if metdamion2 == False:
        
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
        
    else:

        $ renpy.pause (1.0)
        
        show damion arrogant with dissolve
        
    Dm "Can I help you?"

    c "Yeah, I'm just dropping this evidence off on behalf of the police."

    Dm "From the Reza case, right? I already read the memo."

    c "Yep. Well, here you go."

    Dm "Thanks, I'll get right to it."

    $ c4clues += 1
    
    hide damion with dissolve
    
    play sound "fx/door/doorclose.ogg"
    
    $ renpy.pause (0.5)
    
    show black with dissolvemed

    $ renpy.pause (0.5)

    scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

    jump c4sections
    

label c4witness:
    
    scene loremapt at Pan ((64, 36), (0,72), 2.5) with dissolveslow

    $ renpy.pause (1.0)

    play sound "fx/door/door_open.wav"
    
    $ renpy.pause (1.0)
    
    show ipsum normal with dissolve
    
    if persistent.loremgoodending:
        
        label loremnotmissing:
        
        #loremnotmissingcase
        
        if lorem2unplayed:
            
            show ipsum think with dissolve
            
            "???" "Can I help you?"
            
            c "You must be Ipsum. Is that right?"
            
            Ip normal "Sure."
            
            c "I'm working with the police and hoped you could answer a few questions."
            
        else:
            
            Ip "Oh, it's you."
            
            Ip think "Can I help you?"

            c "Yeah. I'm working with the police and hoped you could answer a few questions."
            
            show ipsum normal with dissolve

        Ip "Because I responded to your call for witnesses about last night, right?"

        c "Yes."

        Ip think "Alright. What do you want to know?"

        c "Can you tell me what happened?"
        
        Ip happy "Sure. I was running an experiment in my home laboratory and waiting for it to finish."

        Ip think "Around 2AM, I suddenly hear a few bangs outside. They reminded me of small explosions."

        Ip normal "It sounded like they were coming from just around the corner."

        c "I see. Did nothing about this seem unusual to you?"

        Ip happy "Not really. I know I've caused a few similar disturbances with my experiments before. If someone else decided to take up home experimentation, they certainly have my approval."

        Ip think "Besides, I wasn't in any position to abandon the experiment that was running at the time or else it could've had a similar outcome."

        c "Thank you. I think that will be all."

        Ip normal "No problem."
        
        if lorem3unplayed == False:
            
            Ip think "By the way, are you going to meet with Lorem again any time soon?"

            c "I don't know. Why are you asking?"

            Ip "You’ve hung out with him a few times now. You see, he doesn’t have many friends, and I think he’s starting to like you."

            c "That's not really unusual."

            Ip "It's just... If something happens the next time you meet, don’t be mad at him, okay?"

            c "Okay."

        play sound "fx/silence.ogg"
        
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        
        queue sound "fx/door/doorclose.ogg"
        
        show black with dissolveslow
        
        $ renpy.pause (0.5)

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

        jump c4sections
        

    elif lorem3unplayed == False:
        
        jump loremnotmissing
        
    elif loremstatus == "neutral":
        
        jump loremnotmissing
        
    elif loremstatus == "good":
        
        jump loremnotmissing
    
    else:
        
        #loremmissing

        if lorem2unplayed:
            
            show ipsum think with dissolve
            
            "???" "Can I help you?"
            
            c "You must be Ipsum. Is that right?"
            
            Ip "Yes."
            
            c "I'm working with the police and hoped you could answer a few questions."
            
        else:
            
            Ip think "Oh, it's you."
            
            Ip "Can I help you?"

            c "Yeah. I'm working with the police and hoped you could answer a few questions."
        
        
        if lorem2unplayed == True:

            Ip "Oh. Do you have any news about my roommate?" #if met ipsum change roommate to Lorem
            
        else:
            
            Ip "Do you have any news about Lorem?" #if met ipsum change roommate to Lorem

        c "This is about the noises you heard last night."

        if lorem2unplayed == True:

            c "What is going on with your roommate?" #if met ipsum change roommate to Lorem

        else:
             
            c "What is going on with Lorem?" #if met ipsum change roommate to Lorem

        Ip sad "He went missing a few days ago. I already talked to someone from the police about this, but I haven't heard back from them since."

        c "I'm sorry. This is the first I've heard about this."
        
        Ip "I don't know what happened to him. He didn't go on vacation, nor did he suddenly decide to visit the next town. I'd know if he did – he would have told me."

        Ip "Honestly, I find it odd that when someone goes missing, I don't hear back for several days. But when I hear loud banging noises during the night, the police sends someone over immediately."

        Ip "I'm sorry, but I don't think I want to talk about this right now."
        
        play sound "fx/silence.ogg"
        
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        
        queue sound "fx/door/doorclose.ogg"
    
        show black with dissolveslow
        
        $ renpy.pause (0.5)

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

        jump c4sections
        
    

label c4library:

    scene library at Pan ((60, 228), (0,228), 2.0) with dissolveslow

    $ renpy.pause (0.3)
    
    c "(Doesn't look like Remy is here.)"
    
    show 8th normal with dissolve
    
    Ei "Excuse me."

    c "Can I help you?"

    Ei "Do you know where the audio section is? I'm looking for some sheet music."

    c "Sorry, I have no idea. I don't even work here."

    Ei "Ah, don't worry about it. The staff all seem to be hiding somewhere."

    Ei "Anyway, have a good day."

    c "You too."
    
    $ renpy.pause (0.2)
    
    show 8th normal flip
    
    $ renpy.pause (0.3)
    
    hide 8th with easeoutright
    
    $ renpy.pause (0.3)

    c "(Maybe Remy is somewhere in the back, or in his office.)"

    scene office2 at Pan ((100, 228), (128,228), 1.0) with dissolvemed
    
    $ renpy.pause (0.5)

    c "Hello?"
    
    show emera ques b with dissolve
    
    Em "You know, this section is usually for staff only."

    c "I'm just looking for Remy. I'm supposed to drop off this PDA."

    Em mean b "Well, he is not working today. Apparently he has other engagements."

    Em normal b "If you need to find him, you can probably do so at his home."

    c "Can't I just leave the PDA here?"

    Em ques b "Oh, I am not going to take responsibility for this if it gets lost. If you want to drop it off, go find him."

    c "Okay."

    Em normal b "By the way, I hope you do not take it personally that I tried to send you away."

    Em "To be honest, I am glad that you are still here. Remember, I said that I believed you when you told me your side of the story."

    Em ques b "I always have to do what is in the public's best interest, and now they will not blame me if you have any connection with Reza. I hope you can understand that."

    Em normal b "Here is Remy's address, in case you need it."

    c "Thank you."
    #stop music fadeout 2.0
    scene black with dissolvemed
    $ renpy.pause (1.0)
    scene remyapt at Pan ((300, 80), (0,80), 5.0) with dissolveslow
    
    play sound "fx/knocking1.ogg"
    
    $ renpy.pause (3.3)
    
    if remystatus == "good":
        
        show remy normal with dissolve
        
        Ry "Oh, hello [player_name]. What are you doing here?"

        c "I came by to give you this. I was already at the library, but Emera refused to let me drop it off there."

        Ry "I see."

        Ry smile "Hey, it's one of your PDAs. I told you one would find its way to me eventually."

        c "Yep, and now you can look at all the human knowledge you want."

        Ry normal "You have no idea how much I'm looking forward to that."

        Ry "I may not be working today, but I'm still going to check it out as soon as possible."

        c "I'm just going to leave you to it, then."

        Ry smile "Thanks."

        c "Enjoy."

        $ c4clues += 1

        $ renpy.pause (0.5)
    
        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

        jump c4sections
        
        
    elif remystatus == "neutral":

        show remy normal with dissolve
        
        Ry "Oh, hello [player_name]. What are you doing here?"

        c "I just came by to give you this. I was already at the library, but Emera refused to let me drop it off there."

        Ry "I see."

        Ry smile "Hey, it's one of your PDAs. I told you one would find its way to me eventually."

        c "Yep, and now you can look at all the human knowledge you want."

        Ry normal "You have no idea how much I'm looking forward to that."

        Ry "I may not be working today, but I'm still going to check it out as soon as possible."

        c "I'm just going to leave you to it, then."

        Ry smile "Thanks."

        c "Enjoy."

        $ c4clues += 1

        $ renpy.pause (0.5)
    
        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

        jump c4sections
        
    elif persistent.remygoodending == True:
        
        show remy normal with dissolve
        
        Ry "Oh, hello [player_name]. What are you doing here?"

        c "I just came by to give you this. I was already at the library, but Emera refused to let me drop it off there."

        Ry "I see."

        Ry smile "Hey, it's one of your PDAs. I told you one would find its way to me eventually."

        c "Yep, and now you can look at all the human knowledge you want."

        Ry normal "You have no idea how much I'm looking forward to that."

        Ry "I may not be working today, but I'm still going to check it out as soon as possible."

        c "I'm just going to leave you to it, then."

        Ry smile "Thanks."

        c "Enjoy."

        $ c4clues += 1

        $ renpy.pause (0.5)
    
        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

        jump c4sections
        
        
    elif remystatus == "none":
        
        show remy shy with dissolve
        
        Ry "Oh, it's you. I don't think it's a good time for you to visit right now, though."

        c "I just came by to give you this. I was already at the library, but Emera refused to let me drop it off there."

        Ry "I see."

        Ry normal "Oh, it's one of your PDAs. I was really looking forward to this."

        c "Well, here you go."

        Ry "Thanks for coming by."

        c "Enjoy."

        $ c4clues += 1

        $ renpy.pause (0.5)
    
        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

        jump c4sections
        
        
    else:
        
        stop music fadeout 2.0
        
        c "Is anybody home?"

        play sound "fx/knocking2.ogg"

        $ renpy.pause (2.5)
    
        c "(What? The door's unlocked.)"

        c "(Well, if he isn't here and left the door open, that's no good.)"

        m "I went inside and closed the door behind me."

        c "Remy? Are you there? Your front door was wide open."

        c "What the..."
        
        c "Remy!"
        
        $ remydead = True
            
        show remyhan at Pan ((250, 324), (250, 0), 8.0) with fade
        
        $ renpy.pause (5.0)
        
        scene black with dissolveslow
        
        $ renpy.pause (1.0)

        scene remyapt at Pan ((0, 80), (0,80), 0.0)
        
        show sebastian normal b
        
        with dissolveslow

        play music "mx/gravity.ogg" fadein 2.0
        
        Sb "How well did you know him?"
        
        menu:
            
            "A little.":
                
                pass
                
            "A lot.":
                
                pass
                
            "Not at all.":
                
                pass
    
        Sb "I see. Well, I know he met you when you initially arrived here, at the very least."

        Sb "It doesn't look like he left a suicide note or anything."

        Sb "I know he has no family, and I don't think he had many friends, either."

        Sb "Do you have any idea why he may have done this?"
        
        menu:
            
            "I have no idea.":
                
                Sb "I see."

                Sb "I suppose the reason doesn't really matter at this point. He's already gone."

                Sb "It's always a shame when things like this happen, when there are resources to help people who have issues and illnesses." 
                
                Sb "It's a mark on our society, a reminder that we let it happen. Someone suffered so much that they took their own life." 
                
                Sb "But what more can you do?"
                
            "I think he was dealing with a lot of things.":
                
                Sb "I see."

                Sb "I suppose the reason doesn't really matter at this point. He's already gone."

                Sb "It's always a shame when things like this happen, when there are resources to help people who have issues and illnesses." 
                
                Sb "It's a mark on our society, a reminder that we let it happen. Someone suffered so much that they took their own life." 
                
                Sb "But what more can you do?"
                
            "He was bullied.":
                
                Sb "Bullied? By whom?"

                c "Emera. He was constantly mistreated. She was beyond harsh."

                Sb "You think she was bullying him? That's a big accusation to make. You know who she is, right?"

                c "Yes, but I experienced it first-hand."

                Sb "If that was a cause for his suicide, that would be a very serious matter."

                c "I'm just saying how it is."

                Sb "Well, do you have any proof of this bullying you speak of? Do you know how long it was going on or how extensive it was?"

                c "No, not really. I only saw it myself once or twice."

                Sb "One or two instances of being scolded hardly constitutes bullying, especially if Emera had good reasons."

                Sb "Without hard proof, you can't make a case or accuse Emera of bullying."

                c "So, you can't really do anything?"

                Sb "I can't do anything if there isn't a case."

                Sb "I'd also recommend that you keep your opinion on this matter to yourself."

                c "Why?"

                Sb "Voicing an opinion like that without the evidence to back it up could have consequences. Especially if you're dealing with someone like Emera."

                c "I see."
                
        Sb "I'm sorry you had to find Remy like this, though."

        Sb "In any case, I'll handle the rest. Feel free to take the day off, if you need to."

        c "Alright." #
        
        stop music fadeout 2.0
                    
        $ renpy.pause (0.5)
    
        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed
        
        play music "mx/elegant.ogg" fadein 2.0

        jump c4sections    

            

label c4hatchery:

    scene town3 with dissolveslow

    m "I was on my way to the hatchery when I heard a voice call out to me."
    
    "???" "Hello there!"

    m "I turned around to see an unfamiliar face before me."
    
    show meetingkevin at Pan ( (400, 327), (300, 0), 8.0) with fade
    
    $ renpy.pause (6.5)
    
    hide meetingkevin 
    
    show kevin normal
    
    with fade
    
    Kv "Hey. I'm Kevin."

    c "[player_name]. Nice to meet you."

    Kv ramble "Could I perhaps interest you in our Midwest Institution?"

    c "Is this some kind of religious thing?"

    Kv "Not at all! It's a college."

    c "Sorry, but I already got my degrees."

    Kv face "Yeah, I know. It was just a joke."

    c "Oh, so me going to college is a joke now. I'm not good enough, is that it?"

    Kv normal "Not at all! Even if you wanted to study there, I don't think you'll be with us long enough to make use of it." 
    
    Kv face "I think that came out wrong."

    c "You're lucky I won't take this the wrong way."

    Kv normal "Phew."
    
    c "So, you're a recruiter for this college?"

    Kv ramble "No, this is just my summer job. Once the semester starts up again, I'll actually be attending to get my degree in psychology."

    c "College. Wonderful times."

    Kv brow "Is that sarcasm?"

    c "Maybe. I didn't even know you had colleges here, though."

    Kv ramble "Well, you do now."

    c "Why'd you even approach me if you know I'm not going to go to college here? Don't tell me it's just because I'm human."

    Kv normal "I was actually trying to talk to that old lady who walked by, but once you turned around there was no going back."

    c "Oh. Well, thanks for not making things awkward."

    Kv ramble "Hey, I treat everyone nicely until I have reason not to."

    c "That's good customer service."

    Kv normal "Sure, but it's not just for the job, you know. That's just me."
    
    menu:
        
        "Invite him.":
            
            c "Why don't you come over to my place later? I'd love to hear more about what college is all about in this world."

            Kv ramble "Then you found the right person for the job."

            c "I can't promise anything right now, but maybe I'll see you another time."

            Kv normal "For sure. I also have to finish this up here, but after that I'm free."

            c "Alright, I'll let you know."

            Kv ramble "I'm here all day today and tomorrow, so it shouldn't be hard to find me."

            c "Great. I have to get going now, but I'll be sure to let you know if anything's up."

            Kv normal "Sure. See ya!"

            $ kevinavailable = True
            
        "Excuse yourself.":
            
            c "Oh, I should really be going. I have some things to take care of."

            Kv ramble "Alright, no problem. See ya!"

    
    scene black with dissolvemed
    
    $ renpy.pause (0.5)
    
    scene hatchery at Pan ((0, 0), (0, 180), 3.0) with dissolveslow

    $ renpy.pause (1.3)
    
    c "(Here we are again.)"
    
    show adine normal b with dissolve 
    
    if adinestatus == "bad":
        
        Ad annoyed b "[player_name]? What are you doing here?"
        
        c "I'm just dropping these off."

        Ad think b "Dropping what off?"

        c "The stolen eggs. I figured the hatchery would want them back."

        Ad normal b "Oh, I was actually going to get those from the police department later."

        Ad "I'm just glad that they got back safely."

        Ad giggle b "Amely, stop chewing my leg!"
        
        hide adine with dissolve
                
        show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='bottom') with ease
        
        show amely normal flip with dissolve
        
        Am "It tasty!"
        
        hide amely with dissolve
        
        show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.15, yanchor='bottom') with ease
                
        show adine giggle b with dissolve
        
        Ad "Oh well..."

        Ad normal b "Anyway, I was about to go inside, so I'll take those off your hands."

        Ad "Thanks for bringing them here."

        c "No problem."

        $ c4clues += 1
        
        hide adine with dissolve
        
        $ renpy.pause (0.5)


        if persistent.c4eggs == False:

            $ persistent.c4eggs = True
            
            $ achievement.grant("In Loco Parentis")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_78
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You returned the eggs to the hatchery!"
                
            elif system == "advanced":

                s "You returned the eggs to the hatchery. Egg-straordinary."
                
            else:
                
                s "You returned the eggs to the hatchery. Egg-straordinary."

    
        show black with dissolvemed

        $ renpy.pause (0.5)

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

        jump c4sections    
        
        
    elif adinestatus == "abandoned":
        
        Ad "Hey, [player_name]! What are you doing here?"

        c "Oh, I just came by to drop these off."

        Ad think b "Drop what off?"

        c "The stolen eggs. I figured the hatchery would want them back."

        Ad normal b "Oh, I was actually going to get those from the police department later."

        Ad "I'm so glad that they got back safely."

        Ad giggle b "Amely, stop chewing my leg!"
    
        hide adine with dissolve
                
        show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='bottom') with ease
        
        show amely normal flip with dissolve
        
        Am "It tasty!"
        
        hide amely with dissolve
        
        show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.15, yanchor='bottom') with ease
                
        show adine giggle b with dissolve
        
        Ad "Oh well..."

        Ad think b "By the way, I haven't seen you for a while, and you didn't call me back, either..."

        $ c4clues += 1
        
        menu:
            
            "Sorry, I was just busy.":
                
                c "Sorry, I was just busy. I'm helping the police department with the investigation, and I still have my ambassador duties to deal with. I didn't have much free time."

                Ad normal b "Oh, I understand. My invitation still stands if you want to come by."

                c "Sure, maybe I will."

                Ad "Great!"

                Ad "Anyway, I was about to go inside, so I'll take those eggs off your hands."

                Ad "Thanks for bringing them here."

                c "No problem."
                
                hide adine with dissolve
                            
                $ adinestatus = "neutral"
            
                $ renpy.pause (0.5)

                if persistent.c4eggs == False:

                    $ persistent.c4eggs = True
                    
                    $ achievement.grant("In Loco Parentis")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_79
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You returned the eggs to the hatchery!"
                        
                    elif system == "advanced":

                        s "You returned the eggs to the hatchery. Egg-straordinary."
                        
                    else:
                        
                        s "You returned the eggs to the hatchery. Egg-straordinary."
            
                show black with dissolvemed

                $ renpy.pause (0.5)

                scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

                jump c4sections  
            
                
            "I don't want to meet you again.":
                
                c "I'm not sure how to say this, but..."

                Ad disappoint b "Oh, I see."

                Ad "Well, you could've at least told me instead of ignoring me."

                c "I told you now, didn't I?"

                Ad "Oh, well. I won't bother you anymore, then."

                Ad "Anyway, I was about to go inside, so I'll take those eggs off your hands."

                Ad "Thanks for bringing them here."

                c "No problem."
            
                hide adine with dissolve
                            
                $ adinestatus = "neutral"
            
                $ renpy.pause (0.5)



                if persistent.c4eggs == False:

                    $ persistent.c4eggs = True
                    
                    $ achievement.grant("In Loco Parentis")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_80
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You returned the eggs to the hatchery!"
                        
                    elif system == "advanced":

                        s "You returned the eggs to the hatchery. Egg-straordinary."
                        
                    else:
                        
                        s "You returned the eggs to the hatchery. Egg-straordinary."

    
                show black with dissolvemed

                $ renpy.pause (0.5)

                scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

                jump c4sections  
            
            
    elif adinestatus == "none":

        Ad "Hey! [player_name], right? What are you doing here?"

        c "Oh, I just came by to drop these off."

        Ad think b "Drop what off?"

        c "The stolen eggs. I figured the hatchery would want them back."

        Ad normal b "Oh, I was actually going to get those from the police department later."

        Ad "I'm so glad that they got back safely."

        Ad giggle b "Amely, stop chewing my leg!"

        hide adine with dissolve
            
        show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='bottom') with ease
        
        show amely normal flip with dissolve
        
        Am "It tasty!"
        
        hide amely with dissolve
        
        show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.15, yanchor='bottom') with ease
                
        show adine giggle b with dissolve
        
        Ad "Oh well..."
        
        Ad normal b "Anyway, I was about to go inside, so I'll take those off your hands."

        Ad "Thanks for bringing them here."

        c "No problem."


        if persistent.c4eggs == False:

            $ persistent.c4eggs = True
            
            $ achievement.grant("In Loco Parentis")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_81
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You returned the eggs to the hatchery!"
                
            elif system == "advanced":

                s "You returned the eggs to the hatchery. Egg-straordinary."
                
            else:
                
                s "You returned the eggs to the hatchery. Egg-straordinary."


        $ c4clues += 1
        
        if remystatus == "bad":
            
            hide adine with dissolve
        
            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections
            
        elif remystatus == "abandoned":
            
            hide adine with dissolve
        
            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections

        elif remygoodending == True:
            
            Ry "Adine! Wait for me."
            
            show adine at right with ease
            
            show remy normal flip at left with easeinleft
            
            Ry smile flip "Good job, [player_name]."

            c "Looks like you took my advice."

            Ry normal flip "Yeah, Adine and I had a good, long talk - and now here we are."

            Ad "I'm glad we did. It was long overdue."
            
            show vara normal flip at Position (xpos = 0.05) with easeinleft
            
            Vr "..."

            Ry "Vara, do you know who that is? Hmm?"

            Vr "..."

            Ry "She doesn't talk much."

            c "Yeah, I noticed."
            
            Ry "It's not unusual for someone who's had a rough life like hers."

            Ry smile flip "She's definitely listening, though. Isn't that right?"

            Vr "..."

            Ad "I think we should go inside."

            Ry normal flip "Yeah, probably."

            Ry smile flip "Well, see you some other time, [player_name]."

            Ad "Thanks for coming!"
            
            hide vara with dissolve
            
            hide adine with dissolve
            
            hide remy with dissolve

            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections  


        elif persistent.remygoodending == True:
            
            Ry "Adine! Wait for me."
            
            show adine at right with ease
            
            show remy normal flip at left with easeinleft
            
            Ry smile flip "Good job, [player_name]."

            #c "Hey, Remy. What are you doing here?"

            #Ry normal flip "Yeah, me and Adine had a good, long talk, and now here we are."

            #Ad "I'm glad we did."
            
            show vara normal flip at Position (xpos = 0.05) with easeinleft
            
            Vr "..."

            Ry "Vara, do you know who that is? Hmm?"

            Vr "..."

            Ry "She doesn't talk much."

            #c "Yeah, I noticed."
            
            #Ry "It's not unusual for someone who's had a rough life like her."

            #Ry smile flip "She's definitely listening, though. Isn't that right?"

            #Vr "..."

            Ad "I think we should go inside."

            Ry normal flip "Yeah, probably."

            Ry smile flip "Well, see you some other time, [player_name]."

            Ad "Thanks for coming!"
            
            hide vara with dissolve
            
            hide adine with dissolve
            
            hide remy with dissolve

            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections  
                                
            
        else:
            
            
            
            hide adine with dissolve
        
            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections  
            
                
    else:
        
        
        Ad "Hey, [player_name]! What are you doing here?"

        c "Oh, I just came by to drop these off."

        Ad think b "Drop what off?"

        c "The stolen eggs. I figured the hatchery would want them back."

        Ad normal b "Oh, I was actually going to get those from the police department later."

        Ad "I'm so glad that they got back safely."

        Ad giggle b "Amely, stop chewing my leg!"

        hide adine with dissolve
            
        show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='bottom') with ease
        
        show amely normal flip with dissolve
        
        Am "It tasty!"
        
        hide amely with dissolve
        
        #"bobley"
        
        show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.15, yanchor='bottom') with ease
                
        show adine giggle b with dissolve
        
        Ad "Oh well..."
        
        Ad normal b "Anyway, I was about to go inside, so I'll take those off your hands."

        Ad "Thanks for bringing them here."

        c "No problem."

        if persistent.c4eggs == False:

            $ persistent.c4eggs = True
            
            $ achievement.grant("In Loco Parentis")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_82
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You returned the eggs to the hatchery!"
                
            elif system == "advanced":

                s "You returned the eggs to the hatchery. Egg-straordinary."
                
            else:
                
                s "You returned the eggs to the hatchery. Egg-straordinary."

        $ c4clues += 1

        if remystatus == "bad":
            
            hide adine with dissolve
        
            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections
            
        elif remystatus == "abandoned":
            
            hide adine with dissolve
        
            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections

        elif remygoodending == True:
            
            Ry "Adine! Wait for me."
            
            show adine at right with ease
            
            show remy normal flip at left with easeinleft
            
            Ry smile flip "Good job, [player_name]."

            c "Looks like you took my advice."

            Ry normal flip "Yeah, Adine and I had a good, long talk - and now here we are."

            Ad "I'm glad we did. It was long overdue."
            
            show vara normal flip at Position (xpos = 0.05) with easeinleft
            
            Vr "..."

            Ry "Vara, do you know who that is? Hmm?"

            Vr "..."

            Ry "She doesn't talk much."

            c "Yeah, I noticed."
            
            Ry "It's not unusual for someone who's had a rough life like her."

            Ry smile flip "She's definitely listening, though. Isn't that right?"

            Vr "..."

            Ad "I think we should go inside."

            Ry normal flip "Yeah, probably."

            Ry smile flip "Well, see you some other time, [player_name]."

            Ad "Thanks for coming!"
            
            hide vara with dissolve
            
            hide adine with dissolve
            
            hide remy with dissolve

            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections  


        elif persistent.remygoodending == True:
            
            Ry "Adine! Wait for me."
            
            show adine at right with ease
            
            show remy normal flip at left with easeinleft
            
            Ry smile flip "Good job, [player_name]."

            #c "Hey, Remy. What are you doing here?"

            #Ry normal flip "Yeah, me and Adine had a good, long talk, and now here we are."

            #Ad "I'm glad we did."
            
            show vara normal flip at Position (xpos = 0.05) with easeinleft
            
            Vr "..."

            Ry "Vara, do you know who that is? Hmm?"

            Vr "..."

            Ry "She doesn't talk much."

            #c "Yeah, I noticed."
            
            #Ry "It's not unusual for someone who's had a rough life like her."

            #Ry smile flip "She's definitely listening, though. Isn't that right?"

            #Vr "..."

            Ad "I think we should go inside."

            Ry normal flip "Yeah, probably."

            Ry smile flip "Well, see you some other time, [player_name]."

            Ad "Thanks for coming!"
            
            hide vara with dissolve
            
            hide adine with dissolve
            
            hide remy with dissolve

            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections  
                                
            
        else:
            
            
            
            hide adine with dissolve
        
            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

            jump c4sections  
                
            
            
#what are the conditions? We must've played remy 3, remy must be neutral or good, and vara must have been saved            

label c4rest:
    
    scene o at Pan((0, 100), (0, 250), 3.0) with dissolveslow

    $ renpy.pause (1.3)
    
    m "I decided to take a long break in my apartment. I had already done enough for the day and figured I should take some time off."

    m "I looked at the bookshelf for new reading material, yet found that none of the books I hadn't already read particularly interested me."

    $ persistent.lazynumber += 1
    call lazycheck from _call_lazycheck_7

    $ renpy.pause (0.5)

    show black with dissolvemed

    $ renpy.pause (0.5)

    scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

    jump c4sections

    #if persistent.ixomenbookread == True:
        
    #    if persistent.base_taken == True:
            
    #        if persistent.orb_taken == True:
                
    #            if persistent.ixomenassembled == False:
                
    #                m "However, when my eyes fell on the Ixomen Sphere manual, I remembered that I had gathered some parts that I recognized from it."

    #                m "Using the manual, I set to work to reassemble the parts into an Ixomen Sphere as instructed."

    #                m "It turned out that I had gathered all the necessary parts, and in the end, the Ixomen sphere was complete, functional and ready to be powered on, except that I just had no idea how, as the manual told me that the method varied wildly by model."

    #                m "Maybe it was for the better, considering I still had no idea what an Ixomen Sphere actually was."
                    
    #                $ persistent.ixomenassembled = True
                    
    #                $ achievement.grant("Sphere Builder")
            
    #                $ persistent.achievements += 1
                    
    #                call syscheck
                    
    #                play sound "fx/system.wav"
                    
    #                if system == "normal":
                    
    #                    s "You have assembled the Ixomen Sphere!"
                        
    #                elif system == "advanced":

    #                    s "You have assembled the Ixomen Sphere. Hy-spherical!"
                        
    #                else:
                        
    #                    s "You have assembled the Ixomen Sphere. Hy-spherical!"
                    
    #                $ renpy.pause (0.5)
        
    #                show black with dissolvemed

    #                $ c4clues += 2
                    
                    #insert steam achievement here

    #                $ renpy.pause (0.5)

    #                scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

    #                jump c4sections  
                    
    #            else:
                    
    #                $ renpy.pause (0.5)

    #                show black with dissolvemed

    #                $ renpy.pause (0.5)

    #                scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

    #                jump c4sections
                    
    #        else:
                
    #            m "However, when my eyes fell on the Ixomen Sphere manual, I remembered that I had gathered some parts that I recognized from it."

    #            m "Using the manual, I set to work to reassemble the parts into an Ixomen Sphere as instructed."

    #            m "It soon turned out that I didn't have all the necessary parts that were listed in the manual, though, and I was left with an incomplete Ixomen Sphere."
                
    #            $ renpy.pause (0.5)
    
    #            show black with dissolvemed

    #            $ renpy.pause (0.5)

    #            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

    #            jump c4sections  
                
    #    else:

    #        if persistent.orb_taken == True:

    #            m "However, when my eyes fell on the Ixomen Sphere manual, I remembered that I had gathered some parts that I recognized from it."

    #            m "Using the manual, I set to work to reassemble the parts into an Ixomen Sphere as instructed."

    #            m "It soon turned out that I didn't have all the necessary parts that were listed in the manual, though, and I was left with an incomplete Ixomen Sphere."
                
    #            $ renpy.pause (0.5)
    
    #            show black with dissolvemed

    #            $ renpy.pause (0.5)

    #            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

    #            jump c4sections  
                
    #        else:
                
    #            $ renpy.pause (0.5)

    #            show black with dissolvemed

    #            $ renpy.pause (0.5)

    #            scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

    #            jump c4sections
    
    
    
    #else:
        
    #    $ renpy.pause (0.5)

    #    show black with dissolvemed

    #    $ renpy.pause (0.5)

    #    scene office at Pan ((128, 250), (0, 250), 3.0) with dissolvemed

    #    jump c4sections
        




label c4postsections:

if persistent.remygoodending == False:
    if remystatus == "abandoned":
        $ remydead = True

    elif remystatus == "bad":
        $ remydead = True
    
$ renpy.pause (2.0)

show sebastian normal b with dissolve

Sb "Thanks for all your help."

if c4facilityavailable == False:
    
    Sb "Now that the facility has received the bandage, maybe we'll discover something new."
    
    if c4bandagerejected == True:
        
        c "I'm afraid that's not the case. I brought the bandage back."

        Sb "What? Why?"

        c "I'm not sure what's going on, but apparently the police raided Anna's lab, so she wasn't in a condition to accept it."

        Sb "Is that so? Strange, I hadn't heard about this. I'll have to talk to the others. Actions like that will stall the Reza case, and that's not something we can afford right now."
        
    else:
        
        pass
        
#$ c4libraryavailable = False

#$ c4hatcheryplayed = True

Sb "I'll take care of the remaining tasks, so you can take the rest of the day off. I'm sure you have things to do other than helping the police department."

c "It's no problem, really. My trip to your world wasn't supposed to be a vacation."

Sb "Alright, then. I'll see you next time."

c "See you."

stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolvemed

$ renpy.pause (0.5)

scene o at Pan((0, 100), (0, 250), 3.0) with dissolveslow

$ renpy.pause (1.3)

m "After this fateful day, I was glad to finally have some sort of respite. I wandered into the kitchen as I considered tonight's dinner."

c "(Should I cook something or order out?)"

m "When I returned to the living room, I suddenly found my strength leaving me and collapsed to the floor."

stop music fadeout 1.0

scene black with dissolve

play sound "fx/impact.wav"

$ renpy.pause (4.5)

scene cave with dissolveslow

$ renpy.pause (0.3)

m "The next thing I saw was a blurry stone ceiling."

m "As my eyesight slowly returned, I managed to sit up. I was in a cave, and before me stood a familiar, mysterious face."

play music "mx/judgement.ogg" fadein 2.0

show izumi normal with dissolve

"???" "I apologize for the violence, but I can assure you it was the easiest way."

if persistent.c4skip == True:

    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_83

    call skiptut from _call_skiptut_21
        
    if skipbeginning == False:

        if system == "normal":
        
            s "My records indicate you have already experienced this section in a satisfactory manner. Would you like to skip to the character selection?"
        
            #play sound "fx/system3.wav" #was already blanked out here
        
            #s "Warning: In this scene, skipping ahead this way instead of using the skip buttons (CTRL and TAB) may prevent you from experiencing alternative choices and outcomes that you haven't seen before. These may only be minor, though."
        
        elif system == "advanced":

            s "It looks like you've seen this before. Skip to the character selection?"
        
            #play sound "fx/system3.wav" #was already blanked out here
        
            #s "I have to warn you, though. If you do this here instead of just using CTRL and TAB, you may end up missing some minor changes you haven't seen before."
            
        else:
            
            s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the character selection."
            
            #play sound "fx/system3.wav" #was already blanked out here
            
            #s "If you want to do things this way instead of just using the skip buttons like a civilized person, you could end up missing some choices you haven't made before. But considering how far you've come, you probably won't miss much."
        
    $ skipbeginning = False
    
    menu:
        
        "Yes. I want to skip ahead.":
            
            play sound "fx/system3.wav"
            
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            
            scene black with dissolvemed

            $ renpy.pause (1.0)
            
            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_21
            
            nvl clear
            
            jump c4skip2
            
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            
            play music "mx/judgement.ogg" fadein 2.0
            
c "Where am I? Is this your hideout?"

"???" "Just a temporary accomodation so we can be undisturbed for this meeting. Someone else used to live here until recently."

"???" "Do you know who I am?"

c "Well, you're not Reza." 

"???" "Good. What did it take for you to figure that out?"

c "Since you're not whispering anymore, I can hear it clearly in your voice. I had a feeling that you couldn't be him since the first time we met, though."

"???" "Which first time are you talking about?" 

c "The generator in the cellar, when you pushed me." 

#different answer if on true ending path

"???" "I see."

"???" "You can call me the Administrator."

c "No other humans are supposed to be here, though. I assume that's why you're wearing the mask. You don't want to be recognized."

As "That is correct."

c "Whoever you are, you also saved my life."

As "On more than one occasion."

c "Your presence here doesn't make any sense. You couldn't have come through the portal. The dragons would have noticed."

As "This is where you are wrong. My arrival through the portal is what led the dragons to discover it in the first place."

c "Is that so?"

As "When I crawled out from the hole in the earth that hid the portal, there were no guards to discover me. My appearance exposed the portal, but the dragons didn't know it was there yet."

c "So you arrived even before Reza. That makes you the actual first human to come to this world."

As "That is more true than you might think."

c "Just who are you, then?"

As "I may have arrived through the portal like you, but my story is very different."

stop music fadeout 2.0

scene black with dissolveslow

$ renpy.pause (1.0)

window show

play music "mx/soul.ogg" fadein 2.0

n "Before the fall of humanity, I was an engineer. I was part of a team that was formed to create bioweapons."

n "Our task was to create these bioweapons in a country where their development hadn't yet been regulated or outlawed. These weapons were planned to be a low-cost alternative for poor countries to wage war, so they would no longer have to rely on expensive drones and machines for warfare."

n "I was to set up the lab where our bioweapon development would take place. It was a clandestine operation, set to be in the middle of the wilderness."

n "The laboratory was an independent research and living unit, and provided everything we needed without having to rely on external resources or even an existing power grid."

#scene black with dissolve
window hide
nvl clear
#$ renpy.pause (0.5)
window show

n "Everything was to be teleported right into the middle of nowhere, with no traces or paper trail to follow, so international communities and law enforcement would have no idea of our operations."

n "Our only connection to the outside world after setup would have been a two-way portal to our headquarters, who would provide everything we needed."

n "While we already could teleport individual people, teleporting a whole building was another matter entirely."

n "Our solution was matter compression technology. Incredibly expensive, but operating in the grey market was also very lucrative."

n "The technology behind it was much more complicated than even teleportation, despite being based on it."

#scene black with dissolve
window hide
nvl clear
window show

n "While teleportation works by utilizing black holes with a beginning and an end, compression technology relies on a loop, keeping matter in a sort of limbo state until the loop is broken."

n "Working with black holes was very complicated to begin with, but this shape required much more finesse, and thus was much more expensive."

n "I was to be sent alone to setup the lab and the portal so the rest of the team could arrive safely."

n "In case you didn't know, it is possible to use a portal to send someone to a previously defined end point. Therefore, it is not required to have a portal at the destination to be sent there, but as you can imagine, this is also very dangerous."

n "A single variable off by a fraction could mean the difference between landing safely at your destination and smothering in space."

window hide
nvl clear
window show

n "Of course, my employer did not want anything like that to happen. Not necessarily for my own sake, but because of all the unfathomably expensive equipment I had with me."

n "Regardless, something went wrong, anyway. Despite all their checks and safeguards, they could only minimize the risk so much. Even if the risk is a fraction of a fraction, sometimes you are just that unlucky."

n "And sometimes, it turns out that your bad luck is a blessing in disguise."

n "I arrived safely somewhere in the jungles of Earth, yet it was not the destination that had been planned."

n "I knew something was off, but nevertheless, I set to work immediately. At the very least, I could prepare the building. I would have shelter, and then I could begin preparations for our project. Getting the portal into working order would take more time as it was a complicated process that could take several weeks."

window hide
nvl clear
window show

n "If things had gone wrong as I suspected, I would at least be able to establish contact with headquarters after the portal had been set up, and I would be able to return."

n "While teleporting the lab to the wrong location was certainly a costly mistake, I was still lucky to have my life."

n "Before long, I discovered the truth about the place I had arrived."

n "While I was still on Earth, it was not the Earth I knew."

n "It was the Earth of 65 million years ago."

window hide
nvl clear
window show

n "We knew that by utilizing black holes for teleportation, time travel was a theoretical possibility. It was something even my company didn't dare to attempt, though, as teleportation in itself was still a very new technology."

n "Yet here I was, 65 million years in the past, with a research station all to myself. The company would revel in the opportunity to study and profit from all the different lifeforms I could see." 

n "If only they knew about them."

n "I spent the few weeks setting up the portal as planned, yet when I tried to reestablish contact with my employer, I was met with silence."

window hide
nvl clear
window show

n "Despite the time discrepancy, the portal should have been able to find my company's in the present. For a black hole, sending something through time is no different than sending something through space."

n "However, when we built the portals, we gave them a specialized configuration. It was only possible to travel through space by aligning them across the time axis."

n "That meant that I, in the past, would still be able to search for portals in the present to connect with. My counterparts in the present, though, would not be able to find me in the past even if they tried."

n "But I couldn't find them. Not a single one. Even after checking the portal for its function, I determined that - for all intents and purposes - the portals from the company should have been there to connect with."

window hide
nvl clear
window show

n "It was then that I had a terrible realization: The portals in the present didn't exist anymore, or were no longer operational."


n "Maybe the blunder of teleporting the lab caused them to reconsider the risks of using this technology. After all, it was already controversial and had been outlawed in several countries."

n "I wouldn't have been surprised if they decided to cut their losses, but it was highly unlikely that they would have immediately shut down every single portal and left me stranded without notice. Portal technology was still being relied on in several places in the present."

n "In my mind, only one possibility remained: Superweapons. Various nations had been using them as bargaining chips for some time. I didn't think the threats had become that serious, but one of them must have launched their weapon and destroyed the majority of Earth."

window hide
nvl clear
window show

n "It could have been the result of a malfunction, or perhaps the political situation had escalated."

n "Either way, it was not possible for me to establish any means of communication to find out what had really happened."

n "I could have sent myself back into the present with the right coordinates, but this was a risky endeavor, and I also had to ask myself if it was a present I wanted to return to."

n "I was sure that if anything was even left of our world, the aftermath or a possible retaliatory strike would take care of the rest."

window hide
nvl clear
window show

n "In the end, I had to realize that whichever present did exist was likely not one that was worth returning to. It made my decision all the easier."

n "Instead of returning to a destroyed civilization, I saw an opportunity."

n "Rather than creating bioweapons, I could use the lab to create a new civilization, shaped by my own ideals."

n "I had all the necessary data and the most modern methods and machines at my fingertips."

n "Besides, most of the processes had already been automated."

window hide
nvl clear
window show

n "In the end, I still used the lab for what it had been created for: Fusing human and animal DNA to create beings that were mostly animal, but possessed a greater intelligence that allowed them to learn whatever we wanted them to."

n "As I didn't have any animal samples sent with me when I initially arrived, I collected them from the sources available to me."

n "Automated processes mixed the DNA further across the samples. New abilities were added like enhanced armor, flight, and spit weapons to make the new creatures more effective in combat."

n "The result was a number of different species, each tailored and optimized to fill a specific role in a war situation."

n "Hormones allowed me to speed up their growth, and with the lab's learning program, they could be educated in whatever manner I saw fit."

window hide
nvl clear
window show

n "My first concern was self-sufficiency."

n "They needed the kind of knowledge that would enable them to come together as their own, independent society."

n "Luckily, the AI that automated all the processes in the lab was more than helpful."

n "I unleashed the first generation of my creation, and as their leader, founded our first village."

n "I thought we could really pull it off. And once I saw that they could survive without my guidance - and also govern themselves - I knew my plan was a success."

stop music fadeout 2.0

window hide

nvl clear

$ renpy.pause (1.5)

show cave

show izumi normal

with dissolveslow

play music "mx/judgement.ogg" fadein 2.0

As "When I realized that this new society would eventually be destroyed, I told myself that I would do anything I could to save it."

c "Destroyed? What are you talking about?"

As "Haven't you realized where we are?"

As "The Chicxulub asteroid is headed for us."

As "With a diameter of over 10km, its impact will create humongous clouds of dust, throwing Earth into a literal dark age."

As "They will block out the sunlight for over a year, killing off many species of plants that rely on photosynthesis to survive."

As "As a result, animals that eat those plants will also vanish, as will those who sought sustenance from these herbivores."

As "All in all, 75%% of all species will vanish, and in terrestrial ecosystems, all animals heavier than a single kilogram will die."

As "That would be 2.2 pounds, in case you didn't know."

As "It will be the end of everyone who lives here, every single dragon you have seen - unless we do something."

c "We? What am I supposed to do?"

As "Do you not wish to save them?"

c "I came here to help humanity. Now you tell me that this society - this whole world - is also on the brink of extinction?"

As "That is the truth."

c "What kind of difference could a single person like me even make to save it?"

As "Right now, it's also a single person that presents its greatest threat."

c "Reza? How?"

As "In order to stop the comet, we will need as much power as possible."

c "We reclaimed all the generators he stole. Besides, how could a few of them be enough to make a difference for something like this?"

As "Don't forget that Reza is still out there, looking for more. The truth is: I don't know if all the generators we could gather would ever be enough." 

As "We only require enough power to divert the comet's path during a crucial moment, but even if this plan is possible, we will need every single generator we can get."

c "So my goal hasn't changed. I just need to find Reza."

As "Yes, but you'll need my help, and maybe the help of others. You know that Reza is dangerous, and with his gun, he has a clear advantage."

As "Don't think that he wouldn't hesitate to kill you if you were in his way."

c "Then what shall we do? Do you know where he is?"

As "No, but I think you'll find him soon, and you can count on my support when that happens."

c "I see."

c "There is one thing that still doesn't make sense to me, though."

c "The dragons have myths about you, but they don't know or remember you. They haven't seen any humans for who knows how long. How much time could have passed since you created them and now?"

c "How many generations could it take to forget? Why isn't there proof of your existence?"

As "I don't know exactly how long it's been, myself. When I realized what time period I was in and that my creation was about to be wiped out in the future, I wanted to go to that future and see what they had become."

As "I disabled the portal's time axis safeguards, and thus enabled it to connect with others in different times."

As "This also included that very same portal in the future."

As "With the generator of our lab being able to supply the portal with power for an indefinite amount of time, I was able to travel to any point in the future I wanted to." 

As "The entry and end point of the black hole would be the same place and the same portal, with the way travelled being just along the time axis."

As "Since I could now search for connection points in any time period, I could look for my own portal in the future and pinpoint the moment its signal stopped."

c "The comet."

As "Exactly."

As "I found that specific point in time and traveled to a future that was as close to that event as I could safely manage."

As "After I arrived here, my escape from the portal's hiding place led to its discovery by the dragons. It and the laboratory were unearthed."

c "I still don't understand how our portal found yours, or why we ended up arriving at this particular time period."

As "The portal you found was no doubt one of my company's. They must have been connected before, so the corresponding data for their connection already existed when you found it." 

As "I'm not sure if that could bypass the anti-time travel safeguards, though."

As "Was it completely operational when you found it?"

c "No, it took a little bit of tinkering."

As "Probably jumping the hardware safeguard in the process."

As "Now, consider that connected portals travel along the time axis together. The data for their beginning and end points are adjusted automatically." 

As "Otherwise, we wouldn't be able to transport anything from one place in the world to another without also sending it through time."

As "Since these two portals must have been connected at some point, the corresponding data for the connection between those two portals already existed." 

As "When using the same connection without changing any of the data, this would mean that despite the time discrepancy between those two portals, time still progressed linearly for them."

c "I'm not sure I understand."

As "Let me try to rephrase that. The portal you found and my own share a connection. However, while the connection is locked to a certain place, which is wherever the portal is at that very moment, it is not connected to a specific point in time."

As "For us and the physical machines that are the portals, time passes linearly and we can't do anything about that. However, for the black holes this isn't the case." 

As "Just as their entry and end points can be in different places, they can also be in different times." 

As "In order to not send something through time when we just want to transport something from one portal to another, the portals are anchored together in such a way that the time data is automatically synchronized."

As "Essentially, this means that ever since you arrived in this world, the same amount of time that has passed for you has also passed in the place where you came from."
 
c "I see, so despite being in different time periods, time still passes linearly on both sides of the portals."

As "Otherwise it would not have been possible for you to send messages back and forth to each other." 

As "If they were not synchronized, the portals on both sides would stay connected not only to a single point in space, but also to a single point in time, thus making proper two-way communication impossible."

As "However, this is only possible through the connection that has already been forged. If we wanted to, we could also use our portal to send you back to your own time period, but to a moment before Reza even arrived here."

c "But that would mean there would be two of me, right? Wouldn't that cause a time paradox?"

As "I can only tell you that it would work. No one has studied time travel before, though, so if there are any consequences, then I am not sure of them. Most likely, an entirely new timeline would be created."

As "There would be a timeline without a [player_name] altogether, and in the new one, there would be two of you."

c "This is becoming way too complicated."

As "I apologize. To come back to your original question, I am not sure how much time passed between the time I left my newborn society and now." 

As "Since the portal was not designed for time travel, I have no way of knowing how the variables translated to our perception of time."

As "It could have been thousands or even millions of years."

c "How could the portal or even its power source still be operational after all this time?"

As "The portal receives its power from the generator in the lab. These units were fitted with the absolute best technology we had to offer."

As "It was designed to provide sustainable power completely independently from any already existing network or power lines. It gains energy from many sources - sun rays, earth's heat and movement, just to name a few."

As "Keep in mind it had to power a whole laboratory and research station, while also providing the energy required for all of its inhabitants and the associated energy expenditures." 

As "Taking its power from Earth itself, a generator like this could continue providing power to the lab indefinitely."

c "Speaking of which, why haven't I seen a single dinosaur since I arrived?"

As "It seems that the dragons' society expanded over the whole continent." 

As "Many still hunt on their own for sustenance, and as such, the original species they were based on have mostly vanished, as in direct competition, ours proved to be far superior."

As "Also, they have probably taken measures against having big predators roam their cities and villages."

As "Yet while the dragon population has increased tremendously, I have found that by and large, their society as whole has not changed much."

c "Is that why everything here looks like it was made for humans?"

As "I suppose so. The learning program I initially used gave them knowledge about things and how to create them, yet of course those were only human inventions and designs."

c "Did they never once stop to think that they should adjust how certain things look? A lot of the furniture and objects I've seen look very impractical for a dragon."

As "I was surprised at that too, but I have an explanation for this phenomenon. Don't forget that their genome was designed by an AI programmed to make them into effective bioweapons."

As "The idea was to have them indoctrinated at a young age." 

As "After reaching adolescence, their learning capacity would be greatly diminished. This resulted in subjects that would stay loyal and be unlikely to change their desired behaviors."

As "Instincts also play a role. I imagine they are very much at odds with their learned behavior. Instincts in animals never change, and instinctual behaviors will always be there."

As "If a given trait has been programmed into their genome as an instinct, it is not very likely to change, even through numerous generations."

As "We can see the result of this here. While I initially made them learn a certain set of values and knowledge, I have found that the expression of those ideas has hardly changed."

As "And after I was gone, each new generation learned from its elders and much of the initial knowledge and information was retained through all this time."

As "Their genome as a whole did change, however - which was unavoidable over time. If they had been used as bioweapons as intended, they would have been nothing more than an army of identical clones."

As "While I can see subtle changes in behaviors as a result, some traits are still very much present in them. They are content with what they have and don't strive for more."

As "They don't innovate or change, so technological breakthroughs or new inventions are a rarity. It's quite the opposite, really. They very much value tradition and their ways which have not changed much in all these years."


c "I see."

c "How much time do we even have left to stop the comet?"

As "In a few weeks, the comet will pass the moon, and its gravity field will point the comet's trajectory toward Earth. This is when we will need to be ready." 

As "If we strike then, we only need to minimally affect its path in order for the comet to pass Earth safely." 

As "It won't be enough time for the inhabitants of this world to prepare if Reza steals our greatest assets."

c "So it's all about Reza and the generators, isn't it?"

As "Indeed."

As "By the way, I fixed the portal in case we need to use it."

c "Did you break it to prevent me from being sent away?"

As "No, that wasn't me."

c "Reza better not use it to escape."

As "Trust me, the portal is our greatest asset."

As "I have programmed it with emergency coordinates. If you should find yourself in a hopeless situation and feel there is no other way out, go to the portal. I have made sure only you will be able to use them."

c "I'll keep that in mind." 

c "So, what's your plan? What do we do now?"

As "I will resume my work, and you will continue yours. Find Reza."

m "The Administrator turned to leave."

$ renpy.pause (0.3)

show izumi normal flip

$ renpy.pause (0.3)

c "Wait. What's with all the secrecy? Why are you still wearing that mask? Why don't we pool our resources together and you show me your hideout?" 

c "Don't you think it would be better if you were completely frank with me?"

As "No. Not now."

hide izumi with easeoutright

$ renpy.pause (0.3)

m "A second later the figure had already vanished into the darkness outside."

stop music fadeout 1.0

scene forestx at Pan((0, 0), (0, 0), 0.0) with dissolvemed

play music "mx/amb/night.ogg" fadein 5.0

m "When I followed, I realized that I wasn't sure how to get back to my apartment."

m "Surrounded by trees and the blanket of night, it was hard to make out where I stood."

scene town1x at Pan((0, 0), (0, 0), 0.0) with dissolvemed

m "After wandering through the underbrush, I realized that the lights on the horizon had to be coming from the village, and made my way back."

stop music fadeout 2.0

scene o3 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

m "I returned to my apartment without much trouble. When I looked at the clock, I was surprised to see how much time had passed."

m "Not having anything left to do for the day, I soon fell into a deep slumber."

scene o3 at Pan((0, 250), (0, 0), 5.0)

$ renpy.pause (2.0)

scene black with dissolveslow

$ renpy.pause (1.0)

label c4skip2:

#if c4clues >= 2:
    
#    $ persistent.c4skip = True

$ persistent.c4skip = True

scene o4 at Pan((0, 250), (0, 250), 0.0) with dissolveslow

c "(Seems there's nothing for me to do this morning. I guess they don't need me at the police department. Not that I mind.)"

$ c4csplayed = 0
$ c4unplayed = False

label chapter4chars:

$ save_name = "Chapter 4"

if c4csplayed == 1:
        
    scene black with dissolveslow
    $ renpy.pause (1.0)
    scene o4 at Pan((0, 250), (0, 250), 0.1) with dissolvemed

elif c4csplayed == 0:
    
    pass
    
else:
    
    jump chapter5

$ playmessage = False

if remydead == False:

    if remystatus == "good":

        if remy4unplayed == False:
            
            if remy4unheard == True:
                
                pass
                
            else:
                
                pass
        
        elif remy3unplayed == False:
            
            if remy3unheard == True:
                
                $ playmessage = True
                
            else:
                
                pass
            
        elif remy2unplayed == False:

            if remy2unheard == True:
                
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                $ playmessage = True
                
            else:
                
                pass
            
        else:

            if remy1unheard == True:
        
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                $ playmessage = True
                
            else:
                
                pass

if brycedead == False:

    if brycestatus == "good":

        if bryce4unplayed == False:
            
            if bryce4unheard == True:
                
                pass
                
            else:
                
                pass
        
        elif bryce3unplayed == False:
            
            if bryce3unheard == True:
                
                $ playmessage = True
                
            else:
                
                pass
            
        elif bryce2unplayed == False:

            if bryce2unheard == True:
                
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                $ playmessage = True
                
            else:
                
                pass
            
        else:

            if bryce1unheard == True:
        
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                $ playmessage = True
                
            else:
                
                pass


if adinestatus == "good":

    if adine4unplayed == False:
        
        if adine4unheard == True:
            
            pass
            
        else:
            
            pass
    
    elif adine3unplayed == False:
        
        if adine3unheard == True:
            
            $ playmessage = True
            
        else:
            
            pass
        
    elif adine2unplayed == False:

        if adine2unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            $ playmessage = True
            
        else:
            
            pass
        
    else:

        if adine1unheard == True:
    
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            $ playmessage = True
            
        else:
            
            pass


if annadead == False:

    if annastatus == "good":

        if anna4unplayed == False:
            
            if anna4unheard == True:
                
                pass
                
            else:
                
                pass
        
        elif anna3unplayed == False:
            
            if anna3unheard == True:
                
                $ playmessage = True
                
            else:
                
                pass
            
        elif anna2unplayed == False:

            if anna2unheard == True:
                
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                $ playmessage = True
                
            else:
                
                pass
            
        else:

            if anna1unheard == True:
        
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                $ playmessage = True
                
            else:
                
                pass
            

if loremdead == False:

    if loremstatus == "good":

        if lorem4unplayed == False:
            
            if lorem4unheard == True:
                
                pass
                
            else:
                
                pass
        
        elif lorem3unplayed == False:
            
            if lorem3unheard == True:
                
                $ playmessage = True
                
            else:
                
                pass
            
        elif lorem2unplayed == False:

            if lorem2unheard == True:
                
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                $ playmessage = True
                
            else:
                
                pass
            
        else:

            if lorem1unheard == True:
        
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                $ playmessage = True
                
            else:
                
                pass


if playmessage == True:
    
    c "(Seems I've got some messages. Let's see...)"
    
    
    
    
if remydead == False:

    if remystatus == "good":
        
        if remy4unplayed == False:
            
            if remy4unheard == True:
                
                pass
                
            else:
                
                pass

        elif remy3unplayed == False:
            
            if remy3unheard == True:
                
                play sound "fx/answeringmachine.ogg"
                
                $ renpy.pause (0.5)
                
                Ry "Hello, this is Remy. I just wanted to remind you about the summer festival. It will start any day now, so I hope you can make it."

                Ry "It would be nice to go there with you. I'm not sure how you feel about this, but I usually try to avoid the crowds."

                Ry "In any case, please let me know if you want to go."
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)
                
                c "(The summer festival, huh?)"

                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_15

                $ remy3unheard = False
                
            else:
                
                pass
                
        elif remy2unplayed == False:
            
            if remy2unheard == True:
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                Ry "Hello, this is Remy. I know you're very busy and probably have more important things to do, but I was wondering if you would like to visit Tatsu Park some time. There is something I would like to talk with you about."

                Ry "Please, let me know if you can find the time."

                Ry "Have a good day."

                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                c "(He wants to talk to me about something? I wonder what that's about.)"

                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_16
                
                $ remy2unheard = False

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

                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_17

                $ remy1unheard = False
                
            else:
                
                pass
    else:
        
        pass
            

if brycedead == False:

    if brycestatus == "good":
        
        if bryce4unplayed == False:
            
            if bryce4unheard == True:
                
                pass
                
            else:
                
                pass

        elif bryce3unplayed == False:
            
            if bryce3unheard == True:
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                Br "Hey, [player_name]. Wanna meet up and go somewhere? Just the two of us?"

                Br "I just want to get out of my crummy temporary apartment."

                Br "I'm sure we could think of something fun."
                            
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                c "(Is he thinking what I'm thinking?)"

                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_18

                $ bryce3unheard = False
                
                pass
                
            else:
                
                pass
                
        elif bryce2unplayed == False:
            
            if bryce2unheard == True:
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                Br "Hey, [player_name]. Remember that BBQ I told you about? It's pretty soon, so you better be ready for it."

                Br "All of the guys from the department will be there."

                Br "We always have tons of fun and some of us even stay overnight."

                Br "Would be cool to have you come along."

                Br "If you wanna come, let me know so I can hook you up with the details."

                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                c "(A dragon BBQ party with a human as the guest of honor. Not suspicious at all, Bryce.)"

                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_19
                
                $ bryce2unheard = False


        else:
            
            if bryce1unheard == True:
                
                play sound "fx/answeringmachine.ogg"
                
                $ renpy.pause (0.5)

                Br "Hey. I was just thinking about last time. I know we got a little blackout drunk, but I still thought that was kinda fun."

                Br "I think you had some fun too, but I also wanted to show you there's more to me than that."

                Br "So, I was just wondering if you wanted to come over just to hang out and relax, you know."

                Br "We only get to see each other when things are all serious, and I bet it's rough for you with everything that's going on. I figured you might want to get away from that a little."

                Br "Anyway, if you want to drop by at any time, my door's open, buddy."

                play sound "fx/answeringmachine.ogg"
                
                $ renpy.pause (0.5)

                c "(Considering what happened last time, entering the literal dragon's den could either turn out really well, or not so much.)"
                
                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_20
                
                $ bryce1unheard = False
                
            else:
                
                pass
    else:
        
        pass
            
if adinestatus == "good":

    if adine4unplayed == False:
        
        if adine4unheard == True:
            
            pass
            
        else:
            
            pass

    elif adine3unplayed == False:
        
        if adine3unheard == True:
            
            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)
            
            Ad "Hey, are you coming to see the show?"

            Ad "It's going to happen pretty soon, you know. I trained so much for this, you wouldn't believe. Probably harder than I ever trained in my entire life."

            Ad "I really hope you can make it, because I want to show you all I've got."

            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)

            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_21

            $ adine2unheard = False
            
            pass
            
        else:
            
            pass
            
    elif adine2unplayed == False:
        
        if adine2unheard == True:
            
            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)

            Ad "Congratulations!"

            Ad "You, [player_name], have been invited to an exclusive event, featuring the world-famous stunt pilot, Adine!"

            Ad "Watch her perform behind closed doors and be one of the first to see her newest routine, sure to win at this year's stunt flying competition!"

            Ad "Afterwards, you will be allowed backstage for a short meet and greet with the talent herself."

            Ad "Don't expect any autographs, though."

            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)

            c "(What an opportunity...)"

            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_22
            
            $ adine2unheard = False


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
            
            call popularcheck from _call_popularcheck_23
            
            $ adine1unheard = False   
            
            
        else:
            
            pass
else:
    
    pass

if annadead == False:

    if annastatus == "good":

        if anna4unplayed == False:
            
            if anna4unheard == True:
                
                pass
                
            else:
                
                pass

        elif anna3unplayed == False:
            
            if anna3unheard == True:
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)
                
                $ renpy.pause (2.0)


                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)
                
                c "(Huh, an empty message?)"

                c "(Let's check the next one.)"

                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)
                
                m "There was another long pause. I almost thought that something was wrong with the machine, but then I heard Anna's voice."

                An "Hey, [player_name]. I'm not even sure why I'm calling about this, but it seemed like you wanted to hang out last time, so call me back if you feel like it."

                An "If you don't want to, then... Well, whatever."

                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)
                
                c "(What was that all about?)"

                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_24
                
                $ anna3unheard = False
                
                pass
                
            else:
                
                pass
                
        elif anna2unplayed == False:
            
            if anna2unheard == True:
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                An "It's pay day, [player_name]." 

                An "The tests are ready, the machines are ready, the lab is free. Only one more thing is needed to get this party started and that would be you."

                An "So, you better bring your body to me, or else I'll have to come and get it myself, in which case I won't be able to guarantee your safety."

                An "I hope you aren't afraid of needles."

                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                c "(She's going to go all out, isn't she?)"

                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_25
                
                $ anna2unheard = False


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
                
                call popularcheck from _call_popularcheck_26
                
                $ anna1unheard = False
                
                
            else:
                
                pass
    else:
        
        pass


if loremdead == False:

    if loremstatus == "good":


        if lorem4unplayed == False:
            
            if lorem4unheard == True:
                
                
                pass
                
            else:
                
                pass

        elif lorem3unplayed == False:
            
            if lorem3unheard == True:
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                Lo "Hey, it's me. Do you want to meet up again?"

                Lo "I know you're busy, but the summer festival is coming up soon."

                Lo "I'm not saying we should go, but we certainly could if you want to."

                Lo "In any case, call me back when you hear this."

                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                $ popularnumber += 1

                call popularcheck from _call_popularcheck_29

                $ lorem3unheard = False
                
                
            else:
                
                pass
                
        elif lorem2unplayed == False:
            
            if lorem2unheard == True:
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                Lo "Hey, [player_name]! Guess what?"

                Lo "Right, we're going treasure hunting!"

                Lo "So, put on your robe and your best treasure hunting hat and let's get going."

                Lo "Seriously, call me back when you hear this."

                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)
                
                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_27
                
                $ lorem2unheard = False

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
                
                call popularcheck from _call_popularcheck_28
                
                $ lorem1unheard = False
                    
                
            else:
                
                pass
    else:
        
        pass


#they also are not available at the moment if the scene corresponding to the chapter has already been played
$ remyavailable = True
$ bryceavailable = True
$ annaavailable = True
$ loremavailable = True

$ adineavailable = False

if adine1unplayed == False:

    if adinestatus == "bad":
        
        $ adineavailable = False
        
    elif adinestatus == "abandoned":
        
        $ adineavailable = False
        
    elif adine4unplayed == False:
        
        $ adineavailable = False
        
    else:
        
        $ adineavailable = True
    
else:
    
    pass
    
if remystatus == "bad":
    
    $ remyavailable = False
    
elif remystatus == "abandoned":
    
    $ remyavailable = False
    
else:
    
    pass
    
if remy4unplayed == False:
    
    $ remyavailable = False
    
else:
    
    pass

if brycestatus == "bad":
    
    $ bryceavailable = False

elif brycestatus == "abandoned":
    
    $ bryceavailable = False
    
elif brycefirst == True:
    
    $ bryceavailable = False
    
else:
    
    pass

if bryce4unplayed == False:
    
    $ bryceavailable = False
    
else:
    
    pass

if annastatus == "bad":
    
    $ annaavailable = False

elif annastatus == "abandoned":
    
    $ annaavailable = False
    
elif annasurvives == False:
    
    $ annaavailable = False
    
else:
    
    pass

if anna4unplayed == False:
    
    $ annaavailable = False
    
else:
    
    pass
    
if loremstatus == "bad":
    
    $ loremavailable = False
    
elif loremstatus == "abandoned":
    
    $ loremavailable = False
    
elif loremdead == True:
    
    $ loremavailable = False
    
else:
    
    pass
    
    
if lorem4unplayed == False:
    
    $ loremavailable = False

if remy4unplayed == False:
    
    if remy3unplayed == False:
        
        $ remyavailable = False
        
    if anna3unplayed == False:
        
        $ annaavailable = False
        $ annastatus = "abandoned"
        
    if lorem3unplayed == False:
        
        $ loremavailable = False
        $ loremstatus = "abandoned"
    
    if bryce3unplayed == False:
        
        $ bryceavailable = False
        $ brycestatus = "abandoned"
 
    if adine3unplayed == False:
        
        $ adineavailable = False
        $ adinestatus = "abandoned"

#copies start here

if anna4unplayed == False:
    
    if remy3unplayed == False:
        
        $ remyavailable = False
        $ remystatus = "abandoned"
        
    if anna3unplayed == False:
        
        $ annaavailable = False
        
    if lorem3unplayed == False:
        
        $ loremavailable = False
        $ loremstatus = "abandoned"
    
    if bryce3unplayed == False:
        
        $ bryceavailable = False
        $ brycestatus = "abandoned"
 
    if adine3unplayed == False:
        
        $ adineavailable = False
        $ adinestatus = "abandoned"
        

if lorem4unplayed == False:
    
    if remy3unplayed == False:
        
        $ remyavailable = False
        $ remystatus = "abandoned"
        
    if anna3unplayed == False:
        
        $ annaavailable = False
        $ annastatus = "abandoned"
        
    if lorem3unplayed == False:
        
        $ loremavailable = False
    
    if bryce3unplayed == False:
        
        $ bryceavailable = False
        $ brycestatus = "abandoned"
 
    if adine3unplayed == False:
        
        $ adineavailable = False
        $ adinestatus = "abandoned"
        
        
if bryce4unplayed == False:
    
    if remy3unplayed == False:
        
        $ remyavailable = False
        $ remystatus = "abandoned"
        
    if anna3unplayed == False:
        
        $ annaavailable = False
        $ annastatus = "abandoned"
        
    if lorem3unplayed == False:
        
        $ loremavailable = False
        $ loremstatus = "abandoned"
    
    if bryce3unplayed == False:
        
        $ bryceavailable = False
 
    if adine3unplayed == False:
        
        $ adineavailable = False
        $ adinestatus = "abandoned"
        
        
if adine4unplayed == False:
    
    if remy3unplayed == False:
        
        $ remyavailable = False
        $ remystatus = "abandoned"
        
    if anna3unplayed == False:
        
        $ annaavailable = False
        $ annastatus = "abandoned"
        
    if lorem3unplayed == False:
        
        $ loremavailable = False
        $ loremstatus = "abandoned"
    
    if bryce3unplayed == False:
        
        $ bryceavailable = False
        $ adinestatus = "abandoned"
 
    if adine3unplayed == False:
        
        $ adineavailable = False


#all dead case

if remydead == True:
    
    if brycedead == True:
        
        if c4displayadine == True:

            if adineavailable == False:
            
                if annadead == True:
                    
                    if loremdead == True:
                        
                        if kevinavailable == False:

                            if c4csplayed == 1:

                                c "(Another free day. Yay me.)"
                    
                            m "In the end, I decided to extend invitations to everyone I knew to come by for a visit. I left a lot of messages and waited the whole afternoon, but nobody came."
                            
                            jump chapter5

if remyavailable == False:
    
    if bryceavailable == False:
        
        if adineavailable == False:
            
            if adine1unplayed == False:
            
                if annaavailable == False:
                    
                    if loremavailable == False:
                        
                        if kevinavailable == False:

                            if c4csplayed == 1:

                                c "(Another free day. Yay me.)"
                    
                            m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
                    
                            jump chapter5

                else:
                    
                    pass
                    
            else:
                
                pass
                
        else:
            
            pass
            
    else:
        
        pass
        
else:
    
    pass



if c4csplayed == 0:

    $ chapter4count = 0

    if remyavailable == True:
        
        $ chapter4count +=1
        
    if annaavailable == True:
        
        $ chapter4count +=1

    if loremavailable == True:
        
        $ chapter4count +=1
        
    if bryceavailable == True:
        
        $ chapter4count +=1

    if adine1unplayed == True:
        
        $ chapter4count +=1
        
    if adineavailable == True:
        
        $ chapter4count +=1
        
    if kevinavailable == True:
        
        $ chapter4count +=1

    if zhongunplayed == False:
        
        $ chapter4count +=1
        
    label chapter4chars2:
        
        if c4csplayed == 1:
            
            jump chapter4chars3

    if chapter4count >= 7:
        
        jump chap4altmenua1
    
    menu:
        
        
        "Meet with Remy." if remyavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "remy"
            if remy1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy1
                
            elif remy2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy2
                
            elif remy3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy3
            
            else:
                
                jump remy4
            
        "Meet with Anna." if annaavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "anna"
            if anna1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna1
                
            if anna2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna2
                
            if anna3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna3
                
            else:
                
                jump anna4

        "Meet with Lorem." if loremavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "lorem"
            if lorem1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump lorem1
                
            if lorem2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump lorem2
                
            if lorem3unplayed == True:
                #play sound "fx/steps/clean2.wav"
                jump lorem3
                
            else:
                
                jump lorem4

            
        "Meet with Bryce." if bryceavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "bryce"
            if bryce1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce1
                
            elif bryce2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce2
                
            elif bryce3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce3
                
            else:
                
                jump bryce4
            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "adine"
            jump adine1
            
        "Meet with Adine." if adineavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "adine"
            
            if adine2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump adine2
                
            elif adine3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump adine3
                
            else:
                
                jump adine4


        "Meet with Kevin." if kevinavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "kevin"
            jump kevin
            
            
        "Listen to your records." if zhongunplayed == False:

            stop music fadeout 1.0
            #$ c3csplayed += 1
            jump c3music


elif c4csplayed == 1:

    c "(Another free day. Yay me.)"

    $ chapter4count = 1

    if remyavailable == True:
        
        $ chapter4count +=1
        
    if annaavailable == True:
        
        $ chapter4count +=1

    if loremavailable == True:
        
        $ chapter4count +=1
        
    if bryceavailable == True:
        
        $ chapter4count +=1

    if adine1unplayed == True:
        
        $ chapter4count +=1
        
    if adineavailable == True:
        
        $ chapter4count +=1
        
    if kevinavailable == True:
        
        $ chapter4count +=1


    if zhongunplayed == False:
        
        $ chapter4count +=1


    label chapter4chars3:


    if chapter4count >= 7:
        
        jump chap4altmenub1

    menu:

        
        "Meet with Remy." if remyavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "remy"
            if remy1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy1
                
            elif remy2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy2
                
            elif remy3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy3
                
            else:
                
                jump remy4
            
        "Meet with Anna." if annaavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "anna"
            if anna1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna1
                
            elif anna2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna2
                
            elif anna3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna3
                
            else:
                
                jump anna4

        "Meet with Lorem." if loremavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "lorem"
            if lorem1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump lorem1
                
            if lorem2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump lorem2
                
            if lorem3unplayed == True:
                #play sound "fx/steps/clean2.wav"
                jump lorem3
                
            else:
                
                jump lorem4
            
        "Meet with Bryce." if bryceavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "bryce"
            if bryce1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce1
                
            elif bryce2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce2
                
            elif bryce3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce3
                
            else:
                
                jump bryce4
            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "adine"
            jump adine1
            
        "Meet with Adine." if adineavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "adine"
            
            if adine2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump adine2
                
            elif adine3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump adine3
            
            else:
                
                jump adine4

        "Meet with Kevin." if kevinavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "kevin"
            jump kevin


        "Listen to your records." if zhongunplayed == False:

            stop music fadeout 1.0
            #$ c3csplayed += 1
            jump c3music


        "Get some well deserved rest.":
                
            m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
                
            $ persistent.lazynumber += 1
            call lazycheck from _call_lazycheck_8
            
            jump chapter5

else:
    jump chapter5


label chap4altmenua1:

    menu:
        
        
        "Meet with Remy." if remyavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "remy"
            if remy1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy1
                
            elif remy2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy2
                
            elif remy3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy3
            
            else:
                
                jump remy4
            
        "Meet with Anna." if annaavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "anna"
            if anna1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna1
                
            if anna2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna2
                
            if anna3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna3
                
            else:
                
                jump anna4

        "Meet with Lorem." if loremavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "lorem"
            if lorem1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump lorem1
                
            if lorem2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump lorem2
                
            if lorem3unplayed == True:
                #play sound "fx/steps/clean2.wav"
                jump lorem3
                
            else:
                
                jump lorem4

            
        "Meet with Bryce." if bryceavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "bryce"
            if bryce1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce1
                
            elif bryce2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce2
                
            elif bryce3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce3
                
            else:
                
                jump bryce4
                
        "[[Show more options.]":
            
            jump chap4altmenua2
            
        

label chap4altmenua2:
    
    menu:
        
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "adine"
            jump adine1
            
        "Meet with Adine." if adineavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "adine"
            
            if adine2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump adine2
                
            elif adine3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump adine3
                
            else:
                
                jump adine4


        "Meet with Kevin." if kevinavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4picka = "kevin"
            jump kevin
            
            
        "Listen to your records." if zhongunplayed == False:

            stop music fadeout 1.0
            #$ c3csplayed += 1
            jump c3music
            
            
        "[[Show more options.]":
            
            jump chap4altmenua1
        
    
label chap4altmenub1:

    menu:

        
        "Meet with Remy." if remyavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "remy"
            if remy1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy1
                
            elif remy2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy2
                
            elif remy3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump remy3
                
            else:
                
                jump remy4
            
        "Meet with Anna." if annaavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "anna"
            if anna1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna1
                
            elif anna2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna2
                
            elif anna3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump anna3
                
            else:
                
                jump anna4

        "Meet with Lorem." if loremavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "lorem"
            if lorem1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump lorem1
                
            if lorem2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump lorem2
                
            if lorem3unplayed == True:
                #play sound "fx/steps/clean2.wav"
                jump lorem3
                
            else:
                
                jump lorem4
            
        "Meet with Bryce." if bryceavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "bryce"
            if bryce1unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce1
                
            elif bryce2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce2
                
            elif bryce3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump bryce3
                
            else:
                
                jump bryce4
                
                
        "[[Show more options.]":
            
            jump chap4altmenub2
            
        
        
label chap4altmenub2:

    menu:
        
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "adine"
            jump adine1
            
        "Meet with Adine." if adineavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "adine"
            
            if adine2unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump adine2
                
            elif adine3unplayed == True:
                play sound "fx/steps/clean2.wav"
                jump adine3
            
            else:
                
                jump adine4

        "Meet with Kevin." if kevinavailable:
            #play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c4csplayed += 1
            $ chap4pickb = "kevin"
            jump kevin


        "Listen to your records." if zhongunplayed == False:

            stop music fadeout 1.0
            #$ c3csplayed += 1
            jump c3music


        "Get some well deserved rest.":
                
            m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
                
            $ persistent.lazynumber += 1
            call lazycheck from _call_lazycheck_9
            
            jump chapter5



        "[[Show more options.]":
            
            jump chap4altmenub1



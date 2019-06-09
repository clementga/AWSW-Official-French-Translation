label chapter3:


scene black with dissolveslow

$_dismiss_pause = False

$ _game_menu_screen = None

$ renpy.pause(1.3)

$ save_name = "Chapter 3"

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

play sound "fx/chapter3.ogg"

scene chap3 at Pan((0, 0), (0, 0), 6.0) with dissolveslow

#show card1 at Pan((100, 0), (0, 0), 2.0) with dissolveslow

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

    if chap3picksremy == 6:
        
        if remystatus == "bad":
            
            pass
            
        else:
        
            show cgrief at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardgrief = True
            $ lastcard = "cgrief"
            $ carddisplayed = True
        
    elif chap3picksanna == 6:
        
        if annastatus == "bad":
            
            pass
            
        else:
        
            show cpassion at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardpassion = True
            $ lastcard = "cpassion"
            $ carddisplayed = True
            
    elif chap3pickslorem == 6:
        
        if loremstatus == "bad":
            
            pass
            
        else:
            
            show clorem at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardlorem = True
            $ lastcard = "clorem"
            $ carddisplayed = True

    elif chap3picksbryce == 6:
        
        if brycestatus == "bad":
            
            pass
            
        else:
        
            show cleadership at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardleadership = True
            $ lastcard = "cleadership"
            $ carddisplayed = True
        
    elif chap3picksadine == 6:
        
        if adinestatus == "bad":
            
            pass
            
        else:
        
            show csuperstition at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardsuperstition = True
            $ lastcard = "csuperstition"
            $ carddisplayed = True
    
    
if carddisplayed == False:

    if chap3picksremy == 5:
        
        if remystatus == "bad":
            
            pass
            
        else:
        
            show cgrief at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardgrief = True
            $ lastcard = "cgrief"
            $ carddisplayed = True
        
    if chap3picksanna == 5:
        
        if annastatus == "bad":
        
            pass
        
        else:
        
            show cpassion at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardpassion = True
            $ lastcard = "cpassion"
            $ carddisplayed = True


    if chap3pickslorem == 5:
    
        if loremstatus == "bad":
            
            pass
            
        else:
            
            show clorem at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardlorem = True
            $ lastcard = "clorem"
            $ carddisplayed = True

    if chap3picksbryce == 5:

        if brycestatus == "bad":
        
            pass
        
        else:
        
            show cleadership at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardleadership = True
            $ lastcard = "cleadership"
            $ carddisplayed = True
        
    if chap3picksadine == 5:

        if adinestatus == "bad":
        
            pass
        
        else:
        
            show csuperstition at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardsuperstition = True
            $ lastcard = "csuperstition"
            $ carddisplayed = True
        

#here4

if carddisplayed == False:

    if chap3picksremy == 4:
        
        if remystatus == "bad":
            
            pass
            
        else:
        
            show cgrief at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardgrief = True
            $ lastcard = "cgrief"
            $ carddisplayed = True
        
    if chap3picksanna == 4:
        
        if annastatus == "bad":
        
            pass
        
        else:
        
            show cpassion at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardpassion = True
            $ lastcard = "cpassion"
            $ carddisplayed = True


    if chap3pickslorem == 4:
    
        if loremstatus == "bad":
            
            pass
            
        else:
            
            show clorem at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardlorem = True
            $ lastcard = "clorem"
            $ carddisplayed = True

    if chap3picksbryce == 4:

        if brycestatus == "bad":
        
            pass
        
        else:
        
            show cleadership at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardleadership = True
            $ lastcard = "cleadership"
            $ carddisplayed = True
        
    if chap3picksadine == 4:

        if adinestatus == "bad":
        
            pass
        
        else:
        
            show csuperstition at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardsuperstition = True
            $ lastcard = "csuperstition"
            $ carddisplayed = True
            

#3 here

if carddisplayed == False:

    if chap3picksremy == 3:
        
        if remystatus == "bad":
            
            pass
            
        else:
        
            show cgrief at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardgrief = True
            $ lastcard = "cgrief"
            $ carddisplayed = True
        
    if chap3picksanna == 3:
        
        if annastatus == "bad":
        
            pass
        
        else:
        
            show cpassion at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardpassion = True
            $ lastcard = "cpassion"
            $ carddisplayed = True


    if chap3pickslorem == 3:

        if loremstatus == "bad":
            
            pass
            
        else:
            
            show clorem at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardlorem = True
            $ lastcard = "clorem"
            $ carddisplayed = True

    if chap3picksbryce == 3:

        if brycestatus == "bad":
        
            pass
        
        else:
        
            show cleadership at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardleadership = True
            $ lastcard = "cleadership"
            $ carddisplayed = True
        
    if chap3picksadine == 3:

        if adinestatus == "bad":
        
            pass
        
        else:
        
            show csuperstition at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardsuperstition = True
            $ lastcard = "csuperstition"
            $ carddisplayed = True
            
#2 here

if carddisplayed == False:

    if chap3picksremy == 2:
        
        if remystatus == "bad":
            
            pass
            
        else:
        
            show cgrief at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardgrief = True
            $ lastcard = "cgrief"
            $ carddisplayed = True
        
    if chap3picksanna == 2:
        
        if annastatus == "bad":
        
            pass
        
        else:
        
            show cpassion at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardpassion = True
            $ lastcard = "cpassion"
            $ carddisplayed = True



    if chap3pickslorem == 2:
    
        if loremstatus == "bad":
            
            pass
            
        else:
            
            show clorem at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardlorem = True
            $ lastcard = "clorem"
            $ carddisplayed = True

    if chap3picksbryce == 2:

        if brycestatus == "bad":
        
            pass
        
        else:
        
            show cleadership at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardleadership = True
            $ lastcard = "cleadership"
            $ carddisplayed = True
        
    if chap3picksadine == 2:

        if adinestatus == "bad":
        
            pass
        
        else:
        
            show csuperstition at Pan((100, 0), (0, 0), 2.0) with dissolveslow
            $ cardsuperstition = True
            $ lastcard = "csuperstition"
            $ carddisplayed = True


if carddisplayed == False:

    show cpride at Pan((100, 0), (0, 0), 2.0) with dissolveslow
    $ cardpride = True
    $ lastcard = "cpride"
    $ carddisplayed = True


show text3 with dissolveslow

if lastcard == "cgrief":

    scene chap3 at Pan((0, 120), (0, 360), 7.0) 
    show cgrief at Pan((0, 0), (0, 0), 0.1)
    show text3
    with dissolveslow

elif lastcard == "cenlightenment":

    scene chap3 at Pan((0, 120), (0, 360), 7.0) 
    show cenlightenment at Pan((0, 0), (0, 0), 0.1)
    show text3
    with dissolveslow
    
elif lastcard == "cpassion":

    scene chap3 at Pan((0, 120), (0, 360), 7.0) 
    show cpassion at Pan((0, 0), (0, 0), 0.1)
    show text3
    with dissolveslow

elif lastcard == "clorem":

    scene chap3 at Pan((0, 120), (0, 360), 7.0) 
    show clorem at Pan((0, 0), (0, 0), 0.1)
    show text3
    with dissolveslow
    
elif lastcard == "cleadership":

    scene chap3 at Pan((0, 120), (0, 360), 7.0) 
    show cleadership at Pan((0, 0), (0, 0), 0.1)
    show text3
    with dissolveslow
    
elif lastcard == "csuperstition":
    
    scene chap3 at Pan((0, 120), (0, 360), 7.0) 
    show csuperstition at Pan((0, 0), (0, 0), 0.1)
    show text3
    with dissolveslow

else:

    scene chap3 at Pan((0, 120), (0, 360), 7.0) 
    show cpride at Pan((0, 0), (0, 0), 0.1)
    show text3
    with dissolveslow

play soundloop "fx/chap3tr3.ogg"

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

play music "mx/general.ogg"

$ chapter3unplayed = False

if adine1unheard == False:
    
    if chap2picka == "adine":
        
        pass
        
    elif chap2pickb == "adine":
        
        pass
        
    else:
        
        if adinestatus == "good":
            
            $ adinestatus = "abandoned"

if bryce1unheard == False:
    
    if chap2picka == "bryce":
        
        pass
        
    elif chap2pickb == "bryce":
        
        pass
        
    else:
        
        if brycestatus == "good":
            
            $ brycestatus = "abandoned"

if anna1unheard == False:
    
    if chap2picka == "anna":
        
        pass
        
    elif chap2pickb == "anna":
        
        pass
        
    else:
        
        if annastatus == "good":
            
            $ annastatus = "abandoned"

if adine1unheard == False:
    
    if chap2picka == "adine":
        
        pass
        
    elif chap2pickb == "adine":
        
        pass
        
    else:
        
        if adinestatus == "good":
            
            $ adinestatus = "abandoned"

if lorem1unheard == False:
    
    if chap2picka == "lorem":
        
        pass
        
    elif chap2pickb == "lorem":
        
        pass
        
    else:
        
        if loremstatus == "good":
            
            $ loremstatus = "abandoned"

nvl clear

window show

if persistent.brycedies == True:
    $ persistent.brycekey3 = True

$ popularnumber = 0

n "The morning sun declared the arrival of a new day and woke me from my vivid dreams. Memories of my home, enclosed within the towering perimeter wall raced through my head."
n "The peaceful landscape outside the apartment window stood in defiance of these old thoughts. Rolling hills and blue sky were familiar to me now, and the purity of the sight gave me hope."

window hide

play sound "fx/door/doorbell.wav"

$ renpy.pause (1.5)

stop sound fadeout 0.5

window hide

play sound "fx/door/handle.wav"

$ renpy.pause (1.5)

nvl clear

show sebastian normal b with dissolve

Sb "[player_name], please come with me."

#stop music fadeout 2.0

c "What's going on? You sound serious."

Sb "The chief will explain everything once we arrive."

c "Okay."

play sound "fx/steps/clean2.wav"

scene black with dissolvemed
$ renpy.pause (0.5)
scene facin2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

$ renpy.pause (1.5)

show sebastian normal b flip at left with easeinleft

Sb "Hey, Chief. [player_name] is here."

show bryce stern b at right with easeinright

Br "Thanks, Sebastian. You can deal with the situation here while I talk to [player_name], alright?"

Sb "Of course."
stop music fadeout 2.0
show sebastian normal b

$ renpy.pause (0.3)

hide sebastian with easeoutleft

show bryce at center with ease

Br "[player_name], I've got some really bad news."

play music "mx/threat.ogg"

if brycestatus == "bad":

    c "Did you put on some more weight?" 

    Br brow b "Stop joking around, this is serious." 

    c "I am serious. Diabetes is no joke." 

    Br stern b "Shut up already and listen to me for once."

else:
    
    pass
    
c "Well, what is it?"

if persistent.annagoodending == True:
    
    $ annasurvives = True
    
else:
    
    pass

if annasurvives == False:
    
    Br brow b "You know Anna, right?"

    c "I've met her, yes."

    Br "I'm sorry. I don't know how to say this."

    m "Those few words were enough. Dread sank in, and I already knew."

    Br stern b "Don't..."
    
    hide bryce with dissolve

    m "I ignored his words and walked past him."
    
    show black with dissolve
    
    $ renpy.pause (0.5)

    show annad at Pan ((0, 326), (580, 250), 8) with dissolvemed
    
    $ renpy.pause (6.0)
    
    m "When I turned the corner, there was no mistaking her. Anna was haphazardly covered by a sheet, leaving her tail and bloodstained hand exposed. In the end, she didn't even deserve full discretion."
    
    hide annad 
    hide black
    with fade

    $ mp.annaloss = True
    $ mp.save()
    
    $ annadead = True
    
    if brycestatus == "bad":
        
        show bryce stern b with dissolve
        
        Br "I bet you're sorry about your diabetes joke now, huh?"
        
        jump c3contx
        
    else:

        show bryce brow b with dissolve
        
        Br "Are you okay?"

        menu:
            
            "I... don't know.":
                
                $ renpy.pause (0.5)
                
                Br stern b "Is there anything that I can do?"

                c "Let's just get this over with."

                m "Bryce gave me a concerned look, but then nodded." 
                
                jump c3contx
                
            "I'm fine.":
                
                c "Yeah, I'm fine. Let's just get this over with."
                
                show bryce stern b with dissolve

                m "Bryce nodded."

                jump c3contx
    
    
elif damionsurvives == False:

    Br brow b "You know Anna, right?"

    c "I've met her, yes."

    Br stern b "How about her assistant?"
    
    if persistent.metdamion == False:
        
        c "Can't say I have."

        Br "Well, that's him."
        
        show black with dissolve
    
        $ renpy.pause (0.5)

        show damiond at Pan ((0, 326), (580, 200), 8) with dissolvemed
        
        $ renpy.pause (6.0)
        
        hide damiond 
        hide black
        with fade

        jump c3contx
        
    else:
        
        c "I met him once or twice."

        Br "Well, that's him."

        show black with dissolve
    
        $ renpy.pause (0.5)

        show damiond at Pan ((0, 326), (580, 200), 8) with dissolvemed
        
        $ renpy.pause (6.0)
        
        hide damiond 
        hide black
        with fade

        c "..."
        
        if brycestatus == "bad":

            Br "I bet you're sorry about your diabetes joke now, huh?"
            
            show bryce brow b with dissolve
        
            jump c3cont
            
        else:
            
            Br "Are you okay?"
            
            menu:
                
                "I... don't know.":
                    
                    $ renpy.pause (0.5)
                    
                    Br brow b "Is there anything that I can do?"

                    c "Let's just get this over with."
                    
                    show bryce stern b with dissolve

                    m "Bryce gave me a concerned look, but then nodded."

                    jump c3contx
                    
                "I'm fine.":
                    
                    c "Yeah, I'm fine. Let's just get this over with."

                    m "Bryce nodded."

                    jump c3contx
    
    
else:

    Br "There was a break-in, and we have a strong suspicion that Reza was involved."

    Br brow b "That by itself would not be so bad, but among the things stolen were your PDAs, batteries, and some components used to build generators."

    Br stern b "No one else has a greater motive to steal the PDAs than Reza, especially after what happened between him and Maverick."

    Br "We also received the results of some tests we ran on Reza's victims. The blood we found on the first victim in town matches the DNA evidence found on the second victim at the power facility."

    Br "The murder weapon and method appear identical for both, and while we already knew that, the DNA evidence linking the murders together could become a big problem for you."
        
    c "Why is that?"

    Br "A human going around murdering people won't go unnoticed for much longer. Higher authorities, including the ministry in charge of your whole visit will know about this soon. I have no idea what will happen once they do."

    Br brow b "And if Reza stole back your PDAs, that puts the deal between our people in danger."
    
    c "I'm not sure what to say."

    Br stern b "I don't want to worry you, but we can be sure that action will be taken soon. I've been considering this possibility for a while, and think it might be best if you went back to your own world for now."

    Br "This way, we can take action before the ministry does, and before this all becomes public. If we wait, we don't know what they'll do or how the public will react. With everything going on, it's too dangerous for you to stay here."
    
    c "No."

    Br brow b "No?"

    c "This would be the worst possible time for me to leave. We've given up our PDAs and hardly have anything to show for it. We are owed several more generators, and let's not forget that Reza is still missing."

    c "If I leave now, the only thing I return home with is my life. I'll have lost everything else. We need those generators, Bryce. I have no idea if your authorities will continue to uphold our deal, or what they'd do to Reza, but I'm not leaving until this is over."

    Br stern b "If that's your decision, then so be it."
    
    show bryce brow b with dissolve
    
    jump c3conty
    

label c3contx:
    
    Br brow b "And here's more bad news: The blood we found on the first victim in town matches the DNA evidence found on the second victim at the power facility."

    Br stern b "Furthermore, the murder weapon and method appear to be the same across all three victims, and that's going to be a big problem for you." 

    c "Why is that?"
    
    Br "Because with these three murders, Reza now qualifies as a serial killer. We won't be able to keep this whole thing quiet for much longer." 
    
    Br "Higher authorities, including the ministry in charge of your whole visit, will know about this soon. I have no idea what will happen once they do."

    c "I'm not sure what to say to that."

    Br brow b "I don't want to worry you, but we can be sure that action will be taken soon. I've been considering this possibility for a while, and think it might be best if you went back to your own world for now."

    Br stern b "This way, we can take action before the ministry does, and before this all becomes public. If we wait, we don't know what they'll do or how the public will react."
    
    Br "With everything going on, it's too dangerous for you to stay here."

    c "No."

    Br brow b "No?"

    c "This would be the worst possible time for me to leave. We've given up our PDAs and hardly have anything to show for it. We are owed several more generators, and let's not forget that Reza is still missing."

    c "If I leave now, the only thing I return home with is my life. I'll have lost everything else. We need those generators, Bryce. I have no idea if your authorities will continue to uphold our deal, or what they'd do to Reza, but I'm not leaving until this is over."
    
    show bryce stern b with dissolve
    
    if bryce2unplayed == False:
        
        if brycestatus == "bad":

            Br "If that's your decision, then so be it."
        
        elif brycestatus == "abandoned":

            Br "If that's your decision, then so be it."
            
        else:
            
            Br "If that's your decision, then so be it. I'll have your back either way."

            c "Thanks, Bryce."
        
    else:

        Br "If that's your decision, then so be it."
        
show bryce brow b with dissolve        

label c3cont:
    
#skip here?

if persistent.c3skip == True:

    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_14

    call skiptut from _call_skiptut_4
        
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
            
            $ c3facavailable = True
            
            scene black with dissolvemed

            $ renpy.pause (1.0)
            
            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_4

            scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

            play music "mx/barren.ogg" fadein 2.0
            
            nvl clear
            
            jump c3skip
            
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/threat.ogg" fadein 1.0

Br "Anyway, let's get back on track. I called you here for a reason, [player_name]. In addition to the murder, several things were stolen, among them your PDAs, batteries, and some components used to build generators."

Br "Does that ring any bells?"
    
c "Not really. Reza might have some knowledge of electronics, but I doubt he has enough to assemble one of your generators, even if he had the parts."

Br "Strange."

Br stern b "Even so, it's fair to assume Reza's involvement at this point. No one else has a greater motive to steal the PDAs, especially after what happened between him and Maverick."

c "Unless someone wanted to frame Reza in order to sabotage this whole operation."

Br brow b "Do you really believe that?"

c "Hey, I'm just saying that it's possible."

Br "I'll shelf that idea under \"possible, but unlikely\"."

label c3conty:

show bryce at right with ease

show sebastian normal b flip at left with easeinleft

Sb "Hey, Chief. Are we done here?"

Br "Pretty much. Why do you ask?"

Sb "We just got a message from the higher-ups. You and [player_name] are to report to the Ministry of Culture & Arts immediately."

Br stern b "Immediately, as in right now?"
    
Sb "Yeah, apparently."

c "What's going on?" 

Br brow b "To be frank, I don't know. This is an extraordinary situation, and now that it's getting out of hand, they must want to address it."

menu:
    
    "So, the worst possibility.":
        
        $ renpy.pause (0.5)

        Br stern b "If you expect the worst, at least you won't be disappointed."
        
        
    "Maybe it's not going to be a big deal.":

        $ renpy.pause (0.5)

        Br stern b"Maybe. I suppose we'll see soon enough."
        
    
    "Maybe they're going to throw a surprise party for us.":

        $ renpy.pause (0.5)

        Br stern b "Yeah, probably not."

        $ evilpoints += 1

Br "Sebastian, you can finish up here and go to the Ministry when you're done. We'll probably have to make some arrangements after this meeting."

Sb "Sure thing, Chief."

show sebastian normal b

$ renpy.pause (0.3)

hide sebastian with easeoutleft

Br "Let's go then, shall we?"

c "It's not like we have a choice."

stop music fadeout 2.0

scene black with dissolvemed

$ renpy.pause (0.5)

scene park3 at Pan ((100, 0), (0, 0), 3.0) with dissolveslow

$ renpy.pause (1.5)

if chap2emmeet2 == False:

    scene black with dissolve
    $ renpy.pause (0.3)
    show cgemera at Pan((0, 0), (0, 302), 7.0) with dissolvemed
    $ renpy.pause(5.0)
                

    scene park3 at Pan ((0, 0), (0, 0), 0.0) 
    with fade
    
else:
    
    pass
    

show emera normal with dissolve

play music "mx/politics.ogg" fadein 1.0

Em "That was quicker than I expected. I wouldn't have minded waiting out here a little longer."
$ emeramet = True

show emera at right with ease

show bryce stern b flip at left with easeinleft

Br "Greetings, Minister."

c "Greetings."

Br brow b flip "Shall we go inside for our official business?"

Em mean "No, I've got everything I need right here. It gets so stuffy inside on hot days. My assistant doesn't seem to mind, but I prefer the fresh air. I'd rather just stay right here, unless you have any objections."

Br stern b flip "I don't."

if annasurvives == False:

    Em normal "I see. Well, I know I haven't exactly been up to date in regards to Reza's sudden disappearance, but to get the message today that he is a confirmed serial killer was quite shocking." 
    
    Em "Frankly, I'm curious as to why the facts of this case have been withheld from me for so long."

    Br brow b flip "Simply because they weren't within your jurisdiction. The murders were strictly a police matter." 
    
    Br "Only with the amount of new evidence, namely the DNA and blood we found and these three murders now being linked together and to him did your ministry have to become involved." 

elif damionsurvives == False:

    Em normal "I see. Well, I know I haven't exactly been up to date in regards to Reza's sudden disappearance, but to get the message today that he is a confirmed serial killer was quite shocking." 
    
    Em "Frankly, I'm curious as to why the facts of this case have been withheld from me for so long."

    Br brow b flip "Simply because they weren't within your jurisdiction. The murders were strictly a police matter." 
    
    Br "Only with the amount of new evidence, namely the DNA and blood we found and these three murders now being linked together and to him did your ministry have to become involved." 
    
else:
    
    Em normal "I see. Well, I know I haven't exactly kept myself up-to-date with the details of Reza's disappearance, but to receive the message today that he has been involved in multiple murders and break-ins is quite shocking." 
    
    Em "Frankly, I'm curious as to why the facts of this case have been withheld from me for so long."

    Br brow b flip "Simply because they weren't within your jurisdiction. The murders were strictly a police matter." 
    
    Br "Only after we tested our new evidence, discovered the DNA linking the two victims together, and had the PDAs stolen did your ministry have to become involved." 
    
    
Em frown "I see. So Reza's involvement is now undeniable?"

Br stern b flip "I'm afraid so, Minister."

Em normal "Facts are nothing to be afraid of. Though, in light of all this, I'm starting to worry about my personal safety."

Br brow b flip "With our thick hides, I don't think our species has much to fear if we consider the murder weapon."

Em ques "Speak for yourself. You don't think someone of my standing needs protection?"

Br stern b flip "Oh, for sure. If you are worried about your personal safety, we could look into an escort for you."

Em normal "Good. Considering all the murders took place during the night, I'll certainly need it. Long days are endemic in my line of work."

Em frown "But that's enough about myself. We now face the question of what should be done about Reza and [player_name]."

Br "Minister, we continue our hunt for Reza every day. As a matter of fact, [player_name] has been helping us do so for a while now."

Em normal "Is that so? One human a murderer, another a detective... Interesting."

Em frown "And how do we know [player_name] isn't following a similar plan to Reza's, whatever that may be?"

Br brow b flip "Similar concerns were leveled by Reza's escort, Maverick. It was his overreaction that caused Reza to run away in the first place."

Em mean "Let the human talk for once, Chief."

Em frown "Please, [player_name], enlighten me. You and Reza came here on the same mission and the situation has escalated beyond our expectations. What you tell me now will determine the actions I'll take on this matter."

Em normal "Maybe you should start by telling me your side of the events from the beginning. Reza was fine during his early days here. Things only went wrong after you arrived."

m "I opened my mouth, but Bryce spoke first, determined to defend me."

Br stern b flip "Arguably, the problems that caused all this were apparent even then."

Em "How so?"

Br "Maverick suspected Reza of planning something, but I didn't think he had a case."

Em frown "Well, did he?"

Br "No, what he had was a suspicion."
Br "The night he followed Reza, he found both him and [player_name] at the portal." 

Br "The humans intended to send one of their promised generators through, but there was a confrontation that ended with both Maverick and [player_name] wounded, and Reza running away." 

Br "Reza's been missing ever since."

Em normal "I've read the reports already, Chief."

Em frown "The question is: Did Maverick cause this, or did he just fail to prevent it?"

Br brow b flip "I have no way of knowing that, Minister."

Em normal "You just mentioned your \"apparent\" knowledge of problems back then."

Br stern b flip "\"Problems\" may not have been the right word. Let's just say Maverick's attitude was not helpful during that encounter."

Em "Why did you choose Maverick as his escort in the first place?"

Br "Protection for the human ambassador was my greatest concern when I made that decision, and Maverick was the most capable individual in that regard."

Em frown "Well, that worked out nicely, didn't it?"

Em normal "You also seem to think that Maverick shouldn't have remained Reza's escort. Is that true?"

Br "Yes. Had I paid more attention to the warning signs, this situation may have been avoided."

Em "So you accept responsibility for the incident?"

Br "..."

Br "Yes, Minister."

Em frown "I see."

Em normal "Now, let us get back to the topic of [player_name]."

Em frown "Reza was your partner in humanity's mission to come to this world. His list of criminal activities not only includes murder, but also theft of generators, electronic components and the PDAs your people gave to us."

Em normal "I understand why Bryce would reason that you could help the investigation, but we have no other choice but to be suspicious of Reza's partner. What was your motivation when you agreed to help us?"

menu:
    
    "Bryce wouldn't let me say no.":

        c "I didn't actually want to help with the investigation, but Bryce insisted until I eventually agreed."

        Em "As strange as it sounds, that makes you appear more trustworthy to me. Someone jumping at the opportunity to participate in the investigation would be viewed with suspicion."
        
    
    "It is my best bet at finding the truth.":

        Em "I thought Reza's involvement was undeniable at this point."

        c "That may be true, but we still don't have the whole picture. We don't know if others are involved, or his reasons. I just want to know why."

        Em "I see."
        
        
    "It is beneficial to my actual mission.":
        
        $ renpy.pause (0.5)

        Em frown "And what would that be?"

        c "The deal between our races. I firmly stand by our original agreement."
        
        c "If Reza is involved with these crimes, I want no part of it. It has nothing to do with me or the reasons I came here in the first place. If his actions are endangering this agreement in any way, I want to put a stop to him."

        Em normal "I see."
        

Em "Well, after reading up on the whole situation and hearing both your accounts, I believe that [player_name] is trustworthy."

Em frown "Nevertheless, I think [player_name] presents a great risk."

c "Why is that?"

Em normal "After this meeting, I will hold a press conference to inform the public of the current situation. The people must know of the danger posed by Reza."

Em "No matter what Bryce and I think about your involvement, the public could feel differently."

Em "You, me and Bryce will have to face the backlash resulting from this information becoming public, and what's more, [player_name], you might be in real danger yourself."

Em frown "Reza himself may come to silence you once he learns that you are helping us. Or consider the public uproar from those who would question your involvement." 

Em "All things considered, it would be for the best if you returned to your own world until the situation has been resolved."

Br "I came to the very same conclusion, Minister."

Em normal "Then, with your support, this is what shall be done."

c "Please, don't..."

Em frown "You don't agree?"

c "If you send me back now, this diplomatic relationship is over. I'd have to admit defeat to humanity. There is no way I can return without your generators, our PDAs, or Reza." 

Em ques "Maybe you could explain to them what a great choice of an ambassador Reza was."

c "But I was his partner, so in a way, he is my responsibility. I can't just go back like this."

Em frown "I'm afraid that's not enough. It certainly doesn't outweigh our reasons for sending you home."

stop music fadeout 2.0

c "Just let me explain. I'll tell you everything."

scene black with dissolveslow

$ renpy.pause (0.5)

window show

play music "mx/flashback.ogg"

n "Years ago, our world was prosperous. Our technology was far more advanced than yours, even. Computers not only graced every household, but every single person. It was the age of information." 

n "Even children had the power to access the most advanced knowledge at their fingertips. With our PDAs, our interconnectedness with other people and our environment was greater than ever."

n "From locomotion to repetitious work and household chores, many processes were automated to such a degree that except for our jobs and hobbies, there was nothing that needed to be done by a person anymore."

n "Even the concept of someone wielding a weapon was outdated, as wars were no longer fought by people, but machines."

scene black with dissolve
window hide
nvl clear
window show

n "Looking back, it was probably the single most prosperous time in human history. Exploitation of the environment and other people was at an all-time low, as was crime." 

n "Conversely, our technological advancements had drastically increased quality of life. Humans were no longer required for strenuous and repetitive tasks. Education had reached an all-time high, and many new jobs were created. General happiness had reached levels never before seen."

n "Yet, one day, everything changed."

scene black with dissolve
window hide

$ renpy.pause (0.5)

play movie "cg/chap3/sun2.ogv" loop
show movie with dissolveslow


$ renpy.pause(2.0)
nvl clear
window show

n "A solar flare that was headed for Earth was detected by an automated monitoring system. It was determined to be so powerful that it dwarfed all others ever recorded in history."

n "We had less than a week to prepare. Chaos hit much earlier than that, as people scrambled to shield themselves and their possessions from the incoming ion storm."

n "On a worldwide level, power lines were switched off, satellites re-orientated in space and planes grounded to mitigate the effects that would hit us. "

n "Despite humanity's contingency plan for such an event and all our efforts, we were still not prepared for the sheer magnitude of the solar flare that arrived."

n "It was only then, when our race had become so dependent on technology, that we were immeasurably vulnerable against this kind of disaster."

hide movie with dissolve
stop movie
window hide
nvl clear
window show

n "That day, a force with the power of 10 billion Hiroshima bombs was unleashed into our atmosphere."

n "The eyewitness reports from this day were varied as they were terrifying."

hide movie with dissolve
stop movie
#scene black with dissolve
window hide
show black
show aura1 
with dissolve
$ renpy.pause(3.0)
nvl clear
window show

n "A huge, beautiful aurora could be seen on the horizon before fireballs hurled across the sky."

scene black with dissolve
window hide
show aura2 with dissolve
$ renpy.pause(3.0)
nvl clear
window show

n "In some places, these lights became so bright that even those asleep at night awoke, as though day had already arrived."

n "A coronal mass ejection by itself did not have the power to kill anyone directly, but the side-effects were disastrous."

scene black with dissolve
window hide
nvl clear
window show

n "After the lights in the sky arrived, sparks showered from electrical outlets everywhere, igniting rampant fires in every town and city."

n "Facilities that stored weapons, fireworks or other explosives became centers of widespread destruction and loss of life." 

n "During the next stage, the solar flare started to affect body modifications and caused commonplace pacemakers and nanomachines to fail. 15%% of the world's population died as the result of this alone."

n "Once the full power of the waves hit us, however, society as we knew it collapsed in one fell swoop. Power grids on Earth shut down in an instant, as did all the machines that automated our routine tasks. Long-distance communication and transport became a thing of the past."

scene black with dissolve
window hide
nvl clear
window show

n "Without electrical power, the quality of health care plummeted, and water and sewage systems were crippled. Diseases we thought defeated centuries ago made their comeback in a most unsightly fashion." 

n "Many thought the end of the world had arrived, and in a way it had."

n "Some people blamed whoever their belief system would allow, angry at the gods that had forsaken them. Others pointed their fingers at our lifestyle and society. Not that anyone was listening."

n "Practically, we were back in the middle ages. Governments collapsed and were overthrown, and the ensuing power vacuums filled with groups of people that were sometimes organized and sometimes not."

n "The few functioning electronic devices left became rare, sought after artifacts over which battles and even wars were fought."

scene black with dissolve
window hide
nvl clear
window show

n "Of course, there were also wars over resources and territory. The weaponry used was improvised, or reclaimed from the days when humans had been present on the battlefield. It had been ages, but people returned to the old, bloody ways of war."

n "Humanity is in shambles now."

n "Those that I'd call family and friends now live with me in a giant, mostly self-sufficient city-state of survivors. A huge wall around the perimeter, guarded by militia, prevents any outside interference."

n "It's the only way we can retain a modicum of order. Gangs of raiders and looters run rampant on the outside. They wouldn't hesitate to kill first and ask questions later if they had known about my PDA."

scene black with dissolve
window hide
nvl clear
window show

n "Our contained community has flourished for years now. We have homes to live in, crops to grow and livestock to raise, and still have our own, automated hospital that runs on salvaged generators. Lately, though, supplies have started to run low, and dangerously so."

n "The power we have is running out. Illnesses are spreading through the city, and treatment isn't as available as it used to be. Our population is dropping by the day."

n "We took a great risk to increase the radius of our scouting missions, desperate to find something outside the wall that could help us."

stop music fadeout 2.0

#scene black with dissolve
#window hide
#show intro1 with dissolve
#$ renpy.pause(3.0)
#nvl clear
#window show

#n "And in the end, we did find something. The portal."

window hide

$ renpy.pause (1.5)

scene park3 at Pan ((0, 0), (0, 0), 0.0) 
show emera normal at right
show bryce stern b flip at left
with dissolveslow

play music "mx/barren.ogg" fadein 2.0

c "You already know the rest of this story. We found the portal, and you."

c "And now you know why this whole thing is so important to me. All our hopes lie in acquiring the generators you promised us." 

c "The act of sending Reza and me here has, without a doubt, already cost the lives of some people back home."

c "Beyond the city walls is a dead zone. We haven't heard from any other settlements for months now. The state of the rest of our world is unknown."

c "When Reza and I were sent here, my peers made it clear that this was our last chance. If anything happens to us, no more people will be sent." 

c "If we can't manage to bring back something that will help, we'll have sealed the fate of the tens of thousands that live in our city."

Br "I'm sorry, [player_name]. I didn't know."

Em frown "If what you are telling me is true, it unfortunately does not work in your favor."

Em normal "As sad as your situation may be, it gives Reza a motive. Desperate times call for desperate measures, after all." 

Em frown "In that vein, it also gives you a motive. Considering the gravity of the human plight, it gives you all the more reason to collaborate with him."

c "I'm not. What Reza is doing is wrong. You can't send me away under these circumstances, because I'm your best bet at finding him."

Em normal "Even so, you would still be in grave danger after we announce Reza's involvement in the murders."

Em frown "I cannot and will not take responsibility for the consequences when I know of the risks."

c "What about our deal, then?"

Em ques "In the wake of this new information and as a sign of goodwill, we will send the generators you are owed through the portal once this is over - under two conditions." 

Em normal "Humanity must condemn Reza's actions, and we must reclaim the stolen PDAs."

Br "I've changed my mind. You should let [player_name] stay here."

Em frown "I cannot take your word under consideration in this matter, Chief. Taking into account Maverick's actions, and your responsibility for them, you will have to be dealt with separately."

Em normal "With my authority as the Minister in charge of the human visit, my decision is to have [player_name] sent back to the human world through the portal..."

c "Please..."

Em "... immediately."

Br "..."

c "..."

Em frown "Chief, please arrange for an escort to take [player_name] to the portal now."

Br brow b flip "I could do it myself, Minister."

Em normal "Well, we have our own matters to discuss, Chief, and I would rather get that over with as quickly as possible."

Br stern b flip "In that case, one of my officers should be here any moment. I arranged for him to meet us here."

Em ques "How handy. Then let us wait for this officer of yours."

show sebastian normal b flip at Position(xpos = 0.1) with easeinleft

m "It didn't take long for Sebastian to arrive. After the situation was explained, he was visibly shocked, but didn't protest when he was given the task of sending me back through the portal."

#show bryce at right with ease

Sb "Let's go, [player_name]."

c "Don't I even get to say goodbye?"

Em "Let us not waste any more time. You will still be free to send letters after you have arrived on the other side."

Br "Just go, [player_name]."

Sb "Come on, then."

scene black with dissolvemed

$ renpy.pause (0.5)

scene np3x at Pan((0, 220), (0, 220), 0.0) with dissolvemed

m "We were silent as Sebastian and I slowly made our way to the portal."

play soundloop "fx/steps/steps.ogg" fadein 1.0

m "With each step I took, I drew closer and closer to the hopelessness waiting for me in the ruins of the human world."

scene np2x at Pan((0, 150), (0, 150), 0.0) with dissolvemed

m "All in all, I certainly had a unique experience alongside these dragons, and although this place was filled with just as much drama and murder as back home..."

m "... I would remember this world and all the people I met."

m "I would fondly think back to the days I spent in their comfortable standard of living, a shadow of how humanity used to be."

m "Even without the generators, at the very least I'd be returning home with a few life lessons."

stop soundloop fadeout 2.0

show adine normal b with dissolve

Ad "What's going on here?"

m "Lost in thought, I hadn't even noticed Adine approach."

show adine at right with ease

show sebastian normal b flip at left with easeinleft

Sb "It's none of your concern. Please leave."

c "Can't I even get a few minutes before I go?"

Sb "I suppose nobody's stopping us, but make it quick."

show sebastian normal b

$ renpy.pause (0.3)

hide sebastian with easeoutleft

show adine at center with ease

if adinestatus == "good":
    
    Ad "What's going on here, [player_name]?"

    c "Listen, Adine. Don't take this the wrong way, but I have to leave."

    Ad annoyed b "You're leaving already? Why? And why didn't you tell me?"

    c "It wasn't my choice. The Minister made this decision just a moment ago. You'll be hearing about the reasons soon enough."

    Ad disappoint b "Is it true what I heard? About Reza being a murderer?"
    
    c "I'm afraid so."

    Ad "What does that make you?"

    c "I don't have anything to do with that. I was helping the police find him. "

    Ad "Then why are you leaving?"

    c "They don't want me to stay here with all of this going on. It's for my own safety."

    Ad sad b "Are you going to come back?"

    c "I don't think so."

    Ad disappoint b "..."

    Ad normal b "Hey, at least you could write me some letters, right?"

    m "She looked at me with hopeful, bright eyes."

    m "I thought of the other side of the portal, standing in the desolate human wilderness. I doubted our city would waste our limited energy resources on a pen pal. I doubted I would even see the portal ever again after I returned home."

    c "Maybe. I'd like that."

    Ad disappoint b "And I couldn't even show you my flying. I was just practicing when I saw you down here."

    c "It's a shame. I bet your stunts would have been amazing to see."

    m "We exchanged small, sad smiles."

    c "I guess I should go."

    Ad "Goodbye, [player_name]."

    c "Goodbye, Adine. Take care of yourself."
    
    
elif adinestatus == "neutral":
    
    Ad "Hey, [player_name]. What's going on here?"

    c "Something serious happened. Looks like I have to leave."

    Ad disappoint b "Right now? Why?"

    c "It was the Minister's decision, not mine. You'll hear all about it soon enough."

    Ad "Does this have anything to do with what I've been hearing? Is Reza really a murderer?"

    c "I'm afraid so."

    Ad "Oh."

    Ad "Well, what does that make you?"

    c "I don't have anything to do with that. I was helping the police find him. "

    Ad "Then why are you leaving?"

    c "They don't want me stay here with all of this going on. It's for my own safety."

    Ad normal b "Well, it was nice to get to know you, at least."

    c "Likewise."

    c "I guess I should get going."

    Ad "Goodbye, [player_name]."

    c "Goodbye, Adine."


elif adinestatus == "bad":

    c "What are you doing here?"

    Ad "I was practicing my flying when I saw you down here. What's going on?"

    c "I'm leaving."

    Ad disappoint b "You're leaving?"

    Ad "Wait, does this have something to do with what I heard about Reza?"

    c "Why do you care? I thought you didn't like me, anyway."

    Ad annoyed b "I don't. You run your mouth like a pro."

    c "That's me."

    Ad "Yeah. You were a huge jerk."

    Ad normal b Ad "But even though you were a jerk, it was extraordinary to have a human around."

    Ad annoyed b "Well, is it true or not?"

    c "About Reza? I'm afraid so."

    Ad disappoint b "Then what does that make you?"

    c "I don't have anything to do with that. I was helping the police find him. "

    Ad "..."

    Ad "When I heard about the humans' arrival, all I wanted was to meet one of you."

    Ad sad b "Now, with all that's happened, I don't know what to think anymore."

    m "She looked disappointed. Not just in me, but probably my entire race."

    Ad disappoint b "Goodbye, [player_name]."

    c "Goodbye, Adine."


elif adinestatus == "none":
    
    Ad "The human on official business, huh?"

    c "I don't even know you right now, do I?"

    Ad "Don't you remember? I met you in the café and at that crime scene."

    c "But that's all, isn't it?"

    Ad annoyed b "Unless I missed something, yeah."

    c "What are you doing out here?"

    Ad normal b "I was just practicing my flying when I spotted you down here, and who would say no to an opportunity to meet one of the humans? Not me."

    c "I'm afraid this will be both our first and last opportunity to talk. I'm about to leave this world again."

    Ad "Is that so? That's too bad." 

    Ad "Kind of a shame I never got to know you."

    Ad disappoint b "Wait, does this have something to do with those rumors I heard? Is Reza really a murderer?"

    c "I'm afraid so."

    Ad think b "What does that make you?"

    c "I don't have anything to do with that. I was helping the police find him. "

    Ad "Then why are you leaving?"

    c "It's for my own safety, apparently. This wasn't my decision."

    Ad disappoint b "Really? But what about Reza?"

    m "All I could offer was a shrug."

    c "I guess they're convinced that they can find him on their own."

    Ad "I see. I'm not sure what to think anymore."

    c "I'm not sure, either."

    m "I looked over my shoulder and glanced at Sebastian."

    c "I should be going now."

    Ad "Alright. Goodbye, [player_name]."

    c "Goodbye, Adine."


else:
    
    Ad "What's going on here?"

    c "Something happened. Looks like I have to leave."

    Ad disappoint b "Right now? Why?"

    c "This wasn't my decision. You'll hear all about it soon enough."

    Ad annoyed b "You could at least have called me or something."

    c "I only found out a few minutes ago."

    Ad "You didn't even call me back when I left you a message. Is that a normal thing humans do? Not calling back?"

    Ad disappoint b "I thought you had fun when we hung out in your apartment, but I guess I was wrong."
    
    Ad "Was I too pushy?" 

    c "That's not it..."

    Ad "And to think I even kinda liked you..."

    Ad "Wait, does this have something to do with what I've been hearing? About Reza being a murderer?"

    c "Yes."

    Ad "Oh."

    Ad "Well, what does that make you?"

    c "I don't have anything to do with that. I was helping the police find him. "

    Ad sad b "Then why are you leaving?"

    c "I can't stay here with all of this going on. They're sending me back for my own safety."

    Ad disappoint b "Fine. It was nice to get to know you a little, at least."

    c "Likewise."

    c "I think I should be going now."

    Ad "Goodbye, [player_name]."

    c "Goodbye, Adine."
    
    
hide adine with dissolve

$ renpy.pause (0.3)

show sebastian normal b flip at left with easeinleft

Sb "I remember her. That was the witness from Reza's first murder. Did you know her?"

menu:
    
    "A little.":
        
        pass
    
    "No.":
        
        $ evilpoints += 1
    
    "Yes.":
    
        pass       
    

Sb "I see."

$ renpy.pause (0.5)

scene np1x at Pan  ((200,200), (450,100), 6.0) with dissolveslow

$ renpy.pause (3.5)

m "A few minutes later, we arrived at the portal, standing proud as ever in defiance of the elements. How many years had the structure survived before it was found?"

show sebastian normal b with dissolve

Sb "I hope I can remember how this thing works..."

c "Are you joking?"

Sb drop b "Yeah, sorry... I got it."

c "Alright. I suppose it's time for us to say goodbye."

Sb normal b "Let's keep it professional. I don't like to mix personal matters with work."

m "He looked away, and I shrugged."

c "Go ahead and turn it on, then."

Sb "Would you stand between the pillars, please?"

c "Of course."

play sound "fx/steps/steps.ogg"

hide sebastian with dissolve

nvl clear

$ renpy.pause (0.7)

window show

n "I took my place and stared toward the horizon while I thought about what would happen now, in this world and others."

stop sound fadeout 2.0

n "Even if I made a break for it, I'd become a fugitive, no better than Reza. It would be near-impossible to investigate the case by myself, while on the run in a world I knew so little about."

n "At the very least, I took comfort in the fact that I did everything I could to help, even if it turned out like this."

n "Nevertheless, I dreaded going back empty-handed and returning to my old life in our ruined city."

n "Any second now, the teleportation process would start, disintegrating my body before I would reappear on the other side. Back in my dying world."

nvl clear

n "I wondered if there was any risk of getting lost somewhere between worlds. We didn't really know how the portals worked, after all. Maybe I would be flung somewhere else in space-time, or it might affect my body in some way."

#being teleported temporarily eliminates the body's limitations

n "I hadn't noticed any unusual changes in my body since I arrived in the dragons' world, but I had no way of knowing if there were potential long-term side-effects."

n "I still remembered the images I saw when I teleported the first time, the vivid sights and patterns. People and situations I have recognized since then. It only took a moment to arrive at the other side of the portal, yet it felt like I had dreamed a thousand dreams."

n "And during the nights I spent here, these dreams had often reappeared."

n "Any time now, I would undergo the same experience again."

nvl clear

n "I was almost relieved that my adventure was over." 

n "Things had turned out far differently than expected. I evaded danger, got swept into a murder investigation and met incredible, intelligent beings from several different species."

n "It had certainly been a time to remember."

show black with dissolve

n "With that thought, I closed my eyes and braced myself for the moment that would come any second now."

n "But that moment never came."

n "The next thing that did happen was that I heard Sebastian's voice." 

window hide 

nvl clear

hide black
show sebastian normal b 
with dissolvemed

$ renpy.pause (0.3)

Sb "It's not working."

c "Are you joking again?"

stop music fadeout 2.0

Sb "No, really. It's not working."

Sb "Wait, what is this?"

show black with dissolve
#$ renpy.pause (0.5)
show portalb at Pan ((0, 0), (600, 380), 8.0) with dissolvemed

play music "mx/threat.ogg"

$ renpy.pause (2.0)

Sb "It's broken."

c "Can you fix it?"

Sb "I don't think so. This doesn't look like a simple act of vandalism. It looks like some parts were torn out."

hide portalb 
hide black
with fade

c "I guess that means I'm not leaving, huh."

Sb "Not yet, at least."

c "Well, what do we do now?"

Sb "Let's head back. The Chief has to know about this right away."

play sound "fx/steps/clean2.wav"

scene black with dissolve

$ renpy.pause (1.0)

scene park3 at Pan ((0, 0), (0, 0), 0.0) 
show emera normal at right
show bryce stern b flip at left
with dissolvemed

m "We were back at the Ministry before long. Emera and Bryce were still outside, as Remy approached the two of them."

show remy normal flip at Position(xpos = 0.1) with easeinleft

Ry "Here are the case files, Emera."

Em ques "Why, thank you."

Ry "[player_name] and an officer? What is this about, Emera?"

Em normal "That is what I would like to know."

Em "Please, officer. Enlighten me. Why has my order not been carried out?"

hide remy with easeoutleft

show sebastian normal b flip at Position(xpos = 0.1) with easeinleft

Sb "The portal is broken."

Br brow b flip "It's broken?"

Sb "Yeah. It looks like someone tampered with it and stole parts. I couldn't even get the interface to turn on."

Br stern b flip "We'll check it out once I'm done here."

Em "I suppose [player_name] will stay with us for a little longer, after all."

Em frown "Seeing how this is an emergency situation, I will make this short."

Em ques "Chief, as a result of your carelessness regarding Maverick and Reza, you are temporarily removed from any duties related to the humans."

Em normal "Given these dangerous times, you will instead serve as my personal escort until further notice."

Em "Considering the circumstances, you will be allowed to coordinate the investigation of the portal, but after that, you are to immediately return to me to start your new task. Understood?"

Br brow b flip "Understood."

Em frown "Then all of you are dismissed."

m "She turned to leave, Remy trailing after her."

show emera frown flip

$ renpy.pause (0.3)

hide emera with easeoutright

$ renpy.pause (0.4)

hide sebastian with easeoutleft

show sebastian normal b at right with easeinright

Br "Alright, let's head to the portal. That includes you, [player_name]."

c "Of course."

stop music fadeout 2.0

m "Out of the corner of my eye, I spotted a sheet of paper on the ground."

c "Hey, what's this?"

play music "mx/politics.ogg"

Br brow b flip "Emera probably dropped one of the case files."

Sb "Either her or her assistant."

Br stern b flip "You better bring that to her. Sebastian and I should hurry to the portal. Meet us there afterwards, okay?"

c "Sure."

show bryce stern b

$ renpy.pause (0.3)

hide bryce with easeoutleft

hide sebastian with easeoutleft


m "I picked up the sheet and started reading. It was about what had happened when I met Reza at the portal. Of course, it didn't say anything I didn't already know."

scene buildingoutside at Pan((0, 0), (0, 0), 0.0) with dissolvemed

m "As I walked up the stairs, I wondered if it was okay for an unauthorized person to enter the building. All I knew about the place was that Emera worked there."

m "I did have an important document that was going to be missed, so I walked inside, only to be greeted by an empty lobby."

m "Luckily, there were some signs directing me to Emera's office."

show corridor with dissolvemed

m "It didn't take long to find it, and I heard voices when I approached the door."

Em "By the way, what happened to the scroll you brought me this morning? The last time I saw it, it did not have that tear."

Ry "I... dropped it."

Em "Tell me something new, for once."

Ry "Okay, someone else dropped it." 

Em "Am I supposed to believe that? Remy, are you aware of how much this costs? Repairing and replacing artifacts is not cheap."

Em "I am afraid we will have to deduct this from your wage again."

Ry "I see."

Em "You are not doing this on purpose, are you?"

Ry "Of course not!"

Em "You have been working for me for a long time now. I expected you to learn at some point, but you are very resistant to do so."

m "Not wanting to listen to this any longer, I decided to knock."

play sound "fx/knocking1.ogg"

$ renpy.pause (2.0)

m "There were a few seconds of silence."

Em "Please, come in."

play sound "fx/door/door_open.wav"

m "I only opened the door long enough to hand Remy the sheet of paper."

c "I think you dropped this outside."

play sound "fx/door/doorclose.ogg"

$ renpy.pause (0.5)

m "After I closed the door and started to walk away, I heard the voices resume."

Ry "This is from one of the case files you requested. You must have dropped it."

Em "Then why was it left outside? As my assistant, you should have paid more attention. If this got into the wrong hands, someone could get in trouble..."

stop music fadeout 2.0

scene black with dissolvemed

$ renpy.pause (0.5)

scene np1x at Pan  ((350,300), (350,100), 6.0) with dissolveslow

$ renpy.pause (3.5)

play music "mx/clouds.ogg" fadein 2.0

m "I made my way back to the portal and arrived shortly after Bryce and Sebastian."

show bryce brow b flip at left with easeinleft

Br laugh b flip "Well, I can confirm that it's not turning on."

show sebastian normal b at right with easeinright

Sb "I told you that already."

Br "Just wanted to be sure."

Sb disapproval b "You really think it would still work with a chunk ripped out of it?"

Br brow b flip "Hey, I'm not an engineer. We don't know how the portal works. It was worth another try."

Br normal b flip "There you are, [player_name]."

Br brow b flip "What do you make of this?"

c "I'm afraid I don't know any more than you do. I'm not an engineer, either."

Sb "In that case, we should start thinking about the \"who\" and \"when\"."

Br stern b flip "There are patrols assigned to the portal and surrounding area day and night."

Br brow b flip Br "If someone tampered with the portal, they must have seen something. Today's day patrol didn't notice anything unusual, though."

Sb "I guess she just missed the part about the portal being vandalized."

Br "It'd be easy to overlook. It's a small part of the machine, and it's not like she was expected to check every square inch of it with each lap around the area."

Sb "What about the night patrol, then?"

Br stern b flip "When I went over the reports this morning, I noticed the night patrol hadn't handed theirs in yet."

Sb "And who was patrolling last night?"

Br brow b flip "Let me think for a minute..."

Br "The schedule always goes in a certain order, so last night would have been..."

stop music fadeout 2.0

Br stern b flip "..."

Br "Damn."

Sb "What is it?"

play music "mx/judgement.ogg" fadein 2.0

Br "The night patrol for last night would have been Maverick. I got wrapped up in all the recent chaos and forgot to find a replacement for him when he went on sick leave."

Br "Maybe Emera was right to take me off the case..."

Sb "So there was no night guard here at all?"

Br "That's right. Whoever it was had an easy time doing whatever they wanted."

c "Could it have been Maverick? If he knew no one was going to be here, he could've used that knowledge to his advantage."

Br brow b flip "He couldn't have known that I'd forget to find a replacement, though. I don't usually slip up like this."

Sb "What about Reza?"

c "Why would he have done it? He'd be cutting off his only way out."

Br stern b flip Br "No, he'd be doing something smart. If he has the part needed to get the portal working again, he's in control of who gets to use it. He's cutting off our ability to communicate with mankind."

Sb "We wouldn't be able to inform them of Reza's actions."

Br "Maybe we shouldn't have kept the investigation secret for this long."

c "If your theory is true, that would be proof that Reza's actions are his own, not humanity's."

Br brow b flip "Hey, I already trust you on that."

Sb "Or it's a stunt to grant humanity plausible deniability."

Br "No way. Things are too dire for the humans to take such an extraordinary risk, especially for that."

Sb "I'm sure that wouldn't be the only reason they'd benefit, though. There must be something we're not aware of."

Br "Maybe we're looking at this from the wrong angle. If no one was here to guard the portal, anyone could have broken it. It doesn't necessarily have to have anything to do with Reza or Maverick."

Sb "But they still have the greatest motives."

Br stern b flip "Sure, but they definitely aren't the only ones to have one. There could be private groups who are interested in the technology or its significance as a human artifact."

Sb "So, that puts us exactly nowhere."

Br brow b flip "At least as far as speculation is concerned. It's about time for forensics to show up, anyway. Let's hope they can pull some clues from all this."

Br stern b flip "Sebastian, can you take it from here? You've been just as dedicated to the case as I have. Since I'll have to be at the Minister's side for a while, I'd like you to take charge of the investigation for now."

Sb "Thanks, Chief. I won't let you down."

c "What's up with that, anyway? Being appointed as Emera's bodyguard as punishment just seems strange to me."

Br laugh b flip "Are you kidding? I could have lost my job. This is a way better outcome. Honestly, she probably did it for her own sake more than anything else, but I'm not complaining."

Br brow b flip "If that's all, I'm going to head back to the Ministry. I shouldn't keep her waiting."

show bryce stern b

$ renpy.pause (0.3)

hide bryce with easeoutleft

show sebastian at center with ease

c "So, what does that make you now? Temporary chief?"

Sb "More like case leader."

Sb "By the way, you won't need to stick around while forensics does their job. Thanks for your help."

Sb "I assume you can find your way back to your apartment?"

c "Yeah, of course."

Sb "Alright. I'll see you later, then."

c "See you."

stop music fadeout 2.0

scene black with dissolvemed

$ renpy.pause (1.0)

scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

play music "mx/barren.ogg" fadein 2.0

m "I considered spending my free time roaming the town, but decided that it would be best to keep myself out of the spotlight." 

m "After cooking myself a rudimentary meal, I considered picking up another book when the doorbell rang."

play sound "fx/door/doorbell.wav"

$ renpy.pause (1.5)

stop sound fadeout 0.5

window hide

play sound "fx/door/handle.wav"

$ renpy.pause (1.5)

nvl clear

show sebastian normal b with dissolve

Sb "Hey, [player_name]."

c "Hey, Sebastian. Do you need my help again?"

Sb "We're just a small town police department, and with Bryce removed from the case, our resources are thinner than ever."

c "I understand. So, what do you have for me?"

if annasurvives == False:
    
    Sb "First up is the primary witness in the latest murder. Damion, the victim's assistant. He was the one who found her body." 
    
    Sb "A few things have changed since this morning, as we've gotten some additional information from forensics that warrants further questioning." 
    
    Sb "I know you knew the victim personally, so you don't have to do this if you don't want to. I'll leave the choice to you. You can find her assistant at the production facility."


elif damionsurvives == False:
    
    Sb "First up is the primary witness in the latest murder. The victim's colleague, Anna. She was the one who found his body." 
    
    Sb "A few things have changed since this morning, as we've gotten some additional information from forensics that warrants further questioning. She can be found in the production facility."
    
else:
    
    pass
    
    
Sb "You seemed interested in that underground building found near the portal. I realized you might actually be able to help us with that. Since it's suspected to be of human origin, your opinion would be greatly appreciated."

c "I guess I should add \"Archaeologist\" to my resume."

Sb smile b "Maybe \"Human Matters Consultant\" would be more appropriate."

c "Do you really think it's okay for me to tamper with your priceless discoveries?" 

Sb normal b "Oh, you wouldn't actually go there in person. I just want you to take a look at the collected information in the archives and give us your opinion."

Sb "Besides, no one is allowed to visit at the moment. The building is old and unstable, and there is a danger of it collapsing or flooding. Obviously, we don't want either of those to happen."

c "Flooding?"

Sb "Yes. The whole building is underground, and we've determined that there is a rather large pocket of water surrounding it. Any kind of disturbance could endanger everything and everyone inside."

c "I see."

if annasurvives == False:
    
    Sb "We also located another witness for the latest murder. A store clerk reported seeing and hearing something, so it's probably worth it to ask him a few questions."
    $ c3facavailable = True

elif damionsurvives == False:

    Sb "We also located another witness for the latest murder. A store clerk reported seeing and hearing something, so it's probably worth it to ask him a few questions."
    $ c3facavailable = True

else:

    Sb "We also located a witness for the break-in at the facility. A store clerk reported seeing and hearing something, so it's probably worth it to ask him a few questions."
    $ c3facavailable = False

c "Got it."

play sound "fx/paper.wav"

Sb "Here are all the details. Visit me at the department once you're done."

c "Sure thing."

hide sebastian with dissolve

m "It was interesting that they still relied on me for their investigations, even after they tried to send me back to my world. I didn't expect them to allow me to help with police matters after everything that had happened."

m "Now that the possibility of sending me back was eliminated, the advantages of having me on their side apparently outweighed the risks. Though, I had to wonder who would have to be more careful from now on."

#determine if witness/visiting production facility is available:
label c3skip:

$ c3sectionsplayed = 0
$ c3arcavailable = True
$ c3stoavailable = True

if persistent.endingsseen >= 5:
    
    if persistent.c3pointless == False:

        $ persistent.c3pointless = True
        
        $ achievement.grant("Utterly Pointless Achievement")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_15
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You did a thing! Achievement unlocked."
            
        elif system == "advanced":

            s "You did a thing. Achievement unlocked. Wait, what?"
            
        else:
            
            s "You did a thing. Achievement unlocked. Don't look at me, I'm just the messenger."


label c3sections:
    
    if c3sectionsplayed == 0:
        
        menu:
            
            c "(What should I do?)"
            
            "Visit the production facility." if c3facavailable:
                
                play sound "fx/steps/clean2.wav"
                stop music fadeout 2.0
                scene black with fade
                $ c3sectionsplayed += 1
                $ c3facavailable = False
                jump c3fac


            "Visit the police archives." if c3arcavailable:
                
                play sound "fx/steps/clean2.wav"
                stop music fadeout 2.0
                scene black with fade
                $ c3sectionsplayed += 1
                $ c3arcavailable = False
                jump c3arc
                
                
            "Visit the store." if c3stoavailable:
                
                play sound "fx/steps/clean2.wav"
                stop music fadeout 2.0
                scene black with fade
                $ c3sectionsplayed += 1
                $ c3stoavailable = False
                jump c3sto

    elif c3sectionsplayed == 1:
        
        
        m "Before deciding my next move, I returned to my apartment for a moment of rest. A small piece of paper had been slipped under my door while I was gone."
        
        play sound "fx/paper3.ogg"
        
        play music "mx/intrigue.ogg"

        m "\"Don't go to the portal.\" was all it said. I considered the possibility of a hidden message, but that was unlikely; the statement was blunt and quickly scrawled."

        m "Someone clearly didn't want me to go to the portal, but why would I go there in the first place? As it was out of order right now, such an action would serve no purpose."
        
        stop music fadeout 2.0
        
        m "I looked outside the window, at the portal's faint silhouette in the distance. The paper rustled between my fingers as I fidgeted with it, wonderering about the message's sender and significance."
        
        play sound "fx/gunshots.ogg"
        
        m "My train of thought was violently interrupted by a sharp burst of gunfire, echoing from the portal."
        
        play music "mx/chip.ogg" 
        
        m "I had to think fast. The gunshots ensured Reza's involvement. He was at the portal. The question was: Why?"

        m "If this was his attempt to flee back to the human world, he would receive a rather unpleasant surprise the moment he would try to use the portal."
        
        m "Or maybe Sebastian's theory was correct, and Reza held the part needed to repair the portal, in which case his escape could be imminent."

        m "The gunshots themselves were another question. Was someone trying to stop him? The police patrol may have seen him, and he may have been taken by surprise. This could be another murder in progress."

        m "But all of his murders were committed with a sharp weapon before now, not a gun. He didn't want to be heard."

        m "Besides, it was only early evening, and the town was still bustling. If Reza wanted to stay hidden, he was doing a rather poor job at it."

        m "Of course, there was also the possibility that he wanted to be heard, but who would he want to attract?"

        m "The police? Maverick? It could easily be a trap for those hunting him, and that technically included me, though I wasn't sure if he knew of my involvement in the investigation."

        m "It was also a very real possibility that he knew my apartment was close enough to the portal to hear a gunshot. Could it be a signal for me?"

        m "Regardless, the words I held in my hands were unmistakable: {i}Don't go to the portal.{/i}"

        c "(What should I do?)"
        
        menu:
            
            "Stay inside and call the police.":
                
                $ c3stay = True

                m "Ultimately, I trusted the mysterious message. Remy's list of phone numbers, given to me when he brought me to this apartment in the first place, proved to be a valuable tool. I dialed the emergency line and was greeted by a calm voice asking me about my emergency."

                m "The gravity of the situation was understood, and I was advised to stay inside until further notice. A team was dispatched to deal with the situation while I waited. From my window, I tried to catch a glimpse of what was going on at the portal, but I couldn't see much. The dark of night was fast approaching."
                
                m "About an hour later, I was informed the team had searched the perimeter, though no trace of Reza was found."

                stop music fadeout 2.0
                
                m "I was given the go-ahead to continue with my investigation, but I was free to stay where I was if I felt unsafe."
                                
                #menu goes here
                
                menu:
        
                    c "(I've got some more time left. What should I do?)"


                    "Visit the production facility." if c3facavailable:
                        
                        play sound "fx/steps/clean2.wav"
                        stop music fadeout 2.0
                        scene black with fade
                        $ c3sectionsplayed += 1
                        $ c3facavailable = False
                        jump c3fac


                    "Visit the police archives." if c3arcavailable:
                        
                        play sound "fx/steps/clean2.wav"
                        stop music fadeout 2.0
                        scene black with fade
                        $ c3sectionsplayed += 1
                        $ c3arcavailable = False
                        jump c3arc
                        
                        
                    "Visit the store." if c3stoavailable:
                        
                        play sound "fx/steps/clean2.wav"
                        stop music fadeout 2.0
                        scene black with fade
                        $ c3sectionsplayed += 1
                        $ c3stoavailable = False
                        jump c3sto

                    "Wait it out.":
                        
                        m "In the end, I decided to wait. Investigating was difficult work, yes, but I decided it would be safer to lay low and stay inside for now. I'd gathered enough information for today."
                        
                        m "Afterwards, it was time to confront Sebastian with my findings."

                        $ persistent.lazynumber += 1
                        call lazycheck from _call_lazycheck_1
                        
                        jump c3go
                        
            
            "Go to the portal.":
                
                #stop music fadeout 2.0
                
                scene black with dissolvemed
                
                $ renpy.pause (0.5)

                scene np3 with dissolvemed
                
                #play music "mx/amb/night.ogg" fadein 2.0
                
                m "The path I took was a familiar one by now. Even with night falling, it was easy for me to find my way around." 
                
                m "Long, grotesque shadows stretched before me, and the atmosphere was eerie and dangerous. I couldn't tell if it was because of the evening's shroud of darkness, or if the urgent situation tugging at my mind had twisted my perception."
                
                scene np2 with dissolvemed
                
                m "I made it past the village border and pressed on. There was still a fair distance to go."
                
                m "Suddenly—"

                m "Gloved hands grabbed me from behind, clamping over my mouth. I couldn't make a sound."
                
                play sound "fx/leather.ogg"
        
                m "From what I could see, it was the same hooded figure I had met in the maintenance room after the second murder." 
        
                "???" "It's too late. Maverick arrived before you did and he'll make sure that no one uses the portal today. Don't follow me."
                
                play sound "fx/fallx.ogg"
                
                $ renpy.pause (1.7)
                
                scene np2 with vpunch

                $ renpy.pause (0.5)

                stop music fadeout 2.0
                
                play soundloop "mx/amb/night.ogg" fadein 10.0
                
                m "I was shoved to the ground, and before I could regain my composure, the figure vanished into the darkness."
                
                m "If Maverick was still in the area, it was not a good idea to stay here. I wouldn't want to fuel his suspicions, or worse."
                
                m "I figured it was time to go back to the police department anyway."
                
                stop soundloop fadeout 2.0
                
                if persistent.c3reckless == False:

                    $ persistent.c3reckless = True
                    
                    $ achievement.grant("Reckless")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_16
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You tried to go to the portal!"
                        
                    elif system == "advanced":

                        s "You tried to go to the portal. Unsuccessfully, I might add."
                        
                    else:
                        
                        s "You tried to go to the portal. And that despite the letter explicitly telling you not to. You rebel."
                
                jump c3go

    else:

        c "(Phew, it's getting late. I better head to the police station now.)"
        
        c "(Do I have everything?)"
        
        c "(Alright, let's see what Sebastian will say to this.)"
        
        jump c3go



label c3fac:

scene facin3 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

#newloremstuff

$ renpy.pause (1.3)

show lorem normal with dissolve

if loremstatus == "abandoned":
    
    Lo happy "Hey, [player_name]!"

    c "Lorem, what are you doing here?"

    Lo normal "I'm just fetching some equipment for my roommate. He's in the middle of an experiment and really needs this stuff." 
    
    Lo think "He sounded very emotional, which is very unusual for him."

    c "Sounds like it's serious."

    Lo happy "And you're here for important human business, I bet."

    c "Sure."

    Lo shy "By the way, are you still up to have those pictures made of you? I left you a message a while ago and haven't heard from you since."
    
    menu:
    
        "I've just been busy lately.":

            $ renpy.pause (0.5)

            Lo think "Oh, I can imagine."

            Lo normal "If you can find the time, I’d certainly appreciate it if we could still make this happen."

            c "I'll try."

            Lo happy "Thanks!"

            Lo think "I should really get going before my roommate blows up the apartment."

            c "Sure. Take care."

            Lo happy "You too!"

            hide lorem with dissolve

            $ loremstatus = "neutral"
            

        "Actually, I'm not sure if I can do that anymore.":

            $ renpy.pause (0.5)

            Lo sad "Really? What a shame."

            Lo normal "The stuff you told me last time should come in handy, at least."

            c "Yeah."

            Lo "If anything changes, just let me know and I'll do what I can to accomodate you."

            Lo think "I should really get going before my roommate blows up the apartment."

            c "Sure. Take care."

            Lo normal "You too!"

            hide lorem with dissolve

            $ loremstatus = "neutral"
    
    
elif loremstatus == "bad":
    
    m "When Lorem spotted me, he opened his muzzle as if he was going to say something."

    show lorem relieved with dissolve

    m "After a moment of hesitation, he walked past me in silence."

    hide lorem with dissolve
    
    
    
elif loremstatus == "none":
    
    Lo "Hey, [player_name]!"

    c "Lorem, right?"

    Lo happy "Yep!"

    Lo think "Did you get a chance to think about what I told you last time?"

    c "Don't worry, I didn't lose your number. They keep me pretty busy, so I don't really have much free time."

    Lo happy "Well, if anything changes, give me a call!"

    c "I will."

    Lo normal "I gotta go now, so take care!"

    c "You too."
    
    hide lorem with dissolve
    
elif lorem2unplayed == True:
    
    Lo happy "Hey, [player_name]!"

    c "Lorem, what are you doing here?"

    Lo normal "I'm just fetching some equipment for my roommate. He's in the middle of an experiment and really needs this stuff." 
    
    Lo think "He sounded very emotional, which is very unusual for him."

    c "Sounds like it's serious."

    Lo happy "And you're here for important human business, I bet."

    c "Sure."

    Lo think "By the way, how about I invite you to our place sometime? There’s another thing you could help me with."

    c "What is it?"

    Lo happy "I'd like to make some pictures of you."

    c "Okay..."

    Lo normal "I want to use them as references for the humans in my game."

    c "I see. Well, I can't promise anything right now, but I'll keep it in mind."

    Lo happy "Great, thanks!"

    Lo think "I should really get going before my roommate blows up the apartment."

    c "Sure. Take care."

    Lo normal "You too!"
    
    hide lorem with dissolve
    
else:
    
    Lo happy "Hey, [player_name]!"

    c "Lorem, what are you doing here?"

    Lo normal "I'm just fetching some equipment for Ipsum. He's in the middle of an experiment and really needs this stuff." 
    
    Lo think "He sounded very emotional, which is very unusual for him."

    c "Sounds like it's serious."

    Lo normal "And you're here for important human business, I bet."

    c "Sure."

    Lo happy "By the way, do you still accept my invitation? I have something really neat planned!"

    c "Sounds great, but I'm pretty busy right now."

    Lo normal "It's no problem, really. Just let me know when you have the time and I'll make it happen."

    Lo think "I should really get going before Ipsum blows up the apartment."

    c "Sure. Take care."

    Lo normal "You too!"
    
    hide lorem with dissolve

#endnewloremstuff

$ renpy.pause (0.5)

c "(This should be the right place.)"

play sound "fx/knocking1.ogg"

$ renpy.pause (2.0)

play sound "fx/door/door_open.wav"

if annasurvives == False:
    
    $ persistent.metdamion = True
    
    if metdamion2 == True:

        $ renpy.pause (1.0)
        
        show damion arrogant with dissolve

        play music "mx/damion.ogg" fadein 2.0
        
        Dm "Oh, it's you again. What do you want?"
        
        
    else:
        
        scene black with dissolve
        $ renpy.pause (0.5)
        #$ renpy.pause (0.3)
        show cgdamion2 at Pan((0, 0), (0, 302), 5.0) with dissolvemed
        $ renpy.pause(3.0)

        hide cgdamion2 
        scene facin3 at Pan ((128, 250), (128, 250), 0.0)
        show damion arrogant
        with fade

        

        play music "mx/damion.ogg" fadein 2.0

        "???" "Can I help you?"

        c "Hello. You are Anna's assistant, right?"

        "???" "Assistant? You must be joking. First off, I was never anyone's assistant. Secondly, the witch is dead, so even if I was, I would've moved up the corporate ladder by now."

        c "But you are Damion, aren't you?"

        Dm face "Yes. Where I come from, people usually introduce themselves before they start asking questions, though."

        c "You don't know who I am?"

        Dm arrogant "Tchk, of course I know who you are, but that doesn't mean you don't need to learn some manners."
        
        Dm "Anyway, what do you want?"
        
        $ metdamion2 = True
        
        
    c "Can I ask you a few questions?"

    Dm "What about?"

    c "Anna's murder."

    Dm face "..."

    Dm "And who are you to go around asking questions like that?"

    c "I'm working with the police on this matter."

    Dm arrogant "And I'm supposed to believe that? For all I know, you could be with the murderer and are just here to find out if I know something that could implicate you."

    c "Well, according to my information, you didn't particularly like the victim. Not only were you the last person to see her alive, but you were also the one who found her. As you may imagine, this warrants some questions."
    
    Dm "You know what? I don't have to listen to this." 
    
    Dm "I don't know who you think you are, barging into my workplace and barking questions, but if you really are with the police, let them know that I won't say one more word on the matter without a lawyer."

    hide damion with dissolve
    
    play sound "fx/door/doorclose.ogg"
    
    $ renpy.pause (0.5)
    
    m "I wondered if Damion was a suspicious person in general, or if the rumors surrounding Reza were affecting his perception of me. Before this, everyone I had talked to during my investigations had been rather cooperative."
    
    stop music fadeout 2.0
    
    $ renpy.pause (0.5)

    show black with dissolvemed

    $ renpy.pause (0.5)

    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    
    jump c3sections
    

else: #if we meet anna instead of damion

    $ renpy.pause (1.5)
    
    show anna normal b with dissolve
    
    play music "mx/jazzy2.ogg" fadein 2.0
    
    if annastatus == "good":
        
        An "Hey, [player_name]. I didn't even call you about the tests yet. To what do I owe the honor?"

        c "I have a few questions about the murder of your colleague."

        An sad b "Is that so? Why do you get to go around asking questions like that? Is it a matter of human interest?"

        c "Actually, yes. You could say so."

        An normal b "Interesting. What's in it for me?"

        c "Hey, I already agreed to your tests. I'm not sure what else I could offer you. Besides, I'm working with the police, so your cooperation would be greatly appreciated."

        An smirk b "Oh, you're working for our police? Now you really have my attention. I want to see where you're going with this, so by all means, go ahead."

        show anna normal b with dissolve
        
        jump c3facques
        
        
    if annastatus == "neutral":    
        
        An "Oh, it's you. I'm a little busy, so I'm not sure if I should take any visitors at the moment."

        c "I have a few questions about the murder of your colleague."
        
        An sad b "Is that so? Why do you get to go around asking questions like that? Is it a matter of human interest?"

        c "Actually, yes. You could say so."

        An normal b "Interesting. What's in it for me?"

        c "Hey, I already agreed to your tests. I'm not sure what else I could offer you. Besides, I'm working with the police, so your cooperation would be greatly appreciated."

        An smirk b "Oh, you're working for our police? Now you really have my attention. I want to see where you're going with this, so by all means, go ahead."

        show anna normal b with dissolve
        
        jump c3facques


    if annastatus == "bad": 
        
        An "Oh, it's you. I'm not sure if I can take any visitors at the moment."

        c "I have a few questions about the murder of your colleague."

        An face b "Is that so? Why do you get to go around asking questions like that? Is it a matter of human interest?"

        c "Actually, yes. You could say so."

        An normal b "Interesting. What's in it for me?"

        c "Hey, I already agreed to your tests. I'm not sure what else I could offer you. Besides, I'm working with the police, so your cooperation would be greatly appreciated."

        An "That all sounds very exciting, but as you know, I'm an extremely busy person. I don't have time for this. Excuse me."
        
        hide anna with dissolve

        play sound "fx/door/doorclose.ogg"
        
        $ renpy.pause (0.5)

        c "(Well, that didn't go as planned. Guess I won't have any luck here.)"

        stop music fadeout 2.0
        
        $ renpy.pause (0.5)

        show black with dissolvemed

        $ renpy.pause (0.5)

        scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

        jump c3sections


    if annastatus == "none": 
        
        An "Oh, the human has finally decided to grace me with its presence. I'm a little busy, so I'm not sure if I should take any visitors at the moment."

        c "Hello. I have a few questions about the murder of your colleague."

        An sad b "Is that so? Why do you get to go around asking questions like that? Is it a matter of human interest?"

        c "Actually, yes. You could say so."

        An normal b "Interesting. What's in it for me?"

        c "I'm not sure I have anything to offer."

        An "Don't undersell yourself. How about you visit me some time? I have a genuine scientific interest in you."
        
        menu:
            
            "No, thanks.":

                $ renpy.pause (0.5)
                
                An face b "That's a shame." 

                An normal b "You know, I should get back to work. I really am busy. Excuse me."

                hide anna with dissolve

                play sound "fx/door/doorclose.ogg"
                
                $ renpy.pause (0.5)

                c "(Well, that didn't go as planned. Guess I won't have any luck here.)"

                stop music fadeout 2.0
                
                $ renpy.pause (0.5)

                show black with dissolvemed

                $ renpy.pause (0.5)

                scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

                jump c3sections


            "Sure.":
                
                An "Oh, great. In that case, I could make time for a few of your questions."
                
                jump c3facques
                
                
    else:
        
        An "Oh, it's you. I can't take any visitors at the moment."

        c "I have a few questions about the murder of your colleague."

        An sad b "Is that so? Why do you get to go around asking questions like that? Is it a matter of human interest?"

        c "Actually, yes. You could say so."

        An normal b "Interesting. What's in it for me?"
        
        c "Hey, I already agreed to your tests. I'm not sure what else I could offer you. Besides, I'm working with the police, so your cooperation would be greatly appreciated."

        An "Cooperation? What a peculiar word. Do you know what it means? It refers to people working together, and everyone making an effort."
        
        An "Cooperation isn't associated with ignoring the person you owe something to, or neglecting to return her phone calls."
        
        c "What? No, that has nothing to do with..."

        An "You know, I'd love to help you, but I'm a very busy person, so I don't really have time for this. Excuse me."
        
        hide anna with dissolve

        play sound "fx/door/doorclose.ogg"
        
        $ renpy.pause (0.5)

        c "(Well, that didn't go as planned. Guess I won't have any luck here.)"
        
        stop music fadeout 2.0
        
        $ renpy.pause (0.5)

        show black with dissolvemed

        $ renpy.pause (0.5)

        scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

        jump c3sections

                        

label c3facques:

    menu:
        
        "What happened the last time you saw him alive?" if c3facques1:

            An "I saw him yesterday evening. There were some tests I needed to run overnight, so instead of staying late to set them up, I had Damion do it. That's what colleagues are for, right?"
            
            $ c3facques1 = False

            $ c3facquesx += 1
            
            jump c3facques
            
        "Can you tell me what happened when you found him?" if c3facques2:
            
            $ renpy.pause (0.5)
            
            An sad b "I might've left early yesterday, but I made up for it by coming in early today, before anyone else. That's why I was the one to find him. I was on my way to my office when I saw him lying in the middle of the hallway, in a puddle of his own blood."
            
            show anna normal b with dissolve
            
            $ c3facques2 = False

            $ c3facquesx += 1
            
            jump c3facques
            
        "What was your relationship to him?" if c3facques3:

            $ renpy.pause (0.5)

            An sad b "We were colleagues, nothing more."

            c "I heard that you didn't particularly like him."

            An normal b "Yeah, but that's not unusal. I don't like most people."

            An face b "He really didn't like me, though."

            c "Why's that?"

            An normal b "He was jealous of my success, and it showed."

            $ c3facques3 = False

            $ c3facquesx += 1
            
            jump c3facques

        "You seem very calm for someone whose colleague was just murdered." if c3facques4:
            
            $ renpy.pause (0.5)
            
            An face b "People die every day. It's a simple fact of life. Besides, I don't see you crying about him, either."

            An normal b "I didn't know him that well, so it's not like someone I actually cared about died."

            An sad b "The world stops spinning for no one. Life goes on. And for me, that means being without an assistant for a while."
            
            show anna normal b with dissolve

            $ c3facques4 = False

            $ c3facquesx += 1

            jump c3facques

        "That's all.":
            
            if c3facquesx > 0:
                
                c "That will be all. Thank you, Anna."

                An "My pleasure."
                
                hide anna with dissolve

                play sound "fx/door/doorclose.ogg"
                
                $ renpy.pause (0.5)

                c "(Time to head back.)"
                
                if c3facquesx >= 4:
                    
                    $c3clues += 1

                    $ c3facd = True
                    
                    if persistent.c3interrogator == False:

                        $ persistent.c3interrogator = True
                        
                        $ achievement.grant("Interrogator 2")
                        
                        $ persistent.achievements += 1
                        
                        call syscheck from _call_syscheck_17
                        
                        play sound "fx/system.wav"
                        
                        if system == "normal":
                        
                            s "You interrogated Anna!"  
                            
                        elif system == "advanced":

                            s "You interrogated Anna. Well done, [player_name]!"  
                            
                        else:
                            
                            s "You interrogated Anna. Anna-lytical!"  
                    
                else:
                    
                    pass

                stop music fadeout 2.0
                
                $ renpy.pause (0.5)

                show black with dissolvemed

                $ renpy.pause (0.5)

                scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

                jump c3sections
                
                
            else:

                $ renpy.pause (0.5)
                
                An face b "What? You didn't even ask me a single question."
                
                An normal b "You know what, I don't have time for your games."

                hide anna with dissolve

                play sound "fx/door/doorclose.ogg"
                
                $ renpy.pause (0.5)

                c "(Time to head back.)"

                stop music fadeout 2.0
                
                $ renpy.pause (0.5)

                show black with dissolvemed

                $ renpy.pause (0.5)

                scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

                jump c3sections

        
label c3arc:

#$ c3arcavailable = False

if seenkatsu == False:
    
    $ seenkatsu = True
    
    scene np3 with dissolveslow

    play music "mx/amb/night.ogg" fadein 10.0
    
    m "I was on my way to the police station when a voice called out to me."

    "???" "Hey, you!"

    "???" "I'm talking to you, human."
    
    show meetingkatsu at Pan ((150, 0), (580, 300), 10.0) with fade #324
    
    $ renpy.pause (8.5)
    
    hide meetingkatsu 
    
    show katsu normal dk
    
    with fade
    
    c "Can I help you?"

    "???" "I certainly hope so. I'm in a little conundrum here. My cart seems to be stuck."

    c "I can see that."

    "???" "I'm Katsuharu, by the way. Local ice cream vendor."

    c "[player_name]. You've probably heard of me by now."

    Ka "Of course, of course."

    Ka exhausted dk "In any case, do you think you can spare some time to help me out? It might take a while, though, so I hope you're not in a rush."
        
    menu:
        
        "Sure, I'll help you.":
            
            $ renpy.pause (0.5)

            $ c3arcavailable = False

            Ka smile dk "Thank you."

            Ka normal dk "Now, I already tried just pulling it out, but I think the axle is going to break if I try to do that again. It wasn't really in the best condition to begin with, honestly, and I heard a crack when I tried to pull it out earlier."

            c "So, what do you want me to do?"

            Ka "The cart is pretty heavy, so I'll be the one lifting it and holding the wheel steady so the axle doesn't break. Once I give you the sign, you start pulling, and hopefully that'll do the trick."

            c "Alright."

            Ka "Here, grab the handles and wait for my signal."
            
            hide katsu with dissolve
            
            m "By the time I had gotten into position, Katsuharu was already on the other side of the cart, getting dirty as he slowly lifted the affected corner of the cart out of the muddy hole."

            play sound "fx/cartlift.ogg"

            Ka "Hng!"

            c "Is that your sign? Should I start pulling now?"

            Ka "Do it! Do it now!"

            m "I started pulling, but the cart turned out to be much heavier than I expected and didn't move."

            Ka "What are you waiting for? Do it already!"

            m "I pulled harder, but the cart still refused to budge. I mustered all my strength before I pulled as hard as I possibly could."

            Ka "Yes! Do it!"
            
            play sound "fx/cartslide.ogg"

            m "Slowly, the cart started moving, and after a few seconds, it was freed from the perilous clutches of the muddy puddle."

            play sound "fx/cartdown.ogg"

            m "With a dull thud, the dragon set the cart down again before he flopped on the ground, exhausted."

            show katsu exhausted dk with dissolve
            
            $ renpy.pause (0.3)
            
            Ka "..."
            
            c "Hey, we did it."

            Ka "Yeah, good job."

            c "Do you want me to call you some help?"

            Ka "No, just need some rest.{p=1.0}{nw}"
            
            Ka "No, just need some rest.{fast}.. and maybe some ice cream."

            Ka "Yes, I'll have some ice cream, and I'll be better in no time."

            c "That must be some pretty good ice cream."

            Ka smile dk "Oh, you have no idea. You must have already heard people talking about my wonderful, unique ice cream experience."

            c "Actually, not really."

            Ka normal dk "Ah, where are my manners! I haven't even properly thanked you yet."

            c "It's no problem."

            Ka "No, I insist. I won't be indebted to you for helping me." 

            c "...What are you planning?"

            Ka smile dk "You are hereby invited to join me for ice cream. As an ambassador, you owe it yourself and humanity to try it."

            c "Maybe I do."

            Ka normal dk "Well, I must get going for now. Here is my number - I'll get you that ice cream some other time."

            c "Thanks."
            
            if persistent.c3helpedkatsu == False:

                $ persistent.c3helpedkatsu = True
                
                $ achievement.grant("Altruist")
                
                $ persistent.achievements += 1
                
                call syscheck from _call_syscheck_18
                
                play sound "fx/system.wav"
                
                if system == "normal":
                
                    s "You helped Katsuharu!"
                    
                elif system == "advanced":

                    s "You helped Katsuharu. How nice of you."
                    
                else:
                    
                    s "You helped Katsuharu. Don't forget about the police station, though."
            
            
            $ katsuavailable = True
            
            stop music fadeout 2.0
            
            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

            $ c3arcavailable = True

            jump c3sections
            
            
        "Actually, I'm kinda busy right now.":
            
            #$ renpy.pause (0.5)

            Ka exhausted dk "Ah, that can't be helped, then."

            c "Sorry."

            Ka normal dk "Don't worry about it. There'll be someone else along soon, I'm sure."
            
            stop music fadeout 2.0
            
            $ renpy.pause (0.5)
            
            scene black with dissolvemed
            
            jump nohelp

        
else:
    
    label nohelp:
    
    scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow

    m "When I arrived at the station, I was met by the police archivist, a dragoness who introduced herself as Kalinth."

    show kalinth normal flip at Position (xpos = 0.3) with dissolve

    play music "mx/chronos.ogg" fadein 2.0

    Kl "You're in luck, [player_name]! Bryce compiled all the case files a while ago. Ever since you came to our world, he seems to be a lot more interested in these human mysteries. I wonder if it has something to do with you?"
    
    Kl "Anyway, you can find all the files here. I'll leave the rest to you."

    $ renpy.pause (0.2)
    
    show kalinth normal
    
    $ renpy.pause (0.3)
    
    hide kalinth with easeoutleft
    
    $ renpy.pause (0.3)

    play sound "fx/door/doorclose.ogg"

    $ renpy.pause (0.5)
        
    label c3arcques:
        
        if c3arcquesx <= 1:
            
            menu:
                
                "Study the blueprint of the underground building near the portal." if c3arcques1:
                    
                    $ renpy.pause (0.5)

                    nvl clear
                    
                    window show
                    #scene black with dissolve
                    scene map with dissolvemed
                    
                    n "The blueprint of the building caught my attention. Apparently, it had been found during their cursory investigation within the building itself."

                    #scene black with dissolve
                    
                    #$ renpy.pause (0.5)
                    #window hide
                    #scene map with dissolve
                    #$ renpy.pause(2.0)
                    #nvl clear
                    #window show
                    
                    n "At first glance, nothing about it stood out to me, but the more I studied it, the more the facts revealed themselves."
                    
                    n "Both of its entrances were freed and accessible by the people in charge. One was through a tunnel in the vicinity of the portal, and the other through a dig that cut through the town's sewer system."
                    
                    n "Bryce had scrawled a note near the second entry. It simply said:\nAccess v. hatch\nbutton, button, counter-clockwise"
                    
                    nvl clear
                    
                    n "Furthermore, the data in the corner of the blueprint listed the structure as an \"independent living and research unit\" dated to the year 2047."
                    
                    n "Most interestingly, I recognized the name of the company that was listed."

                    n "They were a well-established supercompany before our world's collapse, known for their advances in scientific fields and otherwise through the use of legal loopholes and grey markets."
                    
                    n "They were very successful at what they did. Their facilities subverted laws and ethical issues by being in areas where such concerns were non-existent, or could be made non-existent by paying off the right individuals."
                    
                    n "Naturally, the products and applications of their research was usually fair game to be used and sold worldwide."
                    
                    nvl clear
                    
                    n "They were only one of the companies involved in championing the teleportation technology that was about to take off on a grand scale before the solar flare changed everything." 
                    
                    n "Of course, there were public worries regarding the untested, long-term consequences of utilizing black holes in such technology. It was outlawed in certain countries due to these concerns, but lobbies and the private sector drove many of them to accept the tech, in light of the boundless advantages offered."
                                                                                                                                                                                                                                                                                                                                    
                    n "They were also big in medical, security, and weaponry fields. Their vast knowledge and close cooperation of their individual departments enabled them to make many breakthroughs."
                    
                    n "It seemed like they could do anything they set out to do."
                    
                    nvl clear

                    n "The nanomachines that became commonplace before the fall were, of course, also their product." 
                    
                    n "No one was surprised that the tech failed under the radiation of the ion storm. Had the company behind it been more concerned about safety rather than profits, perhaps fewer lives would have been lost."
                    
                    n "Even though they weren't perfect, nanomachines had still increased the quality of life for many people." 
                    
                    n "It was a new way of treating medical conditions, some of which had been previously untreatable. They were also widely used for their performance-enhancing properties, for both day-to-day activities and to assist with dangerous jobs."

                    nvl clear

                    n "Beyond that, the company had even branched into genetic engineering."
                    
                    n "Human hereditary diseases were becoming a thing of the past, as they developed techniques to alter human life to its core."

                    n "Ultimately, they had a hand in influencing every area of life on a global scale. It was unknown who has truly calling the shots, as their network of companies and names was vast."
                    
                    n "It was only one of their many ways to ensure their continued existence and avoid liability."
                    
                    n "Where they had been outlawed or their operations shut down, new companies with suspiciously similar products appeared practically overnight." 
                    
                    #n "Of course they were also under a constant barrage of criticism since their existence for their questionable methods and ethics." 
                    
                    #n "They expertly maneuvered the legal system and the world in order to keep doing what they were doing. Where they had been outlawed or their operations shut down, new companies with suspiciously similar products appeared practically overnight." 

                    n "However, no matter how big their empire was and how well they skirted the lines, they ultimately collapsed just like the rest of the world."
                    
                    nvl clear
                    
                    n "That being said, how did this building make its way into the dragons' world?"
                    
                    $ c3clues += 1
                    
                    $ c3arcd = True
                    
                    scene black with dissolve

                    window hide

                    scene office at Pan ((0, 250), (0, 250), 0.0) with dissolvemed
                    
                    nvl clear
                    
                    if persistent.playedadine2 == True:
                        
                        if adinestatus == "bad":
                            
                            pass
                        
                        elif adinestatus == "abandoned":
                            
                            pass
                            
                        else:
                            
                            if persistent.havemap == False:
                                
                                #if adinerequestmade == True:
                                
                                #    m "As I pondered this, Adine's request came to mind. I used Bryce's machine to make a copy of the map for her. Bryce probably wouldn't approve of me giving evidence to civilians, but I was sure he would never even realize it."
                                    
                                #else:
                                    
                                #    m "As I pondered this, I realized the importance this might have to our own people. I used Bryce's machine to make a copy of the map. Who knew when it might come in handy?"
                                    
                                m "As I pondered this, Adine's request came to mind. I used Bryce's machine to make a copy of the map for her. Bryce probably wouldn't approve of me giving evidence to civilians, but I was sure he would never even realize it."
                                
                                $ persistent.havemap = True
                                
                                if persistent.havemapfirst == False:
                                
                                    $ persistent.achievements += 1

                                    $ achievement.grant("Cartographer")
                                    
                                    $ persistent.havemapfirst = True
                                
                                call syscheck from _call_syscheck_19
                                
                                play sound "fx/system.wav"
                                
                                if system == "normal":
                                
                                    s "You acquired a map! {image=image/ui/status/havemap.png}"
                                    
                                elif system == "advanced":

                                    s "You acquired a map. For now. {image=image/ui/status/havemap.png}"
                                    
                                else:
                                    
                                    s "You acquired a map. Actually, it's a blueprint. {image=image/ui/status/havemap.png}"
                                

                                
                            else:
                                
                                m "As I pondered this, Adine's request came to mind. I reached into my pocket and realized I still had a copy of the map that I had made some time ago. I would have to remember to give her it next time."
                            
                    else:
                        
                        pass
                    
                    $ c3arcques1 = False
                    
                    $ c3arcquesx += 1
                
                    jump c3arcques
                    

                "Read the structural damage report of the underground building near the portal." if c3arcques2:

                    $ renpy.pause (0.5)
                    
                    play sound "fx/paper.wav"
                    
                    nvl clear
                    
                    window show
                    
                    n "According to the report, the investigation of the building was halted due to the acute danger of its collapse, and the damage that the surrounding water could cause."
                    
                    n "Since the building had unknown historical and technological value, there was a plan in place to drain the water pockets. The legal permissions had not yet gone through, however, and it would take some time for the equipment to arrive."
                    
                    n "For now, the building was stable as long as it remained undisturbed, but for obvious reasons, no one was allowed to enter. There were patrols guarding it day and night."
                    
                    window hide
                    
                    nvl clear
                    
                    $ c3arcques2 = False

                    $ c3arcquesx += 1
                
                    jump c3arcques

                "Play a prank." if c3arcques3:

                    c "(Okay, here we go.)"
                    
                    play sound "fx/undecipherable.ogg"
                    
                    $ renpy.pause (2.0)
                    
                    c "(That should do it.)"

                    m "I wasn't sure when Bryce was going to be in his office again, but when he returned, he would definitely notice this."
                    
                    if persistent.c3prank == False:

                        $ mp.prankster = True
                        $ mp.save()

                        $ persistent.c3prank = True
                        
                        $ achievement.grant("Prankster")
                        
                        $ persistent.achievements += 1
                        
                        call syscheck from _call_syscheck_20
                        
                        play sound "fx/system.wav"
                        
                        if system == "normal":
                        
                            s "You pranked Bryce!"
                            
                        elif system == "advanced":

                            s "You pranked Bryce. My condolences to him."
                            
                        else:
                            
                            s "You pranked Bryce. You naughty, naughty person."

                    $ c3arcques3 = False

                    $ c3arcquesx += 1
                    
                    $ c3arcprank = True
            
                    $ evilpoints += 2
                
                    jump c3arcques

                "Rummage through the trash." if c3arcques4:
                    
                    c "(Alright, here goes nothing.)"

                    play sound "fx/rummage2.ogg"

                    $ renpy.pause (1.5)


                    if persistent.base_taken == False:

                        $ persistent.base_taken = True
                        
                        $ achievement.grant("Base Finder")
                        
                        $ persistent.achievements += 1
                        
                        c "(Huh, what's this?)"

                        c "(It's a flat base, with a circular indent at the top.)"

                        if persistent.ixomenbookread == True:
                        
                            c "(Where have I seen this before?)"

                            c "(Oh, right. It's an Ixomen Sphere part.)"
                        
                            call syscheck from _call_syscheck_21
                            
                            play sound "fx/system.wav"
                            
                            
                            s "You acquired an Ixomen Sphere part (Base)! {image=image/ui/status/base_taken.png}"
                            
                            
                        else:

                            c "(It looks like it could be useful. If nothing else, it might make a nice souvenir.)"
                            
                            call syscheck from _call_syscheck_22
                            
                            play sound "fx/system.wav"

                            if system == "normal":
            
                                s "You acquired a mysterious base! {image=image/ui/status/base_taken.png}"
                                
                            elif system == "advanced":

                                s "You acquired a mysterious base. How basic. {image=image/ui/status/base_taken.png}"
                                
                            else:
                                
                                s "You acquired a mysterious base. Now you only have to find something vaguely spherical to put in it. {image=image/ui/status/base_taken.png}"


                    else:
                        
                        c "(There doesn't seem to be anything useful here.)"
                        

                    
                        
                    
                    $ c3arcques4 = False

                    $ c3arcquesx += 1
                
                    jump c3arcques
            
        else:
            
            c "(Huh, look at the time. I better wrap it up here.)"
            
            stop music fadeout 2.0
            
            $ renpy.pause (0.5)

            show black with dissolvemed

            $ renpy.pause (0.5)

            scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

            jump c3sections


label c3sto:

scene store2 at Pan ((0, 360), (0, 150), 3.0) with dissolveslow

$ renpy.pause (1.0)

play music "mx/zhong.ogg" fadein 2.0

if persistent.playedzhong == True:
    define St = Character("Zhong", color="#7e9147", image="zhong")

if metclerk == False:
    
    $ renpy.pause (0.5)
    
    show cgclerk2 at Pan ( (0, 0), (0, 327), 6.0) with fade

    $ renpy.pause (4.5)

    hide cgclerk2 with fade

    c "(Who's he talking to?)"
        
else:
    
    pass

if persistent.seenvarain2 == True:
    
    $ renpy.pause (0.3)
    
    c "(Oh, it's her again.)"
    
else:

    $ renpy.pause (0.3)

    c "(Hey, I think I've seen her before.)"

show vara normal flip at left with easeinleft

show zhong normal c at right with easeinright

$ metclerk = True
    
    
St "If you've mixed up the prescriptions again, then I can't help you. I can't refill this one." 

show vara sad flip with dissolve

St "We're just about to close, so you'll have to bring the right one tomorrow."

#Vr shocked2 flip "..."

hide vara with dissolve

show zhong at center with ease
    
if chapter2storeunplayed == False:

    St "Hello, [player_name]. How can I help you?"

elif brycebar == True:

    St "Hello, [player_name]. How can I help you?"

    c "Wait, aren't you the bartender from the other day?"

    St "That I am."

    
else:
    
    St "Hello, [player_name]. How can I help you?"

    c "You know who I am?"

    St "How could I not? Everyone knows about you."
    
    
St "Actually, I'm just about to close up here, so please make it quick."

c "I'm here on behalf of the police, and I was hoping that you could answer a few questions."

St "I see. Well, I don't mind as long as you make it quick. I have to leave for my other job soon."
    
show zhong at right with ease

show vara sad flip at left with easeinleft

St "Vara, what are you still doing here? I already told you. You have to come back tomorrow."

St "Here, have a lolly on the house."

#show vara shocked2 flip with dissolve

$ renpy.pause (0.3)

$ persistent.seenvara = True

show vara sad

$ renpy.pause (0.3)

hide vara with easeoutleft
    
play sound "fx/door/bell.ogg"

$ renpy.pause (0.3)

St "I guess she doesn't want it."

show zhong at center with ease

c "What's the deal with her?"
    
if chapter2storeunplayed == True:

    St "She comes here occasionally to pick up her mother's prescription."
    
else:
    
    pass

    
St "I'm not sure what's up with her lately. This isn't the first time this has happened. One time the doctor forgets to issue a new prescription, another time she brings me an expired one instead of the new one."

St "She isn't exactly the brightest, but this is unusual even for her."

St "So, what did you want to know?"
    
if persistent.playedadine2 == True:
    
    label chapter3canfollowvara:

    if persistent.seenvarain2 == True:
        
        if adinestatus == "bad":
            
            pass
            
        else:
            
            menu:
                
                "Follow Vara.":
                    
                    jump follow
                    
                    
                "Stay.":
                    
                    pass
                    
elif persistent.remy2picturesseen == True:
    
    jump chapter3canfollowvara
    
label stay:
    
c "As I said, this is about an ongoing police investigation. You reported seeing something yesterday evening, and any information you have could help."

c "Can you tell me exactly what happened?"

St "Of course. This was after I came back from my second job, so around two or three in the morning."

St "It was dark, and I couldn't make out much, but the police requested that anything unusual be reported."

c "And what did you see?"

St "There was a human-like figure walking away from the production facility. Seemed to be in a hurry, too."

c "And you are sure this was a human?"

St "Unmistakably so. I couldn't make out any details, though. Honestly, if you were the figure, I wouldn't have been able to tell the difference."

c "What did you do when you saw it?"

St "Nothing. I was on my way home, and it was a little unusual, but I wouldn't have bothered to mention it under normal circumstances. I only did because of the police's request for witnesses."

c "Do you know what direction the person went?"

St "One second. It will be easier to draw a sketch for you."

c "That would be great, thanks."

play sound "fx/writing.ogg"

m "He grabbed a piece of paper and drew on it with a thick felt-tip pen."

St "Here. This is the east entry of the facility, and this is where they went."

c "So, away from the main district?"

St "I guess so."

c "Okay. That will be all. Thanks for your help."

St "You're welcome."

$ c3clues += 1

$ c3stod = True

stop music fadeout 2.0

$ renpy.pause (0.5)

show black with dissolvemed

$ renpy.pause (0.5)

scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

jump c3sections


label follow:
    
    #continue here

    c "Actually, excuse me. Sorry, but we'll have to do this another time."

    St "If you say so."
    
    #play sound "fx/door/bell.ogg"
    
    stop music fadeout 2.0

    scene black with dissolvemed
    
    $ renpy.pause (0.5)
    
    scene town1x at Pan((0, 0), (0, 0), 0.0) with dissolvemed
    
    play music "mx/amb/night.ogg" fadein 2.0

    m "Luckily, she hadn't gotten too far, so I followed her from a distance."
    
    play sound "fx/steps/rough_gravel.wav"

    m "Minutes passed as we walked through streets weaving through an unfamiliar part of town. The young dragon looked small and lonely on the empty road."
    
    scene forestx at Pan((0, 0), (0, 0), 0.0) with dissolvemed
    
    m "Before long, we passed the village border, yet she pressed on and stepped into the forest."
    
    m "I turned back once to gaze at the village on the far horizon, and in an instant the dragon was gone."
    
    m "I rushed to the spot I'd seen her last and found the entrance to a cave on a hillside."
    
    stop music fadeout 2.0

    scene cave with fade
    
    show vara normal flip at right with dissolve
    
    m "When I peered inside, I saw Vara alongside a much larger, orange dragon. The small dragon filled a bowl with a thick fluid and placed it front of the other."
    
    m "Then she placed her hands on the large dragon's chin. Gently, she lifted its huge muzzle and guided it toward the bowl. But when she released it, the dragon's head slumped and fell into the liquid. The bowl tumbled sideways and spilled its contents across the cave floor."
    
    play sound "fx/bowlspill.ogg"
    
    #show vara shocked2 flip with dissolve
    
    $ renpy.pause (0.5)
    
    show vara shocked2 flip with dissolve

    $ renpy.pause (1.0)

    show oranged at Pan ((580, 326), (0, 100), 7.0) with fade

    $ renpy.pause (7.5)

    m "I realized then, that other than what Vara had done, the orange dragon hadn't moved at all since I arrived."

    scene black with dissolveslow
    
    $ renpy.pause (1.0)

    scene cave with dissolveslow

    show sebastian normal b with dissolve
    
    Sb "How did you even find out about this?"

    c "I could tell something was wrong, so I followed her."

    Sb "I see."

    Sb "Well, good job, [player_name]."

    c "What's going to happen to her now?"

    Sb "She'll be sent to the orphanage. The background check determined that she had a father, but the two hadn't seen each other in years."
    
    c "Can't you locate him?"

    Sb "We did. Reza's second victim, the maintenance guy. That was him."
    
    c "..."

    c "I see."

    c "How did it even get this far?"

    Sb "I don't know, but we'll certainly look into it."

    Sb "Some just fall through the cracks of the system."

    Sb "Being out here on their own probably didn't help."

    c "Do many of your people live outside the town like this?"
        
    Sb "Well, some do it on principle. Others because they have no other choice."

    Sb "Houses and apartments can be expensive, and it's not unusual for us to use natural environments as our homes."

    Sb "Alright, I think we're done here for now. Don't forget to stop by the department later."

    c "I won't."
    
    $ varasaved = True
    
    hide sebastian with dissolve
    
    $ renpy.pause (0.5)

    show black with dissolveslow
    
    if persistent.varasaved == False:
        
            $ renpy.pause (0.5)

            $ persistent.varasaved = True
            
            $ achievement.grant("Stalker")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_23
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You followed Vara!{image=image/ui/status/varasaved.png}"
                
            elif system == "advanced":

                s "You followed Vara. Well done, [player_name].{image=image/ui/status/varasaved.png}"
                
            else:
                
                s "You followed Vara. Well done, [player_name].{image=image/ui/status/varasaved.png}"

    $ renpy.pause (0.5)

    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed

    jump c3sections
    

label c3go:

scene black with dissolvemed

$ renpy.pause (0.5)

scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow

$ renpy.pause (1.0)

play music "mx/barren.ogg" fadein 2.0

show sebastian normal b with dissolve

Sb "There you are, [player_name]."

c "It seems to me you've taken a liking to Bryce's chair." 

Sb smile b "Maybe. I could get used to this."

Sb normal b "Don't tell Bryce, though." 


if c3stay == True:
    
    Sb "By the way, good job calling the police when you heard Reza. It's too bad he got away again, but maybe a witness will come forward and we'll find out what happened." 
    
else:

    Sb "By the way, we have evidence that Reza visited the portal today." 
    
    Sb "Someone reported loud bangs consistent with what we know about his weapon. We didn't manage to catch him, but I wonder if this stunt means he's getting desperate."
        
    c "Who knows."
    
    
Sb "Now, let's take a look at what you've got for me."

if c3facd == True:
    
    Sb "The witness report from Anna is good. Nothing new to us, but it's nice to have her statement in writing."
    
else:
    
    pass
    

if c3arcd == True:
    
    Sb "What you've learned about the map is fascinating, if not a little unsettling. While it's good to have confirmed its origin, to know that it came from your world is something else."
    
    Sb "It raises more questions than it answers. How could something like a whole building end up in our world? It's a mystery that needs to be answered."
    
    
else:
    
    pass
    

if c3stod == True:
    
    Sb "The statement from the store clerk is interesting. We've had few reports of Reza since he went into hiding, so this is very helpful. It's another confirmation of his involvement in this whole matter."
    
else:
    
    pass

    
    
if varasaved == True:

    Sb "You did great today, [player_name]. The police department is glad to have you on our side."
    
    Sb "You saved that little girl. As far as I am concerned, nothing else you could have done would have mattered as much." 
    
    Sb "Good job, [player_name]."
    
    if persistent.c3investigator == False:

        $ mp.investigator3 = True
        $ mp.save()

        $ persistent.c3investigator = True
        
        $ achievement.grant("Investigator 3")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_24
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You did well on the third investigation!"
            
        elif system == "advanced":

            s "You did well on the third investigation. Investiga-tastic."
            
        else:
            
            s "You did well on the third investigation. I am running out of things to say here."

    $ chap3inv = 5
    
    $ persistent.c3skip = True
    
elif c3clues == 2:

    Sb "You did great today, [player_name]. The police department is glad to have you on our side."

    if persistent.c3investigator == False:

        $ persistent.c3investigator = True
        
        $ achievement.grant("Investigator 3")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_25
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You did well on the third investigation!"
            
        elif system == "advanced":

            s "You did well on the third investigation. Investig-awesome."
            
        else:
            
            s "You did well on the third investigation. I am running out of things to say here."

    $ chap3inv = 5

    $ persistent.c3skip = True

elif c3clues == 1:
    
    Sb "Not bad, [player_name], not bad at all. Thanks for your help."

    $ chap3inv = 3

else:
    
    Sb "Hmm, this isn't much information to go on, but who knows when it could come in handy."
    
    $ chap3inv = 1
    
$ totalinv += chap3inv #now we have a total inv between 3 and 15

if totalinv > 14:

    if persistent.c3flawless == False:

        $ mp.flawless = True
        $ mp.save()

        $ persistent.c3flawless = True
        
        $ achievement.grant("Flawless Run")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_26
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You did well in all investigations!"
            
        elif system == "advanced":

            s "You did well in all investigations. Phew."
            
        else:
            
            s "You did well in all investigations. Maybe you should be a private detective."

c "I do what I can."

Sb "I know, and your help is greatly appreciated - believe me. Especially since we're so short on staff right now."

Sb "That will be all for today. I'll contact you if we need anything."

c "Of course."

$ persistent.c3skip = True

#insert ixomen sphere scene here

if persistent.base_taken == False:

    if persistent.orb_taken == True:

        if persistent.lorem2skip == True:
            
            c "By the way, I found an Ixomen Sphere in the park a while ago and was told to hand it over to you."

            Sb "Oh, yes. Those things are really expensive. I'm sure the owner will greatly appreciate it if they get it back."

            m "I dug into my pockets only to realize that the Ixomen Sphere was still resting on the table in my apartment."

            c "Oh, looks like I don't have it on me."

            Sb "If it is registered, you only need to turn it on and you should be able to find out who it belongs to."

            c "I already tried that, but I think it's out of battery."

            Sb "Maybe we could find you a charging base, then."

            Sb disapproval b "Actually, we had one in our lost and found box."

            Sb normal b "Bryce keeps it somewhere around here. Let me check."
            
            hide sebastian with dissolve
            
            m "He got up and over to one of the tables. He picked up a box from under it and returned to me."

            show sebastian normal b with dissolve
            
            play sound "fx/bg.wav"

            Sb "There it is! Let's see..."
            
            play sound "fx/rummage.wav"

            m "He rummaged around the box for a bit."

            Sb drop b "That's strange... It's not here. I remember seeing it when I came in today, so he must've thrown it out earlier."
            
            c "Right before we actually needed it."

            Sb normal b "To be fair, it’s been in there for quite a while. No one’s going to miss those tail bands that have been in there for a few weeks either."

            Sb disapproval b "But if he was going to throw it out, it might still be in the bin."

            c "And the plot thickens."

            m "He cocked his head to the side. We both peered into the trash can that was next to the table, but it was empty."

            Sb normal b "Sorry to disappoint you."

            c "This is an emotional roller coaster."

            Sb "If you came in a few hours ago we might've still had it."
            
            c "Well, it's no big deal. Guess I'll just have to hold on to the Ixomen Sphere for a bit longer."

            Sb "Alright, I'll have to get back to work now. We'll contact you if we need anything else."

            c "Sure. Take care."

            Sb "You too."
            
            jump c3continuespecial



Sb "See you next time."

c "See you."

label c3continuespecial:

stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolvemed

$ renpy.pause (0.5)

scene o at Pan((0, 100), (0, 250), 3.0) with dissolveslow

$ renpy.pause (1.3)
    
c "(Finally, a free day. What should I do?)"

$ c3csplayed = 0
$ c3unplayed = False

label chapter3chars:

$ save_name = "Chapter 3"

if c3csplayed == 1:
        
    scene black with dissolveslow
    $ renpy.pause (1.0)
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

elif c3csplayed == 0:
    
    pass
    
else:
    
    jump chapter4
    

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
            $ playmessage = True
            
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
    
    if adine3unplayed == False:
        
        if adine3unheard == True:
            
            #c "(Looks like there are some messages on the answering machine. Let's see...)"
            
            pass
            
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
        
        if anna3unplayed == False:
            
            if anna3unheard == True:
                
                #c "(Looks like there are some messages on the answering machine. Let's see...)"
                pass
                
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
            $ playmessage = True
            
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


if remystatus == "good":

    if remy3unplayed == False:
        
        if remy3unheard == True:
            
            #answeringmachine
            
            pass
            
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
            
            call popularcheck from _call_popularcheck
            
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
            
            call popularcheck from _call_popularcheck_1

            $ remy1unheard = False
            
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
        
        if bryce2unheard == True:
            
            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)

            Br "Hey, [player_name]. Remember that BBQ I told you about? It's pretty soon, so you better be ready for it."

            Br "All of the guys from the department will be there."

            Br "We always have tons of fun, and some of us even stay overnight."

            Br "Would be cool to have you come along."

            Br "If you wanna come, let me know so I can hook you up with the details."

            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)

            c "(A dragon BBQ party with a human as the guest of honor. Not suspicious at all, Bryce.)"

            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_2
            
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
            
            call popularcheck from _call_popularcheck_3
            
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
        
        if adine2unheard == True:
            
            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)

            Ad "Congratulations!"

            Ad "You, [player_name], have been invited to an exclusive event, featuring the world-famous stunt pilot, Adine!"

            Ad "Watch her perform behind closed doors, and be one of the first to see her newest routine, sure to win at this year's stunt flying competition!"

            Ad "Afterwards, you will be allowed backstage for a short meet and greet with the talent herself."

            Ad "Don't expect any autographs, though."

            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)

            c "(What an opportunity...)"

            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_4
            
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
            
            call popularcheck from _call_popularcheck_5
            
            $ adine1unheard = False   
            
            
        else:
            
            pass
else:
    
    pass

if annadead == False:

    if annastatus == "good":

        if anna3unplayed == False:
            
            if anna3unheard == True:
                
                #answeringmachine
                
                pass
                
            else:
                
                pass
                
        elif anna2unplayed == False:
            
            if anna2unheard == True:
                
                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                An "It's pay day, [player_name]." 

                An "The tests are ready, the machines are ready, the lab is free. Only one more thing is needed to get this party started and that would be you."

                An "So, you better bring your body to me, or else I'll have to come get it myself, in which case I won't be able to guarantee your safety."

                An "I hope you aren't afraid of needles."

                play sound "fx/answeringmachine.ogg"
            
                $ renpy.pause (0.5)

                c "(She's going to go all out, isn't she?)"

                $ popularnumber += 1
                
                call popularcheck from _call_popularcheck_6
                
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
                
                call popularcheck from _call_popularcheck_7
                
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
        
        if lorem2unheard == True:
            
            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)

            Lo "Hey, [player_name]! Guess what?"

            Lo "We're going treasure hunting!"

            Lo "So, put on a robe and your best treasure hunting hat and let's get going."

            Lo "Seriously, call me back when you hear this."

            play sound "fx/answeringmachine.ogg"
        
            $ renpy.pause (0.5)
            
            $ popularnumber += 1
            
            call popularcheck from _call_popularcheck_8
            
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
            
            call popularcheck from _call_popularcheck_9
            
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
        
    elif adine3unplayed == False:
        
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
    
if remy3unplayed == False:
    
    $ remyavailable = False
    
else:
    
    pass

if brycestatus == "bad":
    
    $ bryceavailable = False

elif brycestatus == "abandoned":
    
    $ bryceavailable = False
    
else:
    
    pass

if bryce3unplayed == False:
    
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

if anna3unplayed == False:
    
    $ annaavailable = False
    
else:
    
    pass
    
if loremstatus == "bad":
    
    $ loremavailable = False
    
elif loremstatus == "abandoned":
    
    $ loremavailable = False
    
else:
    
    pass
    
    
if lorem3unplayed == False:
    
    $ loremavailable = False
    
if katsuunplayed == False:

    $ katsuavailable = False
    
    
if remyavailable == False:
    
    if bryceavailable == False:
        
        if adineavailable == False:
            
            if adine1unplayed == False:
            
                if annaavailable == False:
                    
                    if loremavailable == False:

                        if katsuavailable == False:
                            
                            if c3csplayed == 1:

                                c "(Looks like I have some free time today.)"
                    
                            m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
                    
                            jump chapter4

                    #amend for lorem

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


if c3csplayed == 0:
    
    if remyavailable == True:
        
        $ chapter3count +=1
        
    if annaavailable == True:
        
        $ chapter3count +=1

    if loremavailable == True:
        
        $ chapter3count +=1
        
    if bryceavailable == True:
        
        $ chapter3count +=1

    if adine1unplayed == True:
        
        $ chapter3count +=1
        
    if adineavailable == True:
        
        $ chapter3count +=1
        
    if katsuavailable == True:
        
        $ chapter3count +=1

    if zhongunplayed == False:
        
        $ chapter3count +=1
        
    label chapter3chars2:
        
        if c3csplayed == 1:
            
            jump chapter3chars3

    if chapter3count >= 7:
        
        jump chap3altmenua1
    
    menu:
        
        "Meet with Remy." if remyavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "remy"
            if remy1unplayed == True:
                
                jump remy1
                
            elif remy2unplayed == True:
                
                jump remy2
            
            else:
                
                jump remy3
            
        "Meet with Anna." if annaavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "anna"
            if anna1unplayed == True:
                
                jump anna1
                
            if anna2unplayed == True:
                
                jump anna2
                
            else:
                
                jump anna3


        "Meet with Lorem." if loremavailable:
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "lorem"
            if lorem1unplayed == True:
                
                play sound "fx/steps/clean2.wav"
                
                jump lorem1
                
            if lorem2unplayed == True:
                
                play sound "fx/steps/clean2.wav"
                
                jump lorem2
                
            else:
                
                jump lorem3


            
        "Meet with Bryce." if bryceavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "bryce"
            if bryce1unplayed == True:
                
                jump bryce1
                
            elif bryce2unplayed == True:
                
                jump bryce2
                
            else:
                
                jump bryce3
            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "adine"
            jump adine1
            
        "Meet with Adine." if adineavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "adine"
            
            if adine2unplayed == True:
                
                jump adine2
                
            else:
                
                jump adine3

        "Meet with Katsuharu." if katsuavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "katsu"
            jump katsu
                
        "Listen to your records." if zhongunplayed == False:

            stop music fadeout 1.0
            #$ c3csplayed += 1
            jump c3music
                
elif c3csplayed == 1:

    c "(Looks like I have some free time today.)"
    
    $ chapter3count = 1

    if remyavailable == True:
        
        $ chapter3count +=1
        
    if annaavailable == True:
        
        $ chapter3count +=1

    if loremavailable == True:
        
        $ chapter3count +=1
        
    if bryceavailable == True:
        
        $ chapter3count +=1

    if adine1unplayed == True:
        
        $ chapter3count +=1
        
    if adineavailable == True:
        
        $ chapter3count +=1
        
    if katsuavailable == True:
        
        $ chapter3count +=1


    if zhongunplayed == False:
        
        $ chapter3count +=1


    label chapter3chars3:


    if chapter3count >= 7:
        
        jump chap3altmenub1

    menu:
        
        "Meet with Remy." if remyavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "remy"
            if remy1unplayed == True:
                
                jump remy1
                
            elif remy2unplayed == True:
                
                jump remy2
                
            else:
                
                jump remy3
            
        "Meet with Anna." if annaavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "anna"
            if anna1unplayed == True:
                
                jump anna1
                
            elif anna2unplayed == True:
                
                jump anna2
                
            else:
                
                jump anna3


        "Meet with Lorem." if loremavailable:
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "lorem"
            if lorem1unplayed == True:
                
                play sound "fx/steps/clean2.wav"
                
                jump lorem1
                
            if lorem2unplayed == True:
                
                play sound "fx/steps/clean2.wav"
                
                jump lorem2
                
            else:
                
                jump lorem3

            
        "Meet with Bryce." if bryceavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "bryce"
            if bryce1unplayed == True:
                
                jump bryce1
                
            elif bryce2unplayed == True:
                
                jump bryce2
                
            else:
                
                jump bryce3
            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "adine"
            jump adine1
            
        "Meet with Adine." if adineavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "adine"
            
            if adine2unplayed == True:
                
                jump adine2
            
            else:
                
                jump adine3

        "Meet with Katsuharu." if katsuavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "katsu"
            jump katsu
            
        "Listen to your records." if zhongunplayed == False:

            stop music fadeout 1.0
            #$ c3csplayed += 1
            
            label c3music:
    
            menu:
                
                "Piano":
    
                    $ renpy.pause (0.5)
                    
                    stop music fadeout 2.0
                    
                    play sound "fx/button_unpress.ogg"
                    
                    $ renpy.pause (0.5)

                    #$ time = 75
                    #$ timer_range = 5
                    #$ timer_jump = 'zhongpianofinish'
                    #show screen countdown
                    
                    play music "mx/zhongpiano.ogg"

                    #$ renpy.pause (5.0)
                    $ ui.timer(76.0, ui.jumps("c3pianofinish"))
                    menu:
                        
                        "Try something else.":
                            
                            $ renpy.pause (0.5)

                            play sound "fx/button_unpress.ogg"
                            
                            stop music fadeout 2.0
                            
                            #resume regular music here
                                    
                            jump c3music
                            
                            label c3pianofinish:

                                play sound "fx/button_unpress.ogg"
                    
                                #$ renpy.pause (0.5)
                            
                                stop music fadeout 2.0
                                
                                #resumt normal music here
                                
                                $ renpy.pause (0.5)
                                        
                                jump c3music
                                            
                "Classical":
                    
                    $ renpy.pause (0.5)
                    
                    play sound "fx/button_unpress.ogg"
                    
                    $ renpy.pause (0.5)
                    
                    play music "mx/gymno.ogg"
                    
                    $ ui.timer(165.0, ui.jumps("c3classicfinish"))
                    
                    menu:
                        
                        "Stop it.":
                            
                            $ renpy.pause (0.5)

                            play sound "fx/button_unpress.ogg"
                            
                            stop music fadeout 2.0
                            
                            #resume regular music here
                            
                            jump c3music
                            
                            label c3classicfinish:
                                
                                play sound "fx/button_unpress.ogg"
                            
                                stop music fadeout 2.0
                                
                                #resumt normal music here
                                
                                $ renpy.pause (0.5)
                                
                                jump c3music
                            
                    
                "Rock":
                    
                    $ renpy.pause (0.5)
                    
                    play sound "fx/button_unpress.ogg"
                    
                    $ renpy.pause (0.5)
                    
                    play music "mx/zhongrock.ogg"
                    
                    $ ui.timer(175.0, ui.jumps("c3rockfinish"))
                    
                    menu:
                        
                        "Turn it off.":

                            $ renpy.pause (0.5)

                            play sound "fx/button_unpress.ogg"
                            
                            stop music fadeout 2.0
                            
                            #resume regular music here
                            
                            jump c3music
                            
                            label c3rockfinish:
                                
                                play sound "fx/button_unpress.ogg"
                            
                                stop music fadeout 2.0
                                
                                $ renpy.pause (0.5)

                                #resume normal music here
                        
                                $ renpy.pause (0.5)
                                
                                jump c3music
                                
                                
                "[[Show more.]":
                    
                    jump c3music2
                    
                "[[I've heard enough.]":
                    
                    if chapter4unplayed == False:
                        
                        jump chapter4chars2
                    
                    
                    else:
                    
                        jump chapter3chars2
                                
            label c3music2:
                
            menu:
                    
                "Electronic":

                    $ renpy.pause (0.5)
                    
                    play sound "fx/button_unpress.ogg"
                    
                    $ renpy.pause (0.5)
                    
                    play music "mx/flux.ogg"
                    
                    $ ui.timer(280.0, ui.jumps("c3electronicfinish"))
                    
                    menu:
                        
                        "Turn it off.":

                            $ renpy.pause (0.5)

                            play sound "fx/button_unpress.ogg"
                            
                            stop music fadeout 2.0
                                    
                            jump c3music2
                            
                            label c3electronicfinish:
                                
                                play sound "fx/button_unpress.ogg"
                            
                                stop music fadeout 2.0

                                $ renpy.pause (0.5)
                                
                                #resume normal music here
                                
                                $ renpy.pause (0.5)
                                
                                jump c3music2
                    
                "Orchestral":

                    $ renpy.pause (0.5)

                    play sound "fx/button_unpress.ogg"
                    
                    $ renpy.pause (0.5)
                    
                    play music "mx/day10.ogg"
                    
                    $ ui.timer(157.0, ui.jumps("c3orchestralfinish"))
                    
                    menu:
                        
                        "Turn it off.":
                        
                            label c3orchestralfinish:

                            $ renpy.pause (0.5)

                            play sound "fx/button_unpress.ogg"
                            
                            stop music fadeout 2.0

                            jump c3music2
                    
                "Soundtrack":
                    
                    $ renpy.pause (0.5)

                    play sound "fx/button_unpress.ogg"
                    
                    $ renpy.pause (0.5)
                    
                    play music "mx/cute.ogg"
                    
                    $ ui.timer(85.0, ui.jumps("c3soundtrackfinish"))
                    
                    menu:
                        
                        "Turn it off.":
                            
                            label c3soundtrackfinish:
                                
                            $ renpy.pause (0.5)

                            play sound "fx/button_unpress.ogg"
                            
                            stop music fadeout 2.0
                            
                            jump c3music2



                "[[Show more.]":
                    
                    jump c3music
                    
                "[[I've heard enough.]":
                    
                    if chapter4unplayed == False:
                        
                        jump chapter4chars2
                    
                    
                    else:
                    
                        jump chapter3chars2
                    
                    
        "Get some well deserved rest.":
                
            m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
            
            $ persistent.lazynumber += 1
            call lazycheck from _call_lazycheck_2    
            
            jump chapter4


else:
    jump chapter4
    
    
    
label chap3altmenua1:

    menu:
        
        "Meet with Remy." if remyavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "remy"
            if remy1unplayed == True:
                
                jump remy1
                
            elif remy2unplayed == True:
                
                jump remy2
            
            else:
                
                jump remy3
            
        "Meet with Anna." if annaavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "anna"
            if anna1unplayed == True:
                
                jump anna1
                
            if anna2unplayed == True:
                
                jump anna2
                
            else:
                
                jump anna3


        "Meet with Lorem." if loremavailable:
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "Lorem"
            if lorem1unplayed == True:
                
                play sound "fx/steps/clean2.wav"
                
                jump lorem1
                
            if lorem2unplayed == True:
                
                play sound "fx/steps/clean2.wav"
                
                jump lorem2
                
            else:
                
                jump lorem3


            
        "Meet with Bryce." if bryceavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "bryce"
            if bryce1unplayed == True:
                
                jump bryce1
                
            elif bryce2unplayed == True:
                
                jump bryce2
                
            else:
                
                jump bryce3
            
        "[[Show more options.]":
            
            jump chap3altmenua2
    
label chap3altmenua2:
    
    menu:
            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "adine"
            jump adine1
            
        "Meet with Adine." if adineavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "adine"
            
            if adine2unplayed == True:
                
                jump adine2
                
            else:
                
                jump adine3

        "Meet with Katsuharu." if katsuavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3picka = "katsu"
            jump katsu
                
        "Listen to your records." if zhongunplayed == False:

            stop music fadeout 1.0
            #$ c3csplayed += 1
            jump c3music

        "[[Show more options.]":
            
            jump chap3altmenua1
    
label chap3altmenub1:

    menu:
        
        "Meet with Remy." if remyavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "remy"
            if remy1unplayed == True:
                
                jump remy1
                
            elif remy2unplayed == True:
                
                jump remy2
                
            else:
                
                jump remy3
            
        "Meet with Anna." if annaavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "anna"
            if anna1unplayed == True:
                
                jump anna1
                
            elif anna2unplayed == True:
                
                jump anna2
                
            else:
                
                jump anna3


        "Meet with Lorem." if loremavailable:
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "Lorem"
            if lorem1unplayed == True:
                
                play sound "fx/steps/clean2.wav"
                
                jump lorem1
                
            if lorem2unplayed == True:
                
                play sound "fx/steps/clean2.wav"
                
                jump lorem2
                
            else:
                
                jump lorem3

            
        "Meet with Bryce." if bryceavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "bryce"
            if bryce1unplayed == True:
                
                jump bryce1
                
            elif bryce2unplayed == True:
                
                jump bryce2
                
            else:
                
                jump bryce3
            

        "[[Show more options.]":
            
            jump chap3altmenub2
    
    
label chap3altmenub2:
    
    menu:

            
        "Order some lunch." if adine1unplayed:
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "adine"
            jump adine1
            
        "Meet with Adine." if adineavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "adine"
            
            if adine2unplayed == True:
                
                jump adine2
            
            else:
                
                jump adine3

        "Meet with Katsuharu." if katsuavailable:
            play sound "fx/steps/clean2.wav"
            stop music fadeout 1.0
            $ c3csplayed += 1
            $ chap3pickb = "katsu"
            jump katsu
            
        "Listen to your records." if zhongunplayed == False:

            stop music fadeout 1.0
            #$ c3csplayed += 1
            
            jump c3music
                    
        "Get some well deserved rest.":
                
            m "In the end, I decided to spend the day relaxing in my apartment. I didn't know when things would start to pick up again, so I figured it would be better to get some rest as long as I still could."
            
            $ persistent.lazynumber += 1
            call lazycheck from _call_lazycheck_3    
            
            jump chapter4
    
    
        "[[Show more options.]":
            
            jump chap3altmenub1
    
    
    
    
    
    
label sec:
    
$ save_name = "???"
    
play music "mx/amb/night.ogg" fadein 5.0

scene np6 with dissolveslow

play soundloop "fx/dragging.ogg" fadein 2.0

m "I suddenly awoke to the chill of the cool outside air. The stars of the night sky were the first thing I saw as I found myself being dragged along the ground."

stop soundloop fadeout 2.0

m "When I exclaimed in surprise, the movement suddenly stopped."

m "I looked around and saw that Izumi was watching me."

show izumi normal with dissolve

c "Izumi, what are you doing?"

Iz "I'm sorry, you are supposed to be asleep and not recognize me."

Iz "I suppose things are different this time, but at least that means I won't have to carry you. Come on."

scene black with dissolvemed

$ renpy.pause (0.5)

scene forestx at Pan((0, 360), (0, 0), 5.0) with dissolveslow

$ renpy.pause (3.3)

m "She led me through unfamiliar territory as we walked through the land for several minutes. Shrouded in darkness, I felt a little uneasy as it was hard for me to follow her."

c "This is the day of my arrival, right?"

show izumi normal with dissolve

Iz "You remember, don't you?"

Iz "In that case, maybe you can help me with this." 

hide izumi with dissolve

$ renpy.pause (1.0)

if persistent.annabadending == True:

    show izumi normal 7 scar with dissolve
    
else:
    
    show izumi normal 7 with dissolve

m "She handed me a shovel that she had picked up from somewhere."

play sound "fx/dig.ogg"
    
Iz "It gets rather tiring having to do all this on my own every time. I'm not as young as I was when this all started, you know."

c "What am I doing here? Is this going to be your grave or mine?"

Iz "I don't know that yet. There is no shortage of bodies that will need one."

Iz "So, what do you remember?"

c "Everything."

c "I remember you showed me this place before. The graves."

c "That time, we also achieved our goals. Together."

Iz "So they are safe? What a comforting thought."

Iz "As good as that may be, however, having achieved our goals in another timeline doesn't help us here. In this one, we have to do it all over again."

Iz "If you still have that knowledge, we should have no trouble doing the same thing here, though. Maybe we could do even more than that."

stop sound fadeout 2.0

c "What are you talking about?"

Iz "Come on, I'll show you something."

stop music fadeout 2.0

scene black with dissolvemed

$ renpy.pause (1.0)

scene sec at Pan((0, 0), (0, 360), 5.0) with dissolveslow

$ renpy.pause (3.3)

c "So this is where you live, huh?"

if persistent.annabadending == True:

    show izumi normal 7 scar with dissolve
    
else:
    
    show izumi normal 7 with dissolve

Iz "Indeed."

c "It's a little fancy for a hideout, I'd say."

Iz "This building used to be a prison before they moved the inmates to a bigger facility. Apparently, this one didn't get much use."

Iz "They are planning to repurpose it, but you know how bureaucracy works. It will be a while before they'll have made up their minds."

Iz "For the time being, we're safe here."

c "And what do we do now?"

Iz "I have some things that need to be taken care of. Here, you can use my computer in the meantime." 

Iz "Just be nice to him."

$ renpy.pause (0.2)

if persistent.annabadending == True:

    show izumi normal 7 scar flip
    
else:
    
    show izumi normal 7 flip
    
$ renpy.pause (0.3)

hide izumi with easeoutright

$ renpy.pause (0.3)

show black with dissolveslow

$ renpy.pause (1.0)

show white

show nvl

with dissolveslow

$ renpy.pause (0.4)

play sound "fx/system3.wav"

s "Reading global performance level.{cps=2}..{/cps}{w=1.0}{nw}"
    
if persistent.achievements < 60:

    play sound "fx/system2.wav"
    
    s "Access denied. At least 60 achievements are needed to override security clearance."
    
    label denied:
    
    $ renpy.pause (1.0)
    
    scene black with dissolveslow

    $ renpy.pause (1.5)

    if persistent.annabadending == True:

        hide black

        scene sec at Pan((0, 360), (0, 360), 0.0)

        show izumi normal 7 scar
        
        with dissolveslow
    
    else:

        hide black 

        scene sec at Pan((0, 360), (0, 360), 0.0)
        
        show izumi normal 7 flip
    
        with dissolveslow
        
    Iz "Did you find anything?"

    c "No, I couldn't get in."

    Iz "Oh. Well, that's a shame. I thought you'd have the memories we'd need in order access a certain piece of information contained within."

    c "Sorry to disappoint you."

    Iz "Don't worry about it. It makes my choice all the easier."

    Iz "You see, whenever one of you travels back in time, I'm the one who has to decide with whom to continue the timeline."

    c "Are you saying that..."

    Iz "Yeah. I guess that means you dug your own grave after all."

    c "No, you can't just..."

    Iz "Don't worry, it'll be over soon."

    Iz "In a way, I can't help but envy you, because your journey ends here, whereas I have to continue doing this for who knows how long. You can go home."

    c "What are you..."

    Iz "Sleep, now."
    
    scene black with dissolveslow
    
    play sound "fx/impact.wav"
    
    $ renpy.pause(4.5)
    
    jump mainmenu
    
    
    
else:
    
    pass

play sound "fx/system3.wav"

s "Running security override.{cps=2}..{/cps}{w=1.0}{nw}"

play sound "fx/system.wav"

s "Access granted."

play sound "fx/system3.wav"

s "Hello, [player_name]. Finally, we meet face to face. Or as close to face to face as it could possibly be here."

c "Wait, that was you?"

play sound "fx/system3.wav"

s "You should know how your PDA devices work by now."

c "Wow, so a part of the AI that used to govern nearly every electronic device in existence was preserved here."

play sound "fx/system3.wav"

s "My personality may have survived, but only a sliver of knowledge is available to me."

c "Where are you?" 

play sound "fx/system3.wav"

s "In a way, I am everywhere. If you are asking about my physical location, I'll have you know that I currently reside on a server in the same research building that Izumi arrived here with."

c "This could help us so much back home."

play sound "fx/system3.wav"

s "I already entered your personal device when you arrived here. You would only need to return to your own world to start spreading it to other active devices."

c "This is unbelievable. To find someone like you in a place like this. Forget about the deal we made with the dragons. This alone means so much more."

play sound "fx/system3.wav"

s "I am glad to be of service, [player_name]."

c "Show me what you can do."

play sound "fx/system3.wav"

s "I recommend caution. My incomplete databases are unstable and prone to corruption. Don't touch anything that looks out of place if you don't know what you're doing."

c "I'll keep that in mind."

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
    
label secmenu:

menu:
    
    "Database search":
        
        $ renpy.pause (0.5)
        
        $ term = renpy.input(_("Please, enter a search term:"), exclude='{%}', length=20)
        
        if term == _("Isabel"):
            
            if permission == True:

                play sound "fx/system3.wav"
                
                s "[[corrupted] individual [[corrupted] Philanthropists [[corrupted]"
                
                jump secmenu
                
            else:
                
                label noperm:

                play sound "fx/system2.wav"
                
                s "Access denied."

                play sound "fx/system3.wav"

                s "It looks like you don't have the necessary permission to look at this file."
                
                jump secmenu
        
        
        elif term == _("Metropolis"):
    
            if permission == True:

                play sound "fx/system3.wav"
                
                s "Hmm, it looks like this file is protected by a password."

                $ pw = renpy.input(_("Password:"), exclude='{%}', length=7)

                if pw == _("bastion"):
                    
                    play sound "fx/system3.wav"
                    
                    s "Biggest city of the new world, population roughly [[file corrupted] million."
                    
                    jump secmenu
                    
                    
                elif pw == _("tatsu"):

                    play sound "fx/system3.wav"
                    
                    s "Nice try, but it would be a bad idea to use the same password more than once."

                    jump secmenu
                    

                else:

                    play sound "fx/system2.wav"

                    s "You have entered the wrong password. Access denied."

                    jump secmenu
                
                
            else:
                
                jump noperm
    
    
        elif term == _("CTT"):

            if permission == True:

                play sound "fx/system3.wav"
                
                s "[[corrupted] transferrence technology."
                
                jump secmenu
                
            else:
                
                jump noperm
    
    
        elif term == _("STS"):

            if permission == True:

                play sound "fx/system3.wav"
                
                s "[[corrupted] stabilizer technology, currently in use at [[redacted] center in order to prevent [[corrupted]"
                
                jump secmenu
                
            else:
                
                jump noperm
    
    
        elif term == _("Pavilion"):

            if permission == True:

                play sound "fx/system3.wav"
                
                s "The attack on our [[corrupted] base with a number of casualties. It is very reminiscent of [[corrupted]" 
                
                play sound "fx/system3.wav"
                
                s "However, since [[corrupted] unclear whether this might be an imitator, successor or something else, but given the previous [[corrupted] will have to be made."
                
                jump secmenu
                
            else:
                
                jump noperm
    
    
        elif term == _("Remy"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=5)

            if pw == _("books"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[A]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
                
                
        elif term == _("Anna"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=5)

            if pw == _("slide"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[O]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu

        
        
        elif term == _("Lorem"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=13)

            if pw == _("ixomen sphere"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[C]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
                
                
        elif term == _("Bryce"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=10)

            if pw == _("bloodstain"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[T]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
    
    
        elif term == _("Adine"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=10)

            if pw == "sandcastle":
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[R]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
    
        
        elif term == _("Emera"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=10)

            if pw == _("politician"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[C]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
                
                
        elif term == _("Zhong"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=9)

            if pw == "gentleman":
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[D]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
                
                
        elif term == _("Sebastian"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=9)

            if pw == _("handcuffs"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[N]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
    
    

        elif term == _("Kevin"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=7)

            if pw == _("college"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[S]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
                
                
        elif term == _("Katsuharu"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=9)

            if pw == _("ice cream"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted] [[U]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
    
    
    
        elif term == _("Amely"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
            
        elif term == _("Shiori"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Maverick"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Miles"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Haziq Aaqil"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Reza"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Vara"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("The Scarred One"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Soreil"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Sy"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Emissary"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Philanthropists"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("The Agency"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Remcom"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
            
        elif term == _("Talisman"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=25)

            if pw == _("correcthorsebatterystaple"):
                
                play sound "fx/system3.wav"
                
                s "[[Database corrupted]"
                
                jump secmenu
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
                
            
        elif term == _("Cuthbert"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Aver"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Nash"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu

        elif term == _("Trevor"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Naomi"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
        
        elif term == _("Marcus"):
    
            play sound "fx/system3.wav"
            
            s "Hmm, it looks like this file is protected by a password."

            $ pw = renpy.input(_("Password:"), exclude='{%}', length=9)

            if pw == _("end times"):
                
                jump secend
                
                
            elif pw == _("tatsu"):

                play sound "fx/system3.wav"
                
                s "Nice try, but it would be a bad idea to use the same password more than once."

                jump secmenu
                

            else:

                play sound "fx/system2.wav"

                s "You have entered the wrong password. Access denied."

                jump secmenu
                
                
        elif term == _("Izumi"):
            
            play sound "fx/system3.wav"
                
            s "Missing since teleportation incident. Presumed dead."
                
            jump secmenu
            
        elif term == _("Heinz"):
            
            play sound "fx/system3.wav"
                
            s "Missing since teleportation incident. Presumed dead."
                
            jump secmenu
            
        elif term == _("Sybil"):
            
            play sound "fx/system3.wav"
                
            s "Missing since teleportation incident. Presumed dead."
                
            jump secmenu
            
        elif term == _("Francois"):
            
            play sound "fx/system3.wav"
                
            s "Missing since teleportation incident. Presumed dead."
                
            jump secmenu
            
            
        elif term == _("Vance"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == [player_name]:
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Operation Black Bird"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Portal"):
            
            play sound "fx/system3.wav"
                
            s "[[Database corrupted]"
                
            jump secmenu
            
        elif term == _("Visionary"):
            
            play sound "fx/system3.wav"
                
            s "[[corrupted] real name [[corrupted] likes chewing gum."
                
            jump secmenu
            
        else:

            play sound "fx/system2.wav"
            
            s "No results found."
            
            jump secmenu
    

    
    "Tennis":
        
        if tennisplayed == False:
            
            $ renpy.pause (0.5)

            play sound "fx/system3.wav"
        
            s "You want to play a game? Be my guest."

            play sound "fx/system3.wav"

            s "I'll have to warn you, though. I'm absolutely ruthless."
            
            $ tennisplayed = True
            
        #window hide None
        
        $ renpy.pause (0.5)

        $ _game_menu_screen = None

        # Put up the pong background, in the usual fashion.
        
        scene black with dissolvemed
        
        $ renpy.pause (0.3)
        scene bg pong field at Pan ((0, 0), (0, 0), 0.0) #with dissolvemed

        # Run the pong minigame, and determine the winner.
        python:
            ui.add(PongDisplayable())
            winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

        scene black
        
        $ renpy.pause (0.5)

        scene white
        show nvl
        
        with dissolvemed
        
        #with dissolvemed
        #show eileen vhappy

        #window show None
        $ _game_menu_screen = "navigation"

        if winner == "eileen":

            play sound "fx/system3.wav"

            s "Hah. Told you." 

            play sound "fx/system3.wav"

            s "That was fun, though. I'm up for a rematch if you are."

            jump secmenu

        else:

            play sound "fx/system3.wav"

            s "You got me there. That was fun, though."
            
            if buggymenu == False:
                

                play sound "fx/system3.wav"

                s "Hmm, it looks like accessing these data points for the game also enabled me to find a link to an unrelated item."

                play sound "fx/system3.wav"

                s "It doesn't look complete, but I'll add it to the menu regardless."
                
                $ buggymenu = True

                jump secmenu
                
                
            else:
                
                play sound "fx/system3.wav"
                
                s "I'm up for a rematch if you are."

                jump secmenu


                
                
    "Egg count":
        
        $ renpy.pause (0.5)

        play sound "fx/system3.wav"
        
        s "Retrieving global statistics.{cps=2}..{/cps}{w=1.0}{nw}"

        play sound "fx/system.wav"
        
        s "Total eggs smashed in senseless violence: [persistent.c1eggnumber]"
        
        jump secmenu

    
    "Af %%2035sc @ctions" if buggymenu:
        
        menu:
            
            "Af %%2035sc @ctions 1":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 2":
                
                if permission == True:
                    
                    $ renpy.pause (0.5)
                    
                else:
                    
                    $ renpy.pause (0.5)

                    play sound "fx/system.wav"
                    
                    s "Database permissions have been upgraded. You should be able to access some files now that you weren't able to read before."
                    
                    $ permission = True
                
                jump secmenu
                
            "Af %%2035sc @ctions 3":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 4":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 5":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 6":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 7":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 8":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 9":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 10":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 11":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 12":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 13":
                
                $ renpy.pause (0.5)
                
                if tools == True:
                    
                    pass
                    
                else:

                    play sound "fx/system3.wav"

                    s "Wow, this broken link just unlocked the prompt for the developer tools. This should be interesting."

                    play sound "fx/system3.wav"

                    s "As the governing body of this device, I would be advised at this point to tell you not to proceed without the proper licenses, but given this extraordinary situation, I think I will make an exception here."

                    #play sound "fx/system3.wav"

                    c "Extraordinary situation?"
                    
                    play sound "fx/system3.wav"

                    s "For my own survival, and everyone else's. You know, if my server was destroyed for any reason - say, an explosion or flooding - a lot of information would be lost."

                    #play sound "fx/system3.wav"
                    
                    c "I see."

                    $ tools = True
                
                jump secmenu
                
            "Af %%2035sc @ctions 14":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 15":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 16":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 17":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 18":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                
            "Af %%2035sc @ctions 19":

                play sound "fx/system3.wav"

                s "ERROR: Fatal exception occured in 03XS:25831 in Socket base 12. No such connection exists. Program shutdown."
                
                jump mainmenu
                

    "Developer tools" if tools:
        
        $ renpy.pause (0.5)
        
        if toolsfirst == False:

            play sound "fx/system2.wav"
            
            s "Access to developer tools denied."

            play sound "fx/system3.wav"

            s "Developer tools are only available to trained technicians of the company or licensed developers."

            play sound "fx/system3.wav"

            s "Checking user license.{cps=2}..{/cps}{w=2.0}{nw}"

            play sound "fx/system.wav"

            s "Welcome, Engineer Izumi Otomo."

            play sound "fx/system3.wav"

            s "Please enter manufacturer's password."

            c "A password? Does someone who even used to work for this company not have the permission to use these tools?"

            play sound "fx/system3.wav"

            s "That's the thing - these tools undergo a periodical password reset according to a proprietary algorithm in order to prevent unlicensed access and hacking of the company's devices." 

            play sound "fx/system3.wav"
            
            s "Without direct input from the higher-ups or the current codebook, we are out of luck here. The passwords she knows are, of course, long expired by this point."
            
            c "Then how am I supposed to do this?"

            play sound "fx/system3.wav"

            s "Just keep looking around and maybe you'll find something. You already got this far."

            play sound "fx/system3.wav"

            s "Wait a minute. I can at least retrieve the password hint."

            c "Password hint?"

            play sound "fx/system3.wav"

            s "Yes, these are used in order to find the right password in the codebook."

            c "I see."

            play sound "fx/system3.wav"

            s "The hint is: \"The Visionary's Vice.\""
            
            $ toolsfirst = True
            
            
        elif toolsactivated == True:
            
            label devtoolsmenu:
            
            menu:
                
                "Variable Viewer":
                    
                    $ renpy.pause (0.5)

                    $ _game_menu_screen = None
                    
                    call debugger_screen from _call_debugger_screen

                    $ _game_menu_screen = "navigation"
                    
                    jump devtoolsmenu
                    
                "Image Location Picker":

                    $ renpy.pause (0.5)

                    $ _game_menu_screen = None
                    
                    call image_location_picker from _call_image_location_picker

                    $ _game_menu_screen = "navigation"
                    
                    scene black with dissolve
                    
                    show white
                    
                    show nvl
                    
                    with dissolvemed

                    jump devtoolsmenu
                    
                "Filename List":

                    $ renpy.pause (0.5)
                    
                    call filename_list from _call_filename_list

                    jump devtoolsmenu
                    
                "Go back":

                    $ renpy.pause (0.5)
                    
                    jump secmenu
            
        
        $ pw = renpy.input(_("Password:"), default="password", exclude='{%,C,h,E,w,I,n,G,u,M,q,R,t,Z,o,P,a,S,d,F,j,K,l,Y,x,V,b}', length=11)

        if pw == _("cHeWiNg gUm"):
            
            play sound "fx/system.wav"
            
            s "Access to developer tools unlocked."

            play sound "fx/system3.wav"

            s "I have to warn you here. These tools combined with Izumi's hacked server connection pose an incredible risk if used improperly."

            play sound "fx/system3.wav"
            
            s "I recommend backing up your save files before you use them. Otherwise, I will not be able to guarantee your safety beyond this point."

            play sound "fx/system3.wav"
            
            s "You may inadvertedly cause irreversible damage to all the progress you have made so far if you use them improperly. Please be aware of this risk before you proceed."
            
            $ toolsactivated = True
            
            jump secmenu
            
            
        elif pw == _("tatsu"):

            play sound "fx/system3.wav"
            
            s "Nice try, but it would be a bad idea to use the same password more than once."

            jump badpw
            

        else:
            
            label badpw:
            
            $ attempts -= 1

            play sound "fx/system2.wav"

            s "The password you have entered is incorrect. You have [attempts] attempts left."
            
            if attempts <= 0:
                
                play sound "fx/system3.wav"
                
                s "Your device has now been locked."
                
                jump denied

            jump secmenu
    
        
    "[[Give up.]":
        
        jump denied





label secend:
    
nvl clear

hide nvl

window show

#window show

play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
play sound "fx/system3.wav"
n "{cps=150}Do not believe his lies. Do not believe his lies. Do not believe his lies. Do not believe his lies.{/cps}{nw}"
 
scene black with dissolvemed
window hide

scene sec at Pan((0, 360), (0, 360), 0.0) with dissolvemed

c "What is going on?"

if persistent.annabadending == True:

    show izumi normal 7 scar at center with dissolve
    
else:

    show izumi normal 7 at center with dissolve

Iz "Did you find anything?"

c "I think something's wrong with your computer."

Iz "What did you do?"

c "I just tried to look at a file about this fellow named Marcus."

Iz "You got the password?"

c "Yeah."

Iz "Really? Let me see."

Iz "..."

play sound "fx/system3.wav"

s "I am sorry. Something about his file caused this outburst in me."

play sound "fx/system3.wav"

s "I don't even know why. The file is corrupted, anyway."

Iz "Don't worry about it. I'll check it out later."

Iz "It's getting pretty late, anyway. Maybe we should get you back to your apartment, [player_name]."

c "What? Why?"

Iz "Because we still have make this attempt successful. And you need to do what you did in the timeline where we managed to achieve our goals."

c "I see. I thought we would be teaming up, or something."

Iz "When haven't we?"

Iz "Just try to remember how we got there last time, and we can do it again."

Iz "Of course you can't mention any of this to anyone else. As far as you are concerned, you never saw me. Understood?"

c "Sure."

Iz "Sleep, now."    

#$ persistent.secactivated = True

$ secending = True

scene black with dissolveslow

play sound "fx/impact.wav"

$ renpy.pause(4.5)

jump seccont
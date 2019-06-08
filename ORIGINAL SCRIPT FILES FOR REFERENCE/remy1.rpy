#+17 -16

label remyhints:
    nvl clear
    window show

    n "Hints:"
    n "{i}The Third War{/i} is directly preceded by {i}The Spark{/i}."
    n "{i}The First War{/i} is directly preceded by {i}The Inception{/i}."
    n "{i}The Invention{/i} is not the third, seventh, or last book."
    n "{i}The Second War{/i} is the 4th book."
    n "There is only one book before {i}The First War{/i}."
    n "{i}The Enlightenment{/i} comes at some point after {i}The Third War{/i}."
    window hide
    return

label remy1:

$ chapter1csplayed += 1
$ remy1unplayed = False
$ remy1played = True
$ persistent.remy1played = True

if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Remy 1"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Remy 1"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Remy 1"
    
else:

    $ save_name = "Chapter 1 - Remy 1"

scene black with fade
$ renpy.pause (1.0)
scene library at Pan ((640, 228), (0,228), 10.0) with dissolveslow

c "(He told me to meet him in the lobby, but nobody's here. Maybe I should look for him. He can't be too far, after all.)"

#insert skip here
if persistent.remy1skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_84

    call skiptut from _call_skiptut_22
        
    if skipbeginning == False:

        if system == "normal":
        
            s "My records indicate you have already experienced this scene in a satisfactory manner. Would you like to skip to the end?"
        
            #play sound "fx/system3.wav"
        
            #s "Warning: In this scene, skipping ahead this way instead of using the skip buttons (CTRL and TAB) may prevent you from experiencing alternative choices and outcomes that you haven't seen before. These may only be minor, though."
        
        elif system == "advanced":

            s "It looks like you've seen this before. Skip to the end of this scene?"
        
            #play sound "fx/system3.wav"
        
            #s "I have to warn you, though. If you do this here instead of just using CTRL and TAB, you may end up missing some minor changes you haven't seen before."
            
        else:
            
            s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the end of this scene."
            
            #play sound "fx/system3.wav"
            
            #s "If you want to do things this way instead of just using the skip buttons like a civilized person, you could end up missing some choices you haven't made before. But considering how far you've come, you probably won't miss much."
            
        
    $ skipbeginning = False
    
    menu:
        
        "Yes. I want to skip ahead.":
            
            play sound "fx/system3.wav"
            
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            
            scene black with dissolvemed
            $ renpy.pause (1.0)
            
            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_22
            
            scene office2 at Pan ((128, 228), (128,228), 0.0)

            show remy normal
            with dissolvemed
            
            play music "mx/fireplace.ogg" fadein 1.0
            
            jump remy1skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            #play music "mx/shoal.ogg" fadein 2.0

play music "mx/choices.ogg"
m "It was quite a spacious building, lined with many bookcases on multiple floors. From the looks of it, it seemed to be as much of an archive as it was a library, with immaculate order permeating the chamber. It was the kind of place I could see myself getting lost in for an afternoon or two, thumbing through all the interesting books it could offer me."
m "I was looking around in wonder, when suddenly, a voice penetrated the silence."

if emeramet == False:

    "???" "REMY!" with vpunch
    
else:
    
    Em "REMY!" with vpunch
    
m "I couldn't see who the voice belonged to, but it came from the more private area in the back. It was followed by footsteps that approached it."
Ry "Oh, you're still here?"

if emeramet == False:

    "???" "Of course I am still here. I have business to attend to."
    
else:
    
    Em "Of course I am still here. I have business to attend to."

Ry "Certainly. I just assumed you'd be done by now, Emera."
Em "Guess your assumption was wrong, then. Be a good boy and bring me some coffee, will you?"
Ry "Of course, Emera."
m "I heard more movement, though I still could not see either of the two who spoke behind all the bookcases. I assumed the area was off-limits to a visitor like myself and decided to wait."
Ry "Here you go."
Em "Now let me read in peace, you silly boy."
Ry "Of course."
m "I heard him walk towards my direction, until he emerged from behind a bookcase and spotted me."

show remy normal with dissolve

Ry "Oh, hello [player_name]. I didn't expect you so soon."
$ remymood = 0
menu:
    "Not like I had anything better to do.":
        pass
        
    "Better be safe than sorry.":
        $ remymood += 1
        
    "Yeah, I probably shouldn't have come at all.":
        $ remymood -= 1

$ renpy.pause (0.5)
show remy smile with dissolve

Ry "Well, I'm glad to see you again, at any rate."


if chapter3unplayed == False:
    
    c "Was that Emera?"
    
    show remy shy with dissolve
    
    Ry "Y-Yes..."
    
    c "Oh..."
    
    Ry "..."
    
else:
    
    c "Who was that back there?"
    
    show remy look with dissolve

    Ry "I guess you heard that, didn't you? That was my superior. She's the Minister of Culture & Arts, which means I'm technically in her employment, though generally speaking I work for the council at large, not just her."

c "So this is where you work, huh?" 

show remy normal with dissolve

Ry "Most of the time, yes."
c "That makes you a librarian, I suppose."
Ry "There's a little more to it. I'm not just in charge of the books, I'm a scholar and study them, too."
Ry "For example, if the council requests knowledge on certain topics, like facts, statistics or other information of interest, it is part of my job to research it and present it to them in an appropriate manner."

menu:
    "So, basically you're an expert on everything?":
        Ry "No, just an expert at finding information."
        
    "That sounds like the kind of thing I'd like to do.":
        $ remymood += 1
        $ renpy.pause (0.5)
        show remy smile with dissolve
        Ry "Guess you came to the right place, then."
        show remy normal with dissolve

    "Just thinking about doing that kind of work day after day gives me a headache.":
        $ remymood -= 1
        $ renpy.pause (0.5)
        show remy look with dissolve
        Ry "I suppose it's a good thing that I am the one who works here and not you."
        show remy normal with dissolve
        
Ry "Anyways, was there a particular reason why you wanted to meet me?"

menu:
    "You're just too damn cute, that's why.":
        $ remymood -= 1
        $ renpy.pause (0.5)
        show remy shy with dissolve
        Ry "D-Don't say that."
        show remy normal with dissolve

    "I was interested in what you said the other day. You have myths about humans?":
        $ remymood += 1
        $ renpy.pause (0.5)
        show remy smile with dissolve
        Ry "Oh, right! I still have work to do, but I could show you something afterwards." 
        show remy normal with dissolve

    "I was bored and coming here seemed to be the most interesting option.":
        Ry "I'll just take that as a compliment."

Ry "Either way, now that you're here, you could help me with something. I've got some books that need to be sorted over there."

menu:
    "I respectfully decline your request for help.":
        Ry "Are you sure? This could take a while and I don't want to keep you waiting."
        menu:
            "I have reconsidered my stance on this matter and have decided to help you.":
                Ry "Very well."
                
            "I'm sure.":
                Ry "In that case, you should  probably wait outside. I don't think the staff would approve of you loitering in the lobby."
                c "I will."
                stop music fadeout 1.0
                play sound "fx/steps/clean2.wav"
                scene black with fade
                $ renpy.pause (0.5)
                nvl clear
                window show
                n "I waited outside for the dragon to finish his work and passed the time by reading a book I had brought from my apartment." 
                n "When I finished the book and the dragon still hadn't appeared, I grew impatient and tried to return inside to check up on him, only to find the door to the library had been locked."
                n "When I looked up, I realized all the lights inside had been turned off as well and the library no doubt had closed for the day."
                n "I was not sure whether he left me waiting on purpose, or had just forgotten about me while he finished his work." 
                n "Either way, it seemed like a sign that we wouldn't meet again."
                window hide
                nvl clear

                $ remystatus = "bad"

                $ remyscenesfinished = 1

                if chapter4unplayed == False:
                    
                    jump chapter4chars
                    
                elif chapter3unplayed == False:
                    
                    jump chapter3chars
                    
                elif chapter2unplayed == False:
                    
                    jump chapter2chars
                    
                else:

                    jump chapter1chars
                
                
    "Sure, not like I have anything better to do.":
        pass
        
    "Alright. How do I fit them in, alphabetically?":
        $ remymood += 1
        Ry "Oh, no. The arrangement you see in this library is based on a sophisticated system that sorts everything in a very intuitive manner based on a number of criteria: genre, author, complexity and age."
        Ry "As you can probably tell, we have a lot of specimens, so just sorting them by alphabet would be far from suf- and ef-ficient."
        menu:
            "That does sound very intuitive.":
                $ remymood += 1
                $ renpy.pause (0.5)
                show remy smile with dissolve
                Ry "It is."
                show remy normal with dissolve
                
            "That sounds complicated.":
                Ry "It's not that hard. I'll show you."
                
            "That sounds really boring.":
                $ remymood -= 1
                $ renpy.pause (0.5)
                show remy look with dissolve
                Ry "Well, if you say so..."
                show remy normal with dissolve
                
Ry "Basically, these eight books you see over there were all part of a section that was moved, so they have to be sorted into their new area."
Ry "The problem is their labels are so old that they've started to fade away, which makes sorting them a little harder. They will get new labels soon, but until then, we'll just have to make do with what we have here."
Ry "All of them are by Haziq Aakil, a writer on the subject of history - and a very prolific one, I might add. You will find the shelf they belong to over there. Now it is just a matter of placing them in the right order, from oldest to newest."
Ry "I have written down everything still legible from the old labels here. For someone like you, putting them in order shouldn't be a problem."
Ry "In any case, I'll be working on something else in the meantime, so let me know once you're done."

show remy normal flip
$ renpy.pause (0.3)
hide remy with easeoutright

label reset:
    pass

nvl clear
window show

n "Hints:"
n "{i}The Third War{/i} is directly preceded by {i}The Spark{/i}."
n "{i}The First War{/i} is directly preceded by {i}The Inception{/i}."
n "{i}The Invention{/i} is not the third, seventh, or last book."
n "{i}The Second War{/i} is the 4th book."
n "There is only one book before {i}The First War{/i}."
n "{i}The Enlightenment{/i} comes at some point after {i}The Third War{/i}."
window hide

$ TheSecondWar = True
$ TheTribe = True
$ TheInvention = True
$ TheEnlightenment = True
$ TheThirdWar = True
$ TheInception = True
$ TheSpark = True
$ TheFirstWar = True
$ remyanswers = 0

label remyques1:

menu:
    
    "The first book is:"
    
    "The Second War" if TheSecondWar: 
        $ TheSecondWar = False
        jump remyques2

    "The Tribe" if TheTribe:
        $ TheTribe = False
        jump remyques2
        
    "The Invention" if TheInvention:
        $ TheInvention = False
        jump remyques2

    "The Enlightenment" if TheEnlightenment:
        $ TheEnlightenment = False
        jump remyques2
        
    "[[Show more books.]":
        jump remyques1x
        
    "[[Show hints.]":
        call remyhints from _call_remyhints
        jump remyques1
        
label remyques1x:
    
    menu:
        
        "The first book is:"
        
        "The Third War" if TheThirdWar:
            $ TheThirdWar = False
            jump remyques2

        "The Inception" if TheInception:
            $ remyanswers += 1
            $ TheInception = False
            jump remyques2

        "The Spark" if TheSpark:
            $ TheSpark = False
            jump remyques2

        "The First War" if TheFirstWar:
            $ TheFirstWar = False
            jump remyques2
            
        "[[Show more books.]":
            jump remyques1
            
        "[[Show hints.]":
            call remyhints from _call_remyhints_1
            jump remyques1x
    

label remyques2:

menu:
    
    "The second book is:"
    
    "The Second War" if TheSecondWar: 
        $ TheSecondWar = False
        jump remyques3

    "The Tribe" if TheTribe:
        $ TheTribe = False
        jump remyques3
        
    "The Invention" if TheInvention:
        $ TheInvention = False
        jump remyques3

    "The Enlightenment" if TheEnlightenment:
        $ TheEnlightenment = False
        jump remyques3
        
    "[[Show more books.]":
        jump remyques2x
        
    "[[Show hints.]":
        call remyhints from _call_remyhints_2
        jump remyques2
        
label remyques2x:
    
    menu:

        "The second book is:"

        "The Third War" if TheThirdWar:
            $ TheThirdWar = False
            jump remyques3

        "The Inception" if TheInception:
            $ TheInception = False
            jump remyques3

        "The Spark" if TheSpark:
            $ TheSpark = False
            jump remyques3

        "The First War" if TheFirstWar:
            $ remyanswers += 1
            $ TheFirstWar = False
            jump remyques3
            
        "[[Show more books.]":
            jump remyques2
            
        "[[Show hints.]":
            call remyhints from _call_remyhints_3
            jump remyques2x
     
label remyques3:

menu:
    
    "The third book is:"
    
    "The Second War" if TheSecondWar: 
        $ TheSecondWar = False
        jump remyques4

    "The Tribe" if TheTribe:
        $ remyanswers += 1
        $ TheTribe = False
        jump remyques4
        
    "The Invention" if TheInvention:
        $ TheInvention = False
        jump remyques4

    "The Enlightenment" if TheEnlightenment:
        $ TheEnlightenment = False
        jump remyques4
        
    "[[Show more books.]":
        jump remyques3x
        
    "[[Show hints.]":
        call remyhints from _call_remyhints_4
        jump remyques3
        
label remyques3x:
    
    menu:

        "The third book is:"

        "The Third War" if TheThirdWar:
            $ TheThirdWar = False
            jump remyques4

        "The Inception" if TheInception:
            $ TheInception = False
            jump remyques4

        "The Spark" if TheSpark:
            $ TheSpark = False
            jump remyques4

        "The First War" if TheFirstWar:
            $ TheFirstWar = False
            jump remyques4
            
        "[[Show more books.]":
            jump remyques3
            
        "[[Show hints.]":
            call remyhints from _call_remyhints_5
            jump remyques3x

label remyques4:

menu:
    
    "The fourth book is:"
    
    "The Second War" if TheSecondWar: 
        $ remyanswers += 1
        $ TheSecondWar = False
        jump remyques5

    "The Tribe" if TheTribe:
        $ TheTribe = False
        jump remyques5
        
    "The Invention" if TheInvention:
        $ TheInvention = False
        jump remyques5

    "The Enlightenment" if TheEnlightenment:
        $ TheEnlightenment = False
        jump remyques5
        
    "[[Show more books.]":
        jump remyques4x
        
    "[[Show hints.]":
        call remyhints from _call_remyhints_6
        jump remyques4
        
label remyques4x:
    
    menu:

        "The fourth book is:"

        "The Third War" if TheThirdWar:
            $ TheThirdWar = False
            jump remyques5

        "The Inception" if TheInception:
            $ TheInception = False
            jump remyques5

        "The Spark" if TheSpark:
            $ TheSpark = False
            jump remyques5

        "The First War" if TheFirstWar:
            $ TheFirstWar = False
            jump remyques5
            
        "[[Show more books.]":
            jump remyques4
            
        "[[Show hints.]":
            call remyhints from _call_remyhints_7
            jump remyques4x

label remyques5:
menu:
    
    "The fifth book is:"
    
    "The Second War" if TheSecondWar: 
        $ TheSecondWar = False

    "The Tribe" if TheTribe:
        $ TheTribe = False
        
    "The Invention" if TheInvention:
        $ remyanswers += 1
        $ TheInvention = False

    "The Enlightenment" if TheEnlightenment:
        $ TheEnlightenment = False

    "The Third War" if TheThirdWar:
        $ TheThirdWar = False

    "The Inception" if TheInception:
        $ TheInception = False

    "The Spark" if TheSpark:
        $ TheSpark = False

    "The First War" if TheFirstWar:
        $ TheFirstWar = False
        
    "[[Show hints.]":
        call remyhints from _call_remyhints_8
        jump remyques5

label remyques6:
menu:
    
    "The sixth book is:"
    
    "The Second War" if TheSecondWar: 
        $ TheSecondWar = False

    "The Tribe" if TheTribe:
        $ TheTribe = False
        
    "The Invention" if TheInvention:
        $ TheInvention = False

    "The Enlightenment" if TheEnlightenment:
        $ TheEnlightenment = False

    "The Third War" if TheThirdWar:
        $ TheThirdWar = False

    "The Inception" if TheInception:
        $ TheInception = False

    "The Spark" if TheSpark:
        $ remyanswers += 1
        $ TheSpark = False

    "The First War" if TheFirstWar:
        $ TheFirstWar = False
        
    "[[Show hints.]":
        call remyhints from _call_remyhints_9
        jump remyques6

label remyques7:
menu:
    
    "The seventh book is:"
    
    "The Second War" if TheSecondWar: 
        $ TheSecondWar = False

    "The Tribe" if TheTribe:
        $ TheTribe = False
        
    "The Invention" if TheInvention:
        $ TheInvention = False

    "The Enlightenment" if TheEnlightenment:
        $ TheEnlightenment = False

    "The Third War" if TheThirdWar:
        $ remyanswers += 1
        $ TheThirdWar = False

    "The Inception" if TheInception:
        $ TheInception = False

    "The Spark" if TheSpark:
        $ TheSpark = False

    "The First War" if TheFirstWar:
        $ TheFirstWar = False
        
    "[[Show hints.]":
        call remyhints from _call_remyhints_10
        jump remyques7
        
menu:
    
    "The eighth book is:"
    
    "The Second War" if TheSecondWar: 
        $ TheSecondWar = False

    "The Tribe" if TheTribe:
        $ TheTribe = False
        
    "The Invention" if TheInvention:
        $ TheInvention = False

    "The Enlightenment" if TheEnlightenment:
        $ remyanswers += 1
        $ TheEnlightenment = False

    "The Third War" if TheThirdWar:
        $ TheThirdWar = False

    "The Inception" if TheInception:
        $ TheInception = False

    "The Spark" if TheSpark:
        $ TheSpark = False

    "The First War" if TheFirstWar:
        $ TheFirstWar = False
        
c "I think that's it."

show remy normal with easeinright

Ry "Oh, you're done? Let's take a look, then."

if remyanswers == 8:

    $ mp.remybooks = 8
    $ mp.save()

    $ remymood += 3
    show remy smile with dissolve
    Ry "Seems you got it all right. Well done, [player_name]."
    
    if persistent.c1booksort == False:

            $ persistent.c1booksort = True
            
            $ achievement.grant("Librarian")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_85
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You brought Remy's books into the correct order!"
                
            elif system == "advanced":

                s "You brought Remy's books into the correct order. Amazing."
                
            else:
                
                s "You brought Remy's books into the correct order. What an achievement."
    
    menu:
        "Phew, that was hard work.":
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "It gets easier with practice."
            jump remycont
            
        "That wasn't too hard...":
            $ renpy.pause (0.5)
            show remy normal with dissolve
            jump remycont
            
        "I didn't know I could have this much fun in a library.":
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "I can't tell if you are serious, but I appreciate your help regardless."
            jump remycont
            
elif remyanswers >= 6:

    $ mp.remybooks = 6
    $ mp.save()

    $ remymood += 1
    Ry "No, this doesn't seem to be completely right. It looks like [remyanswers] books are in the right place, though."
    menu:
        "Let me try again.":
            $ remymood -= 1
            Ry "Alright, I'll come back in a bit."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            jump reset
            
        "This is the best I can do.":
            Ry "Alright, let me fix that up for you."
            play sound "fx/booksort.wav"
            $ renpy.pause (3.0)
            show remy smile with dissolve
            Ry "There, that should be it."
            show remy normal with dissolve
            jump remycont
            
        "[[Give up and leave.]":
            c "I give up. This is stupid and you're stupid for making me do your work for you."
            show remy look with dissolve
            Ry "Well, it's not like I'm forcing you to stay here. You can see yourself out, if you can still find the exit."
            stop music fadeout 1.0
            scene black with fade
            nvl clear
            window show
            n "Apparently Remy hadn't approved of my unwillingness to be his slave." 
            n "Did he really think I wanted to spend my free time doing his work for him?" 
            n "Thanks, but no thanks, buddy."
            window hide
            nvl clear

            $ remystatus = "bad"
            
            $ remyscenesfinished = 1
            
            if chapter4unplayed == False:
                    
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars

elif remyanswers == 1:

    $ mp.remybooks = 1
    $ mp.save()

    show remy look with dissolve
    Ry "Sorry to disappoint you, but it seems only a single book is in the right place."
    menu:
        "Let me try again.":
            $ remymood -= 1
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "Alright, I'll come back in a bit."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            jump reset
            
        "This is the best I can do.":
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "I see. Let me fix that up for you, then."
            play sound "fx/booksort.wav"
            $ renpy.pause (3.0)
            show remy smile with dissolve
            Ry "There, that should be it."
            show remy normal with dissolve
            jump remycont
            
        "[[Give up and leave.]":
            c "I give up. This is stupid and you're stupid for making me do your work for you."
            Ry "Well, it's not like I'm forcing you to stay here. You can see yourself out, if you can still find the exit."
            stop music fadeout 1.0
            scene black with fade
            nvl clear
            window show
            n "Apparently Remy hadn't approved of my unwillingness to be his slave." 
            n "Did he really think I wanted to spend my free time doing his work for him?" 
            n "Thanks, but no thanks, buddy."
            window hide
            nvl clear

            $ remystatus = "bad"
            
            $ remyscenesfinished = 1
            
            if chapter4unplayed == False:
                    
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars         
    
elif remyanswers == 0:

    $ mp.remybooks = 0
    $ mp.save()

    show remy look with dissolve
    Ry "Sorry to disappoint you, but it seems not a single book is in the right place."
    menu:
        "Let me try again.":
            $ remymood -= 1
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "Alright, I'll come back in a bit."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            jump reset
            
        "This is the best I can do.":
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "I see. Let me fix that up for you, then."
            play sound "fx/booksort.wav"
            $ renpy.pause (3.0)
            show remy smile with dissolve
            Ry "There, that should be it."
            show remy normal with dissolve
            jump remycont
            
        "[[Give up and leave.]":
            c "I give up. This is stupid and you're stupid for making me do your work for you."
            Ry "Well, it's not like I'm forcing you to stay here. You can see yourself out, if you can still find the exit."
            stop music fadeout 1.0
            scene black with fade
            nvl clear
            window show
            n "Apparently Remy hadn't approved of my unwillingness to be his slave." 
            n "Did he really think I wanted to spend my free time doing his work for him?" 
            n "Thanks, but no thanks, buddy."
            window hide
            nvl clear

            $ remystatus = "bad"
            
            $ remyscenesfinished = 1
            
            if chapter4unplayed == False:
                
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars          
                
else:
    show remy look with dissolve

    $ mp.remybooks = remyanswers
    $ mp.save()

    Ry "Sorry to disappoint you, but it seems only [remyanswers] books are in the right place."
    menu:
        "Let me try again.":
            $ remymood -= 1
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "Alright, I'll come back in a bit."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            jump reset
            
        "This is the best I can do.":
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "I see. Let me fix that up for you, then."
            play sound "fx/booksort.wav"
            $ renpy.pause (3.0)
            show remy smile with dissolve
            Ry "There, that should be it."
            show remy normal with dissolve
            jump remycont
            
        "[[Give up and leave.]":
            c "I give up. This is stupid and you're stupid for making me do your work for you."
            Ry "Well, it's not like I'm forcing you to stay here. You can see yourself out, if you can still find the exit."
            stop music fadeout 1.0
            scene black with fade
            nvl clear
            window show
            n "Apparently Remy hadn't approved of my unwillingness to be his slave." 
            n "Did he really think I wanted to spend my free time doing his work for him?" 
            n "Thanks, but no thanks, buddy."
            window hide
            nvl clear

            $ remystatus = "bad"
            
            $ remyscenesfinished = 1
            
            if chapter4unplayed == False:
                
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars        
            
            
label remycont:
Ry "In any case, there's a box here that belongs in storage. You can put that away, I'll finish the last bit of sorting, and then we will be done for the day."

menu:
    "Sure thing.":
        $ remymood += 1
        $ renpy.pause (0.5)
        
    "If I have to.":
        $ renpy.pause (0.5)
        
    "Do I have to?":
        Ry "No, you don't have to, but it would be a lot easier for you than it would be for me - considering that you, by nature, are gifted with proper and more dexterous hands than mine." 
        c "Alright, alright. I'll do it."
        
show remy smile with dissolve
Ry "Great! See you in a bit, then."

show remy normal with dissolve
show remy normal flip
$ renpy.pause (0.3)
hide remy with easeoutright

$ renpy.pause (0.5)
play sound "fx/box.wav"

c "(Phew, that is heavier than I thought.)"
m "I lifted the box and carried it towards its shelf, but just as I was about to reach it, I tripped suddenly, sending me to the ground as the contents of the box spilled across the floor."

play sound "fx/fall.wav"

c "Ouch!" with vpunch
m "I scrambled to gather the various items as the voice of the dragon called out to me."
Ry "Is everything alright?"
m "Before I could answer, Remy came around the corner, his face bearing a look of disapproval. He stooped over and helped me pick up the spilled objects."

show remy look with dissolve

c "Yeah, I'm fine."

show remy sad with dissolve

Ry "I was mainly asking about the priceless artifacts you just dropped." 

menu:
    "S-Sorry...":
        $ remymood += 1
        $ renpy.pause (0.5)
        show remy look with dissolve
        Ry "Well, it doesn't look like anything is broken. That could have ended up much worse."

    "Oh, guess my own safety isn't worth as much.":
        $ renpy.pause (0.5)
        show remy look with dissolve
        Ry "It is, but it's not like we could display you in a museum as a replacement."
        show remy normal with dissolve
        Ry "On second thought, I suppose we could, but we would have to stuff you first."
        c "Speaking of stuff, what is all this, anyway?"
        jump remystuff

    "You shouldn't have asked me for help if you were so worried about the condition of these things.":
        $ remymood -= 1
        $ renpy.pause (0.5)
        show remy look with dissolve
        Ry "I suppose you have a point."

    "[[Make fun of him for caring so much about books and scrolls.]":
        m "I picked up one of the scrolls that had unraveled during the commotion and taunted him with it. It now had a large hole after falling on one of the other artifacts."
        c "Oh, look at me, I'm Remy! I'm such a huge NERD. I like scrolls so much that I'd marry them if I could."
        Ry "..."
        c "Wait a minute, is that why that hole is there? I mean, I knew you liked them, but this is a little much, don't you think?"
        Ry "No, it's because you dropped this highly fragile scroll on this relic. You damaged it!" 
        c "Chill out, it's not like it belongs to anyone. It's just a library item." 
        Ry "That makes it even worse. That scroll belongs to everybody. I hope you plan to make up for this."
        c "Nothing a little tape can't fix. No one will even notice the difference." 
        Ry "We don't approve of such an obvious disregard for public property. Don't you realize such behavior does not only reflect poorly on yourself, but also on the whole of mankind? You're an ambassador! How could you be so irresponsible?" 
        c "I already said I was sorry, so shut up already." 
        Ry "You did not say you were sorry!"
        c "Sorry. I mean, sorry for not being sorry earlier." 
        Ry "Frankly, this is inexcusable. We're both lucky that Emera isn't here to see this. I'll have to think about how we can fix it." 
        c "I've got an idea. We only need some white glue, a paperclip and some googly eyes." 
        Ry "..." 
        Ry "I think you should leave." 
        c "I just told you, I've got a great idea!" 
        Ry "Now."
        stop music fadeout 1.0
        scene black with dissolve

        $ remystatus = "bad"
        
        $ remyscenesfinished = 1
        
        if chapter4unplayed == False:
            
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
        
        
c "What is all this stuff, anyway?"

show remy normal with dissolve

label remystuff:
Ry "In preparation for your arrival, I wanted to study what knowledge we had on humans."
c "And what did you learn?"
Ry "Heh, not much. The human is a creature shrouded in mystery and legend, yet one we apparently share some history with."
c "(Sure, dragon. Tell me I'm the mythological creature.)"
Ry "As the story goes, we dragons were once a primitive and savage civilization, living in caves and whatnot. We fought other creatures and amongst each other for resources and territory."
Ry "One day, however, a human arrived who performed many miracles and gave us the gifts of electricity and reason. We refer to this event as our {i}awakening{/i}."    
c "What happened to them? And who were they, anyway?"
Ry "They say it was a divine creature, a supernatural being that saved our species by making peace between our clans and uniting us, as our numbers were dwindling from our pointless conflicts."
Ry "And when the deed was done, they ascended to the heavens from where they came - or turned into a dragon and lived among us, ruling with kindness and wisdom until their eventual passing, depending on who you ask."    
c "And what do you make of this story?"
Ry "As unlikely as it sounds, there is evidence for sudden, unprecedented technological advancement in our timeline. We have artifacts from that time that couldn't have been built with the knowledge we had back then." 
c "I'm starting to think you already have a theory."
Ry "Indeed. I take it you are familiar with the way the portals through which you traveled here actually work?"

menu:
    "Not very.":
        pass
        
    "Actually, I am.":
        $ remymood += 1
        
    "I don't know, nor do I care.":
        $ remymood -= 1
        
Ry "It's simple, really. There are spontaneous wormholes that pop into existence now and then, but their highly unstable nature means that they instantly collapse in on themselves."
Ry "The machinery of the portal merely stabilizes the wormhole so that we may utilize it. We actually are just taking advantage of a naturally occurring phenomenon."

menu:
    "Fascinating stuff.":
        pass
        
    "That's pretty cool.":
        $ remymood += 1
        
    "The longer you keep talking about this, the less I care.":
        $ remymood -= 1
        
Ry "Long story short, my theory is that this legendary person stumbled upon one of these natural wormholes in the split second it existed, bringing them into our world."
c "Being thrust into an unfamiliar world with no means to return to their own. Talk about being at the wrong place at the wrong time."
Ry "Or just the right one, if you ask me. If it wasn't for them, we wouldn't be here today." 
Ry "Oh, what I would give to know more about them."
c "How do you know so much about the portal, anyway?"
Ry "We found it a while ago, so we've had time to study it. Not me personally, mind you, but I followed its developments with great interest."
c "What else have you discovered about it?"
Ry "Not much, I'm afraid. We didn't want to take the risk of permanent damage, so we won't do anything rash until we completely understand the technology and can replicate it for ourselves."
Ry "So far, the only thing it has done for us was locating your portal and connecting us to it. From the interface, it appears to have more functions, but we haven't been able to get any of them to work."
Ry "We were not even sure what it was capable of when we initially turned it on. Only after some time of being active did it actually find your portal, and only then were we able to make the connection."
c "Making that discovery must have been very exciting, especially when you made contact with us and started exchanging letters with us."
Ry "Oh, you have no idea. Especially when Reza arrived and he turned out to be a human, of all things. Some people still worship them, you know."
c "You've mentioned that before. How does that work? Do you have some kind of organized religion based around it?"
Ry "Not exactly. It is more like an adoration on a personal level. I'd count myself amongst them if it wasn't for the fact that I consider myself to have a more reasonable approach to it than others."
Ry "For example, there are those that believe there is much more to your sudden appearance than there really is. I think they expect some sort of miracle from you, similar to what was ascribed to humans in the past."

menu:
    "Well, I can tell you that there is nothing supernatural about me.":
        $ remymood += 1
        $ renpy.pause (0.5)
        show remy smile with dissolve
        Ry "That's what I expected."
        show remy normal with dissolve

    "Those people are stupid.":
        $ remymood -= 1
        $ renpy.pause (0.5)
        show remy look with dissolve
        Ry "Well, they're free to believe what they want. They'll see soon enough, anyway. Live and let live, as they say."
        show remy normal with dissolve

    "Maybe you should worship me.":
        Ry "I'm sure you'd like that, but respect is earned, not given."

Ry "Either way, as a scholar, I'm looking forward to see everything your PDAs have to offer."
c "I could show you sometime."

show remy smile with dissolve

Ry "I see. Well, don't worry about explaining them to me. I'm sure you have much more important things to do while you are here. It is just a question of time until one of them ends up with me, anyway."
c "Actually, the PDAs are one of the reasons I volunteered to come here."

show remy normal with dissolve

Ry "What do you mean?"
c "I know them pretty well. Enough to explain how they work, at least. Of course, that's far from the only reason. I just thought I'd be the kind of person who'd meet all of the requirements, and it turned out I was."
Ry "I see. It was nice of you to volunteer when you must have known there would be considerable risks in coming here."
c "You volunteered as well when you came to meet me, didn't you? I wouldn't think this kind of thing would fall under your jurisdiction regularly."

show remy shy with dissolve

Ry "That is true, but by this point, my interest in these matters shouldn't surprise you."
c "I was more surprised that I arrived under cover of darkness to meet an ambassador, though I haven't seen much of you since."

show remy normal with dissolve

Ry "Initially, they wanted to have an official reception headed by myself, but in the end they changed their minds due to security concerns, as I told you back then." 
c "I suppose that's also why I'm being escorted by the police all the time."
Ry "Yeah, that was supposed to be my job too, until someone from the police department objected and advocated for more security. Better be safe than sorry, I suppose."
c "Let me guess, that someone was Maverick."

show remy look with dissolve
Ry "How'd you know that?"

c "Just a hunch."

show remy smile with dissolve

Ry "At least I still got to meet you."
c "Were you nervous when you did?"

show remy normal with dissolve

Ry "Only the brave or the foolish wouldn't be. I consider myself neither."

menu:
    "I have to admit I was, too. I was speechless when I saw you, and that wasn't just a side-effect of the teleportation.":
        $ remymood += 1
        Ry "To be fair, I would have been as well, if we didn't already know about humans and Reza."

        $ mp.remybrave = "nervous"
        $ mp.save()

    "I think you were pretty brave.":
        Ry "No, it was just scientific curiosity." 
        c "You know what they say about curiosity and cats." 
        Ry "I'm afraid I don't."

        $ mp.remybrave = "brave"
        $ mp.save()

    "I think you were pretty foolish.":
        $ remymood -= 1
        $ renpy.pause (0.5)
        show remy look with dissolve
        Ry "I'm starting to think so, too."
        $ mp.remybrave = "foolish"
        $ mp.save()


m "There was a moment of silence between us and our eyes met briefly, when suddenly, a loud call echoed through the building."
Em "REMY!" with vpunch
Ry "I better go and see what that is about."
Ry "Maybe it would be better if you didn't stay out in the open. At the end of the hallway, you can find my office towards the right. Wait for me there."
c "Alright."

show remy normal flip
$ renpy.pause (0.3)
hide remy with easeoutright
$ renpy.pause (0.5)
stop music fadeout 1.0
scene office2 at Pan ((0, 228), (128,228), 3.0) with dissolveslow

$ renpy.pause (1.0)
c "(So, this is your office, Remy.)"
play music "mx/fireplace.ogg"
$ remywait = True
$ remywaitn = 0
$ remytrash = True
$ remytrashn = 0
$ remyfern = True
$ remynotebook = True
$ remycoffee = True
$ remymirror = True

label remyoffmenu:

menu:
    "Wait." if remywait:
        if remywaitn == 0:
            $ remywaitn += 1
            c "(Let's wait for a bit.)"
            $ renpy.pause (1.0)
            c "(Nothing happened.)"
            jump remyoffmenu
            
        elif remywaitn == 1:
            $ remywaitn += 1
            c "(Let's wait some more.)"
            $ renpy.pause (2.0)
            c "(Nothing happened.)"
            jump remyoffmenu
            
        else:
            $ remywait = False
            c "(Let's wait even longer.)"
            $ renpy.pause (3.0)
            c "(Alright, this was long enough.)"
            
            if persistent.c1boredom == False:

                $ persistent.c1boredom = True
                
                $ achievement.grant("Patient")
                
                $ persistent.achievements += 1
                
                call syscheck from _call_syscheck_86
                
                play sound "fx/system.wav"
                
                $ boredom += 3
                
                if system == "normal":
                
                    s "Your boredom has increased by 3 points!"
                    
                elif system == "advanced":

                    s "Your boredom has increased by 3 points. That'll come in handy."
                    
                else:
                    
                    s "Your boredom has increased by 3 points. Obviously, this is the most important stat of all."

            jump remyoffmenu
            
    "Rummage through his trash." if remytrash:
        c "(Let's see, what do we have here...)"
        play sound "fx/rummage2.ogg"
        $ renpy.pause (1.5)
        if remytrashn == 0:
            $ remytrashn += 1
            c "(What's this? Something's wrapped in paper.)"
            play sound "fx/unwrap.ogg"
            $ renpy.pause (2.0)
            c "(It's a partially eaten sandwich, covered in mold.)"
            c "(I'm not going to eat that.)"
            jump remyoffmenu
            
        else:
            $ remytrash = False
            c "(There are a lot of used tissues. Maybe he had the flu, but dutiful as he is, he still went to work sick. Poor Remy.)"
            jump remyoffmenu
        
    "Look at his notebook." if remynotebook:
        $ remynotebook = False
        c "(Heavy paper, perfect binding. I can tell by the cover alone that this is not the cheap stuff, but the result of quality bookmaking.)"
        c "(Alright, let's take a peek inside...)"
        play sound "fx/paper.wav"
        $ renpy.pause (1.0)
        c "(Looks like unsorted notes. His handwriting is terrible.)"
        c "(A... m... e... nope, can't make it out.)"
        jump remyoffmenu

    "Drink his coffee." if remycoffee:
        $ remycoffee = False
        c "(There's still a little bit left in the cup.)"
        play sound "fx/coffee.wav"
        $ renpy.pause (2.0)
        c "(Ugh... so stale.)"
        jump remyoffmenu
        
    "Look in the mirror." if remymirror:
        $ remymirror = False
        if player_name == "Jayden":
            m "Furrowing my brows, I took a moment to consider the events that took place ever since I arrived in the dragon's world while I looked myself over in the mirror. I was aware of that, regardless of the outcome, humanity would never be the same again after my return."
            m "I considered these implications and also thought about what wisdom and insight could be gained from this and how it would help me on my mission, when it suddenly hit me:" 
            c "How can mirrors be real if dragons aren't real?"
            m "Indeed, truer words had never been spoken."
            jump remyoffmenu
        
        elif player_name == "Jaden":
            m "Furrowing my brows, I took a moment to consider the events that took place ever since I arrived in the dragon's world while I looked myself over in the mirror. I was aware of that, regardless of the outcome, humanity would never be the same again after my return. I considered these implications and also thought about what wisdom and insight could be gained from this and how it would help me on my mission, when it suddenly hit me:" 
            c "How can mirrors be real if dragons aren't real?"
            m "Indeed, truer words had never been spoken."
            jump remyoffmenu
        
        else:
            c "It's just a mirror, nothing special about it."
            jump remyoffmenu
        
    "Look at his computer.":
        c "(I wonder if their computers are similar to ours. Let's see...)"
        m "At the press of a button, the screen came to life, accompanied by the whir of the machine. After a few seconds, colorful images appeared on the screen."

stop music fadeout 1.0
scene black with dissolve
$ renpy.pause (1.0)
scene rpg 
show aaliyah 2
show bonnar 1
show aidith 2
show ryszard 2
show ronan 1
with dissolveslow

#show aaliyah 1 at Position(xpos = 50, xanchor=0, ypos=0, yanchor=0)
show aaliyah 1 at Pan ((0, 0), (-50, 0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Aaliyah: Have you come here to beg for mercy?{/font}{/color}"
#play sound "fx/beep.wav"
#show aaliyah 2 at Position(xpos = 0, xanchor=0, ypos=0, yanchor=0)
show aaliyah 2 at Pan ((-50, 0), (0,0), 0.1)

$ renpy.pause (0.2)

#show ryszard 1 at Position(xpos = -50, xanchor=0, ypos=0, yanchor=0)
show ryszard 1 at Pan ((0, 0), (50,0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Ryszard: No, Aaliyah, we've come to stop you. Your reign of terror over the land of Marmoa is over. You're outnumbered. Just give up and we can end this without bloodshed.{/font}{/color}"
#play sound "fx/beep.wav"
#show ryszard 2 at Position(xpos = 0, xanchor=0, ypos=0, yanchor=0)
show ryszard 2 at Pan ((50, 0), (0, 0), 0.1)

$ renpy.pause (0.2)

show aaliyah 1 at Pan ((0, 0), (-50, 0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Aaliyah: The area is teeming with my soldiers, outnumbering you thousands to one. But I don't even need them. Who knows, if you survive long enough, you might just see why I'm called Aaliyah the Ascended.{/font}{/color}"
#play sound "fx/beep.wav"
show aaliyah 2 at Pan ((-50, 0), (0,0), 0.1)

$ renpy.pause (0.2)

show aidith 1 at Pan ((0, 0), (50,0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Aidith: Oh, you pompous \&\%\*\#\+\@.{/font}{/color}"
#play sound "fx/beep.wav"
show aidith 2 at Pan ((50, 0), (0, 0), 0.1)

$ renpy.pause (0.2)

show bonnar 2 at Pan ((0, 0), (50,0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Bonnar: Calm down, Aidith. Focus.{/font}{/color}"
#play sound "fx/beep.wav"
show bonnar 1 at Pan ((50, 0), (0, 0), 0.1)

$ renpy.pause (0.2)

show ryszard 1 at Pan ((0, 0), (50,0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Ryszard: I'm sorry it has to come to this, Aaliyah. But this ends now.{/font}{/color}"
#play sound "fx/beep.wav"
show ryszard 2 at Pan ((50, 0), (0, 0), 0.1)

$ renpy.pause (0.2)

show aaliyah 1 at Pan ((50, 0), (0, 0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Alliyah: Ronan, get them!{/font}{/color}"
#play sound "fx/beep.wav"
show aaliyah 2 at Pan ((0, 0), (50,0), 0.1)

$ renpy.pause (0.2)

show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Grrr!{/font}{/color}"
#play sound "fx/beep.wav"
show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

$ renpy.pause (0.2)

play music "mx/rpg.ogg"
queue music "mx/rpg2.ogg"

Al "{color=#FFFFF0}{font=Munro.ttf}Battle start!{/font}{/color}"
#play sound "fx/beep.wav"

show aidith 1 at Pan ((0, 0), (50,0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Aidith uses Whirlwind!{/font}{/color}"
play sound "fx/rpg/wind.ogg"
$ renpy.pause (2.0)

play sound "fx/rpg/hit.ogg"

show ronan 1 with vpunch
Al "{color=#FFFFF0}{font=Munro.ttf}Ronan takes 326 damage!{/font}{/color}"

show aidith 2 at Pan ((50, 0), (0, 0), 0.1)

$ renpy.pause (0.3)


show bonnar 2 at Pan ((0, 0), (50,0), 0.1)
Al "{color=#FFFFF0}{font=Munro.ttf}Bonnar uses Earthquake!{/font}{/color}"

play sound "fx/rpg/quake.ogg"
show ronan 1 with Shake((0, 0, 0, 0), 3.0, dist=30)
play sound "fx/rpg/hit.ogg"
show ronan 1 with vpunch
Al "{color=#FFFFF0}{font=Munro.ttf}Ronan takes 465 damage!{/font}{/color}"

show bonnar 1 at Pan ((50, 0), (0, 0), 0.1)

$ renpy.pause (0.3)

show ronan 2
Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Grrrrrrrr!{/font}{/color}"
Al "{color=#FFFFF0}{font=Munro.ttf}Ronan invokes Cosmic Horror! {/font}{/color}"

play sound "fx/rpg/whoosh.ogg"
scene space 
show bonnar 1
show aidith 2
show ryszard 2
with dissolve

play sound "fx/rpg/horror.ogg"

$ renpy.pause (1.0)

show skull with dissolveslow3

hide skull
scene rpg
show aaliyah 2
show bonnar 1
show aidith 2
show ryszard 2
show ronan 1
with dissolve

play sound "fx/rpg/hit.ogg"
show bonnar 2 with vpunch
Al "{color=#FFFFF0}{font=Munro.ttf}Bonnar takes 1089 damage!{/font}{/color}"

play sound "fx/rpg/hit.ogg"
show ryszard 2 with vpunch

Al "{color=#FFFFF0}{font=Munro.ttf}Ryszard takes 1205 damage!{/font}{/color}"

play sound "fx/rpg/hit.ogg"
show aidith 2 with vpunch

Al "{color=#FFFFF0}{font=Munro.ttf}Aidith takes 1373 damage!{/font}{/color}{nw}"

stop music
scene bsod

$ renpy.pause (5.0, hard=True)

scene office2 at Pan ((128, 228), (128,228), 0.0) with fade

c "What the...?"

play music "mx/fireplace.ogg" fadein 1.0

show remy look with dissolve

Ry "Hey, what are you doing?"

menu:
    "I think I broke it.":
        pass
    "Nothing.":
        pass
    "...":
        pass

Ry "Oh no, let me take a look. Why did you even touch the computer?"

menu:
    "I got bored.":
        $ renpy.pause (0.5)
        
    "It's fine, it's just a computer.":
        $ remymood -= 1
        $ renpy.pause (0.5)
        
    "I just wanted to see what was on it.":
        $ renpy.pause (0.5)

show remy normal with dissolve
Ry "Well, whatever you did... At least it seems to be okay."

show remy look with dissolve
Ry "Oh no, my game!"
c "What's wrong?" 
Ry "When you touched the computer, you saw a game running, right?"
c "Yeah, I played a little."

show remy sad with dissolve
Ry "I had it saved specifically at that moment to play it later... and now it's all gone."
c "What do you mean, it's all gone?"
Ry "So much preparation, so many hours spent grinding, just to get there. I can't do all of that again. You wouldn't understand."

menu:
    "Actually, I do.":
        $ remymood += 1
        $ renpy.pause (0.5)
        show remy normal with dissolve
        Ry "You do?" 
        c "Yeah, we used to have similar games where I come from."
        Ry "I see."

    "Calm down, it's just a game.":
        $ remymood -= 1
        Ry "Now I'll never find out how the story ends."
        c "I imagine the good guys will beat the bad guys. That's how it usually goes."
        show remy normal with dissolve
        Ry "Maybe, but the journey is its own reward."

    "Sorry.":
        $ renpy.pause (0.5)
        show remy normal with dissolve
        Ry "To be fair, the computer is old, so it might not have been your fault."
        
Ry "Well, at least my office is still standing."
c "Speaking of which, what's with the bed? It looks like you live here."
Ry "When I have to work late, it's just easier to stay here."

show remy smile with dissolve

Ry "Besides, I have the knowledge of the whole library at my fingertips and can use the resources and equipment as I please, like this computer."
c "Don't you have one at home?"

show remy normal with dissolve

Ry "No, we generally don't have this kind of technology in every household, though it's not exactly rare either. We just use it where we need it."
c "Back home, we used to have computers everywhere. Most of us even carried one on our wrist wherever we went."
Ry "Is that so?"

play sound "fx/bell.ogg"

$ renpy.pause (2.0)

Ry "Oh, that means the library will be closing pretty soon. If you want to do or ask anything in particular, now is the time."

menu:
    "I'd like to know more about your human myths.":
        $ remymood += 1
        Ry "There's a lot we could get into, but I'm afraid we won't have enough time now. Maybe another day."
        
    "Are you \"available\"?":
        $ remymood -= 1
        Ry "What do you mean by that?"
        c "You know, for a relationship."
        show remy look with dissolve
        Ry "That is... If you are going to ask me like that, my answer is going to be no."
        
    "I can't really think of anything.":
        Ry "I guess it's time to go, then. I'd rather not annoy the other employees by staying longer than we should."

if remymood <= 0:
    show remy look with dissolve
    Ry "Anyways, thank you for your help. This certainly was an... informative... meeting."
    menu:
        "Yeah, whatever.":
            pass
            
        "Now kiss me already, you handsome albino.":
            Ry "Absolutely not! What is wrong with you? Besides, I'll have you know that I am not, in fact, an albino." 
            
        "I agree.":
            pass
    
    Ry "See you, then, and have a nice evening."
    c "You too."
    show remy normal flip
    $ renpy.pause (0.3)
    hide remy with easeoutright
    $ renpy.pause (0.4)
    nvl clear
    stop music fadeout 1.0
    window show
    n "And he was gone. I wasn't sure what I did wrong, but I got the impression he would not want to meet with me again, despite the time I had sacrificed to help him out." 
    n "At least there were always other dragons to meet."
    window hide
    
    $ remystatus = "bad"
    
    $ remyscenesfinished = 1
    
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
elif remymood <= 12:
    
    label remy1skip:
    Ry "Anyways, thank you for your help. If there is any way I can repay you, just let me know."
    menu:
        "How about you invite me to dinner some time?":
            $ renpy.pause (0.5)
            show remy smile with dissolve
            Ry "That's fine with me. You've got my number, so call me about it when you have the time."
            c "I will. Have a nice evening."
            show remy normal with dissolve
            Ry "You too."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            
        "How about a kiss?":
            $ renpy.pause (0.5)
            show remy look with dissolve
            Ry "That's... not very appropriate. Have a nice evening."
            show remy look flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            $ renpy.pause (0.5)
            
            
        "I can't really think of anything.":
            Ry "Well, what do humans typically do in such a situation?"
            c "Invite them for a meal, probably."
            show remy smile with dissolve
            Ry "Then that's what I'll do."
            c "Sounds good to me." 
            show remy normal with dissolve
            Ry "Alright then, have a nice evening!" 
            c "You too."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            
    nvl clear
    stop music fadeout 1.0
    window show
    n "We parted amicably, or so I thought." 
    n "Would I see him again?" 
    n "I wasn't sure, but I kept his number, just in case."
    window hide

    $ remystatus = "neutral"
    
    $ remyscenesfinished = 1
    
    $ persistent.remy1skip = True
    if chapter4unplayed == False:
        
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars

else:
    show remy smile with dissolve
    Ry "Anyways, thank you for your help. How about I invite you to my place for dinner some time to repay you?"
    c "Oh, that's not necessary. I enjoyed my time here."
    show remy normal with dissolve
    Ry "I insist."
    c "Alright, then. I already have your number, and you probably have mine as well?"
    Ry "I do."
    c "Great. Call me when it's convenient for you."
    Ry "I will. Good night, [player_name]."
    c "Good night."
    show remy normal flip
    $ renpy.pause (0.3)
    hide remy with easeoutright
    nvl clear
    stop music fadeout 1.0
    window show
    n "I wondered whether the dragon was being nice or just didn't want to feel indebted to me after I helped him." 
    n "In any case, the time I spent in the library had been enjoyable, and I was looking forward to seeing him again." 
    n "Though, I wondered about his insistence on inviting me into his home. Had I just been asked out by a dragon?" 
    n "I was going to find out soon enough..."
    window hide

    $ remystatus = "good"
    
    $ remyscenesfinished = 1
    
    $ persistent.remy1skip = True
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
    
#+13 -12
label bryce1:
    
$ brycebar = False
$ chapter1csplayed += 1
$ bryce1unplayed = False
$ bryce1played = True
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Bryce 1"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Bryce 1"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Bryce 1"
    
else:

    $ save_name = "Chapter 1 - Bryce 1"

if persistent.playedzhong == True:
    define Wr = Character("Zhong", color="#7e9147", image="zhong")

scene black with fade
$ renpy.pause (1.0)
scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow

play music "mx/clouds.ogg" fadein 1.0
m "Once again, I found myself within the police department, which seemed oddly quiet for this time of day." 
m "It didn't take me long to spot Bryce in his office."

show bryce normal b with dissolve

Br "Hey [player_name], what's up?"
c "Nothing much, but you told me to contact you if I could remember anything that might help with the investigation."
Br "That's right. What do you have for me?"
c "I'm not sure if it's worth mentioning, but I have known Reza for a couple of years, so I know some things about his personality."

show bryce stern b with dissolve

Br "Mhm, I see. Well, that's actually more helpful than you might think. Mannerisms, habits - all kinds of things would be useful to add to his profile and to get a better idea of him."

show bryce normal b with dissolve

Br "You know, I'm just about done here for the day, but if you want to discuss it over a beer or something, I'd be more than happy."

$ brycemood = 0

menu:
    "I don't usually drink, though.":
        Br "That's fine, you don't have to." 
        show bryce smirk b with dissolve
        Br "Or maybe we'll find something you'll like."
        menu:
            "That sounds fair.":
                $ renpy.pause (0.5)
                jump contbar
                
            "[[press him about wanting to go to a bar.]":
                c "Actually, I find it worrisome that the chief of police prefers to get drunk instead of hearing important information about a case."
                show bryce brow b with dissolve
                Br "You're quite right. In my own free time I do prefer to get drunk instead of dealing with work. If you find that \"worrisome\", maybe you should try out my job sometime."
                menu:
                    "S-Sorry, that's not what I meant.":
                        $ renpy.pause (0.5)
                        show bryce stern b with dissolve
                        Br "Well, are you coming or not?"
                        menu: 
                            "Alright.":
                                $ renpy.pause (0.5)
                                jump contbar
                                
                            "I'd rather not.":
                                $ renpy.pause (0.5)
                                show bryce normal b with dissolve
                                Br "In that case, you can say whatever it is you have to say to someone else tomorrow, alright?"
                                c "Sure."
                                show bryce laugh b with dissolve
                                Br "Now, please excuse me before I miss happy hour."
                                show bryce laugh b flip
                                $ renpy.pause(0.3)
                                hide bryce with easeoutright
                                $ renpy.pause(1.0)
                                nvl clear
                                stop music fadeout 1.0
                                window show
                                n "My meeting with Bryce ended before it even had a chance to pick up." 
                                n "How could that be?" 
                                n "Was it my mistake?" 
                                n "Or maybe our personalities just weren't compatible." 
                                n "Of course, not having a drunkard as a friend wasn't too bad of an outcome."
                                $ nodrinks = True
                                window hide

                                $ brycestatus = "bad"

                                $ brycescenesfinished = 1
                                
                                if persistent.c1teetotaler == False:

                                    $ persistent.c1teetotaler = True
                                    
                                    $ achievement.grant("Teetotaler")
                                    
                                    $ persistent.achievements += 1
                                    
                                    call syscheck from _call_syscheck_37
                                    
                                    play sound "fx/system.wav"
                                    
                                    if system == "normal":
                                    
                                        s "You rejected Bryce's invitation!"
                                        
                                    elif system == "advanced":

                                        s "You rejected Bryce's invitation. Whatever."
                                        
                                    else:
                                        
                                        s "You rejected Bryce's invitation. Why is anyone's guess."    
                                
                                
                                if chapter4unplayed == False:
                                    
                                    jump chapter4chars
                                    
                                elif chapter3unplayed == False:
                                    
                                    jump chapter3chars
                                    
                                elif chapter2unplayed == False:
                                    
                                    jump chapter2chars
                                    
                                else:

                                    jump chapter1chars

                        
                    "It can't be that hard.":
                        $ renpy.pause (0.5)
                        show bryce stern b with dissolve
                        Br "Alright, kiddo, that's enough. You better go now before you make me really mad."
                        stop music fadeout 1.0
                        scene black with fade
                        nvl clear
                        n "I might not be the wisest person that ever lived, but if I knew one thing, it was that getting on a dragon's bad side was not a very good idea." 
                        n "According to his wishes, I left, wondering what went wrong between us." 
                        n "I just wanted to help, and that was how he showed his gratitude?" 
                        n "I could certainly live without Bryce from now on, then."
                        window hide
                        $ nodrinks = True
                        $ brycestatus = "bad"
                        
                        $ brycescenesfinished = 1
                        
                        if chapter4unplayed == False:
                    
                            jump chapter4chars
                            
                        elif chapter3unplayed == False:
                            
                            jump chapter3chars
                            
                        elif chapter2unplayed == False:
                            
                            jump chapter2chars
                            
                        else:

                            jump chapter1chars

    "Just one? I'll take three.":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce laugh b with dissolve
        Br "We'll see about that."
        show bryce normal b with dissolve
        jump contbar

    "Let's go.":
        jump contbar




label contbar:
show bryce normal b with dissolve

Br "Alright, let's go."

play sound "fx/steps/clean2.wav"

scene black with fade
scene bare with fade

play sound "fx/chair.wav"
$ renpy.pause(1.2)

show bryce normal with dissolve

Br "Here we are."

#insert skip here

if persistent.bryce1skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_38

    call skiptut from _call_skiptut_8
        
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
            call skipcheck from _call_skipcheck_8
            
            scene pad at Pan ((0, 360), (0,360), 0.0)
            show bryce brow
            with dissolvemed
                        
            play music "mx/campfire.ogg" fadein 2.0
            
            jump bryce1skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/clouds.ogg" fadein 1.0

if lorem1unplayed == True:

    c "Not too shabby, I have to admit."
    
show bryce smirk with dissolve

Br "And just in time for happy hour."
c "Do you come here often?"

show bryce laugh with dissolve

Br "Sometimes."

show bryce normal with dissolve
show bryce normal at right with ease
show waiter flip at left with easeinleft

Wr "Hey, you two. What can I bring you?"
Br "Just the usual."
Wr "One generic beer for the chief of police, sure thing. How about you, [player_name]?"
$ beer = False
$ waitermenu = True
label waitmenu:
menu:
    "Me too.":
        $ beer = True
        
    "Nothing yet. I'll have something later, I think.":
        pass
        
    "How'd you know my name?" if waitermenu:
        $ waitermenu = False
        Wr "How couldn't I? Everyone knows about you. So, what will it be?"
        jump waitmenu

Wr "Noted. I'll be right back."
show waiter
$ renpy.pause (0.3)
hide waiter with easeoutleft
$ renpy.pause (1.5)
show waiter flip at left with easeinleft
play sound "fx/glasses.wav"

m "It wasn't long before the waiter returned with a drinking bowl as wide as it was tall, filled to the brim with a foam-topped, dark amber liquid. Carefully, he set it down in front of Bryce, who didn't hesitate to take a big gulp."
if beer == True:
    m "He brought one for me as well, provided in a glass that seemed more appropriate for my kind."
else:
    pass
    
Wr "There you go. Just call me if you need anything."
Br "Of course."

show waiter
$ renpy.pause (0.3)
hide waiter with easeoutleft
$ renpy.pause (0.4)
show bryce normal at center with ease
show bryce brow with dissolve

Br "So, what is it you wanted to tell me about Reza?"
c "There are a few things... I mean, they're probably not much, but anything might help, right?"

show bryce stern with dissolve

Br "That's right. Anything unusual about him, anything that defines his character or stands out about him could help us. How about you tell me what you know about him?"
c "Well, the earliest memory I have of him was when we both went to the same school. We only shared a few classes, though, and a couple of friends." 

c "Overall, I'd say he was an above-average student. We didn't talk very often, but he always was very outspoken and never failed to speak up to make his opinions known."
c "He was the kind of person I'd fully expect to become a politician one day, or at least an activist of some sort. That's the impression I got from him. He spoke a lot, but you could also expect him to act on his word."
c "Of course, his nature caused him to clash with others, sometimes even including the school staff, though his genuine enthusiasm also garnered praise from them. He was quite a character."
c "After we all graduated, I didn't hear anything about him for a long time. Only some years later, after we found the portal, was I surprised to find out he was the human who would be sent to your world. He had volunteered."
c "It wasn't until I was already here that I actually met him again, however brief our interactions were. But then I already told you everything about what happened prior to the eventual scuffle with Maverick."
c "There's only one thing that stands out to me about those events: In the restaurant, when he told me about the letter, he mentioned I would know how to read its secret message."
c "I know he values the use of his own intellect, but when I received the letter later, he apparently fully expected me to remember a random chemistry class we had together years ago in order to see the message."

show bryce brow with dissolve

Br "I see, so you did not arrange this beforehand?"
c "Not at all. I had no idea."
Br "That is quite peculiar."
c "I know. I still wonder what he would have told me if Maverick hadn't interfered when we met at the portal."

show bryce stern with dissolve

Br "We do as well, and you can believe that."
c "How was Maverick even allowed to intercept his letter and read it?"
Br "He could have easily done so since he was in charge of Reza and everything, but he totally shouldn't have. I mean, we wouldn't do anything of the sort with you. Everything he has done in regard to Reza has been a poor show of character."
c "I suppose so..."

show bryce normal with dissolve

Br "In any case, thanks for telling me all of this. You never know when this kind of information could be useful."
c "No problem."
m "Just when I thought an awkward silence might set in, Bryce spotted the waiter and didn't hesitate to speak up."

show bryce laugh with dissolve

Br "Hey, waiter, bring me another."

show bryce normal with dissolve

if beer == True:
    m "I hadn't noticed, but while I was talking, Bryce had been busy sipping on his drink. The empty bowl before him was proof of his proficiency, while I had barely touched my own drink."

else:
    m "I hadn't noticed, but while I was talking, Bryce had been busy sipping on his drink. The empty bowl before him was proof of his proficiency."

show bryce normal at right with ease
show waiter flip at left with easeinleft
play sound "fx/glasses.wav"

Wr "Here you go."

show waiter
$ renpy.pause (0.3)
hide waiter with easeoutleft
show bryce normal at center with ease

if beer == False:
    c "Maybe I should be going now."
    Br "Oh, come on and stay a little. Considering we're here already, might as well enjoy the evening, right? I mean, you don't have to, but I certainly will. Or do you need to be somewhere?"
    menu:
        "Not really. I guess I can stay for a little while.":
            Br "That's what I like to hear." 
            show bryce laugh with dissolve
            Br "Waiter, bring us another beer."
            c "Another one?"
            show bryce normal with dissolve
            Br "This one's for you, silly."
            menu:
                "Alright, then.":
                    pass
                    
                "I don't really drink, though.":
                    show bryce laugh with dissolve
                    Br "Oh, come on, just try a little. Even if you don't like beer, you haven't had one like this before."
                    menu:
                        "I'll try it just for you.":
                            show bryce smirk with dissolve
                            Br "You'll do yourself a favor."
                            
                        "[[Leave.]":
                            c "I really think I should be going."
                            show bryce laugh with dissolve
                            Br "Oh, come on. Really?"
                            scene black with fade
                            nvl clear
                            window show
                            stop music fadeout 1.0
                            n "Without another word, I got up from my seat and left." 
                            n "Luckily, I didn't have much trouble finding my way back alone. I certainly couldn't stand spending any more time with someone like Bryce." 
                            n "Needless to say, I didn't regret leaving him behind."
                            window hide
                            nvl clear
                            $ nodrinks = True
                            $ brycebar = True
                            $ brycestatus = "bad"

                            $ brycescenesfinished = 1
                            
                            $ nodrinks = True


                            if persistent.c1teetotaler == False:

                                $ persistent.c1teetotaler = True
                                
                                $ achievement.grant("Teetotaler")
                                
                                $ persistent.achievements += 1
                                
                                call syscheck from _call_syscheck_39
                                
                                play sound "fx/system.wav"
                                
                                if system == "normal":
                                
                                    s "You rejected Bryce's invitation!"
                                    
                                elif system == "advanced":

                                    s "You rejected Bryce's invitation. Whatever."
                                    
                                else:
                                    
                                    s "You rejected Bryce's invitation. Why is anyone's guess." 


                            if chapter4unplayed == False:
                            
                                jump chapter4chars
                                
                            elif chapter3unplayed == False:
                                
                                jump chapter3chars
                                
                            elif chapter2unplayed == False:
                                
                                jump chapter2chars
                                
                            else:

                                jump chapter1chars
                            
        "I'd rather just go home and read a book.":
            Br "That's a shame, but I won't stop you."
            scene black with fade
            nvl clear
            stop music fadeout 1.0
            window show
            n "Bryce respected my wishes, but staying there longer and getting drunk wasn't exactly my idea of fun." 
            n "I could certainly enjoy myself without alcohol and those who partook in its consumption." 
            n "After all, there were still plenty of interesting novels waiting for me in my apartment."
            window hide
            nvl clear
            $ nodrinks = True
            $ brycebar = True
            $ brycestatus = "bad"
            
            $ brycescenesfinished = 1
            
            if persistent.c1teetotaler == False:

                $ persistent.c1teetotaler = True
                
                $ achievement.grant("Teetotaler")
                
                $ persistent.achievements += 1
                
                call syscheck from _call_syscheck_40
                
                play sound "fx/system.wav"
                
                if system == "normal":
                
                    s "You rejected Bryce's invitation!"
                    
                elif system == "advanced":

                    s "You rejected Bryce's invitation. Whatever."
                    
                else:
                    
                    s "You rejected Bryce's invitation. Why is anyone's guess." 
            
            
            
            if chapter4unplayed == False:
                    
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars
            
else:
    m "Bryce was just about to start on his second when he suddenly spoke up."
    
show bryce smirk with dissolve

Br "You know what, why don't we have ourselves a drinking contest?" 

menu:
    "I would, but I don't think I can beat someone like you.":
        Br "How about a handicap, then? I'll go easy on you."
        c "You're not letting this go, are you?"
        show bryce normal with dissolve
        Br "Just having fun."
        show bryce stern with dissolve
        Br "Alright, let's do this."
        play sound "fx/gulping.wav"
        m "Bryce lowered his snout and gulped down beer at an inhuman rate. The bowl drained rapidly and was empty in an instant."
        stop sound fadeout 1.0
        Br "Fair's fair."
        
    "I'm in.":
        $ renpy.pause (0.5)
        show bryce laugh with dissolve
        Br "That's what I like to hear."
        
    "[[Leave.]":
        c "No, thanks. I'm not interested."
        show bryce laugh with dissolve
        Br "C'mon, it'll be fun."
        c "No way. I'm leaving."
        scene black with fade
        nvl clear
        stop music fadeout 1.0
        window show
        n "Despite Bryce's further protests, I simply got up and left." 
        n "Drinking contests weren't exactly my idea of fun, and if he didn't want to do anything else, he should have found another drinking buddy." 
        n "I knew I could do without him, at any rate." 
        window hide
        $ nodrinks = True
        $ brycebar = True
        $ brycestatus = "bad"
        
        $ brycescenesfinished = 1
        
        if persistent.c1teetotaler == False:

            $ persistent.c1teetotaler = True
            
            $ achievement.grant("Teetotaler")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_41
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You rejected Bryce's invitation!"
                
            elif system == "advanced":

                s "You rejected Bryce's invitation. Whatever."
                
            else:
                
                s "You rejected Bryce's invitation. Why is anyone's guess." 
        
        
        
        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
        
c "(Considering they don't even have cars, at least I won't have to worry about drinking and driving.)"

show bryce normal with dissolve

Br "The rules are simple. We both get a round, then we wait a few moments until the next one so the effects can kick in. Whoever gives up first loses."

menu:
    "That sounds easy enough.":
        $ renpy.pause (0.5)
        show bryce laugh with dissolve
        Br "Sure, just wait until you have a swig of the real stuff and we'll see how easy it is for you."

    "Let's burn some brain cells.":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce smirk with dissolve
        Br "And may whoever burns more win. This is the true game of kings, I'm telling you."
        
    "That's your mistake. I never give up.":
        $ brycemood -= 1
        $ renpy.pause (0.5)
        show bryce brow with dissolve
        Br "We'll see about that."

stop music fadeout 1.0
show bryce stern with dissolve
Br "Alright, let's do this."
play music "mx/archaic.ogg"

play sound "fx/gulping.wav"

m "He made a show of looking me in the eyes while he lowered his muzzle into the bowl before he started guzzling his drink noisily. It was gone in seconds. Certainly, this was going to be tough."

stop sound fadeout 1.0

m "My confidence faltered, but there was no turning back now. How did I think I could win in a drinking contest against a frickin' dragon?" 

play sound "fx/gulp2.wav"

m "Nevertheless, I grasped the drink, putting on the best show I could while I tried to recreate Bryce's feat. After the first sip, however, I realized it was very different from any other beer I had tried before, yet I persevered through the intense taste until the glass was empty." 

stop sound fadeout 1.0

m "I probably wasn't as impressive as Bryce had been just moments earlier, but I couldn't afford to show any weakness. My plan was cut short, though, as I set down the glass and an unusually strong aftertaste hit me, causing me to make a face."

show bryce smirk with dissolve

Br "How'd you like it?"
c "Ugh, this is some really strong stuff."

show bryce normal with dissolve

Br "I told ya. You better know beforehand how much you can take, or it'll hit you harder later on. Wanna give up already?"

menu:
    "Heck, no.":
        $ renpy.pause (0.5)
        show bryce smirk with dissolve
        Br "As you wish."

    "S-Shut up!":
        $ renpy.pause (0.5)
        show bryce laugh with dissolve
        Br "That brought out your fighting spirit, huh? I like that."
    
    "[[Give up.]":
        c "Yeah, I can't stand another drink of this. You win."
        show bryce brow with dissolve
        Br "You can't be serious. You give up already? That's not even a competition, it's laughable."
        c "Laugh all you want, I don't care."
        show bryce laugh with dissolve
        Br "If you can't take it, just get out."
        scene black with fade
        nvl clear
        stop music fadeout 1.0
        window show
        n "And get out, I did." 
        n "There was no point in staying if the only thing he planned to do was taunt me over his victory, even though it didn't look like he enjoyed it much." 
        n "I played his silly game and somehow, he still wasn't happy about it." 
        n "Guess he could play it without me in the future."                    
        window hide
        nvl clear
        $ nodrinks = True
        $ brycestatus = "bad"
        
        $ brycescenesfinished = 1
        
        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
                            

c "So, when's the next round starting?"

show bryce normal with dissolve

Br "Soon enough. Do you feel it? Do you feel the buzz kicking in already?"
c "Err..." 

show bryce smirk with dissolve

Br "Don't lie to me. I can see it in your face. Unless that's blushing I see and not the alcohol."

menu:
    "That's not a blush!":
        $ renpy.pause (0.5)
        show bryce laugh with dissolve
        Br "I'm sure it isn't."

    "Alright, it's a buzz.":
        $ brycemood -= 1
        $ renpy.pause (0.5)
        show bryce brow with dissolve
        Br "That's what I thought."
        
    "I'm not buzzed.":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce flirty with dissolve
        Br "Is that so?"

scene bareblur
show bryce normal 
with dissolve
        
Br "Anyways, how do you like it here so far? I mean, compared to wherever it is that you came from."

menu:
    "I'm having a drinking contest with a dragon. How could I not love this?":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce smirk with dissolve
        Br "We'll see how much you like it when I've drunk you under the table."
         
    "It's alright. Certainly a nice change from what I'm used to.":
        Br "Good to hear. Maybe next time we'll send a dragon over to your world." 
        c "That could be... interesting."
        
    "To be honest, I think I'd rather be home.":
        $ brycemood -= 1
        $ renpy.pause (0.5)
        show bryce brow with dissolve
        Br "Can't fault you for that. Home is where the heart is, after all."
        
show bryce laugh with dissolve

Br "Waiter, bring us another round."

show bryce normal with dissolve

Wr "Coming right up."

show bryce normal at right with ease
show waiter flip at left with easeinleft

play sound "fx/2glasses.wav"

Wr "Here you go. Having ourselves a little contest, are we?"

show bryce laugh with dissolve

Br "You know how it goes."
Wr "That I do."
Wr "Be careful, [player_name]. He's a pro."

$ renpy.pause (0.2)
show waiter
$ renpy.pause (0.3)
hide waiter with easeoutleft

$ renpy.pause (0.8)

show xith normal flip at Position (xpos = 0.165) with easeinleft

$ renpy.pause (0.2)

Xi "Did I hear something about a contest?"

Br smirk "Maybe."

Xi "Up to your old shenanigans, I see."

Br laugh "Now, don't spoil the fun. I don't go around telling people about what you're up to, either."

Xi "Point taken. Enjoy!"

$ renpy.pause (0.2)

show xith normal

$ renpy.pause (0.3)

hide xith with easeoutleft

$ renpy.pause (0.2)

show bryce normal with dissolve

show bryce at center with ease

c "(Of course he wouldn't have challenged me if he wasn't confident he would win. Guess I'll just have to try my best.)"
Br "I went first last time, so it's your turn now."

play sound "fx/gulp2.wav"

m "As I put the glass to my lips and started swallowing the dark amber liquid, I was struck by how much more difficult this round was compared to the first." 
m "One thing that always puzzled me about seasoned drinkers was the sheer amount of liquid they could ingest without issue. Keeping it down, however, was a much different question." 
m "But this contest wasn't about keeping it down."
        
play sound "fx/glassdown.wav"

c "There. Your... turn."

show bryce smirk with dissolve

Br "Did I see you struggling there for a second?"

menu:
    "Let's see how you do.":
        Br "I've had much more than this before."

    "That's my tactic, make you think that I'm struggling so you'll let your guard down.":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce laugh with dissolve
        play sound "fx/tableslap.wav"
        m "Roaring laughter erupted from the dragon as his paw struck the table, rattling the containers resting on it."
        Br "Keep it up, kiddo. You still stand a chance if you can make me die of laughter." 
        
    "I may have underestimated this...":
        Br "You can always give up."
        
Br "As for my turn, let me demonstrate."

show bryce normal with dissolve

play sound "fx/gulpslow.wav"

m "Once again, he consumed his drink, though his swigs were noticeably slower than before. His resolve was also fading, though not as fast as mine had, as he clearly held the advantage. Was there any way I could still turn this around?"

stop sound fadeout 1.0

scene black with dissolve

$ double_vision_on("bareblur")

show bryce smirk with dissolve

Br "There."

show bryce normal with dissolve

Br "Now, let me ask you a question: I know you wanted to tell me all the stuff about Reza, but was that the only reason you wanted to meet with me?"

menu:
    "It was.":
        $ renpy.pause (0.5)
        show bryce smirk with dissolve
        Br "Guess you got more outta this than you asked for, then."
        
    "Well, it doesn't hurt to have friends in high places.":
        $ brycemood -= 2
        $ renpy.pause (0.5)
        show bryce stern with dissolve
        Br "I see."
        
    "Maybe. Having a lil' fun doesn't hurt, right?":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce flirty with dissolve
        Br "Thought so. I won't disagree with that."

show bryce laugh with dissolve

Br "Waiter, next round."

show bryce normal with dissolve

Wr "Coming."

show bryce normal at right with ease
show waiter flip at left with easeinleft

play sound "fx/2glasses.wav"

Wr "There you go."
Br "Thanks."
Wr "How are you holding up?"
c "Just fine, thanks for asking."
Wr "If you say so. Good luck."

show waiter 
$ renpy.pause (0.3)
hide waiter with easeoutleft
show bryce normal at center with ease
show bryce brow with dissolve

Br "Was it your turn... or is it my turn?"

c "It's yours."

show bryce stern with dissolve

Br "Alright."

play sound "fx/gulpslow2.wav"

m "By now it was obvious that Bryce was faltering, though he still was faring much better than I was. He even had to take a break in the middle of his beer, unable to down it in one go."

show bryce smirk with dissolve

stop sound fadeout 1.0

Br "Now... it's yours."

show bryce normal with dissolve

m "He was a lot heavier than me, and even though his bowls held far more liquid than my glasses, how did I think I'd stand a chance against him? When I picked up my glass, I didn't have feeling in my fingers anymore."

play sound "fx/gulp3.wav"

m "I had to pause a few times, but in the end I made it, though I wasn't sure how much more I could take."

play sound "fx/glassdown.wav"

c "S-So, w-what... do we do now?"

show bryce smirk with dissolve

Br "Wait for you to... t-throw up so I win?"

menu:
    "Y-You never said that was a rule.":
        $ renpy.pause (0.5)
        show bryce brow with dissolve
        Br "Well, duh... Of course it doesn't count if you spit out your drink halfway through." 
        show bryce smirk with dissolve
        Br "I suppose it still might if you... lick it all up again."

    "You... wish.":
        Br "I can see you're close. Just a question of time now, sonny."
    
    "M-Might as well do that now...":
        $ brycemood -= 1
        $ renpy.pause (0.5)
        show bryce stern with dissolve
        Br "Just... don't..."

scene black with dissolve
$ double_vision_on("bareblur2")
show bryce normal at center with dissolve

c "C-Can I... ask you a question?"
Br "Go ahead."

menu:
    "Why are you... brown?":
        $ renpy.pause (0.5)
        show bryce brow with dissolve
        Br "Dammit, you don't just ask someone why they're brown! Don't you have... like... differently colored people where you come from? Or do they all look like you?"
        c "You... seriously look like a chocolate cream cake... delicious chocolate cream cake. Can I taste you?"
        
    "Why are you so damn attractive?":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce flirty with dissolve
        Br "I just am... Got nothing more to say 'bout that."
        
    "[[Say nothing.]":
        $ brycemood -= 1
        c "..."
        show bryce stern with dissolve
        Br "Are you still there?"
        c "Yah."
        
show bryce laugh with dissolve

Br "Waiter... next round."
show bryce normal with dissolve

show bryce normal at right with ease
show waiter flip at left with easeinleft
play sound "fx/2glasses.wav"

Wr "There you are."

show waiter
$ renpy.pause (0.3)
hide waiter with easeoutleft
show bryce normal at center with ease

show bryce brow with dissolve

m "Blearily, the dragon looked at me, seemingly unable to focus. I could see he was hitting his limit, but so was I. Maybe, if I just held out a little longer..."
Br "Whose turn is it even?"

menu:
    "I think... it's yours.":
        $ brycemood -= 1
        $ renpy.pause (0.5)
        show bryce stern with dissolve
        Br "I think... it's yours, though..." 
        c "Very well."

    "Mine.":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce smirk with dissolve
        Br "Good."
        
    "I don't even know anymore.":
        $ renpy.pause (0.5)
        show bryce normal with dissolve
        Br "I'm positive it's yours."
        c "Very well."


play sound "fx/gulp4.wav"

m "At this point, I had difficulties picking up my glass. I was about to give up, but I was sure if I held on just one more round it'd be over. I could still win this. I had to wait a few moments after each sip in order to continue, but I did not give up until, eventually, the glass was empty."

play sound "fx/glassdown.wav"
menu:
    "Your... move, \"Chief\".":
        pass
        
    "S-Suck on this, you ssscaly bastard.":
        pass
        
    "[[Say nothing.]":
        pass
        
$ renpy.pause (0.5)
show bryce stern with dissolve

m "For the first time, I could see something in his eyes other than his always present confidence. Was it disbelief, or insecurity? I guessed my feat caught him off guard, as he seemed genuinely impressed. If nothing else, this showed me that even his own conviction was cracking now. I could totally win this."
Br "You're cute... I like you, I really do, but I sure as heck am not going to let you win."

play sound "fx/gulpslow3.wav"

m "He was struggling. It became more and more obvious as he tried to swallow the liquid in his bowl bit by bit. He stopped at one point, panting heavily. I considered taking a cheap shot at him, but as he had refrained from doing so during my turn, I wasn't going to start now."

stop sound fadeout 1.0

Br "There."

scene black with dissolve
$ double_vision_on("bareblur2")
show bryce stern at center with dissolve

m "I was getting tired. I could hear Bryce's voice, but I could not make out the individual words anymore. I decided to rest my eyes, just for a little bit..."      

stop music fadeout 1.0
scene black with dissolve
play sound "fx/impact.wav"
$ renpy.pause(4.5)

scene bareblur2
show bryce stern at center
with dissolveslow

Br "Hey, are you okay? You fell down, and you look kinda messed up."

scene black with dissolve
$ double_vision_on("bareblur2")
show bryce stern at center with dissolve

menu:
    "Yeah.":
        $ renpy.pause (0.5)
        show bryce normal with dissolve
        Br "Good to hear that."
        
    "I'll mess you up if you don't get your face outta my face.":
        $ brycemood -= 1
        $ renpy.pause (0.5)
        show bryce brow with dissolve
        Br "Sheesh, sorry for asking."
        show bryce normal with dissolve
        
    "If you think I'm giving up, you're mistaken. This isn't over.":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce laugh with dissolve
        Br "I can see that."
        show bryce normal with dissolve


Br "Ready for another round? Or do you give up?"

menu:
    "Bring... it ON!":
        $ brycemood -= 1
        $ renpy.pause (0.5)
        show bryce stern with dissolve
        Br "Actually, you know... once you're lying on the ground, you better stop."
        c "Does that mean I win?" 
        show bryce brow with dissolve
        Br "I didn't say that."

    "I think... I better stop here.":
        $ renpy.pause (0.5)
        show bryce smirk with dissolve
        Br "Guess I'll just have another to secure my victory, then."

    "I know when I've had enough, and it's now.":
        $ brycemood += 1
        $ renpy.pause (0.5)
        show bryce laugh with dissolve
        Br "Well done, kiddo. Didn't think you had it in you."

show bryce normal with dissolve
show bryce normal at right with ease
show waiter flip at left with easeinleft

Wr "You know, it was fun watching you and all, but you've both had enough for the evening. I think you'd better leave now. After you've come out from under the table, that is."

scene black with dissolve
$ double_vision_on("bareblur2")
show waiter flip at left with dissolve

c "Alright. I'll be going, then."
Wr "Wait a minute."
c "What... is it?"
Wr "Maybe you should go with him, just to make sure he gets home safely and doesn't do anything stupid, you know? It's kind of an unspoken rule here that whoever is his drinking buddy does so." 
m "When I looked over to him, I discovered that Bryce had passed out for the moment. This could prove difficult."

menu:
    "Fine...":
        $ brycemood += 1
        Wr "Thank you."
        
    "If I have to...":
        Wr "You'll be doing yourself a favor, too."
        
    "[[Leave.]":
        c "Heck, no."
        Wr "That's not very nice of you."
        c "Get outta my way, you scaly sack, before I show you how nice I can be... with my fists!"
        scene black with fade
        nvl clear
        window show
        n "Without looking back, I got up and stumbled back to my apartment on shaky legs." 
        n "When I finally arrived, I was glad to fall into bed and sleep away the whole evening."
        window hide
        nvl clear
        $ leftbryce = True
        $ brycestatus = "bad"
        
        $ brycescenesfinished = 1
        
        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars

show waiter
$ renpy.pause (0.3)
hide waiter with easeoutleft
c "Come on, let's get you home."
c "(He is still unconscious.)"
menu:
    "Dump some water on his face.":
        c "This should do the trick."
        play sound "fx/splash.wav"
        $ renpy.pause (2.0)
        show bryce brow with dissolve
        Br "Wha? 's that you, [player_name]? Where am I?" 
        c "Still in the bar. Come on, let's get you home."
        
    "Slap him.":
        $ brycemood -= 1
        play sound "fx/slap1.wav"
        $ renpy.pause (0.5)
        c "Wake up. Wake up. Wake uuuuuuup!" 
        show bryce brow with dissolve
        Br "What? Is that you, [player_name]?"
        play sound "fx/slap2.wav"
        $ renpy.pause (0.5)
        show bryce laugh with dissolve
        Br "Stop it! I'm awake already."
        c "Sorry."
        show bryce brow with dissolve
        Br "Where am I?"  
        c "Still in the bar." 
        show bryce stern with dissolve
        Br "Ugh..." 
        c "Come on. Let's get you home, you big wuss."

    "Put some pepper on his nose.":
        $ brycemood += 1
        c "(Right, it'll be like a smelling salt.)"
        play sound "fx/salt.ogg"
        $ renpy.pause (1.5)
        c "(Huh... that was actually the salt, not the pepper. Let's try that again.)"
        play sound "fx/salt.ogg"
        $ renpy.pause (2.0)
        show bryce brow with dissolve
        Br "What? Is that you, [player_name]? Where am I?"
        play sound "fx/sniff.ogg"
        $ renpy.pause (1.0)
        Br "And what did you do to my nose? Did you shove something in there while I was out or something?"
        c "We're still in the bar. And I just put some pepper there to wake you up."
        Br "That's the best you could come up with?"
        c "I'm drunk, what'd you expect?"
        Br "Oh, shut up."    
        c "Come on. Let's get you home, you big wuss."

scene black with fade
$ renpy.pause (1.5)
scene pad at Pan ((0, 0), (0,360), 5.0) with dissolveslow
play music "mx/campfire.ogg" fadein 2.0
m "I awoke looking at an unfamiliar ceiling. For a moment, I wondered where I was before the events of last night all came back to me. As I got up and looked around, I realized that I'd apparently slept on the floor."
c "(Where am I? This isn't my apartment.)"

show black with dissolve
$ renpy.pause (0.5)
show cgbryce with dissolvemed
$ renpy.pause(2.0)

c "(Guess I must have passed out after I got Bryce home.)"
c "Hey, Bryce."

menu:
    "You are salivating.":
        m "The dragon moved and let out a groan before he opened his eyes."
        hide cgbryce 
        hide black
        with fade
        show bryce brow with dissolve
        Br "Just as you do, occasionally, I bet."

    "Wake up, fattie.":
        $ brycemood -= 1
        m "The dragon moved and let out a groan before he opened his eyes."
        hide cgbryce 
        hide black
        with fade
        show bryce stern with dissolve
        c "(That got him.)"
        Br "For your information, my kind does tend to look a little bigger than the others, but it also makes us the strongest." 
        show bryce brow with dissolve

    "Good morning, sunshine.":
        $ brycemood += 1
        m "The dragon moved and let out a groan before he opened his eyes."
        hide cgbryce 
        hide black
        with fade
        show bryce brow with dissolve

Br "Daaamn, my head. Why are you even here?"
c "I guess I must have passed out after I escorted you home."

show bryce laugh with dissolve

Br "Oh right, after our little game."
c "Do you remember who won?"

show bryce normal with dissolve

Br "I don't even know, but you stood your ground and I respect that."

show bryce brow with dissolve

Br "You didn't do anything funny while I was out, did you?"

$ mp.teetotaler = False
$ mp.save()

m "The dragon rose from the couch with a nice morning stretch, rubbed his eyes, then held his head high as he let out a grunt and a big yawn."

if brycemood <= 0:
    show bryce stern with dissolve
    Br "That whole contest was stupid."
    c "Well, it was your idea."
    show bryce brow with dissolve
    Br "At least I knew when to stop."
    c "At least it's not like you were egging me on the whole time. Wait, actually, that is exactly what happened."
    show bryce stern with dissolve
    Br "No, you are right. This was a bad idea all around."
    c "That's easy to say after the fact."
    show bryce brow with dissolve
    Br "Yeah, and I clearly held you there against your will and made you drink too, right?"
    c "You may as well have. You know, as an ambassador, I can't really say no to a social meeting with the chief of police."
    Br "So when it's not my fault, it's your job's fault. That's just brilliant, it's everyone's fault but your own. Well done, [player_name]." 
    show bryce stern with dissolve    
    Br "You know what, maybe you should be leaving about now."
    c "Yeah, I guess I should."
    play sound "fx/door/doorclose3.wav"
    scene black with dissolve
    stop music fadeout 1.0

    $ brycestatus = "bad"
    
    $ brycescenesfinished = 1
    
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars

elif brycemood <= 7:
    label bryce1skip:
    show bryce stern with dissolve
    Br "Alright, you know what? I'm sorry. The whole contest thing was a stupid idea and I shouldn't have suggested it, especially not to you."
    c "Well, it's not like you forced me to participate, so I suppose I share some of the blame..."
    show bryce normal with dissolve
    Br "Let's just pretend the whole thing never happened."
    c "Deal."
    show bryce brow with dissolve
    Br "Wait... what time is it?"
    c "Ugh..."
    Br "Damn, I should really get going, or I'll be late for work. You know how to get back to your apartment from here, right?"
    c "I think so."
    show bryce normal with dissolve
    Br "Guess you should be going as well, kiddo. Maybe I'll see you some other time."
    stop music fadeout 1.0

    $ brycestatus = "neutral"
    
    $ brycescenesfinished = 1
    
    $ persistent.bryce1skip = True
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars

else:
    show bryce stern with dissolve
    Br "Alright, you know what? I'm sorry. The whole contest thing was a stupid idea and I shouldn't have suggested it, especially not to you."
    c "Well, it's not like you forced me to participate, so I suppose I share some of the blame..."
    show bryce normal with dissolve
    Br "Let's just pretend the whole thing never happened."
    c "Deal."
    show bryce laugh with dissolve
    Br "Maybe I'll invite you over some other time and show you that there's more to the chief of police than getting drunk and passing out?"
    c "But how are we going to find out who won if we aren't going to have a rematch?"
    show bryce flirty with dissolve
    Br "Heh, I'm sure we'll think of something else that could measure our endurance."
    $ renpy.pause (0.5)
    stop music fadeout 2.0

    $ brycestatus = "good"
    
    $ brycescenesfinished = 1
    
    $ persistent.bryce1skip = True
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars


      
      
#hide blur_image with dissolve










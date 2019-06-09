#-12 +16
label anna1:
    
$ chapter1csplayed += 1
$ anna1unplayed = False
$ persistent.playedanna1 = True
$ anna1played = True
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Anna 1"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Anna 1"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Anna 1"
    
else:

    $ save_name = "Chapter 1 - Anna 1"

scene black with fade
$ renpy.pause (1.0)
scene facin2 at Pan ((0, 200), (128, 200), 3.0) with dissolveslow

play music "mx/jazzy2.ogg"
c "(She told me to meet her here, so she's got to be around somewhere.)"
m "The production facility had many different wings, covering everything from research to processing, in addition to production. It was easy to get lost if you didn't know where you were going."

##skip here if remy is dead

if remydead == False:

    m "I heard some commotion in the distance, and when I approached, I was surprised to see not only Anna, but Remy as well." 
    m "They seemed to be in the middle of a heated conversation. I thought it would be inappropriate to approach now, so I remained several paces back, out of their field of vision, but still close enough to be able to make out their words."

    show anna normal b flip at left with dissolve
    show remy look at right with dissolve

    Ry "We have heard the rumors."

    show anna disgust b flip with dissolve

    An "So you come to me on the basis of rumors? Is that how you operate? What do you want from me?"
    Ry "This is not the first time you've been in trouble, you know. They might not be so lenient with you this time."

    show anna sad b flip with dissolve

    An "I don't know what you are talking about."
    Ry "Consider this a warning. You should proceed carefully, for your own good."

    show anna normal b flip with dissolve

    An "If you wanted to threaten me, the least you could have done was to send someone more intimidating. You may be larger than I am, but even I can see that you're just a big coward. You wouldn't dare to put your dirty claws on me." 

    show remy shy with dissolve

    Ry "I wouldn't. I'm here as a courtesy to you, not to threaten or intimidate. Do with that information whatever you wish." 

    show remy look with dissolve

    Ry "You know we'll be back, and if they find anything, there will be consequences."
    An "Do you think I care?"

    show remy sad with dissolve

    Ry "This attitude of yours is not helpful."

    show anna face b flip with dissolve

    An "Neither are you."

    show remy look with dissolve

    Ry "Well, I've said what I came here to say. Good luck."

    show anna sad b flip with dissolve

    An "Whatever."

    show remy look flip
    $ renpy.pause (0.3)
    hide remy look flip with easeoutright

    m "Remy turned to leave and started walking in my direction. I ducked behind a pillar, and when he went past, I wasn't sure if he'd seen me. Either way, he left, and I was safe to approach now."

$ annamood = 0
$ annaanswers = 0

## end indent for if remy is dead

#insert skip here
if persistent.anna1skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_35

    call skiptut from _call_skiptut_7
        
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
            
            show black with dissolvemed
            
            $ renpy.pause (1.0)

            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_7
            
            scene cafe 
            show anna normal flip
            with dissolvemed
                        
            play music "mx/jazzy2.ogg" fadein 1.0
            
            jump anna1skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/jazzy2.ogg"


if remydead == False:

    menu:
        "What was that all about?":
            $ annamood -= 1
            $ renpy.pause (0.5)
            show anna face b flip with dissolve
            An "Who cares?"
            
        "Hey, Anna.":
            $ annamood += 1
            $ renpy.pause (0.5)
            show anna face b flip with dissolve
            An "Hey, [player_name]."

        "Hellooo.":
            $ renpy.pause (0.5)
            show anna face b flip with dissolve
            An "Hey."
            
    show anna sad b flip with dissolve

    An "Wait, how long have you been here?"

    menu:
        "I saw everything.":
            pass
            
        "Not very long.":
            pass
            
    $ renpy.pause (0.5)
    show anna face b flip with dissolve        
            
    An "Not that it matters much anyway. This is just par for the course for me."
    c "I know Remy. What's the problem?"

    show anna disgust b flip with dissolve

    An "The nerve of that guy. He probably wouldn't be so uptight if it wasn't for that thing with his girlfriend a few years ago." 

    show anna sad b flip with dissolve

    An "But I don't care about him. It's his superiors that are the problem. They don't like me and the research I'm doing. They cite their traditions and values, claiming that those are what have kept us alive for so long." 

    show anna normal b flip with dissolve

    An "If anything were to change, it would obviously fracture the base this society is built on, cause it all to collapse, tear apart families and allow all hell to break lose." 

    show anna sad b flip with dissolve

    An "At least if you believe those old-timers who keep repeating these phrases." 

    show anna face b flip with dissolve

    An "And all that nonsense, because of my research. Valuable research that could save lives, mind you." 
    c "What kind of research are we talking about?"

    show anna normal b flip with dissolve

    An "I could show you sometime, but we're here to have fun, right?"
    c "I thought you wanted to show me, since you said we were both in biology and all that."

    An "Sure, but after doing this all day, you'll have to excuse me for not wanting to talk about it even more." 

    show anna sad b flip with dissolve

    An "Wasting my time with that guy was just another setback, not that I don't already have more than enough work to do. Even right now I'm supposed to be working overtime."

else:

    show anna sad b flip at left with dissolve
    
    menu:
            
        "Hey, Anna.":
            $ annamood += 1
            $ renpy.pause (0.5)
            show anna face b flip with dissolve
            An "Hey, [player_name]."

        "Hellooo.":
            $ renpy.pause (0.5)
            show anna face b flip with dissolve
            An "Hey."
            
    c "Is something wrong? You don't look great."
    
    show anna sad b flip with dissolve

    An "It's nothing, really. Just the usual stress that comes with the job. Even right now I'm supposed to be working overtime."
    
    c "I see. What do you actually do here?"

    show anna normal b flip with dissolve

    An "I could show you sometime, but we're here to have fun, right?"
    
    c "I thought you wanted to show me, since you said we were both in biology and all that."

    show anna sad b flip with dissolve

    An "Sure, but after doing this all day, you'll have to excuse me for not wanting to talk about it even more."
    
    

menu:
    "Guess you can give me the tour some other time, then.":
        $ renpy.pause (0.5)
        show anna normal b flip with dissolve
        An "I will."
        
    "How disappointing.":
        $ annamood -= 1
        $ renpy.pause (0.5)
        show anna disgust b flip with dissolve
        An "Yeah, I'm very sorry we can't accommodate your request right now, your highness."
        show anna normal b flip with dissolve
        
    "I see.":
        $ annamood += 1
        $ renpy.pause (0.5)
        show anna normal b flip with dissolve
        An "Good to know we see eye to eye on this."

if blood == True:
    An "Oh, and thanks for the blood, by the way. The results aren't in yet, but I'll let you know when they are."
    c "Good. I'm just as curious about the results as you are."
    show anna smirk b flip with dissolve
    An "No, you aren't."
    c "I am. I am way curiouser than you are."
    show anna sad b flip with dissolve
    An "Curiouser? Is that even a word?"
    c "It is, since an author popularized its use where I came from."
    show anna normal b flip with dissolve
    An "Then I am way more curiouser than you are."
    c "Not if I am the curiousest."
    show anna face b flip with dissolve
    An "Excuse me for a moment, but I must weep for the English language. At this rate, why don't you just say you're the \"most curiouserest\"?"
    c "I'm not sure, I am not a linguist. Are you?"  
    show anna normal b flip with dissolve
    An "Not exactly, but I have a way with words. My tongue is quite skilled, or so I hear." 
    show anna smirk b flip with dissolve
    An "Some might even say \"cunning\"."
    show anna normal b flip with dissolve
    
else:
    pass
    
c "In any case, if you have to work overtime today, does that mean I should wait for you, or do you want me to come back another time?"
An "Neither, I think my break should start right about... now."

menu:
    "What a lucky coincidence.":
        $ annamood += 1
        $ renpy.pause (0.5)
        show anna smirk b flip with dissolve
        An "It is, isn't it?"
        show anna normal b flip with dissolve
        
    "I hope no one notices your unscheduled break.":
        $ annamood -= 1
        $ renpy.pause (0.5)
        show anna sad b flip with dissolve
        An "As long as you don't rat me out, that shouldn't be a problem."
        show anna normal b flip with dissolve
        
    "I wish I had the ability to make breaks happen at my convenience.":
        An "Just one of the perks of being the manager of this facility."
    
c "So, where are we going?"

show anna smirk b flip with dissolve

An "I don't know where you are going, but I think I need a coffee or five. You can tag along if you like."

menu:
    "It would be my pleasure.":
        $ annamood += 1
        $ renpy.pause (0.5)
        show anna normal b flip with dissolve
        An "We'll see if it'll be mine as well."

    "I think I'd rather not.":
        $ renpy.pause (0.5)
        show anna normal b flip with dissolve
        An "Suit yourself."
        show anna normal b
        $ renpy.pause(0.3)
        hide anna with easeoutleft
        $ renpy.pause(1.0)
        nvl clear
        stop music fadeout 1.0
        window show
        n "Whatever the reason, I decided not to join her in her glorious quest for coffee." 
        n "I wasn't sure whether I would regret the choice I made in the times to come, but in the end, it is what I had to do."
        window hide
        
        $ annastatus = "bad"
        
        $ annascenesfinished = 1

        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
        
    "Sure, why not.":
        $ renpy.pause (0.5)
        show anna sad b flip with dissolve
        An "Now that's a convincing reason."
        show anna normal b flip with dissolve
        
An "I hope you brought your own money, though, because I'm not sharing."
c "I didn't, but everything I purchase is taken care of by my ambassador status."

show anna smirk b flip with dissolve

An "Nice. Actually, that opens up some very interesting possibilities." 
c "It might, but I'd rather not do anything too fishy. I don't want to raise any suspicion, you know." 

show anna sad b flip with dissolve

An "Good point."

show anna normal b flip with dissolve

An "Well, let's go then."

c "After you, milady."

show anna normal b
$ renpy.pause(0.3)
hide anna with easeoutleft

play sound "fx/steps/clean2.wav"

scene black with fade
$ renpy.pause (1.0)
scene cafe with dissolvemed

c "There we are."

play sound "fx/chair.wav"
$ renpy.pause(1.2)

show anna normal flip at left with dissolve

An "Finally. I can't wait to get some coffee into my system."

show adine normal b at right with easeinright

Ad "Oh, hello [player_name]. Nice to see you again."
c "Hey."
Ad "Who's your companion?"

show anna face flip with dissolve

An "Can't you just take my order?"

show adine annoyed b with dissolve

Ad "I apologize. Let me try that again."

show anna sad flip with dissolve

show adine giggle b with dissolve

Ad "Welcome to our establishment. My name's Adine, and I'll be your waitress today. What can I bring you two?"

An "I'll have a coffee."

show adine normal b with dissolve

Ad "Thank you. And what can I bring the esteemed gentleperson on the other side of the table?"

menu:
    "I'll also take a coffee, please.":
        $ annamood += 1
        
    "Just a soda.":
        pass
        
    "Bring me a beer.":

        $ mp.teetotaler = False
        $ mp.save()
        $ annamood -= 1

Ad "No problem, I'll be right back."

show adine normal b flip
$ renpy.pause(0.3)
hide adine with easeoutright

show anna disgust flip with dissolve

An "What's her problem? I'm here to order something, not to chit-chat with the employees."

menu:
    "I think she was just trying to be friendly.":
        $ renpy.pause (0.5)
        show anna face flip with dissolve
        An "I guess I'm not a fan of \"friendly\", then."
        show anna sad flip with dissolve
        
    "I know her, it's fine.":
        $ annamood -= 1 
        $ renpy.pause (0.5)
        show anna sad flip with dissolve
        An "If you say so."

    "I know, she can be pretty annoying.":
        $ annamood += 1
        $ renpy.pause (0.5)
        show anna normal flip with dissolve
        An "I can see that."
        
show adine normal b at right with easeinright

$ renpy.pause(0.6)
play sound "fx/dishes.wav"

Ad "Here you go. Enjoy."

stop sound fadeout 1.0

show adine normal b flip
$ renpy.pause(0.3)
hide adine with easeoutright

scene black with fade

play sound "fx/coffee.wav"
$ renpy.pause(2.5)

scene cafe
show anna normal flip at left
with dissolve

An "Ah, I totally needed that."
c "So, you work in that facility."
An "And your point is?"
c "What's your job there? I mean, what do you do, exactly?"
An "We do all kinds of things. The truth is, we just have all kinds of specialized machinery there which is used by many different people for many different purposes. The building is owned and run by the council, who oversees the schedule."

show anna sad flip with dissolve

An "It is quite handy, since you can go from research, to testing and even manufacturing, all in the same complex."

show anna normal flip with dissolve

An "I started out as a researcher in biology, which is still my main job, but I've been there so long and learned the ins and outs of the building so well that eventually I was asked to take over some  managerial duties."
An "Sure, it means more work, but it also allows me to run a personal project every once in a while. Does that sate your curiosity?"

menu:
    "I've only seen glimpses, but it already sounds like a fascinating place.":
        $ annamood += 1
        $ renpy.pause (0.5)
        show anna sad flip with dissolve
        An "I'm not sure I'd go so far as to call it \"fascinating\", but it surely does give me a lot of opportunities."
        show anna normal flip with dissolve
        
    "It does.":
        An "Good to know."
        
    "Not at all.":
        $ annamood -= 1
        $ renpy.pause (0.5)
        show anna sad flip with dissolve
        An "Well, that's a shame."
        show anna normal flip with dissolve
        
if blood == True:
    c "Oh, I forgot to ask you what you actually planned to do with my blood and the test results."
    
else:
    c "Out of more curiosity, when you asked me about my blood the other day, what were you actually planning on doing with it?"

show anna face flip with dissolve

An "What is this, an interrogation?"

menu:
    "I was just asking a question, that's all.":
        $ annamood -= 1
        An "Well, it's not the first."
        
    "Yes, totally. You can call your lawyer if you like.":
        $ annamood += 1
        $ renpy.pause (0.5)
        show anna smirk flip with dissolve
        An "Maybe I should. I'll tell her you hit me, then sue for damages." 
        
    "I think someone's in a bad mood.":
        $ renpy.pause (0.5)
        show anna normal flip with dissolve
        An "Then you must be talking about Adine, the prying waitress, or yourself, because you haven't seen me in a bad mood yet. Not even close."

menu:
    "Alright, I'll finish my drink quietly, then, if that's what you'd prefer.":
        $ annamood += 1
        $ renpy.pause (0.5)
        
    "Okay, I guess you don't like questions, then.":
        $ renpy.pause (0.5)
    
    "Excuuuse me, princess.":
        $ annamood -= 1
        $ renpy.pause (0.5)
        show anna face flip with dissolve
        An "..."
        
show anna sad flip with dissolve

An "Sorry, I'm just stressed from all the work lately. I'm not getting much respite between my regular work, overtime, personal projects and other disturbances like that Remy sticking his nose where it doesn't belong."
c "What do you usually do during your free time? Having a good work-life balance is very important, you know."
An "I love my job, I really do. Actually, I love it so much that even in my free time, I still do things that have to do with biology."
An "As I said, I've got the opportunity to do my own projects sometimes, so that's what I focus on when I get the chance. It would be a shame to pass up an opportunity like that without using it."
An "With the current influx of work, I rarely leave the facility if I'm not eating or sleeping. Even right now, I'm only on break and have to go back for another shift."
c "Maybe you should do something else for a change."

show anna face flip with dissolve

An "Maybe, but right now that's not really an option. It would help if the council weren't constantly sending their lackeys to mess with me."
c "So that wasn't the first time?"

show anna sad flip with dissolve

An "No, I suppose I'm on their watchlist or something."
c "Why is that?"
An "It's a long story. And not one for a first date."
c "So you're saying this is a date?"

show anna face flip with dissolve

An "No, I'm saying that even if this was a date, which would be more than whatever this is, it wouldn't be very appropriate. Stories about work aren't very romantic."
c "It's always about work with you. Come on, you're on break. Maybe we should do something to take your mind off of all that for once."

show anna sad flip with dissolve

An "Like what?"
c "I'm not sure. Do you have any other hobbies?"
An "Not really."
c "Hey, waitress."

$ renpy.pause (0.5)

show adine normal b at right with easeinright

Ad "How can I help you?"
c "Do you have anything here to entertain your guests? Any games or other distractions?"
Ad "I'm not sure, let me go check."
show adine normal b flip
$ renpy.pause(0.3)
hide adine with easeoutright

show anna sad flip with dissolve

An "What exactly are you trying to do?"

menu:
    "Anything to get you to shut up about work already.":
        $ annamood -= 1
        $ renpy.pause (0.5)
        show anna face flip with dissolve
        An "Whatever."
        
    "Just wait and you'll see.":
        An "The anticipation is killing me."
        show anna normal flip with dissolve
        An "Actually, no. It's boredom."
        
    "I'm being cute and spontaneous?":
        $ annamood += 1
        $ renpy.pause (0.5)
        show anna smirk flip with dissolve
        An "I'll remember this day. For good or bad, I'm not sure yet."
        show anna normal flip with dissolve
        
show adine normal b at right with easeinright
show adine giggle b with dissolve

Ad "It's more for the kids, but we don't really have anything else."

play sound "fx/bg.wav"

show adine normal b with dissolve

c "It's fine, thank you."

show adine giggle b with dissolve

Ad "Have fun!"

show adine giggle b flip
$ renpy.pause(0.3)
hide adine with easeoutright

show anna face flip with dissolve

An "A board game? Really?"
c "I know it's not Knizki's {i}Textile Merchant{/i}, but I suppose it's better than nothing."

show anna sad flip with dissolve

An "{i}Textile Merchant{/i}? Knizki?"
c "It's a game. Never mind."

play sound "fx/rummage.wav"
show anna face flip with dissolve

An "Well, I'm not convinced that this will accomplish anything, unless your goal is to make me regret this day."
c "It seems to be a trivia game. Do you have good general knowledge?"
An "Do you even know what kind of advanced knowledge I have to memorize and work with every single day?"

show anna smirk flip with dissolve

An "You bet I have good general knowledge. Certainly more than enough to beat a foreigner like you."
c "If you're so confident, maybe we should make a bet."

show anna normal flip with dissolve

An "What do you have in mind?"
c "Let's say if I win, I'll get to go on a real date with you." 
c "No fitting me in during your break, no complaining about everything, and no acting as if you're doing me a favor, especially because it was you who wanted to meet me in the first place."

if blood == True:
    show anna smirk flip with dissolve
    An "And if I win, I'll have you come in sometime so I can run more tests on you."
    
else:
    show anna smirk flip with dissolve
    An "And if I win, I'll have you come in sometime so I can run a few tests on you. I won't even need your blood anymore."
    
menu:
    "If that's what you want, so be it.":
        $ annamood += 1
        An "Let's do this, then."
        
    "Alright.":
        $ renpy.pause (0.5)
        
    "I cannot agree to that.":
        $ renpy.pause (0.5)
        show anna normal flip with dissolve
        An "But that's the only thing I'm interested in. You were so cocky you made a bet, but when it comes down to it, I suppose you don't have it in you."
        
        menu:
            "Sorry, but I can't sell my body for a bet.":
                show anna face flip with dissolve
                An "How disappointing. I guess this whole thing was just a waste of time, then."
                show anna normal flip with dissolve
                An "Maybe you should play your children's games with the waitress, because I've got better things to do."
                play sound "fx/chair.wav"
                $ renpy.pause(1.5)
                show anna normal
                $ renpy.pause(0.3)
                hide anna with easeoutleft
                $ renpy.pause(1.0)
                nvl clear
                stop music fadeout 1.0
                window show
                n "She simply got up and left without looking back even once."
                n "And she didn't pay for her coffee, either."
                n "She probably hadn't forgotten, but whether she just didn't care, or if it was her way of sticking it to me, I wasn't sure."
                n "I was quite sure, however, that she probably would not want to meet with me again."
                window hide

                $ annastatus = "bad"

                $ annascenesfinished = 1

                if chapter4unplayed == False:
                    
                    jump chapter4chars
                    
                elif chapter3unplayed == False:
                    
                    jump chapter3chars
                    
                elif chapter2unplayed == False:
                    
                    jump chapter2chars
                    
                else:

                    jump chapter1chars
                
            "I changed my mind, I'll do it.":
                $ renpy.pause (0.5)
                show anna smirk flip with dissolve
                An "Let's do this, then."
                
show anna normal flip with dissolve

An "Since it was your idea, it's only fair that I start. So, how does this work?"
c "It seems to be pretty simple. We take turns drawing cards and asking questions until we've both asked a number that we agree on beforehand. Whoever gets more right in the end wins."
An "How many questions shall it be, then?"
c "How about five?"
An "Let's make it three. Not sure how long this will take, and my break won't be for too long, either."
c "Alright. Go ahead, then."

play sound "fx/shuffle.ogg"

m "I saw mischief in her eyes, her stare piercing, paired with the hint of an arrogant smirk that exposed her anticipation. She seemed confident that she would win and loved every second of it."
m "Slowly, her hand went over to the deck of cards and drew the topmost."
stop music fadeout 1.0
$ renpy.pause (0.5)
play sound "fx/woosh3.ogg"
show eyes at Pan ((500, 0), (0, 0), 1.0)
show round1 at Pan ((-500, 0), (0, 0), 1.0)
show anna smirk flip

with dissolvemed

$ renpy.pause (2.0)

hide eyes
hide round1
with dissolvemed
play music "mx/jazzy2.ogg" fadein 1.0
An "Who is cited as one of our most important historians, his work spanning over 20 books, credited with mapping out our entire history since the beginning of sentience?"

menu:
    "Haziq Aakil":
        $ annaanswers += 1
        $ renpy.pause (0.5)
        show anna face flip with dissolve
        An "How could you even know something like that? You have only been here for what, a few days?"
        menu:
            "Maybe you shouldn't underestimate me.":
                $ annamood += 1
                $ renpy.pause (0.5)
                show anna smirk flip with dissolve
                An "Maybe."
                jump cont1
                    
            "It was a lucky guess.":
                $ annamood -= 1
                $ renpy.pause (0.5)
                show anna disgust flip with dissolve
                An "You won't be so lucky again."
                jump cont1

            "Not a good start for you, is it?":
                $ renpy.pause (0.5)
                show anna normal flip with dissolve
                An "Let's see if you can keep it up."
                jump cont1

    "Otomo Izumi":
        jump wrong1
        
    "Damion Dandelion":
        jump wrong1


label wrong1:
    $ renpy.pause (0.5)
    show anna normal flip with dissolve
    An "I'm afraid that's wrong. I'm so sorry, [player_name]." 
    c "How was I supposed to know something like that?"
    show anna smirk flip with dissolve
    An "It was your challenge. You dig your grave, you lie in it."
    An "Besides, it's not as if it wasn't clear to me from the beginning that I'd win, so no surprises there."
    
label cont1:
    pass
    
c "Let's see how you fare with your first question."
show anna normal flip with dissolve
An "Bring it."

play sound "fx/card.wav"

$ renpy.pause(1.0)

c "How far can you walk into the woods?"
An "Only until the middle. Anything after that and you're walking out of the woods again."
c "You're right. That's a rather weird question, though."

show anna smirk flip with dissolve
An "I suppose I read the right kinds of books growing up. I know most of those trick questions."

show anna normal flip with dissolve

An "Let's see what the second question has in store for you, shall we?"

stop music fadeout 1.0
play sound "fx/card.wav"
$ renpy.pause(1.0)

play sound "fx/woosh3.ogg"
show eyes at Pan ((500, 0), (0, 0), 1.0)
show round2 at Pan ((-500, 0), (0, 0), 1.0)
show anna smirk flip

with dissolvemed

$ renpy.pause (2.0)

hide eyes
hide round2
with dissolvemed

play music "mx/jazzy2.ogg"
An "Alright, if there are five apples and you take away three, how many do you have?"

menu:
    "One.":
        jump wrong2
        
    "Two.":
        jump wrong2
    
    "Three.":
        $ annamood += 1
        $ annaanswers += 1
        An "Guess you also know your trick questions."
        c "Apparently so."
        jump cont2

label wrong2:
    $ renpy.pause (0.5)
    show anna smirk flip with dissolve
    An "No. You see, it's a trick question. Three is the correct answer, because that's the number that you took away."
    menu:
        "What a stupid question.":
            $ annamood += 1
            $ renpy.pause (0.5)
            show anna normal flip with dissolve
            An "Not like mine was any better, but I still knew the answer."
            c "Oh well."
            
        "Let's just move on.":
            $ renpy.pause (0.5)
            show anna normal flip with dissolve
            An "As you wish."

        "That doesn't count.":
            $ annamood -= 1
            $ renpy.pause (0.5)
            show anna sad flip with dissolve
            An "Don't be so childish."
            c "Alright, alright."
            show anna normal flip with dissolve

label cont2:
    pass
    
play sound "fx/card.wav"
$ renpy.pause(1.0)
c "Okay, here's your question: In which year of our timeline did we gain sentience?"
An "Zero. The beginning of our timeline marks the event when we gained sentience."
c "Right again. Have you played this game before?"

show anna face flip with dissolve

An "It's a children's game. These questions aren't really a challenge."

show anna sad flip with dissolve

An "I'll just go ahead and draw the next card, so we can end this."

stop music fadeout 1.0
play sound "fx/card.wav"
$ renpy.pause(1.0)

play sound "fx/woosh3.ogg"
show eyes at Pan ((500, 0), (0, 0), 1.0)
show round3 at Pan ((-500, 0), (0, 0), 1.0)
show anna smirk flip

with dissolvemed

$ renpy.pause (2.0)

hide eyes
hide round3
with dissolvemed

play music "mx/jazzy2.ogg"
An "An adventurer who values his life has to choose between three rooms to cross. Which one of the following would be the safest?"
An "#1: A room filled with poisonous gas. #2: A room filled with one hundred highly trained assassins. #3: A room submerged in water filled with alligators that have not eaten in eight months."

menu:
    "#1, the room filled with poisonous gas.":
        jump wrong3
        
    "#2, the room filled with one hundred highly trained assassins.":
        jump wrong3
        
    "#3, the room submerged in water filled with alligators that have not eaten in eight months.":
        jump wrong3
        
    "None of these.":
        $ annamood += 1
        $ annaanswers += 1
        An "That's right. All the rooms are equally deadly. Alligators can go up to two years or more without food, making room #3 as deadly as the others. The other two rooms should not require any explanation." 
        
        show anna normal flip with dissolve
        
        An "At least according to this card. To be honest, I think the answer is debatable."
        An "Don't worry, I'll still count it as a right answer for you. No need to get your tail caught in a door about it."
        jump cont4

label wrong3:
    $ renpy.pause (0.5)
    show anna normal flip with dissolve
    An "Nope. In fact, all the rooms are equally deadly. Alligators can go up to two years or more without food, making room #3 as deadly as the others. The other two rooms should not require any explanation."
    menu:
        "This question is poorly worded.":
            An "Don't blame me. I didn't make this game."
            
        "This is ridiculous.":
            $ annamood -= 1
            $ renpy.pause (0.5)
            show anna sad flip with dissolve
            An "Guess you don't like this game so much anymore."
            
        "I don't even know what to say to that.":
            $ annamood += 1
            $ renpy.pause (0.5)
            show anna smirk flip with dissolve
            An "I do. I think you're about to lose."
            
label cont4:
    pass
    
c "Looks like this is going to be the last question."

show anna face flip with dissolve

An "Just get it over with already."

play sound "fx/card.wav"
$ renpy.pause(1.0)

c "What is the approximate acceleration speed of a nosediving flyer?"

show anna sad flip with dissolve

An "I'll have to think about that one for a minute."
c "..."
c "I was just kidding."

show anna normal flip with dissolve

An "I still could have calculated that."
c "Okay, here's the real question: What is the only substance known to be lighter in its solid form compared to its liquid state?"
An "Water."
c "That seems to be correct."

show anna face flip with dissolve

An "Of course it is, duh!"

if annaanswers == 3:
    
    if persistent.c1annaanswers == False:

        $ mp.generalknowledge = True
        $ mp.save()

        $ persistent.c1annaanswers = True
        
        $ achievement.grant("General Knowledgist")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_36
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You answered Anna's questions correctly!"
            
        elif system == "advanced":

            s "You answered Anna's questions correctly. Well done."
            
        else:
            
            s "You answered Anna's questions correctly. Feel free to imagine a celebratory rain of confetti pouring down on you, if that makes you feel good."
    
    show anna normal flip with dissolve
    An "Well, it appears to me that our game has ended in a tie."
    c "What do you propose?"
    show anna smirk flip with dissolve
    An "I say we both get our rewards. After all, we each made a good effort to get them."
    c "That's fine with me."
    show anna normal flip with dissolve
    An "I won't have a spot in the facility to do the tests for a while, though, so I suppose next time we meet, it'll be a date."
    c "Don't forget what I said earlier about what I expect from you on this date. You better be on your best behavior."
    show anna sad flip with dissolve
    An "I'll try."
    c "Thank you."
    show anna normal flip with dissolve
    An "In any case, I should head back to work. My break is just about over."
    c "See you soon, then?"
    show anna smirk flip with dissolve
    An "Of course. And I'll make sure you deliver your part of the deal."
    show anna normal flip with dissolve
    An "See you soon."
    show anna normal
    $ renpy.pause(0.3)
    hide anna with easeoutleft
    $ renpy.pause(0.7)
    nvl clear
    stop music fadeout 1.0
    window show
    n "Despite all odds, I managed to match her perfect score in the game we played." 
    n "Even though my bet of forcing her to go on a proper date with me was more to get back at her for her earlier rudeness, I had not expected this outcome. I was not even sure what I expected from this meeting in the first place, but now I was locked into going on a date with her and being her own, personal guinea pig." 
    n "Whether anything good would come of this, I wasn't sure, either."
    window hide

    $ annastatus = "good"
    
    $ annascenesfinished = 1
    
    $ persistent.anna1skip = True
    if chapter4unplayed == False:
        
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
elif annamood > 0:
    
    label anna1skip:
    
    show anna smirk flip with dissolve
    An "Just look at that, I won."
    c "Someone had to."
    show anna normal flip with dissolve
    An "This turned out to be more fun than I expected. Of course, the main reason for that is because I won, but still..."
    c "I get it. You won, you're great, et cetera."
    show anna smirk flip with dissolve
    An "That is true."
    c "So, when should I come in for the tests?"
    show anna sad flip with dissolve
    An "Actually, I'm not sure if I'll get a spot for them in the facility anytime soon, but I'll be sure to let you know."
    c "I'm quite sure you will."
    show anna normal flip with dissolve
    An "But you know what, this wasn't so bad after all. Maybe I'll let you have your date."
    c "Really?"
    An "Sure. I mean, you didn't win, but I think you earned it nonetheless. Or maybe I'm just that nice."
    c "Okay."
    An "Well, it's up to you. Call me if you're interested."
    c "I'll let you know."
    show anna smirk flip with dissolve
    An "I'm still going to collect my prize, though."
    c "I'm sure you'll make sure of that."
    show anna normal flip with dissolve
    An "You bet I will. In any case, I should get going now. My \"break\" is just about to end. Bye!"
    show anna normal
    $ renpy.pause(0.3)
    hide anna with easeoutleft
    $ renpy.pause(0.7)
    nvl clear
    stop music fadeout 1.0
    window show
    n "I was not sure what I had expected out of this encounter, but it certainly wasn't this." 
    n "After all, proposing a proper date was my way of sticking it to her for being rude." 
    n "Even though I lost the bet, she didn't seem to mind going on a date with me, as long as she got what she wanted. Whether I would follow up on it was up to me, though."
    window hide

    $ persistent.anna1skip = True

    $ annastatus = "neutral"
    
    $ annascenesfinished = 1
    
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
else:
    show anna smirk flip with dissolve
    An "And in a twist of fate that shocked no one, Anna, the magnificent, won the game."
    c "Oh, knock it off."
    show anna sad flip with dissolve
    An "What's your problem? I earned this."
    c "I suppose you did, but you had the home field advantage."
    show anna disgust flip with dissolve
    An "You didn't mind that when you proposed we play this stupid game. You're such a sore loser, you know that?"
    c "And you're about the worst winner I've ever met."
    show anna normal flip with dissolve
    An "I think you're just experiencing acute posterior pain, because you don't get to go on a date with me now."
    c "I didn't want to go on a date with you in the first place. I just wanted to teach you some manners."
    show anna face flip with dissolve
    An "Mission accomplished."
    c "See, that's what I'm talking about."
    show anna sad flip with dissolve
    An "Because you'd obviously be such a good teacher, the way you exude virtues such as civility and humbleness, and tried to force someone to go on a date with you on a bet."
    c "Maybe you should step down from your high horse for once."
    show anna disgust flip with dissolve
    An "You criticize me, but you're such a hypocrite. I can't even understand what you're saying. What's a horse?"
    c "There's no reasoning with you."
    An "No, not since one of us thought they were somehow better than the other. Where did the sudden superiority complex come from?" 
    An "Just because, oh my gosh, you happen to be human and therefore deserve special treatment? You're just like Reza in that regard."
    c "Reza..."
    show anna sad flip with dissolve
    An "You know what? I'm leaving now, but don't expect for a minute that I won't make sure that you'll deliver on your end of the deal."
    c "Whatever."
    show anna sad
    $ renpy.pause(0.3)
    hide anna with easeoutleft
    $ renpy.pause(0.7)
    stop music fadeout 1.0

    $ annastatus = "bad"

    $ annascenesfinished = 1

    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars

   
   
    
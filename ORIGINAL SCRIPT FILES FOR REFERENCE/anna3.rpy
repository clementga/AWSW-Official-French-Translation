#-9 +10
label anna3:

$ anna3unplayed = False
$ anna3mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Anna 3"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Anna 3"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Anna 3"
    
else:

    $ save_name = "Chapter 1 - Anna 3"

scene black with fade
$ renpy.pause (1.0)
scene facin2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

$ renpy.pause (1.3)

play music "mx/anna3.ogg" fadein 2.0

show anna normal b with dissolve

An "There you are. I was wondering if you'd even show up."

menu:
    
    "I'm an honorable person.":

        $ renpy.pause (0.5)
        
        An face b "Good for you. And for me, as it turns out."

        $ anna3mood -= 1
        
        show anna smirk b with dissolve


    "I wouldn't miss an opportunity to meet you.":

        $ renpy.pause (0.5)
        
        An smirk b "A glutton for punishment, huh? Not that I mind."
        
        $ anna3mood += 1
        
        
    "I didn't have anything better to do, anyway.":
        
        An "As long as you're here, I don't care."

        show anna smirk b with dissolve
        

An "Follow me, please."
        
hide anna with dissolve

$ renpy.pause (0.5)

show testingroom at Pan ((0, 100), (0, 233), 3.0) with dissolveslow

$ renpy.pause (1.3)

#insert skip here

if persistent.anna3skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck

    call skiptut from _call_skiptut
        
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
            call skipcheck from _call_skipcheck
            
            scene testingroom at Pan ((0, 233), (0, 233), 0.0) with dissolvemed

            show anna normal b with dissolve
                        
            play music "mx/anna3.ogg" fadein 2.0
            
            jump anna3skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/anna3.ogg" fadein 2.0

show anna normal b with dissolve

c "So, what exactly is this room?"

An "It's our testing room for research on live subjects."

c "And what exactly do you test here?"

An smirk b "You'll see that soon enough. I intend to use this facility to its fullest potential."

c "I see."

play sound "fx/wheels.ogg"
        
An normal b "Let's start with this one."

c "What's that?"

An "I can get a good look at your bone structure, muscle groups and organs with this. For the finer details, we'll need a different machine."

An "Would you please lie down here?"

c "Of course."

play sound "fx/bed.ogg"

c "Before we start, can I ask about your qualifications?"

An "You can trust me. I'm a doctor."

c "What kind of doctor?"

An sad b "Well, Doctor of Pharmacy is the only title I currently hold, but I know how to operate this machinery."

c "That doesn't exactly inspire confidence."

An face b "You think I'd let an opportunity like this go to waste by not doing my research? I'll have you know that I'm very qualified to perform these tests."

c "If you say so..."

play soundloop "fx/startx.ogg"
queue soundloop "fx/hum.ogg"

An sad b "Now, please try not to move too much while this is running."

c "And how long will that be?"

An normal b "Good question. I suppose we'll see soon enough."

c "And what do we do now? Just wait until it's over?"

An sad b "What do you want me to do? Dance for you so you don't get bored?"

menu:

    "I wouldn't mind that.":

        $ renpy.pause (0.5)
    
        An face b "I'm sure you wouldn't, but I'm afraid I don't provide {i}those{/i} kinds of services."

        $ anna3mood -= 1

        $ mp.dance = "yes"
        $ mp.save()


    "Just forget I said anything.":

        $ renpy.pause (0.5)
        
        An normal b "I will."

        $ mp.dance = "no"
        $ mp.save()
        
        
    "What does a dancing dragon look like, anyway?":

        $ renpy.pause (0.5)
        
        An smirk b "Is that your scientific curiosity shining through? I can approve of that."

        c "You didn't answer my question."

        An normal b "Well, I'm not going to show you. If you're that curious, you might find the answer in the seedier parts of town."

        c "Your town has seedy parts?"

        An smirk b "Oh, there’s a lot you haven’t seen yet."

        $ anna3mood += 1

        $ mp.dance = "maybe"
        $ mp.save()


c "You know, when I heard that something happened at the facility, I thought it might have been you."

if damionsurvives == False:
    
    An sad b "It's quite something, isn't it? You know, if I stayed as late as I used to, it might have been me instead of Damion."

    An "And it's only because you told me not to stay late so often that I wasn't there that night."

    c "Still, somebody died."

    An rage b "I'm not crying over that bastard."


else:

    An sad b "It's quite something, isn't it? You know, if I stayed as late as I used to, I might have been there when the break-in happened." 
    
    An disgust b "I sure as heck wouldn't just have let them take anything."

    c "No, you'd probably be dead."

    An face b "Really? What makes you think so?"

    c "The perpetrator is the same person who is responsible for the murders you might have heard about recently."

    An sad b "Huh, guess that was a close one, then."


stop soundloop fadeout 2.0


An normal b "Alright, you can move again."

c "Does that mean I'm done?"

An smirk b "That's a good one! We're just getting started."

c "What about the results?"

An normal b "Don't hold your breath. It'll be processing for some time, and the resulting data will be so vast that I'll probably end up studying it for days."

An smirk b "Let's collect some samples now. Where should I start?"

c "Wherever you like." 

An normal b "Show me your claws."

c "That would be \"fingernails\" in my case."

An "I suppose you're right. It would be insulting to call those thin little things of yours claws. They'd probably break off before you could make use of them in any practical way."

c "Just one more way nature gave us the short end of the stick."

An "So, which part would be fine for me to cut off?"

c "Take a piece from the white part. The rest you see is attached to the finger."

An face b "Hold still, then."

c "Don't cut off too much."

An normal b "Don't worry. I only need enough to put it under a microscope."

play sound "fx/nail.ogg"

An "There, was that so bad? Do you want me to put a bandage on your little boo-boo?"

menu:
    
    "Whatever.":

        $ renpy.pause (0.5)
        
        An smirk b "Oh, I guess with the right training, I can make something out of you after all."
        
        $ anna3mood += 1
        
        
    "I'll show you a boo-boo.":

        $ renpy.pause (0.5)
        
        An face b "No, thanks."


    "You better behave. I'm doing you a favor.":

        $ renpy.pause (0.5)
        
        An face b "No you aren't. You're only giving me what you owe."

        $ anna3mood -= 1


c "And what now?"

An normal b "Now it'll go right under the microscope."

hide anna with dissolve

m "She got up and sat down at a table. Intently, Anna stared at a device while messing around with the nail clipping."

play sound "fx/micro.ogg"

An "Let's see..."

c "Putting your fingernail under a microscope is something we used to do in middle school."

An "Quiet, please. There's a scientist at work here."

c "Okay."

An "..."

show anna normal b with dissolve

An "This structure looks a lot like keratin."

menu:
    
    "I could've told you that.":

        $ renpy.pause (0.5)
        
        An face b "Well, good thing you didn't, because that might have saved us some time. Of course we can't have that, right?"
        
        show anna normal b with dissolve


    "Is that supposed to mean anything?":

        $ renpy.pause (0.5)
        
        An sad b "Only to someone who knows what they're talking about."

        show anna normal b with dissolve
        

    "Because it is.":
        
        An "Well, that's not much of a surprise, really."

        $ anna3mood += 1


An "Keratin is the substance that forms the claws on us dragons and most of the animals here. At least as far as mammals, reptiles and birds are concerned."

An "So why you would retain the structure, but not do anything useful with it is beyond me."

c "It gets better. They grow continuously, so they need to be cut regularly."

An "What happens if you don't cut them?"

c "They just keep growing."

An "How much can they keep growing?"

c "Pretty much indefinitely."

An "Do they get thicker at least, or what else happens when they grow?"

c "They just get longer."

An sad b "What a hassle."


c "So, how long are you planning on keeping me here?"

An face b "Getting impatient already?"

c "I'm just saying, our date didn't take all that long, and you mentioned you'll already have days worth of data from that machine."

An normal b "Well, we never specified any terms, and I sat out our \"date\" until it was officially over. This will certainly go by much quicker if you can show a little patience."

menu:
    
    "Says the queen of complaining.":

        $ renpy.pause (0.5)
        
        An smirk b "I don't complain, I just point out errors. Besides, I'd be empress, not just a queen."
        
        show anna normal b with dissolve

        $ anna3mood += 1


    "I'll just shut up, then.":
        
        An "Thank you."


    "Just hurry up.":

        $ renpy.pause (0.5)
        
        An face b "That wouldn't be very wise. You wouldn't want me to make mistakes once I start sticking needles into you."
        
        $ anna3mood -= 1

        show anna normal b with dissolve


An "By the way, how do you feel about needles?"

menu:
    
    "I don't mind them.":
        
        An "Glad to hear that."

        $ mp.needles = "neutral"
        $ mp.save()
        
        
    "Go ahead and poke me if you need to.":

        $ renpy.pause (0.5)
        
        An smirk b "I see. I'll make the most of it, then."
        
        show anna normal b with dissolve

        $ anna3mood += 1

        $ mp.needles = "yes"
        $ mp.save()

    "Please, no.":

        $ renpy.pause (0.5)
        
        An face b "Afraid of needles, are you? Aww, you poor thing."

        An sad b "I guess we can skip that part, because I certainly don't want to deal with you if you start screaming or crying, or whatever else."
        
        show anna normal b with dissolve
        
        $ anna3mood -= 1

        $ mp.needles = "no"
        $ mp.save()


An "You'll need to remove some layers for the next part."

c "What are you going to do?"

An "These are just some electrodes, and I'll also measure your brain activity with one of those helmets."

c "Alright."

play sound "fx/undress.ogg"

An "There you go."

c "..."

An sad b "What is it now?"

menu:
    
    "This is kind of embarrassing.":

        $ renpy.pause (0.5)
        
        An face b "Why?"

        c "Well, we usually don't take off this much in front of others."

        An sad b "Not even for doctors?"

        c "Oh, we do, but that doesn't make it any less embarrassing."

        An normal b "I don't understand. I mean, I get why you would want to put something on if it's cold, considering your lack of fur, but to have this compulsion to always have some layers on is a bit strange."

        c "It's just a social norm where I come from."

        An "As you can probably tell, we don't have a problem showing what we were born with."
        

    "It's kinda cold in here.":

        $ renpy.pause (0.5)
        
        An normal b "Is it? I suppose it might be for you, considering your lack of fur." 
        
        An "Luckily, our scales are pretty good insulators, as you saw last time. It actually goes both ways. We're pretty resistant to both heat and cold."

        c "Just let me know if I turn blue."

        An "You turn blue when you get cold? I'd like to see that."

        c "It was just a joke. Besides, when that happens, it's usually too late to get out of it again unscathed."

        An sad b "What a shame."
        
        show anna normal b with dissolve


    "Nothing.":

        $ renpy.pause (0.5)
        
        An normal b "If you say so."

        
An "This will also take a while. I want to have a good reference and see how your rates change."

An "Your head shape is a little different from ours, but I think this one should do the trick."

play sound "fx/helmet.ogg"

$ renpy.pause (0.5)

An "Perfect, just as if it was made for you."

c "I'm not so sure of that."

c "By the way, how can you even be sure that your machinery will have no adverse effects on me?"

An sad b "I suppose I can't."

c "That is mildly unsettling."

An normal b "Your physiology is similar enough to ours that there shouldn't be any problems."

c "I see."

play soundloop "fx/monitor.ogg" fadein 3.0

An "Now, I'm going to ask you a few questions."

c "What is this, a polygraph test?"

An "No. This is something completely different. I'm also measuring your brain activity here. Besides, I don't really care about the truthfulness of your answers. Rather, this is to establish your natural highs and lows of the values I'm measuring."

c "Go ahead, then."

An "Let's start with the easy ones."

An "Just say no to the following three questions. It doesn't matter if it is true or not. Understood?"

menu:
    
    "No.":

        $ renpy.pause (0.5)
        
        An face b "I set myself up for this one, didn't I?"
        
        show anna normal b with dissolve
        
        
    "Yes.":
        
        pass
        
        
    "I'm not sure.":
        
        An "Just say no, and you'll be fine."
        

    "Does this question count already?":

        $ renpy.pause (0.5)
        
        An sad b "Erhm, no. Apparently, you get it, though."

        show anna normal b with dissolve
        
        
An "The questions start now. Are you human?"

c "No."

An "I see."

An "Is your favorite color [persistent.playercolorname]?"

c "No."

An smirk b "Interesting."

An normal b "Have you been convicted of any crime?"

c "No."

An "I see."

An "Now, we'll get to the real part. You can answer the following questions however you like."

c "Got it."

An "Did it make you uneasy when you had to answer all the test questions negatively?"

menu:
    
    "Yes.":
        
        pass
        
    "No.":
        
        pass
        
    "Not really.":
        
        pass

        
An "I see. Interesting."

An "Have you taken a liking to anyone here since you arrived?"

menu:
    
    "Yes.":
        
        pass
        
    "No.":
        
        pass
        
    "I'm not sure.":
        
        pass
        

$ renpy.pause (0.5)
An smirk b "I see."

An normal b "Did you have any ulterior motives when you came to our world, or is it as simple as we are led to believe?"

menu:
    
    "There are no ulterior motives.":
        
        pass
    
    "No comment.":
        
        pass


An "I see."

stop soundloop fadeout 2.0

An "That's all for this test. You can take off the helmet, and I'll take care of the electrodes."

c "This kinda seemed like an interrogation."

An "I wanted to keep it simple by asking questions that could get a reaction."

c "I see."

An "It's kind of a shame, because in the end a lack of additional subjects for this test means those results might not be very useful to us. We'd probably need a few more humans."

c "Then why do them in the first place?"

An "The data is still useful, just not as useful as it could be. And besides, I did tell you I'd make the most of this room."

c "Well, what's next?"

An "I'm not sure yet. Do I want to get close enough to examine mucosa and orifices?"

menu:
    
    "Probably not.":
        
        An "You might be right."
        
        $ anna3mood += 1
        
    
    "Yes.":

        $ renpy.pause (0.5)
        
        An face b "Is that what you're into? Good to know."
        
        show anna normal b with dissolve

        $ anna3mood -= 1


    "There's only one person in this room who can answer that question.":

        $ renpy.pause (0.5)

        An sad b "I guess so."

        show anna normal b with dissolve

        
An "We quarantined Reza when he initially arrived here, but skipped the procedure with you. After examining Reza, we didn't think humans by themselves posed any danger."        

An "Nevertheless, who knows what kind of illnesses and bacteria you might be housing as an alternate host? I'm not taking that risk without a full protective suit."

c "Does that mean your procedures are going to get a lot more invasive?"

An "No, I'm not in the mood to put the suit on and sterilize the whole room."

c "To be fair, I haven’t heard of anyone I’ve been in contact with getting any strange diseases thus far."

An "Sure, but then I'd have to ask you if any of those actually got close enough to you."

An smirk b "As in... intimately close."

c "No orifice examinations, then."

An normal b "For the next part, we'll actually have to go outside."

c "That sounds like fun."

An "Depends. Here, strap this to your arm."

play sound "fx/pda.wav"

c "What's this?"

An "A handheld monitor. I want to measure how you perform during exercise."

menu:
    
    "I don't like exercising.":

        $ renpy.pause (0.5)
        
        An face b "And I don't like waiting."
        
        show anna normal b with dissolve

        $ anna3mood -= 1


    "Awesome.":
        
        An "At least we found something you like."
        
        
    "Yes, ma'am.":

        $ renpy.pause (0.5)
         
        An smirk b "That's a good little human."

        show anna normal b with dissolve
    
        $ anna3mood += 1


An "Let's go then, shall we?"

c "Sure thing."

scene black with dissolvemed

$ renpy.pause (0.5)

scene fac1 with dissolvemed

show anna normal b with dissolve

c "And now?"

An "Take one lap around the block. I'll be waiting for you here. You can go as fast or slow as you want, but try not to stop until you're back here."

An "I'll be monitoring you, so I'll know if you try to do anything fishy." 

menu:
    
    "I wouldn't do such a thing.":
        
        An "Of course not. The honest and good [player_name] would never do such a thing."

        c "There's no need to make fun of me for it."

        An face b "You're such a bleeding heart, [player_name]."
        
        show anna normal b with dissolve
                
        $ anna3mood -= 1


    "Piece of cake.":
        
        An "Easier said than done, [player_name]. I'll be watching."
        
        
    "No need to point out the obvious.":

        $ renpy.pause (0.5)
        
        An face b "You wouldn't believe the kinds of people I have to deal with sometimes."

        c "I could say the same thing."

        An normal b "Is that so?"

        $ anna3mood += 1
        

An "Anyway, you can start whenever. The monitor should take care of the rest."

hide anna with dissolve

$ renpy.pause (0.7)

scene gate with dissolvemed

if remydead == False:

    m "Trying for a consistent speed, I started with a light jog. Soon, I was outside the gate and around the corner when I met an unexpected surprise."
            
    show remy normal with dissolve

    if remystatus == "good":
        
        Ry smile "Oh. Hello, [player_name]. It's good to see you." 
        
        Ry normal "What are you doing here?"

        menu:
            
            "I made a bet with Anna, and now I have to do some tests for her.":

                $ renpy.pause (0.5)
                
                Ry look "Oh, no. Why'd you do that?"

                c "It's a long story."

                Ry "I hope you are careful around her."

                c "No worries, I am."

                Ry "Is she doing anything... weird, or painful to you?"

                c "No. Or at least not yet."

                Ry "You know, if she tries anything, you can always tell her to stop. If it comes to the worst, your rights as ambassador trump any bar bets you might have made with her."

                c "I'll keep that in mind, thanks!"

                Ry normal "Have you made up your mind about it yet?"

                c "What do you mean?"

                Ry "Our next meeting."

                c "Oh, I haven't forgotten. I've just been a bit busy with all kinds of things, this included. I'll have to get back to you on that."

                Ry smile "No problem."

                Ry normal "Well, I don’t want to distract you from what you are doing. ‘Til we meet again!"

                c "Bye."

                $ anna3stopped = True

                hide remy with dissolve


            "Nothing special, just going out for a jog.":

                $ renpy.pause (0.5)

                Ry smile "I see, just enjoying the fresh air then."

                c "What about you?"

                Ry normal "Oh, I have some errands to run."

                c "Is Emera breathing down the back of your neck again?"

                Ry "Always."

                c "Well, I better not hold you up, then."

                Ry "One question before I go: Have you made up your mind about it yet?"

                c "What do you mean?"

                Ry smile "Our next meeting."

                c "Oh, I haven't forgotten. I've just been a bit busy with all kinds of things, this included. I'll have to get back to you on that."

                Ry normal "No problem."

                c "See you next time, then."

                Ry "Until we meet again."

                hide remy with dissolve
                
                $ anna3stopped = True
                
                
            "Can't talk right now, see you later!":

                $ renpy.pause (0.5)
                
                Ry smile "Okay, have fun!"
                
                hide remy with dissolve
                
                
    elif remystatus == "bad":
        
        Ry look "[player_name]."

        c "Remy."
        
        hide remy with dissolve
        
        m "He just went past me without any further acknowledgement."
        
        
    elif remystatus == "neutral":
        
        Ry "Oh. Hello, [player_name]."

        c "Hey, Remy."

        Ry smile "Just enjoying the fresh air, I see."

        c "What about you?"

        Ry normal "Oh, I have some errands to run."

        c "Is Emera breathing down the back of your neck again?"

        Ry "Always."

        c "Well, I better not hold you up, then."

        Ry "Until we meet again."

        c "See ya."

        $ anna3stopped = True

        hide remy with dissolve
        
        
    elif remystatus == "none":
        
        Ry "Hey, [player_name]."

        c "Hey, Remy. Long time no see."

        Ry "Indeed. Just enjoying the fresh air, I see."

        c "Yeah."

        Ry "You know, if you ever want to come by and visit the library or need to know anything, feel free to ask me."

        c "I will, thanks!"

        Ry "My pleasure."

        $ anna3stopped = True
        
        hide remy with dissolve


    else:
        
        Ry smile "[player_name]!"

        c "Remy."

        Ry normal "What are you doing here?"
        
        menu:
            
            "I made a bet with Anna and now I have to do some tests for her.":

                $ renpy.pause (0.5)
                
                Ry look "I see, so that's why you have that thing strapped to your arm."

                c "Yeah."

                Ry "I guess you've been hanging out with Anna a lot, then."

                Ry shy "Is that why you didn't return my calls?"

                c "It's not like that."

                Ry "I would've warned you about her, but I think you know what you're doing."

                c "You're overreacting."

                Ry sad "Don't worry about it. I'm leaving. I hope you're happy with the decisions you've made."

                Ry "Goodbye, [player_name]."
        
                hide remy with dissolve

                $ anna3stopped = True
                
                
            "Nothing special, just going out for a jog.":

                $ renpy.pause (0.5)
                
                Ry smile "Enjoying the fresh air, I see."

                c "Yeah, what about you?"

                Ry normal "Oh, I have some errands to run."

                c "Is Emera breathing down the back of your neck again?"

                Ry "Always."

                c "Well, I better not hold you up, then."

                Ry shy "I just have one question for you."

                c "What is it?"

                Ry "Is there a reason why you haven't returned my calls?"

                c "Oh, I've just been very busy. I never even check my messages."

                Ry normal "I see. Well, my invitation is still standing."

                c "Good to know. I'll have to see if I can make time for it."

                Ry "Let me know if you can."

                c "Sure thing. I've got to go now, so see you later!"

                Ry "See you."
        
                $ remystatus = "normal"

                hide remy with dissolve

                $ anna3stopped = True


            "Can't talk right now, I have to go!":

                $ renpy.pause (0.5)
                
                Ry shy "I... I see."

                hide remy with dissolve
            
   
    $ renpy.pause (0.5)

else:
    
    m "Trying for a consistent speed, I started with a light jog. Soon, I was outside the gate and around the first corner."

scene fac1 with dissolvemed

m "Afterwards, I finished my lap around the block, arriving only a few minutes after I had started."

show anna normal with dissolve

if anna3stopped == True:
    
    An face b "I suppose it was too much to ask for a lap without any breaks."

    An sad b "Maybe I shouldn't have expected you to be as fit as we are."

    c "I got distracted on the way."

    An normal b "How so? Did you have to stop and smell some flowers?"

    c "I met Remy."

    An face b "Remy? Oh, I wouldn’t mind if that bastard kicked the bucket too."
    
    menu:
        
        "What do you have against him?":

            $ renpy.pause (0.5)
            
            An sad b "He's such a self-rightous do-gooder who can't help but stick his nose where it doesn't belong."

            An face b "I don't care what he does as long as he doesn't mess with me, but he does mess with me so I {i}do{/i} care."
    
            show anna normal b with dissolve
        
        "How can you say that?":
            
            $ renpy.pause (0.5)
            
            An normal b "That's how I feel. Would you prefer me to lie to your face?"
    
    
else:
    
    An "There you are. Not bad."


An "Anyways, I've got your data, so we can head back inside if you're not too exhausted to walk."

c "Of course."

scene black with dissolvemed

$ renpy.pause (0.5)

scene testingroom at Pan ((0, 233), (0, 233), 0.0) with dissolvemed

show anna normal b with dissolve

An "Looking at your data, it's kinda hard to evaluate it without having any reference points. How much exercise do you usually get?"

menu:
    
    "A lot.":

        $ mp.exercise = "lot"
        $ mp.save()
        
        pass
        
    "A little.":

        $ mp.exercise = "little"
        $ mp.save()
        
        pass
        
    "None at all.":

        $ mp.exercise = "none"
        $ mp.save()
        
        pass
        
        
An "I see."

c "You sure get to ask me a lot of questions here."

An "All just part of the tests."

An "Though, I think those were all the tests I needed to run on you for today."

c "Does that mean we're done here?"

An "Oh, some of the data from the scanning machine has been processed. We can look at some pretty pictures of you."

menu:

    "Unflattering as they may be.":

        An "Well, you don't have to look if you don't want to."
    
    
    "Why don't you print them out and have them framed?":

        $ renpy.pause (0.5)
        
        An smirk b "Or better still, sell the prints. I could make bank doing that."

        An normal b "Thanks for the idea."

        c "Wouldn't I deserve royalties from that?"

        An "Sorry, no such written agreement exists."

        $ anna3mood += 1


    "I'd rather be looking at some pretty pictures of you instead.":

        $ renpy.pause (0.5)
        
        An face b "That's the best you can come up with? Seriously."
        
        show anna normal b with dissolve

        $ anna3mood -= 1
        
        

play sound "fx/flicker.ogg"

An "Oh, right. I totally forgot that you are a mammal."

An "To encounter an intelligent mammal, of all things. Well, reasonably intelligent at the very least."

c "Why is that so surprising? You already have your myths about humans."

An "Myths are myths. Having you here in the flesh is an entirely different thing."

An "It's not like I could use our myths to get a scan like this one."

An "It just seems so funny to me. Do you nurse your young from your teats as well?"

c "We do."

An "Let me study your muscle groups for a bit."

c "Do you want me to take my clothes off again?"

An face b "I meant the pictures."

c "Oh, I see."

An normal b "You can stay for a bit longer in case I have any questions."

c "Okay."

hide anna with dissolve

m "While I continued sitting on the bed, she went up to her table and started looking at the scans of muscle groups. As we talked, her eyes never left the screen."

An "Some of these structures are very similar to those found in Damion's kind."

c "I'm not surprised. His stature is similar enough."

An "True, true. Now shut up and let me concentrate."

c "Does that approach ever work?"

An "What are you talking about?"

c "You being that rude to everyone."
        
if anna3mood <= 2:
    
    An "..."

    An "We're done here. Get out."

    c "You can't take what you dish out, huh?"

    m "Suddenly, she got up. A look of rage crossed her face."

    show anna rage b with dissolve
    
    An "I said get the heck out of here."

    m "She grabbed my arm and roughly walked me to the door. After shoving me outside, she quickly closed the door behind me."

    show facin2 at Pan ((128, 250), (128, 250), 0.0) with dissolve
    
    play sound "fx/door/doorclose.ogg"
    
    $ renpy.pause (0.5)

    c "Okay."

    stop music fadeout 2.0
    
    $ renpy.pause (0.5)
        
    $ annastatus = "bad"

    $ annascenesfinished = 3
        
    if chapter4unplayed == False:
                        
        jump chapter4chars
            
    elif chapter3unplayed == False:
            
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars


else:
    
    pass
    
    
An "Sorry."

c "You apologized. That's a new one."

An "I don't want to make any excuses, but with a high-pressure job like mine, I don't really get to go out and socialize much."

An "Add some deterioriating circumstances to that, and you get my life."

c "Don't you have any friends?"

An "Not really. If you keep skipping grades like I did and were on the fast track in university, you wouldn't really have the time to make or keep any friends either."

An "I think the last time I had a real friend was more than a decade ago."

c "What happened to that friend?"

An "Well..."

scene black with dissolvemed

$ renpy.pause (0.5)

nvl clear

window show

n "We went to the same class for a while. I ended up skipping a grade after that year."

n "She found new friends. I didn't."

n "We still met, but those visits became less and less frequent as time went on."

n "I was around ten years old when her parents prompted me to visit her."

n "She was in the hospital. Apparently had been for some time already."

n "I didn't know, because I hadn't seen her for quite a while at that point."

n "She had contracted some sort of degenerative disease that caused her to gradually lose control of her muscles."

window hide
nvl clear
window show

n "Her case was particularly bad. She was already paralyzed from the neck down by the time I went to visit her."

n "When I entered her room, I couldn't even pretend to be her friend. Lying in the bed was just a crude image of her former self. It was as if she was already dead."

n "I couldn't bear to see her like that. It scared me."

n "I didn't stay long."

n "Seeing her like that was... I just told myself I never wanted to end up like her, dying slowly, painfully, and alone."

window hide

$ renpy.pause (1.5)

show testingroom at Pan ((0, 233), (0, 233), 0.0) with dissolveslow
#with dissolvemed

An "That was the last time I saw her. She died a few weeks later."

c "And that’s why you became a scientist?"

An "Not really. I became a scientist because that's apparently what I'm good at."

An "Doesn't make my work any less important, though."

An "Just from what we did here today, we might make a few breakthroughs in several areas."

c "Really?"

An "You are a completely different, yet stable evolutionary line. There are some things that are similar in our bodies, and others that are completely different. Anything that is different and works can tell us something new about biology." 

An "All the various species have their own challenges and diseases. It'll come in handy somewhere, for sure."

c "And you're doing all of that, because of your pure, unselfish heart."

An "Not really. But if I do the brunt of the work, then I deserve to have my name on it."

c "I guess so."

show anna normal b with dissolve

label anna3skip:

An sad b "Well, I think that's it for the day. You can go if you like."

if anna3mood >= 8:
    
    c "I wouldn't mind staying for a bit longer."

    An "Really?"

    An "..."

    An "Well, I want to study those pictures some more, and I can't really have you around if I do anything serious."

    An normal b "But, maybe some other time."

    c "Really?"

    An "Because you're so insistent, I might as well."

    c "Okay."

    An "You know how busy I am, but I can call you if you'd like."

    c "Sure."

    An "If I don't forget, that is."

    c "Well, I'll leave you to your work, then."

    An "Mmm-hmm."

    hide anna with dissolve

    stop music fadeout 2.0
        
    $ renpy.pause (0.5)
        
    $ annastatus = "good"
    
    $ annascenesfinished = 3
    
    $ persistent.anna3skip = True
        
    if chapter4unplayed == False:
                        
        jump chapter4chars
            
    elif chapter3unplayed == False:
            
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
    
else:

    c "Sure. Thanks for having me."

    An normal b "My pleasure. We could get together, if you want to."

    c "Is there even anything left for you to test?"

    An "Well, I'll have plenty of data for a while. So I guess we'd have to find something else for us to do."

    c "I see."

    c "Well, I'll leave you to your work, then."

    An "Mmm-hmm."

    hide anna with dissolve

    stop music fadeout 2.0
        
    $ renpy.pause (0.5)
        
    $ annastatus = "neutral"
    
    $ annascenesfinished = 3

    $ persistent.anna3skip = True
        
    if chapter4unplayed == False:
                        
        jump chapter4chars
            
    elif chapter3unplayed == False:
            
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars


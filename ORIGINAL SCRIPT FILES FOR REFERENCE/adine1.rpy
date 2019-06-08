#+13-14max

label adine1:
$ chapter1csplayed += 1
$ adine1unplayed = False
$ adine1played = True

if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Adine 1"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Adine 1"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Adine 1"
    
else:

    $ save_name = "Chapter 1 - Adine 1"

scene black with dissolvemed
$ renpy.pause (0.5)
scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolvemed
m "I remembered that Adine had told me that the café did deliveries as well, and not having anything else better to do, I figured I should try it out. I made my order with a quick phone call, and it wasn't long before the doorbell rang."

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(Well, that was quick.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)
play music "fx/rain.ogg" fadein 1.0

m "It just so happened that Adine herself stood in the doorway, dripping wet and with damp containers in her grip."

#scene black with dissolve
#$ renpy.pause (0.5)
#scene cgadine2 with dissolvemed
#$ renpy.pause(4.0)

scene black with dissolve
$ renpy.pause (0.3)
show cgadine2 at Pan((0, 302), (0, 0), 7.0) with dissolvemed
$ renpy.pause(5.0)


scene o2 at Pan((0, 250), (0, 250), 0.1) with fade
    
show adine normal b with dissolve

$ adinemood = 0


if chapter3unplayed == False:
        
    Ad "Oh, it's you."
    
    Ad think b "I thought they sent you away after everything that's going on."
    
    c "They changed their minds, so I suppose you'll be stuck with me for a little while longer."
    
    Ad normal b "I see."

    $ adinesendawayseen = True
    
else:

    Ad "Oh, it's you again."

    menu:
        "I thought we were over this, but at least you don't reduce me to my species anymore.":
            $ renpy.pause (0.5)
            show adine giggle b with dissolve
            Ad "I do remember your name, though. It was... [player_name], right?"
            c "That's right."
            show adine normal b with dissolve
        "Likewise.":
            Ad "Shouldn't come as a surprise, considering you knew I deliver for the café."
        "Hey.":
            Ad "Hey."
     

Ad "Here's your order. Sorry, it got a little wet, but it should still be okay."
$ adine1choice1 = True
label adine1choice1:
    pass
menu:
    "What happened to you, did you fall into a river or something?" if adine1choice1:
        Ad "It's raining pretty heavily outside, that's all."
        $ adine1choice1 = False
        jump adine1choice1

    "You're soaked, why don't you come in?":
        $ adinemood += 1
        Ad "Thanks, I was just about to ask you if I could stay for a little while. This was actually my last delivery for the day, and I live on the other side of town."
        c "Of course, I couldn't let you fly back when it's this ugly outside."
        
    "Well, thanks for the food.":
        $ adinemood -= 1
        m "I was just about to close the door in her face again when she suddenly spoke up." 
        show adine disappoint b with dissolve
        Ad "Wait."
        c "What is it?"
        show adine sad b with dissolve
        Ad "Do you think I could come in for a few minutes? It's raining pretty heavily outside, and this was my last delivery for the day. I actually live on the other side of town, and I don't really want to fly back in the rain."
        $ adineques = True
        label menadine:
        menu:
            "I suppose it won't hurt if you come in for a few minutes.":
                $ renpy.pause (0.5)
                show adine normal b with dissolve
                Ad "Thank you."

            "[[Close the door.]":
                $ renpy.pause(0.2)
                hide adine with dissolve
                play sound "fx/door/doorclose3.wav"
                stop music fadeout 1.0
                $ renpy.pause(1.0)
                
                nvl clear
                window show
                n "Without another word, I closed the door, with nothing now separating me from the delights of the slightly soggy food before me." 
                n "I opened my container in anticipation, but what I found inside wasn't at all what I was expecting. It was noodles, with chicken and some sort of sauce." 
                n "The problem was, I hadn't ordered noodles. I rushed to the door, wondering what had gone wrong and what I had done to deserve this, but it was too late." 
                n "Adine was already gone."
                window hide
                $ adinestatus = "bad"
                $ adinescenesfinished = 1

                if chapter4unplayed == False:
                    
                    jump chapter4chars
                    
                elif chapter3unplayed == False:
                    
                    jump chapter3chars
                    
                elif chapter2unplayed == False:
                    
                    jump chapter2chars
                    
                else:

                    jump chapter1chars

            "Sure, come in.":
                $ adinemood += 1
                $ renpy.pause (0.5)
                show adine normal b with dissolve
                Ad "Thank you!"

            "This isn't a homeless shelter." if adineques:
                $ adinemood -= 1
                $ renpy.pause (0.5)
                show adine sad b with dissolve
                Ad "Come on, don't make me fly in the rain like this. Please?"
                $ adineques = False
                jump menadine
            

stop music fadeout 1.0
$ renpy.pause(0.5)
play sound "fx/door/doorclose3.wav"
$ renpy.pause(1.0)

#insert skippy here

if persistent.adine1skip == True:

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_47

    call skiptut from _call_skiptut_10
        
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
            
            $ adine1choice = persistent.adine1choice
            
            $ headgear = persistent.headgear
            
            show black with dissolvemed
            
            $ renpy.pause (1.0)
            
            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_10
            
            if headgear == True:
                
                hide black
                show adine giggle b 
                with dissolvemed
                
            else:
                
                hide black
                show adine giggle 
                with dissolvemed
                        
            play music "mx/serene.ogg"
            
            jump adine1skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

play music "mx/serene.ogg"
c "Feel right at home. I better eat this before it gets cold."
play sound "fx/chair.wav"

m "I sat down at the table and started eating my food while Adine decided to take a seat opposite of myself."
play sound "fx/eating.wav"

Ad "Do you like it?"

if food == "fish":
    c "Yeah, I ordered something I knew I'd actually like this time. I didn't want to make the same mistake I did earlier today."
else:
    c "Yeah, it's actually quite good." 
    
Ad "Do you have something similar where you come from?"
c "We do. As a matter of fact, it's almost scary how close it is to what we have back home."

show adine think b with dissolve

Ad "Really? Maybe we all just share a similar taste."

menu:
    "Maybe.":
        $ renpy.pause (0.5)
        show adine normal b with dissolve
        Ad "At least, that's what I think."
        
    "Maybe there's more to it than that.":
        $ adinemood += 1
        Ad "What do you mean?"
        c "Well, don't you trace your origins back to humans in some way? I know what kind of reputation we have in your culture."
        show adine normal b with dissolve
        Ad "That is true."
        c "Let me ask you this: Where do you think the portal you found came from? Who built it?"
        show adine giggle b with dissolve
        Ad "Humans did it, of course."
        show adine normal b with dissolve
        c "Exactly. If you believe humans had something to do with an artifact created who knows how many years ago, it wouldn't be a stretch to think they could have also influenced you in other ways."
        show adine think b with dissolve
        Ad "Even something as simple as this dish? I like that idea."
        show adine normal b with dissolve
        
    "Maybe I don't care.":
        $ adinemood -= 1
        $ renpy.pause (0.5)
        show adine annoyed b with dissolve
        Ad "I thought you just did."
        show adine normal b with dissolve

c "So, what do you do when you aren't working in the restaurant? Do you have a family?"
Ad "Well, most of the time I take care of my kids."
c "Oh, nice. How many children do you have?"
Ad "They aren't really my children, per se. I just take care of them."
c "You are more of a foster parent, then?"
Ad "Not quite. These are orphaned children I'm talking about. I just volunteer to spend some time with them, so I'm really more of a babysitter and teacher all in one." 
show adine disappoint b with dissolve
Ad "I can't really take them in and care for them 24/7 like a proper parent would. I'd love to, but I work far too much to be a single parent."
Ad "With the amount of time I spend at the restaurant, I don't think the kids would be any better off, so I just help out whenever I can."
c "That's very nice of you."
show adine normal b with dissolve
Ad "Thanks. These kids already didn't get a very good hand in life. I just thought that if I can make even a small difference for them it'd be worth it."
c "I see. What about hobbies? Do you have any?"

show adine annoyed b with dissolve

Ad "Can I ask a question for a change?"

menu:
    "Sure, go ahead.":
        $ renpy.pause (0.5)
        
    "No.":
        $ adinemood -= 1
        $ renpy.pause (0.5)
        show adine disappoint b with dissolve
        Ad "What? Why not?"
        c "Just kidding. Go ahead."
        
    "Well, {i}can{/i} you?":
        $ adinemood += 1
        $ renpy.pause (0.5)
        show adine giggle b with dissolve
        Ad "You're silly. I like that."
        
show adine think b with dissolve
Ad "Well, I don't really know much about you. Actually, I'm not sure if there is anyone here who does."
c "What would you like to know?"
show adine normal b with dissolve
Ad "What did you do before you came here?"

menu:
    "Nothing special.":
        $ adinemood += 1
        c "Nothing special, really. I mean, I have my degrees, but this is the first time I did something that was actually related to them. The work I did previously was just to keep afloat."
        show adine disappoint b with dissolve
        Ad "I know what you mean." 
        show adine normal b with dissolve
        
    "[[Avoid the question by making a bad pun.]":
        $ adinemood -= 1
        c "Nun."
        Ad "Nun? What do you mean?"
        c "I mean that it's {i}nun{/i} of your business."
        show adine annoyed b with dissolve
        Ad "Okay..."
        show adine normal b with dissolve
        
    "That's classified.":
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "Of course it is."
        show adine normal b with dissolve
        
c "I suppose it's my turn again, so tell me about your hobbies."
Ad "The one I enjoy most is probably flying."
c "Just flying?"
show adine annoyed b with dissolve
Ad "Well, not {i}just{/i} flying."
show adine normal b with dissolve
Ad "I do Aerobatics, or stunt flying. I've been doing that on and off for a couple of years now."

menu:
    "You must be the most overqualified delivery flyer in history, then.":
        $ adinemood += 1
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "Actually, that might not be so far from the truth."
        show adine normal b with dissolve

    "That's a cool, but also pretty useless hobby.":
        $ adinemood -= 1
        $ renpy.pause (0.5)
        show adine disappoint b with dissolve
        Ad "That's what hobbies are for, though, right? It's just something I enjoy doing."
        show adine normal b with dissolve
        
    "What's that?":
        Ad "It's the practice of doing flying maneuvers like rolls, spins or loops."
        
Ad "I'm actually hoping to be part of a competition in some time."

menu:
    "So you can do all that, but a little rain is too much?":
        $ adinemood -= 1
        $ renpy.pause (0.5)
        show adine annoyed b with dissolve
        Ad "Just because I can fly in the rain doesn't mean that I want to."

    "Are you that good?":
         Ad "That's what I'm trying to find out."
         
    "Awesome, where can I watch that?":
        $ adinemood += 1
        Ad "I suppose that depends on whether you will still be here when it takes place. It's part of a festival we hold in this town every year."

show adine normal b with dissolve
Ad "Okay, since it is my turn again, well..." 
show adine think b with dissolve
Ad "This might be an unusual question, so... When they said it was a human that would be coming here, I kinda expected something a little different."

menu:
    "That's not really a question.":
        $ adinemood -= 1
        $ renpy.pause (0.5)
        show adine annoyed b with dissolve
        Ad "You know what I mean..."
        show adine normal b with dissolve
        
    "Well, what did you expect?":
        $ renpy.pause (0.5)
        show adine normal b with dissolve
        Ad "I'm not sure exactly, but they do say it was humans that made us who we are today. You don't seem so different from us, though."
                
    "I know.":
        c "I know. Remy told me about some of the commonly held beliefs here."
        show adine normal b with dissolve

Ad "I mean, yeah, you do look different from us, but you're not really anything like some of the things that have been said about your kind."
c "I could say the same thing about you."
show adine think b with dissolve
Ad "Really?"
c "Yeah, we have plenty of myths about dragons."

show adine normal b with dissolve

Ad "Like what?"

menu:
    "There are too many to list.":
        c "There are just too many to list. Some of them good, some not so much."
        show adine think b with dissolve
        Ad "Sounds like what we have on you, actually. Now that I see one of you right in front of me, it's almost silly what some of the myths say."
        show adine normal b with dissolve
        
        $ mp.legends = "many"
        $ mp.save()
        
    "Dragons are greedy, man-eating monsters.":
        $ adinemood -= 1
        c "Well, according to some, you are greedy, man-eating monsters, and also sometimes associated with evil and the apocalypse."
        show adine disappoint b with dissolve
        Ad "Well, that's not very nice."
        show adine think b with dissolve
        Ad "Though to be fair, some of what we have about you isn't very nice, either."
        show adine normal b with dissolve
        c "Phew, good to know you aren't vicious monsters, then."
        Ad "Oh, we can be vicious if we want to be. We just usually know better."
        $ mp.legends = "bad"
        $ mp.save()
        
    "Dragons are noble creatures.":
        $ adinemood += 1
        c "They are often cited as a symbol of power and strength, but also one of wisdom, possessing an intellect that has no equal. They are noble creatures, and their depictions enjoy an almost universal appeal."
        Ad "I could get used to that, though it would be even nicer if it were all true."
        show adine think b with dissolve
        Ad "To be honest, I don't know if it's such a good idea to generalize like that - even if it's good things you're saying about us. We're all different, you know, and not all of us are nice."
        show adine normal b with dissolve
        c "I see."
        Ad "But then, we have said many good things about your kind, too."

        $ mp.legends = "good"
        $ mp.save()
        
c "Well, no matter what you might think about humans, I can assure you that I am in no way special or supernatural."
show adine think b with dissolve
Ad "I disagree with that."        
c "Why?"        
show adine normal b with dissolve
Ad "You say that you aren't special, but just the fact that you're here with us right now is quite special to me and many others. Just try to see it the other way around."
c "You know, you have a good point."
Ad "What were you thinking when you first heard about us?"

menu:
    "I thought it was a joke.":
        c "I thought it was a joke. Of course, all of that changed once I came through the portal."
        show adine giggle b with dissolve
        Ad "See, having something you've only heard about in stories turn out to be real is quite special."
        show adine normal b with dissolve

        $ mp.dragons = "joke"
        $ mp.save()
        
    "I was unsure.":
        c "I wasn't sure what to think about it. That is, until I got here and was standing in front of one of you. And after that, I was just rendered speechless."
        show adine giggle b with dissolve
        Ad "Told you so. It was special for you, too!"
        show adine normal b with dissolve

        $ mp.dragons = "unsure"
        $ mp.save()
        
    "I thought it was awesome.":
        $ adinemood += 1
        c "I thought making a discovery like this was just awesome. Many people would love to have the opportunity I had by coming here."
        show adine giggle b with dissolve
        Ad "See, it's not so one-sided after all, so don't be surprised if some of us feel the same way."
        show adine normal b with dissolve

        $ mp.dragons = "awesome"
        $ mp.save()

c "And it's not just the discovery of you dragons. We found a portal to an entirely different world. We still haven't figured that one out."
Ad "Neither have we."
c "I'm sure we'll find out soon enough."

show adine think b with dissolve

Ad "By the way, interesting selection of books you have there. \"Draconic Desire\", \"Ixomen Sphere\" - are these yours?" 
c "No, they were already here when I moved in."

show adine normal b with dissolve

Ad "Have you read any of them?"
c "I did read \"Sheridan and the Scepter of Sovereignty\"."
Ad "How did you like it?"

menu:
    "It was entertaining, but nothing special.":
        $ renpy.pause (0.5)
        show adine giggle b with dissolve
        Ad "\"Nothing special\" is a good way to describe the entire series, actually."
        show adine normal b with dissolve

        $ mp.sheridan = "neutral"
        $ mp.save()
        
    "I loved it.":
        $ adinemood -= 1
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "I see."
        show adine normal b with dissolve

        $ mp.sheridan = "good"
        $ mp.save()
        
    "It wasn't really my kind of thing.":
        $ adinemood += 1
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "I can see why."
        show adine normal b with dissolve

        $ mp.sheridan = "bad"
        $ mp.save()
        
Ad "Oh, you've got \"Price and Prayer\". You should totally read that one."
c "You think so? Why's that?"
Ad "It's not just an interesting story, it's based on true events. The author is so right when he says there's a lot we can learn from what happened back then."

menu:
    "I'm not sure if it's my kind of book.":
        $ adinemood -= 1
        $ renpy.pause (0.5)
        show adine disappoint b with dissolve
        Ad "It's more than just a book. I suppose it might not seem that important to someone who doesn't live here, though."
        show adine normal b with dissolve
        
    "I'll check it out when I have the time.":
        $ adinemood += 1
        Ad "Let me know when you do. I'd be interested in hearing what you have to say about it."
        
    "It's hard for me to find the time to read anything nowadays.":
        $ renpy.pause (0.5)
        show adine disappoint b with dissolve
        Ad "I know what you mean."
        show adine normal b with dissolve
        
Ad "Alright, since you asked about my family earlier, I'm going to do the same thing. Is there a Mr. or Mrs. [player_name] back home waiting for you?"
c "No, can't say there is."
show adine think b with dissolve
Ad "How about a potential Mr. or Mrs. [player_name], then? Are you looking to date anyone?" 

menu:
    "Maybe.":
        $ adinemood -= 1
        $ renpy.pause (0.5)
        show adine normal b with dissolve
        Ad "Come on, tell me!"
        jump tellme             
        
    "Not really.":
        Ad "I see. Anyone on your radar, then? Someone you think is attractive?"
        jump choiceb
        
    "Yes.":
        $ adinemood += 1
        $ renpy.pause (0.5)
        show adine disappoint b with dissolve
        Ad "Oh, it's a shame you can't be with them now, then."
        show adine think b with dissolve
        Ad "Or are you talking about someone you met here?"
        jump choicec
        
        
        
label tellme:        
    menu:
        "That's none of your business.":
            $ adinemood -= 1
            $ renpy.pause (0.5)
            show adine giggle b with dissolve
            Ad "Oh, I know what that means."
            show adine normal b with dissolve
            Ad "Is there anyone on your radar at least? Someone you think is kinda cute?"
            jump choiceb
        
        "There isn't really anyone.":
            Ad "I see. Anyone on your radar, at least? Someone you think is cute?"
            jump choiceb
            
        "Okay, there's someone.":
            $ renpy.pause (0.5)
            show adine disappoint b with dissolve
            Ad "Oh, it's a shame you can't be with them now, then."
            show adine think b with dissolve
            Ad "Or are you talking about someone you met here?"
            jump choicec

        
label choiceb:
    menu:
        "Well, there's someone.":
            $ renpy.pause (0.5)
            show adine disappoint b with dissolve
            Ad "Oh, it's a shame you can't be with them now, then."
            show adine think b with dissolve
            Ad "Or are you talking about someone you met here?"
            jump choicec
            
        "Not really.":
            $ adinemood -= 1
            $ renpy.pause (0.5)
            show adine giggle b with dissolve
            Ad "No one at all? I don't believe you. I think you just don't want to tell me. So, who is the lucky person?"
            jump nextsc
        
label choicec:
    menu:
        "Maybe.":
            $ renpy.pause (0.5)
            show adine giggle b with dissolve
            Ad "Oh my." 
            show adine think b with dissolve
            Ad "Would it happen to be someone I know?"
            jump choicee
        
        "No.":
            Ad "Oh. Well, that's a shame." 
            show adine think b with dissolve
            Ad "No one from around here catch your eye?"
            jump nextsc
        
        "Yes.":
            $ renpy.pause (0.5)
            show adine giggle b with dissolve
            Ad "Oh my." 
            show adine think b with dissolve
            Ad "Would it happen to be someone I know?"
            jump choicee 
        
label choicee:
    menu:
        "Maybe.":
            $ adinemood -= 1
            $ renpy.pause (0.5)
            show adine annoyed b with dissolve
            Ad "Well, who is it?" 
            jump nextsc
            show adine normal b with dissolve
            
        "Yes.":
            $ adinemood -= 1
            $ renpy.pause (0.5)
            show adine normal b with dissolve
            Ad "Well, who is it?" 
            jump nextsc
            
        "No.":
            Ad "I see."
            show adine normal b with dissolve
            jump nextsc
            
label nextsc:
    c "I'm not sure how many questions that was, but I'm sure it's not your turn anymore."
    
    show adine annoyed b with dissolve
    
    Ad "Are we even still playing this game?"
    
menu:
    "Well, you started it.":
        $ adinemood += 1
        $ renpy.pause (0.5)
        show adine giggle b with dissolve
        Ad "That's true. You seem to be enjoying it, though."
        show adine normal b with dissolve
        
    "Just having fun.":
        $ renpy.pause (0.5)
        show adine normal b with dissolve
        Ad "You and me both."
        
    "Sorry, you gotta play by the rules.":
        $ renpy.pause (0.5)
        show adine normal b with dissolve
        Ad "Well, go ahead, then."
        
c "You know, why don't we make this a little more interesting while we're at it?"
show adine think b with dissolve
Ad "What do you suggest?"
c "Truth or dare."
show adine normal b with dissolve
Ad "What's that?"
c "We continue asking questions, but if one of us doesn't want to answer the question, we have to do something the other person tells us to."
show adine disappoint b with dissolve
Ad "I don't even know what kind of dare I would make you do."
c "It could be something that would make me uncomfortable, or something you'd like to see me do."

show adine think b with dissolve

Ad "Anything?"
c "Well, keep in mind that revenge might be coming quicker than you think, so don't ask someone for anything you wouldn't do yourself."

show adine normal b with dissolve

Ad "Got it. So, who's first?"
c "You asked the last few questions, so it's only fair if I start."

show adine annoyed b with dissolve

Ad "Alright."

show adine normal b with dissolve

menu:
    "Which part of your body is the most ticklish?":
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "Probably my sides."
        show adine normal b with dissolve
        c "Good to know."
        show adine sad b with dissolve
        Ad "You wouldn't misuse that knowledge, would you?"
        c "Of course not."
        show adine normal b with dissolve
        
    "What is your most guarded secret?":
        Ad "I don't really keep secrets."
        c "That's not a real answer."
        Ad "But it's the truth."
        c "You know, you aren't very good at this game."
        show adine disappoint b with dissolve
        Ad "Hey, it's my first time."
        c "Don't worry about it."
        show adine normal b with dissolve
        
    "What's the most embarrassing thing that ever happened to you?":
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "Hmm, let me think..."
        show adine normal b with dissolve
        Ad "There was this one time when I was still a teenager. I was messing around and wanted to try out a new flying maneuver: a barrel roll. Needless to say, it ended badly."
        c "I guess you didn't succeed, then?"
        Ad "No, the roll itself went fine, but I lost control after that and plunged right to the ground."
        c "Oh, were you hurt?" 
        show adine disappoint b with dissolve
        Ad "No, luckily I wasn't too high when I did it, and there was a great puddle of mud on the ground right where I landed. Of course all my friends were there to see it."
        c "That wasn't enough to stop you from ever trying again?"
        show adine normal b with dissolve
        Ad "No. If anything, it only made me want to try harder."
        
Ad "Since it is my turn now: What is your greatest wish?"

menu:
    "World peace.":
        $ adinemood += 1
        c "More than anything, I'd want there to be peace on Earth."
        Ad "That is an honorable wish, [player_name]."

        $ mp.wish = "peace"
        $ mp.save()
        
    "Be the very best, like no one ever was.":
        Ad "That seems to be a very personal wish, [player_name]."

        $ mp.wish = "best"
        $ mp.save()

    "Be rich.":
        $ adinemood -= 1
        c "Be rich and have the freedom to do what I want to, whenever I want to."
        show adine disappoint b with dissolve
        Ad "I see."
        show adine normal b with dissolve

        $ mp.wish = "rich"
        $ mp.save()
        
c "Okay, my turn."
        
menu:
    "What would you do if you were invisible for a day?":
        $ adinemood += 1
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "Invisible, huh?"
        Ad "That's a hard one. I mean, no one would see my flying then, and I do want people to see that."
        c "Well, with this question it's more about what you would do if you had the opportunity to do something without getting caught, like something mischievous or criminal."
        show adine normal b with dissolve
        Ad "Oh, I know what I would do. I'd check out the building they found along with the portal."
        c "What building?"
        Ad "Didn't you hear about that? They found a whole building along with the portal."
        Ad "It's actually underground, and they have it heavily guarded while a team of archaeologists works on it. I think it might contain many secrets and answers about the portal and where it came from."
        c "Interesting. I think I'd like to check that out as well."
    
    "Are you scared of dying?":
        Ad "No, absolutely not."
        c "Why not?"
        Ad "Well, I do have some ideas of what might happen afterwards, but even if what I think isn't true, I'm not afraid of the unknown."
        show adine think b with dissolve
        Ad "In some sort of twisted way, I'm actually kinda curious to find out what it'll be like when it's all over."
        show adine normal b with dissolve
        menu:
            "That's... interesting.":
                $ renpy.pause (0.5)
                show adine think b with dissolve
                Ad "Aren't you curious as well?"
                c "Not this curious."
                Ad "I see."
                show adine normal b with dissolve
            "To be honest, I feel the same way.":
                $ adinemood += 1
                $ renpy.pause (0.5)
                show adine think b with dissolve
                Ad "I see."
                show adine normal b with dissolve
            "You know, if you're so eager to find out, I could help you with that.":
                $ adinemood -= 1
                $ renpy.pause (0.5)
                show adine annoyed b with dissolve
                Ad "That's not funny, [player_name]."
                show adine normal b with dissolve
                
    "What do you think is your biggest physical flaw?":
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "Well, I wouldn't really call it a flaw, but if I could change one thing, it would probably be these stripes on my muzzle." 
        show adine disappoint b with dissolve
        Ad "I don't like them very much."
        menu:
            "I think they're cute.":
                Ad "No matter if people like them or not, they always stand out. That's what I don't like."
                show adine normal b with dissolve
            "I agree with you there.":
                $ adinemood -= 1
                $ renpy.pause (0.5)
                show adine annoyed b with dissolve
                Ad "I know they aren't pretty. You don't have to repeat what I just said."
                show adine normal b with dissolve
            "I'm not sure I'd agree with that.":
                $ adinemood += 1
                $ renpy.pause (0.5)
                show adine normal b with dissolve
                Ad "But then you aren't the one who's supposed to answer the question."
        
Ad "If you knew the world was about to end, what would you do?"
menu:
    "Enjoy life to the fullest until the last moment.":
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "Going out with a bang, huh?"
        show adine normal b with dissolve
        $ adine1choice = "fullest"

        $ mp.worldend = "fullest"
        $ mp.save()
        
    "Say my last goodbyes and hope for the best.":
        $ adinemood += 1
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "An optimist until the very end. I like that."
        show adine normal b with dissolve
        $ adine1choice = "goodbyes"

        $ mp.worldend = "goodbyes"
        $ mp.save()
        
    "Stay outside and watch it all unfold before my eyes.":
        $ renpy.pause (0.5)
        show adine think b with dissolve 
        Ad "That would be quite a show, huh?"
        show adine normal b with dissolve
        $ adine1choice = "outside"

        $ mp.worldend = "outside"
        $ mp.save()
        
    "Hide in a bunker deep underground.":
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "I'm not sure if I could do that. I don't like tight, enclosed spaces."
        show adine normal b with dissolve
        $ adine1choice = "bunker"
        
        $ mp.worldend = "bunker"
        $ mp.save()

$ headgear = True
menu:
    "If you could come back with me to my world right now, would you do it?":
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "That's a very difficult question, you know."
        show adine normal b with dissolve
        Ad "Of course I'd love to visit - maybe as some sort of vacation. But if you're talking about permanently, I'm not sure if I could just pack up and leave everything behind just like that."
        
    "What's your biggest regret?":
        Ad "Oh my..."
        show adine disappoint b with dissolve
        Ad "..."
        Ad "I think it might be time for a dare now."
        c "Alright."
        menu:
            "Remove your headgear.":
                $ headgear = False
                $ renpy.pause (0.5)
                show adine normal b with dissolve
                Ad "Just that? That's not very hard."
                c "I thought I'd go easy on you, since it is your first time and all."
                Ad "I see."
                stop music fadeout 1.0
                scene black with fade
                play sound "fx/undress.ogg"
                $ renpy.pause(2.5)
                scene o2 at Pan((0, 250), (0, 250), 0.1)
                show adine giggle
                with fade
                play music "mx/serene.ogg"
                Ad "There. Satisfied?"
                show adine normal with dissolve
                c "Definitely."
                
                if persistent.c1disrobement == False:

                    $ mp.disrobement = True
                    $ mp.save()

                    $ persistent.c1disrobement = True
                    
                    $ achievement.grant("Disrobement")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_48
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You got Adine to remove her headgear!"
                        
                    elif system == "advanced":

                        s "You got Adine to remove her headgear. Wow."
                        
                    else:
                        
                        s "You got Adine to remove her headgear. Don't let it go to your head."
                
            "Kiss me.":
                $ renpy.pause (0.5)
                show adine think b with dissolve
                Ad "That's your dare?"
                c "Yep."
                Ad "..." 
                show adine annoyed b with dissolve
                Ad "Alright, whatever. I'll do it."
                stop music fadeout 1.0
                scene black with fade
                play sound "fx/kiss.wav"
                $ renpy.pause(1.0)
                scene o2 at Pan((0, 250), (0, 250), 0.1)
                show adine giggle b
                with fade
                play music "mx/serene.ogg"
                Ad "There, I did it. Satisfied?"
                show adine normal b with dissolve
                c "Definitely."
                
            "Bite into a lemon.":
                $ renpy.pause (0.5)
                show adine think b with dissolve
                Ad "Is that all?"
                c "You can find one in the pantry."
                show adine annoyed b with dissolve
                Ad "Alright."
                hide adine with dissolve
                play sound "fx/drmg.wav"
                $ renpy.pause(4.0)
                show adine normal b with dissolve
                Ad "So, should I just take a bite out of this one?"
                c "That's your dare."
                Ad "If you say so..."
                stop music fadeout 1.0
                scene black with fade
                play sound "fx/bite.wav"
                $ renpy.pause(1.0)
                c "(She didn't even peel it or anything...)"
                scene o2 at Pan((0, 250), (0, 250), 0.1)
                show adine normal b
                with fade
                play music "mx/serene.ogg"
                Ad "I'm not sure what's so special about that."
                c "You didn't mind at all?"
                show adine giggle b with dissolve
                Ad "Not a bit." 
                show adine normal b with dissolve
                c "..." 
                c "I see."
        
    "If I asked you to kiss me, would you do it?":
        $ renpy.pause (0.5)
        show adine think b with dissolve
        Ad "Is that your question, or is that already a dare?"
        c "A question. I just couldn't think of anything better."
        show adine normal b with dissolve
        Ad "Well, then my answer would be no. I don't kiss just anyone, you know."
        show adine giggle b with dissolve
        Ad "However, if it was a dare, my answer might be different."
        show adine normal b with dissolve

Ad "Alright, so from those you have met here so far, who is the one you fancy most?"
    
#menu:
#    "Anna.":
#        $ adinemood -= 1
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "Who's that?"
#        c "She works at the production facility where they are making our generators."
#        Ad "Wait, that Anna? "
#        c "You know her?"
#        
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#            
#        Ad "It's a small town. Everyone knows everybody here."
#        c "I see."
#        if headgear == True:
#            show adine annoyed b with dissolve
#        else:
#            show adine annoyed with dissolve
#
#        Ad "I didn't think you were that kind of person."
#        c "I'm not sure what you mean by that."
#        if headgear == True:
#            show adine giggle b with dissolve
#        else:
#            show adine giggle with dissolve
#            
#        Ad "Don't worry about it."
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#        
#    "Bryce.":
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "As in Bryce, the chief of police? You know him?"
#        c "Well, I've met him on more than one occasion now."
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#        Ad "Oh my. What's he like?"
#        
#    "Remy.":
#        $ adinemood += 1
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "Remy?"
#        c "He's actually the first one I met when I came here."
#        if headgear == True:
#            show adine disappoint b with dissolve
#        else:
#            show adine disappoint with dissolve
#            
#        Ad "I know him, yeah."
#        c "Is something wrong?"
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#            
#        Ad "Don't worry, he's a nice one."
#        
#    "Sebastian.":
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "Sebastian? I don't think I know him."
#        c "He's the little guy who works for the police."
#        Ad "Oh, I think I've met him before."
#        if headgear == True:
#            show adine giggle b with dissolve
#        else:
#            show adine giggle with dissolve
#        Ad "He's kinda cute."
#        
#    "Emera.":
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "Wait, are you talking about the Minister of Culture and Arts herself?"
#        c "Yeah."
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#        Ad "How well do you know her?"
#        c "Not very, I haven't actually met her yet."
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "I see."
#        
#    "Otomo Izumi.":
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "Can't say I've heard that name before."
#        c "Oh, right."
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#        
#    "Maverick.":
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "Maverick? The only Maverick I know is the one in the police force who got injured recently."
#        c "That's the one."
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#        Ad "Oh my."
#        
#    "Damion.":
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#        Ad "Who's that?"
#        c "He works at the production facility where they are making our generators."
#        if headgear == True:
#            show adine think b with dissolve
#        else:
#            show adine think with dissolve
#        Ad "Damion, Damion... Doesn't ring a bell."
#        if headgear == True:
#            show adine normal b with dissolve
#        else:
#            show adine normal with dissolve
#        
#    "[[Do a dare instead.]":
c "I think I'll take a dare for this one."

if headgear == True:
    show adine giggle b with dissolve
else:
    show adine giggle with dissolve
    
Ad "Oh, finally."

if headgear == True:
    show adine think b with dissolve
else:
    show adine think with dissolve
            
Ad "Hmm, what am I going to have you do?"
c "Whatever you like."

if headgear == True:
    show adine normal b with dissolve
else:
    show adine normal with dissolve
    
Ad "No, I honestly have no idea."
                       
c "Take your time."
        
if headgear == True:
    show adine think b with dissolve
else:
    show adine think with dissolve        
              
Ad "Alright, let me think for a minute."

#$ renpy.pause(1.0)                
#if headgear == True:
#    scene o3 at Pan((0, 250), (0, 250), 0.1)
#    show adine think b
#    with dissolveslow2   
#else:
#    scene o3 at Pan((0, 250), (0, 250), 0.1)
#    show adine think 
#    with dissolveslow2       
     
$ renpy.pause(1.0)    

c "Oh, looks like it's getting late."

#if headgear == True:
#    show adine think b with dissolve
#else:
#    show adine think with dissolve
    
Ad "Wait, what time is it?"

if headgear == True:
    show adine giggle b with dissolve
else:
    show adine giggle with dissolve
    
Ad "Whoops, seems like I've been here longer than I thought."

if headgear == True:
    show adine normal b with dissolve
else:
    show adine normal with dissolve
    
Ad "I probably should be going now."
c "Seems like the rain has stopped, too."
Ad "Yeah, that's great."


if adinemood >= 8:
    Ad "Anyways, if you want to invite me over again, why don't I give you my personal number and we just skip the part where you order food to make me come by?"
    c "But I like the food."
    
    if headgear == True:
        show adine think b with dissolve
    else:
        show adine think with dissolve
        
    Ad "Or maybe I'll get your number instead. Since you ordered from us, I already have it anyway."
    c "I'm not sure what to say to that."
    
    if headgear == True:
        show adine giggle b with dissolve
    else:
        show adine giggle with dissolve
        
    Ad "Take it as a compliment." 
    
    if headgear == True:
        show adine normal b with dissolve
    else:
        show adine normal with dissolve
        
    Ad "Bye!"
    
    hide adine with dissolve
    
    play sound "fx/door/doorclose3.wav"
    
    $ renpy.pause(2.0)
    stop music fadeout 1.0
    nvl clear
    window show

    n "She was gone as quickly as she had appeared, but given her enthusiasm, I doubted that was the last time I would hear from her."
    
    window hide
    
    $ persistent.adine1skip = True
    
    $ persistent.adine1choice = adine1choice
    
    $ persistent.headgear = headgear
    
    $ adinestatus = "good"

    $ adinescenesfinished = 1
    
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
    
elif adinemood >=0:
    
    label adine1skip:
    
    if headgear == True:
        show adine giggle b with dissolve
    else:
        show adine giggle with dissolve
    
    Ad "You know, if you want me to come over again, you don't have to order anything to do it." 

    $ persistent.adine1skip = True
    
    if headgear == True:
        show adine normal b with dissolve
    else:
        show adine normal with dissolve
        
    Ad "Here's my private number."      
    c "I'll keep that in mind, thanks."
    Ad "Bye!"
    
    hide adine with dissolve
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause(2.0)
    stop music fadeout 1.0

    $ adinestatus = "neutral"

    $ adinescenesfinished = 1

    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars

else:

    c "Will I see you again?"
    Ad "Well, you're always welcome to order food if you're hungry."
    c "That wasn't what I was talking about."

    if headgear == True:
        show adine annoyed b with dissolve
    else:
        show adine annoyed with dissolve
    
    Ad "Oh, I know." 

    if headgear == True:
        show adine disappoint b with dissolve
    else:
        show adine disappoint with dissolve

    Ad "Look, I don't want to be rude or anything, but I think it's better if we go our separate ways from now on. Sorry!"

    hide adine with dissolve
    play sound "fx/door/doorclose3.wav"
    stop music fadeout 1.0
    $ renpy.pause(2.0)
    stop music fadeout 1.0

    $ adinestatus = "bad"

    $ adinescenesfinished = 1

    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
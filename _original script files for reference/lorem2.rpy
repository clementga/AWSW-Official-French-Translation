#+11-13

label lorem2:

$ lorem2unplayed = False
$ lorem2mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Lorem 2"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Lorem 2"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Lorem 2"
    
else:

    $ save_name = "Chapter 1 - Lorem 2"

scene black with fade
$ renpy.pause (1.0)
scene loremapt at Pan ((128, 0), (0,72), 5.0) with dissolveslow

play music "mx/snowflake.ogg" fadein 2.0

play sound "fx/door/door_open.wav"

$ renpy.pause (2.0)

Lo "There you are. Come in!"

if persistent.lorem2skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_112

    call skiptut from _call_skiptut_33
        
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
            call skipcheck from _call_skipcheck_33
            
            scene loremapt at Pan ((0, 72), (0,72), 0.0)

            show lorem normal flip at Position (xpos = 0.3)
            with dissolvemed
            
            play music "mx/snowflake.ogg" fadein 2.0
            
            jump lorem2skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/snowflake.ogg" fadein 2.0

c "Sure."

show lorem shy with dissolve

Lo "Honestly, I can't believe you agreed to do this again."

menu:

    "Don't mention it.":
        
        pass

    "It's my pleasure.":

        $ lorem2mood += 1

    "I don't believe it, either.":
        
        $ lorem2mood -= 1
        

$ renpy.pause (0.5)

Lo happy "Now that I’ve had a chance to work through everything from last time, we can do some real work."

c "Sounds great."

Lo normal "I did a staggering amount of research on mythical humans. Here, let me show you some of the stuff I found."

c "Sure."

play sound2 "fx/fans.ogg"

m "We sat down at the coffee table. Lorem opened up a laptop and started to type away."

play sound "fx/keyboard.ogg"

m "Seeing the laptop brought back memories. In our world, they had become obsolete a long time ago."

Lo relieved "Before I show you these images, I should probably tell you that some of them are really weird. Just don't take them the wrong way."

c "You already told me about the four-headed human, so I think I can handle this."

Lo normal "Alright."

play sound "fx/clicks.ogg"

show black with dissolvemed

$ renpy.pause (0.5)

show snakeman with dissolvemed

$ renpy.pause (4.5)

hide snakeman with dissolvemed

$ renpy.pause (0.5)

hide black 
show lorem normal
with dissolvemed

$ renpy.pause (0.3)

menu:

    "That doesn't look very human to me.":
        
        $ renpy.pause (0.5)

        show lorem think with dissolve

    "He looks friendly.":

        $ renpy.pause (0.5)

        show lorem happy with dissolve
        
        $ lorem2mood += 1

    "He looks attractive.":

        $ renpy.pause (0.5)

        show lorem relieved with dissolve
    
        $ lorem2mood -= 1



Lo "This one is supposed to be one of our ancestors."

c "Ancestors? Well, it does remind me of some of the dragons I've seen here, but I'm not sure what humans have to do with this."

Lo normal "You remember the myth about our creator turning into a dragon, right?"

menu:

    "I don't think I've heard that one before.":

        $ renpy.pause (0.5)

        Lo relieved "I told you about it last time..." 

        Lo happy "The short version is that some believe we were created by a human. What happened to that human after we were made is a mystery, though. Some think they turned into a dragon and lived among us." 

        $ lorem2mood -= 1

    "Yeah.":

        $ renpy.pause (0.5)

Lo think "Now, here is an interesting question: What species did that human turn into?"

Lo "There are a number of dragon species nowadays that aren't genetically compatible with each other. Did the human choose one of them? Did they, perhaps, procreate?"

Lo happy "A shared ancestor is one option. This would mean that the different species split after the human’s involvement in our creation."

Lo normal "If human DNA was involved in some way, this might explain how our different species came to be."

Lo happy "Take a far ancestor of ours and apply various amounts of human DNA. The result would be a number of different species, each with a different amount of resemblance to humans."

menu:

    "Okay.":
        
        pass

    "This is getting weird.":
        
        $ lorem2mood -= 1

    "Interesting.":
    
        $ lorem2mood += 1

$ renpy.pause (0.5)

Lo normal "Now, it has been said that an upright stance and being able to walk on two legs is a more human trait."


menu:

    "Right.":

        $ lorem2mood += 1

    "Most humans walk on two legs, so that's true.":
    
        $ lorem2mood -= 1

    "I'm not sure I'd agree with that.":
        
        pass

$ renpy.pause (0.5)

Lo happy "In any case, it's one of the things that makes humans unique. As a result, some people believe that certain species share more traits with humans than others."

Lo relieved "They think it makes them more noble, or something. Luckily, this doesn't happen often."

c "You can walk on two legs as well, right?"

Lo normal "Sure. In this theory of shared human DNA, this puts me somewhere in the middle, since I still have wings and horns."

c "I can see that."

Lo think "Here, look at this one."

play sound "fx/clicks.ogg"
play sound2 "fx/fans.ogg"

show black with dissolvemed

$ renpy.pause (0.5)

show goblin with dissolvemed

$ renpy.pause (4.5)

hide goblin with dissolvemed

$ renpy.pause (0.5)

hide black 
show lorem normal
with dissolvemed

$ renpy.pause (0.3)

menu:

    "I wouldn't want to live in the same town as this fellow.":

        $ renpy.pause (0.5)

        Lo relieved "Well, you can't always choose your neighbours, and this won't be any different in my game."

        $ lorem2mood -= 1

    "I’m not sure if this is much closer than the previous one.":

        $ renpy.pause (0.5)

        Lo think "Not even a little?"

        c "Maybe a little."

    "What's with the little horns?":

        $ renpy.pause (0.5)

        Lo happy "Since we don't know what the original human looked like, we can’t exactly define which traits separate us from them. As a result, our interpretations of humans can vary wildly."

        $ lorem2mood += 1


c "I'm not sure he's a particularly friendly one, though."

Lo normal "Actually, I think this is supposed to be a human female."

c "Interesting."

Lo think "There are some that don't think humans are friendly at all, though."

c "Really? So far I've only heard positive things about us."

Lo relieved "Some interpretations of our myths don't exactly paint you in the best light."

Lo normal "There are also people who oppose the idea of human worship and what their involvement has meant for us."

c "In what way?"

Lo think "They say the human interference was unnatural and that we need to get back to our roots."

c "And how do they think they can do that?"

Lo normal "Apparently, it means refusing to use modern technology and living in caves or the wilderness again."

c "Like an animal."

Lo think "Pretty much. Most of us think those people are crazy, though."


menu:

    "They sound like the part, for sure.":
        
        $ lorem2mood -= 1

    "I see.":
        
        pass

    "As long as they aren't hurting anyone...":
        
        $ lorem2mood += 1


$ renpy.pause (0.5)

Lo normal "They're harmless, really."

Lo think "You probably won't see one of them around here, anyway."

c "This is an interesting style, though. Do you know how these pictures were made?"

Lo normal "No. I'm sure that information was provided when I looked them up in the library, but I didn't copy all of that."

c "And you're using these as references?"

Lo "I make do with what I can get."

Lo think "Maybe now you can see why I wanted your help, though."

c "Alright, what do you need me to do?"

Lo normal "I just want to make some quick sketches. You can stand over there by the wall."

c "Okay. I can certainly do that."

m "I walked up to the spot he indicated. When I took my place, I saw that he had laid out a number of pens, paper and other art supplies on the table."

c "Oh. This is going to take a while, isn't it?"

Lo "I'll try to be quick about it."

c "Do you want me to strike a pose or something?"

Lo think "A t-pose should be good to get started."

c "What's that?"

Lo happy "Just point your arms sideways, so you look like a giant t."

c "Oh, I get it."

m "Raising my arms to the sides, I wondered how long this would take."

Lo normal "Great. Now try to stay as still as possible."

menu:

    "I'll try.":
        
        $ renpy.pause (0.5)

    "I'm already regretting this.":

        $ renpy.pause (0.5)
        
        $ lorem2mood -= 1

    "Can I still talk?":
        
        $ renpy.pause (0.5)
        
        $ lorem2mood += 1

        Lo happy "Sure, as long as you don't talk with your arms."


show lorem think with dissolve

play soundloop "fx/scribbles.ogg"

m "As I wasn’t allowed to move my head, I stared at Lorem sketching my figure."

m "This went on for a few minutes, until I suddenly heard the sound of a door opening."

play sound "fx/door/door_open.wav"

$ renpy.pause (1.0)

show meetingipsum at Pan ((250, 0), (350,324), 7.0) with fade

$ renpy.pause (5.5)

hide meetingipsum

show lorem normal flip at Position (xpos = 0.2)

with fade

$ renpy.pause (0.2)

show ipsum normal at right with easeinright

if c4witnessavailable == True:

    "???" "Hey Lorem."
    
    show ipsum think with dissolve

    "???" "Oh, right. The human was going to visit today. I totally forgot about that. You don't mind if I take a seat, right?"

    stop soundloop fadeout 2.0

    Lo relieved flip "You just want to study [player_name]!"
    
    show ipsum happy with dissolve

    "???" "Like you aren't doing that right now. Besides, this room is mine as much as it is yours. I'll just watch and be quiet."

    Lo think flip "I thought you had experiments to run."
    
    show ipsum normal with dissolve

    "???" "And they are running. I’d rather not be confined to my tiny room for the next two hours, staring at the ceiling and waiting for them to finish."

    Lo relieved flip "But no experiments on [player_name]."
    
    show ipsum happy with dissolve

    "???" "Yes. I'll just sit here... and maybe take a few notes."
    
else:

    Ip "Hey Lorem."

    Ip think "Oh, right. [player_name] was going to visit today. I totally forgot about that. Are you still working with the police?"

    stop soundloop fadeout 2.0
    
    c "Yeah."
    
    Ip normal "You don't mind if I take a seat, right?"

    Lo relieved flip "You just want to study [player_name]!"

    Ip happy "Like you aren't doing that already. Besides, this room is mine as much as it is yours. I'll just watch and be quiet."

    Lo think flip "I thought you had experiments to run."

    Ip normal "And they are running. I’d rather not be confined to my tiny room for the next two hours, staring at the ceiling and waiting for them to finish."

    Lo relieved flip "But no experiments on [player_name]!"

    Ip happy "Yes. I'll just sit here... and maybe take a few notes."

Lo "I'm sorry, [player_name]. This is my roommate and long-time best friend, Ipsum."

c "Nice to meet you, Ipsum."

Lo happy flip "His scientific bluntness may be off-putting, so please bear with him."

Ip normal "Speak for yourself."

c "(So much for those two being best friends...)"

show lorem normal flip with dissolve

play soundloop "fx/scribbles.ogg"

m "Lorem returned to his drawing, the silence only being interrupted by the strokes of his pen."

#lorem normal, ipsum normal

if annadead == False:

    Ip think "Something interesting happened at work today."

    Lo think flip "Did they finally figure out it was you who was playing all those pranks?"

    Ip happy "No. They'll never catch me."

    Ip normal "I was talking with a colleague about the humans here and I offhandedly mentioned that [player_name] was going to come over."

    Lo relieved flip "I don't like where this is going."

    Ip "Some hours later, Anna barges into my office and says [player_name] is off-limits to anyone besides her as far as tests and experiments are concerned."

    Lo normal flip "Well, I'm not taking any samples. I could hardly be blamed for just looking at [player_name]."

    Ip think "Yes, but that makes me wonder: [player_name], did you agree to visit her and undergo her rigorous testing regimen?"

    menu:

        "I did.":
            
            $ renpy.pause (0.5)

            Ip normal "Oh. Good luck to you, then."

        "Not really.":

            $ renpy.pause (0.5)

            Ip normal "Evidently, she thinks otherwise."

        "Certainly not.":

            $ renpy.pause (0.5)

            Ip normal "Evidently, she thinks otherwise."



    Ip think "Oh, and Lorem: Have you seen my Ixomen Sphere recently?"
    
else:
    
    Ip think "By the way, have you seen my Ixomen Sphere recently?"

Lo think flip "Didn't you take it with you when we went to the park the other day?"

Ip normal "Yes, I did."

Lo normal flip "Well, that's the last time I saw it."

Ip sad "I must have lost it, then. I already searched the whole apartment."

Lo think flip "Did you go into my room?"

Ip normal "..."

Ip "No."

Lo relieved flip "..."

Lo normal flip "Maybe someone found it."

Ip "I had it registered in my name when I got it, so if anyone found it, it should show up sooner or later."



if persistent.orb_taken == True:
    
    
    m "I remembered the sphere that I had found in the park. I dug into my pocket to show it to them."

    c "Wait a minute, are you talking about..."

    Lo relieved flip "Hey, no moving around!"

    m "Quickly, I extended my arms again to make a perfect t-pose."
    
    show lorem normal flip with dissolve

    c "Sorry. I just found something in the park recently that may or may not be your Ixomen Sphere."

    Ip think "Where is it?"

    c "Probably in one of my pockets."

    m "At these words, Ipsum got up and walked over to me."

    Lo relieved flip "So much for just sitting quietly in the corner and letting me work in peace."

    Ip normal "We're talking about a very expensive piece of equipment here."

    Lo "Just give it to him, [player_name]."
    
    show lorem normal flip with dissolve

    m "I searched my pockets and looked for the sphere to no avail."

    c "Huh. It's not here."

    Ip think "So you don't have it after all? What kind of cruel joke are you playing here?"

    c "I must have left it in my apartment."

    Ip sad "What a shame."

    c "I could fetch it after we're done with this."

    Ip normal "It would be better if you just handed it to the police. After all, we don't even know if it is my sphere that you found. Either way, the police should be able to verify it and locate its owner."

    c "Alright."


c "What is an Ixomen Sphere, anyway?"

Lo think flip "It's just a glorified toy for grownups, really."

Ip think "You have no idea what you are talking about. An Ixomen Sphere is a very sophisticated tool with a countless number of uses."

c "Like what?"

Ip happy "It can levitate and follow you around, take photos. You can even use it as a calculator."

Lo happy flip "Making it a glorified toy for grownups."

Ip normal "I use it for my experiments."

c "Well, if they can take photos, I wouldn’t need to stand around like this – that is, if we had it here now."

Ip happy "It is a great companion for all situations in life."

Lo normal flip "It's much easier to draw from a live model than from a photo, though."

c "(Easier for you, maybe...)"

c "I hope this doesn't take much longer, because my arms went numb a while ago."

Lo think flip "Yeah, I think you can relax for now. I'm nearly done with this one."

stop soundloop fadeout 2.0

m "A tingling sensation went up my arms as I relaxed. Slowly, I began to regain feeling in them."

Lo normal flip "Alright, now turn around."

c "I thought we were done already." 

Lo happy flip "Not unless we want our humans to lack a backside."

Ip think "So that's what this is all about."

Lo relieved flip "Ugh. You know what I mean."

Ip happy "I know {i}exactly{/i} what you mean."

c "Isn't it my turn to draw you now?"

Lo "That's not how it works."

Ip normal "I wouldn't mind getting a portrait of myself. I can already see it, the light shining from above, carressing my luscious mane, highlighting each lock as they interplay..."

Lo "This is going to be a long day."

c "That depends on how fast you are."

show lorem normal flip with dissolve

play soundloop "fx/scribbles.ogg"

m "As I was now facing the wall, I couldn't see what Lorem and Ipsum were doing."

m "After a few seconds of silence, I heard some whispering coming from the couch."

c "What are you talking about?"

Ip think "I didn't want to be rude, but I was just curious about your vestments."

Lo happy flip "He said, and I quote: \"This would be more interesting if it wasn't for those clothes [player_name] is wearing..\""


menu:

    "Really?":
        
        pass

    "I see how it is.":
        
        pass

    "Coming here was a very bad idea.":
        
        $ lorem2mood -= 1


$ renpy.pause (0.5)

Ip normal "I'm just saying it would be hard to study an insect if there was a piece of cloth draped over it. Wearing that much just seems odd to me."

Lo normal flip "If humans wear clothes like this, it's only appropriate to depict them as such."
               
Ip sad "And my scientific curiosity shall remain unsatisfied."

show ipsum normal
show lorem happy flip
with dissolve

if annadead == False:

    Lo "Because [player_name] is not here to do that. And you would get in big trouble with Anna."

else:
    
    Lo "Because [player_name] is not here to do that."

c "We actually have a pretty big variety of \"vestments\". I could tell you about it."

Lo think flip "Sounds good, but not right now. I have to finish this up first."

c "Alright."

c "So, Ipsum, I've heard a lot about experiments and science now, but what do you actually do?"

Ip "I work in the facility as a biologist with a minor in physics." 

Ip happy "In addition to the office, I also have my own setup here at home - I assure you, it’s properly isolated from the rest of our apartment. It even has a fume hood to prevent accidents!"

Ip think "But I only use it for the smallest of experiments – usually things unrelated to my job."

menu:

    "Sounds boring.":
        
        $ lorem2mood -= 1

    "Okay.":
        
        pass

    "Sounds interesting.":
        
        $ lorem2mood += 1


$ renpy.pause (0.5)

Lo normal flip "Don't get him started, or we won't hear the end of it."

Ip happy "Maybe you would like to talk about your hobby instead, Lorem."

c "Isn't this already a hobby?"

Lo think flip "I guess you could say so."

Ip think "I was talking about his other hobby, though."

Lo relieved flip "Oh... that."

Lo shy flip "I don't know. It's a little embarrassing, to be honest."

c "There's no need to be embarrassed about your hobbies."

Ip happy "He likes flowers. Once, he even made a crown out of daisies. Cutest thing in the world."

Lo relieved flip "Don't listen to him. As usual, he only tells half the story."

c "What's the other half, then?"

Lo normal flip "I have an extensive love for botany."

Ip normal "The fern he keeps in his room must be the happiest plant alive."

Lo happy flip "I find gardening to be very relaxing, especially when the birds are singing in the morning! It’s so nice to go out there with a nice cup of tea and work in the garden of our apartment building."

Lo normal flip "Which reminds me - Ipsum here has quite an extensive tea collection! Although I’m not sure if he prefers to hoard tea or gadgets. It’s a mystery!"

Ip normal "I heard there was going to be a model of the Ixomen Sphere that can actually make tea. That's going to be a must buy."

Lo think flip "Can it also make cups, or are you supposed to sip it out of the sphere itself?"

Ip "Don't be silly."

c "You two sound just like an old couple."

Lo relieved flip "Couple? Us?"

Ip normal "Not really."

Lo happy flip "We've known each other for a long time, though, if that counts."

show lorem normal flip with dissolve

c "I think it does."

c "By the way, Ipsum, you're not from here, right?"

Ip think "What is that supposed to mean?"

c "Well, you look nothing like any other dragon I've seen here so far."

c "I suppose that's true for Lorem as well. You're both pretty small."

c "But you, Ipsum, also have hair. That's certainly new."

Ip normal "It’s not as unusual as you might think, but you’re right… There aren’t many of us in these parts."

c "I imagine being smaller than the rest of the population would come with its own challenges."

Lo happy flip "It's not that big of deal. If something is unreachable for me, I can fly!"

Ip happy "This apartment was actually intended to house one dragon of a bigger size. That not only makes it fairly cheap, but it's also big enough for both of us."

c "There's one thing I've been wondering: How do you even sit in one of those chairs? Wouldn't the backrest cause problems with your tails?"

Lo think flip "I see what you mean. For me, it's never been a problem, because most chairs are bigger than I am."

Ip normal "It's just a question of getting into the right position." 

Ip "However, this might be different from those of us who mostly walk on four legs, but they usually don't use chairs like these at all."

Lo normal flip "I've seen a few try, though."

Ip think "I suppose they want to imitate humans this way. Even if they can't stand or walk like a human, they can try to sit like one."

Lo happy flip "With varying results. Some I've seen looked really funny, trying to fit in chairs they are too big for, or sitting in odd ways that clearly don't work with their anatomy."

c "I see."

c "Lorem, you asked me about breath weapons last time, but I don't think you ever told me if you had one."

Ip think "Probably because it isn't worth mentioning."

Lo normal flip "It may only be a very small flame, but it can get very hot."

c "What about you, Ipsum?"

Lo happy flip "Yes, Ipsum. What about you?"

Ip happy "My breath weapon is elocution, since words are more powerful than anything else."

show ipsum normal with dissolve

menu:

    "Sure...":
        
        $ lorem2mood -= 1

    "Same as mine, then.":
        
        $ lorem2mood += 1

    "Okay.":
        
        pass
        

$ renpy.pause (0.5)

stop soundloop fadeout 2.0

Lo normal flip "Alright, I'm done with this one. You can turn around."

menu:

    "Really? But staring at the wall was so much fun.":

        $ renpy.pause (0.5)
        
        $ lorem2mood += 1

        show lorem happy flip with dissolve

    "Does this mean we're done?":

        $ renpy.pause (0.5)
        
        $ lorem2mood -= 1

        show lorem relieved flip with dissolve

    "Sure.":
        
        $ renpy.pause (0.5)
        
        show lorem think flip with dissolve



Lo "Let's make one more. Maybe something dynamic."

c "How dynamic are we talking about?"

Lo normal flip "Something that isn't static like the reference models I just did."

Lo think flip "You can strike a pose. Something that's just... you."

c "Alright."

c "(What kind of pose should I go for?)"


menu:

    "A normal pose.":

        c "Alright, what about this?"

        Lo normal flip "Works for me."

    "A thoughtful pose.":

        c "Alright, what about this?"

        Lo think flip "Works for me."

    "A swimwear pose.":

        c "Draw me like one of your..."

        Lo think flip "My what?"

        c "Err.. forget what I just said."

        Lo shy flip "Sure."



Ip think "By the way, did you get the groceries when you came home from work?"

Lo happy flip "Yes, just as usual."

c "Are you two sure you're not in a relationship?"

Ip normal "I certainly am."

Lo normal flip "Actually, Ipsum is deeply in love with his home laboratory."

c "Oh, really?"

Ip happy "I'm not even going to deny that. When I'm not working on something at the office, I do so here."

#new here

c "What are you currently working on?"

Ip normal "I've been looking into the physics of teleportation."

c "You're talking about the portal, right?"

Ip think "Well, I don't have permission to even approach the portal, so I have to resort to a theoretical discussion on its mechanics and make do with what I can pull off in my home laboratory."

c "Maybe I could tell you a few things."

Ip normal "That won't be necessary. I have already read all the available test reports."

c "Okay."

Ip think "Are you aware that using the portal could be incredibly dangerous?"

c "I'm not sure what you're talking about."

Ip "Then you don't have a complete understanding of what the portal actually does and what it means for our world at large."

Ip happy "In order for a portal to function, a natural wormhole is required. It is trapped and becomes the portal's entry."

Ip normal "The portal manipulates the wormhole's exit. This way, something can be sent to whichever destination is chosen."

Ip think "Now, there is a theory about the purpose of the natural wormholes in the universe."

Ip happy "It states that they act as the support pillars of the space-time continuum."

c "How so?"

Ip think "Hmm, how should I explain this?"

Lo happy flip "I think the video game analogy worked pretty well."

Ip normal "Sure. In a video game, what happens when you meet the edge of a map?"

c "You hit a wall?"

Lo normal flip "That happens in some games, but in others..."

c "You reappear on the opposite side."

Ip happy "Right."

Ip think "How does this happen? If our world was a perfect sphere, someone could just keep flying in the same direction and, eventually, they would end up at their starting point again."

c "Sure."

Ip normal "This is just a result of physics. In the abstraction of a video game, however, it doesn't work like that."

Ip "They don't try to replicate a spherical world, but use a 2D plane instead."

c "This is getting confusing."

Ip "Imagine a piece of paper with a world map printed on it."

c "Right."

Ip think "While it shows the entirety of the world, it's still just a simple, flat piece of paper rather than a sphere, right?"

c "Sure."

Ip normal "Let us assume that in a game, our world map looks like that."

Ip "Now, what happens when we approach the edge and walk over it is that we are teleported to the opposite side."

c "Okay."

Ip happy "This doesn't actually make the game world a sphere, but rather a torus."

c "A torus?"

Lo happy flip "You know, like a donut."

show lorem normal flip
show ipsum think
with dissolve

Ip "If that's the comparison you want to make..."

c "Okay."

Ip happy "Now, things are going to get really complicated."

Ip think "Are you familiar with the many-worlds interpretation of quantum mechanics?"

c "Let's say I'm not."

Ip happy "It states that every single time a choice is made by any actor that possesses free will, the universe splits off into different branches."

Ip normal "This means that for every choice you have made, there exists a branch of the universe where you made a different decision."

c "I see."

Ip "Now, we can't communicate with these other branches in any way. You don't know what would happen if you had made a different decision just this morning."

Ip think "You could make an educated guess, but the only person who truly knows what would happen is that alternate you who has made that decision and is living its consequences."

Ip "That is, unless we could communicate with those other branches."

Ip normal "However, there is a barrier that prevents us from doing that."

Ip happy "This barrier is made up of wormholes."

c "How does that work?"

Ip "It is very similar to the torus world model that is used in games. As we approach the edge of our own world, the barrier causes us to end up on the other side instead."

c "Does this mean we get teleported to the other side, like in video games?"

Ip normal "Not necessarily. It would be just as correct to assume that our universe is shaped like a torus."

c "So, which is it, then? Do we get teleported or not?"

Ip think "That depends on how you look at the wormholes’ function."

Ip normal "Imagine this sheet of paper is the entirety of our world..."

m "He took a sheet of paper from Lorem's stack and showed it to me, marking a spot near the edge with a pen."

Ip think "... and this is where you live."

Ip normal "Unfortunately, your workplace is here, on the other side."

m "He drew an x close to the right edge of the paper."

Ip "If the world was flat, this would be very unfortunate."

Ip think "However, if the world was a torus, the left and right edges would be connected. You could take the shorter route to work by going over the edge."

Ip normal "Now, let's say that this is only possible because wormholes connect these two edges together."

Ip think "If you happened to be right at the very edge and looked beyond, everything would look perfectly fine for you." 

Ip "Given that these wormholes stay in their place, you would never know that the world is actually flat and that you can only travel to the other side because the wormholes connect the edges."

Ip normal "You would think that the world is a torus."

c "Right."

Ip think "However, what if the wormholes don't actually bring you to the other side by teleporting you, but instead just bend the paper into the torus shape and hold the edges together?"

Ip normal "If these wormholes failed or were displaced, the paper would unfold, throwing the world into disarray."

Ip "That's what the wormholes and the barrier actually do. They are what hold everything together."

c "So they're really more like glue."

Ip think "If it wasn't for them, the overall construct would collapse in on itself."

c "What construct?"

Ip normal "The entirety of space-time."

Ip think "Now if these theories are true, that would mean using a portal damages the barrier. Each time the portal is activated, the wormhole used for the teleportation is displaced, leaving a small gap where it used to be."

Ip "Do this too often and the overall system will destabilize eventually."

Lo think flip "Alright, maybe you shouldn't talk about your theories about how the world is going to end."

show lorem normal flip
show ipsum normal
with dissolve

Ip "Nothing is going to happen because the portal was used a few times. I just hope humanity is aware of its implications."

c "Maybe we can collaborate."

#snip end

Ip think "I certainly hope so."

c "Your researchers seem to know what they are doing."

Ip normal "I just wish I could be a part of it. With everything that's going on, the future looks incredibly exciting."

c "What do you think is going to happen, Ipsum?"

Lo relieved flip "Now you'll get him started. Don't say I didn't warn you."

Ip happy "The knowledge contained within your PDAs could propel innovation forward by unseen lengths."

Lo normal flip "Meaning a lot more experiments for you to do."

Ip normal "Which would be terribly exciting."

Lo think flip "Personally, I'm more interested in the social implications."

c "What do you mean?"

Lo normal flip "I don't expect there to just be a back and forth of ambassadors forever."

c "Are you talking about colonies?"

Ip "Oh, I bet Lorem would jump at the opportunity to live in the human world."

c "I'm not sure if that would be a good idea."

Ip think "Why not?"

Lo happy flip "Obviously, such an endeavour would need a lot of preparation. We would need to learn about their culture and adjust appropriately."

Lo think flip "I'd expect we'd send an ambassador over there long before that will happen, though. We hardly know anything about their world."

c "Everything's still up in the air as far as diplomatic relations go. We have no idea what the situation could be like in just a week."

Lo happy flip "Yes, and it's all so incredibly exciting! "

Ip normal "Don't get too excited, though, or else you're going to ruin your drawing."

Lo normal flip "It's almost done, anyway."

stop soundloop fadeout 2.0

Lo happy flip "Here, what do you think?"

play sound "fx/paper2.ogg"

m "Lorem leaned over, holding up the paper to Ipsum."

m "Ipsum looked at the paper closely, his gaze shifting back and forth between me and the paper several times."

m "After a few seconds, he seemed to be finished with his evaluation."

Ip think "As a scientist, my professional opinion is that this part looks a little long."

m "He pointed his sharp claw at a part of the paper Lorem was holding."

Lo think flip "Are you sure? Let me see."

play sound "fx/paper.wav"

Ip normal "If I wasn't sure, I wouldn't have said it."

Lo normal flip "I think you're right."

Ip happy "That I am."

play sound "fx/eraser.ogg"

m "Lorem reached for his eraser, purging a few lines from the paper before he switched to his pen again."

Lo happy flip "And it's done."

Ip happy "See, what would you ever do without me?"

Lo think flip "I don’t think I’d hear as many explosions in the middle of the night."

Ip normal "You were happy about it when you forgot to set your alarm that one time."

Lo relieved flip "Hrmph."

play sound2 "fx/silence.ogg"

queue sound2 "fx/alarm.ogg"

m "Suddenly, the sound of an alarm resounded throughout the room."

Ip happy "Oh, my experiment is done."

$ renpy.pause (0.2)

show ipsum normal flip

$ renpy.pause (0.3)

hide ipsum with easeoutright

$ renpy.pause (0.2)

show lorem at Position (xpos = 0.2) with ease

Lo normal flip "And there he goes. Charming fellow, isn't he?"

menu:

    "He sounds fun.":

        $ renpy.pause (0.5)

        Lo happy flip "He certainly keeps things interesting around here. And he's a good art critic."

        c "I can imagine."

        $ lorem2mood += 1


    "Yeah.":

        $ renpy.pause (0.5)

        Lo think flip "He certainly keeps things interesting around here. And he's a good art critic."

        c "I can imagine."

    "I can't stand him.":

        $ renpy.pause (0.5)

        Lo relieved flip "It's a good thing you're not his roommate, then."

        $ lorem2mood -= 1




Lo normal flip "Anyway, looks like we're done here."

c "Phew. It feels good being able to move again."

if lorem2mood >= 9:
    
    
    Lo happy flip "Would you like to stay for dinner? It’d be the least I can do to compensate for your lost afternoon."

    c "Let me see. What time is it?"

    c "It's getting late and I probably shouldn't stay out this long. Looks like I'll have to decline for now."

    Lo think flip "I see. Well, I gotta do something for you, at least."

    c "It was my pleasure. Minus having to stay still for the whole time, this was actually quite fun."

    Lo normal flip "How about I invite you again, then?"

    c "Sure. Works for me."

    Lo happy flip "I'll think of something special."

    c "Just give me a call sometime and we'll figure out the rest."

    Lo normal flip "Sure. Bye!"
    
    $ loremstatus = "good"
    
    $ loremscenesfinished = 2
    
    $ persistent.lorem2skip = True
    
    stop music fadeout 2.0

    $ renpy.pause (0.5)

    if chapter4unplayed == False:
            
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars

    jump chapter2chars



elif lorem2mood >= 2:


    label lorem2skip:
        
        Lo "Would you like to stay for dinner? It’d be the least I can do to compensate for your lost afternoon."

        c "Let me see. What time is it?"

        c "It's getting late and I probably shouldn't stay out this long. Looks like I'll have to decline for now."

        Lo think flip "I see. Well, I gotta do something for you, at least."

        c "Don't worry about it. Maybe some other time."

        Lo normal flip "If you say so."

        Lo happy flip "Thanks for doing this, at any rate. It's been a huge help."

        c "Yeah, I know. Don't worry about it. Really."

        Lo normal flip "Alright."

        c "I should really get going now."

        Lo "Sure. Take care!"

        $ loremstatus = "neutral"
        
        $ loremscenesfinished = 2
        
        $ persistent.lorem2skip = True
        
        stop music fadeout 2.0

        $ renpy.pause (0.5)

        if chapter4unplayed == False:
                
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars

        jump chapter2chars


else:
    
    Lo "I can't thank you enough for doing this." 

    c "You should stop. It's getting really annoying."

    Lo think flip "Oh, I guess you don't want to stay for dinner then."

    c "Haven't I given you enough of my time already?"

    Lo relieved flip "Just forget it, okay?"

    c "I should be going now, anyway. It's getting late."

    Lo "Sure. Bye."

    $ loremstatus = "bad"
    
    $ loremscenesfinished = 2
    
    stop music fadeout 2.0

    $ renpy.pause (0.5)

    if chapter4unplayed == False:
            
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars

    jump chapter2chars





















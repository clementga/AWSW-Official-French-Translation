label remy4:

$ remy4unplayed = False
$ remy4mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Remy 4"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Remy 4"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Remy 4"
    
else:

    $ save_name = "Chapter 1 - Remy 4"

if persistent.playedzhong == True:
    define Fv = Character("Zhong", color="#7e9147", image="zhong")

scene black with dissolvemed
$ renpy.pause (0.5)
scene o4 at Pan((0, 250), (0, 250), 0.1) with dissolvemed

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(Oh, that must be him.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

show remy normal c with dissolve

#insert skip here

if persistent.remy4skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"
    
    call syscheck from _call_syscheck_105

    call skiptut from _call_skiptut_28
        
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
            call skipcheck from _call_skipcheck_28
            
            scene np2x at Pan((0, 250), (0, 250), 0.0)
            show remy shy
            with dissolvemed
            
            play music "mx/campfire.ogg" fadein 2.0
            
            jump remy4skip1
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            #play music "mx/campfire.ogg" fadein 2.0

play music "mx/campfire.ogg" fadein 2.0

c "Remy, what's that on your face?"

Ry smile c "Don't you know what it is?"

c "Well, it looks like lipstick, but I didn't know that was a thing here."

Ry normal c "You're right, it is lipstick. It's not something that existed in this world before, though."

c "How did you get some, then?"

Ry smile c "I have one of your PDAs, remember? I studied it a bit and came across the entry on lipstick. Based on the necessary ingredients, I realized I could make some myself, and so I did."

c "Did you do this to look pretty for me?"

Ry normal c "I just figured you’d miss these kinds of things – things that are normal for you." 

c "It hasn't really been normal back home in quite a while. Lipstick isn't common these days."

c "Didn't the entry specify that it's typically used by females?"

Ry "Now that you mention it, I did get that impression, but I found the sentiment a bit puzzling. Why would a product like this only be used by one gender?"

c "Well, I guess social norms dictated that certain traits are only desirable in one gender, thus highlighting them like this would increase the attractiveness."

Ry "Oh, I think I get it now. It's all based on sexual dimorphism. The biological differences between the sexes are much greater in your species than it is in ours, so I suppose the traits you are looking for can be different, too."

Ry "Generally speaking, sexual dimorphism is much greater in mammals than it is in reptiles." 

Ry "While it can vary wildly by species, external indicators are pretty much always present. Like mammaries, for example - an always-present and often obvious reminder."

Ry shy c "This makes so much more sense now. It's kind of embarrassing."

Ry "Should I... get rid of it?"

menu:
    
    "Yes.":
        
        c "Yes. It doesn't really look nice on you."

        Ry "Oh, sorry."
        
        hide remy with dissolve
        
        #$ renpy.pause (0.3)
        
        play sound "fx/wipe.ogg"
        
        $ renpy.pause (1.5)
        
        show remy normal with dissolve
        
        Ry smile "Here, that should do it."

        $ mp.remylipstick = "no"
        $ mp.save()


    "No.":
        
        c "No, leave it on. It's not as if people here would know about its history."

        Ry normal c "I suppose that's true."

        c "Besides, the thing about females wearing it isn't really a hard rule, and there are males who do it too. Anyone can wear it if they want to, really."

        Ry smile c "Well, if you say so."

        Ry normal c "Still, it's kind of uncomfortable, so I think I'd rather take it off."

        c "Uncomfortable?"

        Ry "I suppose it's not really suited for our scales."

        hide remy with dissolve
        
        #$ renpy.pause (0.3)
        
        play sound "fx/wipe.ogg"
        
        $ renpy.pause (1.5)
        
        show remy normal with dissolve
        
        Ry smile "Here, that should do it."

        $ mp.remylipstick = "yes"
        $ mp.save()
        
        
c "Shall we go, then?"

Ry normal "Actually, it seems we're pretty early. They're probably still setting up."

c "I see. Well, we could just stay here in the meantime."

Ry smile "Oh, for sure."

show remy normal with dissolve

#play sound "fx/door/doorclose3.wav"

#$ renpy.pause (0.5)

Ry "I just realized I haven't actually been in here since I prepared the apartment for you."

Ry "Have you read any of the books I got you?"

c "Oh, so you're the one who stocked the bookshelf?"

Ry "They're all library books. I wanted to provide you with a good sample of what we have to offer, so there should be something in there for anyone."

Ry "Looks like you've read a few books in the Sheridan series."

menu:
    
    "They're pretty interesting.":
        
        Ry "Oh, really?"

        c "I know they're not exactly high-brow, but they're entertaining. And what more do you want a book to be?"

        Ry smile "I guess we all have our own tastes."

    "I just wasn't in the mood for anything more complex.":

        c "Usually, I wouldn't read something like this, but sometimes I'm just not in the mood for anything more complex."

        Ry smile "Oh, I understand. Everyone has their guilty pleasures."



c "Can I offer you some food or drink? I've barely used any of the stuff in the kitchen."

Ry normal "Why not?"

c "I didn't want to touch anything that didn't at least resemble something I know. After all, I have no idea how to prepare them right or even know if they are safe for me to eat."

Ry "Maybe it wasn't such a good idea to get you all those perishables then. I wanted to provide you with a bit of everything, considering I had to prepare the apartment for someone I didn't really know much about."

c "Oh, some of them were good. It's interesting to taste the subtle and sometimes not-so-subtle differences in the similar fruits we have back home."

Ry "Did you throw anything out?"

c "Not really. Why do you ask?"

Ry "You've been here for nearly two weeks now, so even if some of them were safe for you to eat, they probably aren't anymore." 

Ry "Let me clean out your closet. We don't want to have any health hazards for you here, after all."

c "Well, feel free."

hide remy with dissolve

$ renpy.pause(0.3)

play sound "fx/slide.ogg"

$ renpy.pause(1.0)

Ry "Just look at this!"

show remy look with dissolve

m "He showed me a juicy-looking, vaguely spherical fruit whose bright red color was unlike any other fruit I had ever seen."

c "That's a very bright red. I don't think even our best apples could compare."

Ry "Well, they're usually blue. Red means you're supposed to throw them away, as they have expired by then and toxins might have already set in."

c "Oh. Well, I wasn't planning on eating it anyway."

Ry "Or this one, it's all moldy!"

c "I don't see any mold."

Ry "Don't you see these spots?"

c "Sure, but if that's supposed to be mold, it looks very different from the mold we have back home."

Ry "I see."

Ry shy "Maybe it wasn't such a good idea to stock up on perishables. I didn't consider all the implications of doing something like this. Had you eaten the wrong thing, you could be in a hospital right now."

c "Don't stress yourself out about it. Honestly, someone would have to be pretty reckless to just go ahead and start munching on things they don't know about."

c "If anyone was smart enough to be sent here, they probably wouldn't take a risk like that."

Ry smile "Well, I'm glad to hear it."

Ry normal "Nevertheless, I better get rid of everything that's past its date. We don't really want the mold in the air, either."

c "If you say so."

hide remy with dissolve

m "Once more, he dove into the closet. I heard him rummaging around as he checked the fruits and vegetables thoroughly."

play sound "fx/rummage2.ogg"

$ renpy.pause (2.0)

show remy smile with dissolve

Ry "That should be everything."

c "Thanks."

c "I bet the wine didn't go bad, though. Do you want some?" 

Ry normal "I'm not really a big fan of wine."

c "How come?"

Ry "I just can't enjoy it as some others do, I suppose. I'm willing to try anything at least once, though."

c "Anything?" 

Ry "Well, at least as far as food and drinks are concerned." 

menu:
    
    "Let's try some together, then.":

        $ mp.teetotaler = "no"
        $ mp.save()
        
        $ renpy.pause (0.5)

        Ry smile "Well, if you want to."

        c "Sure."

        c "What kind of wine is this, anyway?"

        Ry normal "I'm not sure, I just grabbed it when I got all the other stuff."

        c "Don't tell me you just went for the cheapest one."

        Ry smile "Of course not. Everyone knows that you don't just buy the cheapest stuff. You go for the second cheapest."

        c "Oh, well."

        c "What kind of... container should I get for you, anyway?"

        Ry normal "We're having wine, so let's go for wine glasses. The stem actually makes it possible for me to grip it with my vestigial thumb, so there shouldn't be any problems."

        c "Alright."

        play sound "fx/pouringwine.ogg"
        
        $ renpy.pause (2.0)

        c "Here you go."

        Ry "What shall we drink to?"
        
        menu: 
            
            "An interesting afternoon.":

                $ renpy.pause (0.5)

                Ry smile "Alright. To an interesting afternoon and whatever it may bring."

            "A wonderful friendship.":

                $ renpy.pause (0.5)

                Ry smile "Alright. To a wonderful friendship."

            
            "Whatever.":

                $ renpy.pause (0.5)

                Ry smile "Alright. To whatever, then."



        play sound "fx/clink.ogg"
        
        $ renpy.pause (1.0)

        show remy normal with dissolve

        m "I took a sip from my wine glass. Remy really hadn't been kidding about getting the second cheapest bottle, because that was exactly what it tasted like."

        c "How do you like it?"

        Ry "Must be an acquired taste, I think."

        Ry "How about you?"

        menu:
            
            "It's alright.":

                c "It's okay. I mean, you can't really expect much from a cheap bottle of wine."

                Ry "I see."
                
            "It's bad.":

                c "It's bad. I'm not surprised that you don't like it either."

                Ry smile "Maybe I should buy the third cheapest next time."

                c "Maybe."

                show remy normal with dissolve


    "I'm not a fan either.":
        
        
        c "I'm not a fan either, so I guess we don't need to waste a good bottle of wine by opening it."

        Ry "I'm not sure if this one would qualify as a \"good bottle\"."

        c "Don't tell me you just went for the cheapest one."

        Ry smile "Of course not. Everyone knows that you don't buy the cheapest stuff. You go for the second cheapest."

        c "Oh, well."

        show remy normal with dissolve
        
        
Ry "Just look at the time. I think we could start heading to the festival now."

c "Sure, let's go."

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene town7 with dissolvemed

show remy normal with dissolve

Ry "This is strange. Usually there'd be a crowd by now."

c "Do you think they canceled it? With Reza still being out there, maybe they thought it wasn't a good idea to have a public spectacle like this."

Ry "Cancel the summer festival? Inconceivable!"

c "It doesn't really look like a festival is going on right now, though."

Ry "I don't know what's going on."

c "Hey, I think I know this guy. Let's go and ask him."

show remy at right with ease

show zhong normal c flip at left with easeinleft

Fv "Hey, [player_name]. How can I help you?"

c "We were just planning to go to the festival, but it doesn't seem like there's much going on here yet."

Fv "You came to the right place, but the festival is not starting for another hour, at least."

Ry "What? But the festival has always started at this time."

Fv "You must have missed the memo, then. They moved it by an hour. Something about the daylight and making the fireworks more visible as a result."

Ry "Well, that's a shame."

c "And I'm kinda getting hungry, too."

Fv "I can help you with that."

c "What are you selling?"

Fv "Skewers, meat balls. All kinds of grilled things, really."

Ry smile "Well, I could go for some meat balls. How about you?"

show remy normal with dissolve

menu:
    
    "I'll also take the meat balls.":

        $ mp.vegetarian = False
        $ mp.save()
        
        pass

    "How about some veggie skewers?":
        
        pass

    "Just some grilled cheese for me.":
        
        pass


Fv "No problem, just let me pack this up for you."

play sound "fx/unwrap.ogg"

$ renpy.pause (0.5)

Ry "I guess this makes us your first customers of the day. What do I owe you?"

Fv "For you two, it's free."

Ry "That's very kind of you. Thank you."

Fv "Have fun at the festival."

c "Thanks!"

$ renpy.pause (0.2)

hide zhong with dissolve

show remy at center with ease

c "So, what do we do now? Should we go back?"

Ry "Well, we're already here and got all this stuff. Let's just sit down somewhere."

c "Sure."

scene np2x at Pan((0, 100), (0, 250), 3.0) with dissolveslow

m "We went off to the side as more dragons arrived and started setting up their various booths."

c "How are the meat balls?"

show remy normal with dissolve

Ry "They're actually pretty good. How about your stuff?"

c "It's great. I'm surprised, honestly. You never know with stuff that comes out of food carts."

Ry "You're right. Maybe we got lucky."

c "Or maybe it's because it's still fresh."

Ry smile "Who knows."

c "What was that about fireworks, though? Is the big show coming up later?"

Ry normal "Oh, no. The festival is just getting started, and there are fireworks every day. But the big show is what everyone wants to see. That one is happening in a few days. It officially concludes the festivities."

c "I see."

m "A while later, the festival had kicked off and the crowds were already coming in. Dragons of all shapes and colors filled the paths, ready to see the sights the festival had to offer."

m "Booths lined both sides of the way. It reminded me a lot of a typical carnival setup, with the booths being filled with shops, food stands, games and much more."

c "Seems the festival has already started. Let's go."

Ry "You know what, how about we just stay here? I really don't like crowds."

Ry "I've seen the festival so many times already, I'd rather just stay here with you."

c "I thought you wanted to show me around, but I suppose we can just stay here if you'd prefer that."

Ry "The main attraction is always the big fireworks show at the end of the festival, and that one is not going to happen today, anyway."

c "So, why'd we need to come here in the first place, then? Is something wrong?"

Ry "I just had to realize that as nice as it is right now, you'll have to leave this world again eventually."

Ry shy "I've been alone for such a long time now. I didn't even have a single friend."

Ry "In my job, I always have to smile when serving the customers. How could I be surrounded by people all the time, yet feel so alone?"

Ry normal "All those people have their own lives, families, friends and relationships. Yet I had none of that. In a world where everyone else seemed to be happy, I was the odd one out who had to pretend in order to belong."

Ry shy "How could that not have eaten away at me, day after day?"

Ry normal "Yet, one day, I heard about the plans of the humans coming here."

Ry "Like many others, I was very excited at the prospect of our myths coming true."

Ry "And then, the day came when Reza stepped through the portal - amidst all the pomp and fanfare you could imagine. It was quite a sight to behold, really."

Ry "You wouldn't believe how much joy I felt during that moment. Emera, of course, took all the limelight she could. First there was a big speech in front of a huge crowd, then a procession after she had officially welcomed Reza."

Ry "When it was time for you to arrive and it was decided that it wouldn't be a public event this time due to security concerns, I knew that Emera wasn't going to be there if she wasn't able to make it all about herself."

Ry shy "I begged her to let me do it, just to be able to get this close to a human at least once. To talk with them and see what they were like - to experience them."

Ry "She told me that if I did a few favors for her, I could be the one to greet you." 

Ry sad "I knew that she wasn't going to be there anyway, but if I didn't do what she wanted, she would just send some other lackey instead."

Ry "So I did everything she asked for."

Ry normal "She did keep her word, though - and in the end, I was the one who would introduce you to this little world of ours."

Ry "It might not have seemed like much to you, but with just us two and no one else being there, it was something very special for me."

Ry "It was not just some public spectacle like the summer festival or Reza's arrival, but for the first time in so long, I felt like that moment was about you and me - and no one else."

Ry "For someone in my position, it just made me very happy to have such an extraordinary thing happen to me."

Ry "Of course I was very curious to see how much our myths would line up with reality, and I was even more overjoyed when you visited me in the library."

Ry "When you accepted my invitation and came into my home, I was just glad to have you there."

Ry "It seemed like you wanted to be there and weren't just someone out to use me in some way. I began to feel hope."

Ry "When I met you in the park, I think the only reason I could tell you everything about myself was because I knew you were going to leave again eventually."

Ry "And now, after all of this, I can hardly believe you're still here with me."

c "Why wouldn't I be?"

Ry shy "You're just so nice to me."

Ry "Yet, even after the time I've got to spend with you, it seems that soon, I'll have to let you go again."

label remy4skip1:

Ry normal "At least I got to know you."

if remygoodending == True:

    Ry "And thanks to you, I was also able to reconnect with Adine. Now, it just seems so petty to not have spoken with her for such a long time."

    Ry "All those times when I felt alone and depressed, I really was only a phone call away from someone who still cared about me."

    c "But now that you have, this also means that your worst times are over. You're not alone anymore."

    Ry smile "That is true."

    Ry normal "To some people, it may not matter much if they have one friend more or less. But you know what makes the biggest difference? Having one when you didn't used to."

    Ry "We even went to the orphanage together some time ago to help with the kids there. It seems one of them has taken quite a liking to me."

    c "That sounds lovely."

    Ry "Her name is Vara, and she -"

    c "Vara? I remember her."

    Ry "You know about her, then? It's such a sad story."


else:
    
    c "It can't be all that bad. Ever since I came here, I've met plenty of lovely people - all with their own relationships, struggles and dreams." 
    
    c "I know you think you've been alone here all this time, but don't go back into that kind of thinking when I'm gone."

    c "Rather, why don't you take it as an opportunity? Now that we're here, who's to say that you won't be able to find others once I'm gone?"

    c "I know you're still stuck for a while because of your job, but after that, have you considered a change of scenery?"

    c "You could move to a different place, with all new people and opportunities. Who knows what you might find elsewhere?"

    Ry "A completely new start? I like that idea."
    

Ry "But enough about me."

#insert skip here

if persistent.remy4skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_106

    call skiptut from _call_skiptut_29
        
    if skipbeginning == False:

        if system == "normal":
        
            s "My records indicate you have already experienced this scene in a satisfactory manner. Would you like to skip to the end?"
        
            #play sound "fx/system3.wav" #was already blanked out here
        
            #s "Warning: In this scene, skipping ahead this way instead of using the skip buttons (CTRL and TAB) may prevent you from experiencing alternative choices and outcomes that you haven't seen before. These may only be minor, though."
        
        elif system == "advanced":

            s "It looks like you've seen this before. Skip to the end of this scene?"
        
            #play sound "fx/system3.wav" #was already blanked out here
        
            #s "I have to warn you, though. If you do this here instead of just using CTRL and TAB, you may end up missing some minor changes you haven't seen before."
            
        else:
            
            s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip to the end of this scene."
            
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
            call skipcheck from _call_skipcheck_29
            
            scene o4 at Pan((0, 250), (0, 250), 0.0)
            show remy normal
            with dissolvemed
            
            play music "mx/campfire.ogg" fadein 2.0
            
            jump remy4skip2
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/campfire.ogg" fadein 2.0

Ry "What will you do once you get back to your own world again?"

c "I'm not sure. I don't even know what will happen to me when I return."

c "These last few days, a lot of things have happened that have changed my perspective on what I'm doing here, Reza and those who sent me."

Ry "Is that a bad thing?"

c "I don't know yet. At the very least, though, I can say that I've done what I believed was right."

Ry "You should be careful with rhetoric like that."

c "What do you mean?"

Ry "That kind of talk makes it very easy to justify any means when it serves the right cause, whatever that may be. The more important thing is: Have you done anything that you might regret?"

Ry "No matter what you think, keep in mind that you may be held accountable for your actions by others or even yourself."

Ry "Don't just do something because you think it's for the right reasons. Do it when you are aware of the possible consequences as well."

c "You're right. I have no way of knowing what my actions here will amount to once I return."

Ry "Do you really wish to go back to your own world?"

#c "Even if I had a say in the matter, I don't think it would be a good idea to go against them now." 

c "If I didn't, it would only serve to strain the relationship we've been trying to build with your people here, which is something that could be elementary for our survival."

c "Besides, I didn't do it for those who reign over the city back home, or those who might've wanted to betray me."

c "Let's not forget that even under the worst regimes there are just normal people trying to survive, too."

c "If I have the power to make a difference for them, would it be right for me to just leave them be in order to seek my own happiness? That's exactly the kind of thing you were talking about, right?"

Ry "In the end, we all have to make our own decisions."

c "If I leave them behind, then I leave them to people like Reza and those who sent me here."

Ry "What would you want to do? Overthrow them?"

c "I don't even have the complete picture myself right now. How could I even consider what to do, given what I know?"

c "What I do know, though, is that if I don't do what they expect of me, there will be consequences."

Ry "Maybe you'll just have to wait and see."

c "That's not an option right now. Reza is still out there, armed and dangerous."

Ry shy "Don't you think that's a matter better left to our police force? It could be very dangerous for you to interfere."

c "It's far too late to reconsider. I've already been tangled up in this too much. Besides, I can't stop now." 

c "Don't forget how many he has killed already. He won't hesitate to do so again in order to reach his goal."

c "In the end, it’s my duty to stop him. If I don’t, how would your people look at humanity?"

c "How could I face you again, knowing that my negligence could cause suffering and loss for others here if I just stopped now?"

Ry normal "I wish I could be as brave as you."

c "Don't think bravery has anything to do with it. He must be stopped, one way or another."

Ry "I know. Just be careful, alright?"

c "I'll try."

Ry "We've been here for a while now. How about I walk you back to your apartment?"

c "What about the festival?"

Ry "Well, if you still want to go, we could watch the big fireworks show together in a few days."

c "That's an idea."

Ry smile "Alright, let's do that."

show remy normal with dissolve

m "I watched Remy as he got up again, stretching himself in a way that reminded me of a cat before we prepared to leave again."

scene town7 with dissolvemed

$ renpy.pause (0.2)

show remy normal at right with easeinright

show zhong normal c flip at left with easeinleft

c "Oh, you're still here. How's business?"

Fv "As expected. People always get hungry at these events eventually."

Fv "Can I offer you some more meat balls?"

Ry "No, thanks. I'm quite full from my earlier helping."

Fv "How about you, [player_name]?"

c "A tempting offer, but we're just about to call it a day."

Fv "I see. Are you going to watch the big fireworks at the end of the festival?"

c "That's the plan."

Fv "Be sure not to miss it. You haven’t seen anything until you see the fireworks!"

c "That's what everyone keeps telling me."

Ry smile "Because it's true."

show remy normal with dissolve

c "Anyway, we should probably get going."

Fv "Have a good day, then."

c "You too."

scene o4 at Pan((0, 150), (0, 250), 3) with dissolveslow

$ renpy.pause (1.3)

show remy normal with dissolve

c "And here we are again."

Ry "Indeed."

c "Did you want to clean out my bathroom cabinet as well or something?"

Ry smile "That's a good one."

show remy normal with dissolve

m "He gave a big sigh."

label remy4skip2:
    
$ persistent.remy4skip = True

Ry "You know how I feel. I guess I just wanted to make the most of this day."

if remystatus == "neutral":
    
    c "We're still going to see the fireworks together."

    Ry smile "That's true."

    Ry normal "You know, I'm very curious to see what your reaction to that will be. It's quite a sight to behold."

    c "People just keep saying that."

    Ry "Maybe you will, too."

    c "We'll see."

    Ry smile "Thanks for the wonderful day, though."

    c "Likewise."

    Ry normal "Until we meet again."

    c "See you."
    
    hide remy with dissolve

    stop music fadeout 2.0
    
    play sound "fx/door/doorclose3.wav"

    $ renpy.pause (2.0)
    
    $ remyscenesfinished = 4

    if chapter4unplayed == False:
                            
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
else:
    
    c "Speaking of which, I've never actually seen you without your tie."

    Ry "Well, actually..."
    
    hide remy with dissolve
    
    play sound "fx/undress.ogg"
    
    $ renpy.pause (2.0)
    
    show remy smile b with dissolve
    
    Ry "How about now?"

    c "You are pretty cute, you know that?"

    Ry normal b "Is that just a term of endearment, or are you actually serious?"

    c "I am serious."

    m "He looked at me, hesitating. Then, he took a step forward, his head slowly moving closer to my own."
    
    show remyrom at Pan((580, 326), (350, 0), 8.0) with fade
    
    $ renpy.pause (6.0)
    
    #hide remyrom with fade
    
    #$ renpy.pause (0.3)

    menu:
        
        "Look away.":

            hide remyrom 
            hide remy
            with fade
    
            $ renpy.pause (0.3)
            
            m "When I made the motion to dodge his advance, he stopped in his tracks immediately."

            show remy shy b with dissolve

            Ry "I'm sorry, I just thought..."

            c "Don't worry about it. I'm just not sure if I can do this."

            Ry normal b "Well, it's getting late, so I should probably go now."

            Ry "Do you still want to see the fireworks?"

            c "Oh, for sure."

            Ry "I'll see you, then."

            c "Until we meet again."

            Ry "Thank you for everything."

            $ remystatus = "neutral"

            hide remy with dissolve

            stop music fadeout 2.0
            
            play sound "fx/door/doorclose3.wav"

            $ renpy.pause (2.0)
            
            $ remyscenesfinished = 4

            if chapter4unplayed == False:
                                    
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars
                
                
        "Kiss him.":

            hide remyrom 
            hide remy
            with fade
    
            $ renpy.pause (0.3)
            
            m "We met, and my arms enveloped his neck as our lips touched. For a few seconds, we were closer than ever before. During the kiss, he used a lot more tongue than I expected."
            
            #hide remyrom with dissolvemed
            
            m "Just after we parted, he finished by giving me a small lick on the cheek."

            show remy smile b with dissolve

            Ry "How was that?"

            c "Unique, that's for sure."
            
            Ry normal b "Maybe I shouldn't wear the tie anymore if this is what happens when I take it off."
            
            c "Actually, I think you should keep it."
            
            Ry "Really?"
            
            c "Yeah. It looks good on you."
            
            Ry smile b "Well, if you say so."
            
            Ry normal b "Anyway, it's getting really late, so I should probably get going now."

            Ry "Don't forget about the fireworks."

            c "Oh, for sure."

            Ry "I'll see you, then."

            c "Until we meet again."

            Ry "Thank you for everything."

            $ remystatus = "good"

            $ mp.remyromance = True
            $ mp.save()

            hide remy with dissolve

            stop music fadeout 2.0
            
            play sound "fx/door/doorclose3.wav"

            $ renpy.pause (2.0)
            
            $ remyscenesfinished = 4

            if chapter4unplayed == False:
                                    
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



$ renpy.pause (0.3)

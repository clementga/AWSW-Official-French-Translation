label adine4:

$ adine4unplayed = False
$ adine4mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Adine 4"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Adine 4"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Adine 4"
    
else:

    $ save_name = "Chapter 1 - Adine 4"

scene black with dissolvemed
$ renpy.pause (0.5)
scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(That must be her.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

play music "mx/funness.ogg" fadein 2.0

show adine normal b with dissolve

Ad "Hey, [player_name]."

c "Hey, Adine."

Ad giggle b "Are you ready to go?"

c "Sure am! I can't wait to see everything the festival has to offer."

if persistent.adine4skip == True:

    stop music fadeout 1.0
    
    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_107

    call skiptut from _call_skiptut_30
        
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

            $ renpy.pause (0.5)

            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_30

            scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow

            $ renpy.pause (1.3)

            show adine normal b with dissolve

            play music "mx/fireplace.ogg" fadein 2.0
            
            jump adine4skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/funness.ogg" fadein 2.0

Ad normal b "Oh, I'm sorry if it came across that way, but I don't think we'll actually have much time to take part in the festivities."

c "Oh, really?"

Ad "Yeah, I'll have to spend most of my time at the competition grounds. We'll arrive there early so I can check in and do my warmup, and I'll still have to stick around after my performance to wait for the awards ceremony."

Ad think b "Well, I guess you don't have to wait with me. You could see the rest of the festival if you wanted to."

c "That's out of the question. I'm here to spend time with you. The festival is not that important."

Ad normal b "Besides, we can always see everything on one of the other festival days."

c "True."

Ad "We could even watch the big fireworks show at the end."

c "Yeah, I've heard about that. Everyone keeps telling me how important it is for me to see."

Ad giggle b "It's not that important, but if you have the opportunity, you really should go."

c "I'm not sure if I'll be able to attend, but I'd gladly accompany you if I have the chance."

Ad normal b "Sure. So, today's agenda is emotional support, and next time, we can take in all aspects of the festival. Sound good?"

c "Perfect."

Ad giggle b "Alright. Let's go then."

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene town7 with dissolvemed

#show adine normal with dissolve

m "It took a while for us to arrive at the festival, which had already begun by this point. The last of the booths that lined the way were still being set up, but dragons of all shapes and sizes were already pouring in."

m "Instead of walking directly through the festival, we stayed outside the established paths, heading towards the stage where the competition was going to be held."

scene black with dissolvemed

$ renpy.pause (0.5)

scene fac12 with dissolvemed

m "Eventually, we arrived at a rather large open air area near the facility that had been roped off. At one corner of the building, a few flyers had already gathered."

show adine normal b with dissolve

Ad "Maybe you should wait here while I get my number."

c "Why?"

Ad giggle b "People might get the wrong idea if you show up in the registration line."

Ad think b "Besides, they'd certainly stare and start asking all kinds of questions."

c "Alright, I'll just stay here, then."

Ad normal b "I'll be right back."

hide adine with dissolve

m "After Adine had waddled off to the other flyers, I surveyed my surroundings idly."

m "Beyond the big open air area, seating had been provided, and I could already see a few people waiting for the competition to start. A few had even gathered on the roof of the building to watch from there. "

show adine normal b with dissolve

Ad "I'm back!"

c "Is that your number?"

m "She held up a piece of cloth with a large number printed on it. A few straps were hanging from it."

Ad giggle b "What, this? No, of course not. This is [adinestagename]'s number."

c "Of course. Sorry for the mistake."

Ad normal b "I'm one of the last to start, actually."

c "Are we late?"

Ad "No, I guess the others just arrived earlier to have more time to get ready."

c "What do you think about the other competitors?"

Ad think b "I've seen most of them fly before. Some are really, really good."

Ad normal b "It doesn't seem like there are many newcomers here. So, right now, I'm the odd one out."

c "Maybe you could use that to your advantage."

Ad think b "How so?"

c "Well, you know more about them than they do about you. Having a promising newcomer there might throw them off their game."

Ad normal b "I'm not so sure about that. After all, it's not as if any of our already choreographed performances would change based on what others do now. Each of us just tries to do their best."

Ad think b "Most of them are seasoned flyers, so they already know how to deal with that kind of pressure. If anything, I'm the one who might get nervous and mess up."

Ad normal b "I do have one advantage, though. I'm still pretty young, and this is a sport with a great amount of wear and tear."

Ad think b "There comes a certain point in time when you just can't perform as well anymore as you used to." 

Ad "Many complicated maneuvers can only be performed by younger athletes. The older ones can make up for it using their experience, and with better execution of easier moves."

Ad normal b "In the end, a daring newcomer like me could surprise the audience and the judges with something new and unexpected, which is exactly what I plan to do."

c "How good do you think your chances are?"

Ad think b "With a bit of luck, I might even be able to win. This is just a local competition, after all."

Ad normal b "But you know what? Just being here right now and performing in front of so many people is a win for me. People will know me, and I'll probably get a mention somewhere in a local paper."

Ad "I've trained for years, and my application to compete finally got accepted. Now I just have to make the most of it, and I'll be happy."

Ad "I still can hardly believe that I'm here. This is the moment I've worked so hard for."

c "And I'll be watching you."

Ad giggle b "Oh, stop it. You're making me nervous."

c "Sorry."

Ad think b "Can you help me with this?"

m "She spread out her wing, and only then did I notice that her shoulder joint was tightly bandaged."

c "What's that for?"

Ad normal b "It's just a training bandage to stabilize my shoulder after that little blunder you witnessed last time. We can't fly with these in the competition though, so I'll have to take it off."

c "Okay."

play sound "fx/bandage.ogg"

m "I opened the bandage, carefully unwrapping her wing."

stop sound fadeout 2.0

c "There you go."

Ad "Thanks!"



m "She spread both of her wings, beating them a few times. I couldn't help noticing that the previously bandaged wing was sagging noticeably compared to its counterpart, as if it were misaligned."

show adine think b with dissolve

m "She seemed to be examining her shoulder, somewhat lost in thought when I spoke up."

c "Are you sure you want to do this?"

Ad giggle b "Yes, of course. Why wouldn't I?"

c "I can see you're straining without the bandage."

Ad normal b "I'm fine, really. Don't worry about it."

c "If you're fine without the bandage, how come you were wearing it up to just now? Did you need  it for practice, too? If you couldn't practice without it, maybe you aren't ready to compete without it yet."

Ad annoyed b "Since when are you suddenly an expert on flying? I'm the one who has been doing this for years, not you. This is my dream we're talking about."

c "Do you want them to see you in this condition and judge you based on that rather than when you're at your best?"

Ad disappoint b "I.. just have to try, you know?"

c "What if something goes wrong, though? You don't want to be in that position."

Ad "If I start making excuses now, maybe I'll never stop. I'll always be too nervous, or too injured, or didn't eat right the day before. I feel bad enough as it is."

Ad "Right now, I have the chance to do this. And if I don't take it, maybe I never will."

Ad "I'll always just be a server and delivery girl making minimum wage."

Ad "Is this one chance really too much to ask for?"

c "No, but it doesn't have to be right now. There will always be another year."

c "They've never seen you compete before. If you fly now, they'll judge you based on this performance. You only have one chance at making a first impression, and you know it won't be your best if you fly right now."

c "If it's not good enough, maybe they won't invite you again next year. If you fly now, they won't accept any excuses. But if you tell them you're injured, they might let you fly another time."

Ad "But I don't want to wait another year. I want to do it now. I trained so much, even with this injury, and you tell me I should just let it go?"

c "I just can't help thinking about last time. If you crash like that again, there's no sand here to cushion your fall. It would be much worse."

Ad annoyed b b "You think I don't know that? That I'm not already worrying about this more than I ever have for anything else? I just don't want to make excuses anymore." 

Ad disappoint b "I don't want to wonder if I'll ever amount to anything more than a waitress. I want to be able to follow my dream, and I don't want to wait another year to find out."

c "What about Amely? If something happened to you, how do you think they would explain to her that you just suddenly stopped showing up, huh?"

Ad frustrated b "Don't you dare bring her into this! She has nothing to do with it."

c "Like it or not, what you are doing could have consequences, and there are others besides you who will be affected if something goes wrong."

Ad "You know what? I will fly and do the best damn job I've ever done, and there's nothing you can do to stop me."

hide adine with dissolve

m "Before I could reply, she angrily stomped off towards the building, where by now a number of contestants had arrived."

m "While I had failed to convince her, at least I could say that I had tried my hardest to stop her."

m "I asked myself whether I even wanted to watch the competition at that point. It was possible that she'd do even better than expected, but if my experience was any indication, her performance would not turn out well."

m "In the end, I decided to stay and watch from the sidelines. I didn't want to join the rest of the audience, as I was sure it would get me unwanted attention."

m "After the competition started, I lost myself in thought, thinking over the conversation I had with Adine while watching the other contestants halfheartedly."

m "Adine had been right. Some of them really were very good, but based on what I had seen at her practice session, she did have a shot at winning if everything went well for her."

m "Even though my rational mind doubted that would happen, for her own sake I hoped it would."

m "One by one, the contestants showed off their skills in a variety of moves, usually followed by the applause of the audience. Eventually, it was time for Adine's turn."

"Announcer" "Next on the stage is number 11. A promising newcomer who will show her skills to the public here for the very first time in her debut performance. Please welcome [adinestagename]!"

m "There was an excited bout of clapping. The audience was always curious to see a newcomer on the stage."

m "However, after a few seconds passed, Adine still hadn't emerged."

m "An awkward silence set in as the audience's applause stopped and everyone sat anxiously, waiting for her to show up."

m "She never did. After half a minute or so had passed, the announcer's voice once more echoed across the area."

"Announcer" "My apologies. It looks like number 11 will not be flying today. Next up is number 12, a certain veteran you may know for his somewhat unusual technique..."

m "Before I could even ask myself what had happened, I saw Adine walking out of the building and coming towards me."

show adine disappoint b with dissolve

c "Adine! What did you do?"

Ad "Let's just go somewhere else."

c "Okay."

stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolvemed

$ renpy.pause (1.0)

scene np2y at Pan((0, 100), (0, 250), 5.0) with dissolveslow

play music "mx/amb/night.ogg" fadein 5.0

$ renpy.pause (2.2)

m "We walked away from the festival and sat down under a tree in the outskirts of town. As the competition was already nearly over, the darkness had already set in."

show adine think b with dissolve

Ad "Here should be good."

c "So, what made you reconsider?"

Ad disappoint b "You were right with everything you said."

Ad "When I was inside and had a bit of time to cool off, I realized I didn't want to do it like this, even if I'd have to wait another year."

c "How do you feel now?"

Ad "I know it was the right thing to do, but I can't help thinking that I just came so close. That I could've done it if it hadn't been for that stupid accident."

c "You'll have another chance, I promise."

Ad "Don't make promises you can't keep."

c "..."

Ad normal b "Hey, [player_name]. Look at the sky. Can you see that light? The one that looks a bit brighter than all the others?"

hide adine with dissolve

#show np2y at Pan((0, 250), (0, 0), 1.5)
show np2y at Position(xpos=0.0, xanchor='left', ypos=0.0, yanchor='top') with ease

m "I looked up and saw many celestial bodies lighting up the sky. One of them was noticably brighter than all the other stars."

c "Yeah."

#show np2y at Pan((0, 0), (0, 250), 1.5)
show np2y at Position(xpos=0.0, xanchor='left', ypos=-250, yanchor='top') with ease

show adine normal b with dissolve

Ad "I usually practice in the evening and stay until it's dark, so I see the stars pretty often. I noticed something about that one. It moves."

c "How does it move? It looks pretty stationary to me."

Ad "You won't notice it just by looking at it, but over the last couple of weeks I have noticed that it has changed positions when comparing it to other stars."

c "It can't be a star, then. Stars don't move."

Ad think b "They have an office in one of the cities that watches these kinds of things. I called them about it a while ago."

c "What did they say?"

Ad normal b "It's just an asteroid passing by. It's even been on the news a few times."

c "That makes it sounds pretty important."

Ad giggle b "Yeah. It's a big one, apparently. Otherwise we wouldn't even be able to see it without a telescope."

c "Do they think it's dangerous?"

Ad think b "Why would it be?"

c "I don't know. It could hit the moon, or something like that."

Ad normal b "They assured me that's not going to happen. They say calculating the paths of celestial bodies is a very complicated science, and not really an exact one." 

Ad "They know it's not going to hit the moon, but they're watching it to make sure it passes safely."

c "Not that just watching it would make a difference."

Ad "They don't really know anything more. Apparently, they're also really underfunded. The council doesn't see the need to \"waste people's time and money to look into the sky all day\"."

c "That's strange, don't you think?"

Ad think b "It used to be a pretty important job. But over time, the funding got less and less until only this token office in our biggest city was left."

c "I see."

Ad normal b "It's such a shame, since the whole institution was based on our creation story."

c "In what way?"

Ad think b "In one of the stories, our creator told us to \"watch the skies\"."

c "How religious are you, really?"

Ad normal b "What exactly do you mean?"

c "Well, dragons have these myths about humans. How many of them do you actually believe are true?"

Ad giggle b "Oh, I believe all of it. I just love reading all the stories, theories, and all that."

c "Why is that?"

Ad normal b "Well, I think there's a lot we can learn from it. Much of our society is based on it, including our laws and traditions."

c "I see."

c "Can I ask you a question?"

Ad "Sure, go ahead."

c "What would you think if I told you that I am a time traveller from the future?"

Ad annoyed b "Hey, don't joke about something like that." 

c "Why not?" 

Ad normal b "Because I'd believe you."

Ad think b "Besides, if you were really a time traveller, I'd think you'd come from the past. Like the time when we were created." 

c "Really? Why is that?"

Ad "Because that's the only time in our history where we know of humans ever being here. If you came from the future, that would mean humans were to show up at some point in our future history, and I'm not sure how or why that would happen."

c "Wouldn't that mean that I was your creator?"

Ad normal b "Well, not necessarily. There could've been other humans around, right?"

c "Your myths only mentions one, though."

Ad think b "Yeah, but people speculate, trying to find explanations for those old myths. Maybe, there were more humans around, and they just died. Or their creation rebelled and killed them. Others say they fled across the ocean. We just don't know."

c "What do you think?"

Ad normal b "I don't know. I like reading about all the theories and trying to piece the puzzle together myself. That's why I want to visit that underground building we found. Some of the theories are quite out there."

c "Like what?"

Ad think b "For example, one says that humans are really aliens who came from a different planet. They created us for some reason, and then just vanished again."

c "What would they do that for?"

Ad "Maybe it's an experiment and they're testing us. Some say they're always watching us from up there somewhere with a giant mothership and that maybe, one day, they'll return when we're ready to join them."

c "That is pretty out there, I'll say."

Ad giggle b "Told you so."

Ad normal b "What about the humanity you come from, though? Why don't you tell me more about your world?"

c "I don't like talking about that. It's much prettier here."

Ad annoyed b "I don't believe you."

c "It's the truth."

Ad normal b "I'll believe it when I see it with my own eyes. I'd love to visit your world."

c "I don't think it would be a good idea to visit us right now."

Ad think b "Why not?"

c "Do you know what our world is like? Are there any rumors about that?"

Ad normal b "Not really. There hasn't been much speculation about that yet. Of course we're curious, though. Next time, we want to send one of our ambassadors into your world, to make it even and all that."

c "I'm not sure if that's a good idea."

Ad annoyed b "Don't be so negative."

c "I'm sorry. It's not up to me to determine the best course of action. I'm just a lowly ambassador, after all."

Ad giggle b "Not quite as lowly as a waitress with nothing more than high aspirations."

Ad normal b "Maybe it's time for me to go home."

c "I would walk you, but I guess you'd be faster if you flew."

Ad think b "Nah, I'd rather not without the bandage."

c "Are you serious? And you were going to do your performance like that?"

Ad disappoint b "I know, I shouldn't have tried. You don't have to bring that up again."

c "I'm sorry. For what it's worth, I think you made the right decision in the end."

Ad normal b "Thank you."

c "Shall we go, then?"

Ad "Sure."

stop music fadeout 2.0

$ renpy.pause (0.4)

scene black with dissolvemed

$ renpy.pause (0.5)

#scene town4 at Pan((0, 0), (0, 0), 0.0) with dissolvemed

scene adineapt2 at Pan ((300, 300), (128,300), 3.0) with dissolveslow

play music "mx/fireplace.ogg" fadein 2.0

c "There we are."

#show adine normal b with dissolve

Ad giggle b "Do you want to come in for a bit? Would be a shame for you to have come all this way for nothing."

c "Sure."

#hide adine with dissolve

m "She opened the door, wiping her feet on the doormat before she went inside."

#$ renpy.pause (0.2)

#scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow

#$ renpy.pause (1.5)

#play music "mx/fireplace.ogg" fadein 2.0

show adine normal b with dissolve

Ad "Can I offer you something to drink, maybe?"

c "No, thanks. I'm good."

Ad "How about some TV?"

c "That could be interesting. I haven't watched TV in ages, and I don't have one in the apartment."

Ad think b "You're right. You've got a pretty decent apartment, but they didn't provide a TV. I wonder why."

c "Maybe they wanted to avoid culture shock, or something like that."

Ad "You got a shelf full of books, though. Why would books be fine, but not a TV?"

c "I suppose when they give me books, they know what I'm going to read, but on TV they can't really regulate the content I'm going to see. At least if TV works the same way as ours used to."

Ad normal b "That's true. Maybe they just thought your time would be better spent elsewhere."

c "I guess. If they didn't want me to watch TV, they certainly never told me."

Ad "Actually, there's  a series on right now that could be pretty interesting to you."

c "What is it?"

Ad giggle b "Well, I'm not going to tell you. Do you want me to put it on or not?"

c "Sure, let's do it."

show adine normal b with dissolve

play sound "fx/button_press.ogg"

m "Adine turned on the TV and a brief flicker appeared on the screen before it was filled with the image of a house from the outside."

c "Well, that doesn't look unusual."

Ad think b "Just wait a bit."

m "The camera cut to the inside of the home while the chattering of small talk could be heard." 

m "Then, some figures entered the living room on the screen. They were grotesque, malformed creatures with rather cartoony proportions, covered in odd lumps all over their body. They all shared the same, odd skin tone."

m "It was clear to me that these figures were played by actors in obviously fake, bulky costumes that reminded me of mascots."

c "What are those?"

Ad giggle b "Humans."

c "Humans?"

Ad normal b "That's the name of the series. It's a typical sitcom about a contemporary family as we would expect it, but the twist is that everyone is human."

m "And then I realized why I hadn't been able to identify the creatures on the screen as humans. They were all naked."

m "Since the dragons' concept of clothing was different, they had applied their own principles when creating this series."

m "It was quite bizarre to see a typical family sitcom where all the characters were in obviously fake costumes - and also happened to be naked."

c "Do you like it?"

Ad think b "It's one of my favorites. While it is a sitcom, it manages to address serious and deep issues fairly often, which I don't think would be as effective if we weren't watching them through the lens of this alternate reality."

Ad normal b "This one isn't a bad episode, but it's already nearly over."

c "I guess there's no point in just watching the ending."

Ad "True."

play sound "fx/button_unpress.ogg"

m "By this point, the credits were already rolling, and Adine turned off the TV again."

Ad think b "What do you think?"

c "Let's just say that if a human looking like that suddenly showed up in our world, people would probably run away screaming."

Ad giggle b "They don't look that bad."

c "Sure, it's impressive if we consider what they had to work with, but there's a few things they got wrong."

Ad think b "Like what?"

c "For one, humans mostly wear clothing, and secondly, we don't have tails."

Ad giggle b "Those are just small details. The series is still good, though."

c "Is it popular?"

Ad normal b "For sure. Many people love it."

c "I see. I hope they aren't too scared of me when they see how different I am, though."

Ad giggle b "I didn't run away screaming when I first met you, did I?"

c "True."

label adine4skip:

Ad think b "Now that you're already here, there's something you could help me with."

c "What is it?"

Ad giggle b "Well, it'd be a huge favor to ask, and it's kinda embarrassing..."

c "Just say it. The worst I can do is say no."

Ad think b "How should I say this... It's about my shower."

Ad giggle b "I get pretty dirty from practice sometimes, especially from the bad landings. And recently, the detachable shower head broke." 

Ad "That usually wouldn't be much of a problem, but with this injury I can't quite reach a few places on my own."

Ad disappoint b "It's already not ideal having to manage everything with my wings, but now it's even harder."

c "You want me to scrub your back?"

Ad giggle b "I guess you could put it that way. Told you it was embarrassing."

menu:
    
    "I'll do it.":
        
        c "Don't worry about it. I'm glad to help."

        Ad normal b "Thanks!"

        $ mp.adineromance = True
        $ mp.save()

        jump a4shower


    "I won't do that.":

        c "I'm sorry, but I don't think I'm comfortable with doing that."

        Ad normal b "Yeah, I figured as much. Since you were already here, I thought it was worth a shot. Guess I'll just have to manage on my own. Sorry for asking."

        c "Don't worry about it. It's getting pretty late, anyway, so maybe I should go now."

        Ad think b "Do you still want to watch the fireworks, though?"

        c "Sure, I'll keep you posted."

        Ad normal b "Great. Well, you know where the door is. Be safe!"

        $ persistent.adine4skip = True

        stop music fadeout 1.0
        $ renpy.pause(1.0)

        $ adinestatus = "neutral"

        $ adinescenesfinished = 4

        if chapter4unplayed == False:
            
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars




label a4shower:

Ad giggle b "This way."

hide adine with dissolve

play sound "fx/door/handle.wav"

$ renpy.pause (1.0)

m "I followed her, entering the rather large bathroom."

c "This shower is huge. I wouldn't mind having one of these."

Ad "This isn't just your regular dragon-sized shower. It's made specifically for a flyer like me. We need enough room to stretch our wings."

c "Just think of the possibilities."

m "She took off her goggles and stepped into the roomy walk-in shower. After pressing a button on the wall, water started flowing from the shower head mounted on the wall."

play soundloop "fx/shower.ogg" fadein 1.0

m "She moved around a bit, stretching this and that way in order to cover her whole body in the water. Soon afterwards, she pressed the button on the wall again, and the water flow stopped."

stop soundloop fadeout 2.0

m "She turned to show me her back, wings splayed."

scene black with dissolve

$ renpy.pause (0.5)

show adineshower at Pan ((200, 608), (400,0), 10.0) with dissolveslow

$ renpy.pause (8.5)

#hide adineshower with dissolvemed

#$ renpy.pause (0.5)

#scene adineapt2 at Pan ((128, 300), (128,300), 0.0) with dissolvemed

Ad "The soap and sponge should be right there."

m "I took a sponge that wasn't unlike the ones I knew from back home and added some soap from a rather big bowl." 

m "It seemed to me that each species had their own challenges that needed to be overcome when it came to daily tasks like this one, emphasized by all the different design choices when it came to everyday items. "

Ad "You can start with the wings and work your way down from there."

c "Sure thing."

m "I couldn't help making a joke to ease the tension a bit when I put the sponge on her muzzle."

play sound "fx/rub1.ogg"

c "Hey, it looks like you've got something here. Oh, wait. That's just your stripes."

Ad "Hey, stop that!" with vpunch

c "Sorry, I couldn't resist."

Ad "Good job. Now I've got soap in my nose."

show adineshower at Pan ((400,0), (1080,100), 8.0)

play soundloop "fx/rub2.ogg"

m "I started scrubbing her wings. Now that I could see them up-close and fully extended, I found them to be quite impressive."

$ renpy.pause (1.0)

Ad "..."

$ renpy.pause (1.0)

Ad "You know, I actually tried to do that before."

c "What do you mean?"

Ad "Washing off those stripes."

c "Why?"

$ renpy.pause (1.0)

Ad "..."

$ renpy.pause (1.0)

#show adineshower at Position (xpos = 1080, ypos = 100, xanchor = 1.0, yanchor = 0.0) with ease

show adineshower at Pan ((1080,100), (00,300), 12.0)

Ad "Well, I was just a child back then. You know how kids are. They make fun of everything. Though, I don't know if human children are the same way."

c "They are, trust me."

$ renpy.pause (3.0)

Ad "Don't press too hard there. That's the injured shoulder."

c "I'll be careful."

$ renpy.pause (2.0)

show adineshower at Pan ((00,300), (200,608), 6.0)

m "Eventually, I reached her lower back, and while I was washing a particular spot on her left side, I could see her leg twitching slightly."

c "Are you ticklish there?"

Ad "I guess you noticed."

c "What happens if I do this?"

m "I repeated my ministrations, moving the sponge in circles over that particular spot."

Ad "Hey, stop that!"

stop soundloop fadeout 0.5

play sound "fx/simplecrash.ogg"

$ renpy.pause (0.2)

m "She started squirming, and suddenly, her tail whacked around and hit me in the face, causing me to stumble and fall over backwards." with vpunch

Ad "Are you okay?"

c "I guess I deserved that."

Ad "Well, you tickle the dragon you get the..."

show adineshower at Pan ((200,608), (00,308), 6.0)

c "...tail, apparently."

m "The forked tip of her tail was still hovering inches in front of my face. Its peculiar shape reminded me of something, and I couldn't help but grab it and hold it like a telephone."

c "Hello? Hello?"

Ad "What are you doing?"

c "I think your phone isn't working."

Ad "Stop being silly."

c "Alright, alright. I'm nearly done, anyway."

play soundloop "fx/rub2.ogg"

show adineshower at Pan ((00,308), (00,608), 6.0)

m "I resumed my scrubbing. By now, only her tail was left."

m "Not being entirely sure about my technique, I moved the sponge over the tail's whole length in small circles."

play sound "fx/purr.ogg"

m "When I was nearly done, I noticed a low rumble emanating from her, reminding me of what an oversized cat's purr might sound like."

c "Is that... are you purring?"

show adineshower at Pan ((00, 608), (400,0), 10.0)

stop sound fadeout 0.5

stop soundloop fadeout 1.0

m "Suddenly, her expression changed as she looked over her shoulder."

Ad "Oh, are you done? You should take a step back if you don't want to get hit by the water."

hide adineshower with dissolve

$ renpy.pause (0.5)

scene adineapt2 at Pan ((128, 300), (128,300), 0.0) with dissolvemed

play soundloop "fx/shower.ogg" fadein 1.0
m "After I left the shower again, she pressed a button on the wall, and the water resumed once more. She only stood under it briefly and moved around a bit until the water had completely washed off the suds."

stop soundloop fadeout 2.0
m "When she turned off the water again, I realized that it didn't cling to her much at all. After she shook herself for a bit, she stepped out again, nearly dry."

show adine giggle b with dissolve

Ad "Thanks, I really needed that."

c "You're welcome."

Ad think b "It's probably getting late for you, and I already held you up this long."

c "Don't worry about it."

c "Oh, it's already dark outside."

Ad normal b "I guess that took longer than I thought."

c "I'm not supposed to go outside this late."

Ad think b "You're right. We were advised by the police to stay inside after nightfall because of everything that's going on."

c "For me, this is even more important. We don't know if there's anyone out there who might want to target me."

Ad normal b "I suppose you'll just have to spend the night then."

c "I guess so..."

$ adinestatus = "good"

$ adinescenesfinished = 4

$ persistent.adine4skip = True

stop music fadeout 1.0
$ renpy.pause(1.0)

#$ adinestatus = "normal"

if chapter4unplayed == False:
    
    jump chapter4chars
    
elif chapter3unplayed == False:
    
    jump chapter3chars
    
elif chapter2unplayed == False:
    
    jump chapter2chars
    
else:

    jump chapter1chars


label lorem4:

$ lorem4unplayed = False
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Lorem 4"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Lorem 4"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Lorem 4"
    
else:

    $ save_name = "Chapter 1 - Lorem 4"

scene black with fade
$ renpy.pause (1.0)
scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolvemed

$ renpy.pause (0.3)

play sound "fx/door/doorbell.wav"
$ renpy.pause(3.0)

stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

show lorem normal with dissolve

play music "mx/spring.ogg" fadein 2.0

Lo happy "Hey!"

c "Hey, Lorem."

Lo think "So this is where you live."

c "You already got a glimpse when you delivered Reza's letter, remember?"

Lo shy "Yeah, but back then, I didn't really notice anything. I was nervous."

c "Why were you nervous?"

Lo "Well, there was the fact that I was going to speak to a human. Plus, I didn’t know if you’d actually listen to what I had to say."

Lo "And then I also wondered if I was going to remember everything I wanted to tell you... Or worse, if I’d get thrown out again like when I talked to Reza."

c "You actually talked to Reza?"

Lo think "Well, not really. He just took the letter I had for him and closed the door. But that was before you arrived here."

c "Do you know who sent the letter?"

Lo normal "It came through the portal, so I assume it was from a human."

c "I see."


if persistent.base_taken:
    
    if persistent.orb_taken:
        
        if persistent.endingsseen > 0:

            Lo happy "Oh, that must be the sphere you found."
            
            play sound "fx/spheretake.ogg"

            m "Lorem walked up to the table and picked up the round object I’d found at the park."

            c "Yeah. Maybe you can help me find out if it's actually Ipsum's or not."

            Lo normal "Sure."

            Lo think "Looks like it has no battery, though."

            play sound "fx/sphereslide.ogg"

            m "He turned the sphere a few times, then placed it on the base and plugged it in."
            

            if persistent.ixomenassembled == False:
                
                $ achievement.grant("Sphere Builder")
                
                $ persistent.achievements += 1

                $ persistent.ixomenassembled = True
                                    
                call syscheck from _call_syscheck_29
                                    
                play sound "fx/system.wav"
                                    
                if system == "normal":
                                    
                    s "You have assembled the Ixomen Sphere!"
                                        
                elif system == "advanced":
        
                    s "You have assembled the Ixomen Sphere. Hy-spherical!"
                                        
                else:
                                        
                    s "You have assembled the Ixomen Sphere. Actually, it was Lorem. This should be his achievement."
                                    
                $ renpy.pause (0.3)


            play sound "fx/silence.ogg"

            queue sound "fx/silence.ogg"
            
            queue sound "fx/silence.ogg"
            
            queue sound "fx/silence.ogg"
            
            queue sound "fx/silence.ogg"
            
            queue sound "fx/sphereboot.ogg"

            m "He touched the base in a peculiar way. In response, writing appeared on the sphere’s surface."
            
            show loremsphere at Pan ((0, 326), (200,0), 10.0) with fade
            
            $ renpy.pause (8.5)
            
            hide loremsphere with fade

            Lo happy "Looks like this really is Ipsum's sphere. He'll be relieved to know that it was found."

            c "So, what can we actually do with it now?"

            Lo think "Nothing, really. Unless you know the password, that is."

            c "Well, that's a shame."

            Lo normal "I do happen to know his password, but that's only for emergencies."

            c "No playing around with the sphere, then. Got it."

            $ loremhavesphere = True
        

        else:
            
            pass
    
    else:
        
        pass


else:
    
    pass

Lo think "By the way, did you hear about Ipsum? Apparently, he's become a witness for a murder case."

#insert skippy here

if persistent.lorem4skip == True:

    stop music fadeout 1.0
    
    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_30

    call skiptut from _call_skiptut_5
        
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
            call skipcheck from _call_skipcheck_5

            scene o2 at Pan((0, 250), (0, 250), 0.1)

            show lorem relieved 
            
            with dissolveslow

            play music "mx/spring.ogg" fadein 2.0
            
            jump lorem4skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/spring.ogg" fadein 2.0


if c4witnessavailable == False:

    c "Yeah, I actually took his statement about that not too long ago."
    
else:
    
    c "Oh, I heard about that. Didn't know the witness was Ipsum, though. Small world."

    Lo "How could you know about something like that?"

    c "I've been helping your police for some time now."


Lo shy "Really? Oh, does that mean this has something to do with Reza's disappearance?"

c "There's really no use denying it by this point."

Lo think "How long have you been helping the police, anyway?"

c "Since the day of my arrival, really."

Lo normal "Oh, wow. I guess that explains why you've been so busy."

Lo think "I imagine you can't talk about it, though."

c "I don't really care anymore."

c "Besides, I think it has become common knowledge by this point."

Lo "You're trying to find Reza, right? Wasn't he your friend?"

c "Not sure I'd call him that."

Lo sad "Still, he was supposed to be your partner in this. And now he's just... gone."

c "I'm more worried about what he's doing now."

c "Even if we find him, this may put our diplomatic relationship in peril."

Lo "..."

c "I guess I shouldn't talk about stuff like that."

Lo think "Why not?"

c "It's no use worrying about things that I can't change."

Lo happy "Right. Just focus on the things you can. That's my philosophy."

Lo think "You know, it's a bit of a shame you didn't want to go to the festival."

c "I already had my fair share of adventure the last time we met. Besides, I should probably lay low for now."

Lo normal "You're right. The crowds would probably go crazy if they saw you."

Lo "We could still watch the big fireworks show together, though. We wouldn't even need to go to the festival grounds to do that."

c "Sure, if you like."

Lo "It only takes place at the end of the festival, though."

c "When's that?"

Lo "A few days from now."

c "You've been here a few minutes and already want to schedule our next get-together."

Lo think "Get-together. That's an odd way of phrasing it."

c "Would you prefer if I called it a date?"

Lo shy "I don't know."

Lo happy "It just seems a bit odd to me, considering this all started with me begging you to meet me so I could draw pictures of you."

c "We did that, and then we went treasure hunting, which was your way of saying thanks."

Lo normal "What would you call what we are doing here now, then?"

c "Dinner. I invited you for dinner."

Lo think "I'm not seeing anything to eat here, though."

c "Right. That's because I wasn't sure about what's in the kitchen."

c "I also don't know what you like, so let's just order something."

Lo normal "There are a few places nearby. Do you have anything in mind?"

c "I'm not really in the mood to try something new."

Lo think "Sure. How about pizza?"

c "Sounds good."

Lo happy "Alright, let's just call Pantoli's, then."

c "They already let us down with the treasure hunt. Why do you think this will be different?"

Lo normal "They're the closest, and I haven't ordered from them in ages."

c "Maybe for good reason. If they can't even get the treasure hunt right, I don't want to know what they do to their pizzas."

Lo think "It's just a pizza, [player_name]. How bad could it be?"

c "Alright, if you want to vouch for Pantoli's, go ahead."

if persistent.ixomenassembled == True:

    play sound "fx/spheretake.ogg"

    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/sphereboot.ogg"

    m "Lorem took the sphere from its base and started to manipulate its interface with his fingers."

    c "What are you doing?"

    Lo normal "Looking up the menu."

    c "I thought using Ipsum's sphere was only for emergencies."

    Lo relieved "He went into my room when he was looking for the sphere, and he isn't allowed to do that unless it's an emergency."

    Lo happy "It's the least he can do, considering you found it for him."

    c "Alright."

    Lo think "If you don't want pizza, I can just put it back and we can order something else."

    c "You already touched the sphere. It's too late to put it back now."

    Lo normal "If you say so."
    
else:
    
    c "Actually, I think I've got one of their menus here."

    play sound "fx/paper2.ogg"

    c "Yep, here it is."

Lo think "Let's see, even their smallest pizza is going to be pretty big for me..."

c "We could share one."

Lo normal "Sure. What toppings would you like?"

Lo think "I think I'll go with salad."

menu:
    
    "Seriously? Salad on a pizza?":

        $ renpy.pause (0.5)

        Lo relieved "Don't knock it before you try it."

        c "Next you're going to tell me that you eat pizza with a knife and fork."

        Lo think "Not really."
        
        show lorem normal with dissolve

    "That's a new one. Sounds interesting.":

        $ renpy.pause (0.5)

        Lo normal "Interesting enough to try it?"

        c "I'll look at the other options first."

        #Lo think "Alright."
        
        #show lorem normal with dissolve

    "I'll take that as well.":

        Lo "Are you sure?"

        c "Let me see what else they have."
        
        show lorem normal with dissolve



Lo "Alright. What would you like on your half?"

menu:
    
    "Pepperoni.":

        Lo "Got it."

        show lorem happy with dissolve

    "Grapes.":

        $ renpy.pause (0.5)

        Lo think "Sounds exotic."
        
        show lorem happy with dissolve

    "Salad.":

        $ renpy.pause (0.5)

        Lo happy "Really? Alright."

if persistent.ixomenassembled == True:

    Lo "And it's done. The order has been placed."

    show lorem normal with dissolve

    m "For the next 30 minutes, Lorem showed me many of the other (and less useful) features of the Ixomen Sphere. He made it levitate, showed me a primitive looking website and even used it as a voice modulator."

else:
    
    Lo normal "I'll just place the order, then."
    
    c "Go ahead."
    
    show black with dissolvemed
    
    $ renpy.pause (0.5)
    
    hide black with dissolvemed

    $ renpy.pause (0.5)

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

Lo happy "I'll get it."

hide lorem with dissolve

m "Lorem got up and walked to the door. From my place on the couch, I couldn't see anything, but I heard a bit of talking before he returned to me carrying the square box."

show lorem normal with dissolve

if adinestatus == "none":
    
    Lo "The flyer who just delivered this - I actually know her."

    c "I guess it's not unusual for you to know each other. Your jobs are pretty similar."

    Lo think "I suppose. Some things never change in this town."

elif adinestatus == "neutral":

    label lorem4adinestatusneutral:

    Lo happy "Guess who just delivered us this box of goodness."

    c "I don't know."

    Lo normal "It was Adine. I know her."

    c "I guess it's not unusual for you to know each other. Your jobs are pretty similar."

    Lo think "Yeah, but it seemed like she knows you, too."

    c "I do. What about it?"

    Lo "She asked me what I am doing in your apartment. I thought it was a bit strange."

    c "Maybe she just tried to make some small talk."

    Lo normal "Maybe."
        
    

elif adinestatus == "good":

    jump lorem4adinestatusneutral

else:
    
    Lo think "That was interesting..."

    c "What was?"

    Lo normal "The delivery flyer. I know her."

    c "I guess it's not unusual for you to know each other. Your jobs are pretty similar."

    Lo "Yeah, but it seemed like she knows you, too."

    Lo think "You don't happen to know Adine, do you?"

    c "Actually, I do. What about it?"

    Lo relieved "She had some choice words to say about you. And then she wished me good luck."

    c "Okay. Let's just forget about that."

    Lo normal "Alright."


m "Lorem opened the box and showed me the pizza we had ordered. Memories of days gone by raced through my head."

Lo happy "Alright, let's get this party started." 

c "Don't we need more people for a party?"

Lo normal "With pizza, anything's a party."

c "I feel like I haven't had a pizza like this in ages."

Lo happy "What are you waiting for, then?"

show lorem normal with dissolve

m "I took one of the slices. On its surface, there was an obvious layer of grease that was sure to stain anything it came in contact with."

play sound "fx/pizzabite.ogg"

$ renpy.pause (1.0)

Lo "What do you think?"

c "It's been way too long."

Lo think "Guess you don't mind that we got Pantoli's now, huh?"

show lorem normal with dissolve


play sound "fx/silence.ogg"

queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"

queue sound "fx/pizzabite2.ogg"

m "With these words, he grabbed one of the slices on his half and bit into it."

show lorem relieved with dissolve

m "After chewing a few times, his expression suddenly twisted into a scowl."

c "Is something wrong?"

Lo "Now I remember why I haven't ordered from Pantoli's in a while. Their pizza sucks."

c "It's not that bad."

Lo "Maybe you just haven't had a good pizza to compare it to."

c "Hey, it's still better than nothing."

Lo think "I suppose."

c "By the way, how's your game coming along?"

Lo "..."

Lo relieved "I don't know. I feel like I've hit a wall."

c "Why is that?"

Lo think "Maybe I got in over my head, you know?"

Lo relieved "The more progress I make, the more it becomes apparent that I'll need a lot more help than I thought."

c "So far, you're the only one who's been working on this, right?"

Lo think "Yep, but I'm starting to realize that it won't work out if I continue like this."

c "Why not?"

Lo relieved "It would never be done. Or if it was, it would be very different from what I'd like it to be, so something needs to change."

Lo "I suppose I'm just worried, because once you start involving other people, things get a lot more complicated."

c "How so?"

Lo think "I've always been the odd one out, so I'm not sure how well I could work with a team. You have to find people, work out how to pay them and how to divide the work."

Lo relieved "I guess I'm just starting to realize what kind of investment this would actually be."

c "You sounded a lot more optimistic the last time we talked about this."

Lo "Yeah, it's all fun and games when you're just thinking about ideas that you could turn into a game, but once you actually start working on it, it's a completely different story."

Lo think "At some point, it just becomes another job."

c "Isn't that what you expected?"

Lo relieved "Of course it is. I knew it would be a lot of work, but I guess I'm just not sure if it's all worth it."

c "That depends on why you're making it in the first place. Last time you said that you had nothing to lose either way."

Lo think "Well, maybe I was wrong about that. I do have something to lose."

c "What's that?"

Lo sad "Myself."

Lo relieved "I'm not sure if I'm ready to do what is necessary to finish what I started."

c "If you think about it, what's the worst that could happen?"

Lo "Investing a lot of time and money, only to end up with nothing in the end."

Lo "I could end up disappointing those who play the game, those who collaborated with me, and lastly, myself."

c "That's what you're worried about?"

Lo think "That's what being a creator is like. If you put tons of work and effort into something, you want  people to like it, right? If that's not what's going to happen, why do it in the first place?"

c "But you're not doing this for other people, are you? It's your game and your idea, after all."

Lo "Right, but..."

c "You're not trying to cater to someone else, so what other people think is not important."

c "Besides, what they think is outside of your control, anyway."

c "Just look at what happened with Pantoli's."

c "Why do you think their pizza sucks?"

Lo relieved "They probably cut a lot of corners during production and with the ingredients. They value quantity over quality and are only trying to get as many pizzas out as possible to satisfy demand."

Lo "They are cheap and the pizza tastes like it."

c "Okay, but they are still in business, so this must be working out for them somehow. Even if you don't like it, they are offering something other people clearly want."

c "They probably don't give a damn about whether or not you like their pizza."

Lo "I'm sure they don't."

c "They just give people what they want, and that's why they stay in business."

Lo "Are you saying that I won’t be successful if I don’t cater to others?"

c "No, I'm saying that unless being successful is the goal, you don't need to cater to anyone else."

c "Because if you did, you would end up like Pantoli's and you really would lose yourself."

Lo think "I guess you have a point."

c "So what if other people like their greasy pizzas? That's not what you want to do."

Lo relieved "Certainly not."

c "You said yourself that your philosophy is to focus on the things you can change, so what are your options here?"

c "A wise person once said: Do or do not. There is no try."

Lo think "Not doing this has never been an option for me."

c "Then you make the most of it and nothing else matters."

Lo normal "I think you're right. I should just focus on getting things done as best I can."

c "Who knows, maybe you're wrong about Pantoli's. Maybe they're actually a big family restaurant with a rich tradition and history, and that's why people like them." 

Lo relieved "No, I think it's just because they have cheap pizzas."

Lo sad "..."

Lo "Anyway, there's a good reason for my anxiety."

Lo think "I usually keep to myself and that's always how I've worked best."

Lo "If there's one thing that life has taught me, it's that people fear what they don't know."

Lo "I guess that's an odd thing to say when humans are worshipped by many. Most of them don't actually know any humans. Not like I know you."

Lo "Maybe I should rephrase that. People are afraid of what they don't understand."

Lo sad "I was bullied a lot when I was a kid."

Lo "You know, it can be pretty tough when you're growing up and all the other kids are always bigger than you are."

Lo think "Luckily, that was never a big problem for me. Even in kindergarten, we get told not to make fun of our differences because of how different our species are."

Lo sad "It's just odd that for a society that celebrates our differences, there are still things that are too different even for them."

Lo relieved "When I grew up and went to college, I thought that people would know better than to continue doing those horrible things, but I was ultimately proven wrong."

Lo sad "Their bodies may have been those of adults, but their hearts had stayed in the same place they were a decade before."

Lo "Working on my own has helped, but that is treating the symptom, not the cause of the problem."

Lo "I can't always just run away, and I'll have to step into the limelight and brave the storm again if I want to finish this game."

Lo relieved "There's something about me that you don't know."

Lo "In a way, I owe it to you to tell you, because you're going to find out sooner or later anyway - and when it happens, it should be on my terms rather than someone else's."

label lorem4skip:

c "What is it?"

Lo sad "..."

Lo "I'm a hermaphrodite."

Lo "I was born with both sets of sex organs - and before you ask, that is not something that is at all common in any of our dragon species."

Lo "In the eyes of some, that makes me a freak of nature. Something that needs fixing, or shouldn't exist in the first place."

menu:

    "I don't mind.":
        
        $ persistent.lorem4skip = True
        
        $ renpy.pause (0.5)

        Lo think "You don't?"

        c "Sure, some people may think that it's odd, but I don't really care."

        c "It's just another part of who you are."

        Lo normal "Thank you."

        Lo relieved "That's such a big relief."

        Lo sad "You know, it's not always the bullies who go after me once they know."

        Lo "Too often, it's also been people who I thought were my friends."

        Lo relieved "So, whenever I meet another person, I have to prepare myself for this conversation - not knowing whether they will suddenly turn against me when they find out."

        Lo "And the reactions can be very different."

        Lo sad "Some get angry or make fun of me. Others feel betrayed and don't want to have anything to do with me anymore."

        Lo relieved "By now, I think I've seen it all."

        Lo "I'm so glad that you're not like them, but it's always a gamble."

        Lo "Maybe the next person I tell is going to become violent."

        Lo sad "How can I put myself out there when this could happen wherever I go, you know what I mean?"

        Lo "What will people do when they find out about me and my game? I just don't know."

        Lo "That's what I'm worried about."

        Lo relieved "I only wish there was a place where I could be safe from all of that. Where it just wouldn't matter that this is who I am."

        Lo sad "..."

        Lo "If someone like you - someone with a place of authority - said something, maybe that could change things."

        Lo "I know you can't interfere with our politics, though. You're an ambassador."

        Lo "Doesn't mean I don't have hope that something like that will happen one day."

        $ lorem4pick = "idontmind"



    "I'm not sure what to say.":

        $ persistent.lorem4skip = True
        
        $ renpy.pause (0.5)

        Lo relieved "That already tells me all I need to know."

        Lo "You'd think it's only bullies who go after me once they find out about this, but too often, it's also been people who I thought were my friends."

        Lo "So, whenever I meet someone, I have to prepare myself for this conversation, not knowing whether they will suddenly turn against me when they find out."

        Lo "And the reactions can be so different."

        Lo sad "Some get angry or make fun of me. Others feel betrayed and don't want to have anything to do with me anymore."

        Lo relieved "By now, I think I've seen it all."

        Lo "Maybe the next person I tell is going to become violent."

        Lo sad "I'm glad that you're not one of those, but it's always a gamble."

        Lo "How can I put myself out there when this could happen wherever I go, you know what I mean?"

        Lo "What will people do when they find out about my game? I just don't know."

        Lo "That's what I'm worried about."

        Lo relieved "I only wish there was a place where I could be safe from all of that. Where it just wouldn't matter that this is who I am."

        Lo sad "..."

        Lo relieved "If someone like you - someone with a place of authority - said something, maybe that could change things."

        Lo "I know you can't interfere with our politics, though. You're an ambassador."

        Lo "Doesn't mean I don't have hope that something like that will happen one day."

        Lo sad "I'm sorry, [player_name]."

        Lo "I should go now. I said my piece and I'm sure it's a lot to take in."

        Lo relieved "You can give me a call in a few days when you've had the time to mull it over or want to talk."

        Lo sad "I understand if you won't."
        
        $ lorem4pick = "whattosay"
        
        $ loremstatus = "neutral"
        
        $ loremscenesfinished = 4
        
        $ renpy.pause (0.3)

        hide lorem with dissolve

        stop music fadeout 2.0
        
        play sound "fx/door/doorclose3.wav"

        $ renpy.pause (2.0)

        if chapter4unplayed == False:
                                
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars


    "Get out.":

        $ lorem4pick = "getout"

        Lo "..."

        Lo relieved "So that's what it's going to be, huh?"

        Lo "Don't worry, I understand. It's far from the first time this has happened."

        Lo "I'll go, but let me just say this."

        Lo "I don't blame you. After all, I have no idea what they think about people like me in your world."

        Lo sad "I don't have a right to judge."

        Lo "But that doesn't mean I don't lament the many opportunities that were lost because of this. I hate it."

        Lo relieved "If I hadn't said anything, maybe we could have met a few more times – maybe everything would have been fine."

        Lo sad "But that wouldn't feel right to me."

        Lo relieved "And again, I just have to wonder if those other times didn't mean anything to you."

        Lo sad "Did they?"

        c "..."

        Lo "Maybe it was wrong of me to ever think that I could be your friend."

        Lo "I mean, you did your part. You came to my apartment and let me draw pictures of you."

        Lo "You told me I shouldn't worry about what's going to happen - and after that, I wasn't worried anymore."

        Lo "And what did I do? Nothing."

        Lo "I did nothing."
        
        $ loremstatus = "bad"
        
        $ loremscenesfinished = 4

        $ renpy.pause (0.3)

        hide lorem with dissolve

        stop music fadeout 2.0
        
        play sound "fx/door/doorclose3.wav"

        $ renpy.pause (2.0)

        if chapter4unplayed == False:
                                
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars



Lo relieved "I should probably go now. It's getting late."

Lo normal "You've made me feel a lot better, though."

Lo "You told me not to worry about the future, and maybe you're right."

Lo "Sure, there is still a lot of work ahead, but maybe it's not as hopeless as I thought."

c "It never is."

Lo "Hey, do you still want to see the fireworks show together?"

c "Sure."

Lo "Alright, just give me a call in a few days so we can discuss the details."

c "I'll do that."

Lo "Alright, I'll see you then."

c "See ya."

$ loremstatus = "good"

$ loremscenesfinished = 4

$ renpy.pause (0.3)

hide lorem with dissolve

stop music fadeout 2.0

play sound "fx/door/doorclose3.wav"

$ renpy.pause (2.0)

if chapter4unplayed == False:
                        
    jump chapter4chars
    
elif chapter3unplayed == False:
    
    jump chapter3chars
    
elif chapter2unplayed == False:
    
    jump chapter2chars
    
else:

    jump chapter1chars







$ renpy.pause (0.5)
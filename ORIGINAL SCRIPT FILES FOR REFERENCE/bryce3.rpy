label bryce3:

$ bryce3unplayed = False
$ bryce3mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Bryce 3"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Bryce 3"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Bryce 3"
    
else:

    $ save_name = "Chapter 1 - Bryce 3"

scene black with fade
$ renpy.pause (1.0)
scene beachx at Pan ((0, 0), (300, 0), 5.0) with dissolveslow

$ renpy.pause (3.3)

play music "mx/hydrangea.ogg" fadein 2.0

show bryce smirk with dissolve

Br "There you are, [player_name]."

#insert skip here

if persistent.bryce3skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_102

    call skiptut from _call_skiptut_26
        
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
            call skipcheck from _call_skipcheck_26
            
            scene padx at Pan ((0, 240), (0,360), 3.0) with dissolveslow

            $ renpy.pause (1.3)

            show bryce brow with dissolve    
            
            play music "mx/hydrangea.ogg" fadein 2.0

            $ bryce3do = persistent.bryce3do
            
            jump bryce3skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/hydrangea.ogg" fadein 2.0


Br laugh "Seems like you're the last one."

c "I thought I was on time."

Br normal "Oh, you are. It's just that everyone always gets so excited about this that they come a little earlier."

c "I thought it was strange how late you're holding this little get-together anyway."

Br smirk "It's simple, really. Now we get this beach all to ourselves."

Br brow "Before you go and meet the others, I should probably warn you."

c "What is it?"

Br stern "There is someone here that you may not approve of."

c "And who would that be?"

Br "Maverick."

c "...Why is he here?"

Br "All things considered, I think it's better for him to be here where I can watch him than if he was out there doing who knows what. You know what I mean?" 

Br brow "Besides, if I invited you and not him, I'm not sure how he would've reacted. He's always come to my BBQs before. Plus, maybe if I talk to him, I can find out what he's up to."

c "Does he know that I'm here?"

Br "Yes, and he assured me that he will keep the peace. Can you do the same?"

menu:
    
    "Sure.":
        
        $ renpy.pause (0.5)

        Br normal "Thanks, I appreciate it."

        Br brow "Let's just hope there won't be any incidents."

        $ bryce3mood += 1
        
        show bryce normal with dissolve
        
        
    "I'll try.":
        
        $ renpy.pause (0.5)
        
        Br stern "Please."

        c "Hey, I won't make promises I can't keep."

        Br brow "Well, let's just hope there won't be any incidents."
        
        show bryce normal with dissolve
        
    "Heck, no. I'm outta here.":

        #$ renpy.pause (0.5)
        
        Br "Really? Well, if that's your decision, then so be it."

        c "Whatever, man."

        hide bryce with dissolve
    
        stop music fadeout 2.0
        
        $ renpy.pause (0.5)
        
        $ brycestatus = "bad"

        $ brycescenesfinished = 3
        
        if chapter4unplayed == False:
                        
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars

        
Br "Alright, let's go and meet the others."

m "As we walked a few paces, I saw some familiar faces."

Br brow "Usually there'd be more people here, but with everything else that's going on, some of the others at the department couldn't get any time off."

Br laugh "Hey, everyone! Guess who's finally here."

show bryce normal with dissolve

show bryce at right with ease

show zhong normal flip at left with easeinleft
        
Br "You may remember Zhong, the waiter at that bar."

$ persistent.zhongname = True

Zh "Hello, [player_name]."

c "Hey."

hide zhong with easeoutleft

show sebastian smile flip at left with easeinleft
        
menu:
    
    "Is that you, Sebastian?": #if not played sebastian scene
    
        $ renpy.pause (0.5)
        
        Sb disapproval flip "What are you talking about?"

        c "Sorry, I didn't recognize you without your little cap on."

        Br laugh "That's a good one."

        Sb "Oh, you're already bringing out the jokes."
        
        show sebastian smile flip
        show bryce normal
        with dissolve

        Sb "Let's see how long you're going to last in this company."
                
        $ bryce3mood += 1
        
    "Hey, Sebastian.":
        
        Sb "Hey, [player_name]."
        
hide sebastian with easeoutleft

show maverick normal flip at Position(xpos = 0.1) with easeinleft

Mv "..."

Mv "Hey, [player_name]."


menu:
    
    "Did Bryce tell you to be nice to me?":
        
        Mv "Yes, he did."

        Mv "But you know what? This evening won't be very enjoyable if you decide to have an attitude."

        Mv "Because I can have an attitude too, and I doubt you want to see that."

        hide maverick with easeoutleft
        
        Br brow "That wasn't a good start, [player_name]."

        c "Sorry, I couldn't resist."

        Br "He was able to. Why couldn't you? Maybe I wasn't clear enough earlier. If you provoke him, I might not actually be able to protect you. Just putting that out there."

        $ bryce3mood -= 1
    
    "Hey, Maverick.":
        
        Mv "..."
        
        hide maverick with easeoutleft
        
        
Br "Alright, let's get this BBQ started."

show bryce at Position(xpos = 1.175) with ease

show sebastian smile flip at left with easeinleft

show maverick normal behind bryce at Position(xpos=0.825) with easeinright

show zhong normal flip at Position(xpos = 0.05) with easeinleft

c "I don't see a grill or anything here. And where's the firewood?"

Br "You see that pile of stones over there? That's our grill."

Br laugh "And firewood... Well, we don't need that."

c "I see."

Br smirk "So, who shall light the fire?"

Sb disapproval flip "I could make my own this time."

Zh "Very subtle, Sebastian."

Br laugh "No need to be subtle about it. Zhong, your fire stunk up the whole area last year, and it made everything taste weird."

show bryce normal with dissolve

Mv "I didn't notice a difference."

Sb smile flip "Yeah, because everything tastes the same to you, Maverick."

Zh "I told you, I had the flu."

Br laugh "I'm pretty sure you gave us more than just your fire. I think we got some of your spit in there, too."

show bryce normal with dissolve

Zh "Yes, because of the flu. Everything was congested, so it was hard to get anything out at all."

Sb "You're not making this any better."

Br smirk "Excuses, excuses."

Zh "I'm just telling you how it is. Besides, it wasn't even my idea to light the fire. You were all like: \"Oh, Zhong never lit the fire. He should do it.\" Don't blame me for getting what you wanted."

Br laugh "Yeah, and we learned our lesson."

show bryce normal with dissolve

Sb "Zhong, not even once."

Zh "You wouldn't be complaining so much about it if it wasn't for the flu I had. Maybe I should light it again this time to prove you wrong."

Br laugh "No, thanks. Last year was bad enough."

Mv "Why don't you do it, Bryce?"

Br normal "I'm not sure if I'm feeling up for the task."

Sb "Why doesn't [player_name] do it?"

Mv "I like that idea."

Zh smile flip "Yes, let [player_name] do it."

Br "It seems we have a unanimous decision here."

Br "Go ahead, [player_name]. Show us what you got."

m "Suddenly, they all looked at me, clearly expecting me to light the fire for them."

menu:
    
    "I don't want to disappoint you, but...":
        
        pass

    "I don't suppose you have any matches?":
        
        pass

    "Is this a joke?":
        
        pass
        

Zh "..."

Br "..."

Sb "..."

Mv "..."

m "They were all still watching me, not moving or batting an eye, when suddenly, laughter erupted."

Br laugh "Hahahaha!"

Sb "Haha."

Zh "Heh."

Mv "..."

c "Okay, guys. I get it. The joke's on me."

Br "Should've seen your face."

show bryce normal with dissolve

Sb "Yeah, it was great."

Zh "Don't pay any heed to them. They're always like this."

c "Yeah, I noticed."

Sb "Seriously though, who should light the fire?"

Br normal "You really wanna do it. Don't you, Seb?"

Sb disapproval flip "Is it that obvious?"

Br smirk "Just go ahead, then. We already agreed Zhong is not doing it."

Zh normal flip "Hey, I told you I could prove you wrong this time."

Br laugh "Yeah, let's not ruin our BBQ two years in a row..."

Zh "Maybe next year, then."

Br normal "I don't feel up for it this year, and with Maverick's aim, he probably shouldn't either. I'd rather not risk anything."

Mv "I could hit you anytime."

Br laugh "Sure, but we just want to have a BBQ, not set the whole beach on fire."

Sb smile flip "Hehe."

Br normal "Besides, Sebastian's fire always makes the food so crisp and smoky. I like that."

Br "Any objections?"

Zh "Nope."

Mv "Me neither."

Br smirk "Master of Ceremony, would you light the fire, please?"

Sb "It's not an easy job, but someone's gotta do it."

hide sebastian with easeoutleft

m "Sebastian went up to the small bed of stones they had prepared. Since his back was turned towards me, I couldn't exactly see what he did, but a few seconds later, a fire started burning among the stones."

play sound "fx/firex2.ogg"

Br normal "There we go. Well done, Sebastian."

show sebastian smile flip at left behind zhong with easeinleft

Sb "My pleasure."

Br smirk "Alright, everyone. Pick your poison."


hide zhong with easeoutleft
hide maverick with easeoutright
hide sebastian with easeoutleft

show bryce at center with ease

Br normal "Just to get you up to speed, [player_name] - we've got pretty much everything here you could ask for."

Br "Of course we have all varieties of meat, but we also have some vegetables and cheese, if you're into that sort of thing." 

Br "We even got some of the algae stuff we usually bring for Naomi – one of the girls at the department - but she couldn't come tonight."

Br "Just help yourself, and throw it on the fire."

Br "Sebastian always gets some veggies with his meat, whereas Zhong goes totally crazy over the cheese stuff."

Br brow "Now that I think about it, maybe it was just that damn cheese that made everything so bad last time."

Zh "Oh, shut up. Or else I'll force feed you some of it."

Br laugh "No, thanks. Keep your cheese to yourself, please."

Br normal "Where was I? Oh, right. I go for the meat, personally. As I said, the algae is normally for Naomi. She really likes the stuff, but she's one of the water kinds, so that's not a surprise."

Br "I tried it myself once. Not really my kind of thing, but feel free to take some if you want to."

Br laugh "And then, there's Maverick. He just eats whatever he can get into his muzzle."

show bryce at right with ease
show zhong normal flip at left with easeinleft

Zh "A few years ago, a sandstone managed to hide between some slabs of meat he got. He didn't even notice and just kept on munching."

Mv "Yeah, but that was with Bryce's cooking, so I couldn't tell the difference."

Sb "Tee-hee."

Br "Why, you."

show bryce normal with dissolve

show bryce at Position(xpos = 1.175) with ease

show zhong normal flip at Position(xanchor = 0.5, xpos = 0.05) with ease

show maverick normal behind bryce at Position(xpos=0.825) with easeinright

show sebastian smile flip behind zhong at left with easeinleft


m "After all of us had made our selection and put it on the fire, we sat down in a circle around it. Of course, Bryce made sure that Maverick and I were not sitting next to each other."

Sb "So Bryce, how's that stint with Emera going for you?" 

Br brow "It's weird. I'm not even really doing anything. I just have to follow her around and stand guard in her office. But what's worse, I think I found out why she wanted me to do the whole thing in the first place."

Zh "Oh, do enlighten us."

Br laugh "It's kinda embarrassing, to be honest."

Sb "Now you definitely have to say it."

Br smirk "Alright, alright. The real reason why she wants me to be around her so much is that she totally has the hots for me."

Sb disapproval flip "Oh, come on."

Zh "Seriously?"

Mv "You wish."

Br laugh "You all know what she's like in public, right? But as soon as it's only us two in the room, she's like a totally different person. It's unreal."

show bryce normal with dissolve

Sb "I mean, I believe that she's different in private, but still..."

Zh "Of course, Bryce. When you make up a story, just going out with a high-ranking politician isn't enough. Obviously, she also can't resist your manly allure."

Br laugh "But it's true. I'm not even interested in her. For one, she isn't really my type, and regardless if it's her public or private persona, her personality really sucks."

Sb smile flip "What was that about sucking?"

Br "Oh, shut up. If no one wants to believe me, I'll just stop before I get to the really bad stuff."

show bryce normal with dissolve

c "I can actually confirm that she does act like a totally different person when she doesn't think she's being watched by the general public."

Sb disapproval flip "Hmm, interesting."

Mv "..."

Sb smile flip "Okay, Bryce. Why don't you tell us more? What exactly does she like about you?"

Br laugh "What's {i}not{/i} to like about me?"

Zh "We get it, Bryce. Let's just change the subject."

Br "It's true! I swear!"

Sb "Then give us some details. What's she like in private?"

Br normal "It all started innocently enough, but as I told you, when we were alone she started to get kinda weird after a while."

Br laugh "She wasn't even remotely subtle about it, either. Once, even the words \"cavity search\" came up. From her, mind you, not me." 

Sb "Oh, come on."

Zh "I can't even listen to this anymore."

Br "And then later, she was suddenly like: \"Oh, my back is so stiff! Would you mind giving me a massage? You look like you have the proper strength to give me a good one.\" It's like she's not even trying to hide it."

#br laugh

if emeraunplayed == False:
    
    menu:
        
        "Tell them about your experience with Emera.":
            
            c "She actually did the same thing with me."
            
            Sb disapproval flip "Really?"
            
            Zh "This is getting worse by the minute."
            
            Br brow "Whaat?"
            
            c "I visited her the other day and at some point, she did ask me to give her a massage as well."
            
            Sb smile flip "Does that mean she has the hots for [player_name] too?"
            
            Br "Maybe she does."
            
            Sb "Maybe she does it with everyone she meets."
            
            Zh "I rather doubt that."
            
            Br laugh "Don't tell me she asked you about having children as well."
            
            c "I can honestly say she did not ask me about having children."
            
            Zh "She did what now?"
            
        "Stay silent":
            
            jump bryce3pass
    
    
else:

    label bryce3pass:

        Sb "Did you give it to her?"

        Br "Of course not! I told her I'm no good with massages. That's the truth."

        show bryce normal with dissolve

        Sb "Who would have thought."

        Zh "Do you really believe him, Seb?"

        Sb "I'm not judging, just listening."

        Zh "Emera wanting you to give her a massage hardly constitutes her \"having the hots\" for you, though."

        Br laugh "I'm not even done yet." 

        Zh "Well, I'm done with this."

Br "Earlier today, she told me how nice it would be for a child to grow up with two leaders for parents."

Sb "Actually, I don't think even Bryce could've come up with that one on his own."

Zh "I'm not buying it."

Br "Hey, at least you believe me. Right, [player_name]?"

menu:
    
    "I do.":
        
        c "I do. I can totally picture Emera acting like that."

        Br "See, I told you. If [player_name] believes it, it must be true."

        Mv "Can't argue with that logic."

        $ bryce3mood += 1

    "Sorry, I don't.":
         
        Br "Oh, come on."

        $ bryce3mood -= 1
        
        
    "Sorry, I'm not taking sides on this one.":
        
        Br "Oh well."
        
        
Zh "Maybe it's just the alcohol talking."

Br brow "I didn't even have anything yet."

Sb "Sure, but with as much as you drink, your blood is like, at least 10%% beer by now. I bet you can't even get completely sober any more."
        
Br "Anyway, what do you think I should do about her?"

Zh "Nothing, because you made up the whole thing in the first place."

Br laugh "If I don't do anything, I'll probably end up having to marry her or something."

Zh "And at that point, your story would actually be credible."

Sb "Why don't you just tell her to stop?"

Br brow "It's not that easy, considering our positions. Even though I'm the chief, there's nothing I can do to prevent her from pulling me off the case and making me into her personal body guard."

Br "If I tell her off too strongly, she could totally make my professional life a nightmare."

c "And she totally would."

Sb "I see, so this is a situation that requires careful deliberation and subletly. Not exactly your strong suits, Bryce."

Br laugh "That's why I'm asking you lot. Not that you're much better, though."

Mv "Maybe you should play along for a while just to see what happens. And then, once the time is right, you strike."
        
Zh "And \"strike\" refers to what, exactly?"

Br "I'm not going to indulge her in any way, shape or form."

Br brow "Ugh, this is the kind of situation that's going to cause a huge uproar if I include it in my memoir."

Sb disapproval flip "Who's going to read your memoir, anyway?"

Br laugh "Well, I know at least one person."

Br brow "[player_name], what do you think I should do?"
        
menu:
    
    "Play along and see what happens.":
        
        Br "Seriously, you think I should string her along?"

        c "Well, you said she could make your professional life a nightmare, but if you play along a little, maybe the opposite is true as well."

        Br laugh "Not a bad idea, now that I think about it."

        $ mp.bryce3do = "string"
        $ mp.save()
        
        $ bryce3do = "string"
        $ persistent.bryce3do = "string"
        
        
    "Tell her how you really feel.":
        
        Br "Are you sure?"

        c "Well, if you string her along that would be pretty dishonest. And she might be even more angry when she finds out the truth than if you had just told her up front."

        Br laugh "Good point."
        
        $ bryce3do = "truth"
        $ persistent.bryce3do = "truth"

        $ mp.bryce3do = "truth"
        $ mp.save()
        
        
    "Go on a date with her.":
        
        Br "Really? Why would I do that?"

        c "Well, what's the worst that could happen? Maybe she won't be as bad as you think."

        Br laugh "I kinda doubt that, but you never know."
        
        $ bryce3do = "date"
        $ persistent.bryce3do = "date"

        $ mp.bryce3do = "date"
        $ mp.save()
        
        
show bryce normal with dissolve

c "That kinda makes me curious, though. How does dating work in this world, considering there are so many sentient species around here? Is dating between different species encouraged? Maybe that's why Emera is so interested. Is there ever any crossbreeding?"
        
Zh "I'm sure these questions will go over well in this group."

Sb smile flip "Crossbreeding, that's funny."

Br "Well, there isn't any crossbreeding. It doesn't work like that."        
        
Br laugh "Besides, I thought you were into biology, so shouldn't you already know where hatchlings come from?"

show bryce normal with dissolve

c "You are a completely different life-form from what I've seen before, so I didn't want to make any assumptions."

Zh "There are many interspecies couples, though."

c "And what happens if those couples want to have a child?"

Zh "There are plenty of options, though usually it's either adoption, or a child where only one of the parents is biologically related."

Br laugh "Emera totally wants my children, though."

c "Don't you want to be a father?"

Br "Heck, no! I'm not ready for that. I wouldn't even know what to do with a hatchling. I'd prolly end up breaking its neck by accident or something like that."

show bryce normal with dissolve

Sb "What about you, [player_name]?"

c "What about me?"

Sb "Are you \"having the hots for someone\" here, as Bryce would put it?"

c "To be honest, I have no idea how that kind of relationship would be viewed where I come from. Since we only have one sentient species, I'm not sure what sort of social norms we'd develop if that changed."

Zh "Technically speaking, you dating one of us is no different than Emera dating Sebastian, for example."

Sb "Hey, I'm not getting between the beautiful thing Emera and Bryce have going on."

Br "If you ask me, you can do whatever you like as long as you're here. Knock yourself out."

if remy3unplayed == False:
    
    Sb "Well, I've seen [player_name] hang out with that librarian a few times."

    Br brow "Who? The klutzy one?"

    Sb "Yeah."

    Zh "Come on, Bryce. Don't be like that."

    Br flirty "Oh, I didn't know he was your type."

    menu:
        
        "He's just a friend.":
            
            Sb "I'm sure he is."

            Br laugh "So [player_name] found a friend. That's cool, too."


        "That's none of your business.":
            
            $ renpy.pause (0.5)
            
            Br laugh "Oh, I know what that means."

            Zh "Maybe it doesn't mean anything."
        
        
        "Okay, I like him. Sue me.":

            $ renpy.pause (0.5)
            
            Br laugh "Just don't let him carry your wedding ring, or it'll end up in the gutter."

            c "Hey, don't talk about him like that."

            Br brow "Okay, okay. Sorry for making a joke."
            

        "Don't get too worked up. It's not a thing anymore.":
            
            c "Don't get too worked up. It's not a thing anymore. Actually, I'm not sure if it ever was."

            Br stern "Aww, that's a shame."

            c "No biggie."
            
            
elif adine3unplayed == False:

    Sb "Well, I've seen [player_name] hang out with a certain yellow flyer a few times."

    Br "I only know of one yellow flyer around here, and she usually delivers my pizzas."

    Sb "That's the one."

    Br flirty "I guess that means you're into girls, then."

    menu:
        
        "She's just a friend.":
            
            $ renpy.pause (0.5)
            
            Br laugh "I wouldn't mind being more than a friend with her."

            c "Hey."

            Zh "She already brings you pizzas. Isn't that enough?"

            Sb "Besides, I'm not sure if that would end well. You're a colossus compared to her."
            
        
        "That's none of your business.":

            $ renpy.pause (0.5)
            
            Br laugh "Oh, I know what that means."

            Zh "Maybe it doesn't mean anything."
            
            
        "You got me there. I like her.":
            
            Sb "Not bad, [player_name]."

            Zh "The more important question is: Does she like you back?"

            c "I think so."

            Br laugh "Guess you're making the most of your time here, huh?"
            
            
        "Don't get too worked up. It's not a thing anymore.":
            
            c "Don't get too worked up. It's not a thing anymore. Actually, I'm not sure if it ever was."

            Br stern "Aww, that's a shame."

            c "No biggie."


elif anna3unplayed == False:
    
    Sb "Well, I've noticed that [player_name] has been making a lot of visits to the production facility."
    
    Zh "That could be for a number of reasons."

    Br "Yeah, I bet [player_name] is meeting someone there. The only question is who."

    c "I made a bet with Anna, that's all."
    
    Zh "She's famous. Did you know that?"

    Br "You're playing with fire there, [player_name]."
    
    menu:
        
        "It's nothing serious.":
            
            $ renpy.pause (0.5)
            
            Br brow "Even then, you should be careful around her. She's feisty, that's for sure."
            
        "I only made a bet with her. There's nothing to worry about.":
            
            Zh "A bet?"

            Br "Actually, it sounds like you've got everything to worry about."
            
        "That's none of your business.":
            
            Sb "Oh, I know what that means."

            Zh "Maybe it doesn't mean anything."

            Br brow "Just be careful, [player_name]."
            
        "I probably won't see her again anyway.":
            
            Sb "That might be for the better."

            Br "Let's hope [player_name] doesn't have any lasting damage from the experience."
    
    

elif lorem3unplayed == False:
    
    Sb "Well, [player_name] has hung out with Lorem a few times now."

    Zh "Who's that?"

    Sb "You don't know? Lorem is the -{w=1.0}{nw}"

    Br stern "There's no need to bring that up right now."

    Sb disapproval flip "If you say so."
    
    show sebastian normal flip with dissolve

else:
    
    Sb "Actually, [player_name] has been hanging out with you a lot, Bryce."

    Br brow "..."

    Zh "Awkward."

    Br laugh "So what, [player_name] is a cool person in my book. Or do any of you disagree?"

    Sb "Not me."

    Mv "No comment."


Br normal "By the way, I think the food should be ready now."

Sb "Good catch."

hide maverick with easeoutright
hide zhong with easeoutleft
hide bryce with easeoutright
hide sebastian with easeoutleft

m "Slowly, everyone shuffled towards the fire, which by now had become nothing more than an eerily glowing pile that illuminated the area. One by one, everyone took their hot food from the stone bed and placed it onto the provided paper plates and bowls."

m "When it was my turn, I hesitated, since I could still feel the heat radiating from the stones."

show bryce brow with dissolve

Br "Something the matter?"

c "I think this might be too hot for me to handle."

Br laugh "Right, no scales. Let me get that for you."

Br normal "There you go."

c "Thanks."

show bryce at Position(xanchor = 1.0, xpos = 1.175) with ease

show sebastian normal flip at left with easeinleft

show maverick normal behind bryce at Position(xpos=0.825) with easeinright

show zhong normal flip at Position(xpos = 0.05) with easeinleft

m "We resumed our positions in a circle around the glowing stones, and I waited for my meal to cool down while the others started eating."

Br smirk "Yep, crisp and smoky. Good job, Sebastian."

Sb smile flip "Don't mention it."

Zh "Really, it's good."

Br laugh "I'm still not sure how you can eat that cheese stuff, Zhong."

Zh "Are you going to make fun of my food choices again?"

Sb "To be fair, we make fun of everyone and everything here."

Mv "I don't mind the cheese."

Br "You wouldn't mind eating the whole bed of stones and everything on it as well."

Mv "At least I try something different every once in a while."

Br "I do, too. I think there are at least five different kinds of meat this time around."

Mv "Case in point."

show bryce normal with dissolve

m "The food remaining on the stones slowly disappeared as everyone got their additional helpings. Soon, even the last piece was gone and silence started to set in as the banter slowly died down."

Zh "I think it's time for me to leave."

Br brow "What? Already?"

Zh "Hey, the babysitter can only stay so long."

Br "Oh well."

Sb disapproval flip "Yeah, I should also be heading off. You know I'm starting early tomorrow."

Br laugh "Well, guess we all got what we came here for. What about you, Maverick?"

Mv "Looks like this party is over, anyway."

Br smirk "Don't y'all get lost in the dark, then."

show bryce normal with dissolve

Zh "Of course."

hide zhong with dissolve

Sb "And until next year."

hide sebastian with dissolve

Mv "Thanks for inviting me, Bryce."

hide maverick with dissolve

$ renpy.pause (0.3)

show bryce at center with ease

c "I suppose I should be heading off as well."

Br brow "Oh no you don't."

c "What are you talking about?"

Br "Well, they all live in the vicinity, but your apartment is on the other side of town. I'm not letting you go home alone at this hour. Reza has always operated during the night, and he may just be waiting for an opportunity like this."

c "What do you want me to do, then?"

Br laugh "You can sleep over at my place."

c "If you insist."

Br brow "Damn, now everyone left without cleaning up. At least you're still here to help me."

#show bryce normal with dissolve

c "Of course."

hide bryce with dissolve

m "We started to clean up together, but with the amount of trash left by five people, it was clear it would take a while."

show bryce brow with dissolve

Br "Hey, do you want to know where I got these scars? I bet you're curious."

menu:
    
    "What scars? I never even noticed.":
        
        $ renpy.pause (0.5)
        
        Br laugh "That's a good one. I couldn't have picked more obvious spots if I tried."

    "Not if you're uncomfortable with telling me.":

        $ renpy.pause (0.5)
        
        Br laugh "It's no trouble. Gotta pass the time somehow."
        
    "Go right ahead.":

        $ renpy.pause (0.5)
        
        Br laugh "Guess I was right. You are curious."
        

Br brow "At least they make me look extra intimidating at my job. No one's going to mess with the big, rugged chief of police."

Br laugh "You'd probably think I got them from some crazy, near-death case, but that's only true for one of them."

Br brow "The other was a completely different story."

scene black with dissolvemed

$ renpy.pause (0.5)

nvl clear

window show

n "Back when I was a kid, some of my friends and I always used to play outside and go \"adventuring\" together."

n "We could go anywhere, as long as it was close enough to town. Woods, mountains, beaches, we loved to explore every one of them. We got fairly familiar with our surroundings."

n "Then, one day, we heard from someone that there was a system of caves nearby. Caves! That was something completely new to us. Of course we went there as soon as we could."

n "We were all very excited. It wasn't a big cave system - not big enough to get lost in - but we still had so much fun that day."

n "So much, in fact, that I wanted to go back there right away. The next day, I called up a few friends, but they had a longer school day than I did. Instead of waiting for them, I decided to go alone."

window hide
nvl clear
window show

n "Turns out, going out exploring on my own was a little less exciting than doing so with friends. But I still had a pretty good time, and just walking through the entire underground system was quite an experience."

n "Plus, since I was alone, I could take the time to explore every last nook and cranny that I wanted to."

n "Maybe that was my mistake. When I was in one of the remote corners, the ground suddenly gave way and I fell about 5 metres into the cave below."

n "Luckily, I didn't get any serious injuries from the fall, but as I looked for another exit, an ominous realization set in: This cave had no entry or exit except the one I came in."

n "There were a few holes, but I could never fit through any of them or make them bigger in any way. Even if I could, I didn't know where they'd lead."

window hide
nvl clear
window show

n "In the end, I had to try and climb out on my own. But as you can imagine, I wasn't exactly the best climber in town."

n "Even so, I still got about halfway before I lost my grip and fell down again, cutting my muzzle on the edge of a rock in the process."

n "It bled pretty badly, but at least I knew to put pressure on the wound. I couldn't try to climb out again, however, so I waited."

window hide

$ renpy.pause (0.5)

show bryceback with dissolvemed:
    
    yalign 0.8 xalign 0.2
    
    pause 2.0
    
    linear 10.0 zoom 0.5 #xalign 1.0 yalign 0
    
        
$ renpy.pause (12.5)

hide bryceback with dissolvemed

$ renpy.pause (0.5)
    
window show

n "It took several hours for anyone to even notice that I was missing."

n "I must have been there for about four or five hours, all alone, before I heard footsteps above and a search party found me."

window hide

$ renpy.pause (1.5)

scene beachx at Pan ((300, 0), (300, 0), 0.0)
show bryce laugh
with dissolvemed

Br "Long story short, it turned out that besides the cave system we knew about, there was a much larger one right underneath. Those caves can only be entered with a guide now."

Br smirk "And I got this lovely reminder of the experience on my muzzle."

Br brow "I had plenty of time to think while I was down there, and later in life I often returned to that experience."

Br stern "At first, it made me want to get stronger, but I realized that strength alone wouldn't have saved me."

Br laugh "Our kind will probably never be able to climb much at all, but I can at least try to better myself. I guess the whole experience also kinda explains why I'm building those stupid wooden models now."

Br brow "Feeling so helpless while I waited down there...  it also made me realize I wanted to help others." 

Br "Having been saved by police sure did a lot to make me want to follow the same path. Turns out, I was good enough to even become chief."

Br laugh "Guess that's all of the trash. Thanks for the help."

Br normal "I suppose I'll have to tell you about the second scar some other time. Let's head back now, shall we?"

c "Sure."

scene black with dissolvemed
$ renpy.pause (1.0)
scene padx at Pan ((0, 240), (0,360), 3.0) with dissolveslow

$ renpy.pause (1.3)

show bryce brow with dissolve

label bryce3skip:

Br "Looks like it's already later than I thought. We better head to sleep soon."

if persistent.playedadine2 == True:

    if persistent.havemap == False:

        if gaveadinemap == False:
    
            c "(Oh, right. He may know something about the map Adine wanted.)"
            
            menu:
                
                "Ask him about the map.":

                    c "Before I forget, there was something I wanted to ask you about."
                    
                    Br normal "Sure. What is it?"
                    
                    c "It's about the underground building you found."

                    Br laugh "Right. We can't have any visitors there at the moment, or we'd probably have shown you the place by now."
                    
                    Br brow "Didn't Sebastian tell you to look at all the stuff we have about it in the archives?"
                    
                    c "He did, but I didn't get around to check it out yet."
                    
                    Br normal "Maybe you can do so some another time."
                    
                    Br brow "We should really get some sleep now, though."
                    
                "Don't say anything.":
                    
                    $ renpy.pause (0.5)

Br laugh "You can take the couch, and I'll just sleep on the floor or something."

c "Don't you have a bed?"

Br "Oh, this is just a temporary arrangement. I wanted to be closer to work and the new apartment wasn't ready yet, so I have to stay here for a while."

c "I see."

$ persistent.bryce3skip = True

Br "With all this armor, I'll barely even feel anything, so it doesn't matter where I sleep."

menu:
    
    "There's no need for you to sleep on the floor.":
    
        $ renpy.pause (0.5)
        
        Br brow "What do you mean?"
    
        menu:
            
            "The couch is big enough for both of us.":
                
                $ renpy.pause (0.5)
                
                Br laugh "It is, but I didn't know if you..."

                Br flirty "Well, if you say so."
                
                Br laugh "There's your bed, your highness." 
                
                Br normal "I'll take care of the light."
                
                #Br normal "Follow me, then."
                
                hide bryce with dissolve
                
                $ renpy.pause (0.5)
                
                play sound "fx/switch.wav"
                
                $ renpy.pause (0.4)
                
                scene black #with dissolvemed

                $ renpy.pause (0.5)
                
                Br "There we go."

                Br "Are you even going to sleep in those \"clothes\" of yours? It looks kinda uncomfortable."

                c "We usually have a separate set of clothing to wear during the night, or we just take off a few layers."

                Br "I see."

                Br "Well, it's not like I could take a layer off, except this little blanket here."

                c "Heh."

                Br "Is it okay for you to sleep like this?"

                c "Yeah."

                Br "Well, good night, then."

                c "Good night, Bryce."
        
                stop music fadeout 2.0
                
                $ brycestatus = "good"

                $ brycescenesfinished = 3
                
                if chapter4unplayed == False:
                                
                    jump chapter4chars
                    
                elif chapter3unplayed == False:
                    
                    jump chapter3chars
                    
                elif chapter2unplayed == False:
                    
                    jump chapter2chars
                    
                else:

                    jump chapter1chars
                    
                    
            "I'll sleep on the floor.":
                
                c "I'll sleep on the floor. You've already done enough with the BBQ and everything."

                Br laugh "Well, if you say so. I'm not going to argue."

                Br normal "See you tomorrow, then."

                c "See you."
        
                hide bryce with dissolve
        
                stop music fadeout 2.0
                
                $ renpy.pause (0.5)
                
                $ brycestatus = "neutral"

                $ brycescenesfinished = 3
                
                if chapter4unplayed == False:
                                
                    jump chapter4chars
                    
                elif chapter3unplayed == False:
                    
                    jump chapter3chars
                    
                elif chapter2unplayed == False:
                    
                    jump chapter2chars
                    
                else:

                    jump chapter1chars
    
    
    "Thanks, Bryce.":

        $ renpy.pause (0.5)
        
        Br normal "No problem."

        Br "See you tomorrow, then."

        c "See you."
    
        hide bryce with dissolve
    
        stop music fadeout 2.0
            
        $ renpy.pause (0.5)
            
        $ brycestatus = "neutral"
        
        $ brycescenesfinished = 3
            
        if chapter4unplayed == False:
                            
            jump chapter4chars
                
        elif chapter3unplayed == False:
                
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
    
    
        
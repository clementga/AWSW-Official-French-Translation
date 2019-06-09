label bryce4:

$ bryce4unplayed = False
$ bryce4mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Bryce 4"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Bryce 4"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Bryce 4"
    
else:

    $ save_name = "Chapter 1 - Bryce 4"

scene black with dissolvemed
$ renpy.pause (0.5)
scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolvemed

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(Oh, that must be him.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

play music "mx/shoal.ogg" fadein 2.0

show bryce normal with dissolve

Br "Hey, [player_name]."

c "Hey, Bryce."

#insert skip here

if persistent.bryce4skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_1

    call skiptut from _call_skiptut_1
        
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
            call skipcheck from _call_skipcheck_1
            
            scene o2 at Pan((0, 250), (0, 250), 0.1)

            show bryce brow 
            with dissolvemed
            
            play music "mx/shoal.ogg" fadein 2.0
            
            jump bryce4skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/shoal.ogg" fadein 2.0


c "I know you said you wanted to get out of that small apartment of yours, but I'm not sure if mine is much different."

Br laugh "Well, I figured yours couldn't be any worse than mine. And now that I'm seeing it from the inside, I have to say the council didn't do a bad job with it at all."

c "I assume it's appropriate for someone with my status."

Br normal "Whereas the Chief of Police has to make do with whatever he can get."

c "You said it was only temporary."

Br "It is, but I'm really getting sick of it, to be honest."

c "I can imagine."

Br smirk "Anyway, what's the plan?"

c "Plan?"

Br laugh "We gotta do something, right?"

c "If you want some entertainment, I could offer you a bookshelf full of it."

c "Here, {i}Sheridan and the Scepter of Sovereignty{/i} should be enough to last you a while."

Br smirk "No, thanks. I have enough fiber in my diet already."

c "I suppose you're not a fan of reading, then."

Br brow "Why would I visit you just to read some crummy book? And besides, I do read from time to time."

c "What do you read?"

Br laugh "Signs, menus, magazines..."

c "I don't think that counts."

Br normal "Let me take a look around your apartment, then."

c "Feel free, though I'm not sure if there's anything special about it."

hide bryce with dissolve

m "I watched with amusement as Bryce headed for the kitchen."

c "So that's what you're really looking for."

show bryce laugh with dissolve

Br "Guess what? I found something!"

m "He showed me one of the cheap bottles of wine that had been in the cupboard since I arrived."

c "Why don't you raid the fridge while you're at it?"

Br smirk "No, thanks. This will do for now."

c "Oh, I get it. You want to play spin the bottle."

Br laugh "Sure. We just gotta empty it out first."

c "I assume you don't mean emptying it into the sink."

Br smirk "Of course not, that'd be a terrible waste."

c "A terrible waste of the second cheapest wine from the store."

Br normal "I don't know how you humans are with stuff like that, but here we don't throw away perfectly good things."

c "I'm not sure this wine would qualify as \"perfectly good\"."

Br laugh "Hey, at least it's not the absolute bottom of the barrel."

Br smirk "Now, are you going to help me with this or not?"

menu:
    
    "If I have to.":
        
        $ renpy.pause (0.5)
    
        Br laugh "Well, you don't have to if you think the wine is that bad."

        c "But then you'd drink it all on your own."

        Br smirk "That's nothing for me. This bottle would be about... two beers, I think? Maybe even less than that."

        $ mp.teetotaler = False
        $ mp.save()


    "No, thanks. It's all yours.":

        $ renpy.pause (0.5)

        Br laugh "If you say so."

        c "You aren't planning on drinking it all at once, right?"

        Br smirk "That's nothing for me. This bottle would be about... two beers, I think? Maybe even less than that."


    "Sure.":

        $ renpy.pause (0.5)

        Br laugh "Alright, let's make it one glass for you and the rest for me."

        c "You think that's fair?"

        Br smirk "If I had to guess, I'd say I weigh 5-10 times as much as you do, so this is as fair as it gets."

        c "If you say so."

        $ mp.teetotaler = False
        $ mp.save()


m "I opened the kitchen cabinet to find an appropriate vessel for Bryce, but when I turned to ask him about it, he had already opened the bottle and was suckling on it like a baby."

c "I suppose that means I won't have to do any dishes."

c "How does it taste?"

Br laugh "Like wine, I guess."

c "Cheap wine. Besides, I thought you were more of a beer person."

Br "Hey, I take what I can get."

m "Just a few minutes later, the bottle had been emptied completely."

c "I'm not sure if \"drinking like a dragon\" is a phrase, but if it isn't, it should be."

Br smirk "Hey, not everyone can drink like me."

c "I see."

Br normal "And now we can finally play spin the bottle."

c "Don't we need more people for that?"

Br laugh "Damn, you're right. Now I drank all of this for nothing."

c "Somehow I think the whole spin the bottle thing was just an excuse so you could drink the wine."

Br smirk "What? I would never do such a thing."

c "Of course not."

Br flirty "Well, we could still play it with just the two of us."

c "At that point we wouldn't even need the bottle anymore."

Br laugh "C'mon. Where's your sense of funness?"

c "Is that even a word?"

Br normal "We're here to relax. You should lighten up a bit."

c "It's a bit hard to lighten up given everything that's been happening here. If anything, it's worse now than it's ever been."

c "Reza's actions are threatening our agreement and with it the survival of everyone I know back home."

c "But what really takes the cake is that he may have it out for me because I'm helping all of you."

Br stern "You want to have this conversation right now? Alright, let's have it. Just let it all out." 

c "Yeah, why don't we talk about Maverick? He may have it out for me because he thinks I'm working with Reza."

#c "And then, we have our human leadership back home, who may or may not have had it out for me since the very beginning and only sent me here to use me." 

c "And me? I'm just here, right in the middle of this whole mess, just trying to make the best of it."

Br brow "You know you're only involved in the investigation because we needed your help, right?"

c "I know. And I'm doing what I can, but that doesn't mean it's making the situation any easier."

Br stern "You think I don't know that? Me, the one responsible for every action our police is taking in this matter?"

Br "If you want to go ahead and blame someone, just blame me. I can take it."

c "I'm not blaming you. I'm just saying this whole situation is something I'm not very comfortable with."

Br brow "And whose responsibility is that, huh? However you look at it, it's me."

Br stern "I was the one who didn't listen to Maverick back when he had his suspicions about Reza. If we had acted then, this whole thing might not have spiralled out of control like it did."

Br "And despite what you might think about him, he was the one who found Reza's hideout, even after I forced him into sick leave."

Br "We were practically at Reza's front door and he still got away somehow. If I had done something different, we might have caught him."

Br "Let this be my official apology to you: I apologize for anything I might have done to wrong you." 

Br "I'm sorry for putting you through all of this and having to involve you in our work while trying to fix this whole mess, because in the end, this is all my responsibility."

c "You don't need to apologize for anything."

play sound "fx/bottlesmash2.ogg"

m "He hurled the empty bottle against the wall on the other side of the room where it shattered into pieces."

show bryce angry with dissolve

Br "Then what do you want me to do, huh?" with Shake((0, 0, 0, 0), 2, dist=10)

c "..."

Br "..."

c "I don't know."

Br sad "..."

c "..."

Br "Do you think it's easy for me? Seeing so many people die on my watch?"

Br "Do you think I don't keep asking myself the same questions? What I could've done differently, and if that would've made a difference?"

Br "You'd think as Chief I'd be used to it by now, but I'm not." 

Br "How could someone ever get used to this? It's my duty, you know. But I can't save them all. Never could."

if persistent.varasaved == True:
    
    pass

elif varasaved == False:
    
    Br "You know what happened out on patrol today? We found a dead child and her mother in their home in the outskirts of town."

    Br "The mother died from some sort of illness, and after that, the daughter never left her side again. As if she had just given up on life."

    Br "You try and think how you might explain something like that to the relatives. But I guess in this case we got lucky, because the father was one of Reza's earlier victims."
    

else:
    
    pass
    
Br "You've been to more than enough crime scenes by now. How have you remained so calm? Do all those who have died not matter to you?"

Br "I'm sorry for making you look at a corpse on your very first day here, but you know I had to. Your help here has been invaluable, and it's not like I could ask anyone else." 

Br "It's the same for me, really. Sure, they could ask someone else to be Chief, but If I'm the one who's best suited for the job, who am I to reject that? Otherwise, I'd have to blame myself for every mistake the other Chief made."

c "Is that why you drink?"

Br "It might come as a surprise, but..."

c "Actually, the alcoholic police chief used to be a huge stereotype in our world."

Br "Really?"

c "You wouldn't believe it."

Br "Actually, I do."

Br "The research about alcoholism in the police force is out there, but the general populace doesn't know about it. It's all just internal documents."

c "Why don't people know?"

Br "They don't want to know about unhappy things like that. Besides, they trust their Chief. If they knew about it, maybe they'd start to have their doubts."

c "I thought it was common knowledge that you visit the bar fairly often. Often enough that you're friends with the bartender."

Br "I don't know. Maybe they don't realize how it affects me. They see someone who can drink a lot and does it for fun. They don't realize what it means."

Br "What other stereotypes about the police are there in your world?"

c "That is the biggest one."

Br "I see. Well, alcoholism and suicide both are huge problems in law enforcement."

c "Suicide?"

Br "Yeah. If you have to deal with the things we do on a daily basis, it can affect you in pretty bad ways. Everyone has their breaking point."

Br "We all just cope in our own, different ways. Some do it better than others."

Br "That's why I'm worried about Maverick right now, and why I wish you'd known him as long as I have."

c "You think he's at his breaking point?"

Br "He's taking this whole Reza situation very personally. I'm just worried about him, you know. Just like I'm worried about everything else until we can sort out this whole mess."

c "It's personal for me, too."

Br "No matter what you may think about Maverick or what he may think of you, he still found Reza's hideout, which led us to the generators."

Br normal "I guess you have both helped a lot in this investigation."

Br sad "My point with all this is: We're all a very tight knit group at the police station. Me, Sebastian, Maverick, Naomi - the bond we form on the job is how we know to look out for each other."

Br "I can tell you there's nothing else quite like it."

Br "..."

Br stern "What do you think? How many more have to die to stop Reza?"

Br "If anything, he's more dangerous now than he's ever been before."

Br "You know how much depends on how this all turns out."

Br normal "Whatever happens, I'm just glad to have known you." 

Br "Remember when I told you about the wooden models I'm making?"

Br "I never told anyone else about that. As much as I like everyone at the department, it's just not something I can talk about with them. You saw us at the BBQ. I'd never hear the end of it."

Br sad "Sorry about the bottle, by the way. I'd clean it up, but..."

c "Don't worry about it. It was empty, anyway."

Br normal "Heh, that's the [player_name] I like."

Br "Oh, you won't believe what happened with Emera at work."

c "What did?"


if bryce3do == "string":
    
    Br laugh "Well, I did what you told me and played along with her."

    Br "She asked me for a massage again a while ago and..."

    c "You gave her a massage?"

    Br "Honestly, I have no idea what I did. I don't know how to give a massage, so I just pressed and rubbed her here and there."

    c "What did she do?"

    Br "Well, she seemed to like it a lot. There was a lot of grunting and moaning. Plus, she gave me a lot of compliments."

    c "I guess there was a lot of tension she needed to get rid of."

    Br "She should visit a massage parlor, then. They have people there who are way more qualified than I am."

    c "Do they?"

    Br smirk "Yeah, usually it's those who have better hands than I do. But then, she doesn't really want the massage anyway. She just wants me."

    c "What are you going to do next?"

    Br laugh "I don't know. After I gave her the massage, she just told me to go home and take the rest of the day off. And the next day she acted like nothing happened."

    c "Did she deny that it happened?"

    Br "No, I didn't even bring it up. We just went on with our work as usual."

    c "Strange."

    Br brow "I get the feeling she might ask me to do it again soon."

    c "And what will you do then?"

    Br normal "I'll probably just do it again. If I can get the day off, I can at least go back to the department and work on the case a bit instead of doing nothing in her office all day."

    c "Good point."

    Br laugh "It makes for an interesting story, that's for sure."

    c "True."

    show bryce normal with dissolve


elif bryce3do == "truth":

    Br smirk "I heeded your advice and told her the truth."

    c "Details, Bryce. Tell me everything."

    Br laugh "Well, the day before yesterday, she tried her thing again. Complained about her back pain to get a massage and asked me if I didn't want to settle down eventually."

    Br normal "At some point, I had enough and just told her outright that I'm not interested in her."

    c "For your own sake, I hope you weren't too harsh."

    Br laugh "Hey, you said I should tell her the truth, so I did."

    c "What did you say?"

    Br "Just that I noticed her clear attempts at wooing me, and that I'm not interested. That's all."

    c "And how did she react?"

    Br "Not much. She just looked at me and said: \"Oh, I see.\""

    c "That's all?"

    Br normal "Yeah, and she stopped with the comments after that."

    c "Guess that's not so bad, then."

    Br laugh "Well, not really. Now she's having me do all kinds of stupid things, like guard the outside of her office door for hours on end."

    c "Maybe she's still worried about Reza."

    Br "The building has its own security, so it's pretty clear that she's just doing it to get back at me for rejecting her. She's really good at hiding it, though. I'd never be able to prove it."

    c "You won't have to be with her for much longer."

    Br normal "Yeah, but I guess she'll just keep wasting my time until it's over."

    c "At least you tried to do the right thing."

    Br "Yeah."

    
else:
    
    Br smirk "Well, I did what you told me and asked her out."

    c "How was it?"

    Br laugh "Well, we didn't go yet. She was just doing her usual thing with her comments again yesterday, so I told her I noticed and that it'd be easier if we just went on a date to find out if we're compatible."

    c "And what was her reaction?"

    Br "I'm not sure. It seemed like she was both thrilled and in disbelief that I would propose such a thing."

    Br "She made it pretty clear that if it's just some sort of joke, there will be consequences. And of course I better be punctual."

    c "I can't blame her on the last bit."

    Br smirk "I think she just likes ordering people around."

    c "Maybe she does."
    
    show bryce normal with dissolve
    
    
c "Can I ask you something?"

Br "Go ahead."

c "If I told you that I'm a time traveller from the future, what would you say?"

Br smirk "Time travel? Isn't that something that just happens in bad science fiction novels?"

c "Why only bad science fiction novels in particular? Don't you think there could be a good one?"

Br laugh "Let's just say all science fiction novels, because they're all bad."

c "Huge generalization aside, what if we are in a science fiction story and time travellers are real?"

Br normal "I'd want to see some proof of it first. That's not something you come across everyday, after all."

c "What if I confided it to you as a friend?"

Br laugh "You'd still have to show me some proof or else I'd call you out on the joke."

c "What if I was serious?"

Br smirk "Well, it's pretty far out. That's the kind of thing someone would make up to scam people for their money, or something like that."

c "Alright, let's forget about time travellers. What if I told you there is another human here besides Reza and me?"

Br laugh "This is getting kinda weird, [player_name]."

c "Just entertain me for this question."

Br "Well, unless you had some sort of proof, I'd call you crazy."

c "As a member of law enforcement, aren't you supposed to follow up on every report?"

Br brow "Yes, but that doesn't mean we have to believe everything."

Br "If there is no proof, we'll look for proof. If we don't find some, well..."

Br "Without any proof or leads to follow, there's nothing we can do, anyway."

c "I see."

label bryce4skip:

c "By the way, when you and Sebastian went to the farmhouse to go after Reza, you just left me alone with Maverick in the same room."

Br laugh "I did?"

c "Yeah. I was worried there for a few seconds."

Br normal "Don't you worry about him. You mentioned that you had a talk with him about a week ago, and that didn't end badly for you either. He might be scary, but I don't think you need to be afraid of him."

Br "He's got a very strong sense of justice, so he wouldn't do anything to you without a good reason."

if brycegoodending == True:
    
    c "When we were alone, we had an opportunity to talk where he made his position very clear."

    Br brow "Did he threaten you?"

    c "No, I was honest with him. And in turn, I think he was honest with me as well."

    Br "Oh, really?"

    c "Yeah, I had nothing to hide. If he was willing to talk, I wasn't going to turn down the opportunity."

    Br "How did that go?"

    c "I think he doesn't suspect me as much anymore."

    Br laugh "Guess leaving you alone with him wasn't such a bad thing after all."

    c "I suppose you could say so."

    Br smirk "I just did."


else:
    
    c "The question is whether you or I would find those reasons good, too."

    Br brow "Seriously, don't worry about him. Don't base your opinion of him solely on that incident at the portal."

    Br stern "Do you really think he was wrong to suspect Reza, when Reza went on to do the things he's done?"

    c "When we talked with Emera, she pointed out that incident could've caused this whole mess."

    Br brow "No matter his reasons, do you really think you want to defend Reza's actions like that?"

    c "I don't know."

    Br stern "This sucks for everyone involved, so let's just focus on getting things done when on the job and not let it consume us elsewhere."

    c "Maybe you're right."

play sound "fx/fireworks.ogg"

c "What's that outside? Fireworks?"

Br normal "Yeah, must be the summer festival."

c "You wanted to get out of your apartment, and rather than go to the festival, you came here?"

Br laugh "The festival isn't really anything special for me anymore. Seen one, seen 'em all. Besides, it's usually more a thing for families, really."

c "I see."

c "Are those the fireworks people keep talking about?"

Br normal "No. They have a fireworks show every evening. Nobody really even cares about the first couple of days. It's only on the last day when they bring out the big ones. I usually watch those."

c "Oh, so if there's big explosions, then you care?"

Br "Well, yeah. But it's a big tradition here, maybe even an ideological one. Y'know, everyone in the whole town united under the stars, watching the beautiful fireworks. It's a thing."

c "People have been telling me for the last few days how I just have to see them."

Br laugh "Y'know, you kinda owe it to us as an ambassador to take part in a cultural event like that."

c "I'm going to go anyway, so you don't need to convince me."

Br smirk "Wanna come with me? I know all the good viewing spots. Most of the popular ones are usually super crowded, and we probably want to avoid those."

c "I can't really promise anything right now, but I'll keep it in mind."

Br normal "Well, you've got my number, so let me know as soon as you can."

c "Sure thing."

$ persistent.bryce4skip = True

if brycestatus == "good":
    
    Br laugh "You know, those fireworks are also often a couple thing."

    c "I'm not surprised. They can set the mood for a romantic evening."

    Br smirk "Well, they're still going on outside right now."

    c "Are you saying you want to go outside and watch?"

    Br flirty "No, I'm saying we could take this conversation elsewhere, namely the bedroom."

    c "The bedroom here is nothing special, I can assure you of that."

    Br laugh "Well, it's better than the one I have right now."
    
    Br normal "You know, when you slept over last time and we shared the couch, I took it as a sign."

    Br "Did that mean anything to you? Or was that just two friends sharing a couch that was clearly too small for two people who just wanted to stay friends?"
    
    menu:
        
        "It didn't mean what you thought it meant.":

            $ renpy.pause (0.5)

            Br laugh "That's my bad, then. Guess you humans don't do things the same way as far as that goes."
            
            show bryce normal with dissolve

            jump b4jump
            
        
        "It meant exactly what you thought it meant.":

            $ renpy.pause (0.5)

            Br flirty "Why don't we make this a little more romantic, then? Share a glass of wine and see where the evening takes us..."
    
            jump b4romance

        "It didn't mean anything, but we can still make this a romantic evening.":

            $ renpy.pause (0.5)

            Br smirk "Oh, really?"

            c "I didnt know you were interested."

            Br laugh "Guess you know now."

            c "So, what do you want to do?"

            Br flirty "Well, why don't we make this a little more romantic? Share a glass of wine and see where the evening takes us..."
            
            jump b4romance

    
else:
    
    label b4jump:
        
    Br "It's getting late, so maybe I should get going now."

    c "I suppose so. Thanks for coming, at any rate."

    Br "Thank you for having me. Don't forget to call me about the fireworks."

    c "Yeah, sure."

    hide bryce with dissolve
    
    stop music fadeout 2.0

    play sound "fx/door/doorclose3.wav"

    $ renpy.pause (2.0)

    $ brycescenesfinished = 4

    $ brycestatus = "neutral"
        
    if chapter4unplayed == False:
                        
        jump chapter4chars
            
    elif chapter3unplayed == False:
            
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
    
    

label b4romance:
    
    c "I should have another bottle in the kitchen. I'll go fetch it."

    Br laugh "Sure thing."
    
    hide bryce with dissolve
    
    m "I went into the kitchen to fetch a bottle of wine and two appropriate vessels, wondering how Bryce would manage a wine glass."

    m "When I returned from the kitchen, however, I was met with an unexpected sight."

    show brycerom at Pan ((500,0), (400, 300), 7.0) with fade
        
            
    $ renpy.pause (7.5)


    menu:
        
        "Scream.":

            m "Shocked at the display before me, I let out an involuntary scream."
            
            hide brycerom 
            #show bryce brow
            with fade

            m "Immediately, Bryce sprang to his feet, a somewhat embarrassed look on his face."

            show bryce brow with dissolve

            Br "What is it?"

            c "Is that what a romantic evening is for you?"

            Br laugh "Hey, I already had wine earlier, so I figured I'd speed up the process."

            c "You know what? Just get out."

            Br brow "Hey, I'm sorry. I didn't want to..."

            c "Yeah, whatever. Just go."

            Br stern "Alright, I'm going."
            
            $ brycestatus = "bad"
            
            $ brycescenesfinished = 4

            hide bryce with dissolve
    
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
            
            
        "Reject.":
            
            c "Bryce, what are you doing?" 

            hide brycerom 
            #show bryce brow
            
            with fade
 
            m "Bryce sprang to his feet, a somewhat embarrassed look on his face."

            show bryce brow with dissolve

            Br "What is it?"
                    
            c "Is that what a romantic evening is for you?"

            Br laugh "Hey, we already had wine earlier, so I figured I'd speed up the process."

            c "Seriously, is this how you dragons date?"

            Br "Some do. Some don't."

            c "Okay, so you do, but that's not what you should've done."

            Br normal "Why not? I thought you were interested."

            c "But not like this. That's just... way too fast, and not what we agreed on."

            Br laugh "Sorry, I guess I messed that up. But you know how I am. I rush into things and don't always think things through. That's the Bryce way."

            c "And the Bryce way is not always the best way."

            Br brow "Yeah, I know. Guess I'll take it as a lesson."

            Br normal "I should probably go now. It's getting late, anyway."
            
            $ brycestatus = "neutral"
            
            $ brycescenesfinished = 4

            hide bryce with dissolve
    
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
                
                
                
        "Accept.":
            
            c "Oh my."

            hide brycerom 
            #show bryce brow
            
            with fade

            m "Bryce sprang to his feet, a somewhat embarrassed look on his face."

            show bryce brow with dissolve

            Br "What is it?"

            c "No, that was fine. Don't stop."

            Br flirty "Not something you've seen here before, huh?"

            c "Not like that."

            Br smirk "And then, especially with my kind, they are... Well, I think you can see what I mean."

            c "Mmm-hmmm."

            Br laugh "Do you just want to stand there and keep staring?"

            c "No."

            Br flirty "Then why don't you come a little closer?"

            c "Alright."

            $ mp.bryceromance = True
            $ mp.save()

            $ brycestatus = "good"

            stop music fadeout 2.0
    
            $ renpy.pause (0.5)

            $ brycescenesfinished = 4

            if chapter4unplayed == False:
                    
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars







$ renpy.pause (0.5)
stop soundloop fadeout 3.0
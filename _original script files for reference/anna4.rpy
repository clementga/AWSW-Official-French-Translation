label anna4:

$ anna4unplayed = False
$ anna4mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Anna 4"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Anna 4"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Anna 4"
    
else:

    $ save_name = "Chapter 1 - Anna 4"

scene black with dissolvemed
$ renpy.pause (0.5)
scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(Guess she's here.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

play music "mx/anna4.ogg" fadein 2.0

show anna cry with dissolve

c "Hey, Anna."

An "Hey."

c "What's going on? You sounded pretty worried on the phone."


#insert skip1 here

if persistent.anna4skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_66

    call skiptut from _call_skiptut_17
        
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
            call skipcheck from _call_skipcheck_17
            
            scene o at Pan((0, 250), (0, 250), 0.1)
            show anna face
            with dissolvemed
                        
            play music "mx/anna4.ogg" fadein 2.0
            
            jump anna4skip1
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/anna4.ogg" fadein 2.0
            


An face "Worried? If I was worried, it would mean I was afraid of something that might happen, but I'm way beyond that."

An disgust "I know exactly what's going to happen to me."

An cry "It's over. It's all over."

c "What are you talking about?"

An "First they came to my lab, and now they went to my home, too."

c "Who did?"

An despair "The police. They raided the place. They had a warrant and everything."

An cry "I already know that they have all they need to convict me. I'm going to die in prison."

c "Why?"

An "It's because of those tests I did on you."

c "You will die in prison, because you looked at my fingernail under the microscope?"

c "I'm a bit confused. Why dont you start from the beginning?"

An "Alright."

stop music fadeout 2.0

$ renpy.pause (0.5)

scene black with dissolvemed

$ renpy.pause (0.5)

nvl clear

window show

#window hide
#nvl clear
#window show

$ renpy.pause (0.5)

play music "mx/anna3x.ogg" fadein 2.0

n "This goes years back, and you already know half the story."

n "I was a brilliant mind who had skipped years in school and was on the fast track through university with an incredibly lucrative career in front of me."

n "You wouldn't believe the offers I had, based on all my accomplishments."

n "I was still in school and already solving problems that no one had even touched before."

n "I had so many awards lining my shelves that new ones just went straight to the trash. I didn't need them; I just enjoyed the challenge."

n "Besides, I couldn't care less about what some old people thought about my work. As if I needed their approval. I was already more than any of them could have ever dreamed to be."

window hide
nvl clear
window show

n "The next problem I was going to tackle was an incurable disease."

n "I started my research, but in an ironic twist of fate, I ended up contracting that very same disease myself."

n "Whether someone had not been following health & safety protocols as well as they should have or if I was just unlucky, I'll never know. But the reality was that I now had a disease that was treatable, but not curable."

n "Despite having helped an incredible amount of people with my work, I was now the one who needed help… Yet there was no one who could help me."

n "No one but myself."

n "I was already planning on working on a cure anyway, and what better reason could there ever be than doing it to save myself?"

window hide
nvl clear
window show

n "I told no one about my affliction and set out to do what many others had failed to. Any materials I needed to start my work were easily acquired just by waving my status around."

n "I had free reign over my own lab. I could've even gotten assistants if I wanted to, but I knew they would only be liabilities."

n "I even had a few good leads for ways to combat the disease, although the one that I chose to pursue was not exactly legal."

n "Not without prior approval by the council. My research was promising, though. And while I submitted the paperwork, I knew that these things always moved slowly."

window hide
nvl clear
window show

n "Being pushed through the various boards and committees could have taken months, if not years, depending on how generous they would be. I just couldn't afford to wait that long, as I was working against the clock."

n "So, while waiting for the paperwork to be approved, I had already started with my work. I fully expected them to approve it eventually. How could they not, given that I was tackling an incurable disease?"

n "The method I was going to use was not necessarily a new one, but it was controversial. It didn't even cross my mind that anyone would object, seeing as I would cure thousands, if not millions of future people."

n "But I was younger then, and a little more naïve than I am now."

window hide
nvl clear
window show

n "In the end, my whole project came crashing down in flames."

n "The proposal that I was sure would be approved was ultimately rejected, putting all the work I had already done into jeopardy. I had already made good progress at the time, too."

n "After the rejection, there was going to be an inspection of my workplace in order to determine the progress I had made on the project, which they assumed had been within legal bounds and didn't include the controversial things outlined in the paperwork."

#n "Since my proposal was rejected, I was going to meet with other scientists to determine an alternative strategy."

n "Of course, that meeting was just going to be a pretense, because I knew there were already rumors going around about what really went on in my lab."

window hide
nvl clear
window show

n "In the end, I had very little warning. Thankfully, I managed to dispose of the most egregious evidence before they arrived."

n "They found proof of my wrongdoing, but since they didn't find evidence of how far I had already proceeded, I was able to deny most of their accusations."

n "Using the controversial method when it hadn't been approved was still seen as a very grievous offense, however."

n "I was charged and sentenced harshly, though the sentence was suspended due to their lack of evidence."

n "With all I had done for them, they knew better than to take away my license, and I was able to continue work in other areas, under the condition that it was within a council-owned facility."

stop music fadeout 2.0


window hide
nvl clear

$ renpy.pause (0.5)

show o at Pan ((0, 250), (0, 250), 0.0) 
show anna cry

with dissolveslow
#with dissolvemed

play music "mx/anna4.ogg" fadein 2.0

c "I see. So I assume that those tests on me were against whatever conditions they set for the suspended sentence."

An "Exactly."

c "Why didn't you just do things the proper way and wait for the paperwork to clear?"

An face "Before my paperwork would even get through, you’d be long gone." 

An "Using you as a test subject would’ve been a process that the council would have to discuss with humanity. As such, there might have been another trade agreement and who knows what else!"

An "I just didn't have the time. Quite frankly, I don't even know how much longer I have left."

An cry "This is my death sentence."

c "You thought my test results would help you find a cure?"

An despair "And that's never going to happen now."

c "How did they find out so quickly? It's not been that long since I came to your lab."

An cry "It wasn't just those tests. There was Reza, too."

c "But Reza told me he didn't give you any of his blood when you asked for it."

An "Because that's not what I got from him."

An "This is my life we're talking about. Do you think I didn't spend hours on the ground in the hallway of the facility after Reza's first visit, trying to find a stray hair or anything else I could use?"

An "Or that when I gave him that first generator I didn’t try to graze his skin just enough so that I could salvage a few skin cells?"

#An "Do you think it's fair for me to die in prison, just because I didn't ask for permission?"

c "How did they find out about all this?"

An rage "It was Damion, my assistant. That piece of shit."

An cry "He was blackmailing me."

c "Why?"

An face "Because he's jealous of me. Jealous of my success."

An cry "He found out what I was doing with the stuff I could salvage from Reza."

An "I didn't mind giving him what he wanted, though. I just wanted to live."

An "When he died and the police searched his apartment, they found all the evidence he had on me."

An face "And now, everything is coming down. I will be punished to the full extent of the law, and I will die in prison."

An "My work will forever be tainted. Not that I'll care about that when I'm dead."

An cry "Do you remember that childhood friend of mine I told you about? I never wanted to end up like her, but it seems not even I can do anything to escape that fate."

An "Maybe I deserve it."

An "Maybe it's my punishment. I have to die like she did, because I left her."

An "I will spend my last days bedridden in a prison cell, and no one will visit me or care."

An face "And you know what? With all that data I got from you, I might've actually found a cure."

An cry "..."

An face "I don't want to cry in front of you. I don't want the attention or the pity. I don't want it."

label anna4skip1:

An cry "I didn't cry back when I was diagnosed, and I'm sure as heck not going to cry now."

if persistent.endingsseen > 0:

    if persistent.heardaboutcancer == True:
        
        menu:
            
            "Don't say anything.":
                
                jump a4otherwise
                
            "Tell her you know about her cancer. {image=image/ui/status/heardaboutcancer.png}":
                
                c "You have cancer."

                An "How do you know that?"
                
                if persistent.heardaboutcancerremy == True:

                    c "Remy told me."

                    An disgust "What?"

                    An face "He must have used his position to look into some confidential documents."

                    An disgust "That's not exactly legal either. What a hypocrite. Why don't they just throw him into prison as well and let us rot together, huh?"

                    An "All those filthy bureaucrats. You should've heard them."

                    An "How they don't want to change the rules, because our tradition is sacred and that's how we've survived all those years."

                    An cry "Tradition now demands that I die."

                    An "But you know what? I'm not playing by their rules. Never have."

                    An disgust "Actually, why don't I line up all of those who got me here and kill them?"

                    An "Because if I'm going to die, why shouldn’t I take them with me? I mean, I have nothing to lose if I’m going to die anyway."

                    c "Don't do that."
                    
                    show anna despair with dissolve

                    An "Just give me one good reason!" with Shake((0, 0, 0, 0), 2, dist=10)
                    
                    c "Because where I come from, we can cure cancer."

                    $ mp.annaheardaboutcancer = "remy"
                    $ mp.save()
                    
                else:
                    
                    c "I saw your treatment plan when I was waiting for you on our date."
                    
                    An disgust "What?"
                    
                    show anna rage with dissolve
                    
                    An "How dare you look into my personal belongings?" with Shake((0, 0, 0, 0), 2, dist=10)
                    
                    c "Hey, I wouldn't have if you didn't keep me waiting."
                    
                    An disgust "So what? That doesn't give you any right to look into my stuff!"
                    
                    c "It just happened, okay?"
                    
                    An "Now you show your true colors, [player_name]."
                    
                    An "You are just as duplicitous as our government."
                    
                    An "They keep talking about how they care about everyone, yet that wasn't what happened to me."
                    
                    An cry "It's their backwards rules and traditions that now demand that I die."
                    
                    An disgust "The same rules and traditions that would make them worship you, just because of some stupid, old legend."
                    
                    An "You know it and used it to your advantage to arrange this one-sided trade with us."
                    
                    c "That wasn't me."
                    
                    An face "It doesn't matter if it was you in particular or one of the other humans."
                    
                    An disgust "You still work for them, don't you?" 
                    
                    An sad "You look into things you shouldn't, and Reza does whatever the heck he does nowadays."

                    An face "Why did I even come here today? To have another knife driven into my back?"
                    
                    An sad "I'm just not sure why I ever expected anything different from you."
                    
                    c "It's not like that at all."
                    
                    show anna rage with dissolve
                    
                    An "Oh, really? Prove it." with Shake((0, 0, 0, 0), 2, dist=10)
                    
                    c "Where I come from, we can cure cancer. If you came with me..."
                    
                    $ mp.annaheardaboutcancer = "pry"
                    $ mp.save()
                    
                    

                An cry "..."
                
                An "You can? Are you saying that if I went back with you, if you smuggled me out, that you could cure me?"



                c "We have the facilities. If we had the power from the generators we asked for, we could."

                An rage "Are you kidding me? Because if you are, I'll..."

                c "No, it's the truth."

                An cry "..."

                c "Maybe we could work something out. I'm sure humanity would not object, or maybe we could just give you the technology or the necessary method. We have already cured cancer, so there's no need for you to die."

                An "Why would you do that for me?"

                An "You know I didn't care about you. I just wanted your blood, your data. Just anything that would help me save myself."

                c "And that's exactly what I'm going to give you."

                An "Why? Nobody has ever cared about me. People were always willing to use my research, but I was just a machine to churn out results for them. That's what all the awards were for."

                $ annagoodending = True

else:
    
    label a4otherwise:
         
         pass
         
         
An "I admit that I was selfish. Always. Yet I did great things. At least that's what everyone kept telling me."

An "You know, after that whole affair back then and the suspended sentence, the rumors about me never stopped. Did they warn you about me? Tell you to stay away? I'm sure they have."

An "Why are you still here?"

c "I didn't listen to them, I guess. Just like you."

An face "The Council, Damion, Remy... They were always sabotaging me. If everyone just left me alone, I wouldn't even need your help."

An cry "Why couldn't everyone just leave me alone?"

An "When they gave me the manager position at the facility, that was just to distract me even more. Giving me free reign over the lab so I'd be tempted to do something I shouldn't."
         
An face "How could I not at least try?"

An cry "One of their oh-so-important founding principles is how every individual is important. That's clearly not the case with me. At least, they never showed it was."

An "Now I can see just how different you are."

An "You are the only one who came to me willingly and without any ulterior motives."

An "Or did you?"

c "You invited me. I just took that invitation."

An face "Just to use you."

An cry "And you still came back for more. You let me do all those tests on you. Sure, you complained like a pro, but you sat it out for me."

c "I owed it to you."

An face "You don't owe me anything anymore." #Heck, today I wanted to meet you, because of this whole mess and you still took me in."

   # Heck, even now you took me in even though I never did anything for you."
   # Heck, even now you took me in even though I did nothing for you in return."

c "So what?"

if annagoodending == True:
    
    An cry "Maybe I won't have to die, after all."

    An "If you can cure me, I'll give you whatever you want."

    An "I know there's politics involved, and I know it may not ever happen, but this is my last straw, my last hope."

    c "I'll do what I can."

    An "Thank you."
        
else:
    
    An cry "Maybe I won't have to die alone, after all."

    c "I don't know if I'll be able to be there."

    An "It doesn't matter. You've already done more than enough for me. I'll remember you when I die."


#insert skip2 here

if persistent.anna4skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_67

    call skiptut from _call_skiptut_18
        
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
            call skipcheck from _call_skipcheck_18
            
            scene o at Pan((0, 250), (0, 250), 0.1)
            show anna normal
            with dissolvemed
                        
            play music "mx/anna4.ogg" fadein 2.0
            
            jump anna4skip2
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/anna4.ogg" fadein 2.0

An sad "Anyway, enough of that. I hope you dont mind me hanging around here. My place still looks like the police raided it. Oh, wait, that's exactly what happened."

c "Do you need help cleaning up?"

An face "No, I can pay someone to do it later. I just don't want to be there right now."

An sad "Nice apartment you've got here, by the way. Not quite as fancy as mine, but this isn't bad either. I guess the council treats you nicely, huh?"

c "Hey, it wasn't my decision."

An face "You're such a VIP, aren't you?"

c "I can't be that important if your apartment is nicer than this."

c "Besides, after your rhetoric about being wild and all that when we went on our date, I assumed you were more the type of person who just lives in a hole in the ground."

An sad "That's not what I said. I told you I can appreciate all kinds of different experiences. I could survive in the wild if I wanted to, though." 

An normal "Do you want to know what I did on my last vacation ? I just started walking in a random direction. I spent a week in the wilderness before I came back."

c "That must've been an adventure. I wouldn’t be able to do that without tools."

An sad "I could give you some tips if you'd like."

c "Not sure if I'll ever need them, but I guess they could come in handy."

An "Actually, there's one tip that should take care of everything."

c "Let's hear it, then."

An normal "Just be a dragon. Then you've got everything you need and don't have to rely on tools and other stupid stuff."

c "Yeah, that's super helpful. How do you think I'm supposed to do that?"

An smirk "Not my problem."

c "Actually, can you tell me about your advances in genetic engineering? Maybe you could make it happen."

An face "My personal ones?"

c "I was speaking more of your society as a whole, but if you have personal experience, that could also be interesting."

An sad "We could do so much if we wanted to. Cloning, genetic scrambling or hybrids of our various different species." 

An "Heck, we could even create new species if we wanted to, but that's not going to happen any time soon. Tampering with genetics is not allowed."

c "Why?"
    
An face "Our enlightened society does not see any value in it. Besides, you know about our creation myth, right?"

c "The one about a human creating you?"

An normal "Yeah, that one. It's the only one we have."

An face "Anyway, we are not to tamper with the perfect images after which we were created."

c "And what would those be?"

An normal "The belief is that each species was molded for particular tasks, or a particular role in our society."

c "Really?"

An "Some of them aren't even wrong. It suggests certain species should go into certain jobs, because of their naturally higher aptitude in those fields."

c "Can you give an example?"

An "Well, let's just say that while everyone can join the police force, you'll never be the flyer on duty unless you belong to a species that can fly."

c "That much is a given. I was talking more about if there is any sort of discrimination, for example."

An "You could say so. These structures can be pretty rigid in places, especially where the council is concerned. They really like to employ the members of the various species in their traditional roles."

An sad "Ironically enough, the perpetual nuisance you know as Remy was a revolutionary case where that didn't happen."

c "In what way?"

An normal "Well, a council's aide - particularly one who works in the archives - is usually a member of a species with more dextrous hands. You can't really expect a four legged species to do that kind of job well."

An face "And he doesn't. It's really been a disaster. He's basically become the laughingstock of the whole town."

An sad "When Remy initially got the position, there was a lot of controversy about the subject. Some liked it, some didn't."

c "I thought that for Emera, politics was a popularity contest. Doing something controversial and divisive like that doesn't really fit that image."

An normal "She wasn't like that in the beginning. It certainly caused people to remember her, though, and now that people know her, she has changed her attitude a bit."

An "It was a good move, because it kept her in the spotlight all the time. And she's using it to gain popularity now."

c "So she just likes the attention?"

An sad "I don't know why she does it, and frankly, I don't care. You'd have to ask her yourself, but I doubt she'd tell you. I wouldn't expect honesty from someone like her."

c "Politics always used to be so messy back home... Scandals, arguments, lies. They were everywhere."

An "We do get the occassional scandal from time to time, and of course there's always rumors. You can't really make people stop talking."

c "In a way, I'm glad we don't have all that anymore."

An normal "Why not?"

c "At some point, it just gets tiring. People get loud and argumentative, and those are supposed to be our leaders."

An sad "That's not something people would like here. If you are a council member who wants to be popular, you don't engage in that kind of behavior."

c "That sounds like a nice change of pace."

An face "Not necessarily, since it also leads to reluctant agreements and sweeping issues that should be talked about under the rug. You know what? That doesn't jive with me."

An sad "They like to preserve this fantasy of peace and harmony in our society. For me, it's just so fake." 

An face "People pretend to be something they aren't to conform, because they don't want to stand out. They become faceless puppets, like drones in a hive or cogs in a machine." 

An sad "What kind of world do we live in where speaking one’s mind is seen as something bad? I never held back… Now, see where that got me."

c "I bet some would argue that it would just be easier to conform, then."

An normal "I could never do that. And besides, I don't want to. There is this thing called \"integrity\", and if there's one thing this society needs, that's it."

c "Now you're starting to sound like a politican."

An face "If that's what your politicans sound like, maybe they aren't so bad. Sometimes, I just want to walk up to some of ours and shake them until they wake up and accept the truth."

c "What is the truth?"

An normal "I'm a scientist. Truth are facts that are empirically verifiable by science and tests. After all, the tests I do in my job are to find out if assumptions are true or not."

c "I suppose if you asked different people, their definitions of truth would be very different."

An smirk "What's truth to you, then?"

menu:
    
    "Truth is what I feel is right.":
        
        $ renpy.pause (0.5)

        An face "That's something our politicians would say."

        c "At least they have good intentions if they do what they feel is right."

        An sad "But good intentions alone don't get us anywhere. If we all just followed everyone's ill-informed good intentions, it'd be chaos."

        An face "Just look at me, I'm a victim of this. Stupid backwards laws made on so-called \"good intentions\" are what will put me in prison."

        An sad "That kind of thinking doesn't help in my work, because in the end, feelings can be wrong."

        c "You're not wrong, and we could argue about that all day, but the truth of the matter is that I wouldn't be here with you right now if it wasn't for me just trying to do the right thing."

        An "..."

        show anna normal with dissolve

        
    "I share your view, actually.":

        $ renpy.pause (0.5)

        An face "There aren't nearly enough people like that around here."
        
        show anna normal with dissolve


    "I know that I know nothing.":

        $ renpy.pause (0.5)

        An face "What's that supposed to mean?"

        c "It's a philosophical phrase. It means that, ultimately, we can't really know anything with absolute certainty."

        An sad "Yeah, philosophy is nice and all, but that doesn't really help me when I'm in the lab."

        show anna normal with dissolve


An "You do seem to like talking about this kind of stuff, though."

c "I'm not an ambassador for nothing, you know."

An face "You're an ambassador so you can discuss the nature of truth with different cultures? You know, if you asked the wrong kind of person, these kinds of discussions could turn very ugly."

c "I'm certainly here to learn about what you're thinking and how your society works on a deeper level. Of course I wouldn't just walk up to someone on the street and start talking."

An sad "Maybe you should be talking with someone in social studies, then."

c "Not necessarily. Even if someone like that gave me their opinion, it's still important to hear the people's voices themselves."

An face "Okay. Anything else you want to know?"

c "How much do you really like me?"

An sad "That's not the kind of question I was expecting."

c "You called me when things went down, and you say you don't really know anyone else."

An face "So what?"

c "Is it that hard to admit that you like someone?"

An sad "You know me a little by now. You know what I'm like. Whatever you're looking for, you know I'm not that kind of material."

c "Not even as a friend?"

An face "You want to use emotionally laden words to describe our relationship? We've met a few times, and that does it for you?"

c "This isn't about me. Before anything happens to either of us, I just want to know."

An "You want me to tell you how I feel about you?"

An sad "Even if something happened between us, you know it's not made to last. You will go back to your own world, and I'll probably spend the next few years in prison."

c "You wouldn't like the commitment anyway, would you?"

An normal "True. I wouldn't let something like that hold me back. People don't like me, and I don't like people. That's how it's always been."

An sad "Right now, though, I'd have to say that you're probably the person I hate the least."

c "That's something, I guess."

An normal "And I also can't deny that you have a certain exotic quality about you."

c "Now you're talking."

label anna4skip2:
    
$ persistent.anna4skip = True

An sad "But enough about me. If you've put up with me for this long, it can't all just be your own unselfish kindness, can it?"
    
menu:
    
    "I was smitten with you since the first time I saw you.":
        
        $ renpy.pause (0.5)

        An face "Oh. Looking back, that actually explains a lot."

        An sad "Why else would you follow my every whim?"

        An normal "Not that I mind. We both got what we wanted. And now I even kinda like you."

        An smirk "Usually, people stay away from me after the first date, because that's apparently all it takes. Not for you, I guess."
            
        jump a4romance
    
    "I don't hate you, too.":

        $ renpy.pause (0.5)

        An smirk "I guess we feel the same way, then."
    
        jump a4romance
        
    "I just did it to be nice.":

        An "So, you met with me multiple times just because it was the right to do?"

        c "That's right."

        An "Then why did you meet me now if you don't care?"

        c "You sounded upset and I wouldn't let anyone in such a situation down. I guess I don't like you the same way you like me, though."

        An face "You're such a do-gooder. You spent enough time with me that I started to care, and then it turns out it's just platonic."

        An sad "You know what? I don't deserve you. Find yourself someone who is as nice as you are and be happy."

        c "I can do that, but that doesn't mean I can't hang around with you."

        An "Alright, if that's how you really feel, then do me one favor."

        c "What is it?"

        An "Watch the fireworks with me."
        
        c "The fireworks?"

        An "The big fireworks show at the end of the summer festival. It may be the last one I'll ever see. If the police don't arrest me beforehand, that is."

        c "I really can't promise anything right now, but I'll try."

        An "I figured as much. Don't worry about it, though. I can see it on my own. It just would've been nice to have some company."

        An "Anyway, I guess it's time for me to go. There is plenty of stuff I have to take care of before they take me in. Research papers, the facility and other things."

        c "Don't let me hold you up."

        An normal "Thanks for having me."
        
        $ annastatus = "neutral"

        $ annascenesfinished = 4
        
        hide anna with dissolve
    
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

    
    
label a4romance:
    
    #both are smirk

    An "You know, this might be our last opportunity to do something. Why not make it worth it?"

    menu:
        
        "If you say so.":

            An "Is that a yes?"

            c "Yes."

            m "She strode forward, reaching out with a claw before she hooked it into the neckline of my shirt."
            
            show annarom at Pan ((580,608), (0,0), 12.0) with fade
            
            $ renpy.pause (10.0)
            
            hide annarom with fade

            c "What are you doing?"

            An normal "Well, we have to take these off, don't we?"

            c "Not like that! You'll ruin them. I'll do it."

            An face "Alright, alright. So fussy."

            $ mp.annaromance = True
            $ mp.save()
            
            $ annastatus = "good"

            $ annascenesfinished = 4

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
                
                
        "I can't.":

            c "I'm sorry, but I can't."

            An face "Why not?"

            c "Not now. It wouldn't feel right to me."

            An sad "I see."

            An "Well, I guess it's time for me to go, then. There is plenty of stuff I have to take care of before they take me in. Research papers, the facility and other things."

            c "Don't let me hold you up."

            An normal "Thanks for having me, anyway."
            
            $ annastatus = "neutral"

            $ annascenesfinished = 4

            hide anna with dissolve
    
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
    
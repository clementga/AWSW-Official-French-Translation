#-10 +8

label remy3:

$ persistent.playedremy3 = True
$ remy3unplayed = False
$ remy3mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Remy 3"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Remy 3"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Remy 3"
    
else:

    $ save_name = "Chapter 1 - Remy 3"

scene black with fade
$ renpy.pause (1.0)
scene park2 with dissolveslow

#insert skip here

if persistent.remy3skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_94

    call skiptut from _call_skiptut_24
        
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
            call skipcheck from _call_skipcheck_24
            
            scene park2

            show remy shy
            with dissolvemed
            
            play music "mx/gravity.ogg" fadein 2.0
            
            jump remy3skip1
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            #play music "mx/shoal.ogg" fadein 2.0

play music "mx/gravity.ogg" fadein 2.0

show remy normal with dissolve

c "Hey, Remy!"

Ry "Hello, [player_name]."

c "Is there any particular reason why you wanted to meet here?"

Ry "I enjoy Tatsu Park is all. Have you been here before?"

menu:
    
    "Can't say I have.":

        $ remy3mood += 1
        
    "A few times.":
        
        $ remy3mood -= 1
        
    "Once or twice.":
    
        pass
        

Ry "I see."

Ry "Well, what do you think of it?"


menu:
    
    "It's pretty idyllic.":
        
        $ renpy.pause (0.5)

        Ry smile "It is. I like it a lot here."
    
        show remy normal with dissolve

    
    "It's pretty romantic.":

        $ renpy.pause (0.5)
        
        Ry shy "You think so?"

        c "Yeah, just look at those trees. Would make a nice spot for a date, really."

        Ry normal "I agree with that."

        $ remy3mood += 1
            
    
    "It's nothing special.":

        Ry "I suppose you don't appreciate the simple things, then. I like it here."

        $ remy3mood -= 1
        
        
c "You mentioned you wanted to talk to me about something."

Ry shy "Yes, well... about that..."

Ry "I just have a lot on my mind and I felt like I needed to tell someone."

Ry "I wouldn't burden you if I had anyone else to talk to, but the simple fact is that I don't."

c "Hey, you can talk to me, Remy."

Ry "Thank you. I appreciate that."


c "It's not a problem. What's on your mind?"

Ry sad "I don't even know where to begin."

Ry "Do you ever feel like there is an emptiness inside you? That every day is the same, joyless routine that you wish you could escape - but you can't?"

menu:
    
    "I do.":

        $ mp.depression = "yes"
        $ mp.save()
        
        pass
        
    "I used to.":

        $ remy3mood += 1

        $ mp.depression = "past"
        $ mp.save()
        
    "Can't say I do.":

        $ mp.depression = "no"
        $ mp.save()
        
        $ remy3mood -= 1

Ry "I see."

c "Is this about Emera again?"

Ry "Well, it's not just about her, but working with her doesn't make things any easier."

Ry "To think that just a few years ago I was the happiest I could've been. And now, I have nothing but my miserable life."

c "What happened?"

Ry "It's a long story."

menu:
    
    "We have a lot of time.":
        
        $ remy3mood += 1
        
    "Make it a quick one.":
        
        Ry "I'll try."
        
        $ remy3mood -= 1
        
    "I don't mind.":
        
        pass
        
        
Ry "Okay, well..."

scene black with dissolvemed

$ renpy.pause (0.5)

nvl clear

window show

n "A few years ago, I worked in the public sector. I mean, I still do, but my position was a different one. I didn't work under a minister back then."

n "I was part of a committee tasked with providing independent and factually backed opinions on community topics. It was supposed to help not only politicians, but also the general populace."

n "Free from outside interference, we did our own fact-checking based on research and publicly reported our findings. Our individual members didn't always agree, but we made sure the end results were based on verifiable facts."

n "In this way, we offered a variety of comprehensive opinions on difficult topics. We found the truth, and allowed people and politicians to make up their minds from there. Our work was a key influence in the community, and because the conclusions of each individual member were often very different, it could never be said that we were biased."

#scene black with dissolve
window hide
nvl clear
window show

n "It was during one such assignment that I met a certain person named Amelia."

n "My task was to determine the viability of several projects, each competing for a research grant from our council."

n "Amelia was a member of one of the scientific teams vying for a grant. She was an inventor, and her group was looking for ways to streamline hospital processes and tests by utilizing new technology."

n "The first time I saw her was when our committee watched her group's pitch. One of the things we had to do was determine whether their claims and goals were realistic."

n "In her case, they were."

n "Ultimately, they didn't get the grant, but when she recognized me in a restaurant a while later, we started talking."

window hide
nvl clear
window show

n "She was very smart, and I admired her spirit. She just wanted to help people with her talents - and in this way, she reminded me a lot of myself."

n "We kept seeing one another, and we grew close. Before long, we were dating. It felt so right..."

n "I thought our relationship was about to become very serious, but then she informed me that her research group had applied for another grant."

n "Of course, that complicated things. My committee was once again tasked with judging the viability of the different projects, and while I intended to stay impartial on the matter, she would probably be seen as an influence due to our relationship."

n "With these concerns in mind, we decided to not meet again until the grant winner was determined. We hadn't expected her group to get it, but in the end, they did."

window hide
nvl clear
window show

n "We didn't want to end our relationship over something like that, but if word got out that we were together during the decision-making period, it would've put both our jobs in jeopardy."

n "In the end, we decided to wait and made a commitment. Six months after the grant was given to her team, we would return to one another and make our relationship public. That much time would have ensured that it wouldn't be an issue. We even made plans to move in together when that time came."

n "But we never got that far. I only know the rest of what happened from various reports, but apparently, Amelia got sick. Nothing serious, mind you. She continued working from home as best as she could. The project was already behind schedule, and she didn't want to endanger it."

window hide
nvl clear
window show

n "People were critical and very curious about what the project would amount to, and she didn't want to be responsible for its failure if she took some days off to recuperate." 

n "So, every day, she continued working on the project until the dead of night."

n "One late evening, she went out to pick up her medication - in addition to something to help her stay awake. But she was sick and overworked. The combination of the prescription's side effects and the supplements caused her to collapse. No one was around to see her fall."

n "When she was found the next day, she was covered by a blanket of fresh snow."

n "It was too late." 

n "She froze to death during the cold winter night."

window hide
nvl clear
window show

n "If someone was with her, this would not have happened." 

n "But she died out there, all alone." 

n "All because we kept our relationship a secret."

window hide

$ renpy.pause (1.5)

scene park2
show remy shy
with dissolvemed

Ry "We had plans to move in together. We even talked about having our own, small family."

Ry "Some things are just not meant to be, it seems."

Ry sad "If I had to identify the moment life started going downhill, losing Amelia would be it."

Ry "My heart was ripped out in that moment, and now only emptiness remains. It's like a wound that never closes."

Ry shy "Maybe you saw those pictures in my apartment." 

Ry "Even my home is a reminder of her. We were going to move in to that apartment together."

Ry "And this tie I'm wearing? I got it from her as well."

Ry "When she gave it to me, she said that it was red like her scales. As long as I wore it, she would be with me, in a way."

Ry sad "For so long, I've been holding on to her with all my might. I wish I could stop, because I know it's killing me, but I've been doing it for so long that I don't think I can."

Ry shy "Yet in some way, holding on to Amelia has helped me. When I look back on all the happy memories we made, Emera's bullying hurts a little less, if only because those memories hurt so much more."

Ry sad "And I would love my job if it wasn't for Emera."

Ry "It's a constant struggle - a battle I have to fight every day. Each of her words slices through me, creating new wounds on top of others that never closed."

Ry shy "Some days, I just don't want to do it anymore. I don't know how much longer I can."

show remysad at Pan ((0, 326), (580, 0), 12.0) with fade

$ renpy.pause (10.0)

hide remysad with fade

label remy3skip1:

Ry "I'm not sure if there is anything that can fill the void."

if persistent.endingsseen > 0:

    if persistent.playedadine2 == True:
        
        label remy2goodendingmenu:
        
        if persistent.chapter2libraryvisited == True:

            if adinestatus == "bad":
                
                pass
                
            else:
                
                if persistent.varasaved == True:
                    
                    $ remy3choiceyes = True
                    
    elif persistent.remy2picturesseen == True:

        jump remy2goodendingmenu
                    
if remy3choiceyes == True:                    
                    
    menu:
        
        "Have you ever talked to a professional about this?":
            
            jump c3remotherwise

            
        "I remember you said that you always wanted children. {image=image/ui/status/c2pictures.png}{image=image/ui/status/varasaved3.png}":
            
            $ renpy.pause (0.5)

            Ry look "Yes."

            c "It's not exactly the same thing, but I heard that the orphanage is always looking for more volunteers."

            c "You could help take care of those children."

            Ry shy "Is that so?"

            c "Yeah. The orphanage is notoriously understaffed. The children don't really have anyone else, so each volunteer is a godsend."

            Ry "Losing both parents at such a young age must be horrible. I can't even imagine what that must be like."

            c "You should talk to Adine about volunteering. She knows a lot more about it than I do."

            Ry look "Adine?"

            Ry sad "I don't want to talk to her."

            c "Why not?"

            Ry "She used to be my friend. Well, she was more Amelia's friend than mine."

            c "Why can't you talk to her?"

            Ry shy "I don't know. I don't want to face her. Whenever I see her, it's another reminder of what I lost. Besides, I don't think she wants to talk to me, either."

            c "I think if you wanted to volunteer, she'd gladly accept the help."

            c "Besides, I saw that she tried to talk to you the other day."

            Ry "You saw that?"

            Ry sad "I guess she did try to talk to me, but it was only because she wanted something."

            c "I don't think that was the only reason. Maybe she wanted to reconnect with you."

            c "If she wanted to avoid you, she could have asked someone else at the library for help, but she chose you."

            Ry "I'm not sure about that."

            c "Maybe she actually feels the same way you do, and the map helped her muster up the courage to face you again."

            c "If you want to change something, Remy, you have to take action. What's the worst that could happen if you talk to her?"

            Ry shy "I suppose you have a point. I'll... I'll think about it."

            $ remygoodending = True



else:
    
    label remy3ow:
    
    c "Have you ever spoken to a professional about this?"
    
    label c3remotherwise:

    Ry "No, I don't think I could. Not with a stranger."


Ry "Thank you, [player_name]. Getting all that off my chest already helped a lot."

c "No problem, Remy."

if persistent.playedanna1 == True:

    if annasurvives == True:
    
        c "Anything else on your mind?"

        Ry look "Well, there's the whole thing about Anna."

        c "Yeah, you mentioned that last time. Are you still worried about her?"

        Ry "I am. Who knows what horrible things she's working on in her lab? There's nothing I can do to stop her."

        c "You did what you could. The rest is up to the authorities now."

        Ry "I guess so."

        Ry "I can't help but feel a little pity for her, too."

        Ry "With her condition... I imagine that the ministry's disapproval must have been a tough pill to swallow."

        c "What are you talking about?"

        Ry "She has cancer."

        c "I see."

        Ry "Who knows how much longer she has? Knowing that, every day must be difficult for her."
        
        if persistent.heardaboutcancer == False:
            
            if persistent.heardaboutcancerenvelope == False:
                
                $ renpy.pause (0.3)
            
                play sound "fx/system.wav"
            
                s "You learned about Anna's cancer. {image=image/ui/status/heardaboutcancer.png}"

                $ renpy.pause (0.3)

        $ persistent.heardaboutcancer = True

        $ persistent.heardaboutcancerremy = True
        
        show remy shy with dissolve
        
        
    else:
        
        c "Anything else on your mind?"

        Ry look "Well, there was the whole thing about Anna."

        c "Yeah, you mentioned that last time. Are you still worried about what she was working on?"

        Ry "Not as much. I guess whatever she was doing is over now, but who knows what went on in her lab? I imagine we'll hear all about it once the police search it and her apartment."

        c "I guess there's not much use thinking about it, especially now that she's out of the picture."

        Ry "In the end, I can't help but feel a little sorry for her, too."

        Ry "With her condition... I imagine that the ministry's disapproval must have been a tough pill to swallow."

        c "What are you talking about?"

        Ry "She had cancer."

        c "I see."

        Ry "That kind of diagnosis would drive some people crazy. Maybe that's what it did to her."

        Ry "Having to live with that knowledge must have been difficult."
        
        if persistent.heardaboutcancer == False:
            
            if persistent.heardaboutcancerenvelope == False:
                
                $ renpy.pause (0.3)
            
                play sound "fx/system.wav"
            
                s "You heard about Anna's cancer. {image=image/ui/status/heardaboutcancer.png}"

                $ renpy.pause (0.3)
        
        $ persistent.heardaboutcancer = True

        $ persistent.heardaboutcancerremy = True

        show remy shy with dissolve
                
        
else:
    
    pass

m "Remy paused and gave me an embarrassed smile."

Ry "Quite a bit of time has passed since you arrived, and you've barely been able to speak. I've been talking a lot."

#insert skip2 here

if persistent.remy3skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_95

    call skiptut from _call_skiptut_25
        
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
            call skipcheck from _call_skipcheck_25
            
            scene park2

            show remy normal
            with dissolvemed
            
            play music "mx/gravity.ogg" fadein 2.0
            
            jump remy3skip2
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/gravity.ogg" fadein 2.0

c "I don't mind."

Ry "There must be a lot on your mind too."

menu:

    "Not really.":
        
        $ remy3mood -= 1

    "There is.":
        
        pass
        

Ry "Since I work with Emera, I know all the details surrounding you and Reza. Not many do."

Ry look "Many rumors are going around town."

Ry shy "All this time, you've been working with our police?"

c "Yeah."

Ry "And now you're hunting the person who was supposed to be your partner. That must be really hard for you."

c "I came here because I wanted to do the right thing. Nothing about that has changed."

Ry look "What kind of person is Reza, anyway?"

c "The kind that stops at nothing to achieve what he believes in."

Ry "I can see that. We've already witnessed just how far he will go."

Ry "What do you think about him?"

c "Honestly, I'm not sure. Back home, this relentless quality of his was admired, but I certainly don't condone his actions. Given what I know about him, I think he must have a reason, as weird and twisted as it may be."

Ry shy "And what about you?"

c "I have my own principles."

Ry "I see."

Ry "How is your hunt for Reza going, anyway?"

c "Not too great. We don't have any strong leads or any idea of his whereabouts. In the end, we're just following his trail of murder and destruction."

Ry "People are getting afraid. The rumors are starting to take effect."

c "I thought Emera was going to give a press conference to warn the public."

Ry "That didn't happen. She feared the potential backlash if people knew about Reza while you were still here, so - for the time being - he has been declared as a missing person."

Ry "The public has been informed that if someone sees him, they are to call the police immediately. They were told he may be suffering from an affliction that makes him behave erratically."

Ry "But some people are putting two and two together. No one has seen Reza for a while, even before he was officially declared missing." 

Ry "It's easy to line up the timelines and see that the murders started happening shortly after he vanished." 

Ry "What we know about the break-ins and thefts is also damning. The objects stolen all point toward Reza. I'm not sure how much longer they can keep this a secret."

c "How do you think the public will react, considering that I am still staying here?"

Ry "I don't know. We can't really predict the public opinion, but you can bet there will be critical voices."

c "I'm not sure how I could convince everyone that I'm not involved with Reza's plans."

Ry normal "Well, you do have the council's support. If Emera voiced that you were on our side, it wouldn't be so bad if the public found out."

c "Yeah, but she also made it clear that she believes most people won't have the same opinion. She won't support me publically if their vote is against me."

Ry look "That is true. Emera plays the political game a lot. She aligns with the popular opinion so people will like her."

menu:
    
    "That's a good tactic.":
        
        Ry "If you're playing that game, I guess so."

        $ mp.politicians = "tactic"
        $ mp.save()
    
        $ remy3mood -= 1
        
    "That's very dishonest.":

        $ mp.politicians = "dishonest"
        $ mp.save()
        
        Ry "It is, but that's who she is."
        
        $ remy3mood += 1
    
    "I can't blame her for that.":

        $ mp.politicians = "noblame"
        $ mp.save()
        
        c "I can't really blame her for that. After all, she's supposed to be a representative of the people, right?"

        Ry "I suppose so."
    
    
c "Does the public know about the portal's current state?"

Ry normal "No. If it can be fixed, it wouldn't be worth mentioning - and if they can't fix it, they aren't going to announce it before they know how to deal with the current situation."

Ry look "Compared to Reza, it's not really a problem."

c "It might become one pretty soon. If word gets out and I'm suddenly his accomplice, what would happen to me?"

c "How would you even deal with Reza if you caught him?"

Ry normal "I'm not sure. I suppose we would have to work something out between our legal system and whatever humanity has to say on the matter."

c "And if the portal is done for? What then?"

Ry "Then humanity would be out of the picture for any legal proceedings."

Ry "Reza would likely be held until contact has been re-established or just serve his sentence here."

c "I see. How do your jails work, anyway?"

Ry "Well, if a crime has been committed and proven without a doubt, a jail sentence can be the consequence."

Ry "Our delinquents live in an area separate from the rest of society, monitored at all hours of the day." 

Ry "They receive the help they need, and efforts are taken to make them realize their wrongdoings and integrate them back into our community."

Ry "Life isn't that much different there than it is here. The spaces are more cramped, for sure, but mostly it is just a very controlled environment."

c "That's not much of a punishment."

Ry "It is a consequence, not necessarily a punishment. Our society at large benefits more from people who are rehabilitated, and if mental issues are the cause, those can at least be found and addressed."

c "That sounds like how it used to be back home. These days, in our city, you get three strikes."

Ry "What does that mean?"

c "Three infractions of our rules and you get thrown out of the city. If someone is a drain on our limited resources, we won't support them."

Ry "While I can understand why you needed to incorporate such a policy, the finality of it makes me a bit uneasy."

c "It has worked so far. And it's not as if the outside is completely unkind."

c "Someone expelled from the city might find a different community, or join one of the mobile groups. The situation inside our city-state is still much better than the outside, though. They're very strict with those allowed to live there."

c "It is a privilege. Anyone or anything that threatens the inside society or the lives of its people is removed very quickly."

Ry "How would a murderer like Reza be dealt with? An eye for an eye?"

c "No, we don't do that, but murder is a crime so heinous that immediate expellation is the consequence - regardless of prior infractions."

Ry "I see. What do the citizens think about this system?"

c "Some agree with the methods, some don't - but as long as it works, people won't complain. Weeding out undesirable elements is what keeps their standard of living intact."

Ry "I guess that means politics don't play a big role where you come from."

c "No. They won't change a working system."

Ry look "It varies here, but I'm so tired of Emera and her games. As I work with her, I can see exactly how she plays the public." 

Ry "I know every council member has their own approach, but everything she does is so... tailored towards the public's expectations. For her it's just a popularity contest."

c "You know what? That gives me an idea."

Ry normal "Really? What is it?"

c "The human visit and all of the associated consequences are her responsibility, right?"

Ry "Yes."

c "For her, this situation with Reza must be utterly horrifying. She keeps talking about preventing public backlash, but she's really just trying to protect herself."

Ry "That sounds accurate."

c "Maybe we can use that to our advantage."

Ry "How?"

c "She can't send me back to my world right now. That makes me the only one here with knowledge of Reza, and humans in general."

Ry "That's true."

c "If I speak from this point of authority, we should have a much easier time convincing her of anything we want."

Ry "You couldn't convince her to let you stay in our world, though."

c "Yes, but I was trying to use reason and plead with her. I didn't take into account her fear of public backlash." 

c "I think we can manipulate this fear of hers and use it to our advantage. If there were consequences to fear from Reza, me, or the rest of humanity - and those consequences would make her look bad to the public - that would be reason for her to reconsider any action, right?"

Ry "I suppose so, but what situation could this apply to?"

c "She nearly sent me back through the portal. If she tries anything again, at least we have something we can use against her."

Ry "I think I see where you're coming from."

Ry "Reza is still a mystery to me, though. All things considered, wouldn't it be beneficial for him to just stay here? No offense, but even our prisons offer a better standard of living than your city."

Ry "As such, couldn't that be a reason for him to have vandalized the portal?"

c "I don't think so. You're right, your world is in much better shape than ours, but even if Reza could stay here, he wouldn't. He came here for the same reason I did - to help our people." 

c "He has a very pronounced sense of duty to humanity, and I believed in him when he stepped through the portal. He proclaimed that he would do everything he could." 

c "When I met him again in this world, I had the impression that he wanted to get our mission over with as soon as possible so he could return to our world with aid."

Ry "That's going to be difficult with the portal out of order."

c "The person who did it probably didn't realize it wasn't a very good idea. This might make Reza even more desperate. Who knows what he will do next?"

c "And if anything happens, I can't leave either."

Ry "If the portal is gone for good, I suppose you'd have to stay here. What do you think about that?"

menu:
    
    "That wouldn't be so bad.":
        
        c "That wouldn't be so bad. Of course I still want to help our city, but if there was no way to return, I wouldn't mind living here."

        Ry "I see."
        
        $ mp.liveindragonworld = "neutral"
        $ mp.save()

        show remy shy with dissolve
        
    "I'd love living here.":
        
        c "I'd love living here. Everything I've heard about this place is so wonderful compared to back home."

        Ry smile "That's good to hear. I certainly wouldn't mind if you stuck around."

        $ mp.liveindragonworld = "yes"
        $ mp.save()
    
        $ remy3mood += 1
        
        show remy shy with dissolve
    
    "That'd be a shame.":

        $ mp.liveindragonworld = "no"
        $ mp.save()
        
        Ry "Why's that?"

        c "I came here to help our city-state. My mission would obviously be a failure, and the people back home would never even know what happened to me."

        Ry shy "I suppose I understand."
        
        $ remy3mood -= 1

Ry "..."
    
Ry "Only now do I realize that everything I told you earlier must seem so petty compared to the struggles you face."


menu:
    
    "You're right.":
        
        Ry "I'm sorry, [player_name]."

        c "Don't be. Maybe once you realize how privileged you are to live here, you'll start to appreciate the small things again."
        
        show remy normal with dissolve
        
        $ remy3mood -= 1
        
    "Don't say that.":
        
        $ renpy.pause (0.5)
        
        Ry normal "Why not?"

        c "That's not how it works. That's like saying a person can't be happy, because someone else might be happier than them. Don't downplay your own suffering like that. That kind of thinking only makes it worse."
        
        Ry "Thanks, [player_name]."

        $ remy3mood += 1

    "We all have our own struggles.":
        
        $ renpy.pause (0.5)

        Ry normal "I suppose that's true."


Ry "I can't even imagine what life must be like where you are from."

c "Back home, I was just trying to survive and help others do the same. That hasn't changed. I'm almost afraid of going back to the city, though. Times are so rough."

c "Yet even if I didn't have to go back, I would. I can't just let them down like that, you know? I have to try and do what I can. That's why I came here."

Ry "I wish I could be that strong."

menu:
    
    "Who says you can't?" :
        
        $ renpy.pause (0.5)
        
        Ry shy "I don't know... I just..."
    
    "You aren't. Deal with it.":
    
        $ renpy.pause (0.5)

        Ry shy "..."

        $ remy3mood -= 1

    "What does it matter?":

        c "What does it matter if you aren't as strong? If people only did what they were the absolute best at, they wouldn't be doing much at all."

        Ry shy "That's a good point."


c "You told me about your old job."

Ry "Yeah. I miss those days. What about it?"

c "It's not exactly the same as saving a city, but you were helping people, right?"

Ry normal "That's true."

c "Maybe, once your term with Emera is over, you could do something like that again."

Ry "I really wish I could."

c "..."

Ry "..."

if remy3mood <= 1:
    
    Ry shy "I just realized something."

    c "What is it?"

    Ry "I was trying to figure out why you wanted to hang out with me so often."
    
    c "What are you talking about?"

    Ry "Since Amelia died, I've been alone. It's been years. I don't even have anyone I could consider a friend."
    
    Ry "When you came to our world and started to spend time with me, I thought maybe things were about to change. That, maybe, I'd found a friend."
    
    Ry sad "But you're not that different. You make fun of me and belittle me just like everyone else. Even after everything I told you about myself. You don't care about me, do you?" 
    
    Ry "If I was just your entertainment, that's alright. That's what people do to me. They watch and laugh, in secret or otherwise."

    Ry "I'm beginning to realize that maybe it's not their fault. Maybe it's me."
    
    Ry "Goodbye, [player_name]."

    $ remygoodending = False
    
    hide remy with dissolve
    
    stop music fadeout 2.0
    
    $ renpy.pause (0.5)
    
    $ remystatus = "bad"
    
    $ remyscenesfinished = 3
    
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
    
else:

    label remy3skip2:
    
    Ry shy "Can I ask you a question?"

    c "Of course."

    Ry "Do you even like me? There must be a reason why you've put up with me for this long."

    c "What are you talking about?" 

    Ry "Do you consider me a friend, or maybe more?"
    
    menu:
        
        "I like you as a friend.":
            
            $ renpy.pause (0.5)
            
            Ry smile "That makes me really happy to hear. I haven't had a friend in a very long time."

            Ry normal "I think I should get going now. Thanks for hearing me out, [player_name]."

            c "Likewise."

            hide remy with dissolve
    
            stop music fadeout 2.0
            
            $ renpy.pause (0.5)
            
            $ remystatus = "neutral"
            
            $ remyscenesfinished = 3
            
            $ persistent.remy3skip = True
            
            if chapter4unplayed == False:
                            
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars


        "I like you as more than just a friend.":
            
            Ry "Is that so?"

            Ry "In that case... Well..."

            Ry "Th-the summer festival is coming soon. It's an event we hold in town every year."

            Ry normal "They've got fireworks and all kinds of shows."

            Ry smile "It might be fun for you to experience a different part of our culture."

            Ry normal "What do you say? Would you like to accompany me?"

            c "I'd love to, but I can't promise I won't have other obligations at the time."

            Ry "I see." 

            Ry "Well, I'll call you and we'll see if we can work it out around our schedules."
            
            c "Sure thing."

            Ry "Then it's settled."

            Ry smile "I probably should get going now, though. Thanks for hearing me out, [player_name]."

            c "Likewise."

            hide remy with dissolve
    
            stop music fadeout 2.0
            
            $ renpy.pause (0.5)
            
            $ remystatus = "good"
            
            $ remyscenesfinished = 3
            
            $ persistent.remy3skip = True
            
            if chapter4unplayed == False:
                            
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars
                

        "Don't read too much into our meetings.":
            
            $ renpy.pause (0.5)
            
            Ry sad "Oh, I see. Just forget I said anything. And by that, I mean everything I've ever said to you."

            Ry "I'm sorry I didn't realize it sooner."

            Ry "What am I to you, then? Just a specimen to study? Just someone who provides you with entertainment?"
            
            Ry "You know what? It doesn't matter."

            Ry "Thanks for being honest, at least."

            Ry "Goodbye, [player_name]."

            hide remy with dissolve
    
            stop music fadeout 2.0
            
            $ renpy.pause (0.5)
            
            $ remystatus = "bad"
            
            $ remyscenesfinished = 3
            
            
            if chapter4unplayed == False:
                            
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars

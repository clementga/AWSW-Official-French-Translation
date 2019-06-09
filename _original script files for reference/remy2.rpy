#-12+13

label remy2:

#$ chapter2csplayed += 1
$ remy2unplayed = False
$ remy2mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Remy 2"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Remy 2"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Remy 2"
    
else:

    $ save_name = "Chapter 1 - Remy 2"

scene black with fade
$ renpy.pause (1.0)
scene remyapt at Pan ((300, 80), (0,80), 5.0) with dissolveslow

$ renpy.pause (3.3)

#insert skip here

if persistent.remy2skip == True:
    
    if persistent.remy2picturesseen == True:
    
        stop music fadeout 1.0

        $ renpy.pause (0.3)

        play sound "fx/system3.wav"

        call syscheck from _call_syscheck_113

        call skiptut from _call_skiptut_34
        
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
                call skipcheck from _call_skipcheck_34
                
                scene remyapt at Pan ((0, 80), (0,80), 0.0)

                show remy shy
                with dissolvemed
                
                play music "mx/soul.ogg" fadein 2.0
                
                jump remy2skip
            
            "No. Don't skip ahead.":

                play sound "fx/system3.wav"
            
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

                #play music "mx/soul.ogg" fadein 2.0

    else:
        
        pass
        


show remy normal with dissolve

play music "mx/soul.ogg" fadein 2.0

if remyapologized == False:

    Ry "Thank you again for helping me the other day. Without you, I would have been trapped sorting books for a few more hours. Inviting you over for dinner is the least I can do."
       
    menu:
        
        "It's no problem, really.":

            c "It's no problem, really. Besides, I'm also here to learn more about your kind. Spending some time in the library is only appropriate."

            Ry smile "Well, my gratitude is yours regardless."

            show remy normal with dissolve

            $ remy2mood += 1

            
        "It really is.":

            c "It really is. Sorting that stuff wasn't easy. I definitely deserve something for all my hard work."

            Ry "Well, hopefully you'll find that your dinner more than makes up for it."


        "There's something else you could do for me...":

            c "You know, there's something else in particular you could do for me..."

            Ry shy "Wh- What are you talking about?"

            show remy normal with dissolve

            $ remy2mood -= 1


        "Potato.":

            Ry "I think I have a few potatoes, but potatoes alone don't make for a particularly good dinner. Maybe we can find something else to go with them."

else:
    
    c "Thanks for having me."
    
    Ry "I'm sure you are very busy as ambassador, so thank you for taking the time. I say we let bygones be bygones and hope that today will be different."
    
    c "Sure."

Ry "Anyways, is there anything in particular you would like to eat?"

menu:
    
    "Anything will do.":
        
        $ renpy.pause (0.5)

        Ry smile "I happen to have some nice steaks left. How does that sound?"

        $ mp.vegetarian = False
        $ mp.save()
        
        show remy normal with dissolve
        

    "How about steak?":

        Ry "Oh, you're in luck. I do have a few steaks we could dine upon."

        $ mp.vegetarian = False
        $ mp.save()


    "I could go for some \"meat\" right now...":

        c "I could go for some \"meat\" right now... if you know what I mean."

        Ry smile "Of course! I have a few steaks left."

        show remy normal with dissolve

        $ remy2mood -= 1

        $ mp.vegetarian = False
        $ mp.save()
        
        
    "Do you have something vegetarian?":
        
        Ry "Interesting you say that. Are all humans vegetarians, or is that just you?"
        
        c "Only some humans are vegetarian."
        
        Ry "I see. Luckily for you, I didn't want to assume anything, so I got us some meat-free steaks for the occasion."
        
        $ nomeat = True


Ry "This might take a while, so make yourself at home."

hide remy with dissolve

m "With those words, Remy walked into the partially walled-off kitchen. There was no door, so I saw him open the fridge and take out two steaks before he set them on the counter." 

m "Soon after, he was already preparing the various ingredients with his somewhat clumsy paws." 

play sound "fx/veggies.ogg"

m "He was silent for a moment, then lifted his snout and looked at me from over the partition."

c "What is it?"

Ry "Ah, I was just thinking about something..."

c "I could help cook, if you like."

Ry "Don't worry about it."

c "Alright."

m "I looked around the apartment as Remy cooked and couldn't help but notice the almost mesmerizing tidiness that permeated the place. Shelves were filled with books, scrolls, magazines and other various trinkets."

stop sound fadeout 1.0

m "Suddenly, the repetitious noise of vegetables being cut ceased as Remy returned from the adjoining room."

show remy normal with dissolve

Ry "I'll be back in just a minute."

hide remy with dissolve

play sound "fx/door/door_close.ogg"
queue sound "fx/door/lock.ogg"

m "He went down the hall and vanished through the bathroom door."

c "(What should I do?)"

$ remy2options = 0
$ remy2shelves = True
$ remy2shelves2 = False
$ remy2bath = True
$ remy2pictures = True
$ remy2pictures2 = False
$ remy2picturesn = 0
$ remy2bed = True
$ remy2wait = True

label remy2menu:
    
if remy2options == 3:
    
    jump remy2cont
    
else:
    
    menu:

        "Examine the shelves." if remy2shelves:
            
            m "I moved over to the shelves and idly looked through the books and scrolls. Nothing particularly interesting caught my eye."

            m "From the titles alone, it seemed all genres were more or less represented - fiction and non-fiction alike. the scrolls were neatly sorted in holders, though I couldn't make out the logical consistency behind their arrangement."

            c "(Anatomy, huh? Let's check that out.)"

            play sound "fx/undress.ogg"

            show scroll with fadehold
            
            $ renpy.pause (2.0)

            c "(I'm not quite sure what I expected.)"
            
            hide scroll with fade
            
            $ remy2options +=1
            
            $ remy2shelves = False

            $ rempy2shelves2 = True
            
            jump remy2menu
            

        "Go into the bathroom." if remy2bath:

            c "(Wait a minute, he has a second bathroom? I wonder why.)"
            
            $ remy2options +=1
            
            $ remy2bath = False
            
            jump remy2menu
            

        "Look at the pictures." if remy2pictures:
            
            if remy2picturesn == 0:

                m "I picked up one of the framed photos to examine it more closely. It was a red dragon. I guessed that it was a female of young adult or college age, though I wasn't sure, as it was still hard to tell without looking at the obvious signs." 
                
                m "Her crimson scaled head was adorned with frills that ran down the back of her neck. She wasn't familiar to me."

                $ remy2options +=1
                
                $ remy2picturesn += 1
                
                jump remy2menu

                
            elif remy2picturesn == 1:

                m "The second picture showed Remy in his typical attire - tie, glasses and all."

                $ remy2options +=1

                $ remy2picturesn += 1
                
                jump remy2menu
                
            else:

                m "The last of the three pictures was of another red dragon, who - as far as I could tell - was a fairly young member of its species. It reminded me of a younger version of Remy, although without his typical accessoires."
                
                $ remy2pictures = False

                $ remy2pictures2 = True
                
                $ remy2options +=1

                if persistent.c2pictures == False:

                    $ persistent.c2pictures = True
                    
                    $ achievement.grant("Memories")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_114
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You looked at Remy's pictures! {image=image/ui/status/c2pictures.png}"
                        
                    elif system == "advanced":

                        s "You looked at Remy's pictures. Creep.{image=image/ui/status/c2pictures.png}"
                        
                    else:
                        
                        s "You looked at Remy's pictures. Better than prying into his bedroom, at least.{image=image/ui/status/c2pictures.png}"
                
                jump remy2menu
            

        "Search his bedroom." if remy2bed:

            c "(I probably shouldn't be looking in here, but I'll just take a quick peek.)"
            
            play sound "fx/door/door_open.wav"
            
            $ renpy.pause (1.5)

            c "(Now that's a huge bed, even for a dragon. I suppose they need to account for wings and such, but even considering that, it's pretty big.)"
            
            $ remy2options +=1
            
            $ remy2bed = False
            
            jump remy2menu
            

        "Wait.":
            
            m "I decided to pass the time by humming the theme of a game show."

            c "(Looks like Remy still isn't back.)"
            
            $ remy2options +=1
            
            jump remy2menu
            

        "Escape while I still can.":
            
            m "My choice was an easy one. I had to get out of here. In order to avoid an awkward goodbye, I hurried to leave before he had a chance to come back."

            $ remystatus = "bad"
            
            $ remyscenesfinished = 2
        
            stop music fadeout 2.0

            if chapter4unplayed == False:
            
                jump chapter4chars
                
            elif chapter3unplayed == False:
                
                jump chapter3chars
                
            elif chapter2unplayed == False:
                
                jump chapter2chars
                
            else:

                jump chapter1chars

        
label remy2cont:

play sound "fx/door/lock.ogg"
queue sound "fx/door/door_open.wav"

$ renpy.pause (2.0)

show remy normal with dissolve

#oldskip


m "The bathroom door opened and revealed the white dragon. As he approached, I felt my stomach grumble quietly." 

play sound "fx/rumble.ogg"

m "I barely heard the muffled sound, but when I saw Remy's ears perk, I realized he had more sensitive ears than I expected."

Ry smile "Hungry already, I take it?"

menu:
    
    "I suppose so...":

        Ry "Although, your stomach already answered that question for you."

        $ remy2mood += 1


    "I'll starve if you keep standing around.":
        
        $ renpy.pause (0.5)

        Ry look "Sorry, I'll get back to cooking."

        $ remy2mood -= 1


    "I'm so empty.":
        
        $ renpy.pause (0.5)

        Ry shy "Well, I'll give you something to fill your belly with soon."


    "[[Lift your shirt]":

        m "I pulled up my shirt and exposed my belly to the dragon's gaze. My hands stroked it in a circular motion, caressing the skin, hair and body fat beneath."

        show remy look with dissolve

        c "Do you think that's a lot of hair? Or just a little peach fuzz?"
        Ry "..."
        c "Because I think it is pretty hairy."
        Ry "..."
        c "Some of the hair is actually blond, so you might not be able to tell from a distance..." 
        Ry "..."
        c "Which means you have to touch my belly to feel them."
        Ry "..."
        c "It's very soft."
        Ry "..."
        c "..."
        Ry "..."
        Ry "I'm afraid you need to leave."
        c "..."
        Ry "..."
        Ry "Now."

        stop music fadeout 2.0

        scene black with dissolveslow
        
        $ renpy.pause (0.5)

        m "He shooed me out of his apartment after that, and not wanting to make a scene, I left. I'm still not sure what exactly went wrong that evening, but somehow I didn't think he would want to meet with me again."

        $ remystatus = "bad"
        
        $ remyscenesfinished = 2
        
        if chapter4unplayed == False:
        
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars


hide remy with dissolve

#m "Once again, he entered the kitchen."

m "After entering the kitchen once more, I saw the dragon looked over the kitchen partition again. His mouth opened a little, as though he were going to speak, but his brow scrunched with hesitation."

m "Before I could say anything, he shook his head and continued to cook."

play sound "fx/fry.ogg" fadein 1.0

if nomeat == False:
    
    m "Soon, I heard the sizzling of frying meat as the delicious smell of steak wafted into the room."
    
else:
    
    m "Soon, I heard the sizzling of the frying steaks as their delicious smell wafted into the room."

m "Fueled by its fragrant odor, I slowly lost myself to daydreams as I closed my eyes."

show black with dissolvemed

$ renpy.pause (1.0)

hide black 
show remy normal
with dissolvemed

Ry "Is something wrong? You are salivating."

c "I-It's nothing. I was just thinking about something."

Ry smile "Well, the food is ready. Enjoy."

show remy normal with dissolve

m "I looked down and saw that a plate was already in front of me, piled with steak and vegetables. Remy was already eating, so I took the knife he had provided and cut off a small corner of my steak." 

m "Then, I pierced it with the fork, its three prongs penetrating the flesh unrelentingly. Slowly, I raised it to my mouth, and my tongue glided over the bare substance briefly as it entered my lips." 

m "I took the first bite. A delicately crisp exterior, with a much softer and juicy inside. It melted on my tongue like butter as the taste spread to even the remotest corner of my mouth."

m "It was almost perfect." 

Ry "So, what were you thinking about?"

c "Huh?"

m "Remy's words snapped me back to reality."

Ry "You said you were thinking about something."

$ remy2yourself = True
$ remy2murders = True
$ remy2fire = True

label remy2menu2:
    

menu:
    
    "I looked at some of your scrolls." if remy2shelves2:

        Ry "Which ones?"

        c "The ones on anatomy."

        Ry shy "W-Well, I do have a variety of books and scrolls covering all kinds of different subjects."

        c "I saw as much. You may have heard that I have a degree in biology, which is one of the reasons I was given the honor of coming here in the first place. As such, your anatomy is of high interest to me and one of the things I'm supposed to study."

        Ry "M-My anatomy?"

        c "I was talking about your kind in general, not you in particular..."

        Ry "Oh? In that case, I might be able to find you something more comprehensive than a handful of scrolls."

        c "I would greatly appreciate that. Thank you!"
        
        show remy normal with dissolve
        
        $ remy2shelves2 = False
        
        jump remy2menu2


    "Do you live here by yourself?" if remy2yourself:
        
        $ remy2yourself = False

        Ry "I do. Honestly, you are the first person to visit in a while."
        
        m "He spoke softly, and his gaze wandered."
        
        if persistent.c2pictures == True:
            jump remy2picturesmenu

        if remy2pictures2 == True:

            label remy2picturesmenu:
            
            menu:
                
                "Mention the pictures. {image=image/ui/status/c2pictures.png}":
                    
                    c "Really? I saw those pictures on the coffee table. I thought you might have a family."

                    Ry "Oh, no. That's in the past. I'm not even sure why those photos are still there."

                    Ry "And I don't actually have children. The picture of the young dragon was the product of a silly little program that combined photos. They'd take images of two people and create what the pair's offspring would supposedly look like."

                    Ry "I've always wanted some children of my own, though."

                    c "I see."

                    Ry "How about you, [player_name]? Would you like to have children one day?"

                    $ persistent.remy2picturesseen = True

                    menu:
                        
                        "Yes.":

                            c "I think I would."

                            Ry "Just being able to teach them about the world and watch them grow up... Having a little family would be nice. I'd like that a lot."

                            $ mp.wantchildren = "yes"
                            $ mp.save()


                        "No.":

                            c "I don't think that's something for me."

                            Ry "There's nothing wrong with that. It's not for everyone. It must require a lot of hard work."

                            $ mp.wantchildren = "no"
                            $ mp.save()


                        "I'm not sure.":

                            c "I'm not sure."

                            Ry "Why is that?"

                            c "I just don't know if it's good time to bring a child into the world. I guess I'm not sure if I could be a good parent."

                            Ry "You should give yourself some credit. I often see parents that don't seem to be as aware about the whole situation as you are and as a result have children they don't properly care for. Being conscious about it already makes you a better parent than them."

                            $ mp.wantchildren = "unsure"
                            $ mp.save()

            
                "Don't say anything.":
                    
                    pass
            
        else:
                 
            c "Oh, I see. Thank you again for inviting me."

        $ remy2yourself = False




        jump remy2menu2


    "I was thinking about those recent murders." if remy2murders:

        Ry "Oh, what a terrible thing. People can be so cruel sometimes."

        c "They can be. Where I come from, incidences like this are unfortunately fairly common."

        Ry "Truly? Here, it is almost unnheard of. One just needs to take a look at the statistics to realize that this is very unusual. Or just an exceptionally bad week.."

        $ remy2murders = False

        jump remy2menu2


    "I met Emera recently." if chap2emmeet2:
        
        Ry "You met my boss?"

        c "She was hanging around Tatsu Park."

        Ry "She certainly does that a lot."

        Ry "Let me give you one piece of advice: Don't ever work for a politician."

        $ chap2emmeet2 = False
        
        jump remy2menu2


    "Why did you use a stove to cook?" if remy2fire:

        c "Why did you use a stove to cook? I mean, can't you just use your fire?"

        Ry "Well, for one, not all of us have that ability. Besides, we still appreciate the convenience that comes with appliances like this one, and not everyone wants to eat food cooked with someone else's breath."

        Ry "Breathing fire indoors is also a little unsafe."

        c "I see. That makes a lot of sense."

        $ remy2fire = False

        jump remy2menu2


    "Nothing in particular.":
        
        pass

if persistent.remy2skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_115

    call skiptut from _call_skiptut_35
    
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
            call skipcheck from _call_skipcheck_35
            
            scene remyapt at Pan ((0, 80), (0,80), 0.0)

            show remy shy
            with dissolvemed
            
            play music "mx/soul.ogg" fadein 2.0
            
            jump remy2skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/soul.ogg" fadein 2.0


Ry "Anyways, how do you like the food?"

menu:
    
    "It is adequate.":

        c "It is adequately providing sustenance for my body. My hunger is lessening."

        Ry "I suppose that is a compliment. After all, that is what dinner is for."


    "It is delicious.":
        
        $ renpy.pause (0.5)

        Ry smile "Thank you. I suppose you learn to cook well when you live on your own long enough."

        $ remy2mood += 1
        
        show remy normal with dissolve


    "I would marry this steak if I could.":

        Ry "Seeing how it is already half gone, I don't think this marriage would last particularly long."
        
        
if anna1unplayed == False:
    
    menu:
        
        "Mention that you saw him with Anna.":
            
            c "By the way, I noticed you went to see Anna the other day. What was that all about?"

            Ry look "How do you know about that?"

            c "I saw you two together a little before you left the building."

            Ry normal "That's kind of a long story. Why were you at the facility in the first place?"
            
            c "She said I could come by. Apparently, she wants to run some tests on me."

            Ry look "Oh, that is so typical of her."

            Ry "Let me tell you something: That woman is trouble. Big trouble."

            Ry "A few years ago, she was discovered performing unapproved - and therefore illegal - experiments."

            Ry "She had been running them for a while under the assumption that she would be allowed to, but in the end, our council's ethics committee made the decision against her." 

            Ry "Anna's defense was that she did it for the \"greater good\" and that she was confident that her experiments would be approved eventually." 
            
            Ry "She lambasted us for not allowing her research and said our decision was short-sighted and stifling innovation."

            Ry "In the end, no proof of any actual wrongdoing could be found, so she basically got off scot-free." 
            
            Ry normal "Since then, she's remained under the radar. Until now. There are rumors going around about Anna."

            Ry look "Surprise, surprise. Her latest application involves human DNA."

            Ry "Her casual disregard for rules of any kind should tell you what kind of person she is."

            Ry "She does have a brilliant mind, you know, but the way she uses it..."

            Ry sad "She's... manipulative, arrogant, abusive."

            Ry look "I don't think you should trust her."
            
            menu:
                
                "Maybe she isn't as bad as you say.": 

                    Ry "You don't know her. Nor should you bother getting to know her."

                    c "How much do you really know about Anna? Is it your job to go knocking on people's doors, just because you heard some rumors?"

                    Ry shy "I was just trying to help."

                    c "Really? It sounds like all you did was harass her. Without proof of any actual wrongdoing, that's not a particularly good idea."

                    Ry "Well, I..."

                    Ry "Well, if that's what you think, then I just hope you'll at least be careful around her."
                    
                    show remy normal with dissolve

                    $ remy2mood -= 1

                "I agree.":

                    c "I agree. Something seems off about her."
                    
                    show remy normal with dissolve

                    $ remy2mood += 1
                                
            
        "Say nothing.":
            
            pass


else:
    
    pass


m "Soon, both of our plates were picked clean."

Ry smile "I guess I judged your portion correctly. Unless you want more?"

c "I'm good, thanks." 

if nomeat == False:

    c "That was an interesting steak. What kind of meat was that?"

    Ry normal "Those were aurochs steaks. Are you familiar with that animal?"

else:
    
    c "That was interesting. What was that steak made of, anyway?"
    
    Ry normal "I'm not sure, exactly. It's probably some kind of vegetable blend."
    
    c "I see. What kind of meat is commonly eaten around here, anyway?"
    
    Ry "Aurochs meat. Are you familiar with that animal?"


c "I may have heard of aurochsen before."

Ry "They are rather large, bovine mammals characterized by their horns and body shape."

Ry "We get a range of products from them - from meat and milk, to sub-products like butter and cheese, in addition to leather, felt, oils and creams. We even use their horns and bones for a variety of things."

c "That sounds similar to an animal we have back at home. Speaking of unfamiliar creatures, why don't you tell me more about your species?"


Ry "Are you refering to me, or all of us? Our society is comprised of a number of different species, which you have probably noticed by now."

c "I guess all of you. Let's start with the basics."

Ry "I'm sure you're aware, but unlike the mammalian aurochs, we are reptiles."

Ry "Though this makes me wonder about you. Based on your fur, I'd guess that you are a mammal, but you're very different from other mammals we know."

c "In the same vein, you don't share many characteristics with our reptiles back home. And by the way, we don't have \"fur\", but \"hair\"."

Ry "What's the difference?"

menu:
    
    "I don't know.":

        c "Actually, I don't know. Usually, we refer to animals as having fur, whereas humans have hair."

        Ry "Interesting."


    "Fur has a set length, wheras hair will keep growing.":

        c "Fur has a set length it will grow, whereas hair will keep growing, so we regularly cut it."

        Ry "Is that so? Interesting."

        $ remy2mood -= 1


    "Fur is more dense than hair.":

        Ry "Is that so? Interesting."

        $ remy2mood -= 1


    "There is none.":

        c "There actually isn't one. They share the same chemical structure, so the distinction is pretty much arbitrary. I suppose it is just a way to distinguish the same structure in humans from that in non-human animals." 

        Ry "Is that so? Interesting."
            
        $ remy2mood += 1


Ry "I was wondering something. Are you wearing all those coverings to make up for a lack of hair?"

c "I suppose that's one reason why humans wear clothes."

c "They also provide warmth and protection, and are used to differentiate us from one another. Sometimes, uniforms are used as identification. Other times, clothes are just ornamental. What a person wears can tell us something about the person itself."

Ry "That sounds complicated. We also have uniforms and wear some things for ornamental reasons, though our uses aren't quite as extensive."

c "That brings up an interesting question: Are you endo- or exothermic?"

Ry smile "We produce our own body heat."

c "That is unusual. Where I come from, all reptiles are endothermic. Unless you count birds as reptiles, I guess."

Ry normal "But none of your reptiles are sentient, correct? Maybe it has something to do with our different brain structures."

c "Maybe."

Ry "Now that you've been in our world for a while, how do you like it here?"

menu:
    
    "I like the people.":
        
        $ renpy.pause (0.5)

        Ry smile "That is good to hear! Cultural differences can make things very difficult sometimes, even within the same species. I'm glad things are working out for you so far."

        $ remy2mood += 1


    "I like the landscape.":

        Ry "It is pretty, isn't it?"
        
        show remy smile with dissolve


Ry "Oh, I just remembered: I was able to save my game after all. Your interference was only a minor setback."

menu:
    
    "Okay.":
        
        $ remy2mood -= 1


    "Glad to hear it.":

        $ renpy.pause (0.5)

        Ry "I was quite relieved when I found out."

        $ remy2mood += 1


    "Good job, Remy. You're AWESOME.":

        Ry "It turned out it wasn't a big deal after all."


Ry shy "You know, if that hadn't worked out so well, I would have had to consider making you play up to that point again for me."

menu:
    
    "Ain't nobody got time for that.":

        Ry "Haha, yeah. It was just a joke."
        
        show remy normal with dissolve
            
        $ remy2mood -= 1    
            
            
    "Yeah, sure.":
        
        show remy normal with dissolve
        
        
    "I wouldn't mind playing some of your video games.":
        
        $ renpy.pause (0.5)

        Ry normal "Is that so?"

        c "Yeah, they're fun. I'd like to see what kinds of games you have here."

        Ry smile "I'll keep that in mind. Perhaps I can show you sometime."

        show remy normal with dissolve

        $ remy2mood += 1
            
    
Ry "You know, I'm glad you're here. Since you arrived in our world, we haven't really had the chance to just sit down and talk."
    
menu:
    
    "I agree.":

        c "I agree. It's been a busy time for me, as you can imagine."

        Ry smile "Oh, of course. Thanks for taking the time to pay me a visit!"

        Ry normal "I always have so many things to take care of that it's hard for me to find time to do something simple like this."

        c "At least it worked out this time."
         
        $ remy2mood += 1   
    
    
    "I didn't know you wanted to chat.":
        
        $ renpy.pause (0.5)

        Ry shy "It's not as if I was desperate or anything. I just think it's nice."
        
        show remy normal with dissolve
    
    
    "I'm usually not a sit down and talk kinda person.":

        Ry "Oh. Good to know."
    
        $ remy2mood -= 1
    
    
c "You do have a point, though. I don't really know that much about you."

c "I know where you work, but most of our conversations so far have revolved around things other than you and me."

c "Why don't you tell me more about yourself?"

Ry shy "I-I don't really like talking about myself."

c "Why not?"

Ry normal "I guess I wouldn't know what to say. I'm not really that interesting."

c "I don't believe you."

Ry "There's also the uncertainty of not knowing how another person will react to something I say. I don't want to embarrass myself."

c "Hey, at least you told me that. That's something."

Ry "I suppose."

Ry smile "Anyway, now that you've seen my apartment, I'm wondering what your home on the other side of the portal looks like."

c "It's nothing special. Yours is prettier. Actually, everything here looks nice in comparison to back home."

Ry normal "Is that so?"

c "In some ways, I'm not really looking forward to returning, but it's not like I have a choice in the matter."

Ry smile "I suppose you could always visit if you wanted to."

c "It wouldn't be that easy, I'm afraid. There was an extensive process involved for selecting who would go through the portal, and I was only one of many applicants. I'm still surprised that I ended up being chosen."

Ry normal "At least you're here now."

c "Indeed."

c "So, what have you been up to since the last time I saw you?"

Ry smile "You mean since I went into the kitchen to cook the steaks?"    
    
menu:    
    
    "Is that supposed to be a joke?":
         
        $ renpy.pause (0.5)

        Ry shy "It was, but I guess my attempt at humor was ill-advised."

        show remy normal with dissolve
         
        $ remy2mood -= 1   
            
    
    "Very funny.":

        Ry "I'm just messing with you, [player_name]."
        
        show remy normal with dissolve
    
    
    "Yes, that's what I meant.":
        
        $ renpy.pause (0.5)

        Ry normal "Really?"

        c "No."

        Ry smile "Oh, I believed you for a moment. Guess you got me there, [player_name]."
        
        show remy normal with dissolve
            
        $ remy2mood += 1
        
        
Ry "Ah, with all the talking, I totally forgot about dessert."
        
menu:
    
    "You don't have to bother. I'm on a diet.":

        Ry "This won't have an impact on your weight, I can assure you of that."
        
        
    "Would it happen to be a cream pie with a cherry on top?":
        
        $ renpy.pause (0.5)

        Ry shy "N-No, why do you ask?"

        c "No reason."
        
        show remy normal with dissolve
           
        $ remy2mood -= 1     
        
        
    "I'm up for some dessert.":
        
        $ renpy.pause (0.5)

        Ry smile "Then I have just the right thing for you."

        show remy normal with dissolve
                
        $ remy2mood += 1
        
        
Ry "I'll be just a minute."

play sound "fx/dishes.wav"

$ renpy.pause (0.5)

hide remy with dissolve

m "He neatly stacked our dishes before he took them into one of his forepaws and went back into the kitchen using his other three limbs. I couldn't help but think that it looked pretty awkward."

show remy normal with dissolve

m "When he returned balancing a plate with a rather attractive cake slice in a similar manner, I realized he would have to make multiple trips to carry everything to the table."

menu:
    
    "Wait.":
        
        $ renpy.pause (0.5)
        
        
    "Ask him if he needs help.":

        c "Do you need any help with that?"

        Ry smile "Don't worry about it, I can handle it. You're my guest, after all."

        
    "Help him.":

        c "As soon as I stood up and moved towards him, he made a strange face and spoke up."

        Ry shy "No, no, no, no, no. Sit down, please. I can handle it. You're my guest after all."

        m "Not wanting to upset him, I sat down again and waited."
        
        
hide remy with dissolve

m "Once he placed the first cake slice on the table, he went back to fetch the other. When he approached the table a second time, though, one of the tiny dessert forks started to slip off of the plate."

m "Remy reached with his free forepaw in his attempt to save it, but lost balance without its support and fell over."

play sound "fx/platecrash.ogg"

m "In an instant, the plate, fork and cake slice flew through the air. The dish and silverware clattered as the pristine cake crumbled into a sad heap on the floor."

show black with dissolve
$ renpy.pause (0.5)
show cgspill at Pan((0, 90), (0, 184), 6.0) with dissolvemed
#show cgspill at Pan ((0,184), (0, 184), 0.0) with dissolvemed
$ renpy.pause(4.5)

hide cgspill
hide black
show remy shy

with fade

m "For a few moments, there was silence as Remy and I looked at the result of his blunder."

Ry "I'm sorry, [player_name]."
        
menu:
    
    "You don't need to apologize.":

        $ remy2mood += 1
        
        
    "That's fine, I'll just eat your slice instead.":
        
        $ remy2mood -= 1
        
        
    "I didn't really want dessert anyway.":
        
        pass
        

Ry sad "This isn't just about you and your cake. This always happens to me, no matter how hard I try."

Ry "You have proper hands. So do some of the other species."

Ry "How can someone like me even be a librarian?"

Ry "Not a day goes by without me dropping a scroll and unfurling it across the room."

Ry "But the customers don't care, or pity me too much to say anything. It's a common sight for them, after all." 

c "This is about Emera, isn't it?"
        
Ry "I guess it is. I just don't see why someone like me got to be librarian when there were others more qualified for the position, or who were at least capable of not dropping the inventory on a daily basis."

c "She makes fun of you for it."

Ry shy "I knew it. I mean, why else would she have me do these tasks all the time. Sorting books, carrying things from one place to another."

Ry "I shouldn't be doing that. I shouldn't work somewhere where my worth is only in the entertainment I provide."

c "Why don't you look for a new job?"

Ry sad "These positions have terms, similar to those of ministers. If I ended my employment prematurely, it wouldn't look great."

c "How long do you have left?"

Ry "A while."        
        
menu:
    
    "You should resign, consequences be damned.": 
        
        $ renpy.pause (0.5)

        Ry look "That's easier said than done, but maybe I should consider it."
        
        
    "Can't you report her to a superior or something?":

        Ry "Not really. It's not like I could prove anything. Her public and her private demeanor are two very different things, and it would be my word against hers."
        
        
    "You'll just have to endure it.":

        Ry "Maybe I do."
  

Ry shy "I just wanted to have a nice evening with you, and now it ended up like this. I shouldn't have brought that up."
  
  
if remy2mood > 9:

    c "Then let's not talk about it further. We can still share the other slice, if you like."

    Ry "Alright."
    
    scene black with dissolveslow
    
    nvl clear
    
    stop music fadeout 2.0
    
    window show

    n "I helped him clean up, and after we were done, we shared the remaining slice of cake."

    n "It seemed unreal that someone with his personality could still eat his half with a single bite when I took much longer with my tiny fork."

    n "By the end of dessert, he seemed a little different, though I couldn't pinpoint how."

    n "Eventually, we said our good byes and I left."

    window hide
    
    $ remystatus = "good"
    
    $ remyscenesfinished = 2
    
    $ persistent.remy2skip = True
    
    nvl clear
    
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
elif remy2mood > 1:

    label remy2skip:
    
    c "Don't worry about it. I still think it was a nice evening."

    Ry look "Maybe I should stop being such a sourpuss then."

    c "I can help you clean up."

    Ry normal "Thank you, [player_name]."
    
    $ renpy.pause (0.5)

    scene black with dissolveslow
    
    nvl clear
    
    window show

    n "We cleaned up together and by the end, he seemed to be in higher spirits."

    n "Afterwards, we said our goodbyes and I left, not sure what to think."
    
    stop music fadeout 2.0
    
    window hide
    
    $ remystatus = "neutral"
    
    $ remyscenesfinished = 2

    $ persistent.remy2skip = True
    
    nvl clear
    
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
else:

    c "But you did."

    Ry sad "I know. I'm sorry, [player_name]."

    c "Maybe that's your problem."

    Ry "What?"

    c "You apologize all the time."

    c "Just look at yourself, lying on the floor with bits of cake everywhere. It's pathetic."

    Ry "..."

    c "You can't even respond to that? Maybe that's why Emera keeps making fun of you. You can't stand up for yourself."

    Ry shy "..."

    c "Maybe you should stop apologizing and start doing something about your problems. Otherwise, how do you expect things to change?"

    Ry "I don't know. I suppose you have a point."

    Ry "Well, I guess this evening's over, at any rate."

    c "I'll see myself out."

    Ry "Goodbye, [player_name]."
    
    hide remy with dissolve

    m "As I left the apartment, Remy got to his feet and started to clean up the mess."
    
    stop music fadeout 2.0
  
    $ remystatus = "bad"
    
    $ remyscenesfinished = 2
    
    nvl clear
    
    if chapter4unplayed == False:
                    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
  
  
  
  
  
  
  
  
  
  
  
  
  
        
        



$ remy2mood += 1

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
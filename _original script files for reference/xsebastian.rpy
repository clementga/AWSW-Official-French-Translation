label sebastian:
    
$ chapter1csplayed += 1
$ sebastianunplayed = False

if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Sebastian"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Sebastian"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Sebastian"
    
else:

    $ save_name = "Chapter 1 - Sebastian"

scene black with dissolvemed
$ renpy.pause (0.5)
scene o2 at Pan((0, 250), (0, 250), 0.1) with dissolvemed

play music "mx/feelings.ogg" fadein 2.0

play sound "fx/phonepickup.ogg"

$ renpy.pause (1.0)

c "Hey, Sebastian. This is [player_name]."

c "(Huh, he just hung up.)"

play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

show sebastian normal b with dissolve

c "You're still here?"

Sb smile b "I'm still on the clock, you know."

#insert skip here

if persistent.sebastianplayed == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_60

    call skiptut from _call_skiptut_14
        
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
            call skipcheck from _call_skipcheck_14
            
            show cave2
            show sebastian smile b
            with dissolvemed
            
            play music "mx/feelings.ogg" fadein 2.0

            $ mcwon = False
            
            jump sebastianskip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/feelings.ogg" fadein 2.0

c "Huh. Well, I'm glad you take my security so seriously."

Sb normal b "Just doing my job, sir."

menu:
    
    "Don't call me \"sir\".":
        
        $ renpy.pause (0.5)
        
        Sb shy b "Sorry, my bad. I haven't actually seen a human in flesh and blood before today, so it's kinda hard to tell."
        
        menu:
            
            "Don't worry about it.":
                
                pass
                
            "Actually, I just meant you don't have to be so formal with me.":
            
                pass
                
        $ renpy.pause (0.5)
                
        Sb smile b "Alright."
        
        show sebastian normal b with dissolve
            
        
    "I appreciate it.":
        
        pass

Sb "Anyway, did you need anything?"

c "It's just... It's pretty boring when I have to spend the day all on my own. I don't really know anyone here yet, so I don't know where I could go or what I could do for fun."

Sb "Well, if it were earlier I could've shown you around town and given you the tour, but it's getting dark outside, and I think most places are closed by now. Let me think..."

Sb "Do you like being outdoors?"

menu:
    
    "Yeah!":
        
        $ renpy.pause (0.5)

        Sb smile b "Oh, me too!"
        
        show sebastian normal b with dissolve
        
        
    "Not really.":

        Sb "I see."

        Sb "Maybe I could change your mind about that."
        
        c "What do you mean?"


Sb "What do you think about camping?"

c "You want to go camping, right now?"

Sb "Well, it might not be my best idea, but I'm not sure there's much else we could do at this time."

#c "Don't we need... stuff for that?"

#Sb smile b "Oh, you don't have to worry about that."

c "Would it even be okay for us to just... go outside?"

Sb smile b "I'm supposed to be guarding you, you know. Technically, I'm still on the clock, but camping would be much more fun than you just staying inside and me guarding your door, don't you think?"

Sb "Besides, I'm supposed to accompany you wherever you go. You're not our prisoner, so of course you're free to go wherever you want to."

Sb "If you wanted to spend a night outside and experience the countryside, not only could I not stop you, but I'd be obligated to come with you."


Sb "So, what do you say?"

menu:
    
    "Sign me up.":

        Sb "Sure. Let me just grab a few things."


    "I think I'd rather just stay here.":
        
        $ renpy.pause (0.5)

        Sb drop b "Really? Even after you called me and wanted to do something?"

        Sb normal b "Well, maybe next time."

        c "I'll see you around."

        Sb "I'm at the front door if you need anything."

        hide sebastian with dissolve
        play sound "fx/door/doorclose3.wav"
        stop music fadeout 1.0
        $ renpy.pause(1.0)
        
        $ sebastianfail = True

        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars


scene black with dissolvemed
$ renpy.pause (0.5)
scene cave2 with dissolveslow

$ renpy.pause (0.2)

show sebastian smile b with dissolve

Sb "Well, here we are."

c "I'm surprised we even got a spot this late after what you told me."

Sb "With a member of the police force and someone who is as important as you are, it's not really surprising. They probably regard it as an honor to be hosting us."

c "So, this is it? No tent, or anything?"

Sb normal b "Oh, tent camping would have been a bit more complicated to set up at the last minute."

c "Is there any other form of camping?"

Sb "What you're seeing here is cave camping. Essentially they're run like hostels, but you sleep in caves like this one."

c "Well, at least we got some furnishing. Could use a few sleeping bags, though." 

Sb smile b "If you wanted a comfy bed, you should've stayed in your room. This here is the real deal."

menu:
    
    "So I'm supposed to just sleep on the ground?":
        
        $ renpy.pause (0.5)
        
        Sb drop b "Oh, I get it. Your skin is sensitive and all that. Is that going to be a problem?"

        c "Well, I'm not going to die from it."


    "Sounds great.":
        
        Sb "Yep. Just us and nature itself."
        
        
c "We even have some natural lighting in here. So much for the \"real deal\"."

Sb disapproval b "We could just sit in the dark if you'd prefer that."

c "No, I think this will do."        
        
Sb smile b "Have you ever gone camping before?"
        
menu:
    
    "Not like this.":

        $ mp.camping = "notlikethis"
        $ mp.save()
        
        $ renpy.pause (0.5)

        Sb normal b "I see."
        
    "Plenty of times.":

        $ mp.camping = "often"
        $ mp.save()

        $ renpy.pause (0.5)

        Sb normal b "I see."
        
        
    "Nope, this is a first.":

        $ mp.camping = "first"
        $ mp.save()

        Sb "Let's make it a good one, then."
        
Sb drop b "You know, I was kinda nervous when I met you the first time."

c "I could tell."
        
Sb smile b "It was quite a thing to hear that humans were going to visit our world, but when I met you and it turned out you were just like an ordinary person, that really threw me off."

c "Didn't you meet Reza before?"

Sb normal b "Actually, no. Everything about your visit is clouded in secrecy, so I didn't get to hear much about Reza from Maverick before I met you."
        
c "I see."

c "So, are you one of those who expected me to act a certain way because I'm human?"

Sb "Actually, that didn't have much to do with it. Any high-profile guest would have made me nervous, especially if I was in charge of keeping them safe." 

Sb "I also happen to be the newest guy on the force, so I didn't exactly want this to turn into a career-ender right there."

menu:
    
    "You've been doing a great job so far. Don't worry about it.":

        $ renpy.pause (0.5)

        Sb smile b "Thank you. I'll do my best."

        c "I'm sure of it."
        
        show sebastian normal b with dissolve
        
        
    "With the whole murder situation going on, you should be careful that it doesn't end more than just your career.":
        
        $ renpy.pause (0.5)
        
        Sb drop b "Good point."
        
        show sebastian normal b with dissolve
        
    "Better hope these walls aren't going to cave in, then.":

        $ renpy.pause (0.5)

        Sb smile b "If these walls start to crack, I'm not going to be worried about my career."

        c "Good point."

        show sebastian normal b with dissolve
        
        
c "How long have been on the force? They didn't assign the rookie to me, did they?"

Sb smile b "Just because I'm the newest guy doesn't mean I'm a rookie. It's been a few years now."

c "I suppose that means you don't get many new recruits."
        
Sb normal b "Not here, at the very least. This is just a small town, so we don't really need them all that often.  I got lucky when I got this position, because I figured there'd be more competition from the locals."

c "Locals? Don't you live here?"

Sb "I live here now, but I actually grew up in a small farming village that mostly consisted of runners like me."

c "Runners?"

Sb "Oh, that's just what we call our species sometimes. We've got pretty powerful legs."

c "I can see that."

c "Are there many villages where the inhabitants are mostly of the same species?"

Sb "For sure. It's mostly smaller ones though, because the bigger they get, the more variety you'll find."

c "I see."
        
Sb "I only have my home town to compare, but from what I've heard, there are other villages that are fairly similar. They can only survive like that if they lead much simpler lives or if they focus on a certain industry that species is good at."

c "So your species is good at farming?"

Sb smile b "Better than the earth dragons at least, even though they come in handy pulling the plows."

c "Why did you decide to become a police officer?" 

Sb "I just wanted to see what's out there beyond our vegetable fields and if whatever was there was like the stories I'd heard."

c "Is it?"

Sb "Oh, yes. It's been great."

c "Now that you mention it, I don't really know much about this town, either."

Sb disapproval b "Well, what would you like to know?"

$ landavailable = True

$ landposavailable = False

$ peopleavailable = True

$ peopleposavailable1 = False

$ peopleposavailable2 = False

$ sebastianquestionsanswered = 0

label sebastianquestions:
    
if sebastianquestionsanswered > 4:
    
    jump sebastiancont
    
else:

    menu:
        
        "What can you tell me about the land?" if landavailable:
            
            $ renpy.pause (0.5)

            Sb smile b "The land? Well, I hear they have fertile soil. Not as fertile as my home town, though."

            c "I was talking more about if they have any sort of industry."

            Sb normal b "Oh, I see. This town is actually quite unique, because even though it's fairly small, it has its own production facility. With that, we basically have our own full production chain."

            c "So your one factory is everyone's pride and joy here?"

            Sb "In a way, yes. It makes us fairly independent and keeps everything local."
            
            $ landavailable = False

            $ landposavailable = True
            
            show sebastian disapproval b with dissolve

            $ sebastianquestionsanswered += 1

            jump sebastianquestions
            
        
        "What can you tell me about the people?" if peopleavailable:

            $ renpy.pause (0.5)

            Sb smile b "They're a friendly bunch, for the most part. Of course I also meet some unpleasant fellows in my line of work, but luckily, those seem to be the minority."

            Sb normal b "There was also a bit of a culture shock when I initially came here with all the different species living here together, but my police training took care of that."

            $ peopleavailable = False

            $ peopleposavailable1 = True

            $ peopleposavailable2 = True

            show sebastian disapproval b with dissolve
            
            $ sebastianquestionsanswered += 1

            jump sebastianquestions


        "What is it like to work with Bryce?" if peopleposavailable1:
            
            $ renpy.pause (0.5)

            Sb normal b "He kinda took me under his wing when I came here, and I've been working with him ever since. Pun not intended."

            Sb "I found it a bit weird that the big shot himself had to show the country bumpkin the ropes, though." 

            Sb "I thought he saw it as a challenge or that he wanted to scare me away, but honestly, he's been great. Everyone here trusts him a lot."

            show sebastian disapproval b with dissolve
            
            $ peopleposavailable1 = False

            $ sebastianquestionsanswered += 1

            jump sebastianquestions


        "What's it like having so many different species on the force?" if peopleposavailable2:
        
            $ renpy.pause (0.5)

            Sb normal b "Compared to my home town, it's been quite an interesting change. On one hand, you get all kinds of different people with all kinds of different strengths, abilities and backgrounds that can make your work so much easier." 

            Sb "On the other hand, it also creates all kinds of new problems that I never would have expected. I won't forget the first time I had to follow a shoplifter who also happened to be a flyer."

            show sebastian disapproval b with dissolve
            
            $ peopleposavailable2 = False

            $ sebastianquestionsanswered += 1

            jump sebastianquestions


        "Do you have any special recommendations or secrets I should know about this town?" if landposavailable:

            $ renpy.pause (0.5)

            Sb smile b "Secrets? This town doesn't really have any secrets."

            Sb disapproval b "Not that I know of, at the very least."

            c "Maybe you just don't belong to the inner circle yet."

            Sb smile b "I'd think as a member of the police force I'd get to see everything there is to see."

            Sb normal b "Either way, I don't think there's anything that special about our town."

            show sebastian disapproval b with dissolve
                    
            $ landposavailable = False

            $ sebastianquestionsanswered += 1

            jump sebastianquestions


label sebastiancont:

Sb smile b "But hey, I'm not the only one who's been new here. What are your impressions? Good, bad, ...ugly?"
        
menu:
    
    "No comment.":
        
        $ renpy.pause (0.5)

        Sb disapproval b "No comment?"

        c "Well, it's a bit early to say anything. It's only been a day."

        Sb "I see."

        $ mp.world = "none"
        $ mp.save()
        

    "It's been a bit hectic so far.":

        $ renpy.pause (0.5)

        Sb disapproval b "Oh, that is understandable with everything that's been going on."

        c "Maybe it's a good thing most places were closed. I'm not sure if I would've enjoyed any more sightseeing much."

        Sb smile b "I suppose you're just not a runner like I am. We don't mind staying on our feet."

        $ mp.world = "hectic"
        $ mp.save()


    "It's been fun so far.":
        
        $ renpy.pause (0.5)

        Sb drop b "Fun? That's not something I'd expect you to say after we showed you a corpse on your first day."

        c "Hey, if Bryce said it had to be done, then it's part of the job."

        $ mp.world = "fun"
        $ mp.save()


Sb disapproval b "I'm not sure if it was a good idea by Bryce to take you to the crime scene, though. I know he's a hands-on guy, but that really was a bit much. Pun not intended."

c "If you need my help, I'm glad to give it. Fostering goodwill and all that."

Sb normal b "Well, at least you don't seem to be traumatized from the experience."

c "..."

Sb smile b "Anyway, how about some fun?"

c "What kind of fun are you talking about?"

Sb "I brought some playing cards. A staple for any camping trip."

c "I see. What are we playing?"

Sb "Just a little game called {i}Bastion Breach{/i}. Ever heard of it?"

c "Can't say I have."

Sb "We often play it in the break room to pass the time. It's good fun, though things can get quite heated sometimes."

Sb "Let me go over the rules."

c "Sure."

label gamestart:

$ d2unplayed = True
$ d3unplayed = True
$ d4unplayed = True
$ d5unplayed = True
$ d6unplayed = True
$ d7unplayed = True
$ d8unplayed = True
$ d9unplayed = True
$ d10unplayed = True
$ djunplayed = True
$ dqunplayed = True
$ dkunplayed = True
$ daunplayed = True

play sound "fx/riffle.ogg"

scene black with dissolvemed
$ renpy.pause (0.5)
scene table 
show 2d at Position (xpos = 120, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show 3d at Position (xpos = 260, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show 4d at Position (xpos = 400, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show 5d at Position (xpos = 540, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show 6d at Position (xpos = 680, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show 7d at Position (xpos = 820, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show 8d at Position (xpos = 960, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show 9d at Position (xpos = 1100, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show 10d at Position (xpos = 1240, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show jd at Position (xpos = 1380, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show qd at Position (xpos = 1520, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show kd at Position (xpos = 1660, xanchor = "center", ypos = 0.95, yanchor = 0.4)
show ad at Position (xpos = 1800, xanchor = "center", ypos = 0.95, yanchor = 0.4)

show back2 at Position (xpos = 120, xanchor = "center", ypos = 1, yanchor = 0.4)
show back3 at Position (xpos = 260, xanchor = "center", ypos = 1, yanchor = 0.4)
show back4 at Position (xpos = 400, xanchor = "center", ypos = 1, yanchor = 0.4)
show back5 at Position (xpos = 540, xanchor = "center", ypos = 1, yanchor = 0.4)
show back6 at Position (xpos = 680, xanchor = "center", ypos = 1, yanchor = 0.4)
show back7 at Position (xpos = 820, xanchor = "center", ypos = 1, yanchor = 0.4)
show back8 at Position (xpos = 960, xanchor = "center", ypos = 1, yanchor = 0.4)
show back9 at Position (xpos = 1100, xanchor = "center", ypos = 1, yanchor = 0.4)
show back10 at Position (xpos = 1240, xanchor = "center", ypos = 1, yanchor = 0.4)
show backj at Position (xpos = 1380, xanchor = "center", ypos = 1, yanchor = 0.4)
show backq at Position (xpos = 1520, xanchor = "center", ypos = 1, yanchor = 0.4)
show backk at Position (xpos = 1660, xanchor = "center", ypos = 1, yanchor = 0.4)
show backa at Position (xpos = 1800, xanchor = "center", ypos = 1, yanchor = 0.4)

show 5c at Position (xpos = 120, xanchor = "center", ypos = 540, yanchor = 0.5)
show kc at Position (xpos = 260, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show 6c at Position (xpos = 400, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show 10c at Position (xpos = 540, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show 8c at Position (xpos = 680, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show ac at Position (xpos = 820, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show jc at Position (xpos = 960, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show qc at Position (xpos = 1100, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show 4c at Position (xpos = 1240, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show 7c at Position (xpos = 1380, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show 3c at Position (xpos = 1520, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show 9c at Position (xpos = 1660, xanchor = "center", ypos = 0.5, yanchor = 0.5)
show 2c at Position (xpos = 1800, xanchor = "center", ypos = 0.5, yanchor = 0.5)

with dissolvemed


Sb "As you can see, each of us starts with all cards of a given suit in their hands. You're diamonds and I'll be hearts."

menu:
    
    "Of course.":
        
        pass
        
    "You've got my heart already.":

        Sb "Is that so?"

        Sb "Anyways..."

    "You stole all those hearts, didn't you?":

        Sb "Haha, well... Maybe I did."

        Sb "Anyways..."


label sebgameexplanation:

show sebastian hand at Pan ((0, 650), (0, 350), 1.0) with dissolve

$ renpy.pause (0.5)

show sebastian hand at Pan ((0, 350), (-1000, 400), 3.0) #with dissolve

$ renpy.pause (3.0)

show sebastian hand at Pan ((-1000, 400), (-1000, 750), 1.0)

$ renpy.pause (0.5)

hide sebastian hand with dissolve

Sb "What you see in the center is the {i}middle row{/i}, which is a line of shuffled cards from another suit."

Sb "This way, each game is going to be unique since the middle row always changes between games."

show sebastian hand at Pan ((300, 600), (400, 300), 3.0) with dissolve#slow

Sb "Now, this is how the game works: We will play a round for each card in the middle row, starting with the one you see at the very left."

hide sebastian hand with dissolve

hide backk with dissolve

hide 8d with dissolve

show back at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)

show backk at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)

with dissolve

Sb "During each round, we both decide which card to play and put it there face down - like this."

show kh at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
show 8d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
with dissolve

Sb "Once we have both played a card, we flip them over. The highest card wins the round, and whoever played it gets a point."

play sound "fx/lose.ogg"
show lose at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
show win at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
with dissolve

Sb "To clarify, 2 is the lowest card and the king is the highest. The ace is a special card - it beats every face card, but will lose against any number card."

Sb "Now, the card from the middle row also counts, so it's possible that neither of us will get the point for a round."

Sb "If there is a tie, no clear winner between the three cards, or the middle row has the highest card, no player will get a point for that round. However, the next round will give the winner an extra point to make up for it."

Sb "At the end, the player with the most number of points wins the game."

Sb "Did you get all that?"



menu:
    
    "Yes. Let's get started.":
    
        hide back
        
        hide backk
        
        hide kh
        
        hide 8d
        
        show backk at Position (xpos = 1590, xanchor = "left", ypos = 1, yanchor = 0.4)
        
        show 8d at Position (xpos = 890, xanchor = "left", ypos = 0.95, yanchor = 0.4)
        
        hide win
        
        hide lose
        
        with dissolve
    
        jump sebgamestart
    
    "No. Please explain it again.":
        
        hide back
        
        hide backk
        
        hide kh
        
        hide 8d
        
        show backk at Position (xpos = 1590, xanchor = "left", ypos = 1, yanchor = 0.4)
        
        show 8d at Position (xpos = 890, xanchor = "left", ypos = 0.95, yanchor = 0.4)

        hide win
        
        hide lose
        
        with dissolve
      
        jump sebgameexplanation


label sebgamestart:
    
Sb "So, this game is all about bluffing and mind games. We can always see what cards have been played, so each of us knows exactly what the other player has left."

Sb "Alright, are you ready?"

c "Sure."

Sb "Don't worry, I'll go easy on you."

Sb "Take all the time you need to make your selection." 

stop music fadeout 1.0
#$ renpy.pause (1.0)

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb1 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (2.0)

hide eyesseb
hide roundb1
with dissolvemed

#$ renpy.pause (2.0)
$ mcpoints = 0
$ sebpoints = 0
$ pointsthisround = 1

play music "mx/chronos.ogg"

Sb "Ahh, a 5 for the first card makes for an interesting start." 

Sb "You could try to surpass it and play something higher, but if I'm going to do the same, you don't know how high I would go to not only beat the 5, but your higher card as well." 

Sb "Alternatively, you could count on me trying to beat a higher card and play a low one instead, thus making me waste mine."

Sb "What's it going to be, [player_name]?"

#warning: horrendous coding ahead

if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back2
    with dissolve
    show 2d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "tie"
    
if result == "3":
        
    hide 3d 
    hide back2
    with dissolve
    show 3d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "tie"

if result == "4":
        
    hide 4d 
    hide back2
    with dissolve
    show 4d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "tie"

if result == "5":
        
    hide 5d 
    hide back2
    with dissolve
    show 5d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "tie"

if result == "6":
        
    hide 6d 
    hide back2
    with dissolve
    show 6d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "win"

if result == "7":
        
    hide 7d 
    hide back2
    with dissolve
    show 7d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "win"

if result == "8":
        
    hide 8d 
    hide back2
    with dissolve
    show 8d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "win"

if result == "9":
        
    hide 9d 
    hide back2
    with dissolve
    show 9d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "win"

if result == "10":
        
    hide 10d 
    hide back2
    with dissolve
    show 10d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "win"

if result == "j":
        
    hide jd 
    hide back2
    with dissolve
    show jd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "win"

if result == "q":
        
    hide qd 
    hide back2
    with dissolve
    show qd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "win"

if result == "k":
        
    hide kd 
    hide back2
    with dissolve
    show kd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide back2
    with dissolve
    show ad at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "tie"



Sb "As you can see, I played a lowly 2 just to see what would happen."

Sb "Getting to know your opponent and their tendencies is just as important as analyzing potential moves and strategies."

#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win1 at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose1 at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    Sb "The first point is yours, but now you'll have to ask yourself: Was it worth it?"
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie1 at Position (xpos = 120, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1

    Sb "A tie. I guess we both tried to do the same thing here."

else:
    
    play sound "fx/lose.ogg"
    show lose1 at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win1 at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1

    Sb "You played your ace, huh? Not exactly the best move for the first round."


#round2 start

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb2 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb2
with dissolvemed

Sb "The king presents us with an interesting conundrum, especially when getting him early when most cards are still available. I'll let you figure this one out, though."

if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back3
    with dissolve
    show 2d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "tie"
    
if result == "3":
        
    hide 3d 
    hide back3
    with dissolve
    show 3d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "tie"

if result == "4":
        
    hide 4d 
    hide back3
    with dissolve
    show 4d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "tie"

if result == "5":
        
    hide 5d 
    hide back3
    with dissolve
    show 5d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "tie"

if result == "6":
        
    hide 6d 
    hide back3
    with dissolve
    show 6d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "tie"

if result == "7":
        
    hide 7d 
    hide back3
    with dissolve
    show 7d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "tie"

if result == "8":
        
    hide 8d 
    hide back3
    with dissolve
    show 8d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "tie"

if result == "9":
        
    hide 9d 
    hide back3
    with dissolve
    show 9d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "tie"

if result == "10":
        
    hide 10d 
    hide back3
    with dissolve
    show 10d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "tie"

if result == "j":
        
    hide jd 
    hide back3
    with dissolve
    show jd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "tie"

if result == "q":
        
    hide qd 
    hide back3
    with dissolve
    show qd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "tie"

if result == "k":
        
    hide kd 
    hide back3
    with dissolve
    show kd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "tie"

if result == "a":
        
    hide ad 
    hide back3
    with dissolve
    show ad at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "ace"




#insert if cases for result here
    
if roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie2 at Position (xpos = 260, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1

    Sb "Looks like a tie. Of course, the only card that beats a king is the ace, but playing it here would be a rookie mistake. It's definitely a safer play to just get rid of a low card here."
    
else:
    
    play sound "fx/tie.ogg"
    show tie2 at Position (xpos = 260, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1

    Sb "You did the predictable thing and play the ace, the only card that beats a king. Since my 3 beats your ace, though, this round is considered a tie. You may think that's not so bad, but taking away your ace with just a lowly 3 gives me big advantage during the rest of the game."


#round3 start

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb3 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb3
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back10
    with dissolve
    show 2d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "lose"
    
if result == "3":
        
    hide 3d 
    hide back10
    with dissolve
    show 3d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "lose"

if result == "4":
        
    hide 4d 
    hide back10
    with dissolve
    show 4d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "lose"

if result == "5":
        
    hide 5d 
    hide back10
    with dissolve
    show 5d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "lose"

if result == "6":
        
    hide 6d 
    hide back10
    with dissolve
    show 6d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "lose"

if result == "7":
        
    hide 7d 
    hide back10
    with dissolve
    show 7d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "lose"

if result == "8":
        
    hide 8d 
    hide back10
    with dissolve
    show 8d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "lose"

if result == "9":
        
    hide 9d 
    hide back10
    with dissolve
    show 9d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "lose"

if result == "10":
        
    hide 10d 
    hide back10
    with dissolve
    show 10d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "tie"

if result == "j":
        
    hide jd 
    hide back10
    with dissolve
    show jd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "win"

if result == "q":
        
    hide qd 
    hide back10
    with dissolve
    show qd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "win"

if result == "k":
        
    hide kd 
    hide back10
    with dissolve
    show kd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide back10
    with dissolve
    show ad at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "lose"




#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win3 at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose3 at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    Sb "Your point."
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie3 at Position (xpos = 400, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1

    Sb "Looks like a tie."

else:
    
    play sound "fx/lose.ogg"
    show lose3 at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win3 at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1

    Sb "My point."


#round4 starts here

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb4 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb4
with dissolvemed



if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide backq
    with dissolve
    show 2d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "lose"
    
if result == "3":
        
    hide 3d 
    hide backq
    with dissolve
    show 3d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "lose"

if result == "4":
        
    hide 4d 
    hide backq
    with dissolve
    show 4d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "lose"

if result == "5":
        
    hide 5d 
    hide backq
    with dissolve
    show 5d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "lose"

if result == "6":
        
    hide 6d 
    hide backq
    with dissolve
    show 6d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "lose"

if result == "7":
        
    hide 7d 
    hide backq
    with dissolve
    show 7d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "lose"

if result == "8":
        
    hide 8d 
    hide backq
    with dissolve
    show 8d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "lose"

if result == "9":
        
    hide 9d 
    hide backq
    with dissolve
    show 9d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "lose"

if result == "10":
        
    hide 10d 
    hide backq
    with dissolve
    show 10d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "lose"

if result == "j":
        
    hide jd 
    hide backq
    with dissolve
    show jd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "lose"

if result == "q":
        
    hide qd 
    hide backq
    with dissolve
    show qd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "tie"

if result == "k":
        
    hide kd 
    hide backq
    with dissolve
    show kd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide backq
    with dissolve
    show ad at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "tie"




#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win4 at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose4 at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie4 at Position (xpos = 540, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1


else:
    
    play sound "fx/lose.ogg"
    show lose4 at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win4 at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1


if mcpoints > sebpoints:
    
    Sb "Guess I should start playing seriously."
    
elif sebpoints > mcpoints:
    
    Sb "Don't worry, you can still win."
    
else:

    Sb "You're not too bad so far."
    
    
#round5 starts here

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb5 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb5
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide backj
    with dissolve
    show 2d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "lose"
    
if result == "3":
        
    hide 3d 
    hide backj
    with dissolve
    show 3d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "lose"

if result == "4":
        
    hide 4d 
    hide backj
    with dissolve
    show 4d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "lose"

if result == "5":
        
    hide 5d 
    hide backj
    with dissolve
    show 5d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "lose"

if result == "6":
        
    hide 6d 
    hide backj
    with dissolve
    show 6d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "lose"

if result == "7":
        
    hide 7d 
    hide backj
    with dissolve
    show 7d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "lose"

if result == "8":
        
    hide 8d 
    hide backj
    with dissolve
    show 8d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "lose"

if result == "9":
        
    hide 9d 
    hide backj
    with dissolve
    show 9d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "lose"

if result == "10":
        
    hide 10d 
    hide backj
    with dissolve
    show 10d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "lose"

if result == "j":
        
    hide jd 
    hide backj
    with dissolve
    show jd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "tie"

if result == "q":
        
    hide qd 
    hide backj
    with dissolve
    show qd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "win"

if result == "k":
        
    hide kd 
    hide backj
    with dissolve
    show kd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide backj
    with dissolve
    show ad at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "tie"




#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win5 at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose5 at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    Sb "Damn."
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie5 at Position (xpos = 680, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1

    Sb "A tie? Okay."

else:
    
    play sound "fx/lose.ogg"
    show lose5 at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win5 at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1

    Sb "Nice."


#round6 starts here

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb6 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb6
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back9
    with dissolve
    show 2d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "lose"
    
if result == "3":
        
    hide 3d 
    hide back9
    with dissolve
    show 3d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "lose"

if result == "4":
        
    hide 4d 
    hide back9
    with dissolve
    show 4d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "lose"

if result == "5":
        
    hide 5d 
    hide back9
    with dissolve
    show 5d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "lose"

if result == "6":
        
    hide 6d 
    hide back9
    with dissolve
    show 6d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "lose"

if result == "7":
        
    hide 7d 
    hide back9
    with dissolve
    show 7d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "lose"

if result == "8":
        
    hide 8d 
    hide back9
    with dissolve
    show 8d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "lose"

if result == "9":
        
    hide 9d 
    hide back9
    with dissolve
    show 9d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "tie"

if result == "10":
        
    hide 10d 
    hide back9
    with dissolve
    show 10d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "win"

if result == "j":
        
    hide jd 
    hide back9
    with dissolve
    show jd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "tie"

if result == "q":
        
    hide qd 
    hide back9
    with dissolve
    show qd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "tie"

if result == "k":
        
    hide kd 
    hide back9
    with dissolve
    show kd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "tie"

if result == "a":
        
    hide ad 
    hide back9
    with dissolve
    show ad at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "tie"



#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win6 at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose6 at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    

    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie6 at Position (xpos = 820, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1
    


else:
    
    play sound "fx/lose.ogg"
    show lose6 at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win6 at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1



$ difference = mcpoints - sebpoints

if difference == -1:
    
    Sb "Looks like it's pretty even so far."
    
elif difference == 0:

    Sb "Looks like it's pretty even so far."
    
elif difference == 1:

    Sb "Looks like it's pretty even so far."
    
elif difference < -1 :
    
    Sb "It's not looking too great for you."
    
else:
    
    Sb "Damn, you're better than I thought. Are you sure you haven't played this before?"


#round7 starts here

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb7 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb7
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back4
    with dissolve
    show 2d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "tie"
    
if result == "3":
        
    hide 3d 
    hide back4
    with dissolve
    show 3d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "tie"

if result == "4":
        
    hide 4d 
    hide back4
    with dissolve
    show 4d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "tie"

if result == "5":
        
    hide 5d 
    hide back4
    with dissolve
    show 5d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "tie"

if result == "6":
        
    hide 6d 
    hide back4
    with dissolve
    show 6d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "tie"

if result == "7":
        
    hide 7d 
    hide back4
    with dissolve
    show 7d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "tie"

if result == "8":
        
    hide 8d 
    hide back4
    with dissolve
    show 8d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "tie"

if result == "9":
        
    hide 9d 
    hide back4
    with dissolve
    show 9d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "tie"

if result == "10":
        
    hide 10d 
    hide back4
    with dissolve
    show 10d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "tie"

if result == "j":
        
    hide jd 
    hide back4
    with dissolve
    show jd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "tie"

if result == "q":
        
    hide qd 
    hide back4
    with dissolve
    show qd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "win"

if result == "k":
        
    hide kd 
    hide back4
    with dissolve
    show kd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide back4
    with dissolve
    show ad at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "tie"



#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win7 at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose7 at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie7 at Position (xpos = 960, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1


else:
    
    play sound "fx/lose.ogg"
    show lose7 at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win7 at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1


if mcpoints == 7:
    
    Sb "Seriously, how could I lose seven times in a row? Guess you win this one, [player_name]. I won't be able to catch up, so let's just finish it for the sake of it."
    
elif sebpoints == 7:

    Sb "I'm sorry to say this, but you just lost. The best you could do now is losing by one point, even if you win every round after this one."
    
else:

    Sb "This is the halfway point, so now it's really going to get serious. Anyone can still win."


#round8 starts here

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb8 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb8
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide backa
    with dissolve
    show 2d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "tie"
    
if result == "3":
        
    hide 3d 
    hide backa
    with dissolve
    show 3d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "tie"

if result == "4":
        
    hide 4d 
    hide backa
    with dissolve
    show 4d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "tie"

if result == "5":
        
    hide 5d 
    hide backa
    with dissolve
    show 5d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "tie"

if result == "6":
        
    hide 6d 
    hide backa
    with dissolve
    show 6d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "tie"

if result == "7":
        
    hide 7d 
    hide backa
    with dissolve
    show 7d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "tie"

if result == "8":
        
    hide 8d 
    hide backa
    with dissolve
    show 8d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "tie"

if result == "9":
        
    hide 9d 
    hide backa
    with dissolve
    show 9d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "tie"

if result == "10":
        
    hide 10d 
    hide backa
    with dissolve
    show 10d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "tie"

if result == "j":
        
    hide jd 
    hide backa
    with dissolve
    show jd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "lose"

if result == "q":
        
    hide qd 
    hide backa
    with dissolve
    show qd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "lose"

if result == "k":
        
    hide kd 
    hide backa
    with dissolve
    show kd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "lose"

if result == "a":
        
    hide ad 
    hide backa
    with dissolve
    show ad at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "tie"




#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win8 at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose8 at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    Sb "This one's yours."
    
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie8 at Position (xpos = 1100, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1

    Sb "Interesting..."

else:
    
    play sound "fx/lose.ogg"
    show lose8 at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win8 at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1

    Sb "I'll take this one."



#round9 starts here

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb9 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb9
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide backk
    with dissolve
    show 2d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "lose"
    
if result == "3":
        
    hide 3d 
    hide backk
    with dissolve
    show 3d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "lose"

if result == "4":
        
    hide 4d 
    hide backk
    with dissolve
    show 4d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "lose"

if result == "5":
        
    hide 5d 
    hide backk
    with dissolve
    show 5d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "lose"

if result == "6":
        
    hide 6d 
    hide backk
    with dissolve
    show 6d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "lose"

if result == "7":
        
    hide 7d 
    hide backk
    with dissolve
    show 7d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "lose"

if result == "8":
        
    hide 8d 
    hide backk
    with dissolve
    show 8d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "lose"

if result == "9":
        
    hide 9d 
    hide backk
    with dissolve
    show 9d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "lose"

if result == "10":
        
    hide 10d 
    hide backk
    with dissolve
    show 10d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "lose"

if result == "j":
        
    hide jd 
    hide backk
    with dissolve
    show jd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "lose"

if result == "q":
        
    hide qd 
    hide backk
    with dissolve
    show qd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "lose"

if result == "k":
        
    hide kd 
    hide backk
    with dissolve
    show kd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "tie"

if result == "a":
        
    hide ad 
    hide backk
    with dissolve
    show ad at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "tie"



#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win9 at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose9 at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    Sb "Oh, well..."
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie9 at Position (xpos = 1240, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1

    Sb "Oh my..."

else:
    
    play sound "fx/lose.ogg"
    show lose9 at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win9 at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1

    Sb "Yee-haw."
    
    
    
#round10 starts here

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb10 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb10
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back8
    with dissolve
    show 2d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "lose"
    
if result == "3":
        
    hide 3d 
    hide back8
    with dissolve
    show 3d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "lose"

if result == "4":
        
    hide 4d 
    hide back8
    with dissolve
    show 4d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "lose"

if result == "5":
        
    hide 5d 
    hide back8
    with dissolve
    show 5d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "lose"

if result == "6":
        
    hide 6d 
    hide back8
    with dissolve
    show 6d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "lose"

if result == "7":
        
    hide 7d 
    hide back8
    with dissolve
    show 7d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "lose"

if result == "8":
        
    hide 8d 
    hide back8
    with dissolve
    show 8d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "tie"

if result == "9":
        
    hide 9d 
    hide back8
    with dissolve
    show 9d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "win"

if result == "10":
        
    hide 10d 
    hide back8
    with dissolve
    show 10d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "win"

if result == "j":
        
    hide jd 
    hide back8
    with dissolve
    show jd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "win"

if result == "q":
        
    hide qd 
    hide back8
    with dissolve
    show qd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "win"

if result == "k":
        
    hide kd 
    hide back8
    with dissolve
    show kd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide back8
    with dissolve
    show ad at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "lose"





#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win10 at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose10 at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1

    Sb "Darn."
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie10 at Position (xpos = 1380, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1

    "Tie? Okay."

else:
    
    play sound "fx/lose.ogg"
    show lose10 at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win10 at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1

    "Phew."
    

#round11 starts here

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb11 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb11
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back7
    with dissolve
    show 2d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "lose"
    
if result == "3":
        
    hide 3d 
    hide back7
    with dissolve
    show 3d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "lose"

if result == "4":
        
    hide 4d 
    hide back7
    with dissolve
    show 4d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "lose"

if result == "5":
        
    hide 5d 
    hide back7
    with dissolve
    show 5d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "lose"

if result == "6":
        
    hide 6d 
    hide back7
    with dissolve
    show 6d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "lose"

if result == "7":
        
    hide 7d 
    hide back7
    with dissolve
    show 7d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "tie"

if result == "8":
        
    hide 8d 
    hide back7
    with dissolve
    show 8d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "win"

if result == "9":
        
    hide 9d 
    hide back7
    with dissolve
    show 9d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "win"

if result == "10":
        
    hide 10d 
    hide back7
    with dissolve
    show 10d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "win"

if result == "j":
        
    hide jd 
    hide back7
    with dissolve
    show jd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "win"

if result == "q":
        
    hide qd 
    hide back7
    with dissolve
    show qd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "win"

if result == "k":
        
    hide kd 
    hide back7
    with dissolve
    show kd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide back7
    with dissolve
    show ad at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "lose"





#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win11 at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose11 at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie11 at Position (xpos = 1520, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1


else:
    
    play sound "fx/lose.ogg"
    show lose11 at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win11 at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1

    


$ difference = mcpoints - sebpoints

if difference == -1:
    
    Sb "This is getting interesting."
    
elif difference == 0:

    Sb "This is getting interesting."
    
elif difference == 1:

    Sb "This is getting interesting."
        
else:
    
    Sb "Yeah, this game is pretty much over."
    
    
#round12 starts here    

play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb12 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb12
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back5
    with dissolve
    show 2d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "tie"
    
if result == "3":
        
    hide 3d 
    hide back5
    with dissolve
    show 3d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "tie"

if result == "4":
        
    hide 4d 
    hide back5
    with dissolve
    show 4d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "tie"

if result == "5":
        
    hide 5d 
    hide back5
    with dissolve
    show 5d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "tie"

if result == "6":
        
    hide 6d 
    hide back5
    with dissolve
    show 6d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "tie"

if result == "7":
        
    hide 7d 
    hide back5
    with dissolve
    show 7d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "tie"

if result == "8":
        
    hide 8d 
    hide back5
    with dissolve
    show 8d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "tie"

if result == "9":
        
    hide 9d 
    hide back5
    with dissolve
    show 9d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "tie"

if result == "10":
        
    hide 10d 
    hide back5
    with dissolve
    show 10d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "win"

if result == "j":
        
    hide jd 
    hide back5
    with dissolve
    show jd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "win"

if result == "q":
        
    hide qd 
    hide back5
    with dissolve
    show qd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "win"

if result == "k":
        
    hide kd 
    hide back5
    with dissolve
    show kd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide back5
    with dissolve
    show ad at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "tie"




#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win12 at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose12 at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie12 at Position (xpos = 1660, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1
    

else:
    
    play sound "fx/lose.ogg"
    show lose12 at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win12 at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1

$ renpy.pause (0.5)

#round13 starts here    
    
play sound "fx/woosh4.ogg"

show eyesseb at Pan ((500, 0), (0, 0), 0.7)
show roundb13 at Pan ((-500, 0), (0, 0), 0.7)

with dissolvemed

$ renpy.pause (0.5)

hide eyesseb
hide roundb13
with dissolvemed


if d2unplayed == True:
    $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

#textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")

if d3unplayed == True:
    $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d4unplayed == True:
    $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d5unplayed == True:
    $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d6unplayed == True:
    $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d7unplayed == True:
    $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d8unplayed == True:
    $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d9unplayed == True:
    $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if d10unplayed == True:
    $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if djunplayed == True:
    $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dqunplayed == True:
    $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if dkunplayed == True:
    $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

if daunplayed == True:
    $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



$ result = ui.interact()

$ renpy.block_rollback()

if result == "2":
        
    hide 2d 
    hide back6
    with dissolve
    show 2d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d2unplayed = False
    
    $ roundresult = "lose"
    
if result == "3":
        
    hide 3d 
    hide back6
    with dissolve
    show 3d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d3unplayed = False
    
    $ roundresult = "lose"

if result == "4":
        
    hide 4d 
    hide back6
    with dissolve
    show 4d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d4unplayed = False
    
    $ roundresult = "lose"

if result == "5":
        
    hide 5d 
    hide back6
    with dissolve
    show 5d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d5unplayed = False
    
    $ roundresult = "lose"

if result == "6":
        
    hide 6d 
    hide back6
    with dissolve
    show 6d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d6unplayed = False
    
    $ roundresult = "tie"

if result == "7":
        
    hide 7d 
    hide back6
    with dissolve
    show 7d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d7unplayed = False
    
    $ roundresult = "win"

if result == "8":
        
    hide 8d 
    hide back6
    with dissolve
    show 8d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d8unplayed = False
    
    $ roundresult = "win"

if result == "9":
        
    hide 9d 
    hide back6
    with dissolve
    show 9d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d9unplayed = False
    
    $ roundresult = "win"

if result == "10":
        
    hide 10d 
    hide back6
    with dissolve
    show 10d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ d10unplayed = False
    
    $ roundresult = "win"

if result == "j":
        
    hide jd 
    hide back6
    with dissolve
    show jd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ djunplayed = False
    
    $ roundresult = "win"

if result == "q":
        
    hide qd 
    hide back6
    with dissolve
    show qd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dqunplayed = False
    
    $ roundresult = "win"

if result == "k":
        
    hide kd 
    hide back6
    with dissolve
    show kd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ dkunplayed = False
    
    $ roundresult = "win"

if result == "a":
        
    hide ad 
    hide back6
    with dissolve
    show ad at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ daunplayed = False
    
    $ roundresult = "lose"



#insert if cases for result here
if roundresult == "win":
    
    play sound "fx/win.ogg"
    show win13 at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show lose13 at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve
    
    $ mcpoints += pointsthisround
    $ pointsthisround = 1
    
    
elif roundresult == "tie":
    
    play sound "fx/tie.ogg"
    show tie13 at Position (xpos = 1800, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve
    
    $ pointsthisround += 1


else:
    
    play sound "fx/lose.ogg"
    show lose13 at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win13 at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    $ sebpoints += pointsthisround
    $ pointsthisround = 1


Sb "Alright, that's it."

stop music fadeout 1.0

scene cave2
show sebastian normal b
with fade

play music "mx/feelings.ogg" fadein 2.0

$ mcwon = False

if mcpoints > sebpoints:

    Sb smile b "Seems like you won, fair and square. Of course I went easy on you. You know that, right?"

    c "Yeah, sure."

    $ mcwon = True
    
    if persistent.c1bastion == False:

        $ persistent.c1bastion = True
        
        $ achievement.grant("You are a winner!")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_61
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You won a game of {i}Bastion Breach{/i}!"
            
        elif system == "advanced":

            s "You won a game of {i}Bastion Breach{/i}. Congratulations."
            
        else:
            
            s "You won a game of {i}Bastion Breach{/i}. Without cheating, I hope."
    
    
elif sebpoints > mcpoints:

    Sb smile b "I'm sorry to say this, but you just lost."

    c "Yeah, I noticed."

    Sb "I guess I can't help it. I'm just that good."

    c "You beat someone who played this for the first time ever. Congratulations."

    Sb "Don't be a poor sport about it now. Maybe you'll win next time."

    c "If there ever is such a thing."

    $ mp.breach = "lost"
    $ mp.save()
    
elif sebpoints == mcpoints:
    
    Sb shy b "Huh, just look at that. We've got a draw."

    c "Is there no tie breaker or anything?"

    Sb disapproval b "No, not really."

    c "Guess it's a draw, then."

    Sb "This doesn't happen often. How peculiar."

    Sb smile b "Well, you didn't lose. That's pretty good for your first game."

    c "Thanks."

    $ mp.breach = "draw"
    $ mp.save()

elif pointsthisround >= 13:
    
    Sb shy b "What the heck just happened?"

    c "Seems we got a lot of ties here."

    Sb "No one at the department is going to believe me when I tell them about this."

    c "So, who won?"

    Sb disapproval b "No one. This is a draw. And the draw-iest draw I've ever seen, if I may say so."

    c "You certainly can."

    $ mp.breach = "ultradraw"
    $ mp.save()

    $ mp.breachultradraw = True
    $ mp.save()

elif mcpoints >= 13:
    
    Sb drop b "This is about the worst game of {i}Basion Breach{/i} I've ever played. How could this happen against a rookie like you?"

    c "Maybe I just got lucky."

    Sb disapproval b "Probably."

    c "Or maybe I'm just that good."

    Sb "Yeah, yeah. Whatever."

    play sound "fx/system.wav"

    s "You won a game of {i}Bastion Breach{/i}!"

    $ mcwon = True

    $ mp.breach = "ultrawin"
    $ mp.save()

    $ mp.breachultrawin = True
    $ mp.save()

else:
    
    Sb smile b "Wow, just look at that. I totally eradicated you."

    c "You just beat someone who played this for the first time ever, congratulations."

    Sb "{cps=10}E-R-A-D-I-C-A-T-E-D{/cps}{cps=1}.{/cps}"

    c "Alright, this is turning into a serious case of {i}bad winner syndrome{/i}."

    Sb "I mean, even if you just picked your cards randomly, you should at least have gotten one or two right just by chance, but this is something else entirely. Maybe I'm just that good."

    c "Guess I got unlucky."

    Sb "Actually, no. Sorry, but I really am just that good."

    c "Are you done?"

    Sb "..."

    Sb "Guess I am."

    c "Do you do this every time you win?"

    Sb "Only when my opponent gets completely {cps=10}{i}eradicated{/i}{/cps} like you just did."

    c "I see."

    $ mp.breach = "ultraloss"
    $ mp.save()

    $ mp.breachultraloss = True
    $ mp.save()


Sb normal b "I'll just put these away."

play sound "fx/riffle.ogg"

c "No rematch?"

Sb shy b "Maybe some other time. It's getting kinda late now."

c "If you say so."

Sb smile b "Hey, maybe next time you could teach me a human card game."

menu:
    
    "Sure.":
        
        $ renpy.pause (0.5)
        
    "Maybe.":
        
        $ renpy.pause (0.5)
        
    "I don't know any card games.":
        
        Sb "Really? Well, then we'll just have to play {i}Bastion Breach{/i} again."

        c "Sure..."

label sebastianskip:

Sb disapproval b "Maybe we should get some sleep now. I imagine it'll be just as busy tomorrow as it was today, and let's not forget I'll have to get up early to report about all this."

if mcwon == True:
    
    c "Don't leave out the part where I totally won."

    Sb "You wish."

$ renpy.pause (0.3)

play sound "fx/extinguish.ogg"

scene black with dissolve

$ renpy.pause (0.8)

Sb "So, how do you like your bed of rocks?"

menu:
    
    "It's alright.":

        Sb "Well, then. Have a good night."

        c "Good night, Sebastian."


    "It's pretty cold.":

        Sb "I suppose it takes some getting used to."

        c "A blanket would have been nice, at the very least."

        Sb "I could warm you up."

        c "Not sure it would be safe to keep a fire burning overnight."

        Sb "You're right, but I wasn't talking about that."

        c "I see..."

        Sb "Either way, the only blanket I can offer is myself."
        
        menu:
            
            "I'll take it.":

                Sb "Alright, then."

                play sound "fx/undress.ogg"
                
                $ renpy.pause (2.0)

                Sb "Is that better?"

                c "Sure."

                $ mp.sebastianromance = True
                $ mp.save()
                
            "No, thank you.":

                Sb "I see. Have a good night, then."

                c "Good night, Sebastian."


$ sebastianfail = False
#$ persistent.sebastianfail = False

$ persistent.sebastianplayed = True

$ mp.sebastianplayed = True
$ mp.save()

stop music fadeout 1.0
$ renpy.pause(1.0)

if chapter4unplayed == False:
            
    jump chapter4chars
    
elif chapter3unplayed == False:
    
    jump chapter3chars
    
elif chapter2unplayed == False:
    
    jump chapter2chars
    
else:

    jump chapter1chars

#sebastianfail = False at end which determines whether or not we have played his scene successfully

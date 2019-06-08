#-12, +15

label bryce2:

#$ chapter2csplayed += 1
$ bryce2unplayed = False
$ bryce2mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Bryce 2"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Bryce 2"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Bryce 2"
    
else:

    $ save_name = "Chapter 1 - Bryce 2"

scene black with fade
$ renpy.pause (1.0)
scene pad at Pan ((0, 220), (0,360), 3.0) with dissolveslow

$ renpy.pause (1.3)

show bryce normal with dissolve

play music "mx/campfire.ogg"

Br "Hey, [player_name]! Good to see you."

menu:
    
    "Thanks for the invitation.":
        
        $ renpy.pause (0.5)
        
        Br laugh "No need to be so formal."

        Br normal "Sure, I'm the chief, but here, I'm just Bryce."
        
        $ bryce2mood += 1


    "You too.":
        
        pass
        
    "Your face.":

        $ renpy.pause (0.5)
        
        Br brow "What's wrong with my face?"

        c "Never mind. I thought something was off, but that's how you always look."
        
        show bryce stern with dissolve

        Br "Just come inside."
        
        $ bryce2mood -= 1


if nodrinks == False:

    c "Wait a minute, something seems different here..."

    Br brow "What do you mean?"

    c "Oh, that's it; we're both sober."

    Br "I thought we weren't going to mention that."

    c "Right."

Br laugh "Don't mind the chaos, this is just a temporary arrangement."

#insert skip here

if persistent.bryce2skip == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_31

    call skiptut from _call_skiptut_6
        
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
            call skipcheck from _call_skipcheck_6
            
            scene pad at Pan ((0, 360), (0,360), 0.0)
            show bryce laugh
            with dissolvemed
                        
            play music "mx/campfire.ogg" fadein 2.0
            
            jump bryce2skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/campfire.ogg" fadein 2.0

show bryce normal with dissolve

m "He led me inside and motioned to the couch. When I took a seat and looked around, I realized that his apartment was obviously designed with only a single person in mind."

Br laugh "Ah, some days, all you can do is be glad they're over."

c "Long day at work?"

Br "You know how it is at the police department, especially with everything going on."

menu:
    
    "Is this a bad time for me to visit?":

        $ renpy.pause (0.5)
        
        Br normal "Heck, no. I could use some good company right now."

        $ bryce2mood += 1


    "Hey, things are pretty overwhelming for me, too. Being an emissary's no joke.":

        $ renpy.pause (0.5)
        
        Br brow "Good point. Guess we both have a lot to complain about."

        c "Hey, it's not a contest. We can commiserate."
        
    
    "How many dead have you found so far?":
        
        $ renpy.pause (0.5)
        
        Br stern "Too many. Each one we find is one too many."

        c "..."
        

Br laugh "So, what do you usually do for fun in your world?"

menu:
    
    "Read.":
        $ renpy.pause (0.5)
        
        Br brow "A little book-lover, aren't you?"

        Br laugh "Can't say I am." 

        $ mp.hobby = "books"
        $ mp.save()
        
        show bryce normal with dissolve


    "Meet with friends.":

        $ renpy.pause (0.5)
        
        Br normal "Right with ya on that one."

        #show bryce normal with dissolve

        $ mp.hobby = "friends"
        $ mp.save()
        
        $ bryce2mood += 1
        
        
    "Spend time outside.":
        
        Br "I get to be outside every single day."

        Br normal "I guess that means you don't mind me dragging you around everywhere?"

        c "If it weren't for the corpses and life-threatening situations, sure."

        Br laugh "Heh."

        $ mp.hobby = "outside"
        $ mp.save()

        show bryce normal with dissolve


    "Work out.":

        $ renpy.pause (0.5)

        Br brow "Is that so? I couldn't tell."

        c "Well, you don't really have a good frame of reference."

        Br laugh "Heh, guess not."

        $ mp.hobby = "workout"
        $ mp.save()

        show bryce normal with dissolve
        
        $ bryce2mood += 1
        

c "How about you?"

Br laugh "Different things. A little bit of this, a little bit of that... You know how it is."

c "That's not very specific."

Br brow "Alright, I'll show you something, but promise me you won't laugh, okay?"

menu:
    
    "Sure.":
        
        $ renpy.pause (0.5)

        Br normal "Good."
        
        $ bryce2mood += 1


    "I can't promise anything.":
        
        $ renpy.pause (0.5)
        
        Br stern "Just keep in mind what I could do to ya if you piss me off."

        $ bryce2mood -= 1
        

    "Just show me. We're both adults here.":
        
        Br "I sure hope so."


hide bryce with dissolve

#play sound "fx/wooden2.ogg"

m "He went to a shelf on the far side of the room and picked up a long object, carrying it in his maw as he returned to the table before me and gently set it down."

show bryce stern with dissolve

m "It was a wooden model ship."

m "From first appearances, I guessed it was a child's first attempt at assembling a model. While the shape was recognizable, there were odd pieces jutting out or not fitting together properly. In some places, globs of dried glue remained from excessive use."

menu:
    
    "Who's the Parkinson's-afflicted gent who did this?":
        
        $ renpy.pause (0.5)
        
        Br brow "I did this. What is Parkinson's?"

        c "It's a degenerative disorder that causes a range of symptoms, among them uncontrollable shaking."

        Br "Oh, I get it. No, I don't have a degenerative disorder, at least not that I know of."

        Br stern "And I know fully well what it looks like, but that's not my point."

        show bryce brow with dissolve
        
        $ bryce2mood -= 1


    "What's this?":
        
        $ renpy.pause (0.5)

        Br laugh "Well, you asked about my hobbies. I guess this is the latest one."
        
        show bryce brow with dissolve

    
    "Looks nice.":
        
        $ renpy.pause (0.5)

        Br brow "You don't need to lie to me, I know fully well what it looks like. But that's not the point."


Br "Even though I try, I don't always make the best decisions."

Br "I know I'm not the most patient person."

Br stern "But in my line of work, you never know what they're gonna throw at you next, so you always have to be prepared. You can't have any exploitable weaknesses."

Br normal "And of course, I wanna be fit for duty. As the chief, people look up to me, so I have to be at my best at all times."

Br brow "We can both tell the model's not very good. I don't really have the patience or the dexterity for it."

Br "But I tried my hand at this to get better."

Br "Sure, it took me way longer than it should have, and my claws were covered in glue for a week afterwards."

Br normal "But, you know, these models aren't even intended for us. They're made for runners like Sebastian who have the proper hands to do that stuff."

Br "I know this ship isn't much, but it's something."

Br "And maybe - if I keep trying - I'll get better." 

c "Wait a minute, you have ships?"

Br brow "Not in this town, but yeah, we have ships alright."

Br "Why does that surprise you?"

c "I just find it interesting, because where I come from, we also have vehicles for land and air travel."

Br normal "Well, some of us can fly, and some of us can run well, but none of us can swim beyond the seas."

c "Do you even have different continents?"

Br brow "Not that I know of. You'd probably have to ask someone who knows more about our world than I do."

c "How can you not know about something like that?"

Br laugh  "Well, we do get the occassional explorer who ventures out into uncharted seas, but I don't really keep track of that kind of thing."

c "Would you want to visit if they ever found one?"

Br brow "I can't say that I don't find the thought exciting, but in the end, I've got my people here, and they need their chief."

c "Maybe you could take a vacation and see what's out there."

Br "Hah! If I ever have time for that, maybe."

c "Can you swim?"

Br "Not particularly well. You may have noticed that I'm not exactly streamlined."

menu:
    
    "Don't worry, fat floats on water.":
        
        $ renpy.pause (0.5)

        Br stern "Seriously? Just because I don't look like a body builder doesn't mean I'm out of shape. Heck, I work out every day, and I train for strength - not to just look the part. Everything you see is 100%% pure muscle."

        $ bryce2mood -= 1


    "You're the pinnacle of masculinity.":
        
        $ renpy.pause (0.5)
        
        Br flirty "Glad you think so."
        
        Br normal "These muscles are the result of years of hard work."

        show bryce stern with dissolve

        $ bryce2mood += 1


    "Not quite.":
        
        $ renpy.pause (0.5)

        Br normal "But I can do something else. Wanna see?"

        c "Sure."
        
        show bryce stern with dissolve


Br "Alright, put your hand on my forearm."

c "Don't you technically have four legs?"

Br brow "I guess, but it's easier to say forearm than specifying the upper part of my foreleg."

Br laugh "Besides, using the word \"leg\" might get misinterpreted. That might make you think of my thigh, and that would be something else entirely."

menu:
    
    "Not that I'd mind grabbing your thigh.":
        
        $ renpy.pause (0.5)

        Br flirty "Is that so?"

        Br laugh "Well, let's just keep it on the arm for now."

        show bryce normal with dissolve

        $ bryce2mood += 1


    "Haha, right.":
        
        $ renpy.pause (0.5)
        
        show bryce normal with dissolve


    "I wouldn't think of touching you there.":
        
        $ renpy.pause (0.5)

        Br "Haha, well then."

        show bryce normal with dissolve

        $ bryce2mood -= 1


m "I placed my hand on the upper part of his foreleg, somewhat surprised at the warmth radiating from his scales."

Br stern "I hope you're ready, because here I go."

m "His forearm shifted, the shape of his muscles changing as they became more defined. In a moment, they were firm and bulging, his scales flaring under the stress and looking as though they might pop off at any moment. It reminded me of a flexing body builder in a skin-tight lycra suit."

m "After a few seconds, his muscles relaxed and regained their former shape."

Br smirk "See, that's what I'm talking about."

menu:
    
    "Color me impressed.":
         
        Br "Didn't expect that, huh?"
         
         
    "[[Flex your own puny muscles.]":
        
        c "You think you're the only one who can do that? Just take a look at this."
        
        show bryce brow with dissolve

        m "I rolled up my sleeves and flexed my arms, showing them off from the best angle as I struck a pose."

        Br laugh "Nice try, buddy, but I still don't think you want to arm wrestle with me."
        
        show bryce smirk with dissolve
                
        $ bryce2mood += 1
        
        
    "What a waste of time.":
        
        $ renpy.pause (0.5)

        Br stern "Alright, you don't care. I get it."

        $ bryce2mood -= 1



c "It's too bad that all those muscles couldn't help you when Reza got away and you got stuck on those stairs."

Br laugh "Hey, that wasn't my fault. It was the damn stairs."

Br stern "Speaking of which, this whole case has been completely insane. Us always a step behind Reza, and Maverick running around trying to catch him himself..."

Br brow "I wonder what he's been up to."

c "Maverick?"

Br stern "Yeah."

c "We had an interesting conversation not too long ago."

Br brow "What? When exactly was that?"

c "When I went into town to check your list of places Reza had been to."

Br "How come you didn't say anything about that before?"

c "I didn't think it was anything worth mentioning. It was a pretty one-sided conversation, anyway."

Br stern "Alright, maybe you should start from the beginning."

scene black with dissolve
$ renpy.pause (1.5)
scene pad at Pan ((0, 360), (0,360), 0.0) 
show bryce stern
with dissolvemed

Br stern "I don't want to say he's crazy, but I have no idea what he's talking about."

c "Me neither."

Br "You know, next time you should let the police decide whether something like that is worth mentioning or not."

Br brow "Why did you not tell us about this, again?"

c "I thought it was just Maverick being Maverick."

Br stern "He's not normally like that."

Br "I don't get it. Why has he been acting like that?" 

c "Do you think he's on to something?"

Br "I don't know, but there must be a reason behind his behavior."

menu:
    
    "Maybe he's just crazy.":

        Br "That's not the Maverick I know, but maybe he's lost it."

        $ bryce2mood -= 1
        
        
    "Maybe it's just a misunderstanding.":
        
        Br "Even if it started out that way, it's now turned into something dire. We need to find Reza as soon as possible."
        
        
    "Maybe he's right about Reza.":
        
        $ renpy.pause (0.5)

        Br brow "You think so?"

        c "Considering everything that's happened here so far, it's possible."

        Br stern "That would put you in a very bad position."

        c "I know, but if it was him, I can't change what he's done. I can only try to help you as much as possible."

        $ bryce2mood += 1


Br brow "I'm just thinking out loud, but Reza was the first of your kind to come here. He arranged the generator and PDA trade and then you came through the portal to deliver your part of the deal."

Br "Did your people have any goals or long-term plans for us? Or was this exchange going to be a one-off thing?"

c "It was supposed to be a scouting mission more than anything. A test to see if this kind of business relationship could work out. And if it did, it would make humanity very happy. Things aren't looking good on that front right now, though."

c "But, yeah, that's another reason why I'm helping you."

Br stern "However this whole thing turns out - no matter what happens - I've got your back, okay?"

menu:
    
    "Thank you.":
        
        $ renpy.pause (0.5)

        Br normal "No prob, buddy."

    
    "Likewise.":
        
        $ renpy.pause (0.5)
        
        Br smirk "Now that's the spirit."
        
        $ bryce2mood += 1


    "Watch your own back first.":

        $ renpy.pause (0.5)
        
        Br brow "If you say so."

        $ bryce2mood -= 1


Br laugh "Hey, I'm gonna grab myself a beer. You want one?"

menu:
    
    "Sure.":
        
        $ renpy.pause (0.5)

        Br smirk "Alright."

        $ mp.teetotaler = False
        $ mp.save()

        $ bryce2mood += 1


    "No, thanks.":
        
        $ renpy.pause (0.5)
        
        Br normal "If you say so."
    
    
    "I thought we didn't want to get drunk again." if nodrinks == False:
        
        $ renpy.pause (0.5)
    
        Br brow "If I want a beer in my own home, I sure as heck am gonna get myself a beer."

        Br laugh "Besides, it's just one beer; no one's gonna get drunk from that."
    
        $ bryce2mood -= 1
        
        
    "Can't you even stop drinking for the few hours I'm here?" if nodrinks: 

        $ renpy.pause (0.5)
    
        Br brow "If I want a beer in my own home, I sure as heck am gonna get myself a beer."

        Br laugh "Besides, it's just one beer; no one's gonna get drunk from that."
    
        $ bryce2mood -= 1
    
    
hide bryce with dissolve

m "Bryce got up and left through one of the doors to fetch his beer, leaving me alone in the room."    

$ bryce2magazine = False
$ bryce2legs = False

menu:
    
    "Wait.":

        c "(Well, he's taking his time.)"
        
        
    "Examine the blanket.":

        c "(What an interesting pattern.)"

        c "(The way the dark blue stripes contrast against the lighter hue is very pleasing to the eye.)"

        c "(It reeks of alcohol and dragon.)"
        
        if persistent.c2eau == False:

            $ persistent.c2eau = True
            
            $ achievement.grant("Eau de Dragon")
            
            $ persistent.achievements += 1

            $ mp.eaudedragon = True
            $ mp.save()
            
            call syscheck from _call_syscheck_32
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You examined Bryce's blanket!"
                
            elif system == "advanced":

                s "You examined Bryce's blanket. No comment."
                
            else:
                
                s "You examined Bryce's blanket. I hope you enjoyed yourself."
            
    
    "Look at the magazine on the coffee table.":
        
        m "Bold letters proclaimed the magazine's title as {i}Universal Fitness{/i}, its models on the cover catching my eye with their confident and athletic poses."

        m "Headlines like {i}STRONGER, THICKER TAILS{/i} and {i}AMAZING TIPS FOR BURNING PASSION{/i} gave me an indication of its topics."

        m "Curiosity got the best of me and I found myself staring at the first double page, which profiled their {i}Athlete of the Month{/i}. It was accompanied by a range of pictures showing off the athlete's body from different angles in a number of poses."

        if persistent.c2magazine == False:

            $ persistent.c2magazine = True
            
            $ achievement.grant("Research Material")
            
            $ persistent.achievements += 1

            $ mp.magazine = True
            $ mp.save()
            
            call syscheck from _call_syscheck_33
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You looked at Bryce's magazine!"
                
            elif system == "advanced":

                s "You looked at Bryce's magazine. Uh-huh."
                
            else:
                
                s "You looked at Bryce's magazine. I would've done the same."
        
        
        m "When I heard the door creak open, I quickly put the magazine back on the table before Bryce lumbered back into sight. He had the handle of a beer-filled basket clamped in his maw."
            
        $ bryce2magazine = True
        
        jump bryce2cont2
        
        
    "Stretch your legs a bit.":
        
        m "Not wanting to just sit around and wait, I did some simple stretching exercises to pass the time."
        
        if persistent.c2legs == False:

            $ persistent.c2legs = True
            
            $ achievement.grant("Leg Stretcher")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_34
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You stretched your legs for a bit!"
                
            elif system == "advanced":

                s "You stretched your legs for a bit. Really?"
                
            else:
                
                s "You stretched your legs for a bit. Apparently, this is worthy of an achievement."
                

        $ bryce2legs = True

    
play sound "fx/door/handle.wav"

$ renpy.pause (0.5)

m "Bryce lumbered back through the door, the handle of a beer-filled basket clamped in his maw."

show bryce normal with dissolve

label bryce2cont2:
    
    pass
    
play sound "fx/basket.ogg"

show bryce normal with dissolve

m "He carefully set the basket on the coffee table and took out the beers one-by-one. Once he was done, he swatted the empty basket into a far corner."

Br smirk "Help yourself if you like."

m "Bryce's store-bought beer looked very different from what I had seen in the bar. They were presented in large plastic bowls that were sealed at the top, reminding me of yogurt containers."

m "He broke the seal on one of the containers with his claw and proceeded to drink it noisily."

play sound "fx/chug.wav"

$ renpy.pause (0.5)

Br laugh "Sweet, sweet nectar. Always does its job."
    
if bryce2magazine == True:
    
    Br smirk "You know, you can keep looking at the magazine if you want. Not surprised you'd be curious."

    c "Hey, I'm not the one who bought it."

    Br laugh "You didn't mind looking when you had the opportunity. It's nothing to be ashamed of."

    c "Let me guess, you only buy it for the articles."

    Br smirk "Believe it or not, but their fitness tips are actually pretty good. The pictures are just a bonus."
    
else:
    
    pass
    
    
c "Can I ask you something?"

Br normal "Go for it."

c "Please don't take this the wrong way, but I watched how you carried the beer."
    
c "I was going to ask how you do daily tasks like shopping, for example, but I guess those baskets are your best friends."

Br laugh "That's just how we do things around here. Not sure why that's so special to you."

c "That makes me wonder. I know you can use your forelegs well enough for things, but what about your hind legs? Can you walk on those?"
    
Br normal "Good question. If you're just talking about my species, some of us can. At least a little."

Br laugh "But me? I probably wouldn't be able to take more than two steps that way."

c "Interesting."

Br brow "Maybe that's something I should practice as well. It'd be a good exercise in discipline."

Br laugh "Regardless, I wouldn't be part of any competition anytime soon."

c "You have competitions?"

Br normal "Oh, yes. Each species gets their own athletic competition with a few events every other year."

c "That sounds fun. Ever thought of joining in?"

Br laugh "It's not really my kind of thing."

Br brow "I mean, it's always just about who's the best, and the strongest, and who has the biggest muscles and all that. I'm not into that whole competitive lifestyle."

Br stern "And some of those events can also be a bit dangerous. One accident and it could be over for me as chief."

c "That sounds rough. What kind of competitions do you have?"

Br normal "They usually highlight the individual species' strengths and abilities."

Br "We get to do strength-based stuff, the flyers get to fly, the runners get to run, and so on."

Br laugh "Speaking of which, it's kinda funny just how upright you are when you move."

Br brow "The runners lean forward and use their big tails for balance, whereas you have yours tucked into whatever that is you are wearing."

c "Actually, we don't have tails."

Br "Are you kidding me?"

c "Not at all."

Br laugh "Seriously? Everything alive has a tail. How can you just not have one?" 

menu:
    
    "That's just the way we are.":
        
        pass

    "Evolution, I suppose?":
        
        $ renpy.pause (0.5)

        Br brow "Guess you were robbed of more than just your fur." 
        
        show bryce laugh with dissolve

    "Some animals just don't have tails, us included.":
        
        pass


Br "But tails are wonderful; just look at mine! That's a pretty wicked weapon right there." 

Br brow "And you just have nothing?"

c "Can't help it."

Br "You know what? I don't believe you."

c "I'm not sure how I can make this any more clear."

Br "Show me."

menu:
    
    "No way.":

        Br "Why the heck not?"

        c "I'm not sure if I can adequately explain this, but we wear these things for a reason. Asking to see what is underneath is very offensive in our culture."

        Br "Is that so?"

        c "Yes."

        Br "Sounds like an excuse to me, but I'm not going to argue."
            
        $ bryce2mood -= 1
        
        
    "[[Show him.]":
        
        c "(Alright, here goes nothing.)"
        
        stop music fadeout 1.0

        scene black with fade
        play sound "fx/undress.ogg"
        $ renpy.pause(2.5)

        scene pad at Pan ((0, 360), (0,360), 3.0) 
        show bryce laugh
        with fade

        play music "mx/campfire.ogg" fadein 2.0
        
        Br "I can't believe it. You really don't have a tail."

        c "Told you so."

        Br brow "Why do you cover it all up, anyway?"

        c "It's a human thing. We usually don't show our bodies to strangers."

        Br "So, friends are fine?"

        c "That would be an unusual friendship. Let's just say that displaying that area would usually imply more."

        Br flirty "Is that so?"

        $ bryce2mood += 1


    "Maybe another time.":

        Br "What's stopping you?"

        c "Erhm... we humans don't show that on the second date."

        Br normal "How about the third?"

        c "We'll see. Besides, you wouldn't have anything to look forward to otherwise."

        Br laugh "You tease."


c "Okay, so we've got tails covered, but what about wings?"

Br normal "I don't think we can call those little things on my back wings."

c "What are they, then?"

Br brow "Articulated pieces of armor, I guess."

c "Can you flap them?"

Br normal "I can try."

m "Bryce got up on all fours, grounding his body in preparation for what was to come."

Br stern "Hngh!"

m "His face contorted into a grimace as his upper body strained."

m "He held the pose for a few seconds, but nothing happened except for his continuous groan of effort."

m "Then, suddenly, his wings started to move. Slowly at first, they swayed up and down."

m "They gradually picked up speed and moved with a rhythm that could rightfully be called \"flapping\". It reminded me of the pigeons I often saw back home."

m "After holding it for a few seconds, he breathed a sigh of relief as he relaxed and the flapping motion stopped again."

m "A single bead of sweat rolled down the side of his face as he looked at me, panting."

menu:
    
    "That was awesome!":
        
        $ renpy.pause (0.5)

        Br laugh "Yeah, that was certainly a first." 

        Br "Too bad they don't have any flapping competitions for my species."

        $ bryce2mood += 1


    "Can you do that again? I wasn't looking.":

        $ renpy.pause (0.5)

        Br smirk "You cheeky lil' bastard."


    "You didn't even take off!":

        $ renpy.pause (0.5)

        Br brow "Well, let's see you do better."

        $ bryce2mood -= 1


Br normal "That was exhausting. Just the right time for a beer."
    
menu:
    
    "Stop him.":

        m "I snatched the beer out of his reach at the last moment."

        Br brow "Hey! That one's mine."

        c "I wasn't going to drink it."

        Br laugh "Then give it back."

        c "No, you've had enough."

        Br brow "Really? You're acting like a child."

        c "Yes, really. We said no getting drunk this time, so I'm cutting you off."

        Br laugh "I can easily drink another beer without it affecting me."

        c "No, you can't."

        Br brow "You're really pissing me off right now, you know that?"

        c "That's your own fault."

        Br stern "Just give me back my damn beer!"

        c "No."

        m "He lunged for it, but I was quick enough to leap away and position the sofa between us, matching his movements as he tried to get around it."

        Br brow "What's wrong with you?"

        c "I'm perfectly fine, thank you."

        Br "Then I guess I didn't notice how unbearable you are because we were drunk last time."

        c "Then I guess you can't enjoy my company sober."

        Br "You're overreacting. Why are you making such a big deal out of this?"

        c "No, the fact that you are getting so worked up about this proves to me that you are the one who is overreacting and that I'm right. You have a drinking problem."

        m "He was fuming, and if the situation wasn't resolved quickly, I knew he'd snap."

        Br stern "Alright, this is your last chance. Give me back my beer and I'll forget this ever happened."

        c "The only reason you forget things like this is because you keep getting drunk enough to do so. Besides, what are you going to do about it? What if I just opened it and poured it out? What would you do then, huh?"

        Br "You wouldn't dare!"
        
        play sound "fx/beeropen.ogg"

        m "I took the flap of the seal between two fingers and pulled on it just enough so the seal broke and the hissing sound indicated to both of us that the vacuum was gone."

        Br "RARGH!" with vpunch

        m "We ran a few more circles around the furniture, but his heavy stomps weren't enough to catch me." 
        
        play sound "fx/fall3.ogg"
        
        hide bryce with dissolve
        
        m "He tried to clamber over the couch, but his weight knocked it to the floor, and he spilled over the back of it and onto the floor. The apartment rattled with the force and the model ship, still on the table, fell and burst into splinters."

        Br "You bastard!"

        m "While he was still flailing around on the ground, I dashed through the front door."
        
        stop music fadeout 2.0
        
        scene black with dissolvemed

        m "Once outside, I dumped out the beer and rushed back to my own apartment."
    
        $ brycestatus = "bad"
        
        $ brycescenesfinished = 2
        
        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
    
    
    "Do nothing.":
        
        play sound "fx/gulp2.wav"
        
        m "I sat back and watched as Bryce took the last beer, opened it, and took his first sip with a slurp."
    
    
    "Ask him if he should really have another.":

        c "Should you really have another beer?"

        Br laugh "Why, did you want the last one? We can share."

        c "No, but you said there was more to you than getting drunk and this is your third one already."

        Br brow "If you say it like that you make me sound like an alcoholic or something. I just forgot, okay?"

        c "Okay."
        
        show bryce normal with dissolve
    
    
    
Br "So, I've been wondering, what does it take for someone to become humanity's ambassador?"

c "I'm still not quite sure how I ended up here. I guess in my case it was a combination of the right degrees, volunteering and a great deal of luck."

Br brow "But what kind of job did you have before that? Were you, like, a politican, or a diplomat, or what?"

c "Actually, I was none of those things. Reza, maybe - but certainly not me."

Br "I guess it's not like you needed ambassadors to represent humanity before, right? That makes this whole process a first, unless you had aliens show up at your place before."

c "It's funny that you say that, because for a while there actually was speculation that you were aliens."

Br laugh "Well, it's not like we fly around in spaceships or anything."

c "Strictly speaking, the word alien refers to any form of life that doesn't originate from our own planet."

Br brow "So that makes us aliens to each other, huh?"

c "Well, I'm not sure if that would be a good descriptor for your kind."

Br "Oh. Why not?"

c "Let's just say that where I come from, the word often carries negative connotations with it."

Br laugh "That's no good. What does that make us, then?"

c "I don't know. Maybe we'll have to make up a new word for sentient, civilized dragons." 

c "What do you think about us humans, anyway?"

Br normal "I know many others have their own ideas of what humans are or what they're supposed to be. I'm not buying into all that, so I'll just take it as it is."

c "And how is it?"

Br brow "Well, you've been interesting enough so far, and Reza... I'm reserving judgment on that one."

Br laugh "It's so funny to see people talking about humans all the time and what your presence could mean, while I'm one of the few who's actually gotten to meet you and knows what you're like." 

Br brow "And people still don't know about Reza. That'll certainly be interesting."

c "What do you think will happen once the truth about him gets out?"

Br "I'll start worrying about that once we know what the truth actually is."

c "Good point."

Br "You work with the police long enough, you learn not to have any preconceived notions about such things. Take things as they are and do what's necessary."

c "I imagine you've seen many things as chief."

Br stern "I certainly have. They're usually not the kind of thing I should tell people about, though."

c "Why not?"

Br brow "Not sure how it's done where you are from, but here people usually don't like me telling them about the horrible things I see at work."    
    
menu:
    
    "It can't be that bad.":
        
        $ renpy.pause (0.5)

        Br stern "You have no idea."

        $ bryce2mood -= 1    
            
    
    "I've probably seen worse.":

        Br "What, you wanna trade stories?"

        c "Not really."

        Br stern "I see."
            
        $ bryce2mood += 1    
    
    
    "I see.":
        
        $ renpy.pause (0.5)
        
        

Br laugh "Man, look at the time. We spent all afternoon talking."

c "Guess I should be heading back to my apartment."
    
    
    
if bryce2mood > 10:

    Br normal "You know, a few friends and I do this BBQ thing every year, and it's going to be pretty soon. You wanna come?"

    c "Sure, that sounds fun."

    Br laugh "Alright, I'll call you later with the details."

    Br normal "Can you find your way out?"

    c "Yeah."

    Br smirk "See you soon, then."

    c "See you."

    $ brycestatus = "good"
    
    $ brycescenesfinished = 2
    
    $ persistent.bryce2skip = True
    
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
    
    
elif bryce2mood > 2:
    
    label bryce2skip:
    
    Br normal "Yeah, it's getting pretty late, and I still have to prepare some stuff for tomorrow."

    Br "Can you find your way out?"

    c "Yeah."

    Br "See you soon, then."

    c "See you."

    $ brycestatus = "neutral"
    
    $ brycescenesfinished = 2

    $ persistent.bryce2skip = True

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

    Br brow "You know, I'm really not feeling this."

    c "What do you mean?"

    Br "'twas fun the first time around when we were in the bar. No offense, but you were kind of a jerk this time."

    c "Really? Is that how you are going to talk to me?"

    Br laugh "Hey, I said \"no offense\"."

    c "Two can play that game."

    c "No offense, but the only problem worse than your weight is your alcoholism."

    Br stern "Hey."

    c "\"Hey\", what? I said \"no offense\", bruh."

    Br brow "After saying something like that, you still don't think you're a jerk?"

    c "Maybe you should just stick to your chief of police thing."

    Br stern "Yeah, I guess that'll be the extent of our interactions from now on."

    c "Agreed."

    Br brow "Don't let the door hit your tail on the way out."
    
    $ brycestatus = "bad"
    
    $ brycescenesfinished = 2

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

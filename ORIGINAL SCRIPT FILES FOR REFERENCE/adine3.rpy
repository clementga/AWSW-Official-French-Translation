label adine3:

$ adine3unplayed = False
$ adine3mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Adine 3"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Adine 3"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Adine 3"
    
else:

    $ save_name = "Chapter 1 - Adine 3"

scene black with fade
$ renpy.pause (1.0)
scene town4 at Pan((0, 0), (0, 0), 0.0) with dissolvemed

play music "mx/adine3.ogg" fadein 2.0

c "Here we are again."

play sound "fx/knocking1.ogg"

$ renpy.pause (3.0)

Ad "Just a minute!"

play sound "fx/door/doorchain.ogg"

$ renpy.pause (2.0)

show adine normal b with dissolve

Ad think b "I hope I didn't forget anything."

c "You said something about going to the beach."

Ad normal b "Yep!"

if chapter3unplayed == False:

    if adinesendawayseen == False:
    
        Ad "You know, I'm glad they decided not to send you away after all."
        
        c "Me too."

        $ adinesendawayseen = True

Ad giggle b "Oh, guess who got her entry confirmation for the stunt flying competition!"

menu:
    
    "You did?":
        
        $ renpy.pause (0.5)
        
        Ad normal b "That's right!"

    "Is it me?":
        
        Ad "Don't be silly, [player_name]!"
        
        show adine normal b with dissolve

        $ adine3mood += 1
        
    "Remy did.":

        $ renpy.pause (0.5)
        
        Ad think b "What? What are you talking about?"

        c "It was a joke."

        Ad annoyed b "Oh. Not a particularly good one."

        Ad normal b "Anyways, it's me."

        $ adine3mood -= 1


Ad "I've got it right here in black and white."

Ad "{i}We are happy to confirm your entry into the annual stunt flying competition. Please have your competitor number ready and show up at the organisator's booth at the summer festival by...{/i}"

Ad "Well, who cares about the rest? I'm in!"

c "That's great."

Ad "Yeah, but the festival's pretty soon. I have to make the most of the time until then to get my skills up to par."

c "I thought you already had years of experience."

Ad "Yeah, but now I have to practice the best routine I can possibly come up with, not to mention making sure I can execute it flawlessly when the time comes. Practicing in general is very different than practicing for an event like this one."

c "I see."

Ad giggle b "Are you ready to see some stunt flying?"

c "Sure."

Ad normal b "Let's go then."

scene beach at Pan ((0, 0), (300, 0), 5.0) with dissolveslow


$ renpy.pause (2.5)

if persistent.adine3skip == True:

    stop music fadeout 1.0
    
    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_44

    call skiptut from _call_skiptut_9
        
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

            $ renpy.pause (0.5)

            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_9

            scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow

            $ renpy.pause (1.3)

            show adine disappoint b with dissolve

            play music "mx/adine3.ogg" fadein 2.0

            $ adinestagename = persistent.adinestagename
            
            jump adine3skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/adine3.ogg" fadein 2.0

c "So, this is where you usually practice?"

show adine normal b with dissolve

Ad "I practice just about anywhere, but today's a nice day for a beach visit. Water and sand are also good surfaces to practice complicated maneuvers on, in case you can't make the landing."

c "Makes sense."

c "Well, don't let me hold you up."

Ad giggle b "Oh, I can't just start practicing right now. I'm still giddy with excitement from getting that letter earlier. Besides, I wanted to hang out with you while we're here as well."

c "Sounds good to me. Do you visit the beach often?"

Ad normal b "Not really. Except for practice, that is. It does make for a nice backdrop while I fly, though."

c "I see."

Ad "Do you ever go to the beach?"

c "No. It's not something that was possible for me the last couple of years, but it certainly used to be something other people would do."

Ad think b "I see. Sunning yourself can be nice sometimes, but I'm not really a fan of going swimming."

c "There is so much more you can do at the beach, though."

Ad normal b "Like what?"

c "You already mentioned sunning. Do you ever get a tan?"

Ad think b "What's that?"

c "I guess that's a no, then."

c "To be fair, you are completely covered in scales, so I imagine you wouldn't be affected."

c "Tanning is a reaction of the skin when it's exposed to sunlight. If humans stay in the sun for a while, our skin can get darker."

Ad "How strange."

c "And if we are exposed for too long, we can even get what is called a sunburn."

Ad "And what's that?"

c "Well, the skin can take on a reddish tint, and it can also be painful and cause dizziness."

Ad "So, you have to be careful not to stay in the sun for too long?"

c "Pretty much, though that isn't necessarily true for all of us. Depending on the skin tone, people can be more or less affected by the radiation."

Ad "I see. That sounds kinda complicated."

Ad normal b "Does that mean we shouldn't stay here for too long?"

menu:
    
    "I'll just have to be careful.":

        $ mp.tan = "easy"
        $ mp.save()
        
        pass
        
    "Don't worry about it.":

        $ mp.time = "normal"
        $ mp.save()
        
        pass
        
    "It won't affect me much, if at all.":

        $ mp.time = "hard"
        $ mp.save()
        
        pass
        
Ad "I see. Just let me know if I need to do anything."

c "Sure. Will do."

c "You said you don't like swimming all that much. Why is that?"

Ad giggle b "Well, as you can imagine, I prefer the air to the sea, even though we flyers have quite a relationship with the water."

c "What kind of relationship are we talking about?"

Ad normal b "We use it to hunt."

c "I see. So you go fishing, but can't swim all that well."

Ad "Pretty much. We can do enough to safely hunt and paddle on the surface, but that's about it. If we actually want to go swimming, it's recommended we wear a life vest."

c "Is it that bad?"

Ad giggle b "Our wings are made for flying, not for swimming. The movements and musculature are rather different. With some training, we can learn to swim better, but it still wouldn't really be effective."

c "I see."

Ad normal b "And besides, who would choose to learn to swim if we already have the air to ourselves?"

c "Flying is just your thing, I guess."

Ad "Pretty much."

Ad think b "You made it sound as if beaches are a pretty important thing for humans."

c "I wouldn't say important. Rather, it's a unique way for people to spend time. It was often done as a leisure activity or a way to spend holiday vacations."

Ad giggle b "That sounds pretty important to me. What else did you do at the beach?"

c "Let me think..."

m "I got an idea and started looking for something in the sand on the ground. With a bit of digging, I found a flat, smooth stone and showed it to her."

c "Do you have any idea what I'm going to do with this?"

Ad normal b "Not really."

c "Let me show you something."

m "I went to the edge of the water, followed closely by Adine."

c "Now, watch this."

m "I extended my arm with the best technique I could muster before I threw the stone towards the water." 

play sound "fx/stones.ogg"

m "Spinning in the air, the stone bounced on the water's surface a few times before it sunk into the sea."

Ad think b "What was that?"

c "Stone skipping. Never heard of it?"

Ad normal b "No! How'd you do that?"

c "I can show you."

m "I looked around for another suitable stone and soon found one near the edge of the water."

c "Let's start with the stone. Ideally, we want one that has a big surface area, but is as flat as possible."

Ad "Got it."

c "This one is also really smooth, which helps too."

Ad think b "Okay, so we need smooth, flat stones."

c "Now, the technique is also pretty important."

c "I'm not sure how well this will translate to your anatomy, but I'll just show you how I do it, and then we can figure out what you can do."

Ad giggle b "Okay."

show adine normal b with dissolve

c "Hold the stone like this, extend your arm, and curl it like this. Then, you have to throw in such a way that it stays relatively stable in the air, but spins as fast as you can make it."

c "I do it like this."

play sound "fx/stones.ogg"

m "I threw the stone, once again showing her how it subsequently bounced a few times over the water's surface before it sunk into the sea."

Ad disappoint b "I'm not sure if I can do that."

c "We'll see. Maybe we can figure something out."

c "Let's look for a stone first."

Ad normal b "Okay."

m "We both started looking for another appropriate stone. I saw Adine scratching around the sand with one of her feet. She crouched down to pick something up before she returned to me."

Ad "Here, what about this one?"

c "That should work. See, you've already got that part down."

Ad giggle b "Guess so."

show adine normal b with dissolve

c "Okay, now for the technique..."

m "She was holding the stone in the claws at the edge of her wing. I tried to guide her by pulling her wing back like I would an arm, but it became clear to me that it lacked a lot of maneuverability an arm would have."

c "For the throw, you'll want to move your wing forward as fast as you can, and at the very end of the extension, let go of the stone."

Ad "I'll try."

m "I could see her moving her wing awkwardly. She pushed it forward before releasing the stone, which sunk without bouncing a single time."

play sound "fx/singlesplash.ogg"

$ renpy.pause (0.5)

Ad think b "That didn't work."

c "Yeah. There wasn't really enough spin on it."

Ad normal b "Let me try again!"

c "Alright."

m "I waded a few steps into the water to retrieve the stone she'd thrown only moments ago."

c "Here you go."

Ad think b "I'll try something different this time."

c "Feel free."

m "Instead of using her wing, she took the stone into the dextrous claws on one of her feet as she continued to stand on the other leg." 

m "Effortlessly, she pulled her leg back before rapidly moving it forward and releasing the stone." 

play sound "fx/splashes2.ogg"

m "It flew in a bit of an upward arch before it bounced off the water's surface once and subsequently sunk into the ocean's waters."

c "Nice!"

Ad giggle b "Not bad, huh?"

c "I had no idea you could do that with your leg."

Ad normal b "Actually, our legs are what we mainly use to grab things. It only gets complicated if I'm supposed to be moving at the same time, like when I'm waiting in the café."

c "Interesting. I suppose for someone who's hunting while flying that's pretty much a requirement."

Ad "It is. Actually, if I'm at home and eating chips or something, I usually use my feet as well."

menu:
    
    "That's kinda gross.":
        
        $ renpy.pause (0.5)
        
        Ad annoyed b "Hey, I know to wash my feet before I start eating something with them. I don't see how it's that different from doing it with your hands."
        
        show adine normal b with dissolve
        
        $ adine3mood -= 1
        
        
    "That sounds kinda funny.":
        
        $ renpy.pause (0.5)
        
        Ad giggle b "It probably isn't even half as funny as you're picturing it."
        
        show adine normal b with dissolve
        
        
    "I wish I could do that with my feet.":
        
        $ renpy.pause (0.5)
        
        Ad "Oh, really?"

        c "Yeah, some monkeys actually can. They basically have hands instead of feet."

        Ad think b "So they have four hands?"

        c "Yep."

        Ad normal b "That seems like it'd be handy, but I think I like my wings better."
                
        $ adine3mood += 1
        
        
Ad "That was a neat trick, though. So, what else can you do at the beach?"

c "I dunno. Build sandcastles?"

Ad giggle b "I haven't done that in like two decades."

m "I tried to imagine what Adine building a sandcastle would look like. Based on what I knew now, she probably wouldn't be using her wings."

c "Would you believe me if I told you we used to have contests for building sandcastles back home?"

Ad normal b "Really?"

c "Yeah, people would build huge, detailed sculptures that would be taller than both of us, just with sand."

Ad think b "Oh, wow. That sounds hard, though."

menu:
    
    "It is.":

        $ renpy.pause (0.5)
        
        show adine normal b with dissolve
        
        
    "It's not that hard.":

        $ renpy.pause (0.5)
        
        Ad normal b "Really? Are you talking from experience?"

        c "Kinda."
        
        
    "You could try it if you like.":

        $ renpy.pause (0.5)

        Ad giggle b "Hah, I'm not sure I have the patience for that."
        
        show adine normal b with dissolve


Ad "To me, it seems a bit of a shame to build big, elaborate sculptures out of something like sand that clearly won't last. I mean, if you're going to spend so much time on it, why not create something that will stay?"

menu:
    
    "I agree.":
        
        c "I agree. All that effort only to be swept away by the tide or worn down by the weather seems wasteful."

        Ad think b "It's kinda sad if you think about it."
    
        c "I guess we won't be building any sandcastles, then."
        
        show adine normal b with dissolve
        
    
    "That's actually the point of those contests.":

        $ renpy.pause (0.5)

        Ad think b "Oh, really?"

        c "Yes, people demonstrate their skill in creating these sculptures. And by using something like sand, they prove that it doesn't matter if the sculpture gets destroyed in the end because they can just do it again if they like."

        Ad normal b "I see. That's pretty interesting."

        c "Actually, it's not unlike your stunt flying competition."

        Ad think b "How so?"

        c "Well, during your competition, nothing lasting is created from the performance itself. It's all about the experience and memories. You have to prove that you are skilled enough to do those stunts right at that very moment just for the competition."
            
        Ad normal b "That's a good point."
            
    
Ad "I'm in the mood for a snack."

#Ad giggle b "Time to go fishing, then."

Ad "Should I get something for you as well?"
    
menu:
    
    "Yes, please.":

        $ mp.vegetarian = False
        $ mp.save()
        
        pass
        
    "No, thanks.":
        
        pass
        
        
Ad "Alright."

Ad giggle b "You can watch me if you like. Maybe you can learn a thing or two from it."

c "You want to teach me how to fish?"

Ad think b "Sure, since you taught me the... What was it called, again?"

c "Stone skipping."

Ad normal b "Right. Since you taught me the stone skipping, I can show you how to fish."

c "Okay."

Ad "We actually have two very different ways of doing it. There is hunting and angling."

Ad "Personally, I prefer hunting, though."

c "I can see why."

Ad "Let me demonstrate."

hide adine with dissolve

play sound "fx/takeoff.ogg"

m "She took a few steps back, then started running towards the edge of the sea. Rapidly flapping her wings, she jumped into the air at the last second, taking off and flying around the area."

m "I could see her staring at the sea intently, circling a few times before descending towards the water's surface, claws extended. When she got close enough, her claws suddenly sunk into the water, only to reappear with a fish in their grasp."

play sound "fx/landing.ogg"

m "Afterwards, she returned and landed near me."

show adine normal c with dissolve

Ad "Did you see that?"

c "Yeah, but I think my distinct lack of wings would probably prevent me from doing the same thing."

Ad annoyed b "You don't have to do exactly the same thing. In the end, I'm just grabbing them right out of the sea. You could do that."

c "I'm not so sure about that. I bet it's a lot easier with your claws. Fish can be pretty slippery."

Ad giggle b "I guess you have a point."

Ad normal b "Well, there's still the other method."

c "Angling."

Ad giggle b "Yep, angling. See my tail?"

m "She showed me her tail. At its end, there was a fork in it. With its distinct shape, size and color, it reminded me a lot of a banana."

c "What about it?"

Ad normal b "This is the bait." 

m "She sat down near the edge of the water, letting her tail hang down into it."

Ad think b "This can take a while sometimes, but there are techniques which can speed up the process."

Ad normal b "The right amount of movement attracts different kinds of fish. That way, we can even choose what we're going to get."

c "And that works?"

Ad "Yeah. Not all the time, but often enough."

c "Interesting."

Ad giggle b "There are even groups that exchange tips and such for angling this way."

show adine normal b with dissolve

play sound "fx/fish.ogg"

m "Suddenly, I saw her whip her tail upwards, which caused a fish to be launched towards the beach where it landed on the ground with an audible thud."

Ad giggle b "There you go."
    
c "That didn't take too long."

Ad normal b "It can be very hit and miss. I just got lucky this time, and it's not even the kind of fish I really wanted." 

c "I guess that's why you prefer hunting."

Ad giggle b "Yep, and you also don't get the nibble scars on your tail where the fish bite you."

c "I see."

Ad normal b "Though, I suppose angling is also going to be hard for you without a forked tail like we have."

c "Actually, we have fishing rods for that where I come from."

Ad think b "What's that?"

c "The principle is very similar. Basically, it's a long stick that we hold over the water. A line connected to it has a bait and hook at the end to catch the fish. When the fish bites the hook, we can reel in the line to get the fish to us."

Ad "So you are using a tool to do a very similar thing."

c "Basically, yes."

c "Sometimes, we also fish using nets."

Ad normal b "Oh, some of us do that as well. Not my kind, but usually it's those who either work for a fishing company or sell seafood on the market."

c "I imagine someone like you doesn't have to buy their fish on the market, though."

Ad "True, but sometimes it's easier to just get them there to get what I want to, instead of coming all the way here."

c "I see."

Ad think b "Speaking of which, let me get a few more for later."

c "Feel free."

hide adine with dissolve

m "Once more, Adine took to the sky to hunt for fish. While it was interesting to watch her for a bit, she kept hunting for a while, and I started passing the time by collecting some seashells."

show adine think c with dissolve

Ad "Phew, that should last me for a while."

Ad normal b "Oh, what are those? Seashells?"
    
menu:
    
    "I was bored.":

        c "I got bored, so I collected a few."

        Ad "What are you going to do with them now?"

        c "I'll just leave them here. No point in doing anything with them."

        Ad think b "I see."
        
        show adine normal b with dissolve
    
        $ adine3mood -= 1
    
    
    "They're for you.":

        Ad "For me? What for?"

        c "Well, you could decorate your apartment with them or something."

        Ad "I see."

        Ad think b "Maybe I should ask you to clarify this, but does this have any particular significance for humans?"

        c "Not really, it's just a gift."

        Ad normal b "Oh, okay."

        Ad "Well, thank you, [player_name]!"
            
        $ adine3mood += 1    
            
    
    "Just a souvenir for when I get back home." if persistent.seashells == False:

        Ad "I see."
            
        $ persistent.seashells = True

        $ mp.seashells = True
        $ mp.save()
        
        $ persistent.seashells = True
            
        $ achievement.grant("Souvenir")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_45
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You got some seashells!"
            
        elif system == "advanced":

            s "You got some seashells. Three of them."
            
        else:
            
            s "You got some seashells. Are you sure it's okay to take them? Well, too late for that now..."

    
Ad "All that hunting was a good warm-up. I feel about ready to start with the practice now."    

c "Go ahead, I'll watch from here."

Ad giggle b "Actually, now that I'll be part of an official competition, I need a fancy stage name."

c "Do you have something in mind?"

Ad think b "Not really. Have you got any ideas?"

menu:
    
    "Freefall": #darkfall
        
        if persistent.adinestagename == "Freefall":
            
            Ad "Freefall? Where have I heard that before?"

        else:

            Ad "Freefall?"

        Ad normal b "Actually, that sounds pretty nice!"

        Ad think b "Do you mind if I go with that?"

        c "Not at all."

        Ad normal b "Freefall it is, then."
        
        $ adinestagename = "Freefall"

        $ persistent.adinestagename = "Freefall"

        $ mp.adinestagename = "Freefall"
        
    
    "Lightning":

        if persistent.adinestagename == "Lightning":
            
            $ renpy.pause (0.5)
            
            Ad giggle b "I kinda had an idea you'd say that."
            
            Ad normal b "I like it, though."

        else:
        
            Ad "Lightning?"

            Ad normal b "I like the sound of that."

        Ad think b "Do you mind if I take that name?"

        c "Not at all."

        Ad normal b "Lightning it is, then."
        
        $ adinestagename = "Lightning"

        $ persistent.adinestagename = "Lightning"

        $ mp.adinestagename = "Lightning"
        
        
    "Neowing": #blackwing

        if persistent.adinestagename == "Neowing":
            
            Ad "That's weird. I think I'm having a déjà vu right now."
            
            Ad normal b "Either way, that sounds gracious and acrobatic. I like it."
            
        else:

            Ad "Neowing?"

            Ad normal b "That sounds gracious and acrobatic. I like it."

        Ad think b "Do you mind if I go with that?"

        c "Not at all."

        Ad giggle b "Guess I'll be Neowing from now on, then."
        
        show adine normal b with dissolve
        
        $ adinestagename = "Neowing"

        $ persistent.adinestagename = "Neowing"

        $ mp.adinestagename = "Neowing"
        
    
    "Angel": #fallen angel

        if persistent.adinestagename == "Angel":
            
            Ad "Oh, why didn't I think of that? Ever since I knew about the contest, I've been thinking of this name."
            
            Ad giggle b "What a crazy coincidence."
            
        else:

            Ad "Angel? Like the mythological human with wings?"

            Ad normal b "That sounds pretty awesome!"

        Ad think b "Do you mind if I go with that?"

        c "Not at all."

        Ad normal b "Angel it is, then."
            
        $ adine3mood += 1    
    
        $ adinestagename = "Angel"

        $ persistent.adinestagename = "Angel"

        $ mp.adinestagename = "Angel"
    
    
    "Stormhawk": #blackhawk

        if persistent.adinestagename == "Stormhawk":
            
            Ad "Now this is peculiar. I feel like I've heard the word hawk before, but I'm not sure what it means."
            
            c "It's a bird of prey."
            
            Ad giggle b "Oh, I see."
            
        else:

            Ad "Stormhawk?"

            Ad normal b "That sounds powerful and dynamic. I like it."

            Ad think b "Do you mind if I go with that?"

            c "Not at all."

        Ad normal b "Then, henceforth, I shall forever be known as \"Stormhawk\"."
    
        $ adinestagename = "Stormhawk"

        $ persistent.adinestagename = "Stormhawk"

        $ mp.adinestagename = "Stormhawk"
        
    
    "[[Custom name]":
        
        c "Hmm, let me think."
        
        c "How about..."
        
        label adinestagenameentry:
            
            pass
        
        if not mp.adinestagename:
        
            $ adinestagename = renpy.input("Enter a stage name for Adine:", default="Stagename", exclude='{%}', length=10)
            #$ adinestagename = renpy.input(c "How about", default="Stagename", exclude='{%}', length=10)
            
        else:
            
            $ adinestagename = renpy.input("Enter a stage name for Adine:", default=persistent.adinestagename, exclude='{%}', length=10)

            if adinestagename == persistent.adinestagename:
                
                Ad "[adinestagename]? Where have I heard that before?"
                
                Ad giggle b "Either way, it's a good name. I'll keep it."

                $ persistent.adinestagename = adinestagename

                $ mp.adinestagename = adinestagename
                
                show adine normal b with dissolve
                
                jump mpsave
                
            else:
                
                pass

        #$ mp.adinestagename = player_name

        $ mp.adinestagename = adinestagename

        if adinestagename == "":
            $ adinestagename = "Stagename"
            
        elif adinestagename == "Adine":
            
            Ad giggle b "Try again."
            
            show adine think b with dissolve
            
            jump adinestagenameentry
            
        Ad "[adinestagename]? Are you sure?"
        
        menu:
            
            "Yes.":

                $ renpy.pause (0.5)
                
                Ad normal b "That sounds alright."

                Ad think b "Do you mind if I go with that?"

                c "Not at all."

                Ad normal b "[adinestagename] it is, then."
                
            "No.":
                
                jump adinestagenameentry

label mpsave:
        
$ mp.save()

Ad "Alright, are you ready to see some aerobatics?"

c "I certainly hope so."

Ad "I'll start off with a few easy moves."

c "The stage is yours, [adinestagename]."

Ad "Thanks!"

hide adine with dissolve

m "Effortlessly, she took to the skies, circling around the area a few times before she started to do a few maneuvers."

show black with dissolve
$ renpy.pause (0.5)
show adineflying at Pan ((0, 326), (580, 0), 5) with dissolvemed
$ renpy.pause(3.5)
hide black
hide adineflying
with fade


m "A roll, followed by a loop, after which she did another roll. It seemed to be less of a practiced routine and more of a warm-up to me."

m "Gradually, her maneuvers got more complicated. I saw circles that got smaller and smaller, a brief nosedive, and multiple loops and rolls one after another."

m "Then, she landed and returned to me."

show adine normal c with dissolve

Ad "What do you think?"

c "That was great!"

Ad "You haven't even seen the best part yet."

c "What would that be?"

Ad "My very own Adine's special. Or rather, [adinestagename]'s special. It's a routine I came up with and have been practicing for a while."

Ad think c "It's pretty difficult, so I'll probably spend the rest of my time until the competition perfecting it as much as possible."

c "What does it look like?"

Ad normal c "It starts off with circles near the ground. Then, as I ascend, the circles get smaller and smaller. Once I reach the highest point, I go into a nosedive through the middle of the circles." 

Ad "At the show, I'll use a smoke trail when doing the circles, so everyone can actually see me going through the circles I made."

c "That sounds pretty cool."

Ad "That's not all of it. While nosediving, I'll do a few rolls, and just before I hit the ground, I'll pull up again. Lastly, I'll end with a few loops and go to the next maneuver. It all ends up making a neat shape in the sky with the smoke trails."

c "Sounds like you've got it all figured out already."

Ad giggle c "Yeah, now I only have to perfect my execution of it."

c "Don't let me hold you up."

Ad normal c "Alright, here we go."

hide adine with dissolve

m "With determination in her eyes, she took to the skies once more. When she reached a certain height, she slowly descended again until she was close to the water's surface."

m "Then, she started making her circles, slowly ascending as the circles gradually got smaller and smaller."

m "Once her circles became as small as possible, she suddenly turned herself around and went into a nosedive."

m "Her speed quickly increased while she moved towards the water. Then, she did a roll, and another, followed by the third. Dangerously close to the water's surface, she suddenly pulled up, but as she did so, one of her feet went below the surface, where it apparently caught onto something, causing her to spin out of control."

m "I saw her feeble attempt to regain control as she barely managed to steady herself enough to get back to the beach. She made a rough landing, rolling on the ground a few times after colliding with the sand."

c "Adine! Are you alright?"

show adine disappoint c with dissolve

Ad "Well, that wasn't supposed to happen."

c "It looked pretty impressive until the landing."

Ad sad b "Ouch, my wing hurts."

c "Let me take a look."

c "Can you move it?"

Ad disappoint b "A bit, but it really starts to hurt if I go further than this."

c "At least it doesn't seem to be broken."

Ad annoyed b "Yeah, I guess it's a sprain. Happens all the time."

c "Really?"

Ad disappoint b "Well, not all the time, but it happens."

c "What about the competition?"

Ad annoyed b "The injury is going to put a serious damper on my practice schedule, but I'm not giving up anytime soon."

c "I guess practice is over for today, at the very least."

Ad disappoint b "Yeah, let's head back."

scene black with dissolvemed

$ renpy.pause (0.5)

scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow

$ renpy.pause (1.3)

show adine disappoint b with dissolve

label adine3skip:

Ad "I should have some bandages in the cabinet over there."

play sound "fx/cabinet.ogg"

c "I'll get them for you."

#$ renpy.pause (0.5)

c "What now?"

Ad "Would you do me the honors?"

c "Of course. Where should I start?"

Ad think b "I think it's this joint right here."

Ad disappoint b "Yep, definitely."

c "Okay. Let me try to get this right."

play sound "fx/bandage.ogg"

if persistent.chapter2libraryvisited == True:
    
    if persistent.playedremy3 == True:
        
        c "Can I ask you something?"

        Ad normal b "Sure, go right ahead."

        c "You went to visit Remy in the library the other day, right?"

        Ad annoyed b "How do you know that?"

        c "I was there, and Remy told me about everything."

        Ad think b "What do you mean, everything?"

        c "Amelia."

        Ad disappoint b "Oh."

        Ad think b "Why'd he tell you about all that?"

        c "He's dealing with a lot of stuff, it seems."

        Ad annoyed b "Well, he isn't the only one. I actually wanted to talk with him again, but if he doesn't respond, then I can't do anything, either."

        c "I see."

        Ad disappoint b "I guess I remind him too much of her."

        Ad "If he knew what I know, I'm not sure what he would do."

        c "What's that?"

        Ad "When she got sick, I often visited her. I just wanted to check up on her and take a little of the edge off, considering what she was going through at work."

        Ad "The night she died, I was actually with her. I stayed with her until pretty late, but as I had to work the next day, I eventually left. It was late enough, and I told her to take it easy."

        Ad "She told me that she was just going to finish up one little thing before she got some much needed sleep."

        Ad sad b "But only after I left did she realize that she had run out of her medication and went out alone to get a refill. If she just told me, or if I had paid more attention and noticed, I could've gotten it for her, and then none of this would have happened."

        Ad "And that's not even the worst of it. When she died, she..."

        Ad disappoint b "She was pregnant."

        Ad "They had already made so many plans, and I expected them to announce their engagement any day."

        c "Remy doesn't know she was pregnant?"

        Ad "He doesn't. Or at least, I think he doesn't. They couldn't talk to each other much, as they had to keep their relationship secret. It's not exactly something she'd want to mention in just a few sentences."

        Ad "If he knows, then it certainly wasn't from her telling him about it."

        c "I see."

        Ad "If he doesn't know, please don't tell him."

        c "Alright."

        Ad "I know it must have been much harder for him than it was for me, but that doesn't mean I got out of it unscathed. I lost my best friend."

        Ad "I blamed myself for a long time, too. I guess I still do. How could I face him, knowing that I could've averted this tragedy so easily?"

        c "I think his own feelings aren't that different."

        Ad think b "How so?"

        c "He also blames himself for not being with her when it happened."

        Ad disappoint b "Because they had to keep their relationship secret."

        c "Yeah."

        Ad "I see."

        Ad sad b "That must be horrible for him."

        c "I think he still hasn't gotten over it."

        Ad disappoint b "I wish I could help him. I really do."

        c "What did you do after it all happened?"

        Ad "For a while, I just felt guilty. But eventually, I realized there are those who have it much worse than myself. I decided to take what I had experienced and to turn it into something positive. That's when I started volunteering at the orphanage."

        Ad normal b "Why just let tragedies be tragedies if I could do something to help?"

        c "I share the same sentiment."

        Ad "How so?"

        c "I came here hoping that I could help humanity."

        Ad think b "Maybe you're not just helping humanity."
        
    else:
        
        $ renpy.pause (5.0)
    
else:
    
    $ renpy.pause (5.0)
    

stop sound fadeout 3.0

c "Here, that should do it. How does it feel?"

Ad normal b "Much better. Maybe with this I can even start practicing again in a day or two."

c "Just be safe."

Ad "Of course."

if persistent.endingsseen > 0:

    if persistent.havemap == True:
        
        c "(Oh, I totally forgot I still have a copy of that map for her.)"
        
        menu:
            
            c "(Should I give her the map?)"
            
            "Yes. {image=image/ui/status/havemap.png}":

                c "By the way, I have something for you."

                Ad think b "Really? What would that be?"

                play sound "fx/paper.wav"
                
                c "Ta-da!"

                Ad "Is that what I think it is?"

                c "If you think that it's a map of the underground building, then yes."

                Ad giggle b "Wow. I really didn't expect that."

                Ad normal b "How'd you get it?"

                c "Let's just say I had a chance to inspect it alone, and there was no one between me and the copier to stop me."

                Ad "That's amazing. You know people could get into big trouble for this, right?"

                c "Well, it's yours now. Do with it whatever you want."

                Ad think b "I guess I will."

                c "I have to warn you, though."

                Ad "What about?"

                c "You might have heard about the water pockets surrounding the building. Any kind of disturbance could be fatal for any prospective explorers."

                Ad normal b "I heard about that. Is it really as bad as they say?"

                c "Yes, it is. I'd be careful if I were you. Or at least wait until they have taken care of the water pockets, so there is no danger if you decide to pay it a visit."

                Ad "Alright. It'll be a while until I get a chance to visit, anyway. All my free time right now will go towards practicing for the competition."

                c "I see."
    
                #$ adinestatus = "good"
                
                $ adinegoodending = True
                
                $ persistent.havemap = False
                
                $ gaveadinemap = True
                
            "No.":
                
                pass
            
            
else:
    
    pass
    

Ad "Well, thanks for the help with the bandage. And sorry about cutting practice short today. I guess you didn't get to see any proper aerobatics after all."

c "It's no big deal. Your health is more important."

if adine3mood <= 2:
    
    Ad "Thanks for coming, at any rate."

    c "You're welcome."

    c "I guess I'll leave you to recuperate now, and maybe I'll see you next time."

    Ad "Sure thing! Bye!"

    $ persistent.adine3skip = True

    hide adine with dissolve

    stop music fadeout 2.0
        
    $ renpy.pause (0.5)
        
    $ adinestatus = "neutral"

    $ adinescenesfinished = 3
        
    if chapter4unplayed == False:
                        
        jump chapter4chars
            
    elif chapter3unplayed == False:
            
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
            
else:
    
    Ad "Are you going to come to the show?"

    c "If I can, sure."

    Ad disappoint b "Oh, right. You might be busy."

    c "I'll have to see if I can make it. I'd love to be at the show, though."

    Ad normal b "I'll contact you later with all the details, and we can figure it out from there."

    c "Sounds good."

    Ad "I'll see you next time, then."

    c "See you."

    $ persistent.adine3skip = True

    hide adine with dissolve

    stop music fadeout 2.0
        
    $ renpy.pause (0.5)
        
    $ adinestatus = "good"

    $ adinescenesfinished = 3
        
    if chapter4unplayed == False:
                        
        jump chapter4chars
            
    elif chapter3unplayed == False:
            
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
label lorem3:
    
$ lorem3unplayed = False
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Lorem 3"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Lorem 3"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Lorem 3"
    
else:

    $ save_name = "Chapter 1 - Lorem 3"

scene black with dissolvemed
$ renpy.pause (0.5)
scene o4 at Pan((0, 250), (0, 250), 0.1) with dissolvemed

$ renpy.pause (0.3)

play sound "fx/door/doorbell.wav"
$ renpy.pause(3.0)

stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

show lorem normal with dissolve

if persistent.lorem3skip == True:

    stop music fadeout 1.0
    
    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_59

    call skiptut from _call_skiptut_13
        
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
            call skipcheck from _call_skipcheck_13

            scene forest2 at Pan ((0, 0), (0,0), 0.0)

            show lorem normal 
            
            with dissolveslow

            play music "mx/sprite.ogg" fadein 2.0
            
            jump lorem3skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            #play music "mx/adine3.ogg" fadein 2.0

play music "mx/sprite.ogg" fadein 2.0

c "Hey, Lorem."

Lo "Hey, [player_name]."

c "So, where exactly are we going? You mentioned something about treasure hunting, but don't tell me we're actally trying to unearth some ancient human artifacts."

Lo happy "Don't worry. This is going to be fun!"

c "I'll just hope for the best."

Lo normal "I'm not sure who came up with it, but someone gave this kit to me as a present a few months ago."

m "He showed me the map. It was a piece of paper that had obviously been treated to look much older than it really was."

menu:

    "Doesn't look like much.":

        $ renpy.pause (0.5)

        Lo think "Well, it's a map and instructions. What more do you need?"

    "Sounds like fun.":

        $ renpy.pause (0.5)

        Lo happy "I'm glad you agree."


c "I’m not sure if I can be of much assistance though. I don’t exactly know much about the area."

Lo normal "But you're big and strong!" 

Lo think "Or, at least, you are bigg{i}er{/i} and strong{i}er{/i} than I am."

Lo happy "You can do the digging."

c "Great."

Lo normal "Besides, I've wanted to do this for a while now and Ipsum is always busy, so I figured this would be as good a time as any."

c "Do we need to bring a shovel, or do you expect me to dig with my bare hands?"

Lo think "Well, the instructions say we only need this map and a pen."

menu:

    "I've got a pen.":
        
        $ renpy.pause (0.5)


    "What about ourselves?":

        $ renpy.pause (0.5)

        Lo relieved "I think that one's a given."

    "Alright.":
        
        $ renpy.pause (0.5)



Lo happy "Great, then we're all set."

c "So, where are we supposed to go?"

Lo think "If this is the facility, then the place indicated is... the school. Or, rather, somewhere between the school and the administrative building."

c "Let's go, then."

play sound "fx/steps/clean2.wav"

scene black with fade

$ renpy.pause (1.0)

scene school at Pan ((0, 0), (0, 360), 8.0) with dissolveslow

$ renpy.pause (6.5)

show lorem normal with dissolve

Lo happy "Here we are. The X on the map is right between these two buildings, so it must be around here somewhere."

c "Back to school, huh?"

Lo normal "Not quite yet. Everyone's on summer break right now."

Lo happy "Which is a good thing, because we really wouldn't want you to get swarmed by all the children. They would go crazy if they saw you."

c "How does school work here, anyway?"

Lo think "Are you talking about this one, or schools in general?"

c "In general. I'd like to know more about how your school system works as a whole."

Lo normal "I see you won't let a learning opportunity go by."

c "I'm just doing my job."

Lo happy "You should start looking for that treasure, then."

c "Sure."

m "While I looked for hints as to the treasure’s whereabouts, Lorem started talking."

Lo think "Right. We do have quite the education system. Different schools and districts run on their own, so when looking at details, things can vary a lot. However, there are a few things that are true no matter which region you are in."

Lo normal "Compulsory education lasts for about 10 years. There are a lot of options for schools and school systems."

Lo happy "Choice is an important factor here. We recognize that there isn't one system that works best for everyone, so there are many options depending on what path you want to take."

c "That doesn't sound too different from what it used to be like in my world, but nowadays things are a bit more chaotic."

c "Practical skills are valued most in our city, and you aren't really given a choice to do anything else. Sure, people can learn other things on their own, but it's not as if school is mandatory anymore."

c "People just do whatever they feel like."

Lo think "Did you grow up like that, too?"

c "No, I still got to experience our old education system - college included."

Lo normal "What was your favorite subject?"

menu:

    "Math.":
        
        $ renpy.pause (0.5)

        Lo think "I see."

        Lo normal "My favorite was art class."

        Lo happy "Trying out different mediums was always so much fun."


    "Art.":

        $ renpy.pause (0.5)

        Lo happy "Really? Me too. I always liked trying out different mediums."

    "Physical Education.":

        $ renpy.pause (0.5)

        Lo think "I see."

        Lo normal "My favorite was art class."

        Lo happy "Trying out different mediums was always so much fun."


Lo normal "I tried sculpting again recently." 

c "What for?"

Lo relieved "Art doesn't need a justification."

Lo normal "But, anyway, it helps me visualize what the characters in my game should look like."

c "Can't you do that with a computer?"

Lo "Sure, but working with a physical medium makes things easier for me. Instead of working with an interface, there's only my hands and a lump of clay. No technological gadgets required."

c "I see."

Lo think "Did you find anything yet? I sure haven't."

c "No. I feel like we must be missing something."

Lo "Maybe, but the map clearly marked this place. You can see it for yourself."

c "Yeah, the X definitely points to this alley."

Lo normal "Then it must be here somewhere."

$ lorem3trough = False
$ lorem3windows = False

label lorem3searchmenu:

menu:

    "Look inside the windows." if lorem3windows == False:

        c "Maybe it has something to do with the windows."

        Lo think "You think so?"

        c "It's as good a guess as any."

        Lo normal "I suppose..."

        c "You can fly, right?"

        Lo happy "Sure."

        c "Okay, you check out the windows on the left. You should get a better view inside if you fly up to them."

        Lo normal "Alright."
        
        hide lorem with dissolve
        
        play sound "fx/flap1.ogg"

        m "As Lorem flew up to the windowsill with a few flaps of his wings, I turned to the right to look inside the windows of the administrative building."

        m "The curtains were closed, but through a small gap, I could barely see inside."

        m "I got closer and closer, hoping to get a better view when my forehead bumped into the glass with a dull thud."

        m "I heard some movement behind the curtains. Suddenly, they were drawn open to reveal a black dragoness who looked down on me with disapproval."

        m "In an instant, her expression changed to one of shock and surprise. Before anything else could happen, I quickly stepped away from the window and outside her view."
        
        show lorem normal with dissolve

        Lo "Just empty classrooms on my side." 
        
        Lo think "Did you find anything?"

        c "Nothing."

        $ lorem3windows = True
        
        show lorem normal with dissolve
        
        jump lorem3searchmenu

    "Investigate the water trough." if lorem3trough == False:

        c "Maybe it has something to do with the water trough and the faucets."

        Lo normal "Maybe. Let's check it out."

        m "We walked over and looked inside the water trough. Inside, the dirt was already a few inches high - a clear indicator that it hadn't been cleaned for a while."

        Lo think "I guess the janitor is on summer break, too."

        c "Or maybe they left it here on purpose because our treasure is inside."

        Lo "It's all dried up, though. Way too hard to start digging."

        c "Maybe that's what the faucets are for."

        Lo normal "If you say so."

        play soundloop "fx/faucet1.ogg"
        
        queue soundloop "fx/faucet2.ogg"

        m "We turned on the faucets and watched as the trough slowly filled with water."

        stop soundloop fadeout 5.0

        Lo think "That should be enough."

        c "And now?"

        Lo normal "We start digging."

        c "..."

        Lo happy "Come on, what kind of treasure hunters would we be if we didn't get our hands dirty?"
        
        play sound "fx/mud.ogg"

        m "I immersed my hands in the sludge."

        c "This is still pretty hard."
        
        stop sound fadeout 2.0

        Lo think "Let's turn on the water again, then."

        play soundloop "fx/faucet1.ogg"
        
        queue soundloop "fx/faucet2.ogg"
        
        show lorem normal with dissolve

        m "Lorem joined me. Both of us dug around in the sludge, which slowly became clearer as more water filled the trough."
        
        Lo happy "Hey, I think I've got something?"

        c "Really?"

        Lo think "Yeah, I think it's stuck to the bottom."

        m "Lorem's face was straining as he tried to pull harder and harder on the object he had found."

        c "Maybe I should try?"

        Lo "I think I got it."

        play sound "fx/splash.wav"

        m "Suddenly, his hands reappeared from beneath the murky water, holding a small, shiny object in their grasp."

        Lo happy "There it is."

        c "What is it?"

        m "He opened his hands to reveal a big screw."

        Lo relieved "Oh."

        c "Maybe you should put that back."

        Lo normal "Yeah, maybe."

        m "By now the water had become clear enough that we could see where the screw originally was."

        m "After Lorem replaced it, we noticed that – besides the water – the trough was completely empty."
        
        stop soundloop fadeout 5.0

        c "I guess it's not here after all."

        Lo think "But at least the janitor will be grateful for the cleaning."

        c "Maybe."

        $ lorem3trough = True
        
        show lorem normal with dissolve
        
        jump lorem3searchmenu

    "Examine the walls.":
        
        pass

c "Maybe it has something to do with the walls."

Lo think "What makes you think so?"

c "We're clearly missing something here, so maybe there is some sort of hint we've been overlooking."

c "Something that wouldn't be obvious to anyone else who came through here."

Lo "I have no idea what you're talking about. These walls don't really look special to me."

m "My gaze slowly went along the walls, trying to find something, anything that could have a hidden meaning."

c "Hey, look at that."

Lo normal "What do you mean?"

c "That kinda looks like an X on the wall, don't you think?"

Lo think "I guess so."

c "Maybe it's here somewhere."

Lo happy "Look, there!"

hide lorem with dissolve

m "Lorem crouched down and stuck his hand in an indentation that ran along the wall near the ground." 

show lorem happy with dissolve

Lo "A-ha!"

c "What is it?"

m "He pulled out a cylindrical, shiny object and held it up to me."

Lo normal "It looks like some sort of capsule. Maybe there's something inside."

c "That's going to be a pretty small treasure."

play sound "fx/screwopen.ogg"

m "He screwed it open and held the two halves of the cylindrical object in his hands. To our surprise, it didn't have any empty space on the inside – nothing could be hidden within."

m "Instead, the inside of the two halves were engraved."

c "What does it say?"

Lo think "2J."

c "That's it?"

Lo normal "Yep. It's also on the other half."

c "It might be coordinates."

Lo think "The grid on the map had numbers and letters like that."

play sound "fx/map.ogg"

Lo normal "That means 2J would be... here."

c "Right in the middle of a forest."

Lo happy "Let's go."

scene black with dissolvemed

$ renpy.pause (1.0)

scene forest1 at Pan ((0, 360), (0,0), 8.0) with dissolveslow

$ renpy.pause (6.5)

c "Finding our spot might be a bit more difficult from here on out."

show lorem think with dissolve

Lo "Why is that?"

c "We don't really have buildings and addresses as reference anymore. Here we only have a spot in the middle of a forest."

Lo happy "Don't worry, I have an excellent sense of navigation."

Lo think "Let's hope we find it before it gets too dark, though - or things might become a lot more complicated."

c "I'd rather not get lost here."

Lo normal "You won't have to worry about anything. If there are any predators in the area, they'll see me as a better target than you."

c "Don't tell me there are predators in these woods."

Lo happy "Not really. There might be a stray or two, but that should be it. These woods are considered to be very safe."

c "Even if that's true and if worse comes to worst, you can just fly away."

Lo relieved "I guess that's true."

Lo think "You kinda sound like you don't like the woods, though."

menu:

    "I like going for walks in the woods, as long as it's safe.":

        $ renpy.pause (0.5)

        Lo happy "Then you don't have anything to worry about here."

    "They're creepy.":

        $ renpy.pause (0.5)

        Lo relieved "You don't have anything to worry about."



Lo normal "I already told you, there shouldn't really be any predators in these parts."

Lo happy "And it's not like these woods are haunted or anything."

c "Haunted? That reminds me of something..."

Lo think "What is it?"

c "Maybe you'll be interested in this. In our world, there is a forest that was notorious for the many suicides that took place there. It was said to be haunted by angry spirits."

Lo relieved "That sounds horrible."

Lo think "But why are there so many suicides there? And why are the spirits so angry?"

c "Well, in Japanese folklore, people have a soul or spirit that is called {i}reikon{/i}."

c "Upon a person's death, the reikon separates from the body and goes to a form of purgatory."

c "After certain rites have been performed, the reikon then goes on to join its ancestors and becomes a protector of the living family."

c "However, under certain circumstances - like the rites not being performed correctly or dying in a sudden or violent manner - the reikon transforms into a {i}yūrei{/i} instead."

c "The yūrei can return to the physical world and haunts it until it has been laid to rest."

c "So, there you go. Another myth for your collection."

Lo relieved "Well, I know where not to go for my next vacation now."

menu:

    "It's just a myth, anyway.":

        $ renpy.pause (0.5)

        Lo normal "I suppose..."

    "I wouldn't want to visit either.":

        $ renpy.pause (0.5)

        Lo normal "That makes two of us."



c "What do you think about stuff like that?"

Lo think "Paranormal stuff?"

Lo normal "You know, until a few weeks ago, humans were still just a myth."

Lo think "And if we look at the portal, it's like... something that came out of science fiction."

c "Ipsum certainly seemed interested in it."

Lo normal "He is. He actually read up on some new theories about it."

c "Like what?"

Lo think "You remember him telling you about the different branches and how the barrier separates them, right?"

c "Yeah."

Lo normal "So, since the barrier is made up of wormholes and using the portal displaces them, it leaves gaps in the barrier."

c "I distinctly remember him talking about something like that."

Lo "Through these gaps, he thinks we can communicate with our alternate selves in the other timelines."

c "How does that work?"

Lo happy "It all goes into the nature of existence itself."

Lo think "Who are you as a person? Do you think you are just the [player_name] from this branch? What about the ones from all the other timelines who have made other decisions?"

Lo "Would you consider yourself to be the same person as them? The only difference between you and the [player_name] from another branch may be that you decided to skip breakfast this morning."

Lo normal "Maybe you are all of them."

c "How is that possible?"

Lo happy "Like a seed from which many roots can sprout, or a tree and its branches, there may be a uniting factor that branched off into these different timelines - your fundamental nature."

Lo normal "You might call it a soul or something similar, but the idea is that even though there are many different versions of you, there is an aspect that unites all of you."

c "A part of myself that stands over me? Kinda like a super-ego?"

Lo think "An interesting comparison."

Lo normal "If we use a similar model here, then we can say that you are also made up of three distinct parts."

Lo "In each timeline, you have a physical body which is driven by its own base desires that it seeks to fulfill. All physical needs like hunger, thirst and even breathing fall under this category."

Lo "However, as a being with free will you are also capable of making your own decisions. That includes being able to act contrary to what your body is telling you."

Lo think "This ability to think and make decisions on your own is your rational mind - the self."

Lo normal "And lastly, there is the third part I just talked about. The one that stands above all of you and unites you in some way. Let's call this your {i}higher self{/i}."

Lo "Through this higher self, you may be able to communicate with your alternate selves in some way." 

Lo "Usually the barrier would prevent this, but through the gaps, communication becomes a possibility. The more gaps there are, the easier this should be."

c "And how would I go about doing that?"

Lo think "I suppose that would be the job of the higher self."

c "So I can't control it?"

Lo normal "These are all just theories. We wouldn’t really know until it happened. Only then could we study it."

c "If it was to happen, how would I know?"

Lo happy "If someone else's experience gets relayed through this connection to you, it could manifest in a number of ways."

Lo think "Maybe it could be something like a déjà vu, or a false memory. Maybe even dreams."

Lo normal "But the biggest difficulty would be to recognize that this phenomenon is happening in the first place." 

c "It's certainly quite out there, you have to admit."

Lo happy "Sure, but quantum mechanics are already complicated enough. Once you look at what lies beyond, it's just crazy territory."

c "What do you think about all this?"

Lo think "I think it might already be happening."

c "Really?"

Lo "Just think about it. If the possbility of it ever happening is there, then it's more than likely that it already has."

c "I'm not sure I follow."

Lo normal "Let us assume that this is an average timeline. The portals have been found by both of our people, contact has been made and now you and Reza are both here for a visit."

Lo "A few letters were exchanged before you and Reza were sent here, so that means the portal has already been used a few times."

Lo happy "Using a portal once might only have an infinitely small effect on the barrier, like poking a hole in a castle wall with a needle."

Lo think "However, if you multiply this by a nearly infinite number of possible timelines in which these same events have happened, the effects must already be noticable." 

Lo normal "Of course, some people may be more susceptible to this than others."

c "Do you think you've already experienced it?"

Lo sad "I don't know. I've been having some weird dreams lately."

menu:

    "Dreams can always be weird, though.":

        Lo "I know. It's just... I don't know."

    "Me too.":

        $ renpy.pause (0.5)

        Lo think "Really?"


scene black with dissolve

$ renpy.pause (0.5)

scene forest2 with dissolvemed

m "We were just entering a clearing, and from my view, I could see some odd lines that had been drawn on the ground."

c "Hey, I think this is the spot."

show lorem think with dissolve

Lo "Why do you think so?"

c "Well, the giant X on the ground kinda gives it away."

play sound "fx/flap1.ogg"

hide lorem with dissolve

m "Lorem took flight with a few flaps of his wings. After looking at the scenery from above, he returned to me."

show lorem happy with dissolve

Lo "You're right, it does look like a giant X."

if lorem3trough == True:
    
    c "Guess it's time to get our hands dirty again."

    Lo normal "That may not be necessary this time." 
    
else:
    
    c "Guess it's time to get our hands dirty."

    Lo normal "That may not be necessary."


c "What are you talking about?"

hide lorem with dissolve

m "He went to the center where the lines crossed and picked up an object that was lodged halfway into the ground. He returned to me once more, holding another capsule similar to the one we had found near the school."

show lorem normal with dissolve

c "If we have to go back to town after walking all this way, I’ll..."

play sound "fx/screwopen.ogg"

show lorem think with dissolve

$ renpy.pause (1.5)

Lo "And it's open. Apparently we're going to 6K now."

c "And where is that?"

Lo normal "There is an abandoned store on the other side of the forest. That's where we're going."

c "That just means the way back is going to be even longer."

scene black with dissolvemed

$ renpy.pause (0.5)

scene storex at Pan ((0, 0), (0,184), 5.0) with dissolveslow

$ renpy.pause (3.5)

c "Are you sure we should even be here?"

show lorem normal with dissolve

Lo "This is the place indicated by the map."

c "I was talking about the building being roped off..."

Lo think "Maybe that's just part of the game."

c "Is the flooding part of the game too?"

Lo normal "Hey, you can give up if you want to. I certainly won't."

Lo think "Now, are you going to help me or not?"

c "I guess..."

c "I just didn't expect that I'd have to get wet for this."

Lo happy "All part of being a treasure hunter."

c "Let's just look for the X."

Lo normal "Sure."

play sound "fx/flap1.ogg"

hide lorem with dissolve

m "Lorem flew up to the light fixtures to get a view from above while I checked out the shelves."

show lorem think with dissolve

Lo "I remember when we could still shop here."

c "What happened?"

Lo relieved "Apparently, the area has a problem with flooding."

c "I can see that."

Lo think "So much work and resources are needed to erect a building like this one, and in the end it just gets abandoned."

c "We have plenty of empty buildings where I come from."

Lo "Oh really? Not sure this is a good reminder of home, though."

c "At least we don't have a problem with flooding."

Lo relieved "..."

c "I nearly got sent back, by the way."

Lo think "Really? Why?"

c "Political reasons. Oh, I don't think I'm supposed to talk about it."

Lo normal "You just did."

Lo think "Is it related to that announcement they made about Reza?"

c "Maybe."

Lo "Huh, guess things are pretty serious."

c "They are."

Lo sad "..."

Lo think "Have you found anything yet?"

c "Not really."

Lo normal "Maybe it's underwater."

c "You think so?"

Lo "It's certainly not anywhere near the ceiling, I already checked there."

c "And I found nothing near the walls or the shelves."

Lo "It could be hidden beneath a floor tile or something like that."

c "I suppose you're right."

Lo normal "Let's do it."

menu:

    "Alright.":
        
        pass

    "If I have to...":

        pass

$ renpy.pause (0.5)

play sound "fx/splash.wav"

hide lorem with dissolve

m "Without hesitation, Lorem vanished beneath the water's surface."

m "I breathed in deeply, crouched down and began looking underwater as well."

scene black with dissolvemed

play soundloop "fx/underwater.ogg" fadein 2.0

show underwater at Pan ((540, 0), (540, 304), 7.0) with dissolveslow

$ renpy.pause (5.5)

m "I looked around, but nothing seemed out of the ordinary to me." 


play sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/underwatercrash.ogg"

m "Just as I was about to resurface and get some air, I heard a splash accompanied by a loud thud."

scene black with dissolve

play sound "fx/splash.wav"

scene storex at Pan ((0, 184), (0,184), 0.0) with dissolvemed

c "(What was that?)"

c "Lorem?"

m "Everything was quiet as I looked around for my companion."

play soundloop "fx/loremknocks.ogg"

m "Suddenly, I heard frantic knocks coming from a shelf that was lying on the ground, half submerged in the water. I realized that it was still standing when we came in earlier."

play sound "fx/wading.ogg"

m "As I waded over to it, it soon became clear that the knocks where coming from beneath."

stop soundloop fadeout 2.0

stop sound fadeout 1.0

c "Lorem?"

play sound "fx/racksplash.ogg"

m "Quickly, I mustered all my strength and grabbed the shelf, lifting it up until it fell over to the other side with a loud splash."

play sound2 "fx/splash.wav"

show lorem relieved with dissolve

m "Lorem resurfaced, gasping for breath."

c "What just happened?"

Lo "I was looking underwater and suddenly the shelf just came down on top of me."

c "Are you okay?"

Lo think "Yeah, I think so. My leg hurts a bit, but that's about it."

Lo happy "But I totally saw something. Let me show you."

play sound "fx/splash.wav"

hide lorem with dissolve

m "Without waiting for a reply, Lorem dove down into the water again, resurfacing just a few seconds later holding an ominous metal box that had a large X on it."

#play sound "fx/splash.wav"

show lorem happy with dissolve

Lo "This should be it."

c "Let's hope it's waterproof, though."

play sound "fx/metalbox.ogg"

$ renpy.pause (1.0)

Lo normal "From the looks of it, it is."

Lo think "We should go outside, though. It'll be hard to read anything in here."

c "Sure."

scene black with dissolvemed

$ renpy.pause (0.5)

scene forest2 with dissolveslow

$ renpy.pause (0.3)

c "Well, what's inside?"

show lorem normal with dissolve

m "Lorem held up the box to me. I took one of the sheets of paper that were inside and started reading."

play sound "fx/paper.wav"

c "I think these are pizza vouchers."

m "Lorem was holding another sheet which he started reading aloud."

Lo happy "{i}Congratulations! You have solved Pantoli Pizza's annual treasure hunt. Remember the code word enclosed for an instant rebate on your next order and a chance for the grand prize.{/i}"

Lo "{i}You could be the lucky winner for a year's supply of Pantoli's Pizza. This competition will run until...{/i}"

Lo relieved "Oh."

c "What is it?"

Lo "It's expired. The treasure hunt, the contest - apparently it all ended months ago."

c "..."

c "Can we still get the pizza?"

Lo think "Well, I don't think that offer is still valid."

c "I mean, we could still get pizza regardless. This whole thing has made me really hungry."

Lo normal "I suppose this concludes our treasure hunt."

c "What do we do now?"

Lo happy "Maybe we could see this experience as another reminder that the journey is its own reward."

c "Or that the early bird gets the worm."

Lo relieved "You really want some pizza, don't you?"

c "That makes me wonder, though. Why didn't they get rid of the hints and this box when the contest expired?"

Lo normal "They must've realized that people may still have these kits at home, even when the contest is over. If people went out looking for a hint in the woods and it wasn't there anymore, they might look for hours until they decided there was nothing to find."

c "Or they just didn't care. You know, I'm slowly starting to lose hope in Pantoli's Pizza."

c "Sending us here is really negligent. Who knows what would've happened to you if I wasn't here."

c "Maybe this whole building could crash down on the next unlucky people who end up here."

label lorem3skip:

Lo think "Maybe that's why it was roped off in the first place."

c "But you thought it was part of the game. Maybe they should've put up a sign or something."

hide lorem with dissolve

m "While I was talking, Lorem walked towards one of the wooden poles that was used to rope off the building."

m "He picked up a large rectangular object from the ground that was hidden in the grass. It was a wooden sign."

show lorem think with dissolve

Lo "{i}Warning! Do not proceed past this point. The treasure hunt has concluded and there is nothing more to find. Danger ahead!{/i}"

c "We could find the treasure, but not this huge sign? What does that say about us?"

Lo relieved "I'm not sure, exactly."

Lo think "We should probably head back before it gets too dark, though. We still have to go through the woods again."

c "Alright, let's go."

Lo normal "Do you want to pick up some pizza on the way home?"

c "I don't know."

$ persistent.lorem3skip = True

stop music fadeout 2.0
    
$ renpy.pause (1.0)
    
$ loremstatus = "good"

$ loremscenesfinished = 3
    
if chapter4unplayed == False:
                    
    jump chapter4chars
        
elif chapter3unplayed == False:
        
    jump chapter3chars
    
elif chapter2unplayed == False:
    
    jump chapter2chars
    
else:

    jump chapter1chars




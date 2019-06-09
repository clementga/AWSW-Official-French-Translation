#-9 - +10
label anna2:

#$ chapter2csplayed += 1
$ anna2unplayed = False
$ anna2mood = 0
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Anna 2"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Anna 2"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Anna 2"
    
else:

    $ save_name = "Chapter 1 - Anna 2"

scene black with fade
$ renpy.pause (1.0)
#scene facin2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

scene facin2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow
    
play music "mx/cruising.ogg"

c "(And just on time. Now, where is she?)"
    
play sound "fx/knocking1.ogg"

c "Hello?"

c "(What's this? Looks like a message.)"
    
m "Something came up at the last second. \nWait for me, it shouldn't be too long. \nAnna."

c "(I guess \"at the last second\" is meant in a literal sense here, or else she could've just called me.)"

c "(Guess we're playing the waiting game, then.)"

scene black with dissolvemed
$ renpy.pause (0.5)
scene facinx at Pan ((128, 250), (128, 250), 0.0) with dissolvemed

c "(Okay, it's been like an hour and my patience is slowly, but surely running out.)"

menu:
    
    "Go home.":
        
        m "In the end, I decided that enough was enough. Not wanting to wait any longer, I left, even though she still owed me that date."

        $ annastatus = "bad"

        $ annascenesfinished = 2
        
        stop music fadeout 2.0

        if chapter4unplayed == False:
        
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
            
    "Wait.":
        
        c "(I've already waited this long, so guess I can wait a little longer...)"

        #scene facin2 at Pan ((128, 250), (128, 250), 0.0) with fade

        scene black with dissolvemed
        $ renpy.pause (1.0)
        scene facin3 at Pan ((128, 250), (128, 250), 0.0) with dissolvemed

        c "(I'm not sure who the world record holder for \"most patient person\" is, but now I feel like a contender.)"

        c "(Still no sign of her, though.)"


menu:
    
    "Go home.":
        
        m "In the end, I decided that enough was enough. Not wanting to wait any longer, I left, even though she still owed me that date."

        $ annastatus = "bad"
        
        $ annascenesfinished = 2
        
        stop music fadeout 2.0

        if chapter4unplayed == False:
        
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
            
    "Wait.":
        
        c "(Well, if she doesn't show up soon, I'm done.)"
        
        show anna normal with dissolve
        
        c "There you are. Where have you been all this time?"
            

    "Try to get into her lab.":
        
        c "(Alright, I'm gonna score myself some sweet lab equipment. That's the least she can do for making me wait.)"
        
        c "(Or maybe I'll just wait inside. Standing around here is getting rather tedious.)"

        play sound "fx/knobrattle.ogg"
        
        $ renpy.pause (1.0)

        c "(Hmm, pushing the door does nothing. Neither does pulling.)"

        c "(Guess I'm out of options here.)"
        
        c "(Hey, what's this?)"
        
        m "At the bottom of the door, the corner of an envelope was noticably sticking out."
        
        menu: 
            
            "Take it.":
                
                m "Pulling at the corner, I was now holding the envelope in my hands."
                
                c "(Well, I gotta pass the time somehow, right?)"
                
                play sound "fx/paper.wav"
                
                $ renpy.pause (0.5)
                
                c "(Let's see... Dear Anna... appointments for the next month... treatment plan... Dr. Valedo...)"
                
                c "(I probably shouldn't be looking at this.)"
                
                play sound "fx/paper2.ogg"
                
                m "Quickly, I put the letter back into the envelope and pushed it through the gap in the door."
                
                if persistent.heardaboutcancerenvelope == False:
                    
                    $ persistent.heardaboutcancer = True

                    $ persistent.heardaboutcancerenvelope = True
                    
                    $ achievement.grant("Snoop")
                    
                    $ persistent.achievements += 1
                    
                    call syscheck from _call_syscheck_110
                    
                    play sound "fx/system.wav"
                    
                    if system == "normal":
                    
                        s "You looked at Anna's envelope! {image=image/ui/status/heardaboutcancer.png}"
                        
                    elif system == "advanced":

                        s "You looked at Anna's envelope. Naughty. {image=image/ui/status/heardaboutcancer.png}"
                        
                    else:
                        
                        s "You looked at Anna's envelope. Better not let her catch you. {image=image/ui/status/heardaboutcancer.png}"
                
                

                show anna normal with dissolve
                
                An "What are you looking at?"
        
                c "Your beautiful door. Where have you been all this time?"
                
                
            "Leave it.":
                
                $ renpy.pause (0.5)
        
                show anna normal with dissolve
                
                An "What are you looking at?"
        
                c "Your beautiful door. Where have you been all this time?"

        
#show anna normal with dissolve

An "Reading comprehension must not be your strong suit, because my note clearly said I'd be back soon."

c "Note to self: The word \"soon\" now refers to a time span of over 2 hours when waiting for a scheduled appointment."

An sad "Has it really been that long?"

An face "It certainly didn't feel like it."
        
        

#insert skip here

if persistent.anna2skip == True:

    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_111

    call skiptut from _call_skiptut_32
        
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
            call skipcheck from _call_skipcheck_32
            
            scene facin3 at Pan ((128, 250), (128, 250), 0.0) with dissolvemed

            show anna normal with dissolve

            $ anna2mood = 5
                        
            play music "mx/cruising.ogg" fadein 1.0
            
            jump anna2skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/cruising.ogg"

An sad "Alright, sorry for making you wait."

menu:
    
    "You better be.":

        $ renpy.pause (0.5)
        
        An disgust "I just told you that I am, so get off my back. Do you want this date now or not?"

        c "I suppose so."
        
        $ anna2mood -=1
        
        show anna sad with dissolve
        
        
    "Let's just go.":
        
        pass
        
        #$ renpy.pause (0.5)
        
        #show anna sad with dissolve
        
    "Losing track of time happens to the best of us.":

        #$ renpy.pause (0.5)

        An "It happens to me all the time."

        $ anna2mood +=1
        

An "I guess we missed our movie."

c "Can't we see the late screening or something?"

An face "That was the late screening. The theater's closed now."

c "Maybe we should reschedule."

An sad "That won't work. At least not for me."

An face "Today was the only day I could leave early. I won't have another chance any time soon."

c "So, what do we do now?"

An sad "Maybe the coffee place is still open. I don't know."

c "I guess that's better than nothing."

scene black with dissolve
$ renpy.pause (0.5)
scene alley with dissolveslow

show anna normal with dissolve
show anna face with dissolve

An "Closed as well."

c "That's just peachy."

c "Why do you keep working so late, anyway?" 

An "Because what I'm doing is important."

if chap2facres2 == False:

    c "You're doing cancer research, right?"

    An disgust "And who told you that?"

    c "Damion. I stopped by your lab some time ago, but you weren't there."

    An rage "That shard-borne bastard! What else did he tell you about me?"

    c "Nothing much. The whole thing wasn't really about you, anyway."

    An sad "I see..."

    c "Sounds like you two don't get along that well."

    An face "That's the understatement of the century. Being trapped in a small room with the likes of him for hours on end every day is a scenario born of a sick mind with the intention of making me suffer as much as possible. It certainly doesn't make my research any easier."

    c "The stress probably doesn't help you either, and it's not worth jeopardizing your health over. Don't overwork yourself. You can't save anyone if you're dead."

    An sad "If I don't find a cure, no one else will. No one else can."
    
else:

    c "I understand wanting to see things through to completion. How long have you been working on your current project?" 

    An sad "Not long enough to finish it."

    c "That's not good. You're going to burn yourself out."

    An face "So what?"

    c "Is your work really worth jeopardizing your health over? You're not going to help anyone if you're dead."

    An sad "If I don't finish this, no one else will. No one else can."
    

if blood == True:
    
    if gotresultsviapost == True:
        
        pass
        
    else:
    
        An face "Besides, I was only late today because I got your stupid blood work ready."

        c "You have the test results?"

        An normal "Yeah. Want to know what I have to say about them?"

        c "Definitely."

        An "Okay, how much do you know about genetics?"

        c "A little bit, I guess."

        An "Don't worry, I'll put it into words that are easy for you to understand."

        An "To start off, I've found that, on average, about 90%% of your genes are homologous to our species' genes."

        An "That may seem like a lot, but to put it into perspective, about 50%% of your DNA is also shared with fruit."

        An "To further elaborate, you and your human neighbor back home are probably around 99.9%% genetically similar. If you compared the various sentient species we have here to each other, they would only be around 95-97%% similar."

        An "As for what exactly all of this tells us..."

        An "Although a match of 90%% sounds like a lot, it's not as much as you might think. Still, for two beings from a different world altogether, that's quite remarkable."

        An smirk "Beyond DNA, the biggest similarity between us is within the brain structure, but that's not surprising, considering our high-level cognitive abilities."

        c "That'll surprise Maverick."

        An normal "What do you mean?"

        c "He doesn't seem to like humans very much. I'm sure he'll be displeased to know how similar we are."
        
        An "Oh, he doesn't like anyone, really. He's just like me in that way."

        c "Yeah, you two would make a great couple."

        An smirk "You're a little late for that. I'm already his ex-girlfriend."

        c "Really? How did that go?"

        An normal "Not how you might think. It actually went pretty well. For a while, at least."

        An "But in the end, we both got too absorbed in our jobs until we realized we had drifted apart too much and agreed it would be better if we just broke up."

        An "I still respect him for the work he does. I mean, we even used to solve crime together. I'd be in the lab, running tests, and he'd be out on the field, chasing after the perps. Those were good times."

        c "I guess nowadays he just chases after me."

        An face "What?"

        c "I don't know, maybe I shouldn't say that. But if you know him, maybe you can help me out."

        An normal "I certainly can't help you if you don't tell me what's going on."

        c "Okay, but this is just between us, alright?"

        An face "Sure, whatever."

        c "Maverick is convinced that I'm the accomplice of a crime. He made a point to tell me that he's searching for proof to legally arrest me, or worse."

        An normal "Oh, I wouldn't worry about that."

        c "Really?"

        An "It's nothing. He can't find any proof that doesn't exist."

        c "Still, it doesn't feel nice to be threatened and stalked, especially by someone like him."

        An "That's just him. He gets way too into it once he sets his sights on something."

        c "I noticed."

        An face "It's his job. What do you expect?"

        c "I wish he'd just leave me alone."
        
        stop music fadeout 2.0

        An normal "He wasn't always like this, you know."

        An "A couple of years ago, he was assigned to this one case."
        
        scene black with flash

        show maverick nice b gray with dissolveslow
        
        play music "mx/dramatic.ogg" fadein 3.0

        An "He was still relatively new on the force. Young and eager to help. Then reality came crashing down on him."

        An "There was a serial killer who shook up the whole town. The victims were apparently eaten."

        An "We later found out that the killer's actions were the result of a degenerative disease, which brought his feral nature to the foreground."

        An "At that point, he was just a wild animal. Turned into a cannibal that hunted under the shadow of night."

        An "Everyone in town was up in arms, terrified that they'd be next. The police did everything they could. A curfew was instated and patrols guarded the streets at night... And then they found him munching on his fifth victim."

        An "Poor little Maverick was not prepared for what he would find."
        
        scene black with dissolvemed
        $ renpy.pause (2.0)
        
        scene fb gray 
        show bryce stern old b gray at Position(xpos = 0.76)
        show maverick nice b gray at Position(xpos = 0.96)
        with dissolvemed
        
        Br "Stand back, Maverick. I'll handle this."
        
        Mv scared b gray "Miles?"

        An "It was his brother."

        show bryce stern old b gray at Position(xpos = 0.70) with ease

        Br "Step away from the body, Miles."

        An "Miles couldn't comprehend their words, and only saw rivals who wanted to take away his prey."
        
        An "And he wasn't about to just let go of it without a fight."
        
        show miles angry flip gray at Position(xpos = -0.0) with easeinleft
        
        play sound "fx/growl.ogg"

        m "Miles raised his head from his kill, blood dripping from his maw. The officers' breaths were smothered by the deathly stillness of the night. Fangs bared, the feral dragon snarled and stood strong in front of his meal, prepared to protect it from the two who intruded upon his territory."

        Br brow b old gray "Whatever this is, Miles, it's over. Don't make it worse now."
        
        play sound "fx/snarl.ogg"
        
        show miles growl flip gray with dissolve
        
        $ renpy.pause (1.0)

        show miles growl flip gray at Position(xpos = 0.16)
        #show bryce stern b old gray at Position(xpos = 0.6)
        with move6
        
        #show miles growl flip gray at Position(xpos = 0.30)
        #show bryce stern b old gray at Position(xpos = 0.6)
        #with move6
        
        play sound "fx/bite.ogg"
        show miles bite flip gray with dissolvequick
        
        show bite 2 flip gray at Position (xpos = 0.45) #behind maverick
        hide bryce
        hide miles
        with dissolvequick

        $ renpy.pause (0.0)
        
        #hide miles
        #hide bryce
        #with move7outbottom
        
        scene black with dissolvemed

        m "In an instant, Miles was upon Bryce. They clashed in a flurry of teeth and claws. Miles had the advantage with his small frame and quick movements, and Bryce could not get a clear hit in. It all happened so fast that Maverick didn't know what to do."

        m "They rolled on the ground and Bryce ended up on his back, as helpless as a turtle. Miles pinned him and clamped his jaws on his neck."

        play sound "fx/bitescr.ogg"
        
        m "Bryce's claws were the only thing preventing Miles from biting down, and they were slipping, slick with blood and quivering with fatigue, as he tried to push him off."

        m "For a brief moment, Bryce thought he'd meet his end, when the jaws suddenly relaxed and he was able to dislodge them."

        m "When he looked up, he saw that Maverick had managed to get to Miles from behind. He bit through his brother's neck from above."
        
        play sound "fx/squish.ogg"
        
        $ renpy.pause (1.0)

        m "Blood flowed down Maverick's jaws and over Miles' lifeless body. Bryce had been saved, but the young dragon wore a wide-eyed, empty stare."
                
        stop music fadeout 2.0
        
        window hide
        
        $ renpy.pause (2.0)  
             
        scene alley
        show anna normal
        with dissolveslow

        An "Maverick blamed himself for not taking better care of his brother. He knew Miles had problems and was taking medication for it, but he wished he could have done more to help him." 
        
        An "The medication wasn't the right one, by the way."

        An "Maverick takes solace in the fact that he was able to save Bryce, but he's never been the same since that incident. Now, he scrutinizes everyone and everything."

        c "I'm not sure how that's supposed to help me."

        An "It doesn't, but now you know why he is how he is. It's not unusual for him to act like this, so you might just have to wait it out."

        play music "mx/cruising.ogg" fadein 1.0
        
        An "Anyway, let's get back to your test results. Since you were so interested, did you want a copy of them?"
         
        c "Yeah, I'd appreciate that."

        An "No problem."

        c "I heard you also wanted Reza's blood."

        An "Of course. I invited him over too, but that was before you arrived here."

        c "And I thought what we had was special." 

        An smirk "Oh, it is. Reza was too stuck up to agree to anything." 

        c "He wouldn't even participate in an exhilarating round of trivia board games?" 

        An sad "Not even that, can you believe it?" 

        c "I can almost see the sarcasm dripping from your mouth."

        An normal "Still, it's kind of a shame. It would've been interesting to compare your blood to his."

        c "What a shame indeed."
    
    
                
else:
    
    pass


c "Let's just enjoy our romantic date in the back alley of a coffee shop."

An "Of course."

c "Unless you want to take this someplace else."

An smirk "What, you don't like hanging around dirty back alleys?"

menu:
    
    "I'd prefer someplace inside.":
        
        $ renpy.pause (0.5)
        
        An normal "Hey, I bet you've never had a date in an alley before."

        c "I haven't. Not sure I ever wanted to."

        An "Where's your sense of adventure?"

        c "Oh, hang on. There it is. Yes, I can feel the adventure kicking in."
        
        
    "I'd rather be someplace less dirty.":

        $ renpy.pause (0.5)
        
        An normal "I guess that's a valid point."

        c "We could always go back to your lab."

        An "And have you hanging around sensitive lab equipment? Denied."


    "Actually, I do.":

        $ renpy.pause (0.5)

        An normal "Now that's the spirit."


c "I'm getting kinda hungry. I figured we'd be having a meal on our \"date\"."

An face "What, can't you go a few hours without having to stuff your face?"

An normal "I could offer you a handful of dirt, if that's to your taste, [player_name]."

menu:

    "That's gross.":
        
        c "That's gross. How can you even think about doing something like that?"

        An face "I bet you're one of those people who never ate dirt when they were young. That's how you develop allergies."

        c "Can't you think of something else?"

        An normal "Well, there's this one place that never closes. Let's just go there."

        c "Sure."
        
        $ anna2mood -= 1


    "I'll pass.":
        
        An "I'm afraid that's all we have on the menu."

        An "Unless... Well, I know one place that never closes. Let's go there."

        c "Sure."

    "I already have my own dirt." if persistent.dirttaken:
        
        c "Sorry, but I already have my own dirt."

        An smirk "Oh, really? What kind of dirt would that be?"

        c "Only the finest governmentally-funded dirt from Tatsu Park. Your filthy back-alley stuff has nothing on this."

        An normal "You win this round."

        c "Either way, a side dish would be nice."

        An smirk "I know this one place that never closes. Let's go there."

        c "Sure."

        $ mp.dirt = True
        $ mp.save()

        $ anna2mood += 1
        
play sound "fx/steps/clean2.wav"

scene black with dissolvemed

$ renpy.pause (1.0)

scene farm night with dissolvemed

m "After several minutes of walking, Anna led me to the outskirts of town. We arrived at a farm house; on one side, fields stretched toward the horizon, and on the other were lush, green hills with fenced populations of animals."

show anna normal with dissolve

c "What kind of restaurant is this supposed to be?"

An smirk "Self-serve."

menu:
    
    "I seriously doubt that.":
        
        $ renpy.pause (0.5)
        
        An normal "Just think about it this way: What's the worst that could happen?"

        An "We get caught, and maybe they'll tell me to compensate them. Or we'll just say it was your idea and that you didn't know it was forbidden or something. You have diplomatic immunity, so there's nothing they could do."
    
    "You're a bad girl, Anna.":
        
        An "I know."

        $ anna2mood += 1
        
        
    "I'm no filthy thief. I'm outta here.":

        $ renpy.pause (0.5)
        
        An face "Really, you're going to bail after coming all the way out here?"

        An disgust "Fine, then go ahead and starve."
        
        stop music fadeout 2.0
        
        scene black with dissolveslow
        
        window show

        n "I wasn't sure exactly what she was planning, but I wasn't going to be involved."
    
        n "I quickly left, making my way back to my apartment after the events that had just taken place."
        
        window hide
        
        nvl clear
    
        $ annastatus = "bad"
        
        $ annascenesfinished = 2
        
        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars
    
    
An "How well can you hunt?"

c "Me? Even if I knew how, it's not like I have any equipment here."

An face "Equipment? What a sissy."

An normal "You've got hands and teeth. What more do you need?"

c "A long-range weapon, maybe?"

An smirk "Like fire? I suppose even you could make use of that."
    
An normal "Alright, since I'm apparently the only one capable of acquiring food, I'll be right back."

hide anna with dissolve

m "Anna walked over to a fenced enclosure of animals that reminded me of sheep. She crouched and squeezed herself through the bars, after which I lost sight of her."

c "(Waiting game 2.0, start.)"

m "It took only a couple of minutes for her to return, dragging one of the animals behind her with her now-bloodied jaws and hands."

show anna normal c with dissolve

An smirk c "Dinner's ready."

c "What kind of animal is this?"
    
An normal c "It's called a Mouflon."

An "Anyway, do you have a part you'd prefer?"

An smirk c "See how nice I am? I'm even letting you choose first."
    
menu:
    
    "Offal.":

        An "Good choice."
        
        show anna normal c with dissolve
        
        $ anna2mood += 1

        $ mp.vegetarian = False
        $ mp.save()
    
    
    "Rump.":
        
        $ renpy.pause (0.5)

        An normal c "No problem."

        $ mp.vegetarian = False
        $ mp.save()
    
    
    "Anything will do.":

        $ renpy.pause (0.5)
        
        An normal c "Okay."

        $ anna2mood -= 1
        
        $ mp.vegetarian = False
        $ mp.save()

        
    "I'm not hungry anymore.":
        
        $ renpy.pause (0.5)
        
        An face c "Really, that makes you lose your appetite?"
        
        An normal c "Then I'll just have more for myself."
        
        $ nofood = True
        
        $ anna2mood -= 2
    
    
play sound "fx/gore.ogg"

m "Using one of her claws, she skinned the dead Mouflon and divided it into various pieces."

if nofood == False:

    An "Do you want yours grilled or raw?"

    c "Grilled. Unless prepared properly, raw meat carries a significant risk of diseases for us."

else:
    
    An "Now, do I want this grilled or raw? What do you think?"
    
    c "Raw meat actually carries a significant risk of diseases for us if not prepared properly."

An face c "How inept can your species even be? You can't hunt on your own, and you need tools and help at every step. You don't even have claws to cut things up."

An normal c "I'm not sure how you could ever survive in the wild."

An "Seriously, what god did you piss off to end up like that?"
    
menu:
    
    "Evolution.":
        
        c "I guess after millions of years of evolution, nature decided that we didn't need those abilities anymore. Instead, we got very articulate hands and arms, and our upright stance. Those let us do many other things."

        An "Like what?"

        c "Who builds everything in your society? Who's responsible for the delicate tasks, like assembling electronics, manufacturing, or cooking and bartending?"

        An smirk c "That's mostly us, the runners. We've got proper hands, after all."
        
        show anna normal c with dissolve

        c "Now compare your arms to mine. Ours are much longer and have way more mobility."

        c "Especially our fingers. They have an incredible amount of articulation."

        c "The difference between you and me is about as big as the difference between you and another of your species'."

        c "Just imagine what we could do with our advantages."

        An face c "Oh, you think you can school me?"

        c "Sure I can."

        An normal c "Don't get cocky. We've overcome the limitations of individual species with all of our technology."

        c "Actually, we have technology back home that is far superior to yours."

        An smirk c "I'd love to see it. Though, we've already gathered plenty of information on your tech from the databases contained in the PDA. What will you do when we catch up?"

        c "If you get there, we'll see."

        $ mp.belief = "evolution"
        $ mp.save()
        
        
    "None. Humans were made in god's image.":
        
        $ renpy.pause (0.5)
        
        An face c "Do you really believe that?"

        c "I do."

        An smirk c "How cute. I guess that's one way to make yourself feel superior to other species."

        $ anna2mood -= 1

        $ mp.belief = "god"
        $ mp.save()
    
    
    "I have no idea.":
        
        c "I have no idea. It's kinda sad when you look at it from that perspective. So many different species have so many amazing natural abilities that it seems like we got the bad end of the deal."

        c "We always held on to the fact that we had our brains and intellect, but now that we found you, that doesn't really make us unique anymore."

        An smirk c "Mother nature has been so cruel to your race that I almost feel sorry for you."

        $ anna2mood += 1

        $ mp.belief = "noidea"
        $ mp.save()
        
        
show anna normal c with dissolve
            
m "She opened her maw wide before a liquid shot from both corners of her mouth and onto the ground below the parts of the Mouflon she had prepared."

play sound "fx/firex2.ogg"

if nofood == False:

    m "After a few seconds, the liquid burst into flame, heating up our dinner."
    
else:
    
    m "After a few seconds, the liquid burst into flames, heating up her dinner."

c "That's a neat trick."

An smirk c "I bet you wish you could do that, huh?"    

menu:
    
    "No, I'm not a monster.":
        
        $ renpy.pause (0.5)
        
        An face c "If I'm a monster, then what are you supposed to be?"

        c "Human."

        An "So, being biologically inferior somehow makes you better than us. Got it."
        
        show anna normal c with dissolve
        
        $ anna2mood -= 1
    
    
    "That'd be wicked cool.":
        
        An "Right? It comes in handy."
        
        show anna normal c with dissolve
    
        $ anna2mood += 1
    
    
    "I'm not sure.":

        $ renpy.pause (0.5)
        
        An normal c "Why not?"

        c "It would be a neat ability to have, but I don't think I'd want a deadly weapon at my disposal at all times. Furthermore, I'm not sure about what could happen if other humans had access to that skill."

        An "Good point."
        
        
c "How does that work, anyway? Don't you ever burn your mouth?"

An "Not at all. There are actually two different components. They only catch on fire when a sufficient quantity of both is present."
    
c "Interesting."

show cgcampfire at Pan ((0, 500), (1500, 100), 24.0) with fade

$ renpy.pause (16.0)

hide cgcampfire with fade

m "The flames weakened and grew smaller until they went out, revealing steamy, appetizing pieces of meat."

An "Help yourself."

if nofood == False:

    m "I grabbed a piece, but dropped it as soon as I felt the heat on my fingertips."

    c "Ouch, that's still hot."

    An smirk c "Can't take a little heat, huh? That's too bad."
    
else:
    
    c "No, thanks."

m "Unaffected by its temperature, she took a piece into her hand, tore a chunk out of it with her teeth, and started chewing."

c "I guess your scales are a good insulator."

An normal c "Evidently so."

c "How does it taste?"

An smirk c "Just wonderful. Stolen goods always taste best. I can already picture the old farmer reduced to tears after he discovers one of his precious Mouflons is gone."

menu:
    
    "You're a wild one, Anna.":
        
        An "Thanks. I could teach you a thing or two."

        show anna normal c with dissolve
        
        $ anna2mood += 1


    "Seriously, knock it off.":
        
        c "It's bad enough that you roped me into all this, and now you're making fun of the person you stole from. Seriously, knock it off."

        An "If he didn't want someone to steal his things, he should've built a taller fence."

        c "How would you feel if I just walked into your lab and took your stuff?"

        An normal c "You wouldn't be able to, because I actually take security seriously."

        $ anna2mood -= 1


    "What a shame.":
        
        An "And he is such a good man, too. Poor him."
        
        show anna normal c with dissolve
    
    
if nofood == False:

    An "I think it should be cool enough for your sensitive little fingers now."

    m "Carefully, I grabbed one of the pieces, which by now had indeed cooled down enough to not burn me anymore and took a bite."

    m "It was a little bland, I had to admit, but not bad for something that was alive less than an hour ago, and prepared in the wild."

    An smirk c "How do you like your Mouflon à la Anna?"

    menu:
        
        "It could use a few spices.":
            
            c "It tastes a little bland. I think it could use a few spices."

            An face c "I'm not one to destroy a perfectly good piece of meat with stupid vegetables, but you can put some grass on it if you like."

            c "That's not quite the same thing."
            
            $ anna2mood -= 1


        "Not bad.":
            
            c "Not bad, I'd have to say."

            An "Especially at that price."


        "I feel like a wild animal.":
            
            An "Quite different from sitting in an expensive restaurant and using their fancy cutlery and napkins, isn't it?"

            c "Yeah, I like it."

            $ anna2mood += 1
        
        

c "How often do you just go out and hunt on your own?"

An normal c "Only when necessary, or when I feel like it."

An "I still go to fancy restaurants because I can afford it, but they don't mean much to me."

An "For me, it's all about the experience, and one isn't necessarily better than the other."

menu:
    
    "I can see your point. This was unusual, but fun.":
        
        c "I can see your point. This certainly isn't how I thought the evening would go, but it was pretty fun."
        
        $ anna2mood += 1


    "I would've preferred the fancy restaurant.":
        
        An "I can see why; you're totally lost in the wild. You need everything to be done for you by an army of lackeys and cooks." 

        An "Even out here, I can take care of myself. I got the Mouflon, I cut it up and - surprise, surprise - I was also the one who cooked it."

        $ anna2mood -= 1


An "Anyways, I'm stuffed."

if nofood == False:

    c "Me too."

c "There's still plenty left over. What are we going to do with it all?"
    
An smirk c "We can just leave it here. Hey, maybe the old farmer will help himself to it."
    
menu:
    
    "How nice of us to leave some for him.":
        
        An "Yeah, he should pay me for cooking him such a nice meal."
    
        $ anna2mood += 1
        
        show anna normal c with dissolve
    
    
    "Won't this attract predators or something?":
        
        $ renpy.pause (0.5)
        
        An normal c "So what? They need to eat, too."
        
        $ anna2mood -= 1
    
    
    "Talk about recycling.":
        
        $ renpy.pause (0.5)
        
        An normal c "Hey, it's meat. 100%% biodegradable."
    
    
An "We should probably leave before that senile has-been wakes up from his evening nap."
    
c "Yeah, let's go."
    
scene black with dissolve
$ renpy.pause (1.0)
scene facin3 at Pan ((128, 250), (128, 250), 0.0) with dissolve

show anna normal with dissolve

label anna2skip:

c "Well, that was interesting."
    
if blood == True:

    if gotresultsviapost == True:
        
        jump anna2else
        
    else:
    
        An "Wait a minute. I've got something for you."
        
        hide anna with dissolve
        
        play sound "fx/door/door_open.wav"
        
        $ renpy.pause (3.0)
        
        show anna normal with dissolve
        
        An "Here you go. Your test results, black on white."

        play sound "fx/paper.wav"
        
        $ persistent.havetestresults = True

        $ persistent.havetestresultsfromanna = True

        c "Thanks, but did you really need to spend all that extra time getting this done today?"

        An sad "I just wanted to get it over with when I had the chance."
        
        show anna normal with dissolve

else:
    
    label anna2else:
    
    m "Can I ask you something? Did you really have to make me wait two hours so you could finish whatever you were doing?"

    An face "I had something important to take care of in the lab, and I just wanted to get it over with."

    show anna normal with dissolve
    

c "Maybe you should start thinking about not working so late on a regular basis. It might do you some good, Anna."


if anna2mood > 6:
    
    An sad "You know, I think you have a point."

    An "I haven't been feeling like myself lately. There are various reasons for that, but working too much might be one."

    An normal "Today was kinda fun, so maybe I should make the effort to get out every once in a while."

    An smirk "Speaking of which, now that our date is officially over, we should talk about your end of the deal."

    c "Of course."

    An normal "There is an opening soon where I can fit you in. I'll call you with all the details."

    c "I shall be looking forward to that."
    
    $ renpy.pause (0.5)

    $ annasurvives = True
    
    stop music fadeout 2.0
    #$ renpy.pause(2.0)
    $ annastatus = "good"
    
    $ annascenesfinished = 2
    
    $ persistent.anna2skip = True
    
    if chapter4unplayed == False:
    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
    
elif anna2mood > 1:
    
    An face "Why do you think so?"

    c "I'm just saying, if it usually gets as bad as it did today, that's not a good sign."

    An sad "I just didn't pay attention to the time, but I guess that's because I barely go out anyway and I didn't even think about watching the clock."

    An face "Okay, point taken."

    c "So, what are you going to do?"

    An sad "I'll think about it."

    An smirk "You know, now that this date is officially over, if I don't work overtime every single day, I could fit you in for your end of the deal."

    c "Of course you didn't forget about that."

    An normal "I'll let you know the details. Or just call me, if I forget."

    c "Sure."

    $ renpy.pause (0.5)

    $ annasurvives = True
    
    stop music fadeout 2.0
    #$ renpy.pause(2.0)
    $ annastatus = "neutral"
    
    $ annascenesfinished = 2

    $ persistent.anna2skip = True
    
    if chapter4unplayed == False:
    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
    
    
else:

    An disgust "How dare you tell me what to do?"

    c "Maybe if you got out a little more you wouldn't be so choleric all the time."

    An face "When did you become such a know-it-all? Oh, wait, you have been this whole time, and you know what? It's getting old really fast."

    c "Your attitude only proves my point, you know."

    An disgust "My work is my business, not yours. Keep your nose out of it and get back to whatever it is you're supposed to be doing here."

    c "Hey, I was only trying to help."

    An face "Yeah, you know how you can help me right now? By getting the cuss out of here."

    c "Alright, I'm leaving."

    An sad "Thank you."
        
    $ renpy.pause (0.5)
        
    stop music fadeout 2.0
    #$ renpy.pause(2.0)
    $ annastatus = "bad"
    
    $ annascenesfinished = 2
    
    if chapter4unplayed == False:
    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars

    

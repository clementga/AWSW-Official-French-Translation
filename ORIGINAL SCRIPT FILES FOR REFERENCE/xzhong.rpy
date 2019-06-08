label zhong:
    
$ zhongunplayed = False

if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Zhong"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Zhong"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Zhong"
    
else:

    $ save_name = "Chapter 1 - Zhong"
    
scene black with dissolvemed
$ renpy.pause (0.5)
scene bare with dissolvemed

play music "mx/starlight.ogg" fadein 2.0
    
c "(Where is he?)"

c "Anybody here?"

show zhong serv b with dissolve

c "There you are."

#insert skip here

if persistent.playedzhong == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_108

    call skiptut from _call_skiptut_31
        
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
            call skipcheck from _call_skipcheck_31
            
            show bare
            show zhong serv b
            with dissolvemed
            
            play music "mx/starlight.ogg" fadein 2.0
            
            jump zhongskip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/starlight.ogg" fadein 2.0

m "Suddenly, he grabbed my hand and bowed to plant a wet kiss on it with his snout."
    
play sound "fx/kiss.wav"

$ renpy.pause (1.0)

show zhong normal b with dissolve
    
if persistent.playedzhong == True:

    Zh "Hello, [player_name]."
    
else:
    
    Wr "Hello, [player_name]."

    c "I'm sorry, but I don't think we've actually been properly introduced before. What was your name again?"

    Wr "You can call me Zhong."
    

c "Where is everyone?"

Zh "Well, the bar is already closed and everybody's gone home, so it's just us."

c "I see."

c "Wait, is that Bryce sleeping under the table?"

Zh smile b "Oh, you're right. Guess we're not alone, then."

c "Does this happen often?"

Zh normal b "Sometimes."

c "You should start charging him rent."

Zh smile b "That's an idea. Maybe then I wouldn't have to work two jobs."

c "Right, what's up with that?"

Zh serv b "They're both just part-time, so it's no big deal."

c "I see. Which one do you prefer?"

Zh normal b "It's hard to say, really. Bartending is much more fun, but working in the store pays better and is also more stable."

c "At least you get to wear a uniform in both. That doesn't exactly seem common around here."

Zh "Yeah, they're usually very simple. I like this one, but after a while the collar can get a bit tight around the neck."

Zh "The store uniform is just a chore to get on. The hat, the apron - it all feels a bit constricting."

menu:
    
    "I can see that.":
        
        pass
        
    "You look kinda cute in it, though.":
        
        $ renpy.pause (0.5)

        Zh shy b "You think so?"

        Zh smile b "Well, that's a new one."

m "He was interrupted by a loud snore that came from under the table. When I looked down, I saw it was Bryce turning over in his sleep."

Zh serv b "What, Bryce? You want another beer? Sorry, mate, but the bar's already closed."

Zh normal b "Isn't he wonderful?"

menu:
    
    "He's a bit rough around the edges, but he seems like a stand up guy.":
        
        $ renpy.pause (0.5)
        
        Zh smile b "That's pretty accurate, I'd say."

    "Let's hope his body doesn't start getting rid of any... liquids while he's passed out.":

        $ renpy.pause (0.5)

        Zh smile b "Don't worry about that. I have my trusty mop for situations like that."

        c "Hopefully, you won't need it tonight."

        Zh serv b "It's just another part of the job. I'm pretty used to it by now."


c "You seem to know Bryce pretty well. How long have you known each other?"

Zh normal b "Since childhood, really. We both grew up here."

Zh serv b "If you think he's a bit rough now, you should have seen him in his youth. Such a troublemaker."

Zh normal b "But you can rely on him for anything. I'd trust him with my life."

c "It seems like a lot of people have confidence in him as the chief of police."

Zh serv b "They do, and rightfully so." 

Zh normal b "The things he's done for me personally were way beyond his duties. The mark of a true friend."

c "What did he do?"

Zh "Oh, it's a long story. It has more to do with myself than him, really."

c "Come on, you can't just start like that and then not spill the beans."

Zh serv b "Well, if you say so."

stop music fadeout 2.0

show black with dissolveslow

nvl clear

$ renpy.pause (0.5)

window show

n "I was adopted when I was merely a hatchling. It's really not a big deal to me and never really came as a surprise to anyone, considering my parents aren't even the same species as me."

n "My family isn't originally from around here. When I was eight years old, my father got a job here, so we relocated."

n "Moving across the continent meant losing all my friends, and making new ones wasn't so easy for me. I was young, and new, and just a little scared."

window hide

nvl clear

window show

n "Even back then, Bryce was a very curious fella, especially when other people were involved. He came up to me in school, introduced himself, and we've been friends ever since."

n "Many years later, Bryce was already on the force and my desire to find my biological parents had grown so much that I made some efforts to find them."

n "Bryce pulled a few strings, and with his help, I was able to track them down. He even accompanied me on the trip."

window hide

nvl clear

$ renpy.pause (1.0)

Br "Do you want me to come inside as well?"

Zh "No, just stay here, alright?"

Br "Sure."

m "I mustered all my courage and went up to the door of their run-down home."

play sound "fx/knocking1.ogg"

$ renpy.pause (2.0)

play sound "fx/door/door_open.wav"

$ renpy.pause (2.0)

"Resident" "What do you want?"

Zh "Hello. Is this the residence of Huang Fu and Xiuying?"

"Resident" "Who wants to know that?"

Zh "Well, about 20 years ago, you gave up your child for adoption, and..."

"Resident" "Oh, no."

"Resident" "You know what? I'm not dealing with this right now. We didn't give you away just so you could show up whenever you please."

Hu "And don't even think of calling me father."

Zh "...I won't."

m "He turned around and went back inside. Just as he was about to close the door again, another person appeared next to him."

Xu "Don't be rude, Huang. Come in for a tea or something, alright?"

Zh "Alright."

play sound "fx/steps/rough_gravel.wav"

$ renpy.pause (5.0)

stop sound fadeout 1.5

play music "fx/clock.ogg"

Xu "Here, sit down. I'll go and make us some tea."

play sound "fx/chair.wav"

$ renpy.pause(2.5)

play sound "fx/pouringwine.ogg"

$ renpy.pause(2.5)

play sound "fx/clink.ogg"

Xu "Here you go."

$ renpy.pause(1.5)

Xu "Don't you want to join us, Huang?"

Hu "You invited him in. He's your guest, not mine. I don't want to have anything to do with this."

$ renpy.pause(1.5)

Xu "I guess he doesn't want to talk."

Zh "Guess so."

$ renpy.pause(1.5)

Xu  "Maybe he's not ready yet."

Zh "Maybe." 

Xu "..."

Zh "I guess 20 years isn't long enough."

$ renpy.pause(1.5)

Xu "Look, I wanna say I'm sorry, but I know nothing I say can make up for what happened."

Xu "We had to give you away because we were young and stupid. These days, we aren't young anymore."

Zh "..."

Xu "How do you like the tea?"

Zh "It's alright."

Xu "Oh, I've got something for you."

play sound "fx/chair.wav"

m "She got up, walked away from the table and vanished into a different room. Huang Fu was sitting on a couch nearby in front of the TV, his eyes glued to the screen."

m "After a few moments, Xiuying returned and joined me again."

Xu "Here, take this."

Zh "What is it?"

Xu "It's a hat we got you when you were little. It's one of the few things we still have from back then."

Zh "Thank you."

$ renpy.pause(1.5)

Xu "Do you want some more tea?"

Zh "No."

Xu "Okay."

Zh "..."

Xu "I don't want to ask you this, but do you have some cash to spare? We really need some food and Huang doesnt like to go hunting."

Zh "..."

Zh "I just brought enough for the trip back home. I don't think that..."

Hu "Oh, you don't have anything? Then what are you still doing here?"

Zh "You can watch TV, but not provide for your family? What a man."

play sound "fx/chair.wav"

Hu "Get out of my house!" with Shake((0, 0, 0, 0), 2, dist=10)

Xu "No, please..."

Zh "Yeah, maybe it's time for me to go."

play sound "fx/door/door_open.wav"

stop music fadeout 2.0

Hu "And don't even think of coming back. How dare you come here and disturb us like that!" with Shake((0, 0, 0, 0), 2, dist=10)

Br "Is there a problem here, sir?"

Hu "Who the heck are you?"

Br "Police. It sounds like you might have some trouble here. Perhaps of a domestic nature?"

Hu "Not at all."

Xu "I'm sorry, Zhong. He doesn't know what he's doing."

Zh "I can see that."

Xu "..."

Zh "Come on, Bryce. Let's go."

Br "You're done?"

Zh "I think I've seen what I need to."

Br "Alright."

$ renpy.pause (2.5)

hide black 

show zhong normal b

with dissolveslow

play music "mx/starlight.ogg" fadein 2.0

Zh "I cried so much that day."

c "I'm sorry to hear that."

Zh serv b "Not that it matters much anymore. It's all in the past."

Zh "But, Bryce... He's been there for me when I needed him then, and he's still there today."

Zh normal b "Well, except for the part where, in a way, he's responsible for the whole town now."

c "How's he handling it?"

Zh smile b "Pretty well, I'd say. Everyone trusts him and thinks he's doing a great job."

Zh serv b "Anyway, let's put on some music. Give the ol' jukebox a little whirl."

c "Sure."

play sound "fx/chair.wav"

hide zhong with dissolve

m "He got up and walked over to the jukebox in the corner to look at the selection."

Zh "Let's see..."

show zhong normal b with dissolve

Zh "What kind of music do you like?"

Zh "Actually, I'm not sure if your music is in any way similar to ours."

Zh serv b "Let's just put on a few different songs and you tell me what you think, alright?"

c "Sure."

Zh normal b "Feel free to pick anything that strikes your fancy."

$ zhongpiano = True
$ zhongclassic = True
$ zhongrock = True
$ zhongelectronic = True
$ zhongorchestral = True
$ zhongsoundtrack = True

$ zhongmusicsplayed = 0

$ zhongenough = False

label zhongmusic:
    
#insert if zhongmuscicsplayed >5 case
if zhongmusicsplayed >5:

    if persistent.c2music == False:

        $ mp.music = True
        $ mp.save()

        $ persistent.c2music = True
        
        $ achievement.grant("Audiophile")
        
        $ persistent.achievements += 1
        
        call syscheck from _call_syscheck_109
        
        play sound "fx/system.wav"
        
        if system == "normal":
        
            s "You listened to a bunch of music!"
            
        elif system == "advanced":

            s "You listened to a bunch of music. Like a true connoisseur."
            
        else:
            
            s "You listened to a bunch of music. Just for the achievement. Admit it."
    
    
    jump zhongcont

menu:
    
    "Piano" if zhongpiano:
        
        $ zhongpiano = False
        $ zhongmusicsplayed += 1
        $ zhongenough = True
        
        $ renpy.pause (0.5)
        
        Zh serv b "Ah, something easy. Do you know what a piano is?"

        c "You can play the piano?"

        Zh normal b "Not really. Not that many can, actually. There are many kinds of instruments that can only be played by certain species, you see."

        c "Makes sense."
        
        stop music fadeout 2.0

        Zh serv b "Alright, now listen to this."
        
        play sound "fx/button_unpress.ogg"
        
        $ renpy.pause (0.5)

        #$ time = 75
        #$ timer_range = 5
        #$ timer_jump = 'zhongpianofinish'
        #show screen countdown
        
        play music "mx/zhongpiano.ogg"

        #$ renpy.pause (5.0)
        $ ui.timer(76.0, ui.jumps("zhongpianofinish"))
        menu:
            
            "Let's try something else.":
                
                $ renpy.pause (0.5)

                play sound "fx/button_unpress.ogg"
                
                stop music fadeout 2.0
                
                #resume regular music here
                
                Zh normal b "Didn't you like it?"
                
                menu:
                    
                    "It's alright. I just want to try something else.":
                        
                        $ renpy.pause (0.5)

                        Zh serv b "I see."
                        
                        show zhong normal b with dissolve
                        
                    "Not really.":

                        Zh "I suppose it's not to everyone's taste."

                        c "That's what makes it a taste."
                        
                jump zhongmusic
                
                label zhongpianofinish:

                    play sound "fx/button_unpress.ogg"
        
                    #$ renpy.pause (0.5)
                
                    stop music fadeout 2.0
                    
                    #resumt normal music here
                    
                    $ renpy.pause (0.5)
                    
                    Zh normal b "That's it. How'd you like it?"
                    
                    menu:
                        
                        "It's pretty good.":

                            Zh "I like it, too."
                            
                        "Not bad, but I've heard better.":

                            Zh "You think so?"

                            c "It seems a bit simple."

                            Zh serv b "Oh, you think humanity has better pianists, is that it?"

                            c "Not necessarily. It might just be the song."

                            Zh "Maybe we should have a piano battle. Dragons versus humans."

                            c "I'm not sure that would draw a big crowd."

                            Zh normal b "I'd watch it, for sure."
                            
                        "It's pretty bad, to be honest.":

                            Zh "Maybe we should try something else, then."
                            
                    jump zhongmusic
                                
    "Classical" if zhongclassic:
        
        $ zhongclassic = False
        $ zhongmusicsplayed += 1
        $ zhongenough = True
        
        $ renpy.pause (0.5)

        stop music fadeout 2.0
        
        Zh serv b "Now, this one's a real classic. I think it's one of the oldest songs we know about."
        
        play sound "fx/button_unpress.ogg"
        
        $ renpy.pause (0.5)
        
        play music "mx/gymno.ogg"
        
        $ ui.timer(165.0, ui.jumps("zhongclassicfinish"))
        
        menu:
            
            "Stop it.":
                
                $ renpy.pause (0.5)

                play sound "fx/button_unpress.ogg"
                
                stop music fadeout 2.0
                
                #resume regular music here
                
                Zh normal b "Wanna hear something else? Alright."
                
                jump zhongmusic
                
                label zhongclassicfinish:
                    
                    play sound "fx/button_unpress.ogg"
                
                    stop music fadeout 2.0
                    
                    #resumt normal music here
                    
                    $ renpy.pause (0.5)
                    
                    Zh normal b "Quite an old-timey tune, this one."
                        
                    c "I think I've heard it before."

                    Zh "Well, it is a real classic. Someone else might have played it somewhere you've been before."

                    c "No, I mean I've heard it before I ever set foot in this world."

                    Zh serv b "Really?"

                    c "It sounds a bit different, but it's close enough that I don't think this is a coincidence."

                    Zh normal b "Well, if that's the case, then I'm totally the wrong person you should be telling this."

                    c "I'll have to investigate this once I return to my own world."

                    Zh "For sure."
                    
                    jump zhongmusic
                
        
    "Rock" if zhongrock:
        
        $ zhongrock = False
        $ zhongmusicsplayed += 1
        $ zhongenough = True
        
        $ renpy.pause (0.5)

        stop music fadeout 2.0
        
        Zh serv b "Without further ado, here we go."
        
        play sound "fx/button_unpress.ogg"
        
        $ renpy.pause (0.5)
        
        play music "mx/zhongrock.ogg"
        
        $ ui.timer(175.0, ui.jumps("zhongrockfinish"))
        
        menu:
            
            "Turn it off.":

                $ renpy.pause (0.5)

                play sound "fx/button_unpress.ogg"
                
                stop music fadeout 2.0
                
                #resume regular music here

                Zh normal b "Oh, is it too loud for you? I didn't consider your ears may be more sensitive than ours."

                c "Let's just try something else."
                
                jump zhongmusic
                
                label zhongrockfinish:
                    
                    play sound "fx/button_unpress.ogg"
                
                    stop music fadeout 2.0
                    
                    $ renpy.pause (0.5)
                    
                    show zhong normal b with dissolve
                    
                    #resume normal music here
            
                    $ renpy.pause (0.5)
                    
                    jump zhongmusic
        
    "Electronic" if zhongelectronic:
        
        $ zhongelectronic = False
        $ zhongmusicsplayed += 1
        $ zhongenough = True

        $ renpy.pause (0.5)

        stop music fadeout 2.0

        Zh serv b "This is something a bit more modern."
        
        play sound "fx/button_unpress.ogg"
        
        $ renpy.pause (0.5)
        
        play music "mx/flux.ogg"
        
        $ ui.timer(280.0, ui.jumps("zhongelectronicfinish"))
        
        menu:
            
            "Turn it off.":

                $ renpy.pause (0.5)

                play sound "fx/button_unpress.ogg"
                
                stop music fadeout 2.0

                Zh normal b "What do you think?"
                
                menu:
                    
                    "Not enough action for my taste.":

                        Zh "I see."
                        
                    "It makes for nice background music.":

                        Zh "Yeah, you're right. Maybe not for the bar, though."

                        c "Maybe."
                        
                jump zhongmusic
                
                label zhongelectronicfinish:
                    
                    play sound "fx/button_unpress.ogg"
                
                    stop music fadeout 2.0

                    $ renpy.pause (0.5)
                    
                    show zhong normal b with dissolve
                    
                    #resume normal music here
                    
                    $ renpy.pause (0.5)
                    
                    jump zhongmusic
        
    "Orchestral" if zhongorchestral:
        
        $ zhongorchestral = False
        $ zhongmusicsplayed += 1
        $ zhongenough = True

        $ renpy.pause (0.5)

        stop music fadeout 2.0
        
        Zh serv b "This one's a bit slow, so you'll have to wait a while for it to get going."

        c "Alright."

        play sound "fx/button_unpress.ogg"
        
        $ renpy.pause (0.5)
        
        play music "mx/day10.ogg"
        
        $ ui.timer(157.0, ui.jumps("zhongorchestralfinish"))
        
        menu:
            
            "Turn it off.":
            
                label zhongorchestralfinish:

                $ renpy.pause (0.5)

                play sound "fx/button_unpress.ogg"
                
                stop music fadeout 2.0

                Zh normal b "What's your verdict?"
                
                menu:
                    
                    "I don't like slow music.":

                        Zh "I see."
                        
                    "I don't like orchestral music.":

                        Zh "I see."
                        
                    "That was pretty decent.":
                    
                        $ renpy.pause (0.5)

                        Zh smile b "It's one of my favorites, actually."

                        c "Oh, really?"

                        Zh normal b "Yeah."
                        
                jump zhongmusic
        
    "Soundtrack" if zhongsoundtrack:
        
        $ zhongsoundtrack = False
        $ zhongmusicsplayed += 1
        $ zhongenough = True
        
        $ renpy.pause (0.5)

        stop music fadeout 2.0
        
        Zh serv b "Now, this is something a bit different. It's from the soundtrack of some video game, I think."

        play sound "fx/button_unpress.ogg"
        
        $ renpy.pause (0.5)
        
        play music "mx/cute.ogg"
        
        $ ui.timer(85.0, ui.jumps("zhongsoundtrackfinish"))
        
        menu:
            
            "Turn it off.":
                
                label zhongsoundtrackfinish:
                    
                $ renpy.pause (0.5)

                play sound "fx/button_unpress.ogg"
                
                stop music fadeout 2.0

                Zh normal b "So, what do you think about this one?"
                
                menu:
                    
                    "It's not really my kind of music.":

                        Zh "It's unusual, that's for sure."
                        
                    "I like it.":

                        Zh "Really? I didn't think you would."

                        c "Why's that?"

                        Zh "Just a guess."
                        
                jump zhongmusic

     
    "[[I've heard enough.]" if zhongenough:
        
        jump zhongcont
        


label zhongcont:

play music "mx/starlight.ogg" fadein 2.0
    
c "What kind of music do you like, anyway?"

Zh serv b "I like a bit of everything, really."

Zh smile b "I actually collect all kinds of music and paraphernalia, and the jukebox is curated by me."

c "Oh, nice."

Zh normal b "Sometimes, people even donate some stuff they don't need anymore. I'm pretty well known among the patrons for it."

c "Is the stuff on display over there yours, too?"

Zh "I'm actually trying to sell those."

c "You're selling your collection?"

Zh "I'm only downsizing. That's just a player and a few old records I'm trying to sell for my holiday fund."

c "Oh, where are you going?"

Zh smile b "It's going to be a family holiday - just my son and myself. Mainly for my son, though. We're planning to travel across the whole country, making stops in various cities along the way."

Zh normal b "I've been planning it for a while now and trying to save up to make it happen. We could never really afford a vacation while his mother was still around, so..."

c "What happened to her?"

Zh "I wish I knew."

Zh "We fought a lot back then, about all kinds of things. When I think back to that time now, it seems like that was all we did. Argue about petty things that people don't need to argue about."

Zh "Of course it's easy to say that after the fact, and when it's already too late."

Zh "I never would have thought it was bad enough to warrant doing what she did, though."

c "What did she do?"

Zh "One day, she was just gone. Packed up her things and left in the dead of night."

Zh "I don't know where she went or what became of her."

Zh "In the end, I think she just wasn't ready to be a mother."

Zh "This was almost four years ago now."

Zh serv b "But, yeah, that's why I think we need that holiday - to spend some quality time together."

Zh normal b "It's also why I took that second job in the grocery store. He's going to turn 9 in a few months and I want to surprise him with it then."

Zh smile b "He saw this movie where a family goes on vacation across the country and all kinds of crazy hijinks happen along the way. He loved it so much and asked me all the time when we were going on a vacation like that."

Zh normal b "I just want to give that to him. I think he needs it."

c "You said his birthday is in a few months. Will you be able to afford it?"

Zh "We're more than halfway there already. With the second job, it really shouldn't be a problem. I'd just like to have more of a buffer, because this holiday will have all the bells and whistles you can imagine."

c "I see."

c "How about I buy some of those records?"

Zh "Really?"

c "You said they're for sale, right?"

Zh "Yes, but..."

c "I'll just put it down as expenses in regards to my visit here, so it'll be all taken care of."

Zh "You would do that?"

c "Maybe, after you played me some of that music, I just can't resist and need those records for myself. Actually, I'll need the player too, because I doubt those are going to work with our own players back home."

c "Besides, I could really use a souvenir."

Zh "Thank you. Thank you so much."

Zh smile b "Let me just get that for you."

hide zhong with dissolve

$ renpy.pause (0.5)

show zhong smile b with dissolve

play sound "fx/player.ogg"

Zh "Here you go."

menu:
    
    "Try to give it back.":

        c "You know what, why don't you keep it?"

        Zh normal b "What do you mean?"

        c "Well, what if I wanted to donate this back to your collection?"

        Zh "Oh, no. That would be too much. It's yours. Please, take it."

        c "Alright."

        Zh smile b "Besides, these aren't so special that they need to be part of the collection. Otherwise, I wouldn't be selling them."

        c "Okay, I get it."

        Zh normal b "It'll also be interesting for humanity to have, I think."

        c "For sure."

        Zh serv b "Maybe you can show me some human music in return sometime." 

        c "Deal."

    
    "Keep it.":

        c "Thanks. I'll take good care of it."
        
        Zh serv b "I'm sure of that."
        
        
c "So, I suppose you're back in the game now, huh?"

Zh normal b "Game? What game?"

c "I mean dating."

Zh shy b "What makes you think so?"

c "Well, what's all this? Why'd you ask me out?"

Zh normal b "You seemed like a nice person. I wanted to know what you're like."

c "Do you kiss the hand of every nice person you meet?"

Zh serv b "Guess you got me there. I suppose that makes my intentions rather obvious, even though I know it won't last."

Zh smile b "Besides, I'm not sure if I'd call it a game. That's something that Bryce would do."

Zh normal b "I'd prefer to take things slower and have a lasting relationship."

menu:
    
    "I agree.":
    
        $ renpy.pause (0.5)

        Zh serv b "I see."

        $ mp.relationshiptype = "slow"
        $ mp.save()


    "I prefer Bryce's approach.":

        $ renpy.pause (0.5)

        Zh serv b "Whatever works for you."

        $ mp.relationshiptype = "fast"
        $ mp.save()

    
    "I think both can be fun.":

        $ renpy.pause (0.5)

        Zh serv b "Whatever works for you."

        $ mp.relationshiptype = "both"
        $ mp.save()


c "Why'd you ask me out if you know it's not going to last, though?"

Zh "Bryce told me about you, y'know. It made me realize I've got to get out there again."

c "So the first thing you do is ask out the strange visitor from an exotic place."

c "Be honest, did you just ask me out because I'm human?"

Zh normal b "Not only."

Zh serv b "I figured you could tell me more about how humans date and give me some advice."

c "I'm not sure if my experience would be worth anything here."

Zh normal b "You're bound to have a different perspective of everything that goes on here. Maybe you pick up on things we haven't considered. I just want to hear your opinion."

Zh serv b "It's not just about dating, you know."

c "Well, let's talk about dating if you're interested in that. I doubt I'd be able to have a frank discussion about this with just anyone I meet here."

Zh normal b "Alright. I think by now you've got a taste about how Bryce is with these kinds of things. He likes messing around. It seems like he's got someone new every couple of months."

Zh "You should see him on some nights and how people just swarm around him. Can't blame him for that, though. He's a popular guy."

c "Do you envy him?"

Zh "No, I don't want what he has, but I'm finding it hard to find just one prospective partner."

Zh serv b "You'd think I'd pick up on these things while working, but then it's typically not long-term relationships that are formed here."

c "I see."

Zh normal b "I don't exactly have that much free time to put myself out there. I'm also not getting younger, and don't forget that I already have a child to take care of."

Zh "That doesn't make things easier, you know. In a way, you're not just dating the person, you're also dating the kid, if you know what I mean."

c "Now that just sounds wrong."

Zh "Oh, shush."

Zh "It can make things rather difficult, that's all."

c "Alright, maybe we'll have to work on your approach. What's the first thing you notice about a person?"

Zh serv b "Their personality."

c "Really?"

Zh normal b "I meet so many people here every day. When they're customers, the thing that always stands out about them most is how they treat their servers."

c "I see."

Zh "Besides, I'm not interested in relationships based on looks. I like talking to people and getting to know them that way."

Zh serv b "This also makes the whole thing harder for me, because I have to invest a lot more time to find out if we're compatible."

Zh normal b "You know, if a relationship doesn't work out for Bryce, he can just find someone else the next day, but for me this process can take a few months."

c "I can imagine."

c "I don't think there's a recipe for success I can give you, though."

Zh "Why not?"

c "You seem to be doing pretty well already. You're nice and polite. I don't think you need to do anything different."

Zh serv b "Is that what you think?"

c "Yeah. Sure, it may take awhile to find someone, but I don't think there are any shortcuts for what you're trying to do. Just keep going and it'll happen eventually."

c "Besides, you've got some time to figure things out for yourself with your vacation coming up, right?"

Zh smile b "That's true. It'll be an eye-opening experience in a number of ways. Maybe the relationship front is going to be one of them."

c "Now that's the right attitude."

Zh serv b "And on that note, maybe we should call it night. It's pretty late."

c "Yeah, you're right."

label zhongskip:

Zh "Well, thank you for the wonderful evening."

c "Likewise."

Zh "Not to mention the advice, and for buying my stuff."

c "You're welcome."

Zh "Be safe, take care, and maybe I'll see you some other time."

c "Maybe."

$ persistent.playedzhong = True

$ mp.playedzhong = True
$ mp.save()

stop music fadeout 2.0
#$ renpy.pause(1.0)

if chapter4unplayed == False:
            
    jump chapter4chars
    
elif chapter3unplayed == False:
    
    jump chapter3chars
    
elif chapter2unplayed == False:
    
    jump chapter2chars
    
else:

    jump chapter1chars

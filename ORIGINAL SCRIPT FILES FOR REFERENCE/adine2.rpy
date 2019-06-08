#+19, -21

label adine2:

#$ chapter2csplayed += 1
$ adine2unplayed = False
$ adine2mood = 0

if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Adine 2"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Adine 2"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Adine 2"
    
else:

    $ save_name = "Chapter 1 - Adine 2"

scene black with fade
$ renpy.pause (1.0)
scene town4 at Pan((0, 0), (0, 0), 0.0) with dissolvemed

play music "mx/warming.ogg"

c "(This should be the right address.)"

play sound "fx/knocking1.ogg"

$ renpy.pause (3.0)

Ad "I'm coming!"

play sound "fx/door/doorchain.ogg"

$ renpy.pause (2.0)

show adine normal b with dissolve

Ad "Oh, it's you. I was expecting someone else. You're a little early."

c "Yeah, I didn't know how long it would take me to get here. Better early than late, right?"

if chapter3unplayed == False:

    if adinesendawayseen == False:
    
        Ad "You know, I'm glad they decided not to send you away after all."
    
        c "Me too."
    
        $ adinesendawayseen = True

scene black with dissolve
$ renpy.pause (0.5)
scene cgamely at Pan ((0, 0), (580, 326), 8) with dissolvemed
$ renpy.pause(5.5)
#show cgamely with fade

#$ renpy.pause (4.0)

#hide cgamely 
scene town4 at Pan((0, 0), (0, 0), 0.0)
#show amely normal at Position(xpos = 0.63)
show adine normal b
with fade

c "And who might that be?"

Ad "This is Amely. She's one of the kids I work with."

hide adine with dissolve

show town4 at Position(xpos=0.0, xanchor='left', ypos=1.01, yanchor='bottom') with ease

show amely normal at Position(xpos = 0.63) with dissolve

c "Hello, Amely."

Ad "Say hi, Amely."

Am "Hello."

hide amely with dissolve

show town4 at Position(xpos=0.0, xanchor='left', ypos=0, yanchor='top') with ease

show adine normal b with dissolve

Ad "I just have to bring her back to the orphanage real quick. Feel free to make yourself at home in the meantime, okay?"

c "Sure."

hide adine
with dissolve

$ renpy.pause (1.0)

if persistent.playedadine2 == False:
    
    if persistent.c2pictures == False:
        
        play sound "fx/system.wav"
        
        s "You met Amely! {image=image/ui/status/c2pictures.png}"

        $ renpy.pause (0.5)
        
$ persistent.playedadine2 = True

scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow

$ renpy.pause (1.5)

if persistent.adine2skip == True:

    stop music fadeout 1.0
    
    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_89

    call skiptut from _call_skiptut_23
        
    if skipbeginning == False:

        if system == "normal":
        
            s "My records indicate you have already experienced this scene in a satisfactory manner. Would you like to skip ahead a bit?"
        
            #play sound "fx/system3.wav"
        
            #s "Warning: In this scene, skipping ahead this way instead of using the skip buttons (CTRL and TAB) may prevent you from experiencing alternative choices and outcomes that you haven't seen before. These may only be minor, though."
        
        elif system == "advanced":

            s "It looks like you've seen this before. Skip ahead a bit?"
        
            #play sound "fx/system3.wav"
        
            #s "I have to warn you, though. If you do this here instead of just using CTRL and TAB, you may end up missing some minor changes you haven't seen before."
            
        else:
            
            s "So, it turns out you've seen this before. Either you could watch this again, or we could save some time and just skip ahead a bit."
            
            #play sound "fx/system3.wav"
            
            #s "If you want to do things this way instead of just using the skip buttons like a civilized person, you could end up missing some choices you haven't made before. But considering how far you've come, you probably won't miss much."
        
    $ skipbeginning = False
    
    menu:
        
        "Yes. I want to skip ahead.":
            
            play sound "fx/system3.wav"
            
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            
            show black with dissolvemed
            
            $ renpy.pause (1.0)

            $ persistent.skipnumber += 1
            call skipcheck from _call_skipcheck_23

            show adine normal b behind black with dissolve
            
            hide black with dissolvemed

            play music "mx/warming.ogg"

            $ adine2mood = 5
            
            jump adine2skip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/warming.ogg"

c "(So this is where you live, Adine. Small, but cozy.)"

show adine normal b with dissolve

Ad "I'm back!"

c "That was quick."

Ad giggle b "Being able to fly does have its perks, you know."

c "Wait, you flew her back?"

Ad normal b "Well, I am a delivery flyer."

c "She doesn't get scared or anything?"

Ad "Not at all. She's such a brave little girl."

c "So, what exactly is it that you do at the orphanage?"

Ad "I'm a volunteer. I help them out with whatever they need, and sometimes take care of the kids."

Ad "They only have so many social workers. The ratio is about one social worker for every ten children, so it's good for the kids to spend some time one-on-one with someone they know."

Ad think b "I guess you could almost call it babysitting, but for the kids, we basically become foster parents."

Ad disappoint b "The older they get, the less likely they are to be adopted. She might be too old to be considered soon..."

menu:

    "What a shame.":
        
        Ad "Yeah, I know."
        $ adine2mood += 1
        
    "I can see why.":
        
        $ renpy.pause (0.5)
        
        Ad think b "What do you mean?"

        c "She seems like an annoying little brat. I certainly wouldn't let one of those into my home."

        Ad disappoint b "How can you say that?"

        c "I'm just being honest."

        Ad annoyed b "You know, sometimes, honesty is not the best policy."
        
        Ad disappoint b "Someone has to look out for her."

        $ adine2mood -= 1
        
    "I'd adopt her if I could.":
        
        Ad "I'm afraid it's just not that easy, and the actual numbers of adoptions aren't very promising, either."
        

Ad "I'm worried about what will happen to her if she doesn't find a family."

Ad "We will still take care of her, of course, but it's not quite the same as having parents."

Ad "I'd adopt her myself, but I don't think I could care for her properly. Not as a single parent with my packed work schedule."

Ad "I still volunteer as often as I can, because if I don't, who will? Someone needs to be there for those kids."

menu:
    
    "You're wasting your time.":
        
        $ renpy.pause (0.5)
        
        Ad annoyed b "It's called empathy. Maybe you should try it sometime."
        
        show adine disappoint b with dissolve

        $ adine2mood -= 1
        
    "That's very nice of you.":

        $ renpy.pause (0.5)
        
        Ad normal b "Thanks, but for me, it's not about being nice. I almost feel obligated to help, you know?"
        
        show adine disappoint b with dissolve

        $ adine2mood += 1

    "Someone else would probably volunteer, even if you didn't.":
        
        Ad "Maybe, maybe not. The only thing I know for certain is that they could use all the help they can get."

Ad "Anyway, let's talk about something less depressing."

c "Like what?"

Ad think b "Let me think."

Ad disappoint b "Oh, I just remembered that someone died here recently."

c "Here, in your apartment?"

Ad normal b "No, not here, silly. It was close, though. Barely a block from here."

c "Right, the murder of the maintenance guy. I remember that."

Ad disappoint b "Wait, it was murder? I didn't know that; I thought it was an accident or something. That's terrible."

c "Sorry for mentioning it."

Ad "Finding the first victim was already bad enough for me, and now I have to hear there was another murder in town... I wish I could get some good news for once."

menu:
    
    "At least it wasn't you who was murdered.":
        
        $ renpy.pause (0.5)
        
        Ad think b "That's a strange way of looking at it, but you have a point."
        
        show adine normal b with dissolve

    "Don't be so sensitive.":
        
        $ renpy.pause (0.5)
        
        Ad annoyed b "You're not really a people person, are you?"
        
        show adine normal b with dissolve

        $ adine2mood -= 1

    "Don't just focus on the bad things.":
        
        c "Don't just focus on the bad things. It's no use lamenting something you can't change."
        
        Ad "Sorry, [player_name]. I guess I should be more positive."
        
        Ad "It's just not always easy, you know."
        
        c "Maybe you'll get some good news soon."
        
        Ad normal b "I hope so."
        
        $ adine2mood += 1
        
        show adine normal b with dissolve
    
    
Ad "That reminds me, I've got something I wanted to try on you."

c "Try on me?"

Ad "It's nothing too dramatic. I read this magazine the other day and found a few interesting articles ."

m "Using her partial hands, she held up a magazine to show me its cover. A rather bold-looking female was presented on the front, adorned with trinkets like rings and jewels. Various headlines gave me an idea of the content within. It reminded me a lot of the typical gossip magazines back home."

c "{i}LIFESTYLE: The Magazine for Modern People{/i}?"

Ad giggle b "This issue even came with a set of fortune cards!"

menu:
    
    "I'm not sure what to expect.":
        
        Ad "Isn't that the whole fun of it?"

        $ adine2mood += 1
        
        show adine normal b with dissolve
        
        
    "Those types of magazines are usually trash.":

        $ renpy.pause (0.5)
        
        Ad annoyed b "Come on, don't knock it before you try it."
        
        show adine normal b with dissolve

        $ adine2mood -= 1


    "I'm sure they're qualified to determine my fate.":
        
        c "With articles like {i}5 Steps to Get the Partner of Your Dreams{/i}, I'm sure they're qualified to determine my fate."

        Ad normal b "Come on, it'll be fun."

        c "If you say so."

Ad "What should we look at first?"

menu:
    
    "I don't care.":
        
        $ renpy.pause (0.5)
        
        Ad think b "Alright, let's see."


    "You decide.":

        $ renpy.pause (0.5)
        
        Ad think b "Alright, let's see."

        $ adine2mood += 1
        

    "Throw the stupid magazine in the trash.":
        
        $ renpy.pause (0.5)

        Ad annoyed b "That's very funny, [player_name]."

        $ adine2mood -= 1
        

play sound "fx/pages.ogg"

Ad normal b "Here, this article talks about dreams and what they mean."

Ad think b "Have you had any strange or recurring dreams lately?"

menu:
    
    "My dreams are usually nonsense.":
        
        $ renpy.pause (0.5)
        
        Ad normal b "Well, according to this article, that means you're a really creative person."

        c "Good to know."


    "I've been dreaming of fire.":
        
        Ad "Fire? That's interesting."

        Ad normal b "Apparently, it's a rather common symbol that can mean a variety of things."

        Ad think b "Another thing to consider is the significance of the symbol to the dreamer. So, what does fire mean to you?"

        Ad normal b "Fire can be destructive, but also wild and passionate. It can represent an issue or problem you can no longer ignore, similar to an actual fire breaking out."

        Ad giggle b "It also mentions prophetic dreams, but let's hope that yours don't fall into that category."

        c "I doubt they do."

        Ad think b "Phew."
        
        show adine normal b with dissolve

        $ adine2mood += 1


    "I don't dream at all.":
        
        $ renpy.pause (0.5)
        
        Ad normal b "Actually, that's not the case. You only think that because you don't remember your dreams."

        Ad think b "But even that can tell us something."

        Ad "Dream recall is linked to how strong of a sleeper you are and the duration of your rest."
        
        Ad normal b "Light sleepers recall their dreams more often, particularly if they wake up during the night. It seems that dream recall is closely related to waking up during the right phase of sleep."

        Ad "So, if you maintain the same schedule every day and sleep for the same amount of time every night, it could prevent you from remembering your dreams."
        
        $ adine2mood -= 1
        
        
    "My dreams are often about people I know.":
        
        Ad "That could be for a variety of reasons. One theory is that dreams are a way for the brain to process day to day experiences, so it's not unusual to dream of people you've met."

        Ad normal b "But a recurring dream involving the same people is a different story. That could represent strong emotions for or unresolved issues with that person."
        

c "What about your dreams?"

Ad think b "It kinda feels like they're different every night. Most of them are nonsense, but sometimes I dream of people I used to know."
        
Ad "What do you make of all this?"        
        
menu:
    
    "It's a whole bunch of baloney, if you ask me.":

        $ renpy.pause (0.5)
        
        Ad disappoint b "But dreams are so interesting. They must mean something."

        c "Or maybe they don't mean anything at all. You're overthinking it."

        Ad think b "I'm just saying there's got to be a reason they exist. Even the article concludes that scientists haven't figured out exactly why we dream. It's a big mystery."
        
        $ adine2mood -= 1

    
    "I don't know.":
        
        Ad "Even the article concludes that  scientists haven't figured out exactly why we dream. It's a big mystery."
                
        
Ad normal b "Alright, let's move on."

play sound "fx/pages.ogg"

c "Oh, I thought you meant moving on from the magazine."

Ad annoyed b "Don't be such a sourpuss. There's some interesting stuff in here."

menu:
    
    "I'll reserve judgment on that.":

        $ renpy.pause (0.5)
        
        Ad think b "That's probably for the best."


    "Do you think you can hit the trash can with it from here? You should try.":
        
        $ renpy.pause (0.5)
        
        Ad think b "Okay, maybe you didn't like the first article, but just wait for what I'm going to show you now."
        
        $ adine2mood -= 1
        

    "That dream stuff wasn't so bad.":
        
        $ renpy.pause (0.5)
        
        Ad giggle b "See, I told you this was going to be fun."
        
        $ adine2mood += 1


c "What's next?"

Ad normal b "A personality test. Didn't you always want to know what kind of relationship would suit you?"

menu:
    
    "I already know what I want in a relationship.":
        
        $ renpy.pause (0.5)
        
        Ad giggle b "In that case, we'll find out if what you think about yourself is true."


    "I'd like to see a close relationship between this magazine and the trash can.":
        
        $ renpy.pause (0.5)
        
        Ad annoyed b "Why do you have to be like that? You don't have to take this seriously, but at least have some fun with it."

        c "But I'm already having so much fun."

        $ adine2mood -= 1


    "Sure, why not.":
        
        $ renpy.pause (0.5)
        
        Ad giggle b "Let's find out."

        $ adine2mood += 1


Ad normal b "Okay, first question: In a relationship, what role do you take?"

menu:
    
    "I prefer to take the reins.":
        
        $ renpy.pause (0.5)
        
        Ad giggle b "Is that so?"
        
        show adine normal b with dissolve

        $ mp.type = "reigns"
        $ mp.save()

        $ adine2mood += 1
        
        
    "My partner should be the leader.":
        
        $ renpy.pause (0.5)
        
        Ad think b "Really? I didn't think you'd be that kind of person."
        
        $ adine2mood -= 1

        $ mp.type = "partner"
        $ mp.save()

        show adine normal b with dissolve


    "I like to switch it up every once in a while.":
        
        $ mp.type = "switch"
        $ mp.save()

        Ad "Variety is the spice of life, right?"


Ad "Moving on to the next question."

c "Wait, aren't you going to answer the questions, too?"

Ad "I'll take the test after you. I don't want to keep track of both our scores at once."

c "Alright."

Ad "Question number two: What is your favorite dessert?"

$ adine2menuask = True

label adine2menb:

menu:
    
    "Chocolate cream cake.":
        
        Ad "An all-time classic. Who doesn't like chocolate cake?"
        
    "Lemon ice cream with sprinkles.":
        
        $ renpy.pause (0.5)
        
        Ad giggle b "That's unusual, but sounds really interesting. I'd love to try some!"
        
        show adine normal b with dissolve
        
        $ adine2mood += 1

    "Coconut soufflé.":
        
        Ad "I'm always worried I'll mess up soufflés; they're just so fragile. I'd certainly try one if I had the opportunity, though!"

    "Red hot chili cookies.":
        
        $ renpy.pause (0.5)
        
        Ad think b "I don't think chilies should go anywhere near something that's supposed to be a dessert, but that's just me."

        show adine normal b with dissolve
        
        $ adine2mood -= 1


    "What does this question have to do with relationships?" if adine2menuask:
    
        $ renpy.pause (0.5)
    
        Ad annoyed b "Oh, just answer it."
        
        $ adine2mood -= 1
        
        show adine normal b with dissolve

        $ adine2menuask = False
        
        jump adine2menb
        
Ad "Here's the next question: What is your dream job?"

menu:
    
    "Farmer.":
        
        $ renpy.pause (0.5)
        
        Ad think b "Some people believe that kind of life is very idyllic, but I think it would also be a lot of work."

        $ mp.job = "farmer"
        $ mp.save()

    "Businessperson.":

        $ renpy.pause (0.5)
        
        Ad think b "I don't understand the appeal of that kind of job. It certainly doesn't mesh well with my ideals."
        
        $ adine2mood -= 1

        $ mp.job = "business"
        $ mp.save()

    "Stay-at-home parent.":

        $ renpy.pause (0.5)
        
        Ad think b "I'm with you on that one, but does that really qualify as a job?"

        c "Are you questioning the almighty magazine?"

        Ad giggle b "Forget I said anything."

        $ mp.job = "parent"
        $ mp.save()

        $ adine2mood += 1

show adine normal b with dissolve

c "How many more questions are there?"

Ad giggle b "That's all of them."

Ad normal b "Now, to look up the results."

play sound "fx/pages.ogg"

$ renpy.pause (2.0)

Ad think b "Oh, it says here that the results are outlined in the weight-loss booklet that came with the magazine, but I already threw that away."

menu:
    
    "Why'd you do that? You clearly needed it.":

        $ renpy.pause (0.5)
        
        Ad sad b "Do you think so?"

        c "Yeah."

        Ad disappoint b "Oh, well."
            
        $ adine2mood -= 1
    
    
    "What a shame.":
        
        $ renpy.pause (0.5)
        
        Ad disappoint b "Yeah, I really wanted to know."
    
        $ adine2mood += 1

    
    "Guess we'll never find out what kind of relationship would suit me.":
        
        Ad "Yeah, how else would you know?"

        c "There's no other way. I'll be at a loss for the rest of my life."



Ad giggle b "But now we get to the best part: The fortune cards!"

menu:
    
    "Do we really have to do that?":

        $ renpy.pause (0.5)
        
        Ad disappoint b "Come on, what's the worst that could happen?"

        c "I could waste precious minutes of my life that I'm never going to get back."
        
        Ad normal b "Haha. Very funny."
    
    
    "You know that stuff's not real, right?":

        $ renpy.pause (0.5)
        
        Ad annoyed b "I just want to try it out for fun. You need to be more open-minded."

        $ adine2mood -= 1
        
        
    "That's what I was looking forward to.":
        
        $ renpy.pause (0.5)

        Ad normal b "Me too."
    
        $ adine2mood += 1
    

c "How is that supposed to work, anyway? I mean, they're just cards. How can they predict the future?"

Ad think b "Apparently, there are different schools of thought regarding the use of fortune telling cards."

Ad "The cards themselves don't know anything. They're just a tool."

Ad normal b "So, the information actually comes from somewhere else."

c "But where, though?"

Ad think b "Well, one interpretation is that it's our subconscious who gives us the answers that we seek."

Ad normal b "Similar to how dreams can be interpreted, the interpretation of the cards is very dependent on the person itself and the symbols they recognize in the card's images."

Ad "We recognize images that are relevant to our lives, and that gives us an idea about ourselves and our current problems."

Ad think b "However, that is just the most grounded interpretation out there. People usually associate something more paranormal with fortune cards."

Ad "One of those explanations is that the cards are our way to communicate with a higher being, a paranormal entity that knows more than we do and can give us subtle nudges using the cards."

c "And who would that be?"

Ad giggle b "The explanations range from ghosts to angelic beings. One even involved humans."

c "Really?"

Ad normal b "Yeah, people would say you could communicate with humans this way."

Ad think b "And then there was also something they called {i}higher self{/i}."

c "Higher self?"

c "How come you know so much about this?"

Ad normal b "Because I read the article about it."

c "Oh."

Ad think b "Okay, what should I draw for you?"

c "Why don't I get to be the one who's reading the fortune?"

Ad giggle b "Because I paid for this magazine, so the cards are mine."

c "Okay."

c "So, what are my options?"

Ad normal b "I could read your past, present or future."

Ad think b "What is it going to be?"
    
menu:
    
    "Past.":
        
        $ mp.time = "past"
        $ mp.save()

        Ad "Reading the past sounds a little strange, since you already know it, but it might help you see things in a new light or give you a new perspective."
        
        show adine normal b with dissolve
        
        play sound "fx/shuffle.ogg"
        
        $ renpy.pause (3.0)

        Ad "Let me see what this card means..."
        
        play sound "fx/card.wav"
        
        Ad think b "Your past is filled with fire, strife and conflict. Yet like steel, you adopted it and were tempered by it. What didn't kill you only made you stronger." 

        Ad "As a result, you grew up quickly and became a mature and decisive individual. You know what you want and you have the potential to get it."

        Ad normal b "What do you think about that?"
            
        menu:
            
            "It's true.":
                
                $ renpy.pause (0.5)
                
                Ad think b "Is that so?"

                Ad normal b "Then it's up to you to keep learning from your past and moving forward with that knowledge."
                
                show adine think b with dissolve
                
                $ adine2mood += 1
            
            
            "It's not true.":
                
                c "That doesn't really apply to me. Like, at all."

                Ad think b "Maybe I did it wrong."

                c "Who knows? Maybe you should ask your almighty magazine."

                Ad giggle b "Don't be silly."
                
                show adine think b with dissolve
                
            "This is very generic.":
                
                c "This is very generic. You know that it's intentionally vague so everyone feels like it applies to them, right?"

                Ad annoyed b "You can't really expect a great amount of detail from a one card reading."

                c "Yeah, I'm sure that's the reason."

                $ adine2mood -= 1
                    
                show adine think b with dissolve




    "Present.":

        $ mp.time = "present"
        $ mp.save()
        
        Ad "Let's see what it says about the present... According to this, understanding our present situation is paramount to understanding the future, as what we do now influences the future that will become our present."

        show adine normal b with dissolve
        
        play sound "fx/shuffle.ogg"
        
        $ renpy.pause (3.0)

        Ad think b "Oh, this is interesting."
        
        play sound "fx/card.wav"
        
        c "What does it mean?"

        Ad "Crossroads are ahead of you. Be wary of your decisions, for the consequences may be dire. Careful actions may have rewarding results, but carelessness could have consequences reaching further than you might think."

        Ad normal b "At least, that's what the description says."

        Ad "What's your opinion on this?"

        menu:
            
            "I'm not sure what this could mean.":
                
                c "To be honest, I'm not really sure what this could mean."

                Ad "Well, we make decisions every single day of our lives. I think it's just telling you to be careful."

                c "That's good advice."

                show adine think b with dissolve
                
                
            "I feel like this is totally true.":

                c "I feel like this is totally true, especially if you consider what it means for me to be here. I'm aware that whatever I do here could impact a lot of lives."

                Ad "I see. In that case, I agree that you should be very careful."
                
                show adine think b with dissolve
                
                $ adine2mood += 1
                
                
            "This is very generic.":

                c "This is very generic. You know that it's intentionally vague so everyone feels like it applies to them, right?"

                Ad annoyed b "Well, you can't really expect a great amount of detail from a one card reading."

                c "Yeah, I'm sure that's the reason."
                
                show adine think  b with dissolve
                                
                $ adine2mood -= 1


    "Future.":

        $ mp.time = "future"
        $ mp.save()
        
        Ad "The prediction of the future is what most people associate with these readings. However, their purpose is to prepare the person in question for a possible future, rather than just predicting it."

        show adine normal b with dissolve
        
        play sound "fx/shuffle.ogg"
        
        $ renpy.pause (3.0)

        Ad think b "Oh my..."
        
        play sound "fx/card.wav"

        c "What is it?"

        Ad "The card we've drawn is associated with drastic measures, particularly those with a final conclusion." 
        
        Ad "This can be interpreted in many ways, but it can refer to death, the ultimate conclusion. It can also mean many other things, like a violent outcome of a brewing conflict, or a positive resolution of a long-running conflict."

        Ad "What do you think?"
        
        menu:
            
            "I think I know what this refers to.":
                
                Ad "Really? How can you already know about the future?"

                c "Let's just say I have a hunch. It mentioned resolutions to conflicts that have been brewing, and there's definitely stuff brewing."
                
                $ adine2mood += 1


            "I wonder if I should be worried.":
                
                $ renpy.pause (0.5)

                Ad normal b "If anything, it's not supposed to make you worry, but give you some input so you can prepare for what is to come."

                c "And what would that be?"

                Ad think b "I suppose you'll find that out when the time comes."


            "This is very generic.":
                
                c "This is very generic. You know that it's intentionally vague so everyone feels like it applies to them, right?"

                Ad annoyed b "Well, you can't really expect a great amount of detail from a one card reading."

                c "Yeah, I'm sure that's the reason."
                
                show adine think b with dissolve

                $ adine2mood -= 1

Ad "I guess that's everything the magazine has to offer."

menu:
    
    "This certainly was interesting.":
        
        $ renpy.pause (0.5)
        
        Ad normal b "I guess that means you had fun, then?"

        c "Sure, let's call it that."

        $ adine2mood -= 1


    "Now you can finally put it in the trash where it belongs.":
        
        Ad "Actually, yeah. It's not like I'm going to read the articles again."
            
        Ad normal b "But I'll keep the cards, because it'd be a shame to just throw them away. The pictures are so artistic and pretty."

        c "I agree with you there."
        
        play sound "fx/can.ogg"
        
        $ renpy.pause (1.0)
        
        Ad disappoint b "It's got to be so much work to create a magazine like this. From selecting the topics, writing the articles, doing all the photos and the layouts... And then to get it to shops and into the hands of customers. All that work just for it to end up in the trash."

        Ad think b "With how often they come out, it's like they're designed to be disposable."

        c "At least they can recycle the materials."

        Ad normal b "That's true, I suppose."
        
        $ adine2mood += 1
        
        
    "What a shame.":

        $ renpy.pause (0.5)

        Ad normal b "I could try to find the diet booklet if you're that desperate to find out the personality test results."

        c "Please don't."

        Ad giggle b "Alright."
        
        show adine normal b with dissolve
    

Ad "So, do you have anything interesting going on at the moment? I can't imagine what ambassador life is like."

c "It's been busy. I thought this whole thing would go by quickly and without any mishaps, but now it seems like there's always something happening." 

Ad think b "Oh, really?"

c "Yeah. I figured I'd come here, do the exchange and leave again, but apparently it's not that easy."

Ad disappoint b "It never is."

c "You speak like you've had experience as an ambassador."

Ad normal b "Well, no, but doing deliveries is similar. People order something, I fly to them, we exchange the product for payment and then I go back. It's basically the same thing."

c "Yeah, sure."

Ad think b "But things always go wrong. For example, imagine you have two deliveries to make and the first one goes smoothly, okay?"

c "I'm imagining it very hard right now."

Ad normal b "Alright, so you get to the destination of the second delivery, and they actually check what you're handing them. It turns out that you mixed up the orders, but you already delivered the first one."

c "That's certainly not a pleasant situation to be in."

Ad "Now you have to go back to the first family you delivered to, who by now have probably noticed that they got the wrong delivery, and exchange what you gave them for what they actually ordered."

c "Right."

Ad giggle b "But it turns out that they didn't mind the mix-up. As a matter of fact, they have already started eating what they got instead."

Ad normal b "It's not so bad that they aren't angry, but now you can't exchange the orders anymore, so you have to fly back to the restaurant to get the second order remade."

c "Happens all the time."

Ad disappoint b "As a result, the people waiting for the second order do get angry, because their order has to be remade and delivered all over again."

c "And the plot thickens."

Ad annoyed b "They complain and, of course, get their meal comped." 

Ad disappoint b "The restaurant can no longer sell that first order you still have, so the orders for both families are deducted from your paycheck and you end up eating nothing but ramen all week again, just so you can make rent this month."

c "That is unfortunate."

Ad normal b "And that's why you always double check your orders, because even a small mistake can have consequences reaching further than you'd think."

c "Sometimes we just have to learn the hard way."

Ad disappoint b "I guess so."

c "Anyway, what else have you been up to recently?"

Ad normal b "Do you remember the stunt flying competition I told you about?"

c "Of course. I assume your participation is a given by now?"

Ad think b "Actually, I'm not so sure about that. I mailed the application earlier today, so hopefully it will arrive before the deadline."

Ad giggle b "Or maybe I should just fly it over myself. While showing off a few moves, that is."

c "You should fly over anyway to make sure you get in. It would be a shame if you couldn't enter because of a technicality."

Ad normal b "Yeah, I really should drop by."

label adine2skip:

Ad think b "By the way, could you do me a favor?"

c "That depends on the favor, I suppose."

Ad normal b "It's kind of a long story, but there's something I need. You know some people at the police station, right?"

c "Yes?"

Ad think b "I think they're in possession of a map related to an underground building they found."

c "I've heard about that."

Ad normal b "Oh, that's great! Maybe you can get them to hand it over? It doesn't even have to be the real thing, a copy would be just fine."

c "What do you even need it for?"

Ad think b "Let's just say I'm interested in doing a little investigation of the place myself."

c "What's so special about it?"

Ad normal b "It's supposed to be a remnant of an earlier civilization, or maybe even something created by humans. Who wouldn't be interested in that?"

menu:
    
    "What, an actual human in front of you is not enough?":

        $ renpy.pause (0.5)
        
        Ad giggle b "If I had you all to myself it might be enough, but since your stay is only temporary, I'll need some other human-related things to keep me busy."

        $ adine2mood += 1
        
    
    "I can think of a few people.":

        $ renpy.pause (0.5)
        
        Ad disappoint b "Even if you don't believe in the myths, it's still a fascinating discovery."

        $ adine2mood -= 1
        
    "I'd pay it a visit myself if I could.":
        
        Ad "See? I think if you put your word in, we could easily make it happen."


c "How do I even ask for something like that?"

Ad think b "You could always say that humanity is interested in it."

c "Honestly, they probably would be."

Ad sad b "Could you ask them for me, please?"

$ adinerequestmade = True

menu:
    
    "I can try.":
        
        c "I won't promise anything, but I can certainly try."

        Ad normal b "Thank you! That means a lot to me."

        $ adine2mood += 1

    
    "I'll think about it.":
        
        c "I'll have to think about it. No promises."

        Ad normal b "Thank you!"
        

    "No.":
        
        c "Even if I wanted to, the police have bigger problems to deal with. I don't want to burden them more by making them look for a piece of paper."

        Ad disappoint b "Well, it was worth a shot."

        $ adine2mood -= 1


c "I didn't know you were into archaeology."

Ad think b "I wouldn't care as much if it turned out to just be some old building. The whole thing about it being made by humans is what's really interesting."

c "Why's that?"

Ad normal b "Well, the myths wouldn't be very mythical anymore if that was the case. We'd have proof."

c "And that so shortly after finding out that humans are, in fact, real."

Ad giggle b "Yes! What a time to be alive."

c "So you believe in all of that stuff?"

Ad normal b "\"Belief\" isn't the right word when you're standing right in front of me, you know. That alone is a miracle. I get excited all over again just thinking about it."

c "Speaking of which, all this excitement made me lose track of the time."

Ad think b "Is it that late already?"

Ad giggle b "Oh, actually, I have places to be. Especially if I want to make sure my contest application arrives on time."

c "Guess I should be going then, huh?"

if adine2mood > 11:
    
    Ad think b "Unless you want to sit in my empty apartment."

    Ad normal b "You could always pay me a visit during practice sometime, if you like."

    c "You mean your stunt flying practice?"
    
    Ad giggle b "Yeah!"

    Ad normal b "Anyway, I really have to go, so I'll call you later, okay?"

    c "Sure."
    
    hide adine with dissolve

    play sound "fx/door/doorclose3.wav"
    stop music fadeout 1.0
    $ renpy.pause(2.0)
    $ adinestatus = "good"

    $ adinescenesfinished = 2

    $ persistent.adine2skip = True
    
    if chapter4unplayed == False:
    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    
    
elif adine2mood > 1:
    
    Ad normal b "For now, at least. I certainly wouldn't mind if you stopped by again sometime."

    c "Will there be any magazines involved?"

    Ad think b "Actually, that magazine doesn't come out that often, so we wouldn't have anything new from them. I could get a different one if you wanted to, though."
        
    c "Don't bother."

    Ad giggle b "Heh, if you say so."

    Ad normal b "Anyway, I really have to go, so I'll see you around!"
    
    hide adine with dissolve

    play sound "fx/door/doorclose3.wav"
    stop music fadeout 1.0
    $ renpy.pause(2.0)

    $ persistent.adine2skip = True

    $ adinestatus = "neutral"

    $ adinescenesfinished = 2

    if chapter4unplayed == False:
    
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
    

else:

    Ad normal b "Yeah, please do."

    c "That almost sounds like you want me to leave."

    Ad "Because I do."

    c "Seriously? What did I do?"

    Ad annoyed b "Besides acting like a jerk, not much."

    c "You're just too sensitive. And your magazine was stupid."

    Ad disappoint b "Whatever. I have to go now, anyway, so please just leave."

    stop music fadeout 1.0
    $ renpy.pause(1.0)

    $ adinestatus = "bad"

    $ adinescenesfinished = 2

    if chapter4unplayed == False:
        
        jump chapter4chars
        
    elif chapter3unplayed == False:
        
        jump chapter3chars
        
    elif chapter2unplayed == False:
        
        jump chapter2chars
        
    else:

        jump chapter1chars
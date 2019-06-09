label katsu:

$ katsuunplayed = False
$ katsuavailable = False
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Katsu"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Katsu"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Katsu"
    
else:

    $ save_name = "Chapter 1 - Katsu"

scene black with fade
$ renpy.pause (1.0)
scene np3x at Pan((0, 0), (0, 220), 4.0) with dissolveslow

$ renpy.pause (2.3)

play music "mx/fun.ogg" fadein 2.0

show katsu normal with dissolve

c "There you are. I wasn't sure if I was going to find you from the description you gave me."

Ka "Well, this corner is where I do business. You could've asked anyone and they would've told you where to find me."

#skip here

if persistent.playedkatsu == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_103

    call skiptut from _call_skiptut_27
        
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
            call skipcheck from _call_skipcheck_27
            
            scene town2 at Pan ((150, 400), (150, 400), 0.0)
            show katsu normal flip at Position (xpos = 0.35)
            with dissolvemed
            
            play music "mx/fun.ogg" fadein 2.0
            
            jump katsuskip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/fun.ogg" fadein 2.0


c "I see."

Ka smile "Now, what would you like for your ice cream?"

c "Well, what do you have to offer?"

Ka normal "What I have to offer?"

Ka excited "As for the main dish, I have ice cream, gelato, frozen yoghurt, frozen custard, soft serve, sorbet, sandwiches, popsicles, mellorine, sherbet, cold taffy, snow cones and haluhalo."

c "Alright."

Ka "For sides, I can offer you waffles, sticks, pretzels, cups, wafer cones, cake cones, sugar cones, chocolate-coated cones, double cones or vanilla cones."

c "That's a lot of variety you have there."

Ka smile "And I haven't even started on about the toppings. Now you know why I have to keep dragging this big cart everywhere."

show katsu at Position (xpos = 0.8) with ease

show bryce normal b flip at left with easeinleft

Br "Excuse me?"

Ka normal "I'm sorry, but we're closed."

Br brow b flip "You don't look closed."

Ka "But we are."

Br stern b flip "I really want to buy an ice cream, though. Please? It's really hot, and I'll pay you twice as much."

Ka "Sorry, we are closed."

Br "Can you at least tell me when you're going to be open?"

Ka "When I feel like it. Now, off you go."

Br "But..." 

m "Katsuharu waved a claw dismissively."

Ka exhausted "Off you go."

Br brow b flip "Sheesh, whatever. I'll just go and jump into a lake or something."

$ renpy.pause (0.3)

show bryce brow b

$ renpy.pause (0.3)

hide bryce with easeoutleft

$ renpy.pause (0.1)

show katsu at center with ease

c "Why did you come here when you're closed?"

Ka normal "This is just my spot. Has been for a long time. I'll open for those pesky customers later, but right now I have a guest to entertain."

c "I see."

c "How long have you been doing this?"

Ka "I've been in this business for over 40 years now."

c "Oh, wow."

Ka "You see, I'm this town's only real ice cream vendor."

Ka "Sure, you could just go into a store and buy any premade ice cream nowadays, but it's just not the same."

Ka smile "My customers know that. They love my ice cream."

Ka normal "Of course I don't just sell it, I also do ice cream parties and catering."

c "Ice cream parties?"

Ka smile "Only for very special occasions."

c "The townsfolk must really like your ice cream, then."

Ka normal "Oh, yes. Business has been wonderful for decades. Lately though, everything just seems to be going down."

c "Why is that?"

Ka exhausted "Every day, less customers find their way to me. If I don't sell everything, things start to spoil and I have to throw them away. I never had to do that before."

Ka "If it keeps going like this for much longer, I might have to face the reality of bankruptcy. I was planning to retire in a few years... But I can't. Not like this."

Ka "It wouldn't be nearly as bad if I hadn't also lost all my savings recently."

c "Oh no! What happened?"

Ka normal "Well, I happen to be an avid player of a game called Mahjong, and just as it so happens, sometimes people play it for money, too."

c "You lost all your life savings by gambling?"

Ka smile "That's the funny thing about gambling - sometimes you win, and sometimes you don't."

Ka excited "Sometimes you win big, and sometimes you lose all your savings. That's just how it goes."

c "I see."

c "How did you decide to become an ice cream vendor, anyway?"

Ka normal "I have quite a history, human, so I'd hope you're prepared."

c "Well, I am an ambassador, so if you have a story to tell, I'll listen."

Ka "As you wish."

stop music fadeout 2.0

show black with dissolveslow

nvl clear

$ renpy.pause (1.0)

window show

play music "mx/morningrise.ogg" fadein 2.0

n "I have very fond memories of my childhood. When I was little, we had a confectioner in town who offered all kinds of specialties - from cookies and sweets to cakes and chocolates." 

n "The owner was a kind, old dragoness who made everything that was sold in her shop with her own two claws. Her confectionery was always very good, but it was her ice cream that was truly exceptional."

n "Even as a small child, I could always taste the difference - even when my peers didn't care and proclaimed one ice cream as good as the next."

n "As I grew up, I came to a fundamental understanding about people. There are those who are content with the lowest common denominator, and those - like me - who could appreciate the finer details in expertly crafted things."

window hide
nvl clear
window show

n "I talked with her when I heard of her plans to retire, to see if someone else was to continue running the shop, or if she had taken in an apprentice. But, to my utter dismay, I learned that this was not the case."

n "You see, she was the kind of humble person who didn't think of herself or her wares as special in any way, so she never felt the need to preserve them."

n "I realized that without my intervention, her art would be lost forever."

n "I begged and pleaded with her not to let this happen, but she insisted that I had vastly overestimated her skill."

n "It was not until I ran out and brought her some of the store-bought pulp they dared to call ice cream that she gave in and agreed with me."

window hide
nvl clear
window show

n "As a creator, she of course had never felt the need to buy some for herself when she could just make her own. And after only eating her own, wonderful ice cream for all these years, it had just become ordinary for her. She had never realized how exceptional it truly was."

n "Even though she was already at retirement age at the time, she took me in as an apprentice to teach me the fine art of confectionary."

n "I was her student for a few years and learned the basics of many different recipes, but unfortunately, she passed away before I could learn the secrets to her particular blend of ice cream."

n "For the next couple of years, I travelled from city to city, trying to find her relatives or confectioners of a similar caliber in order to find the last ingredients of her recipe."

window hide
nvl clear
window show

n "Going from one disappointment to the next, I finally tracked down a distant nephew who remembered her from his own childhood." 

n "Even back then, her ice cream had apparently been very popular in the family. He was very happy to hear that she was able to fulfill her dream of owning her own confectionery."

n "However, after he told me that the recipe was the confectioner's own and that she had never divulged it to anyone else, I had to realize that this was a secret she had apparently taken with her to the grave."

n "Nowadays, people tell me that I have surpassed her. What they don't know is that all the different recipes I use - all the varieties I offer - came to be when I tried to recreate her recipe."

n "I never succeeded."

#stop music fadeout 2.0

window hide
nvl clear

$ renpy.pause (1.5)

hide black 

with dissolveslow

#play music "mx/fun.ogg" fadein 2.0

$ renpy.pause (0.2)

Ka exhausted "Just look at the number of different ice creams I sell. People tell me how impressive that is and how they are all wonderful." 

Ka "They think it makes me better than her, but she only ever sold a single flavor, a single variety. She never needed anything else, because that one flavor was perfect."

#Ka "Now I try to cover up my imperfections with toppings and sides or different flavors."

Ka "I can only ascribe my own success to what I learned from her."

Ka "Of course, this corner is not the only place where I sell the ice cream. I also have my spots in the surrounding villages, but even out there I can slowly see the influence of the cities taking over."

Ka "The trouble is, nowadays people just don't appreciate the art anymore. They only care that they can eat, and not about what they eat. They are too quick to settle for what they can get from the local supermarkets. Ugly, mass-manufactured pulp. Gah!"

Ka normal "You know, some of those companies have approached me before. They wanted to buy my recipes, but I won't let them ruin what I have by making it cheap and easy to produce like the stuff they sell."

Ka "My ice cream is only what it is because I still make it myself with my own two hands. This is the way it has been and how it's always going to be."

c "You mentioned you were planning to retire in a few years. What's going to happen then? Do you have any students who will take over the business afterwards?"

m "The dragon gave a big sigh."

Ka exhausted "I wish. I've had a few students who wanted to learn the art, but they all gave up sooner or later."

c "Why is that?"

Ka normal "I may be very forgiving, but the recipes aren't. Some steps require manual labor, and people don't expect the harsh conditions that come with the job."

Ka "Many apply only because they know how successful I am or how much I sell on a hot day, but they don't see all the work that goes on behind the scenes."

Ka exhausted "I see the same influence of the cities corrupting the youth of today. They are lazy and seek instant-gratification, wanting to make the recipes easier and cut corners, but I won't stand to compromise on quality."

Ka "If there is no one willing to learn, appreciate and preserve the art, it will tell me there is no desire for my ice cream in this world anymore."

Ka normal "Let them have their cheap stuff if that's all they want. I'd rather take my recipes to the grave than let the big companies have them."

Ka smile "I have a grandson who may be my last hope. Unlike others, he was always interested not only in eating my ice cream, but also in learning what it took to make it. In a year or two, he will be old enough to become my apprentice if he so desires."

Ka normal "I am not sure if his interest will still be present. Even if it is, I don't know if he will be able to brave the hardships that come with it. But I have hope."

Ka exhausted "However, that is talk for the future. I have much more pressing problems right now."

c "Like what?"

Ka "You see, this area used to be the popular spot for people to meet each other, but ever since Tatsu Park opened, it's not worth it to come to my corner anymore. The store is closer now."

c "Maybe you shouldn't count on the people seeking you out. You should try coming to the people instead. That's what a cart is usually for, right? Have you tried moving it somewhere else?"

Ka normal "Moving?"

c "Well, that's what the wheels are for, right?"

Ka "But this has been my spot for the last 40 years. It's always worked out great for me."

c "Considering it's not working out so great right now, maybe it's time for a change."

m "The dragon raised a claw to his chin, his expression telling me that he was deep in thought."

Ka "I guess I don't really have anything to lose at this point. What do you propose?"

stop music fadeout 2.0

scene black with dissolveslow

$ renpy.pause (0.5)

scene town2 at Pan ((300, 400), (150, 400), 3.0) with dissolveslow

$ renpy.pause (1.3)

play music "mx/fun.ogg" fadein 2.0

show katsu exhausted with dissolve

Ka "I'm not sure how I let you convince me to come here when this is the place that stole all my customers from me."

c "I don't think that's the right way to look at it."

c "The world is ever changing, and you can't stop that. You have to find ways to deal with it, or else you'll be left behind in the past."

c "It's too easy to just blame the change and be done with it. You shouldn't really be so quick to give up, you know?"

Ka "But all my customers know that the other corner is my spot. How are they going to find me here?"

c "I think the people who will buy some ice cream will spread the word."

Ka normal "You think so?"

c "It's summer. I'm sure there are tons of people around who'd like to buy an ice cream right now."

Ka smile "Well, if you think you can sell ice cream better than me, then please, go right ahead."

c "What do you usually do?"

Ka normal "What do you mean?"

c "Well, what's your usual sales tactic?"

Ka "I don't need to do anything special. People always used to come to me. During my best times, they'd wait for my arrival in lines and I'd be sold out in minutes."

c "I see. That may have worked before, but these times call for different measures, I think."

play sound "fx/cart2.ogg" fadein 1.0 

hide katsu with dissolve

m "We set up the cart at one of the busier corners. Once it was ready, we only needed to get the word out."

stop sound fadeout 1.0

c "Ice cream! Ice cream!"

c "Ice cream by the one and only Katsuharu, here in Tatsu Park!"

c "Get some while supplies last!"

m "It didn't take much to make the people in the vicinity take notice."

m "The first customers arrived quickly. Of course, everyone recognized Katsuharu and loved his ice cream, but they also commended him on this new location."

m "Others, however, were attracted by me. The human that was generally under police protection openly selling ice cream gave people plenty of excuses to come over for a short chat."

m "Soon, people were flocking to the cart as word got around of the human selling Katsuharu's legendary ice cream in Tatsu Park."

show katsu normal flip at Position (xpos = 0.2) with easeinleft

show grey normal at right with easeinright

Gr "Could I get one of these, please?"

Ka smile flip "Of course! One ice cream for my favorite art student."

Gr "H-How did you know?"

Ka normal flip "I've seen you around. Besides, your accessories kinda gave it away."

Gr "Oh, okay."

$ renpy.pause (0.2)

show grey normal flip

$ renpy.pause (0.3)

hide grey with easeoutright

$ renpy.pause (0.5)

show leymas normal at right with easeinright

Le "I need some ice! My colleagues are dehydrated from working in the heat."

Ka "How many cups would you like?"

Le "Let's make it ten."

Ka smile flip "Alright, here you go. Ten cups, plus one extra. Just for you."

Le "Thank you! I'll make it count."

$ renpy.pause (0.2)

show leymas normal flip

$ renpy.pause (0.3)

hide leymas with easeoutright

#$ renpy.pause (0.3)

#hide katsu with dissolve

show katsu normal flip with dissolve

m "Business was booming, but it wasn't until a certain person showed up that things were about to get serious."

show emera normal b at right with easeinright

Em "Well, this is interesting."

c "M-Minister..."

Em frown b "What do you think you're doing here?"

c "Well, what does it look like?"

Em ques b "It looks like you're selling ice cream, and since I personally know Katsuharu, I know that it's exquisite ice cream at that."

c "Not a bad guess."

Em normal b "I don't want to tell you what to do, but if the trade commissioner finds out about this, I won't hear the end of it. He'll probably be blathering about unfair competition and abuse of your status."

Em ques b "I wouldn't mind his complaints, you know, but since I am in charge of your visit, it's all going to come back to me, and he's going to want an explanation."

c "I just wanted to help Katsuharu. That's all."

Em frown b "Help him? Is he in trouble?"

#show emera at right with ease

#show katsu normal flip at left with easeinleft

Ka exhausted flip "Alas, the human speaks the truth. Ever since the opening of Tatsu Park, my business has been plagued by drought and become forsakened like a desert."

Em "Well, it's not hard to see why when you kept staying at your old spot on the other side of town."

Ka normal flip "It was [player_name]'s idea to come here."

Em ques b "And it was a good one. You don't look like you're having much trouble here at all, my friend."

Ka exhausted flip "Yes, I will have to admit defeat on that front, but in hindsight, all successful ideas look like good ones."

Em normal b "My friend, how come you never told me about any of this? I could have arranged something for you."

Ka "I was sure you had more troubling issues yourself than taking care of a businessman who should be able to take care of himself."

Em ques b "Well, I won't stand for this town's only ice cream vendor going out of business. With this new location, I don't think you'll have any more trouble, but in order to resolve this little situation here right now, I think I'll have to go with a different solution."

Em normal b "You want to sell some ice cream, [player_name]? Then I'll just have to buy the rest of your inventory."

Ka excited flip "Minister must be very hungry then. Or very hot. Maybe both."

Em ques b "I'm sure the other employees in my building will appreciate a little something to combat the heat. "

Em normal b "Would you mind if I borrowed this cart for a while? Otherwise, I'm not sure how I would go about transporting it all safely."

Ka "Not at all. Just let me know when I can retrieve it."

Em ques b "Of course."

$ renpy.pause (0.2)

show emera ques b flip

$ renpy.pause (0.3)

play sound "fx/cart2.ogg" fadein 1.0

hide emera with easeoutright

stop sound fadeout 5.0

$ renpy.pause (2.0)

show katsu at Position (xpos = 0.35) with ease

c "Well, that was interesting."

Ka "This could have hardly turned out better for me. I can already feel the excitement of my glory days returning to these old bones of mine."

c "It sounded like you two knew each other."

Ka normal flip "Indeed. I have served her ice cream since the beginning of my career."

c "Talk about a long-time customer."

Ka smile flip "And a good one, too. I know she not only has enjoyed my ice cream out of tradition or necessity, but also due to an appreciation of the finer arts. She is a connoisseur, like me."

c "And she bought the whole inventory."

Ka normal flip "Yes, but don't just see her as a big spender. She is a true patron of the arts."

c "Do you like her?"

Ka exhausted flip "How dare you say something like that about her? She is a muse, an inspiration. Her lifestyle embodies the philosophy of my art."

Ka normal flip "And you ask if I like her? Pah!"

c "I see how it is."

Ka excited flip "Anyway, I guess I should be thanking you for the help. Again."

c "There's no need for that."

Ka smile flip "I'd offer you some more ice cream, but I'm afraid we're all out for the day."

c "Actually, I didn't even have one earlier."

Ka normal flip "What?"

c "Yeah, that customer you didn't want to serve interrupted us, and now Emera took the rest with her."

Ka "Oh, you're right."

label katsuskip:

Ka exhausted flip "What a great shame. You sold all my stock, yet didn't get a chance to indulge in the luxury yourself."

c "It's no big deal."

Ka smile flip "You know, you could come by next time when I'm in town again. Now that you have saved my business, I'd let you eat all the ice cream you want."

c "Thanks."

Ka exhausted flip "Well, maybe not all of it, or else I might go bankrupt again..."

stop music fadeout 2.0
$ renpy.pause(1.0)

if persistent.playedkatsu == False:

    $ achievement.grant("The Artisan")

    $ persistent.playedkatsu = True

    $ persistent.achievements += 1

    call syscheck from _call_syscheck_104

    $ mp.playedkatsu = True
    $ mp.save()

    play sound "fx/system.wav"

    if system == "normal":

        s "You met with Katsuharu!"
        
    elif system == "advanced":

        s "You met with Katsuharu and saved his business. Good job."
        
    else:
        
        s "You met with Katsuharu and saved his business. But who wouldn't at the prospect of free artisan ice cream?"

if chapter4unplayed == False:
            
    jump chapter4chars
    
elif chapter3unplayed == False:
    
    jump chapter3chars
    
elif chapter2unplayed == False:
    
    jump chapter2chars
    
else:

    jump chapter1chars














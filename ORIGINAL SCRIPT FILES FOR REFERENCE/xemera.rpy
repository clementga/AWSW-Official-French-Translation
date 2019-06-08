label emera:
    
$ emeraunplayed = False

if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Emera"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Emera"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Emera"
    
else:

    $ save_name = "Chapter 1 - Emera"
    
scene black with dissolvemed
$ renpy.pause (0.5)
scene corridor with dissolvemed

c "(This should be the right place.)"
    
play sound "fx/knocking1.ogg"

$ renpy.pause (2.0)

Em "Come in."

c "(Well, here goes nothing.)"

play sound "fx/door/door_open.wav"

scene black with dissolvemed

$ renpy.pause (0.5)

scene emeraroom at Pan ((0, 0), (0, 180), 5.0) with dissolveslow

$ renpy.pause (3.3)

#insert skip here

if persistent.playedemera == True:
    
    stop music fadeout 1.0

    #$ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_68

    call skiptut from _call_skiptut_19
        
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
            call skipcheck from _call_skipcheck_19
            
            scene emeraroom at Pan ((0, 180), (0, 180), 0.0)
            show emera normal b
            with dissolvemed
            
            play music "mx/forge.ogg" fadein 2.0
            
            jump emeraskip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            #play music "mx/campfire.ogg" fadein 2.0

show emera mean with dissolve

play music "mx/forge.ogg" fadein 2.0

Em "What a pleasant surprise. I didn't expect you to take me up on my offer. I'm sure you are a very busy person."

menu:
    
    "That I am.":
        
        pass
        
    "I have no doubt the same is true for you.":
        
        pass
        
    "Not too busy for a visit like this one.":
        
        pass


$ renpy.pause (0.5)

Em frown "I'm sorry I have to say this, but I won't have much time for you today. As edifying as your visit is no doubt going to be, I have a meeting to attend shortly. However, I'm still grateful you came to visit."

c "I'm sure someone of your standing is always busy. Thank you for taking the time to meet me."

Em mean "Charming as always, aren't you?"

c "So, what exactly is this? An official meeting? A trade negotiation?"

Em normal "Oh, please. This is just two people having a conversation. After all, we still owe you for the PDA devices you gave us, so until we deliver our part, there is nothing to negotiate."

c "I see."

Em mean "If it was up to me, though, I'd rather listen to you all day than having to work through this stack of paperwork."

c "Is it really all that boring?"

Em normal "Well, sometimes."

Em frown "It's just an unpleasant part of the job, I suppose. In the end, working as the {i}Minister of Culture & Arts{/i} involves just as much paperwork as any other bureaucratic position."

Em normal "On some days, I have to keep reminding myself that there are actual people and problems behind those numbers, and those are the people I'm responsible for."

Em frown "One mistake, and those people turn against you faster than... something that is very fast. That's why I prefer to go where the people are rather than being stuck back here. It makes things much clearer than the abstraction of words and numbers."

c "Is that what this is for you? A game, or a popularity contest?"

Em ques "I may use the law, [player_name], but I don't break it."

Em normal "As much as I may dislike it, a game is certainly what this is. When I came into office, it didn't take long for me to realize that you can't win if you don't play."

c "..."

Em frown "Let me ask you one thing, [player_name]: Do you enjoy your work as ambassador?"

menu:
    
    "I do.":
        
        $ renpy.pause (0.5)

        Em normal "Lucky are those whose purpose is enjoyable. Too bad not all of us are."

        $ mp.work = "yes"
        $ mp.save()

    "I don't.":
        
        $ renpy.pause (0.5)

        Em ques "Such is the burden we have to bear, [player_name]."

        $ mp.work = "no"
        $ mp.save()

    "Work doesn't have to be enjoyable.":

        c "Work doesn't have to be enjoyable, but it can still be fulfilling. That is especially true for what I'm doing right now."

        Em normal "Indeed."

        $ mp.work = "neutral"
        $ mp.save()


c "That doesn't sound like you enjoy your job very much, though."

Em frown "Well, I look at it this way: Just one term of having been on the council and I'll have left my mark."

Em ques "One term of being stuck behind a desk with my paperwork. At least I get to do something where I can make a difference, even if that doesn't happen very often. {i}Culture & Arts{/i} don't exactly give me much room for doing what I'd want to, you know."

Em normal "Still, I prefer stacks of papers and meetings to working in a mine and pulling carts or logs, or whatever else they would have us earth dragons typically do."

Em ques "When I look at those who have to do hard manual labor, I can't help but feel empathy towards them. I'm impressed by their tenacity to work in conditions that I would never want to. I wish to help them."

c "What about those who enjoy that kind of work?"

Em normal "Sure, but I'm not talking about them. I'm talking about those like myself who are just not cut out for that kind of job."

Em mean "Being in charge of your visit in this world, however, has been quite an opportunity."

c "Was it just that - an opportunity?"

Em ques "Of course not. I have been a staunch believer in {i}humanism{/i} for a long time."

c "{i}Humanism{/i}?"

Em normal "The belief in humans and their contribution to our existence."

c "I see."

Em ques "Some people say I only took this matter into my hands as just another publicity stunt, but I can assure you my feelings on the matter are genuine regardless."

c "(Pun intended?)"

Em normal "I would argue that making it a public spectacle only confirms my position on the matter."

Em frown "In the end, I don't have any hard feelings, because I know the critics are only another part of the job I have to deal with."

Em "You should see how quick they are to jump at my throat and second guess every decision I've ever made. How ironic it is for people like that to have a platform where they can spout their opinions when I'm the one making all the hard decisions."

Em normal "It doesn't matter, though. I know that I will never please everyone, but my numbers do speak for themselves. In the end, it is all just a great self-sacrifice to make a difference."

c "Is that why you became a politican?"

Em ques "I'd like to think it was all preordained. My parents were the vehicle so I could get this far."

if persistent.bornread == True:

    c "That reminds me of this book I've seen. It was called {i}Born to Serve{/i}, I think..."

    Em normal "How very perceptive of you. Indeed, I happen to have quite a fondness for it, since Avdon's experience is not unlike my own."
    
else:
    
    pass
    
Em frown "I always knew I was destined for greatness, just like my parents before me." 

Em mean "However, they thought I would need to work hard like them to get there. That's where they were mistaken."

Em frown "I grew up as an only child in a village mostly known for its mining industry. My father was a very business-minded individual. He worked hard to provide for us and advance his career, whereas my mother was more of a... spiritual person."

Em normal "After years of saving up, they combined their interests and created a new business out of nothing, a gamble that paid off handsomely." 

Em frown "I did what was expected of me. I studied and worked hard until I came to resent it. By that point I was at crossroads in regards to my future career."

Em ques "My parents wanted me to continue my studies, but I decided against doing that. Studying and working hard so that I may study and work hard ad infinitum wasn't something that was particularly appealing to me."

Em frown "In the end, I didn't see the difference between working hard in the mines and studying perpetually. Instead, I started to look for alternative options."

Em normal "There was an opening for a political position, and I decided to seize the opportunity and applied for it. At the time, I wasn't sure whether to be surprised at the fact that I got the position, but if I look back at it now, it certainly shouldn't have."

Em frown "I was very qualified for the job, but I also have a feeling that my parents might have persuaded those in power, because they knew this would be another step up for our family."

c "Persuaded them? How?"

Em normal "This is only speculation, of course, but I wouldnt put it past them to do something like that - no matter if it was with words, gifts or something else."

c "How has that worked out for you?"

Em frown "Now that I am here, the stacks of books have merely been replaced by stacks of paperwork. At least I am popular, though."

c "Are you, really?"

Em mean "I know I am polarizing, but why try to please everyone and accomplish nothing when I know it's impossible to please everyone in the first place?"

Em normal "It is a departure from the usual way of thinking, and while not liked by everyone, some of my moves have been lauded by a great majority."

Em frown "My strategy is to take risks that may or may not pay off when I know I have nothing to lose rather than playing it safe and just perpetuating the status quo."

c "You have nothing to lose?"

Em ques "I am not afraid of political suicide, because I don't value the position itself. I only value the opportunities I am given while having this power, so as long as I have it, I shall use it until I can no longer do so."

Em frown "My approach has been called {i}daring{/i} or {i}brave{/i} just as much as it has been derided by others who don't like what I am doing."

Em normal "I'm not sure if this will start a trend or if there will be others who will follow suit, but either way I'll be glad once my term is over."

c "What are you going to do then?"

Em "People who have been on the council usually don't have trouble finding a job to their liking, but I wouldn't even need to do that. I am settled for life and could retire now if I wanted to."

c "Retire? Is that what you would like to do?"

Em "I already feel like I have left my mark and seen everything there is to see in the political landscape, so once this is over, I'd like to settle down for good and start a family."

c "Really?"

Em frown "I'm an only child. My parents want me to make them some grandchildren and to continue the lineage, so all that responsibility rests on me now that I've proven my worth."

c "Is that what you would like to do as well?"

Em normal "In this case, I'll have to agree with them. Frankly, I am tired of all the work. More so than ever before."

Em "Besides, it would be a shame to let everything they built go to waste, don't you think?"

c "What is that supposed to mean?"

Em ques "I'm talking about our family fortune, of course. And what would a family fortune be without a family?"

c "I see."

Em normal "The funny thing is, they were never like this when I was growing up. It was only after they had made it big that they started getting all self-important about it. Illusions of grandeur included."

Em frown "Now that I'm getting older, I'm sad to say that it's not exactly getting easier. I probably would have had better chances if I started a family first and tried to have a career afterwards."

c "Why is that?"

Em normal "Being known like I am has made me popular, but it's making things complicated on the relationship front." 

Em frown "On one hand, there are those that immediately disregard me due to my public image or my politics. On the other, we have those that are only interested in me because of being well-known."

Em "In a way, I'm getting evaluated before I even have a chance of getting to know someone, or before they get to know the person behind the politics." 

Em "No matter if positive or negative, these snap judgments create a sort of proto-relationship that I had no input in and causes them to have certain expectations or opinions about me."

c "I suppose you can't change someone's mind if they have already made it up."

Em normal "Oh, you can. It's just not an easy thing to do. Not that dating isn't already complicated enough as is."

c "Maybe it'll be easier once your term is over. People may not recognize you as much."

Em frown "Maybe. It also doesn't help that there is a rather limited selection for prospective fathers in this town."

c "I didn't even consider that."

Em normal "Maybe I'll return to my home town once my term is over."

c "Can I ask you something?"

Em frown "You have already asked me a lot of things since you came here. I'm sure one more won't hurt."

c "Why did you employ Remy?"

Em "..."

Em "You see, politics is a rather unusual field here. As a pursuit that mostly requires intellectual ability, it is very open to members of any and every species who wishes to apply to such an office."

Em normal "However, the council members themselves are responsible for the workers they employ to help with their office's duties, and that is an area where certain standards and prejudices already start to seep in."

Em "The council members either employ members of their own species, or they pick members of a species that is stereotypically used in that area."

Em frown "Shortly after I came into office, I was faced with the question of who to employ to take care of the archives." 

Em "I didn't really know of a suitable candidate that I wished to employ off the top of my head, so I had to make do with the applicants I received."

Em normal "They were numerous. Among them was a number of hopefuls from my home town who now banked on the idea I would employ someone I already knew or of my own species."

Em "I could have hired one of them, but I had to realize that this decision - my first in the office - would already be under scrutiny."

Em frown "It certainly would have been very unusual to hire an earth dragon to take care of the archives, but I was sure it would have been looked at from a certain angle, with a certain bias."

Em "They would have claimed that I only employed another earth dragon because they belonged to the same species or came from the same town as me. They wouldn't even consider that I made the decision based on merit."

Em normal "With the same biased thinking being present in the applicants, it would have been hard to find anyone among them who was actually suited to the position of working in the archives."

Em "Typically, the position is held by a species with proper hands, as it is often necessary to handle small and precious objects in the archives, but since I typically don't do things the typical way, I wanted to do something different."

Em frown "After I sorted out applicants that only seemed to want to be there to advance their career or to have something important to put on their resume, the remaining number was actually fairly small."

Em "Remy was one that stood out to me from the rest. I wondered about his rationale to even apply for the position, given that it was unheard of for a member of his species to be the caretaker of the archives."

Em normal "Either, he was incredibly naïve, or he knew that his chances were practically nil but was willing to try regardless."

Em "I was curious to find out when I invited him for a job interview."

Em frown "He seemed genuinely enthusiastic and had a passion for the subject, qualities I was looking for."

Em "He also had a background that actually made him well-qualified for the position, at least on paper."

Em normal "Ultimately, he reminded me of my parents and how they managed to break out of their mold and made it big by doing their own thing."

Em "I saw an opportunity that aligned with my own goals."

Em frown "Of course, there were also practical considerations, but I thought with time and practice, and his tireless nature, any difficulties could be overcome."

Em "Maybe he could rise above his peers just like my parents did. I only gave him the same chance. I knew I was making a gamble, but I thought with someone like him, it could very well pay off."

Em normal "Going against every recommendation, guidance and advice I received, I ultimately decided to hire him - a decision that immediately made big headlines."

Em "It was the beginning of the trend that would give me the image I have now. There was a lot of coverage about it, and I think it gave Remy a lot more attention than he wanted."

Em frown "This might have been a good thing if he did his job well, but this didn't turn out to be the case."

Em "The first time he messed up, I made a joke about it and told him that this happens to everyone a few times. If only it had stayed at just a few times."

Em normal "Soon enough, my decision made more headlines from my cynical critics who lambasted me, citing his shortcomings as evidence."

Em "Of course I couldn't go easy on him during that time. He wanted the job, so I held him to the standards of the job. If I treated him any differently, it would've only gotten worse."

Em frown "He might have to work twice as hard, but if he can't do the job, maybe he isn't cut out to do it. But if he can, he'll have proven his worth to the whole town."

c "I heard that isn't working out so well for him."

Em normal "Tell me about it. It's one of my few decisions that haven't ended up working in my favor, even though many people were all for it when it was initially announced."

c "Why don't you just replace him?"

Em frown "That wouldn't be such a good idea. For one, it would only prove the people right who doubt that I made the right choice, and secondly, it would only draw attention to the whole issue all over again."

c "That is unfortunate."

Em normal "Luckily, I make enough headlines these days for it to not matter much anymore."

Em frown "Oh, I'm going to be late for my meeting if I don't hurry up. Would you mind helping me with this?"

play sound "fx/clink3.ogg"

c "{i}Horn Shine{/i}, what's that?"

Em normal "Just some color for my horns."

c "You're painting them? What for?"

Em frown "It's a public outing. Are you telling me you don't do things to make yourself look different?"

c "We do, I just didn't expect your horns would be one of those things."

Em normal "I see. Well, the brush is over there, so get it and get going."

c "Alright."

m "I walked over to her table where I saw the brush among a number of other tools I couldn't quite place and a few stacks of papers. She really hadn't been exaggerating when she had mentioned her workload."

c "Anything I need to know before I start?"

Em frown "Not really. You know how a brush works, don't you?"

menu:
    
    "Sure do.":
        
        pass
        
    "In theory, at the very least.":
        
        pass
        

Em normal "Just so you know, I'll blame you in front of the whole council if you mess it up."

c "Of course."

hide emera with dissolve

play sound "fx/uncork.ogg"

m "I removed the cork from the glass bottle that was filled with a red, somewhat viscous liquid. After dipping the brush into it, I started painting her horn in a bright red."

play sound "fx/brush.ogg"

m "It only took a few applications for the horn to be covered completely."

c "Is that good?"

Em "Oh, we're not done yet. Don't forget my elbow and those on my neck."

c "Alright."

play sound "fx/brush.ogg"

$ renpy.pause (2.0)

c "Here, that should do it."

Em "Let me take a look."

m "She walked up to a mirror and turned her head a few times so she could see herself from every angle."

show emera laugh b with dissolve

Em "Not too shabby, [player_name]. Maybe you would make a good assistant."

menu: 
    
    "Maybe.":

        $ mp.assistant = "maybe"
        $ mp.save()
        
        $ renpy.pause (0.5)
        
    "For you? Anytime.":
        
        $ renpy.pause (0.5)

        Em mean b "Wouldn't that be nice."

        $ mp.assistant = "yes"
        $ mp.save()
    
    "Maybe not.":
        
        $ renpy.pause (0.5)

        Em normal b "You should have a bit more confidence in yourself, [player_name]."

        $ mp.assistant = "no"
        $ mp.save()
    
    
Em ques b "Anyway, how does it look? What do you think about the color?"
    
menu:
    
    "It goes well with your make-up and jewelry.":

        $ renpy.pause (0.5)

        Em laugh b "Oh, thank you. That's exactly what I was going for."
    
    
    "It contrasts nicely with your natural color.":

        $ renpy.pause (0.5)

        Em normal b "That's good to know."
    
    
    "I thought they already looked nice before.":

        $ renpy.pause (0.5)

        Em normal b "Is that so?"
    
        c "Yeah, I don't think you need to paint them."

        Em mean b "Funny you would say that. Actually, they aren't naturally white, either."

        c "Oh, really?"

        Em normal b "Yes, but don't tell that to anyone."
    
    
label emeraskip:

Em ques b "You know what? All that sitting around is making my back so horribly stiff. Would you mind giving me a massage? I could certainly use one right now."
    
$ emeramenu = True

label emeramenu:
    
menu:
    
    "I don't know how." if emeramenu:

        $ renpy.pause (0.5)

        Em normal b "Oh, don't you worry about that. I'll guide you through it."
        
        $ emeramenu = False
        
        show emera ques b with dissolve
        
        jump emeramenu
        
    
    "Not at all.":

        $ renpy.pause (0.5)

        Em normal b "You're a real lifesaver, [player_name]."

        Em frown b "I know it's a strange request, but having to sit in this office for hours on end working through all these papers takes its toll on my body."

        Em "You know, my kind tends to be very physical and I haven't quite gotten used to this office lifestyle yet."

        $ mp.emeraromance = True
        $ mp.save()

        
    "Actually, I should probably get going.":
        
        $ renpy.pause (0.5)

        Em normal b "..."

        Em frown b "Is that so?"

        Em "In that case, don't let me hold you up."

        Em mean b "Thanks for the visit."

        c "Thank you for having me."
        
        if persistent.playedemera == False:

            $ persistent.playedemera = True
            
            $ achievement.grant("The Politician")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_69
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You just met with Emera!"
                
            elif system == "advanced":

                s "You just met with Emera. Good job."
                
            else:
                
                s "You just met with Emera. What an interesting lady..."
        

        stop music fadeout 1.0
        $ renpy.pause(1.0)

        #$ sebastianfail = True

        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars

#show emeramassage with fade

hide emera with dissolve

m "She lay down on a mat and pillow she had quickly produced from somewhere and presented her back to me. I briefly wondered if she kept these items in the office for occasions just like this one."

show emeramassage at Pan((960, 250), (960, 0), 6.0) with fade

$ renpy.pause (3.0)

c "So, what should I do?"

Em "You can start at the neck and work your way down."

c "Well, I don't know much about massaging an earth dragon. What kind of... movements are we talking about here?"

Em "Just put your palms on it and start rubbing in circles. And don't hold back. I assure you we earth dragons can take anything you dish out."

c "Alright."

play soundloop "fx/massage.ogg"

m "I put my hands on her rather girthy neck and did as she told me, rubbing my palms on it in a circular motion."

m "I was about to ask her if I was doing it right when I heard her voice."

Em "Oh, yeah. That is lovely."

Em "Just be careful around the spines. I think we both don't want this to end with an impaled hand."

m "After she had mentioned them, I couldn't help but watch her spines a bit more closely while I continued my ministrations." 

m "They seemed to be made from the same material as the horn on her muzzle. Even though they were not as girthy, they still started out with a rather wide base, ultimately culminating in a point that didn't seem sharp enough to cause any damage by accident."

Em "Hmmmm..."

play sound "fx/buck.ogg"

m "When I resumed my treatment, she suddenly bucked, her spines only missing me by inches when she suddenly threw her head up."

c "(I guess she wasn't kidding about watching out for the spines.)"

show emeramassage at Pan((960, 0), (960, 250), 4.0)

m "Fearing a bit for my safety, I moved down to her shoulders."

Em "Your hands are wonderful, [player_name]."

c "Is that so?"

Em "Mmmm-hmmm. The movements, the incomparably soft skin on your hands..."

c "I'll take it as a compliment."

Em "It most certainly is."

show emeramassage at Pan((960, 250), (960, 500), 4.0)

m "I moved further down to her back, noticing the increased roughness and armor that covered her there."

Em "Don't hold back now, [player_name]. Put your strength into it, or I won't even feel a thing."

m "Following her guidance, I increased the pressure from my palms more and more."

Em "Harder!"

m "I gave it everything I could, and as I kept going at her, I noticed the muscles beneath her armor softening noticably."

Em "You know how to please, dont you?"

menu:
    
    "Apparently, I do...":

        Em "Indeed..."


    "If you say so...":

        Em "I certainly do."

show emeramassage at Pan((960, 500), (960, 800), 6.0)

m "By this point I had moved down to her hips, giving them the same treatment as with the rest of her body."

Em "Yes, that's the spot."

Em "You dont know what having to sit in an office all day does to my hips, [player_name]."

m "Unrelentingly I continued, vowing not to stop until every last knot in her muscles was gone."

Em "Don't stop now, [player_name]. Give it all you got!"

stop soundloop fadeout 0.5

$ renpy.pause (0.5)

play soundloop "fx/massage2.ogg" fadein 1.0

m "I went faster, tenderizing her like a rump steak."


Em "Just like that!"



Em "Yes!"



Em "YES!"

stop soundloop fadeout 1.0

m "And with that, my treatment was done, her hips now as soft and supple as a jello-filled beanbag."

Em "..."

c "..."

Em "..."

Em "..."

Em "..."

c "..."

Em "That was amazing."

c "Thank you."

hide emeramassage 

show emera laugh b

with fade

Em "If you were to open a massage parlor here, you would have no shortage of customers."

c "Is that so?"

Em normal b "Your hands are truly magical, [player_name]. They are a gift. Don't waste it."

c "I'll keep that in mind."

Em frown b "Anyway, I should probably head off to my meeting, and I'm sure you also have places to be, [player_name]."

c "Maybe I'll see you again."

Em mean b "I'm sure of it."

if persistent.playedemera == False:

    $ persistent.playedemera = True
    
    $ achievement.grant("The Politician")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_70

    $ mp.playedemera = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    if system == "normal":
    
        s "You just met with Emera!"
        
    elif system == "advanced":

        s "You just met with Emera. Good job."
        
    else:
        
        s "You just met with Emera. What an interesting lady..."

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
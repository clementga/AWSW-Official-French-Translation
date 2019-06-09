label kevin:

$ kevinunplayed = False
$ kevinavailable = False
if chapter4unplayed == False:
                    
    $ save_name = "Chapter 4 - Kevin"
    
elif chapter3unplayed == False:
    
    $ save_name = "Chapter 3 - Kevin"
    
elif chapter2unplayed == False:
    
    $ save_name = "Chapter 2 - Kevin"
    
else:

    $ save_name = "Chapter 1 - Kevin"

scene black with dissolvemed
$ renpy.pause (0.5)
scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

$ renpy.pause (0.5)

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(That must be him.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

play music "mx/dash.ogg" fadein 2.0

show kevin normal with dissolve

Kv ramble "Hello!"

c "Good to see you again."

Kv normal "This is where you live, huh?"

c "For the time being."

#insert skip here

if persistent.playedkevin == True:
    
    stop music fadeout 1.0

    $ renpy.pause (0.3)

    play sound "fx/system3.wav"

    call syscheck from _call_syscheck_62

    call skiptut from _call_skiptut_15
        
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
            call skipcheck from _call_skipcheck_15
            
            show o2 at Pan((0, 250), (0, 250), 0.1)
            show kevin normal
            with dissolvemed
            
            play music "mx/dash.ogg" fadein 2.0
            
            jump kevinskip
        
        "No. Don't skip ahead.":

            play sound "fx/system3.wav"
        
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"

            play music "mx/dash.ogg" fadein 2.0


Kv ramble "That's pretty nice for a small town like this one."

c "Are you not from around here?"

Kv normal "No, I'm just here for the job until the next semester starts. Basically, I'm trying to drum up interest for the college and see if there's anyone around who'd like to apply for it."

c "How's that working out?"

Kv ramble "Well, I haven't actually met that many candidates out here so far." 

Kv brow "For a town like this one, it's typical for the young people to go into an apprenticeship to prepare for their future job rather than go to college, but if there's anyone willing, we want to find them."

c "Even out here?"

Kv normal "Yeah, there's always a need for more highly educated people in the cities as they expand."

c "Cities? That's the first I hear of cities in this world. I thought this town was where it's at."

Kv brow "Then you've really been missing out. This town isn't really all that special when it comes down to it."

Kv ramble "I've lived in the city for most of my life. Of course, that's also where the college is. I don't think they'd build one out here, anyway."

c "I'd think as ambassador they'd show me around a bit, but apparently that isn't the case."

Kv normal "Your visit is a bit of a political issue right now. The bottom line is that it's also for your own protection."

Kv brow "Everything surrounding the portal has been a well-kept secret. People know that it exists and that we currently have human visitors, but the exact location is only known to those who live here."

Kv "If it ever got out, I don't think this town could face the ensuing torrent of tourists trying to catch a glimpse of you."

Kv normal "Travel has been restricted as well. There are strict conditions for people who want to come out here. The only reason I was allowed to is because this isn't the first time I'm doing this job. The people here already know me."

Kv brow "Heck, I didn't even know this was the town in question until I arrived and heard everyone talking about you."

c "Well, I'm glad they are taking this matter seriously."

Kv ramble "They certainly are."

c "I'd like to know more about these cities you talked about, though."

Kv normal "Well, I can only speak about the one I live in, but what do you want to know?"

c "I only really have this town as a point of reference, so why don't you tell me about what's different?"

Kv face "Gee, that's only pretty much everything."

Kv normal "Out here, living in general seems to be a lot cheaper than it is in the city, and there is much more room for everything." 

Kv ramble "There are green spaces, fields, parks and farms. You don't really see that in the city."

Kv brow "People are more laid-back and there is a bigger sense of community as everybody knows everyone, which can be both good and bad."

Kv "For example, rumors travel fast and survive well in areas like this one. In the city, you can just make new friends when that happens, but out here, a few well-placed stories could mean social death."

Kv ramble "In the city, it's also much more crowded. Buildings pretty much line the streets and there isn't much room for anything else."

Kv normal "But with the clubbing scene and opportunities for socializing, there's no shortage of potential friends."

Kv ramble "There are also many different jobs and education opportunities that you wouldn't find out here."

c "Like what?"

Kv normal "Creative jobs of all kinds, for example. Game designers, writers, artists - that kind of stuff."

Kv ramble "The same goes for teaching positions in those areas as well."

Kv brow "For example, if I wanted to learn how to write a romance novel, I can find a course for that easily. Out here this would be a lot more difficult. You know what I mean?"

c "Yes, absolutely." 

Kv ramble "In a way, it feels like you're always busy when you live in the city. The streets are usually filled with people trying to get somewhere."

Kv brow "Of course, this is also a side-effect of the small apartments as people tend to go out more often and seek entertainment elsewhere."

c "Which do you prefer?"

Kv normal "In the end, I suppose I prefer the city. That's not to say that I think one is better than the other. Different strokes for different folks and all that."

Kv ramble "You know, out here people would probably laugh at some of the things I do in my free time, but in the city, you get enough like-minded people to even get conventions going about all kinds of things."

c "What conventions do you go to?"

Kv "I like all kinds of geeky things. Cartoons, comics and all that stuff. I've even written a few fanfics before too, since I can't really draw all that well."

c "Aren't cartoons usually for kids?"

Kv normal "That's like saying books are usually just for kids. Cartoons are just a medium. Of course there are some that are aimed at kids, but there are cartoons for adults as well."

c "\"Cartoons for adults\". I see."

Kv face "Not like that. Well, I mean, there are cartoons like that, but that wasn't what I was talking about."

c "In any case, what else falls under geeky interests for you?"

Kv normal "Let's see..."

Kv ramble "I guess you could say I'm kind of a techie. I do like following news about technology and hearing all about new developments in the industry."

c "You must be pretty interested in the portal, then."

Kv brow "Oh, right. I didn't even consider that I could actually go there and check it out. If I knew where it was, that is."

c "I could show you."

Kv ramble "If you did that, you'd be like the coolest human I've ever met."

Kv brow "I suppose you'd be that by default, since you're also the only human I've ever met, but you get the idea."

c "Let's just go."

Kv normal "I'll be right behind you."

scene black with dissolvemed

$ renpy.pause (0.5)

scene np1x at Pan  ((200,200), (450,100), 6.0) with dissolveslow

$ renpy.pause (3.5)

c "There it is in all its glory."

show kevin normal with dissolve

Kv "That looks so much cooler than I thought it would."

show kevin at right with ease

show sebastian normal b flip at left with easeinleft

Sb "Halt! State your business."

c "I just wanted to show the portal to my friend here."

Sb disapproval b flip "Well, \"Friend\", you can look, but don't touch anything. And no photos, either."

Kv brow "Do I look like I have a camera?"

Sb normal b flip "Well, you could be hiding something in your fur."

Kv normal "Are you going to give me a pat down?"

Sb disapproval b flip "I don't think so."

Sb normal b flip "What's that, though?"

Kv ramble "Fliers for our Midwest Institution. I could give you one if you're interested in going back to school."

Sb disapproval b flip "No, thank you. I am quite happy with my current job, which is protecting the portal from any unsavory individuals."

c "What's up with you, Sebastian?"

Sb normal b flip "Just doing my job, [player_name]. He could be a spy."

c "Really?"

Sb disapproval b flip "There has been a lot of interest in the portal from the cities. They have made us offers, but for now we're not doing anything until we see how your visit turns out."

Sb normal b flip "In the end, it's just a political power struggle. Small towns like us have to protect our interests."

Kv brow "And in the process, reinforce the stereotype of country bumpkins being conspiracy nuts."

Sb disapproval b flip "You know I could arrest you, right?"

Kv brow "Respect is a two-way street. Just saying."

Sb normal b flip "Trust is good, but control is better. It's just a matter of perspective."

Kv normal "Well, I think I've seen enough here, anyway. Let's head back, [player_name]."

c "Sure."

scene black with dissolvemed

$ renpy.pause (0.5)

scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

show kevin normal with dissolve

c "You're not going to leak anything, are you?"

Kv face "Of course not."

Kv brow "Now that I think about it, I totally could, though."

c "Oh, really?"

Kv ramble "I have some connections and a potential audience."

c "Now you're starting to sound like Sebastian had a point."

Kv "Not really. I just know a few people from writing a column in our college magazine. It got popular enough that it was even featured in the local newspaper for a while."

c "Interesting. What did you write about?"

Kv normal "Nothing special, really. It was just commentary about current events."

c "I see. I guess you were pretty involved in your local community, then."

Kv brow "Not more than anyone else, I think."

c "What's it like to actually live on campus?"

Kv normal "College in general is a pretty unique period of life, I'd say."

Kv brow "Something I've noticed is that some people are not prepared for the independence they have when living on campus."

Kv ramble "You are given a chaotic schedule where you have nothing to do on some days, whereas on others you are kept busy with classes, homework and other things that you have to do."

Kv brow "With study buddies, roommates and classmates it's not really hard to make new friends."

Kv ramble "You also get to meet a lot of people who share similar interests from taking the same classes or being in the same clubs."

Kv normal "And don't forget about the dorms, so all these people are always within reach - which can also be both good and bad. You can be tempted to hang out with friends when you should really be studying."

Kv brow "For many people it becomes the first taste of real freedom and independence. Some just handle it better than others, I suppose."

Kv ramble "That can be a problem with team projects, for example. There's always someone who ends up never showing up and not doing any part of the work."

Kv normal "For me, it's not really a problem since I actually enjoy what I'm doing here. I don't mind the homework, and sometimes, I read up on subjects in advance so I don't get left behind."

Kv brow "I've even corrected the professor once or twice during a lecture."

c "I think that wouldn't be a good idea with certain kinds of professors."

Kv ramble "Well, with ours I was even allowed the privilege of giving a guest lecture for my own class once."

c "Yeah, that's the kind of thing I was talking about."

Kv normal "Come on, learning should be fun! It certainly is for me."

c "I suppose being able to have that kind of attitude makes it a lot easier."

Kv ramble "It certainly does."

c "Let's see if it keeps up once you have a few more semesters under your non-existant belt."

Kv brow "Don't be so negative. And just for your information, I do have a belt at home."

Kv normal "Besides, it's not as if I'm some sort of anti-social hermit who only focuses on his studies. I just know when to say no to my friends."

c "Oh, really?"

Kv ramble "Yes, we usually get together on the weekends and do some cooking together. People can only stand so much frozen food before they get sick of it, and eating out in the city can add up pretty quickly if you're not careful."

c "I see."

Kv normal "We rotate the cook every week, but apparently people are looking forward to when it's my turn. I've gotten a lot of compliments for my homemade mac and cheese."

c "Now you're making me hungry."

Kv ramble "I bet they all miss it, but they'll get to taste it again once summer vacation is over in a month or so."

c "And in the meantime, you're just out here handing out fliers?"

Kv brow "Yep. It's good to help our college, and I can also save up a bit in the process. It's certainly easier than trying to juggle a job and homework at the same time later on if things get tight."

c "What were you studying again?"

Kv normal "Psychology."

c "I see."

c "Alright, go ahead and analyze me right now."

Kv "..."

Kv face "It doesn't really work like that."

c "I know. You just passed the test."

Kv brow "Oh, I know what you're getting at."

Kv ramble "Maybe I'll steal that test from you, though. Might be worth trying it out on a few people I know."

c "Be my guest."

c "On a more serious note, tell me something about what you're learning."

Kv brow "What, anything?"

c "I just want to get an idea of the subject, and whether it's comparable to our own understanding of psychology."

Kv normal "I see."

Kv ramble "Well, I could tell you about an old and very simplified model of our psyche that we got taught in introductory classes."

c "Sounds good."

Kv normal "Okay, so this model divides our psychic apparatus into three distinct parts, called {i}id{/i}, {i}ego{/i} and {i}super-ego{/i}."

Kv ramble "The {i}id{/i} represents our most basic desires and instinctual drives. That is, our physical needs and wants - like hunger and thirst - as well as desires and impulses."

c "What's the difference?"

Kv normal "An impulse is more like wanting to lash out in anger, for example. The id seeks out immediate gratification for these urges."

Kv brow "It is in conflict with the {i}super-ego{/i}, which represents learned behavior like cultural and moral rules, and societal standards. The kind of stuff we learn from our role models like parents, teachers or guardians."

Kv ramble "The super-ego is the part that forms our conscience and controls our sense of right and wrong. It seeks to uphold these standards to perfection, which most of the time goes against what the id wants at any given moment."

c "You sound like you had to rote-learn a lot of this."

Kv normal "If those internalized rules are broken, this misbehavior is punished by the super-ego with feelings of guilt and shame. This way, we are compelled to behave in accordance to these rules even if the id tempts us to do otherwise."

Kv ramble "And inbetween these two conflicting parts of us, there is the {i}ego{/i} who is trying to mediate."

Kv "It represents our rational mind that seeks to please the id's drives in a way that doesn't harm us or goes against the super-ego's goals."

Kv normal "However, it also serves another master - the external world."

Kv "The ego includes all our decision-making and how we respond to external stimuli. Ultimately, it is the one calling the shots while trying to balance the needs of the id, the super-ego and the external world."

Kv ramble "And there you have it - an outdated, simplified model of our psyche. It still serves as a good introduction, though."

c "Thank you. Actually, I think I may have heard about something like this before..."

#end

c "Why did you go with psychology in particular?"

Kv brow "I'm just interested in how people work, I suppose."

Kv normal "It's also an incredibly diverse subject - and so are the potential jobs." 

Kv ramble "Just being able to understand people is such a huge factor in many fields, and the skills you learn can come in handy in all areas of life, really."

Kv brow "When people hear about psychology, most usually think of psychologists or psychotherapists, but they can also be counselors for communities and organizations, researchers or teachers."

Kv normal "You also often see them teaming up with other professionals to influence every part of society. Just think about hospitals, courtrooms, prisons - even schools and universities."

Kv ramble "They can also become coaches for high-performance jobs where they work with CEOs, athletes and performers of all kinds."

Kv normal "Every institution and every business that works with people can profit from the presence of someone who has studied psychology." 

Kv ramble "That's why you'll also find this kind of knowledge to be incredibly helpful even when you are a manager or in sales, because those jobs require empathy and an understanding of your client's needs."

Kv normal "Understanding people is just something that can come in handy pretty much wherever you go, and that's what psychology is all about."

Kv ramble "Even in video games, psychology is a factor. Horror games are an obvious example, but also with tutorials or UI design and how people interact with your game, psychology and player expectations are always going to be a factor."

c "I think I get the idea."

Kv normal "Out here, I think a lot could still be done to improve the image of the field, you know."

c "What do you mean?"

Kv brow "There is a bit of a stigma to admitting that you need help, especially when you're doing fine physically."

Kv normal "For them, it's a sign of weakness, so in order to preserve their image, they hide everything away. But locking away those feelings doesn't solve the problem. If anything, it only makes it worse."

c "Is that something you'd like to work with?"

Kv face "Me? Honestly, I don't know if I could tackle a big issue like that. It's good for me that psychology is such a diverse field, because I'm not quite sure where I'm going with it yet, or what particular job I'd like to have after I'm done with my studies."

c "I see. I think you still have plenty of time to figure that out."

Kv brow "Yep. Before I came here for my summer job, I was interning at a psychotherapist's office for a month. I got to hear about some very interesting and also tragic cases." 

Kv "I thought I wanted to help people with issues like that, but sometimes it's pretty hard not to be affected too much by those stories, so I'm not sure if that's the right job for me."

c "But you already like working with people, right?"

Kv face "I don't know. Maybe interning there was a little too close to the sun for me."

c "If you didn't, why would you be the one to hand out the fliers?"

c "It's just like you mentioned earlier - psychology comes in handy with sales and similar jobs where you have to interact with people. Handing out fliers is pretty similar to that, don't you think?"

Kv normal "I guess."

c "You seem to be doing well enough with that. You're helping to bring your college and people together, and in this way, you're helping both."

Kv ramble "And it's been a lot of fun, too. After all, I got to meet you and even got a glimpse of the portal."

c "Who knows, maybe one of those people you handed a flier will one day turn out to be famous for their work."

Kv normal "Now, I think that's a little too idealistic, but I get your point."

Kv "It doesn't always have to be about big problems. Little problems need solving, too."

c "Like what you're eating on the weekend."

Kv ramble "Hahaha, yeah."

Kv brow "What about you, though?"

c "What do you mean?"

Kv normal "Well, I don't want to pry, but we've been talking all this time and you know a lot more about me now than I do about you."

Kv brow "Maybe you can't say anything about where you grew up or what you studied because it's top secret or whatever, but I'd be lying if I said I wasn't curious."

c "Well, I don't like talking about myself all that much, and I think there are some things that are better left unsaid."

Kv normal "I see."

c "But if you're curious, I guess it's only fair I share a few things as well."

c "You know, it's been fun talking about college. I already got my degrees a while ago."

c "It was interesting to go hunting for jobs with my unusual combination of degrees, but I thought that would open a few doors."

c "But before I got anywhere, our world underwent a few changes that made a lot of jobs obsolete."

c "It's been a rough time since then."

c "Turns out those degrees came in handy after all, because in the end they enabled me to come here."

c "If I consider all the good and bad that's happened here since my arrival, it's been a vacation compared to home, and it looks like the vacation might come to an end soon."

c "I dont know whats going to happen after that. I can only hope my visit here will have started something that will mean change for our world, but I'm not sure if that's going to happen."

c "I shouldn't be such a downer, though. Sorry for bringing it up, but maybe that explains why I don't like talking about it."

c "What's your professional opinion on this?"

Kv "Well, in my professional opinion as a flier distributor, I'd recommend a generous application of hugs, but that's just me. You look like you could need them."

menu:
    
    "I don't think that will be necessary.":
        
        pass
        
    "Go for it.":
        
        $ renpy.pause (0.5)
        
        hide kevin with dissolve

        play sound "fx/undress.ogg"
        
        m "He took a step forward, and I soon found myself being enveloped in the furry dragon's embrace. With him pulling me close, it felt like a giant, furry blanket was all around me as the hairs tickled my exposed skin."
        
        m "After a few seconds, we parted and he took a step back again."

        $ mp.kevinromance = True
        $ mp.save()
        
        
show kevin normal with dissolve

Kv "I hope things can be better for you in the future. I don't think I can do anything to help with that, though."

c "I know. You prefer the little problems."

show o2 at Pan((0, 250), (0, 250), 0.1) behind kevin with dissolveslow

$ renpy.pause (0.5)

label kevinskip:

Kv face "It's getting dark. I should probably head out and look for a cave, or else I'll have to sleep in the streets."

c "What are you talking about?"

Kv normal "Well, it seems like all the hostels are already full. Despite the vetting process for visitors, enough people got in to take all available short-term lodging spots in this town."

c "Oh, really?"

Kv brow "Yep. Despite only a few people knowing your location, or that of the portal, journalists and tourists are flocking to the towns, hoping to catch a glimpse, or at least find a clue of your whereabouts."

Kv face "That only leaves me with the option of finding or renting a cave for the night, or sleeping in the streets."

Kv ramble "Not that I'd mind sleeping in a cave, but for someone like me it's usually something for an adventurous weekend rather than a way of life. And rocks don't exactly make for the best bedding."

menu:
    
    "You could sleep here.":
        
        $ renpy.pause (0.5)
        
        Kv brow "Really?"

        c "Yeah. There's plenty of room here and it's kinda my fault that you couldn't find another place, anyway."

        Kv ramble "I guess that means you don't share the officer's suspicions about me being a spy, then."

        c "Not really."

        Kv normal "You know, I could totally take this room apart while you're sleeping."

        c "You're not helping your case there. Besides, you won't really find anything special here."

        Kv ramble "Hey, I'd keep an eye on that copy of \"Draconic Desire\" you've got on the shelf there. I might be tempted to snatch it when you're not looking."

        c "Like I'd mind. If you need something for bedtime reading, feel free to help yourself."

        Kv normal "Oh, I will."
        
        if persistent.playedkevin == False:

            $ persistent.playedkevin = True
            
            $ achievement.grant("The Student")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_63

            $ mp.playedkevin = True
            $ mp.save()
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You met with Kevin!"
                
            elif system == "advanced":

                s "You met with Kevin and learned a lot about city and college life. Congratulations."
                
            else:
                
                s "You met with Kevin and learned a lot about city and college life. Now you're prepared for a possible life at dragon college, I guess."
        
        
        #$ renpy.pause(1.0)
        
        stop music fadeout 2.0

        if chapter4unplayed == False:
                    
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars

    
    "Well, you better get going, then.":

        $ renpy.pause (0.5)
        
        Kv face "Yeah, I should head out before it gets too dark to see anything. This town doesn't really have the best lighting at night, either."

        c "Good luck with your search."

        Kv normal "You too."
        
        hide kevin with dissolve

        stop music fadeout 2.0
        
        play sound "fx/door/doorclose3.wav"

        $ renpy.pause (2.0)

        if persistent.playedkevin == False:

            $ persistent.playedkevin = True
            
            $ achievement.grant("The Student")
            
            $ persistent.achievements += 1
            
            call syscheck from _call_syscheck_64

            $ mp.playedkevin = True
            $ mp.save()
            
            play sound "fx/system.wav"
            
            if system == "normal":
            
                s "You just met with Kevin!"
                
            elif system == "advanced":

                s "You just met with Kevin and learned a lot about city and college life. Congratulations."
                
            else:
                
                s "You just met with Kevin and learned a lot about city and college life. I don't know what else to say about this."

        if chapter4unplayed == False:
                                
            jump chapter4chars
            
        elif chapter3unplayed == False:
            
            jump chapter3chars
            
        elif chapter2unplayed == False:
            
            jump chapter2chars
            
        else:

            jump chapter1chars



















label remy5:

show black with dissolvemed
$ renpy.pause (0.5)
scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow

$ save_name = "Chapter 5 - Remy"

play sound "fx/door/doorbell.wav"
$ renpy.pause(1.0)

c "(That must be him.)"
stop sound fadeout 0.5
$ renpy.pause(0.4)
play sound "fx/door/handle.wav"
$ renpy.pause(1.0)

show remy normal with dissolve

Ry "Are you ready to see the fireworks?"

c "My body is ready."

Ry smile "Alright, let's go."

scene black with dissolvemed
$ renpy.pause (0.5)
scene viewingspot with dissolvemed

play music "mx/amb/night.ogg" fadein 5.0

m "After a few minutes of walking, we arrived at a rather empty looking area near the edge of town."

c "Looks deserted to me. I thought everyone was watching the fireworks."

show remy normal with dissolve

Ry "They are, but they're doing it somewhere else. I don't really like the crowds, and I think you would appreciate me leading you here if you knew what they were like."

c "Better be safe than sorry, at any rate."

Ry smile "That's what I'm thinking."

c "This reminds me a bit of the night I arrived here. Everything was dark and empty, and it was just us walking through the landscape."

Ry normal "Yeah, you're right."

Ry "Oh, I think it's starting. Now, watch!"

play soundloop "fx/fireworks3.ogg"

m "We were quiet as we waited and the stillness of the night enveloped us. Soon, I heard the sound of the first rocket making its way into the night sky after which it exploded in a pattern of colors."

m "More rockets followed, their thunderous noise echoing throughout the land."

show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow
$ renpy.pause (6)
#hide fireworks with dissolveslow


stop music fadeout 2.0

hide fireworks with dissolveslow

#stop music fadeout 2.0

#hide fireworks with fade

m "Suddenly, a terrible realization hit me."

play music "mx/judgement.ogg" fadein 0.5

m "Considering how public of an event this was and how I was told multiple times that everyone would be watching the fireworks, now would be the best time for Reza to do anything he planned to do."

m "Not only was the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever have."

m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."

c "Remy, I think we need to go. Now."

Ry "What is wrong, [player_name]?"

c "I know where Reza is. We need to stop him."

Ry sad "Shouldn't we call the police or something?"

c "We don't have the time!"

Ry shy "I'm not sure if I could fight him."

c "You're right. If you're there, he probably won't hesitate to shoot."

Ry sad "Maybe you can hold him off, and I'll try to get some help."

c "Alright, let's do that. Go!"

hide remy with dissolve

m "I started running as Remy's voice called out to me."

Ry "Where is he? Where should I go?"

c "The portal! He'll be there."

#copied passage

scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow

$ renpy.pause (3.5)

#call function here

call endingjustafewminuteslater from _call_endingjustafewminuteslater_2

#end copied passage

Mv "Maybe I can."

play music "mx/fervor.ogg" fadein 0.5

m "Suddenly, Maverick and Remy appeared next to me."

show reza at Position(xpos=0.9, xanchor='center') with ease

show maverick normal flip at Position(xpos=0.2, xanchor='center') with easeinleft

show remy look flip at Position(xpos=0.05, xanchor='center') with easeinleft

Rz angry "You planned this, didn't you, [player_name]?"

#Rz "Traitor!" with Shake((0, 0, 0, 0), 2, dist=10)

Rz "Traitor!" with hpunch

Rz "And to think I let you distract me with such a cheap trick! Just because I thought there was still a shred of humanity within you..."

play sound "fx/rev.ogg"

show reza gunself with dissolve

show reza gunpoint with dissolve

m "He pulled out his gun, not sure which one of us he should be aiming at."

Rz "Just let me go, and I'll forget this thing ever happened."

c "You've got six bullets for three people. Do you think you can really do that, Reza? Do you think this is worth risking your life for?"

Rz angry "I've been risking my life for this every day for the last two weeks. What did you do during that time? Sip champagne in your nice apartment?"

Rz "Besides, this generator and the whole building came from our time."

show izumi normal behind reza at Position(xpos=1.25, xanchor='center')
Rz "They belong to humanity!" with Shake((0, 0, 0, 0), 2, dist=10)

#Rz "They belong to humanity!" with hpunch
show reza at Position(xpos=0.45, xanchor='center')
#show izumi normal at right 
show remy at Position(xpos=-0.3, xanchor='center')
show maverick at Position(xpos=-0.3, xanchor='center')
with ease

m "Suddenly, the Administrator came out of the shadows in the hallway behind Reza."

show izumi normal at right with ease


As "No, they belong to me."

#$ renpy.pause (0.3)

play sound "fx/rev.ogg"

show reza angry flip

m "Confused, Reza spun around, aiming his gun at the newcomer who was slowly walking towards him."

Rz "Who the fuck are you? Freeze! I said freeze!"

show izumi at Position(xpos=0.8, xanchor='center') with ease

As "Want to waste your bullets on me? Feel free. You can't stop all of us."

play sound "fx/rev.ogg"

Rz gunpoint flip "If you say so."

play sound "fx/gunshot2.wav"

$ renpy.pause (0.5)

play sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/silence.ogg"
queue sound2 "fx/impact3.ogg"

hide izumi with easeoutbottom

m "He pulled the trigger, and the Administrator fell to the ground with a dull thud that knocked her mask off."

$ persistent.izumiseen = True

show izumiinjured4 at Pan((300, 0), (600, 608), 7.0) with fade

$ renpy.pause (5.0)

hide izumiinjured4 
show maverick at Position(xpos=0.2, xanchor='center')
show remy at Position(xpos=0.05, xanchor='center')
show reza at Position (xpos = 0.9, xanchor = 'center')
with fade

m "Mortified by the display before me, I found myself unable to move as the events of the following seconds unfolded before my eyes."

show reza gunpoint at Position (xpos = 0.9, xanchor = 'center')

play sound "fx/gunshot2.wav"

$ renpy.pause (0.5)

hide remy with easeoutbottom

m "Reza was quick with his gun and shot Remy once before Maverick could charge him."

play sound "fx/snarl.ogg"
show maverick angry flip with dissolve

$ renpy.pause (1.0)


#show maverick at Position(xpos=0.6, xanchor='center') with move6
#hide reza with easeoutbottom

#hide reza
#hide maverick
#with dissolve

show maverick at Position(xpos=0.65, xanchor='center') with move6

play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top") 
show reza at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top") 
with move9

#$ renpy.pause (2.0)

queue sound "fx/bite.ogg"

m "Maverick pounced, snarling, and knocked Reza to the ground before embedding his teeth into the body before him."

play sound "fx/gunshots4.ogg"

#hide maverick with dissolve

m "Despite his thrashing and screaming, Reza managed to find his target and pulled the trigger twice."

m "Immediately, the jaws dislodged. Reza pulled himself a few feet away while Maverick's body convulsed uncontrollably."

show reza annoyed b at center with dissolve

m "Holding his bleeding wound and breathing heavily, Reza looked at me."

Rz "You're not going to help me, are you? Then it is futile."

play sound "fx/rev.ogg"
show reza gunself b with dissolve

m "He raised his gun, aiming at me while I regained my composure and tried to run."

hide reza with dissolve

play sound "fx/gunshot3.ogg"

queue sound "fx/impact3.ogg"

play sound2 "fx/silence.ogg"

queue sound2 "fx/silence.ogg"

queue sound2 "fx/silence.ogg"

queue sound2 "fx/trigger2.ogg"

queue sound2 "fx/trigger1.ogg"

queue sound2 "fx/trigger1.ogg"

queue sound2 "fx/trigger1.ogg"

$ renpy.pause (0.5)

m "A single gunshot resounded through the hallway, and as soon as I heard it, a sharp pain shot through my back. I fell to the ground immediately." with hpunch

m "He continued pulling the trigger, but no more bullets came."

stop music fadeout 2.0

m "After a few seconds of silence, I slowly turned around."# and saw him with his head slumped."

show rezabitten at Pan ((100, 56), (0,0), 7.0) with fade

play music "mx/movingon.ogg" fadein 0.2

$ renpy.pause (3.0)


m "Reza was leaning against the wall, his head slumped forward lifelessly."
#hide rezabitten with fade

show maverickdead4 at Pan((140, 0), (0,79), 7.0) with fade

$ renpy.pause (5.0)

show izumidead4 at Pan((0, 0), (140,79), 7.0) with fade

$ renpy.pause (3.0)

m "Maverick and the Administrator - both lying in a pool of their own blood - were not moving."

hide izumidead4

hide maverickdead4

hide rezabitten

with fade


m "I crawled over to Remy and was glad to hear him breathing."

m "He had been hit in the side, and I saw blood trickling from the wound onto the ground below him."

show remy shy with dissolve

m "He raised his head, looking at me with an expression of pain."

c "You're wounded."

Ry "So are you."

c "We need to stop the bleeding."

m "I put some pressure on his wound, momentarily halting the blood that was trickling down his body."

c "Can you do this?"

Ry "Let me try."

m "He felt around his side, trying to get the right grip before he applied pressure on his own. I let go, and after a bit of adjustment, Remy could stop the bleeding on his own for now."

m "I took off my shirt and briefly considered whether I would be able to use it to dress Remy's wound, but I soon realized it was not long enough to wrap around him properly."

m "Besides, if he couldn't walk for now, it would not make a difference anyway, and he would have to stay here while he held his wound shut."

m "Instead, I used the shirt to curb my own bleeding, folding it and wrapping it around my abdomen tightly."

Ry "Look, Reza is gone... and that other person."

m "Remy was right. Both Reza and the Administrator were gone."

Ry "You have to go. Go and stop Reza."

c "I need to find you some help first. I can't just leave you like this."

Ry "..."

show remy angry with dissolve

Ry "Don't you dare tell me you would be doing me any favors by saving me. If it's just going to be one of us, I don't want it to be me." with Shake((0, 0, 0, 0), 3, dist=10)

Ry shy "You don't know how it is to live every day as I have, always wondering if the pain will ever stop or if things will ever change again."

Ry "And when they finally do, you come along and tell me this? Don't do that to me."

Ry "I'm not going through this again."

c "What do you want me to do?"

Ry "This is bigger than us... bigger than me."

Ry "Just... go."

Ry "Go and stop Reza."

c "Alright."

if remygoodending == True:

    if persistent.endingsseen == 0:
        
        pass
    
    else: 
    
        jump remygoodending
    
else:
    
    pass

scene black with dissolvemed
$ renpy.pause (0.5)
scene np2y at Pan ((0, 100), (0, 100), 0.0) with dissolvemed

m "I hobbled to my feet and made my way back outside, just in time to see Reza vanishing through the portal."

scene black with dissolveslow

$ renpy.pause (2.0)

nvl clear

window show

n "I made my way back to Remy to look for something to treat his wound. Given everything that had just transpired, I had no idea what was going to happen."

n "I also wondered where the Administrator had gone."

n "I checked a few of the rooms and even found a first aid kit that I used to treat both of us."

n "Soon, however, I heard steps behind me. As I turned around, I was surprised to see another human face."

n "It was a soldier."

n "\"Who are you? What are you doing here?\", I asked him."

n "\"We're here to save you. Reza told us about everything.\", he replied."

window hide
nvl clear
window show

n "I didn't know what Reza had told them, but I certainly didn't want to leave just yet. I tried to protest and told them about Remy, and the soldier let me know that they would take care of it. For now, however, their orders were clear and I was to come with them immediately."

n "Another soldier arrived and took the generator with him. Then, they escorted me back through the portal."

n "After all this time, I wondered what would happen now - to our world and the dragons'."

n "I arrived on the other side, only to be met by a team of EMTs who were already expecting me."

n "I was urged to lay down in a cot, which was quickly transported into the back of an ambulance."

window hide
nvl clear
window show

n "They took off my bandages and examined my wounds as I heard them calling out medical terms I didn't understand."

n "A breathing mask was put on me, and soon, I lost consciousness."

n "I wasn't sure what exactly Reza had told them, but with him dead and me wounded, humanity decided to take what they thought was theirs by force - which included the underground building itself."

n "Hoping for a diplomatic solution, the dragons retreated and borders were established, all within a manner of days."

window hide
nvl clear
window show

n "The thousands of people living in our city were quickly relocated. For them, it was a better solution than any other. Here, they had an already working infrastructure, buildings, and things looked just like they used to."

n "When I awoke from my induced coma, it was with the expected dose of confusion as I had to realize the place was deserted, and it hadn't been just the building - it was the entire city. Everyone was gone."

n "Whatever Reza had told humanity had been enough for them to ultimately decide to leave me behind as a traitor while they sought out their promised land."

window hide
nvl clear
window show

n "To their credit, they could have killed me, but just leaving me behind and to my own devices was exactly the kind of punishment I would expect from them."

n "I wasn't even sure how much time had passed since I returned."

n "While they had permanently disabled the portal, I was at least able to find plenty of supplies they had left behind as I roamed the city to make a new life for myself."

n "After a few days of checking building after building and getting to know my new surroundings, I was surprised to see a shadow flying overhead."

n "It was a dragon."

stop music fadeout 2.0

window hide

nvl clear

$ renpy.pause (2.0)

show city at Pan ((0, 360), (0, 0), 7.0) with dissolveslow

$ renpy.pause (5.3)

c "Hey!" 

m "Blinded by the sun, I couldn't quite make out the dragon before it landed and approached. It was Remy."

show remy normal with dissolve

play music "mx/prayer.ogg"

c "Remy! What are you doing here?"

Ry "I've been looking for you for the last few days. Honestly, I wasn't sure whether I was going to find you at all."

c "I don't even know how long it's been since I last saw you."

Ry "It must have been a few weeks."

c "Why did you come here?"

Ry shy "We need you. You have to tell them what really happened. What Reza did, and everything else."

Ry "After you went back, the soldiers found me and I was interrogated."

Ry "When they were negotiating with our council, they realized that Reza's account of what happened here differed a lot from what really went down. Of course there are a lot of blanks they need to fill in, too."

Ry "They needed to find someone who was willing to go back to find you, so I did."

Ry normal "Besides, I owed it to you for everything you've done for me."

c "Remy..."

Ry "I guess they realized the error they made by leaving you behind, but now all of us need you as a witness. You must tell them the truth."

c "How is your wound?"

Ry "It's fine. I was patched up pretty well, all things considered."

Ry "Come on, we've got no time to lose."

c "The portal is just around the corner, but how are we going to get back? They deactivated it."

Ry "I know, that's why they gave me something to repair it."

c "Let's go, then."

scene black with dissolvemed
$ renpy.pause (0.5)
show city at Pan ((0, 0), (0, 0), 0.0) with dissolvemed

m "A few minutes later, we arrived at the portal. I thought about alternative options, considering we would be able to use it now."

m "Time travel came to my mind, and while I knew about the portal's capabilities to do so, I had no idea how."

m "Either way, I would do what I could to make things right."

m "I watched as Remy reactivated the portal, using its interface with his somewhat clumsy paws."

show remy normal flip at Position (xpos = 0.4) with dissolve

Ry look flip "Something's not right here. It can't find the other portal."

m "A terrible realization hit me as I considered, hoped for other possibilites."

c "You said it was a few weeks since I last saw you, right? And you've been looking for me for how long? A week?"

Ry normal flip "Yes."

c "Remy, I think I've got some very bad news."

Ry look flip "What is it?"

m "Suddenly, I heard someone approaching us from behind, and after I turned around, it was the Administrator who stood before us."

show remy at left with ease

if persistent.annabadending == True:

    show izumi normal 4 scar at Position (xpos = 0.85, xanchor='right') with easeinright
    
else:
    
    show izumi normal 4 at Position (xpos = 0.85, xanchor='right') with easeinright

As "I have finally found you." 

As "Come on, we need to go back. "

c "Back? They're all gone."

Ry "What are you talking about?"

As "In the time you were here, the meteorite you knew about collided with Earth. The civilization you knew, and the human settlement are no more."

Ry shy flip "What? How?"

c "Reza knew this was going to happen."

As "How ironic that Reza would drag himself through the portal in his gravely injured state to try and save humanity by telling them about the generator, you and the meteorite, only to fall on deaf ears about that last, crucial part."

As "Now, they are all gone."

As "I wasn't talking about returning to them, however, but going back to a time even before that - the day of your arrival."

Ry normal flip "You want to use the portal for time travel? I knew about the possibilities, but doing it for real... fascinating."

c "Can Remy come with us?"

As "No. It is complicated enough as it is."

c "Then I don't want to go."

As "I don't think you realize what is at stake here. All the others you have met are dead. Their whole civilization was wiped out in one fell swoop, and their world lies in ashes. Only we can go back and try to prevent this from ever happening."

c "But..."

Ry shy flip "It's alright, [player_name]. Just go. You have to save them."

As "That is my utmost goal."

c "Alright, I'll do it."

As "Very well. Take your position, please."

hide izumi
hide remy
with dissolve

m "I stood in the middle of the portal, and after pressing a few buttons, the Administrator joined me."

if persistent.annabadending == True:

    show izumi normal 4 scar with dissolve
    
else:
    
    show izumi normal 4 with dissolve

c "What should I call you?"

m "She looked at me with a mild expression of bewilderment."

c "Now that you don't wear the mask anymore, we can do without the code name."

As "You can call me Izumi."

m "I could see the faintest hint of a smirk."

Iz "Not that it matters much. Once we arrive on the other side, you probably won't remember a thing."

hide izumi with dissolve

play sound "fx/tel.wav"

$ renpy.pause (2.0)

show remy shy b with dissolve

m "As I heard the familiar sound of the portal starting up, the last thing I saw was Remy watching us as he slowly undid his tie and slipped it off his neck."


#cgs shown contain adine as a hint?

$ _game_menu_screen = None

stop music fadeout 2.0

#scene black with dissolvemed

#nvl clear

#window show

#$ renpy.show("port1")
#$ renpy.transition(Dissolve(2))

#play sound "fx/telstart.ogg"
#play sound "fx/tel.wav"

#n "{cps=40}Not the time of dragons or man, but the time of [player_name] had come.{/cps}{nw}"

#scene port2 with dissolveslow
#scene port1 with dissolve
#scene port2 with dissolve
#scene port1 with dissolve
#scene port2 with dissolve
#scene port1 with dissolve
#scene port2 with dissolve
#scene port1 with dissolve


#$ renpy.pause (2.0)

stop sound fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

$ renpy.block_rollback()

play sound "mx/movingon.ogg"

$ renpy.pause (0.8)

show rezabitten at Pan ((-500, 56), (-200,0), 24.0)
show credits1 at left
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

show remyapt at Pan ((0, 170), (600, 0), 24.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

#show cgemera at Pan((-600, 0), (-600, 302), 25.0) 
show remysad at Pan ((-250, 326), (430, 0), 25.0)
show credits5 at left 
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed
#stop movie

#

show cgvara at Pan ((0, 326), (1580, 0), 25)
show credits7 at right 
with dissolvemed

$ renpy.pause (10.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

#

show cg1 at Position(xpos=0.8, xanchor='center')
show credits9 at left 
with dissolvemed

$ renpy.pause (10.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (10.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (9.0)

scene black with dissolvemed

stop sound fadeout 2.0

$ renpy.pause (4.0)

$ persistent.lastendingseen = "bad"

$ persistent.endingsseen += 1

call izumimask from _call_izumimask_3

if persistent.remybadending == False:

    $ persistent.remybadending = True
    
    $ achievement.grant("Alone")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_71

    $ mp.remybadending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Remy's bad ending!"
    

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "remy"
    
    jump tut
    
else:

    jump mainmenu


#good ending starts here

label remygoodending:
    
scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r flip at Pan((400, 0), (100, 100), 6.0) with dissolvemed

$ renpy.pause (3.5)

m "I hobbled to my feet and made my way back outside. In the distance, near the portal, I saw Reza and something that was standing between them."

show reza angry b at center with dissolve #at Position(xpos=0.85, xanchor='center') with dissolve

m "As I drew nearer, I recognized it as Vara who was growling at him."

play sound "fx/varagrowl.ogg"

show vara growl flip at left with dissolve

m "Reza aimed a kick at her, only to lose his balance and fall when she bit and held onto his shin."

show reza at Position(xpos=0.4, xanchor='center') with ease

play sound "fx/bite.ogg"

$ renpy.pause (0.5)

show reza at Position(xpos=0.4, xanchor='center', ypos=1.0, yanchor='top')
show vara at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='center')
with ease

#$ renpy.pause (0.5)


m "After he fought her off with a few kicks, his hand dove into his pocket to grab a few bullets, which he proceeded to load into his revolver."

play sound "fx/hit2.ogg"

show vara at Position(xpos=-0.10, xanchor='left', ypos=0.90, yanchor='center')
with ease

play sound "fx/hit2.ogg"

queue sound "fx/reload.ogg"

show vara at Position(xpos=-0.20, xanchor='left', ypos=0.80, yanchor='center')
with ease

#play sound "fx/rev.ogg"
#queue sound "fx/gunshot2.wav"


m "I went as fast as I could, but with my injuries I had no chance to stop him as he aimed at Vara."

play sound "fx/rev.ogg"

$ renpy.pause (0.5)

queue sound "fx/gungore.ogg"

show vara shocked flip with dissolve

#show reactionshocked at Pan ((200, 0), (100,0), 6.0)
#show reactionnone at Pan ((200, 0), (100,0), 6.0)
#show reaction5 at Pan ((100, 0), (200,0), 6.0)
#show reaction4 at Pan ((100, 0), (200,0), 6.0) 
#show reactionnormal at Pan ((200, 0), (100,0), 6.0)
#show translucent
#with dissolve

#$ renpy.pause (7.0)

#show reaction4 at Pan ((150, 0), (150,0), 6.0)
#show reactionnormal
#with dissolve

#$ renpy.pause (0.5)

#play sound "fx/bulletimpactsl2.ogg"

#hide reactionnormal
#show reactionnone
#with dissolve

#$ renpy.pause (0.5)

#hide reactionnone
#show reactionshocked
#with dissolve

#$ renpy.pause (0.5)

#hide reaction4
#hide reaction5
#hide reactionshocked
#hide reactionnormal
#hide reactionnone

#with dissolve

$ renpy.pause (1.0)

play sound "fx/silence.ogg"
#queue sound "fx/silence.ogg"
queue sound "fx/varafall.ogg"

hide vara with easeoutbottom

$ renpy.pause (1.0)

hide reza
show reza annoyed b at center with easeinbottom

$ renpy.pause (0.3)

show reza at Position(xpos=0.4, xanchor='center') with ease

$ renpy.pause (0.3)

show reza at Position(xpos=0.3, xanchor='center') with ease

$ renpy.pause (0.3)

show reza at Position(xpos=0.2, xanchor='center') with ease

#show izumi normal at center with easeinbottom

#show izumi at Position(xpos=0.3, xanchor='center') with ease

m "Slowly, he got up again and walked over to the portal's controls when the Administrator suddenly appeared behind him."

if persistent.annabadending == True:

    #show izumi normal 4 scar at center with easeinbottom
    show izumi normal 4 d at center with easeinbottom
    
else:
    
    #show izumi normal 4 at center with easeinbottom
    show izumi normal 4 c at center with easeinbottom

#show izumi at Position(xpos=0.3, xanchor='center') with ease
#cts

#show maverick at Position(xpos=0.65, xanchor='center') with move6

#play sound "fx/impact3.ogg"

#show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top") 
#show reza at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top") 
#with move9


#show izumi at Position(xpos=0.3, xanchor='center') with ease

show izumi at Position(xpos=0.3, xanchor='center') with move6

play sound "fx/impact3.ogg"

play sound2 "fx/silence.ogg"
#queue sound2 "fx/silence.ogg"
#queue sound2 "fx/silence.ogg"
#queue sound2 "fx/silence.ogg"

queue sound2 "fx/rolldownhill.ogg"

show izumi at Position(xpos=0.2, xanchor='center', ypos=1.0, yanchor="top") 
show reza at Position(xpos=0.1, xanchor='center', ypos=1.0, yanchor="top")
with move8


#hide reza
#hide izumi
#with dissolvequick


m "Immediately, she was on him, throwing him to the ground before starting to pound his head with her fists. Together, they rolled down the slope of the small hill on which the portal stood."

play sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/silence.ogg"
queue sound "fx/hit2.ogg"
queue sound "fx/gunshot2.wav"


m "When they came to a halt, the fight resumed. There was a flurry of fists, and suddenly, I heard the distinct sound of a gunshot, after which the Administrator slumped and fell."

m "Eventually, I arrived, only to be able to confirm that both of them were dead."

m "I went up to the portal and examined Vara for any signs of life. I found none."

show remy shy with dissolve

m "When I looked up again, I saw Remy looking at me with a pained expression."

m "I stepped away, giving him some space as he stepped up to the small corpse."

show varadead at Pan((520, 0), (400, 326), 8.0) with fade

$ renpy.pause (6.0)

Ry "Were you looking for me? Did you sneak out again? Poor girl."

m "He enveloped her as his tears started raining down on the small body."

stop music fadeout 3.0

$ renpy.pause (0.5)

scene black with dissolveslow

$ renpy.pause (2.0)

window show

n "Soon, more help arrived. Remy and I got all the medical attention we needed."

n "Besides those we already knew to be dead, it was also too late for Maverick."

n "I warned them about the comet, telling them to check the PDAs I had given them for verification of my claims."

n "A few minutes later, EMTs arrived and I was put into an artificial coma due to my injuries."

n "In the weeks I was out, a variety of things happened."

n "After everything that had taken place, negotiations were fierce between humanity and the dragons."

n "Out of respect, Reza's body was returned to humanity through the portal. While his actions had shattered all goodwill on the dragon's side, Reza's wounds did their job to do the same for humanity."

window hide
nvl clear
window show

n "I, too, was to be returned to humanity, but as my condition didn't allow it, humanity took the dragons' refusal to transfer me as a sign they were keeping me as a hostage."

n "I wasn't a priority for humanity, though - a fact I was aware of well before I ever arrived in this world. As far as they were concerned, Reza and I had our chance, and the results weren't pretty."

n "Ultimately, the dragons decided to return the PDAs before all contact was cut."

n "Luckily, my claims were taken seriously, and there was already a plan in place to divert the comet."

n "While they would have to use the lab's generators to do it, humanity decided to use their portal's power source to support their slowly failing city for a while longer as they looked for other, more long-term solutions."

window hide
nvl clear
window show

n "After I awoke from my coma, I had to consider my options."

n "While the dragons were able to create a new power source for the portal, I wouldn't have known how to send myself back to humanity, as their portal was already deactivated - at least not without the expertise of the dead Administrator."

n "The only coordinates remaining in the portal were those she left as a last resort. It turned out they were to send someone back in time to the day I arrived here."

n "As soon as I could, I met with Remy, who told me about everything I had missed."

window hide
nvl clear

$ renpy.pause (2.0)

scene park2 with dissolveslow

show remy normal with dissolve

play music "mx/library.ogg" fadein 2.0

c "So, the comet has been diverted, and you've replaced the power source for the portal. I guess I must've been gone for a long time."

Ry "A few weeks, yes."

Ry "What will you do now?"

c "I could use the portal to return to the day of my arrival. After all, I came here to save our dying city, which is something I failed to do."

Ry "But you saved us."

c "That is true, but I can't help thinking that there could have been a diplomatic solution. If I just hadn't been in a coma during the negogiations..."

Ry "Whatever you want to do now, you can be sure that you'll have the council's support."

Ry "You could just stay here if you wanted to."

c "I bet you wouldn't mind that, would you?"

Ry smile "You know how I am. Humans just fascinate me."

Ry normal "This isn't just about me, though. Of course I would love it if you stayed with us, but I know there are many other factors at play here, and that it won't be an easy decision for you to make."

Ry "Don't let me stop you from going back if that's what you want to do, though. I'll be fine."

c "Are you sure about that?"

Ry "Yes. After all, I'm not alone anymore. In  the last few weeks, I spent a lot of time with Adine, and I'd say we're pretty good friends now. As sad as it is what happened with Vara, there is another girl at the orphanage we've been taking care of pretty often."

Ry "Maybe you've seen her. Her name is Amely, and she's just the sweetest little girl."

Ry smile "Besides, if you really end up going back in time, I'll see you again."

#cgs shown contain adine as a hint?

$ _game_menu_screen = None

stop music fadeout 2.0

stop sound fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

$ renpy.block_rollback()

play sound "mx/eveningmelody.ogg"

$ renpy.pause (1.5)

show varadead at Pan((520, 0), (0, 326), 20.0)
show credits1 at left
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits2 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#show remyrom at Pan((980, 326), (750, 0), 20.0)
show remysad at Pan ((750, 326), (1430, 0), 25.0)
show credits3 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits4 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#play movie "cg/chap3/sun2.ogv" loop

show oranged at Pan ((-350, 326), (-850, 100), 20.0)
show credits5 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits6 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed
#stop movie

#

show cgspill at Pan((0, 90), (250, 184), 20.0)
show credits7 at right 
with dissolvemed

$ renpy.pause (8.0)

show black2 at right with dissolvemed

show credits8 at right with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

#

show cg1 at Position(xpos=0.8, xanchor='center')
show credits9 at left 
with dissolvemed

$ renpy.pause (8.0)

show black2 at left with dissolvemed

show credits10 at left with dissolvemed

$ renpy.pause (8.0)

scene black with dissolvemed

scene logo with dissolvemed

$ renpy.pause (8.5)

scene black with dissolvemed

stop sound fadeout 1.0

$ renpy.pause (4.0)

$ persistent.anygoodending = True

$ persistent.lastendingseen = "good"

$ persistent.endingsseen += 1

call izumimask from _call_izumimask_4

call optimistcheck from _call_optimistcheck_1

if persistent.remygoodending == False:

    $ persistent.remygoodending = True
    
    $ achievement.grant("Casualties of War")
    
    $ persistent.achievements += 1
    
    call syscheck from _call_syscheck_72

    $ mp.remygoodending = True
    $ mp.save()
    
    play sound "fx/system.wav"
    
    s "You have seen Remy's good ending!"

if persistent.endingsseen == 1:

    $ persistent.firstending2 = "remy"
    
    jump tut
    
else:

    jump mainmenu
















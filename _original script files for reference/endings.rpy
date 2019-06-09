label badending:
    scene black with dissolveslow
    $ renpy.pause(1.0)
    nvl clear
    play music "mx/gymno.ogg"
    window show
    n "The choices you made led you to this rather unfavorable outcome."
    n "In the full story of {i}Angels with Scaly Wings{/i}, this would have a number of consequences."
    n "For one, you could no longer pursue the dragon you were just spending some time with - making their route inaccessible for the remainder of the current playthrough. This, of course, has its own ramifications, such as not being able to rely on their help when you need it and limiting the ways you can alter the end of the game."
    n "They will also want to avoid you, leading to some interesting situations when you run across them later on."
    n "In the end, {i}Angels with Scaly Wings{/i} is all about the choices you make, so be sure to make them wisely or suffer the consequences."
    n "Luckily for you, there are other characters to spend your limited time with, so your loss might not be all that bad."
    nvl clear
    jump cont

label neutralending:
    scene black with dissolveslow
    $ renpy.pause(1.0)
    nvl clear
    play music "mx/gymno.ogg"
    window show
    n "You completed the character scene and arrived at a neutral outcome."
    n "Congratulations! Some don't even get that far."
    n "A neutral outcome is just what it sounds like: Not too bad, but not too great either. It also represents the dragon's current feelings towards you. In any case, it will be up to you to further the relationship, if you so desire, and want to hear the rest of their story."
    n "In the end, {i}Angels with Scaly Wings{/i} is all about your choices, so whether you pursue this dragon further or not is completely up to you."
    n "In the full game, your time in the dragons' world will be limited, so the one you spend it with will be an important decision to make, with consequences reaching farther than you might think."
    n "Though, a neutral outcome might be just what you wanted, as it keeps your options open without the need for commitment." 
    n "However, \"just enough\" might not be sufficient to reach the goal you want."
    nvl clear
    jump cont
       
label goodending:
    scene black with dissolveslow
    $ renpy.pause(1.0)
    nvl clear
    play music "mx/gymno.ogg"
    window show
    n "You impressed the dragon you were just spending time with. Good job!"
    n "In the full game of {i}Angels with Scaly Wings{/i}, this means they will continue to pursue you and will want to meet with you again."
    n "Depending on the character, their interest will materialize in a number of behaviors, such as calling your phone or showing up in unexpected places."
    n "However, if your feelings about them change or if they hear about you spending time with another dragon, this may turn out badly."
    n "In any case, {i}Angels with Scaly Wings{/i} is all about the choices you make, so it will be up to you to decide how to handle these situations."
    nvl clear
    jump cont
   
label cont:
    n "Regardless of your outcome, this demo offers an easy way to go back and experience the different possiblities you could have achieved."
    n "If you wish, we can return you to the scene selection screen so you can replay the same character scene and make different choices, or play another one that features a different character."
    n "Once again, the choice is yours."
    window hide
    nvl clear
    stop music fadeout 1.0
    menu:
        "Bring me back.":
            jump sceneselect
            
        "No, I'm done.":
            pass
            
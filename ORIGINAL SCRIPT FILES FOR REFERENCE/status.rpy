screen status:
    tag smallscreen
    window id "save" at popup_offcenter:
        style "smallwindow_big2"
        add "image/ui/navmenu/status.png" yalign 0.1 at title_slide
        
        vbox:
            xalign 0.5 yalign 0.5
            spacing 50
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                vbox:
                    
                    if persistent.remymet:

                        if remydead:
                            
                            add "image/ui/status/remydead.png" xalign 0.5
                            text _("Status: {b}--{/b}\nScenes played: {b}[remyscenesfinished]{/b}") style "status_text"
                            
                        elif remystatus == "none":

                            add "image/ui/status/remy_neutral.png" xalign 0.5
                            text _("Status: {b}Neutral{/b}\nScenes played: {b}[remyscenesfinished]{/b}") style "status_text"
                            
                        elif remystatus == "neutral":

                            add "image/ui/status/remy_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[remyscenesfinished]{/b}") style "status_text"
                            
                        elif remystatus == "normal":

                            add "image/ui/status/remy_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[remyscenesfinished]{/b}") style "status_text"
                            
                        elif remystatus == "good":

                            add "image/ui/status/remy_good.png" xalign 0.5
                            text _("Status: {b}Impressed{/b}\nScenes played: {b}[remyscenesfinished]{/b}") style "status_text"
                            
                        elif remystatus == "bad":
                            
                            add "image/ui/status/remy_bad.png" xalign 0.5
                            text _("Status: {b}Bad{/b}\nScenes played: {b}[remyscenesfinished]{/b}") style "status_text"
                            
                        elif remystatus == "abandoned":

                            add "image/ui/status/remy_abandoned.png" xalign 0.5
                            text _("Status: {b}Abandoned{/b}\nScenes played: {b}[remyscenesfinished]{/b}") style "status_text"
                        
                    #add "image/ui/status/locked_portrait.png" xalign 0.5
                    #text "Unknown character" style "status_text"
                vbox:
                    
                    if persistent.annamet:

                        if annadead:
                            
                            add "image/ui/status/annadead.png" xalign 0.5
                            text _("Status: {b}--{/b}\nScenes played: {b}[annascenesfinished]{/b}") style "status_text"
                            
                        elif annastatus == "none":

                            add "image/ui/status/anna_neutral.png" xalign 0.5
                            text _("Status: {b}Neutral{/b}\nScenes played: {b}[annascenesfinished]{/b}") style "status_text"
                            
                        elif annastatus == "neutral":

                            add "image/ui/status/anna_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[annascenesfinished]{/b}") style "status_text"
                            
                        elif annastatus == "normal":

                            add "image/ui/status/anna_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[annascenesfinished]{/b}") style "status_text"
                            
                        elif annastatus == "good":

                            add "image/ui/status/anna_good.png" xalign 0.5
                            text _("Status: {b}Impressed{/b}\nScenes played: {b}[annascenesfinished]{/b}") style "status_text"
                            
                        elif annastatus == "bad":
                            
                            add "image/ui/status/anna_bad.png" xalign 0.5
                            text _("Status: {b}Bad{/b}\nScenes played: {b}[annascenesfinished]{/b}") style "status_text"
                            
                        elif annastatus == "abandoned":

                            add "image/ui/status/anna_abandoned.png" xalign 0.5
                            text _("Status: {b}Abandoned{/b}\nScenes played: {b}[annascenesfinished]{/b}") style "status_text"
                    
                    #add "image/ui/status/locked_portrait.png" xalign 0.5
                    #text "Unknown character" style "status_text"
                vbox:
                    
                    if persistent.loremmet:

                        if loremdead:
                            
                            add "image/ui/status/loremdead.png" xalign 0.5
                            text _("Status: {b}--{/b}\nScenes played: {b}[loremscenesfinished]{/b}") style "status_text"
                            
                        elif loremstatus == "none":

                            add "image/ui/status/lorem_neutral.png" xalign 0.5
                            text _("Status: {b}Neutral{/b}\nScenes played: {b}[loremscenesfinished]{/b}") style "status_text"
                            
                        elif loremstatus == "neutral":

                            add "image/ui/status/lorem_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[loremscenesfinished]{/b}") style "status_text"
                            
                        elif loremstatus == "normal":

                            add "image/ui/status/lorem_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[loremscenesfinished]{/b}") style "status_text"
                            
                        elif loremstatus == "good":

                            add "image/ui/status/lorem_good.png" xalign 0.5
                            text _("Status: {b}Impressed{/b}\nScenes played: {b}[loremscenesfinished]{/b}") style "status_text"
                            
                        elif loremstatus == "bad":
                            
                            add "image/ui/status/lorem_bad.png" xalign 0.5
                            text _("Status: {b}Bad{/b}\nScenes played: {b}[loremscenesfinished]{/b}") style "status_text"
                            
                        elif loremstatus == "abandoned":

                            add "image/ui/status/lorem_abandoned.png" xalign 0.5
                            text _("Status: {b}Abandoned{/b}\nScenes played: {b}[loremscenesfinished]{/b}") style "status_text"
                        
                        
                    #add "image/ui/status/locked_portrait.png" xalign 0.5
                    #text "Unknown character" style "status_text"
                vbox:
                    
                    if persistent.brycemet:
                        
                        if brycedead:
                            
                            add "image/ui/status/brycedead.png" xalign 0.5
                            text _("Status: {b}--{/b}\nScenes played: {b}[brycescenesfinished]{/b}") style "status_text"
                            
                        elif brycestatus == "none":

                            add "image/ui/status/bryce_neutral.png" xalign 0.5
                            text _("Status: {b}Neutral{/b}\nScenes played: {b}[brycescenesfinished]{/b}") style "status_text"
                            
                        elif brycestatus == "neutral":

                            add "image/ui/status/bryce_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[brycescenesfinished]{/b}") style "status_text"
                            
                        elif brycestatus == "normal":

                            add "image/ui/status/bryce_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[brycescenesfinished]{/b}") style "status_text"
                            
                        elif brycestatus == "good":

                            add "image/ui/status/bryce_good.png" xalign 0.5
                            text _("Status: {b}Impressed{/b}\nScenes played: {b}[brycescenesfinished]{/b}") style "status_text"
                            
                        elif brycestatus == "bad":
                            
                            add "image/ui/status/bryce_bad.png" xalign 0.5
                            text _("Status: {b}Bad{/b}\nScenes played: {b}[brycescenesfinished]{/b}") style "status_text"
                            
                        elif brycestatus == "abandoned":

                            add "image/ui/status/bryce_abandoned.png" xalign 0.5
                            text _("Status: {b}Abandoned{/b}\nScenes played: {b}[brycescenesfinished]{/b}") style "status_text"
                        
                        
                    #add "image/ui/status/locked_portrait.png" xalign 0.5
                    #text "Unknown character" style "status_text"
                vbox:
                    
                    if persistent.adinemet:
                        
                        if adinedead:
                            
                            add "image/ui/status/adinedead.png" xalign 0.5
                            text _("Status: {b}--{/b}\nScenes played: {b}[adinescenesfinished]{/b}") style "status_text"
                            
                        elif adinestatus == "none":

                            add "image/ui/status/adine_neutral.png" xalign 0.5
                            text _("Status: {b}Neutral{/b}\nScenes played: {b}[adinescenesfinished]{/b}") style "status_text"
                            
                        elif adinestatus == "neutral":

                            add "image/ui/status/adine_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[adinescenesfinished]{/b}") style "status_text"
                            
                        elif adinestatus == "normal":

                            add "image/ui/status/adine_neutral.png" xalign 0.5
                            text _("Status: {b}Good{/b}\nScenes played: {b}[adinescenesfinished]{/b}") style "status_text"
                            
                        elif adinestatus == "good":

                            add "image/ui/status/adine_good.png" xalign 0.5
                            text _("Status: {b}Impressed{/b}\nScenes played: {b}[adinescenesfinished]{/b}") style "status_text"
                            
                        elif adinestatus == "bad":
                            
                            add "image/ui/status/adine_bad.png" xalign 0.5
                            text _("Status: {b}Bad{/b}\nScenes played: {b}[adinescenesfinished]{/b}") style "status_text"
                            
                        elif adinestatus == "abandoned":

                            add "image/ui/status/adine_abandoned.png" xalign 0.5
                            text _("Status: {b}Abandoned{/b}\nScenes played: {b}[adinescenesfinished]{/b}") style "status_text"
                            
                    #add "image/ui/status/locked_portrait.png" xalign 0.5
                    #text "Unknown character" style "status_text"
                    
            
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                
                if cardduty == True:
                    
                    add "image/ui/status/duty.png"
                    
                if cardenlightenment == True:

                    add "image/ui/status/enlightenment.png"
                    
                if cardconflict == True:

                    add "image/ui/status/conflict.png"
                    
                if cardhope == True:

                    add "image/ui/status/hope.png"
                    
                if cardinception == True:

                    add "image/ui/status/inception.png"
                    
                if cardloss == True:

                    add "image/ui/status/loss.png"
                    
                if cardpride == True:

                    add "image/ui/status/pride.png"
                    
                if cardtrauma == True:

                    add "image/ui/status/trauma.png"
                    
                if cardgrief == True:
    
                    add "image/ui/status/grief.png"
                    
                if cardpassion == True:

                    add "image/ui/status/passion.png"
                    
                if cardlorem == True:

                    add "image/ui/status/lorem.png"
                    
                if cardleadership == True:

                    add "image/ui/status/leadership.png"
                    
                if cardsuperstition == True:

                    add "image/ui/status/superstition.png"
                        
                    #add "image/ui/status/Card.png" zoom 0.36
                    #add "image/ui/status/Card.png" zoom 0.36
                    #add "image/ui/status/Card.png" zoom 0.36
                    #add "image/ui/status/Card.png" zoom 0.36
                    #add "image/ui/status/card2.png" #zoom 0.36
                    
    vbox:
        xalign 0.962 yalign 1.0 #xalign 0.962 yalign 0.79
        spacing 20
        
        if persistent.playedadine2 == True:

            add "image/ui/status/c2pictures.png"
            
        elif persistent.c2pictures == True:

            add "image/ui/status/c2pictures.png"
            
        else:
            
            pass
            
        if persistent.varasaved == True:
            
            add "image/ui/status/varasaved2.png"

        if persistent.heardaboutcancer == True:
            
            add "image/ui/status/heardaboutcancer.png"
            
        if persistent.orb_taken == True:
            
            add "image/ui/status/orb_taken.png"
            
        if persistent.base_taken == True:
            
            add "image/ui/status/base_taken.png"
            
        if persistent.havetestresults == True:
            
            add "image/ui/status/havetestresults.png"
            #add "image/ui/status/varasaved.png"
            
        if persistent.havemap == True:
            
            add "image/ui/status/havemap.png"
            
        add "image/ui/status/invi.png"
    
style status_text is default:
    xmaximum 300
    xalign 0.5
    size 22

##############################################################################
# Transforms
#
    
transform left:
    #xalign 0.2
    xalign 0.0
    yalign 1.0
    
transform right:
    #xalign 0.8
    xalign 1.0
    yalign 1.0
    
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
        
transform alphadissolvefast:
    alpha 0.0
    linear 0.3 alpha 1.0
    on hide:
        linear 0.3 alpha 0
        
transform codex_rotate:
    rotate -7
    
transform popup:
    xalign 0.0 yalign 0.5 alpha 0.0 yzoom 0.0
    easein 0.3 alpha 1.0 yzoom 1.0
    on hide:
        easeout 0.3 alpha 0.0 yzoom 0.0
        
transform popup_offcenter:
    xalign 0.0 yalign 0.75 alpha 0.0 yzoom 0.0
    easein 0.3 alpha 1.0 yzoom 1.0
    on hide:
        easeout 0.3 alpha 0.0 yzoom 0.0
        
transform popup2:
    xalign 0.0 yalign 0.5 alpha 0.0 yzoom 0.0
    0.5
    easein 0.3 alpha 1.0 yzoom 1.0
    on hide:
        easeout 0.3 alpha 0.0 yzoom 0.0
        
transform choicebg:
    alpha 0 zoom 1.2 xalign 0.5 yalign 0.5
    linear 0.2 alpha 1.0 zoom 1.0 yalign 0.5
    
transform choice_slide:
    alpha 0.0 xalign 0.0 yalign 0.5
    easein 0.7 alpha 1.0 xalign 0.1
    
transform title_slide:
    alpha 0.0 xalign -0.1
    easein 0.7 alpha 1.0 xalign 0.05
    on hide:
        easeout 0.7 alpha 1.0 xalign -0.1
    
transform choice_gear_slide:
    alpha 0.01 xalign 0.0
    easein 0.7 alpha 0.1 xpos 45
    
transform top_button:
    subpixel True
    xanchor 0.5 yanchor 0.5
    on idle:
        linear 0.1 zoom 1.0
    on hover:
        linear 0.1 zoom 0.97
    on selected_hover:
        linear 0.1 zoom 0.94
        0.1

##############################################################################
# System 
#
    
##############################################################################
# Choice Screen
#

transform zoom_fade_in:
    alpha 0.0 zoom 1.2
    easein 0.5 alpha 1.0 zoom 1.0
    on hide:
        easeout 0.5 alpha 0.0 zoom 1.2
    
##############################################################################
# Menu Screen 
#

define menudissolve = Dissolve(0.2)
define xdissolveslow = Dissolve(2.0)
    
transform bar_fade_in:
    alpha 0.01
    zoom 1.4
    easein 0.7 alpha 1.0 zoom 1.0
    
transform bar_slide_up:
    yalign 0.9
    easein 0.7 yalign 0.5
    
#Text Screen

transform text_fade_in:
    alpha 0.01
    easein 0.7 alpha 1.0
    
transform text_slide:
    xalign 0.3
    easein 0.7 xalign 0.4
    
#Characters

transform zoomin:
    ease 0.5 zoom 1.5 yalign -1.5
    
transform zoomout:
    easein 0.5 zoom 1.0
    
##############################################################################
# Time Passing Screens 
#

transform minuteslater:
    alpha 0.0 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 xzoom 0.0
    linear 0.1 alpha 1.0 xzoom 0.5
    linear 0.1 xzoom 0.0
    linear 0.1 xzoom -0.5
    linear 0.1 xzoom 0.0
    linear 0.1 xzoom 1.0
    on hide:
        linear 0.1 alpha 0.0 yzoom 0.01
    
screen minuteslater:
    text "Later On..." font "Euphorigenic.ttf" size 96 at minuteslater
    
# Transitions

define longdissolve = Dissolve(2.0)


##############################################################################
# Interrogation Text
#

transform text_zoom_in:
    zoom 1.5 alpha 0.0
    ease 0.5 zoom 1.1 alpha 1.0
    ease 4.5 zoom 1.0
    on hide:
        ease 1.0 alpha 0.0 zoom 0.9
            
transform text_zoom_out:
    zoom 0.5 alpha 0.0
    ease 0.5 zoom 0.9 alpha 1.0
    ease 4.5 zoom 1.0
    on hide:
        ease 1.0 alpha 0.0 zoom 1.1
        
transform text_spin_in:
    zoom 1.5 alpha 0.0
    ease 0.5 zoom 1.1 alpha 1.0 rotate 360
    ease 4.5 zoom 1.0
    on hide:
        ease 1.0 alpha 0.0 zoom 0.9 yzoom 0.1
        
transform text_wave_in:
    zoom 0.8 alpha 0.0
    ease 0.3 zoom 0.9 yzoom 1.5 alpha 0.3
    ease 0.3 zoom 0.95 yzoom 1.0 xzoom 1.5 alpha 0.7
    ease 0.3 zoom 1.0 xzoom 1.0 alpha 1.0
    ease 4.0 zoom 1.1
    on hide:
        ease 1.0 alpha 0.0 yzoom 0.1
        
        

# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window id "window":

            vbox:
                style "say_vbox"

                if who:
                    text who id "who"
                    add "image/ui/dialogline.png"
    
                text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:
    add "image/ui/choicebg.png" xalign 0.5 yalign 0.5 at zoom_fade_in

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox at zoom_fade_in:
            style "menu"
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action [action, Play("audio", "se/sounds/select3.ogg")]
                        hovered Play("audio", "se/sounds/select.ogg")
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = 1200
    style.menu_choice_button.xmaximum = 1200

    style.menu_choice.size = 39
    style.menu_choice.hover_color = "#4D4D4D"
    style.menu_choice.selected_color = "#4D4D4D"
    style.menu_choice_button.background = None

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:
    tag menu
        
    add "image/ui/title/background.png"

    if persistent.trueending:
        add "image/ui/title/title_overlay4.png"

    elif persistent.anygoodending:
        add "image/ui/title/title_overlay3.png"

    else:
        add "image/ui/title/title_overlay.png"

    if persistent.neutralending:
        add "image/ui/title/neutralending.png"

    if persistent.evilending:
        add "image/ui/title/evilending.png"
        
        if persistent.neutralending:
            add "image/ui/title/bloodygun.png"
        
    if persistent.remybadending:
        add "image/ui/title/remybadending.png"

    if persistent.remygoodending:
        add "image/ui/title/remygoodending.png"
        
    if persistent.brycebadending:
        add "image/ui/title/brycebadending.png"

    if persistent.brycegoodending:
        add "image/ui/title/brycegoodending.png"

    if persistent.adinebadending:
        add "image/ui/title/adinebadending.png"

    if persistent.adinegoodending:
        add "image/ui/title/adinegoodending.png"

    if persistent.annabadending:
        add "image/ui/title/annabadending.png"

    if persistent.annagoodending:
        add "image/ui/title/annagoodending.png"

    if persistent.lorembadending:
        add "image/ui/title/lorembadending.png"

    if persistent.loremgoodending:
        add "image/ui/title/loremgoodending.png"

    if persistent.secretending:
        add "image/ui/title/secretending.png"

    if persistent.sebastianplayed:
        add "image/ui/title/sebastian.png"
        
    if persistent.playedzhong:
        add "image/ui/title/zhong.png"
        
    if persistent.playedemera:
        add "image/ui/title/emera.png"
        
    if persistent.playedkatsu:
        add "image/ui/title/katsu.png"
        
    if persistent.playedkevin:
        add "image/ui/title/kevin.png"
    
    #text "V. 1.0" xalign 0.02 yalign 0.98 color "#FFF" drop_shadow None size 40 text_align 1.0
    
    hbox:
        xalign 0.5
        yalign 0.83
        spacing 40
        imagebutton auto "image/ui/title/start_%s.png" action [Play("audio", "se/sounds/new.ogg"), Start()] hovered Play("audio", "se/sounds/select.ogg")
        imagebutton auto "image/ui/title/load_%s.png" action [Show("preferencesbg"), Show('load'), Play("audio", "se/sounds/open.wav")] hovered Play("audio", "se/sounds/select.ogg")
        imagebutton auto "image/ui/title/options_%s.png" action [Show("preferencesbg"), Show("preferences"), Play("audio", "se/sounds/open.wav")] hovered Play("audio", "se/sounds/select.ogg")
        imagebutton auto "image/ui/title/gallery_%s.png" action [Show('gallery', transition=dissolve), Show('gallery_page_1'), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg")
        imagebutton auto "image/ui/title/quit_%s.png" action [Quit(confirm=True), Play("audio", "se/sounds/exit.wav")] hovered Play("audio", "se/sounds/select.ogg")
    
    # Help button
    imagebutton auto "image/ui/title/help_%s.png" action [Show("preferencesbg"), Show("help"), Play("audio", "se/sounds/open.wav")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.955 yalign 0.13
    
transform nav_button:
    subpixel True
    xanchor 0.5 yanchor 0.5
    on idle:
        linear 0.1 zoom 1.0
    on hover:
        linear 0.1 zoom 0.96
    on selected_hover:
        linear 0.1 zoom 0.93
        0.1
        linear 0.1 zoom 1.0

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation

transform ingame_menu_light:
    linear 5.0 xalign -2.0
    xalign 2.0
    repeat
    
transform navopen:
    alpha 0.3
    
transform navmenu_button_far:
    zoom 0.86 yalign 0.5
    on idle:
        linear 0.1 alpha 0.3
    on hover:
        alpha 1.0
    on selected_idle:
        alpha 1.0
    on selected_hover:
        alpha 1.0
        
transform navmenu_button_mid:
    zoom 0.76 yalign 0.5
    on idle:
        linear 0.1 alpha 0.3
    on hover:
        alpha 1.0
    on selected_idle:
        alpha 1.0
    on selected_hover:
        alpha 1.0
        
transform navmenu_button_center:
    zoom 0.66 yalign 0.5
    on idle:
        linear 0.1 alpha 0.3
    on hover:
        alpha 1.0
    on selected_idle:
        alpha 1.0
    on selected_hover:
        alpha 1.0

screen navigation:
    tag menu
    frame:
        add "image/ui/ingame_menu_bg2.png" at alpha_dissolve
        add "image/ui/navmenu/menu_title.png" at alpha_dissolve
        add "image/ui/ingame_menu_bg_light.png" at ingame_menu_light
    
        hbox at zoom_fade_in:
            xalign 0.5
            yalign 0.13
            spacing 55
            vbox:
                imagebutton idle "image/ui/back_title.png" hover "image/ui/back_title.png" action [Return(), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") at navmenu_button_far
                null height 20
            vbox:
                null height 7
                imagebutton idle "image/ui/save_title.png" hover "image/ui/save_title.png" action [Show('save_nav'), Hide('load_nav'), Hide('preferences_nav'), Hide('videosettings_nav'), Hide('audiosettings_nav'), Hide('textsettings_nav'), Hide('achievements'), Hide('achievement_page'), Hide('status'), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") at navmenu_button_mid
            vbox:
                null height 10
                imagebutton idle "image/ui/load_title.png" hover "image/ui/load_title.png" action [Show('load_nav'), Hide('save_nav'), Hide('preferences_nav'), Hide('videosettings_nav'), Hide('audiosettings_nav'), Hide('textsettings_nav'), Hide('achievements'), Hide('achievement_page'), Hide('status'), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") at navmenu_button_mid
            imagebutton idle "image/ui/navmenu/status.png" hover "image/ui/navmenu/status.png" action [Show('status'), Hide('load_nav'), Hide('save_nav'), Hide('preferences_nav'), Hide('videosettings_nav'), Hide('audiosettings_nav'), Hide('achievements'), Hide('achievement_page'), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") at navmenu_button_center
            imagebutton idle "image/ui/navmenu/achievements.png" hover "image/ui/navmenu/achievements.png" action [Show('achievements'), Show('achievement_page_1'), Hide('load_nav'), Hide('save_nav'), Hide('preferences_nav'), Hide('videosettings_nav'), Hide('audiosettings_nav'), Hide('status'), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") at navmenu_button_center
            vbox:
                null height 7
                imagebutton idle "image/ui/settings_title.png" hover "image/ui/settings_title.png" action [Show('preferences_nav'), Hide('load_nav'), Hide('save_nav'), Hide('videosettings_nav'), Hide('audiosettings_nav'), Hide('textsettings_nav'), Hide('achievements'), Hide('achievement_page'), Hide('status'), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") at navmenu_button_mid
            vbox:
                imagebutton idle "image/ui/quit_title.png" hover "image/ui/quit_title.png" action [MainMenu(), Play("audio", "se/sounds/alert.ogg")] hovered Play("audio", "se/sounds/select.ogg") at navmenu_button_far
                null height 20
                
    #show status
    #action Show ('status')
    #below is just a paste of the status screen
    #use status
    #show screen status
    
    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
#here

screen save_input():
    window:
        has vbox

        text "Enter a name for your save file:"
        input length 20 default save_name
    
screen file_picker_save:
    frame:
        xpadding 0
        ypadding 0
        xalign 0.5
        yalign 0.5
        has vbox
        
        grid 3 2:
            xalign 0.5
            xfill True
            xmaximum 800
            for i in range(1, 7):
                vbox:
                    #spacing 10
                    button:
                        style "savebutton"
                        action [FileSave(i), Play("audio", "se/sounds/yes.wav")]
                        #action [Show('save_input'), Play("audio", "se/sounds/yes.wav")]
                        key "save_delete" action [FileDelete(i), Play("audio", "se/sounds/alert.ogg")]
                        hovered Play("audio", "se/sounds/select.ogg")
                        
                        add FileScreenshot(i) xalign 0.5 yalign 0.5
                        
                    $ description = "% 2s. %s\n%s" % (
                        FileSlotName(i, 3 * 2),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))
                    
                    text description size 26 xalign 0.5 text_align 0.5
                    
        hbox:
            xalign 0.5
            
            textbutton _("Auto"):
                action [FilePage("auto"),Play("audio", "se/sounds/select3.ogg")] style "savenavigation"
                hovered Play("audio", "se/sounds/select.ogg")
            null width 20

            textbutton _("Quick"):
                action [FilePage("quick"),Play("audio", "se/sounds/select3.ogg")] style "savenavigation"
                hovered Play("audio", "se/sounds/select.ogg")
            null width 20

            for i in range(1, 9):
                textbutton str(i):
                    action [FilePage(i),Play("audio", "se/sounds/select3.ogg")] style "savenavigation"
                    hovered Play("audio", "se/sounds/select.ogg")
                null width 10
            null width 20
    
    imagebutton idle "image/ui/filepicker/Btn_Prev.png" hover "image/ui/filepicker/Btn_Prevx.png" action [FilePagePrevious(), Play("audio", "se/sounds/select.ogg")] xalign 0.12 yalign 0.525 at top_button hovered Play("audio", "se/sounds/select.ogg")
    imagebutton idle "image/ui/filepicker/Btn_Next.png" hover "image/ui/filepicker/Btn_Nextx.png" action [FilePageNext(max=8), Play("audio", "se/sounds/select.ogg")] xalign 0.88 yalign 0.525 at top_button hovered Play("audio", "se/sounds/select.ogg")
    
screen file_picker_load:
    frame:
        xpadding 0
        ypadding 0
        xalign 0.5
        yalign 0.5
        has vbox
        
        grid 3 2:
            xalign 0.5
            xfill True
            xmaximum 800
            for i in range(1, 7):
                vbox:
                    #spacing 10
                    button:
                        style "savebutton"
                        action [FileLoad(i), Play("audio", "se/sounds/yes.wav")]
                        key "save_delete" action [FileDelete(i), Play("audio", "se/sounds/alert.ogg")]
                        hovered Play("audio", "se/sounds/select.ogg")
                        
                        add FileScreenshot(i) xalign 0.5 yalign 0.5
                        
                    $ description = "% 2s. %s\n%s" % (
                        FileSlotName(i, 3 * 2),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))
                    
                    text description size 26 xalign 0.5 text_align 0.5
                    
        hbox:
            xalign 0.5
            
            textbutton _("Auto"):
                action [FilePage("auto"),Play("audio", "se/sounds/select3.ogg")] style "savenavigation"
                hovered Play("audio", "se/sounds/select.ogg")
            null width 20

            textbutton _("Quick"):
                action [FilePage("quick"),Play("audio", "se/sounds/select3.ogg")] style "savenavigation"
                hovered Play("audio", "se/sounds/select.ogg")
            null width 20

            for i in range(1, 9):
                textbutton str(i):
                    action [FilePage(i),Play("audio", "se/sounds/select3.ogg")] style "savenavigation"
                    hovered Play("audio", "se/sounds/select.ogg")
                null width 10
            null width 20
    
    imagebutton idle "image/ui/filepicker/Btn_Prev.png" hover "image/ui/filepicker/Btn_Prevx.png" action [FilePagePrevious(), Play("audio", "se/sounds/select.ogg")] xalign 0.12 yalign 0.525 at top_button hovered Play("audio", "se/sounds/select.ogg")
    imagebutton idle "image/ui/filepicker/Btn_Next.png" hover "image/ui/filepicker/Btn_Nextx.png" action [FilePageNext(max=8), Play("audio", "se/sounds/select.ogg")] xalign 0.88 yalign 0.525 at top_button hovered Play("audio", "se/sounds/select.ogg")
                
screen save:
    modal True
    tag smallscreen
    window id "save" at popup:
        style "smallwindow"
        add "image/ui/save_title.png" xalign 0.01 yalign 0.1 at title_slide
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("save"), ToggleVariable("navmenuopen", False), Hide("preferencesbg", transition=dissolve), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        use file_picker_save
        
screen save_nav:
    tag smallscreen
    window id "save" at popup:
        style "smallwindow"
        add "image/ui/save_title.png" xalign 0.01 yalign 0.1 at title_slide
        use file_picker_save

screen load:
    modal True
    tag smallscreen
    window id "load" at popup:
        style "smallwindow"
        add "image/ui/load_title.png" xalign 0.01 yalign 0.1 at title_slide
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("load"), ToggleVariable("navmenuopen", False), Hide("preferencesbg", transition=dissolve), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        use file_picker_load
        
screen load_nav:
    tag smallscreen
    window id "load" at popup:
        style "smallwindow"
        add "image/ui/load_title.png" xalign 0.01 yalign 0.1 at title_slide
        use file_picker_load
        
init -2 python:
    style.savebutton = Style(style.default)
    style.savebutton.insensitive_foreground = None
    style.savebutton.idle_foreground = ("image/ui/filepicker/saveframe_idle_fg.png")
    style.savebutton.hover_foreground = ("image/ui/filepicker/saveframe_hover_fg.png")
    style.savebutton.insensitive_background = ("image/ui/filepicker/saveframe_idle.png")
    style.savebutton.idle_background = ("image/ui/filepicker/saveframe_idle.png")
    style.savebutton.hover_background = ("image/ui/filepicker/saveframe_hover.png")
    style.savebutton.xmaximum = 192
    style.savebutton.ymaximum = 108
    
    style.savenavigation = Style(style.default)
    style.savenavigation.background = None
    style.savenavigation_text.idle_color = "#FFFFFF"
    style.savenavigation_text.hover_color = "#333333"
    style.savenavigation_text.selected_color = "#333333"
    style.savenavigation_text.font = "Ardnas.otf"
    style.savenavigation_text.size = 50
    style.savenavigation_text.drop_shadow = (2,2)

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#preferences

screen preferencesbg:
    frame:
        add "image/ui/ingame_menu_bg2.png" xalign 0.5 yalign 0.5 at alpha_dissolve
        add "image/ui/ingame_menu_bg_light.png" at ingame_menu_light

screen preferences:
    modal True
    tag smallscreen
    window id "preferences" at popup:
        style "smallwindow"
        
        add "image/ui/settings_title.png" xalign 0.01 yalign 0.1 at title_slide
        
        vbox xalign 0.5 yalign 0.5:
            spacing 10
            textbutton _("Video") action [Hide("preferences"), Show("videosettings"), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
            textbutton _("Audio") action [Hide("preferences"), Show("audiosettings"), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
            textbutton _("Text") action [Hide("preferences"), Show("textsettings"), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
            
        #textbutton "Reset Data" action [Hide("preferences"), Show("delete_data_alert"), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.9 yalign 0.8 style "menubutton"
            
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("preferences"), Hide("preferencesbg", transition=dissolve), ToggleVariable('navmenuopen', False), Play("audio", "se/sounds/close.ogg")]  hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        
screen preferences_nav:
    tag smallscreen
    window id "preferences" at popup:
        style "smallwindow"
        
        add "image/ui/settings_title.png" xalign 0.01 yalign 0.1 at title_slide
        
        vbox xalign 0.5 yalign 0.5:
            spacing 10
            textbutton _("Video") action [Hide("preferences_nav"), Show("videosettings_nav"), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
            textbutton _("Audio") action [Hide("preferences_nav"), Show("audiosettings_nav"), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
            textbutton _("Text") action [Hide("preferences_nav"), Show("textsettings_nav"), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
            
        #textbutton "Reset Data" action [Hide("preferences"), Show("delete_data_alert"), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.9 yalign 0.8 style "menubutton"
            
screen delete_data_alert:
    modal True
    tag smallscreen2
    window id "delete_data_alert" at popup2:
        style "alertwindow"
    
        hbox xalign 0.5 yalign 0.8:
            spacing 250
            textbutton _("Yes") action [Hide("delete_data_alert"), Show("delete_data_alert_2"),  Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"
            textbutton _("No") action [Hide("delete_data_alert"), Hide("preferencesbg", transition=dissolve), ToggleVariable('navmenuopen', False), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"
    
        label _("Resetting the game data will delete all current progress, save files and unlocks. This cannot be reversed! Continue?"):
            style "yesno_prompt"
            text_style "yesno_prompt_text"
            
screen delete_data_alert_2:
    modal True
    tag smallscreen3
    window id "delete_data_alert" at popup2:
        style "alertwindow"
    
        textbutton _("Continue") action [Hide("delete_data_alert_2"), Hide("preferencesbg", transition=dissolve), ToggleVariable('navmenuopen', False), Play("audio", "se/sounds/close.ogg"), Jump("resetall"), MainMenu()] style "yesnobutton" xalign 0.5 yalign 0.8
    
        label _("All data has been reset."):
            style "yesno_prompt"
            text_style "yesno_prompt_text"
        
screen videosettings:
    modal True
    tag smallscreen2
    window id "videosettings" at popup2:
        style "smallwindow"
        
        add "image/ui/videosettings_title.png" xalign 0.01 yalign 0.1 at title_slide
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            textbutton _("Fullscreen") action [Preference("display", "fullscreen"), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "1600 x 1200" action [Preference("display", 0.83333333333), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "1366 x 768" action [Preference("display", 0.71145833333), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "1280 x 720" action [Preference("display", 0.666666666667), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton _("Netbook") action [Preference("display", 0.53333333333), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            
        #imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("videosettings"), Hide("preferencesbg", transition=dissolve), ToggleVariable("navmenuopen", False), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("videosettings"), Show("preferences"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        
screen videosettings_nav:
    tag smallscreen2
    window id "videosettings" at popup2:
        style "smallwindow"
        
        add "image/ui/videosettings_title.png" xalign 0.01 yalign 0.1 at title_slide
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            textbutton _("Fullscreen") action [Preference("display", "fullscreen"), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "1600 x 1200" action [Preference("display", 0.83333333333), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "1366 x 768" action [Preference("display", 0.71145833333), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "1280 x 720" action [Preference("display", 0.666666666667), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton _("Netbook") action [Preference("display", 0.53333333333), Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("videosettings_nav"), Show("preferences_nav"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        
screen audiosettings:
        modal True
        tag smallscreen2
        window id "audiosettings" at popup2:
            style "smallwindow"
            
            add "image/ui/audiosettings_title.png" xalign 0.01 yalign 0.1 at title_slide
                    
            vbox xalign 0.5 yalign 0.5:
                spacing 30
                frame:
                    style_group "pref"
                    has vbox
        
                    label _("Music")
                    bar value Preference("music volume")
                    
                frame:
                    style_group "pref"
                    has vbox
        
                    label _("Sound")
                    bar value Preference("sound volume")
        
                #frame:
                    #style_group "pref"
                    #has vbox
        
                    #label _("Voice")
                    #bar value Preference("voice volume")
                    
            if config.sample_sound:
                textbutton _("Test"):
                    xalign 0.85
                    yalign 0.82
                    action Play("sound", config.sample_sound)
                    #style "soundtest_button"
                    style "menubutton"
            
            #if config.sample_voice:
                #textbutton "Test":
                    #xalign 0.85
                    #yalign 0.78
                    #action Play("voice", config.sample_voice)
                    #style "soundtest_button"
                    
            #textbutton "Reset Levels" action [Play("audio", "se/sounds/open.ogg"), Jump("resetlevels")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.9 yalign 0.8 style "menubutton"
            
            #imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("audiosettings"), Hide("preferencesbg", transition=dissolve), ToggleVariable("navmenuopen", False), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
            
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("audiosettings"), Show("preferences"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
            
screen audiosettings_nav:
        tag smallscreen2
        window id "audiosettings" at popup2:
            style "smallwindow"
            
            add "image/ui/audiosettings_title.png" xalign 0.01 yalign 0.1 at title_slide
                    
            vbox xalign 0.5 yalign 0.5:
                spacing 30
                frame:
                    style_group "pref"
                    has vbox
        
                    label _("Music")
                    bar value Preference("music volume")
                    
                frame:
                    style_group "pref"
                    has vbox
        
                    label _("Sound")
                    bar value Preference("sound volume")
                    
            if config.sample_sound:
                textbutton _("Test"):
                    xalign 0.85
                    yalign 0.82
                    action Play("sound", config.sample_sound)
                    #style "soundtest_button"
                    style "menubutton"
                    
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("audiosettings_nav"), Show("preferences_nav"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        
        
screen textsettings:
        modal True
        tag smallscreen2
        window id "textsettings" at popup2:
            style "smallwindow"
            
            add "image/ui/textsettings_title.png" xalign 0.01 yalign 0.1 at title_slide

            vbox xalign 0.5 yalign 0.5:
                spacing 30
                style_group "prefs"
        
                # The left column.
                vbox xalign 0.5:
                    style_group "pref"
    
                    label _("Text Speed")
                    bar value Preference("text speed")
        
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
        
                hbox xalign 0.5:
                    spacing 30
                    style_group "pref"
    
                    vbox:
                        label _("{b}Skip{/b}")
                        textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")
                        textbutton _("All Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "all")] hovered Play("audio", "se/sounds/select.ogg")
    
                    vbox:
                        label _("{b}After Choices{/b}")
                        textbutton _("Stop Skipping") action [Play("audio", "se/sounds/select3.ogg"), Preference("after choices", "stop")] hovered Play("audio", "se/sounds/select.ogg")
                        textbutton _("Keep Skipping") action [Play("audio", "se/sounds/select3.ogg"), Preference("after choices", "skip")] hovered Play("audio", "se/sounds/select.ogg")
                        
            #imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("textsettings"), Hide("preferencesbg", transition=dissolve), ToggleVariable("navmenuopen", False), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
            
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("textsettings"), Show("preferences"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        
            
screen textsettings_nav:
        tag smallscreen2
        window id "textsettings" at popup2:
            style "smallwindow"
            
            add "image/ui/textsettings_title.png" xalign 0.01 yalign 0.1 at title_slide

            vbox xalign 0.5 yalign 0.5:
                spacing 30
                style_group "prefs"
        
                # The left column.
                vbox xalign 0.5:
                    style_group "pref"
    
                    label _("Text Speed")
                    bar value Preference("text speed")
        
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
        
                hbox xalign 0.5:
                    spacing 30
                    style_group "pref"
    
                    vbox:
                        label _("{b}Skip{/b}")
                        textbutton _("Seen Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "seen")] hovered Play("audio", "se/sounds/select.ogg")
                        textbutton _("All Messages") action [Play("audio", "se/sounds/select3.ogg"), Preference("skip", "all")] hovered Play("audio", "se/sounds/select.ogg")
    
                    vbox:
                        label _("{b}After Choices{/b}")
                        textbutton _("Stop Skipping") action [Play("audio", "se/sounds/select3.ogg"), Preference("after choices", "stop")] hovered Play("audio", "se/sounds/select.ogg")
                        textbutton _("Keep Skipping") action [Play("audio", "se/sounds/select3.ogg"), Preference("after choices", "skip")] hovered Play("audio", "se/sounds/select.ogg")
                                  
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("textsettings_nav"), Show("preferences_nav"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        

init -2 python:

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 0.5

    style.pref_slider.left_bar = "image/ui/settings/bar_full.png"
    style.pref_slider.right_bar = "image/ui/settings/bar_empty.png"
    #style.pref_slider.hover_left_bar = "image/ui/bar_hover.png"
    style.pref_slider.thumb = "image/ui/settings/thumb.png"
    style.pref_slider.thumb_offset = 20
    style.pref_slider.thumb_shadow = None
    style.pref_slider.ymaximum = 64
    style.pref_slider.xmaximum = 750
    style.pref_slider.xalign = 0.5
    style.pref_slider.left_gutter = 20
    style.pref_slider.right_gutter = 20

    style.soundtest_button.background = None
    style.soundtest_button.xalign = 1.0
    #style.soundtest_button.hover_color = "#4D4D4D"
    
    style.pref_button.background = None
    
    style.pref_button_text.color = "#FFFFFF"
    style.pref_button_text.size = 32
    style.pref_button_text.hover_color = "#4D4D4D"
    style.pref_button_text.selected_color = "#4D4D4D"
    
    style.pref_label.xalign = 0.5
    style.pref_label_text.color = "#FFFFFF"
    style.pref_label_text.font = "Ardnas.otf"
    style.pref_label_text.size = 48

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:
    modal True
    window id "yesno" at popup:
        style "alertwindow"
    
        hbox xalign 0.5 yalign 0.8:
            spacing 250
            textbutton _("Yes") action [yes_action, Play("audio", "se/sounds/yes.wav")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"
            textbutton _("No") action [no_action, Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"
    
        label _(message):
            style "yesno_prompt"
            text_style "yesno_prompt_text"

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
transform quick_menu:
    zoom 1.5

screen quick_menu:

    # Add an in-game quick menu.
        hbox:
            style_group "quick"
        
            #xalign 0.98
            xalign 0.99
            yalign 0.98
            
            #spacing 30

            if persistent.showautoforwardbutton == True:

                imagebutton auto "image/ui/buttons/quick_save_%s.png" action [Play("audio", "se/sounds/yes.wav"), QuickSave()] at quick_menu hovered Play("audio", "se/sounds/select.ogg")
                imagebutton auto "image/ui/buttons/quick_load_%s.png" action [Play("audio", "se/sounds/alert.ogg"), QuickLoad()] at quick_menu hovered Play("audio", "se/sounds/select.ogg")
                imagebutton auto "image/ui/buttons/quick_skip_%s.png" action [Play("audio", "se/sounds/select3.ogg"), Skip()] at quick_menu hovered Play("audio", "se/sounds/select.ogg")
                imagebutton auto "image/ui/buttons/quick_auto_%s.png" action [Play("audio", "se/sounds/select3.ogg"), Preference("auto-forward", "toggle")] at quick_menu hovered Play("audio", "se/sounds/select.ogg")
            
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 0
    
    style.menu_overlay_button.background = None
    style.menu_overlay_button_text.size = 42
    style.menu_overlay_button_text.idle_color = "#8888"
    style.menu_overlay_button_text.font = "Ardnas.otf"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
          
##############################################################################
# Keymap
#

screen keymap_screen:
    key "K_F1" action Show('help')
    key "1" action QuickSave()
    key "2" action QuickLoad()


#another screen
screen my_keys():
    #Dismiss keys
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()    

#to stop
#show screen my_keys()

#to resume
#hide screen my_keys
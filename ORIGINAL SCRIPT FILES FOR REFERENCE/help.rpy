##############################################################################
# Help
#
    
screen help:
    modal True
    tag smallscreen
    window id "help" at popup:
        style "smallwindow"
        
        add "image/ui/help_title.png" xalign 0.01 yalign 0.1 at title_slide
        
        text _("\nLeft Click, Enter - Select                                  F Key - Fullscreen\nDel Key - Delete save                                        S Key - Screenshot\nRight Click, Esc - Menu                                      Middle Click - Hide text\nSpace - Advance\nArrow Keys - Select up/down\nCtrl - Skip\nTab - Toggle skip\nMousewheel, Page Up/Down - Rollback and Rollforward") style "smallwindow_text" size 30
            
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("help"), Hide("preferencesbg", transition=dissolve), Play("sound", "se/sounds/close.ogg")] hovered Play("sound", "se/sounds/select.ogg") style "smallwindowclose" at nav_button

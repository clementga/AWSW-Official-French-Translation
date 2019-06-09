init python:

    # Step 1. Create the gallery object.
    g = Gallery()
    
    # Locked and hover images
    
    g.hover_border ="image/ui/gallery/gallery_hover.png"
    #hover Play("sound", "se/sounds/select.ogg")
    g.locked_button = "image/ui/gallery/gallery_locked.png"

    # Step 2. Add buttons and images to the gallery.

    # A button that contains an image that automatically unlocks.
    g.button("dawn")
    g.image("test")
    g.unlock("test")

    # This button has multiple images assocated with it. We use unlock_image
    # so we don't have to call both .image and .unlock. We also apply a
    # transform to the first image.
    g.button("dark")
    g.unlock_image("bigbeach1")
    g.unlock_image("beach1 mary")
    g.unlock_image("beach2")
    g.unlock_image("beach3")

    # This button has a condition associated with it, allowing code
    # to choose which images unlock.
    g.button("end1")
    g.condition("persistent.unlock_1")
    g.image("transfer")
    g.image("moonpic")
    g.image("girlpic")
    g.image("nogirlpic")
    g.image("bad_ending")

    g.button("end2")
    g.condition("persistent.unlock_2")
    g.image("library")
    g.image("beach1 nomoon")
    g.image("bad_ending")

    g.button("1")#, hover Play("sound", "se/sounds/select.ogg")
    g.condition("persistent.remygoodending")
    g.image("extra1")
    #hover Play("sound", "se/sounds/select.ogg")

    g.button("2")
    g.condition("persistent.annagoodending")
    g.image("extra2")

    g.button("3")
    g.condition("persistent.loremgoodending")
    g.image("extra3")

    g.button("4")
    g.condition("persistent.brycegoodending")
    g.image("extra4")

    g.button("5")
    g.condition("persistent.adinegoodending")
    g.image("extra5")

    g.button("6")
    g.condition("persistent.sebastianplayed")
    g.image("extra6")

    g.button("7")
    g.condition("persistent.playedzhong")
    g.image("extra7")

    g.button("8")
    g.condition("persistent.playedemera")
    g.image("extra8")

    g.button("9")
    g.condition("persistent.playedkatsu")
    g.image("extra9")

    g.button("10")
    g.condition("persistent.playedkevin")
    g.image("extra10")

    g.button("11")
    g.condition("persistent.evilending")
    g.image("extra11")

    g.button("12")
    g.condition("persistent.trueending")
    g.image("extra12")

    # The last image in this button has an condition associated with it,
    # so it will only unlock if the user gets both endings.
    g.button("end3")
    g.condition("persistent.unlock_3")
    g.image("littlemary2")
    g.image("littlemary")
    g.image("good_ending")
    g.condition("persistent.unlock_3 and persistent.unlock_4")

    g.button("end4")
    g.condition("persistent.unlock_4")
    g.image("hospital1")
    g.image("hospital2")
    g.image("hospital3")
    g.image("heaven")
    g.image("white")
    g.image("good_ending")
    g.condition("persistent.unlock_3 and persistent.unlock_4")

    # The final two buttons contain images that show multiple pictures
    # at the same time. This can be used to compose character art onto
    # a background.
    g.button("dawn mary")
    g.unlock_image("dawn1", "mary dawn wistful")
    g.unlock_image("dawn1", "mary dawn smiling")
    g.unlock_image("dawn1", "mary dawn vhappy")

    g.button("dark mary")
    g.unlock_image("beach2", "mary dark wistful")
    g.unlock_image("beach2", "mary dark smiling")
    g.unlock_image("beach2", "mary dark vhappy")

    # The transition used when switching images.
    g.transition = dissolve

# Step 3. The gallery screen we use.
screen gallery:
    modal True
    frame:
        add "image/ui/gallery/gallery_bg.png" xalign 0.5 yalign 0.5 at alpha_dissolve
        add "image/ui/ingame_menu_bg_light.png" at ingame_menu_light
        #hovered Play("sound", "se/sounds/select.ogg")
    
    imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action  [Hide("gallery", transition=dissolve), Hide("gallery_page"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" xalign 0.945 yalign 0.035 at nav_button

screen gallery_page_1:
    
    tag gallery_page
    
    grid 4 3:
        xalign 0.5
        yalign 0.5
        spacing 40

        # Call make_button to show a particular button.
        add g.make_button("1", "image/ui/gallery/extrax1.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg") #hovered Play("sound", "se/sounds/select.ogg")
        add g.make_button("2", "image/ui/gallery/extrax2.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")
        add g.make_button("3", "image/ui/gallery/extrax3.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")
        add g.make_button("4", "image/ui/gallery/extrax4.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")

        add g.make_button("5", "image/ui/gallery/extrax5.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")
        add g.make_button("6", "image/ui/gallery/extrax6.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")
        add g.make_button("7", "image/ui/gallery/extrax7.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")
        add g.make_button("8", "image/ui/gallery/extrax8.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")

        add g.make_button("9", "image/ui/gallery/extrax9.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")
        add g.make_button("10", "image/ui/gallery/extrax10.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")
        add g.make_button("11", "image/ui/gallery/extrax11.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")
        add g.make_button("12", "image/ui/gallery/extrax12.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None, hover_sound="se/sounds/select.ogg", activate_sound="se/sounds/select3.ogg")

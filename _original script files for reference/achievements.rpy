#63 total achievements

screen achievements:
    tag smallscreen
    window id "save" at popup_offcenter: #remove the _offcenter bit to change the alignment
        style "smallwindow_big2" #remove 2 to change the window size If you see this, you shouldn't be looking at this code. There is nothing to find here.
        # You can insert a variable here by using [variable]
        # text "Achievement progress: [variable]" xalign 0.92 yalign 0.8 size 22
        if persistent.secretending == True:
            text _("Achievement progress: [persistent.achievements]+1/63") xalign 0.92 yalign 0.85 size 22
        else:
            text _("Achievement progress: [persistent.achievements]/63") xalign 0.92 yalign 0.85 size 22
        add "image/ui/navmenu/achievements.png" yalign 0.1 zoom 0.6 at title_slide
    
        
screen achievement_page_1:
    tag achievement_page
    window at popup_offcenter:
        background None
        xpadding 0
        ypadding 0
        #xalign 0.5 yalign 0.5
        imagebutton idle "image/ui/filepicker/Btn_Prev.png" hover "image/ui/filepicker/Btn_Prevx.png" action [Show('achievement_page_5'), Play("audio", "se/sounds/select3.ogg")] xalign 0.12 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
        imagebutton idle "image/ui/filepicker/Btn_Next.png" hover "image/ui/filepicker/Btn_Nextx.png" action [Show('achievement_page_2'), Play("audio", "se/sounds/select3.ogg")] xalign 0.88 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
        vbox:
            xalign 0.2
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.c1blood == True:
                    
                    add "achievements/blood_donation.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Blood Donation{/b}\nGive Anna your blood.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1fish == True:
                    
                    add "achievements/bravery.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Bravery{/b}\nOrder the daily special.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1books == True:
                    
                    add "achievements/bookworm.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Bookworm{/b}\nRead a bunch of books.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1meds == True:
                    
                    add "achievements/prescription.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Prescription{/b}\nTake a dragon dose of medication.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1liquid == True:
                    
                    add "achievements/daredevil.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Daredevil{/b}\nDrink a mysterious liquid.") style "achievement_text"
        vbox:
            xalign 0.5
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.c1eggs == True:
                    
                    add "achievements/ovicide.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Ovicide{/b}\nWaste a perfectly good batch of eggs.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1fruits == True:
                    
                    add "achievements/fruitarian.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Fruitarian{/b}\nLearn a lot about fruits.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1decline == True:
                    
                    add "achievements/nuisance.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Nuisance{/b}\nRefuse to help Bryce 99 times.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1invhigh == True:
                    
                    add "achievements/investigator_1.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Investigator 1{/b}\nDo well on the first investigation.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1booksort == True:
                    
                    add "achievements/librarian.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Librarian{/b}\nBring Remy's books into the correct order.") style "achievement_text"
        vbox:
            xalign 0.8
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.c1boredom == True:
                    
                    add "achievements/patient.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Patient{/b}\nWait for Remy until you get bored.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1annaanswers == True:
                    
                    add "achievements/general_knowledgist.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}General Knowledgist{/b}\nAnswer Anna's questions correctly.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1teetotaler == True:
                    
                    add "achievements/teetotaler.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Teetotaler{/b}\nReject Bryce's invitation.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1disrobement == True:
                    
                    add "achievements/disrobement.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Disrobement{/b}\nGet Adine to remove her headgear.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c1bastion == True:
                    
                    add "achievements/you_are_a_winner.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}You are a winner!{/b}\nBeat Sebastian at his own game.") style "achievement_text"
                
screen achievement_page_2:
    tag achievement_page
    window at popup_offcenter:
        background None
        xpadding 0
        ypadding 0
        imagebutton idle "image/ui/filepicker/Btn_Prev.png" hover "image/ui/filepicker/Btn_Prevx.png" action [Show('achievement_page_1'), Play("audio", "se/sounds/select3.ogg")] xalign 0.12 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
        imagebutton idle "image/ui/filepicker/Btn_Next.png" hover "image/ui/filepicker/Btn_Nextx.png" action [Show('achievement_page_3'), Play("audio", "se/sounds/select3.ogg")] xalign 0.88 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5

        vbox:
            xalign 0.2
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.c2interrogator == True:
                    
                    add "achievements/interrogator_1.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Interrogator 1{/b}\nInterrogate Damion.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c2bandage == True:
                    
                    add "achievements/finders_keepers.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Finders, Keepers{/b}\nAcquire the bloody bandage.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.dirttaken == True:
                    
                    add "achievements/archeologist.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Archeologist{/b}\nFind a handful of dirt.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c2landscape == True:
                    
                    add "achievements/landscaper.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Landscaper{/b}\nAppreciate the landscape.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.orb_taken == True:
                    
                    add "achievements/orb_finder.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Orb Finder{/b}\nFind a mysterious orb.") style "achievement_text"
        vbox:
            xalign 0.5
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.c2storeaisles == True:
                    
                    add "achievements/window_shopper.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Window Shopper{/b}\nLook at everything the store has to offer.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c2investigation == True:
                    
                    add "achievements/investigator_2.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Investigator 2{/b}\nDo well on the second investigation.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c2pictures == True:
                    
                    add "achievements/memories.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Memories{/b}\nLook at Remy's pictures.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.heardaboutcancerenvelope == True:
                    
                    add "achievements/snoop.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Snoop{/b}\nLook at Anna's envelope.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c2legs == True:
                    
                    add "achievements/leg_stretcher.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Leg Stretcher{/b}\nStretch your legs.") style "achievement_text"
        vbox:
            xalign 0.8
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.c2eau == True:
                    
                    add "achievements/eau_de_dragon.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Eau de Dragon{/b}\nExamine Bryce's blanket.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c2magazine == True:
                    
                    add "achievements/research_material.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Research Material{/b}\nLook at Bryce's magazine.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c2music == True:
                    
                    add "achievements/audiophile.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Audiophile{/b}\nListen to a bunch of music.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.playedemera == True:
                    
                    add "achievements/the_politician.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}The Politician{/b}\nMeet with Emera.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.havemapfirst == True:
                    
                    add "achievements/cartographer.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Cartographer{/b}\nAcquire a map.") style "achievement_text"

screen achievement_page_3:
    tag achievement_page
    window at popup_offcenter:
        background None
        xpadding 0
        ypadding 0
        imagebutton idle "image/ui/filepicker/Btn_Prev.png" hover "image/ui/filepicker/Btn_Prevx.png" action [Show('achievement_page_2'), Play("audio", "se/sounds/select3.ogg")] xalign 0.12 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
        imagebutton idle "image/ui/filepicker/Btn_Next.png" hover "image/ui/filepicker/Btn_Nextx.png" action [Show('achievement_page_4'), Play("audio", "se/sounds/select3.ogg")] xalign 0.88 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
    
        vbox:
            xalign 0.2
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.base_taken == True:
                    
                    add "achievements/base_finder.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Base Finder{/b}\nFind a mysterious base.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c3prank == True:
                    
                    add "achievements/prankster.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Prankster{/b}\nPlay a prank on Bryce.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c3helpedkatsu == True:
                    
                    add "achievements/altruist.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Altruist{/b}\nHelp Katsuharu.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c3interrogator == True:
                    
                    add "achievements/interrogator_2.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Interrogator 2{/b}\nInterrogate Anna.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.varasaved == True:
                    
                    add "achievements/stalker.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Stalker{/b}\nFollow Vara.") style "achievement_text"
        vbox:
            xalign 0.5
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.c3reckless == True:
                    
                    add "achievements/reckless.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Reckless{/b}\nGo to the portal.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c3investigator == True:
                    
                    add "achievements/investigator_3.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Investigator 3{/b}\nDo well on the third investigation.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c3flawless == True:
                    
                    add "achievements/flawless_run.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Flawless Run{/b}\nDo well in all investigations in a single playthrough.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.seashells == True:
                    
                    add "achievements/souvenir.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Souvenir{/b}\nKeep the seashells.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.playedkatsu == True:
                    
                    add "achievements/the_artisan.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}The Artisan{/b}\nMeet with Katsuharu.") style "achievement_text"
        vbox:
            xalign 0.8
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.c4eggs == True:
                    
                    add "achievements/in_loco_parentis.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}In Loco Parentis{/b}\nReturn the eggs to the hatchery.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.ixomenassembled == True:
                    
                    add "achievements/sphere_builder.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Sphere Builder{/b}\nAssemble the sphere.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.playedkevin == True:
                    
                    add "achievements/the_student.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}The Student{/b}\nMeet with Kevin.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.lazy == True:
                    
                    add "achievements/lazy.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Lazy{/b}\nDecide not to meet anyone or investigate 10 times.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.skip == True:
                    
                    add "achievements/fast_forward.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Fast Forward{/b}\nSkip ahead 10 times.") style "achievement_text"

screen achievement_page_4:
    tag achievement_page
    window at popup_offcenter:
        background None
        xpadding 0
        ypadding 0
        imagebutton idle "image/ui/filepicker/Btn_Prev.png" hover "image/ui/filepicker/Btn_Prevx.png" action [Show('achievement_page_3'), Play("audio", "se/sounds/select3.ogg")] xalign 0.12 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
        imagebutton idle "image/ui/filepicker/Btn_Next.png" hover "image/ui/filepicker/Btn_Nextx.png" action [Show('achievement_page_5'), Play("audio", "se/sounds/select3.ogg")] xalign 0.88 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
    
        vbox:
            xalign 0.2
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.popular == True:
                    
                    add "achievements/popular.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Popular{/b}\nHave two messages waiting for you at the same time.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.c3pointless == True:
                    
                    add "achievements/utterly_pointless_achievement.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Utterly Pointless Achievement{/b}\nDo a thing.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.izumimask == True:
                    
                    add "achievements/unmasking.png" xalign 0.5
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                text _("{b}Unmasking{/b}\nSee what lies beneath the mask.") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.firstending == True:
                    
                    add "achievements/it_begins.png" xalign 0.5
                    text _("{b}It Begins{/b}\nSee your first ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.neutralending == True:
                    
                    add "achievements/detonation.png" xalign 0.5
                    text _("{b}Detonation{/b}\nSee the neutral ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
        vbox:
            xalign 0.5
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.remybadending == True:
                    
                    add "achievements/alone.png" xalign 0.5
                    text _("{b}Alone{/b}\nSee Remy's bad ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.remygoodending == True:
                    
                    add "achievements/casualties_of_war.png" xalign 0.5
                    text _("{b}Casualties of War{/b}\nSee Remy's good ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.annabadending == True:
                    
                    add "achievements/sacrifice.png" xalign 0.5
                    text _("{b}Sacrifice{/b}\nSee Anna's bad ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.annagoodending == True:
                    
                    add "achievements/tragic_hero.png" xalign 0.5
                    text _("{b}Tragic Hero{/b}\nSee Anna's good ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.lorembadending == True:
                    
                    add "achievements/remember.png" xalign 0.5
                    text _("{b}Remember{/b}\nSee Lorem's bad ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
        vbox:
            xalign 0.8
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.loremgoodending == True:
                    
                    add "achievements/the_plan.png" xalign 0.5
                    text _("{b}The Plan{/b}\nSee Lorem's good ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.brycebadending == True:
                    
                    add "achievements/catastrophy.png" xalign 0.5
                    text _("{b}Catastrophy{/b}\nSee Bryce's bad ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.brycegoodending == True:
                    
                    add "achievements/murderer.png" xalign 0.5
                    text _("{b}Murderer{/b}\nSee Bryce's good ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.adinebadending == True:
                    
                    add "achievements/getaway.png" xalign 0.5
                    text _("{b}Getaway{/b}\nSee Adine's bad ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.adinegoodending == True:
                    
                    add "achievements/decisions.png" xalign 0.5
                    text _("{b}Decisions{/b}\nSee Adine's good ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"

screen achievement_page_5:
    tag achievement_page
    window at popup_offcenter:
        background None
        xpadding 0
        ypadding 0
        imagebutton idle "image/ui/filepicker/Btn_Prev.png" hover "image/ui/filepicker/Btn_Prevx.png" action [Show('achievement_page_4'), Play("audio", "se/sounds/select3.ogg")] xalign 0.12 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
        imagebutton idle "image/ui/filepicker/Btn_Next.png" hover "image/ui/filepicker/Btn_Nextx.png" action [Show('achievement_page_1'), Play("audio", "se/sounds/select3.ogg")] xalign 0.88 yalign 0.55 at top_button hovered Play("audio", "se/sounds/select.ogg") #yalign changed from 0.5
    
        vbox:
            xalign 0.2
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                if persistent.evilending == True:
                    
                    add "achievements/betrayal.png" xalign 0.5
                    text _("{b}Betrayal{/b}\nSee the evil ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.optimist == True:
                    
                    add "achievements/optimist.png" xalign 0.5
                    text _("{b}Optimist{/b}\nSee your first good ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"
            hbox:
                spacing 5
                
                if persistent.trueending == True:
                    
                    add "achievements/hope.png" xalign 0.5
                    text _("{b}Hope{/b}\nSee the true ending.") style "achievement_text"
                    
                else:
                
                    add "image/ui/achievements/locked_achievement.png" xalign 0.5
                    text _("{b}Hidden Achievement{/b}") style "achievement_text"

            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"
                
            

            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"

        vbox:
            xalign 0.5
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"
                
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"
                
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"
                
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "" style "achievement_text"
                
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"

            
        vbox:
            xalign 0.8
            yalign 0.6
            spacing 10
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"
                
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"
                
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"
                
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"
                
            hbox:
                spacing 5
                
                    
                add "achievements/translucent.png" xalign 0.5
                #text "{b}Hope{/b}\nSee the true ending." style "achievement_text"

    
    
style achievement_text is default:
    xmaximum 300
    yalign 0.5
    size 20


#Maybe you found something after all
###
#
#
#
#
 #                                                                  
  #                                                                 
   #                                                                
    #                                                               
     #                                                              
      #                                                             
       #                                                            
       #                                                            
       #                                                            
      #           `                                                 
     #          :                                                   
     #         ..     ,.                                            
    #        ,.;    :,                                              
   #        .,;;;;'.;                                               
  #         ,;;;;'.;.                                               
 #         :,;;;',;;'                                               
#       `;:,;'';:;;;;;',;                                           
#      .:`';'  ,:;;;:';;                                            
#      ;.''''` `++;,;;;;                                            
#       '',,;;'''',:''''::'.                                        
#      ',,,,,,'':',;,';;;'                                          
#     .;,,,,,'',,;';;;',''  `                                       
#       ;:,,`;,,,,'::;;;;;                                          
#      ';;,:,,,,,,;,;:::;;                                          
#     :,,,:,:,,,,,:,':;;.,::.                                       
#    `,,,,,;,,,;.`,,,:,::::                                         
#     ,,,,,.:,.:..:,,,;;:::                                         
#      ,,,;.,  ...;,,:,;,;:`                                        
#           '  ,..;,,,,:':;,.                                       
#           '  :..',,,,,,:::,                                       
#           ;  `.';,,,,,:'::                                        
#          :`  ,.;,,,,,,,,::'.                                      
#          '   :.;,,,,,,,,;;:                                       
#          '   ..;,,,,,,,,,,;                                       
#              ..:,,,,,,,,,,,;                                      
#              ...,,,,,,,,,,,,                              .:      
#             ;...,,,,,,.,,,,,;                              :`     
#             ....,,,,,,,,,,,,,                              :,     
#             ....,,,,,;,,,,,,,:                             ,,     
#             .....,,,,,,,,,,,,,;                            ;.     
#             ......,,,:,,,,,,,,,,                    .      .,     
#             ........,,;,,,,,,,,,:                   `     :,;     
#             ........,,,,,,,,,,,,,:                   '  ..,.      
#             .......,,,,,,,,,,,,,,,:                   ,,,,,:      
#             :......,,,,,,,,,,,,,,,,                    ;.;,.      
#             `......,,,,,,,,,,,,,,,,`                      ,,      
#             :;.....,,,,,,,,,,,,,,,,.                      ,,      
#             ,,.....,,,:,,,,,,,,,,,,.                      :,;     
#            `,,:....,,,;,,,,,,,,,,,,:                      :,,     
#            :,,,:....,,,,,,,,,,,,,,,'                      ;,,     
#            ,,,,,....,,,,,,,,,,,,,,,;                      ;,,     
#           ,,,,,,'...,;,,,,,,,,,,,,,:                      :,,     
#           :,,,,,,....,,,,,,,,,,,,,,,                      ,,,     
#           ,,,,,,,...,,,,,,,,,,,,,,,:'                     ,,,     
#          .,,,,,,,:..,,,,,,,,,,,,,,,,,.                    ,,,     
#          :,,,,,,,:.;,,,,,,,,,,,,,,,:,:                   ,,,:     
#          ,,,,,,,,;.,,,,,,,,,,,,,,,,:,,.                  ,,,.     
#          ,,,,,,,:',,,,,,,,,,,,,,,,,:,,;                 .,,,      
#         ;,,,,,,;;;,,,,,,,,,,,,,,,,,,,,:                :,,,,      
#         ,,,,,,;;;;,,,,,,,,,,,,,,,,,,,:,`              ;,,,,.      
#         ,,,,,;;;;',,,,,,,,,,,,,,,,,,:,,'             ::,,,,       
#        :,,,,;;;;;:,,,,,,,,,,,,,,,,,,,,,:            ::,,,,`       
#        ,,,,;;;;:,,,,,,,,,,,,,,,,,,,,,,:,;         ;,,,,,,:        
#        ,,,':, `,,,,,,,,,,,,,,,,,,,,,,,,,:       :;,,,,,,,         
#        ,,,:   ,,;,,,,,,,,,,,,,,,,,,,,,::,;',,:,,;,,,,,,,          
#       .,,    :,:',,,,,,,,,,,,,,,,,,,,,:,,:,:;,,:,,,,,,,,          
#       ':;   ,,,''',,,,,,,,,,,,,,,,,,,,,:,,;,,,,,,,,,,,:           
#      ;;';   ,,,':'+;,,,,,..,,,,,,,,,::,,,,,;,,,,,,,,,:            
#      ;'`'  :,,,+'''+,,,,..,,,,,,,,,:,,,,,,,;,,,,,,,,,             
#     `+'`, .,,,,,';',,,,,,,,,,,,,,,,:,:,:,,,:,,,,,..               
#     .; .  ,,,,,,,,,,,,,,,,,,,,,,:,,,:,,,,,:'.....:                
#      .   ,,,,,,,,,,,,,:,,,,,,,,:,,:,,,,,,:,::;:`                  
#          :,,,,,,,,,,,,,',,,,,,,:,,:,,,,,:,,,:                     
#          ,,,,,,,,,,,,,` :,,,,,,,,::,,,:,:,,,:                     
#          ,,,,,,,,,,,,     `,,,,,,,,,,,,,,,,,,,                    
#         `,,,,,,,,,;,         ::,,,,,,,,,.,,,,:                    
#          ,,,,,,,,,,,,;`       ,,::,,,,,,,,,,,,:                   
#           ',,,,,,,,,,,,       :,,,,;,,,,,,,,,,:                   
#              :,,,,,,,,.       `,,,,, `,,,,,,,,,'                  
#                 :,,,,;         ,,,,,    :,,:::,:                  
#                 ,,,,,          ;,,,,`     .,,,,,;                 
#                ;,,,,`           ,,,,;        ',,,:                
#                ,,,,:            ,,,,,          ;,;                
#               ,,,,,             :,,,,            :'               
#               ,,,,,              ,,,,.            .               
#              .,,,,:              ,,,,:             :              
#              ,,,,,               ,,,,:                            
#             :,,,,,               ,,,,:                            
#         `  :,,,,,,.             :,,,,,                            
#      '+:,,,,,,,,,,;;;;         :,,,,,,`                           
#    ''''',,,,,,,,,;'.          .,,,,,,,;                           
#   +''';:::::`               `'';''':;;,                           
#                             '''''''';;;                           
#                             '''+'''';;;.                          
#                            ;'' '''`';;'                           
#                                :.   ,;                            
#                                                                   
#                                                                   
                                                                   

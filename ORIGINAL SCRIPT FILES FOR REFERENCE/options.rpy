init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = "auto"
    config.autoreload = False

    config.fix_rollback_without_choice = True

    ## These control the width and height of the screen.

    config.screen_width = 1920
    config.screen_height = 1080

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Angels with Scaly Wings"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "Angels with Scaly Wings"
    config.version = "1.05"

    # User defined layers
    config.layers = [ 'master', 'texture', 'transient', 'screens', 'overlay' ]
    
    # Music channel
    renpy.music.register_channel("nature", "sfx", True)
    renpy.music.register_channel("nature2", "sfx", True)
    renpy.music.register_channel("nature3", "sfx", True)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("soundloop", "sfx", True)
    renpy.music.register_channel("movie2", "sfx", True)
    
    # Auto voice
    config.auto_voice = "voice/english/{id}.ogg"
    
    # Mouse cursor
    config.mouse = { 'default' : [ ('image/ui/cursor.png', 15, 15)] } 
    
    # Window icon
    config.window_icon = "icon1.png"
    config.windows_icon = "icon3.png"

    # Theme
    theme.roundrect(
        ## Theme: Roundrect
        ## Color scheme: Basic Blue
                                    
        ## The color of an idle widget face.
        widget = "#003c78",

        ## The color of a focused widget face.
        widget_hover = "#0050a0",

        ## The color of the text in a widget.
        widget_text = "#c8ffff",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ffffc8",

        ## The color of a disabled widget face. 
        disabled = "#404040",

        ## The color of disabled widget text.
        disabled_text = "#c8c8c8",

        ## The color of informational labels.
        label = "#ffffff",

        ## The color of a frame containing widgets.
        frame = "#6496c8",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "#dcebff",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#dcebff",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )
    
    # Transitions
    menudissolve = Dissolve(0.2)
    longdissolve = Dissolve(4.0)
    
    # Quit
    config.quit_action = Quit(confirm=True)

    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("image/ui/dialogbox.png", 0, 0)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    #style.window.left_margin = 20
    #style.window.right_margin = 20
    #style.window.top_margin = 20
    #style.window.bottom_margin = 20

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 250
    style.window.right_padding = 250
    style.window.top_padding = 30
    style.window.bottom_padding = 0

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 330
    style.window.yalign = 1.0

    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "TitilliumWeb-Regular.ttf"

    ## The default size of text.

    style.default.size = 39

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    config.has_sound = True
    config.has_music = True
    config.has_voice = True

    ## Sounds that are used when button and imagemaps are clicked.

    style.button.activate_sound = "se/sounds/select.ogg"
    style.imagemap.activate_sound = "se/sounds/select.ogg"

    ## Sounds that are used when entering and exiting the game menu.

    config.enter_sound = "se/sounds/menuopen.wav"
    config.exit_sound = "se/sounds/close.ogg"

    ## A sample sound that can be played to check the sound volume.

    config.sample_sound = "se/sounds/test.wav"
    config.sample_voice = "se/sounds/samplevoice.ogg"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "mx/menu.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = None

    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = menudissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = menudissolve

    ## Used between screens of the game menu.
    config.intra_transition = menudissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = menudissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = menudissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = Dissolve(2.0)

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = menudissolve

    ## Used when a game is loaded.
    config.after_load_transition = menudissolve

    ## Used when the window is shown.
    config.window_show_transition = menudissolve

    ## Used when the window is hidden.
    config.window_hide_transition = menudissolve

    config.say_attribute_transition = dissolve


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "Angels with Scaly Wings"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 60

    #########################################
    ## More customizations can go here.
    
    style.default.drop_shadow = [(1, 1)]
    #style.drop_shadow_color = "#000"
    
    #All frames
    style.frame.background = None
    style.frame.ypadding = 0
    style.frame.xpadding = 0
    
    #Style for Alert Box
    style.alertwindow = Style(style.default)
    style.alertwindow.background = "image/ui/menubg_options.png"
    style.alertwindow.xmaximum = 1920
    style.alertwindow.ymaximum = 300
    style.alertwindow.xpadding = 0
    style.alertwindow.ypadding = 0
    
    #Style for Small Menu Box
    style.smallwindow = Style(style.default)
    style.smallwindow.background = "image/ui/smallwindow.png"
    style.smallwindow.xalign = 0.5
    style.smallwindow.yalign = 0.5
    style.smallwindow.xmaximum = 1920
    style.smallwindow.ymaximum = 550
    style.smallwindow.xpadding = 0
    style.smallwindow.ypadding = 0
    
    #Style for Small Menu Box (Body text)
    style.smallwindow_text.size = 32
    style.smallwindow_text.drop_shadow = (1,1)
    style.smallwindow_text.color = "#FFFFFF"
    style.smallwindow_text.xpos = 300
    style.smallwindow_text.ypos = 40
    style.smallwindow_text.xmaximum = 1800
    #style.smallwindow_text.drop_shadow = None
    
    #Style for Small Menu Box (Bigger)
    style.smallwindow_big = Style(style.default)
    style.smallwindow_big.background = "image/ui/smallwindow_big.png"
    style.smallwindow_big.xalign = 0.5
    style.smallwindow_big.yalign = 0.5
    style.smallwindow_big.xysize = (1920,750)
    style.smallwindow_big.xpadding = 0
    style.smallwindow_big.ypadding = 0
    
    #Style for Small Menu Box (Body text)
    style.smallwindow_big_text.size = 32
    style.smallwindow_big_text.drop_shadow = (1,1)
    style.smallwindow_big_text.color = "#FFFFFF"
    style.smallwindow_big_text.xpos = 300
    style.smallwindow_big_text.ypos = 40
    style.smallwindow_big_text.xmaximum = 1800
    
    #Style for Small Menu Box (Bigger)
    style.smallwindow_big2 = Style(style.default)
    style.smallwindow_big2.background = "image/ui/smallwindow_big2.png"
    style.smallwindow_big2.xalign = 0.5
    style.smallwindow_big2.yalign = 0.75
    style.smallwindow_big2.xysize = (1920,880)
    style.smallwindow_big2.xpadding = 0
    style.smallwindow_big2.ypadding = 0
    
    #Style for Small Menu Box (Body text)
    style.smallwindow_big2_text.size = 32
    style.smallwindow_big2_text.drop_shadow = (1,1)
    style.smallwindow_big2_text.color = "#FFFFFF"
    style.smallwindow_big2_text.xpos = 300
    style.smallwindow_big2_text.ypos = 40
    style.smallwindow_big2_text.xmaximum = 1800
    #Style for Small Menu Box (Close button)
    style.smallwindowclose = Style(style.default)
    style.smallwindowclose.xmaximum = 34
    style.smallwindowclose.ymaximum = 56
    style.smallwindowclose.xpos = 1860
    style.smallwindowclose.ypos = 65
    
    #Text style for yes/no prompt
    style.yesno_prompt.xalign = 0.5
    style.yesno_prompt.yalign = 0.3
    style.yesno_prompt_text.color = "#000"
    #style.yesno_prompt_text.hover_color = "#FF0000"
    style.yesno_prompt_text.size = 48
    style.yesno_prompt_text.font = "Ardnas.otf"
    style.yesno_prompt_text.drop_shadow = None
    
    #Style for Menu Button
    style.menubutton = Style(style.default)
    style.menubutton.xalign = 0.5
    style.menubutton_text.color = "#FFFFFF"
    style.menubutton_text.size = 68
    style.menubutton_text.font = "Ardnas.otf"
    style.menubutton_text.drop_shadow = (2,2)
    style.menubutton_text.hover_color = "#4D4D4D"
    #style.menubutton_text.selected_color = "#4D4D4D"
    
    #Style for Menu Button 2
    style.menubutton2 = Style(style.default)
    style.menubutton2.xalign = 0.5
    style.menubutton2_text.color = "#FFFFFF"
    style.menubutton2_text.size = 52
    style.menubutton2_text.font = "Ardnas.otf"
    style.menubutton2_text.drop_shadow = (2,2)
    style.menubutton2_text.hover_color = "#4D4D4D"
    #style.menubutton2_text.selected_color = "#4D4D4D"
    
    #Style for Yes/No Button
    style.yesnobutton = Style(style.default)
    style.yesnobutton.xalign = 0.5
    style.yesnobutton_text.color = "#000"
    style.yesnobutton_text.size = 80
    style.yesnobutton_text.font = "Ardnas.otf"
    style.yesnobutton_text.drop_shadow = None
    style.yesnobutton_text.hover_color = "#4D4D4D"
    
    #Text style for buttons
    style.button_text.color = "#fff"
    style.button_text.size = 40
    
    #Text style for subtitles
    style.subtitle_text.size = 52
    style.subtitle_text.text_align = 0.5
    style.subtitle_text.xalign = 0.5
    style.subtitle_text.yalign = 0.9
    style.subtitle_text.outlines = [(3, "#000000")]
    style.subtitle_text.xmaximum = 1700
    #style.subtitle_text.slow_cps = True 
    
    #Text style for top subtitles
    style.subtitle2_text.size = 52
    style.subtitle2_text.text_align = 0.5
    style.subtitle2_text.xalign = 0.5
    style.subtitle2_text.yalign = 0.1
    style.subtitle2_text.outlines = [(3, "#000000")]
    style.subtitle2_text.xmaximum = 1700
    #style.subtitle2_text.slow_cps = True 

    #Change the screenshot for saves
    config.thumbnail_width = 160
    config.thumbnail_height = 90
    
    # Position the navigation on the right side of the screen.
    style.gallery_nav_frame.xpos = 1280 - 10
    style.gallery_nav_frame.xanchor = 1.0
    style.gallery_nav_frame.ypos = 12
    
    # Name label
    style.say_label.size = 62
    style.say_label.bold = False
    style.say_label.font = "Ardnas.otf"
    
    # NVL Window
    style.nvl_window.background = "image/ui/nvlscreen.png"
    style.nvl_window.top_padding = 200
    style.nvl_window.left_padding = 200
    style.nvl_window.right_padding = 200
    style.nvl_window.bottom_padding = 200
    
    style.narrator_text.italic = True
                         
## This section contains information about how to build your project into 
## distribution files.
init python:
    
    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Scaly-Wings"
    
    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Angels with Scaly Wings"
    
    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False
    
    ## File patterns:
    ## 
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##    
    ##
    ## In a pattern:
    ##
    ## / 
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("**.rpy", None)
    
    ## To archive files, classify them as 'archive'.
    
    # Base
    build.classify('game/**.rpyb', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/**.ico', 'archive')
    build.classify('game/**.icns', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.ogv', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.abc', 'archive')
    build.classify('game/**.aw2', 'archive')
    build.classify('game/**.aw3', 'archive')
    build.classify('game/**.mp4', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    
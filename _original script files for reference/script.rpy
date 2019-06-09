
#typing function

init python:
    
    def my_func():
        
        if renpy.display.interface.last_event.__dict__.get("key", None) == 8:
            
            renpy.music.play("fx/delete.ogg", channel="audio")
            
        else:
            
            renpy.music.play("fx/type.ogg", channel="audio")


#tennis code here

init:

    image bg pong field = "pong_field.png"

    python:

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                # Some displayables we use.
                self.paddle = Image("pong.png")
                self.ball = Image("pong_ball.png")
                self.player = Text(_("Player"), size=36)
                self.eileen = Text(_("System"), size=36)
                self.ctb = Text(_("Click to Begin"), size=36)

                # The sizes of some of the images.
                self.PADDLE_WIDTH = 15 #8
                self.PADDLE_HEIGHT = 142 #79
                self.BALL_WIDTH = 27 #15
                self.BALL_HEIGHT = 27 #15
                self.COURT_TOP = 194 #108
                self.COURT_BOTTOM = 976 #543

                # If the ball is stuck to the paddle.
                self.stuck = True

                # The positions of the two paddles.
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = self.playery

                # The speed of the computer.
                self.computerspeed = 630.0 #350.0

                # The position, dental-position, and the speed of the
                # ball.
                self.bx = 398 #88 = 58 + 30/ 344 + 54
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                self.bspeed = 540.0 #300.0

                # The time of the past render-frame.
                self.oldst = None

                # The winner.
                self.winner = None

            def visit(self):
                return [ self.paddle, self.ball, self.player, self.eileen, self.ctb ]

            # Recomputes the position of the ball, handles bounces, and
            # draws the screen.
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                # Figure out the time elapsed since the previous frame.
                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                # Figure out where we want to move the ball to.
                speed = dtime * self.bspeed
                oldbx = self.bx

                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed

                # Move the computer's paddle. It wants to go to self.by, but
                # may be limited by it's speed limit.
                cspeed = self.computerspeed * dtime
                if abs(self.by - self.computery) <= cspeed:
                    self.computery = self.by
                else:
                    self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

                # Handle bounces.

                # Bounce off of top.
                ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
                if self.by < ball_top:
                    self.by = ball_top + (ball_top - self.by)
                    self.bdy = -self.bdy
                    renpy.sound.play("pong_beep.wav", channel=0)

                # Bounce off bottom.
                ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
                if self.by > ball_bot:
                    self.by = ball_bot - (self.by - ball_bot)
                    self.bdy = -self.bdy
                    renpy.sound.play("pong_beep.wav", channel=0)

                # This draws a paddle, and checks for bounces.
                def paddle(px, py, hotside):

                    # Render the paddle image. We give it an 800x600 area
                    # to render into, knowing that images will render smaller.
                    # (This isn't the case with all displayables. Solid, Frame,
                    # and Fixed will expand to fill the space allotted.)
                    # We also pass in st and at.
                    pi = renpy.render(self.paddle, 1920, 1080, st, at) #800/600

                    # renpy.render returns a Render object, which we can
                    # blit to the Render we're making.
                    r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                    if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                        hit = False

                        if oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                            self.bdx = -self.bdx
                            hit = True

                        elif oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                            self.bdx = -self.bdx
                            hit = True

                        if hit:
                            renpy.sound.play("pong_boop.wav", channel=1)
                            self.bspeed *= 1.10

                # Draw the two paddles.
                paddle(362, self.playery, 362 + self.PADDLE_WIDTH) #58 +10 //#88 = 58 + 30/ 344 + 54//
                paddle(1544, self.computery, 1544) #724 // 800- 58 - 10 //courtend is 742, distance is 18 = 32 //new courtend is 1576

                # Draw the ball.
                ball = renpy.render(self.ball, 1920, 1080, st, at) #800/600
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                              int(self.by - self.BALL_HEIGHT / 2)))

                # Show the player names.
                player = renpy.render(self.player, 1920, 1080, st, at) #800/600
                r.blit(player, (516, 45)) #20, 25 /480 + 20* 1.8

                # Show Eileen's name.
                eileen = renpy.render(self.eileen, 1920, 1080, st, at) #800/600
                ew, eh = eileen.get_size()
                r.blit(eileen, (1422 - ew, 45)) #790/25   1440-18 = 1422

                # Show the "Click to Begin" label.
                if self.stuck:
                    ctb = renpy.render(self.ctb, 1920, 1080, st, at) #800/600
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (960 - cw / 3.6, 54)) #400, 2, 30


                # Check for a winner.
                if self.bx < 0: #-200
                    self.winner = "eileen"

                    # Needed to ensure that event is called, noticing
                    # the winner.
                    renpy.timeout(0)

                elif self.bx > 1640: #1000
                    self.winner = "player"
                    renpy.timeout(0)

                # Ask that we be re-rendered ASAP, so we can show the next
                # frame.
                renpy.redraw(self, 0)

                # Return the Render object.
                return r

            # Handles events.
            def event(self, ev, x, y, st):

                import pygame

                # Mousebutton down == start the game by setting stuck to
                # false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

                # Set the position of the player's paddle.
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                self.playery = y

                # If we have a winner, return him or her. Otherwise, ignore
                # the current event.
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()


###game end

default can_cont = True #The variable that will determine if we can dismiss or not
   
init -1 python:
    def dis_block(): #This is the funciton that returns our variable
        global can_cont
        return can_cont
    config.say_allow_dismiss = dis_block #This tells the computer to check our function to see if dismissing is allowed.

#newscriptbelow

screen nodismiss(): #Our screen, while it is visible, no one can dismiss anything at all
    key "dismiss" action NullAction()

#special script:

screen tsetup:
   
    timer 0.1 action Preference("auto-forward", "enable") repeat False

#    key "K_RETURN" action NullAction()
#    key "K_KP_ENTER" action NullAction()
#    key "K_SPACE" action NullAction()
#   
#    key "mousedown_4" action NullAction()
#    key "K_PAGEUP" action NullAction()
#    key "mousedown_5" action NullAction()
#    key "K_PAGEDOWN" action NullAction()
#   
#    key "mouseup_3" action NullAction()
#    key "mouseup_1" action NullAction()
#
#    key "K_ESCAPE" action NullAction
#   
#    key "mouseup_3" action NullAction()
#    key "mouseup_1" action NullAction()
#    key "joy_dismiss" action NullAction()   
   
screen returnset:
    timer 0.1 action Preference("auto-forward", "disable") repeat False
   
define nnvl = Character(None, kind=nvl)



#ending screen

screen disable_leftclick():
    key "mousedown_1" action With(None)

#countdown script

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:

    timer time repeat False action [Hide('countdown'), Jump(timer_jump)]
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    #bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

#another screen
screen my_keys():
    #Dismiss keys
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()    

#stop script here

init python:
    import pygame
   
    def kill_all_ui():
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.USEREVENT)
       
    def restore_ui():
        pygame.event.set_blocked(None)
           
#label start:
    #$ kill_all_ui()
    # ANY ANIMATIONS OR TRANSITIONS GO HERE.
    #$ restore_ui()

#particle burst script starts here

transform particle(d, delay, speed=1.0, around=(config.screen_width/2, config.screen_height/2), angle=0, radius=200):
    d
    pause delay
    subpixel True
    around around
    radius 0
    linear speed radius radius angle angle

init python:
    class ParticleBurst(renpy.Displayable):
        def __init__(self, displayable, interval=(0.02, 0.04), speed=(0.15, 0.3), around=(config.screen_width/2, config.screen_height/2), angle=(0, 360), radius=(50, 75), particles=None, mouse_sparkle_mode=False, **kwargs):
            """Creates a burst of displayable...
           
            @params:
            - displayable: Anything that can be shown in Ren'Py (expects a single displayable or a container of displayable to randomly draw from).
            - interval: Time between bursts in seconds (expects a tuple with two floats to get randoms between them).
            - speed: Speed of the particle (same rule as above).
            - angle: Area delimiter (expects a tuple with two integers to get randoms between them) with full circle burst by default. (0, 180) for example will limit the burst only upwards creating sort of a fountain.
            - radius: Distance delimiter (same rule as above).
            - around: Position of the displayable (expects a tuple with x/y integers). Burst will be focused around this position.
            - particles: Amount of particle to go through, endless by default.
            - mouse_sparkle_mode: Focuses the burst around a mouse poiner overriding "around" property.
           
            This is far better customizable than the original ParticleBurst and is much easier to expand further if an required..
            """
            super(ParticleBurst, self).__init__(**kwargs)
            self.d = [renpy.easy.displayable(d) for d in displayable] if isinstance(displayable, (set, list, tuple)) else [renpy.easy.displayable(displayable)]
            self.interval = interval
            self.speed = speed
            self.around = around
            self.angle = angle
            self.radius = radius
            self.particles = particles
            self.msm = mouse_sparkle_mode
       
        def render(self, width, height, st, at):
               
            rp = store.renpy
               
            if not st:
                self.next = 0
                self.particle = 0
                self.shown = {}
               
            render = rp.Render(width, height)
           
            if not (self.particles and self.particle >= self.particles) and self.next <= st:
                speed = rp.random.uniform(self.speed[0], self.speed[1])
                angle = rp.random.randrange(self.angle[0], self.angle[1])
                radius = rp.random.randrange(self.radius[0], self.radius[1])
                if not self.msm:
                    self.shown[st + speed] = particle(rp.random.choice(self.d), st, speed, self.around, angle, radius)
                else:
                    self.shown[st + speed] = particle(rp.random.choice(self.d), st, speed, rp.get_mouse_pos(), angle, radius)
                self.next = st + rp.random.uniform(self.interval[0], self.interval[1])
                if self.particles:
                    self.particle = self.particle + 1
           
            for d in self.shown.keys():
                if d < st:
                    del(self.shown[d])
                else:
                    d = self.shown[d]
                    render.blit(d.render(width, height, st, at), (d.xpos, d.ypos))
                   
            rp.redraw(self, 0)
           
            return render

        def visit(self):
            return self.d

image boom = ParticleBurst([Solid("#%06x"%renpy.random.randint(0, 0xFFFFFF), xysize=(5, 5)) for i in xrange(50)], mouse_sparkle_mode=True)

#multipersistentscript here:

init python:
    mp = MultiPersistent("awsw")

#blurscript start here:
init:
    
    $ navmenuopen = False
    
    
    if persistent.c1blood:
        $ achievement.grant("Blood Donation")
                    
    if persistent.c1fish:
        $ achievement.grant("Bravery")

    if persistent.c1books:
        $ achievement.grant("Bookworm")

    if persistent.c1meds:
        $ achievement.grant("Prescription")
                    
    if persistent.c1liquid:
        $ achievement.grant("Daredevil")
                    
    if persistent.c1eggs:
        $ achievement.grant("Ovicide")
                    
    if persistent.c1fruits:
        $ achievement.grant("Fruitarian")

    if persistent.c1decline:
        $ achievement.grant("Nuisance")
                    
    if persistent.c1invhigh:
        $ achievement.grant("Investigator 1")
                        
    if persistent.c1booksort:
        $ achievement.grant("Librarian")
                    
    if persistent.c1boredom:
        $ achievement.grant("Patient")
                    
    if persistent.c1annaanswers:
        $ achievement.grant("General Knowledgist")
        
    if persistent.c1teetotaler:
        $ achievement.grant("Teetotaler")
        
    if persistent.c1disrobement:
        $ achievement.grant("Disrobement")

    if persistent.c1bastion:
        $ achievement.grant("You are a winner!")
        
    if persistent.c2interrogator:
        $ achievement.grant("Interrogator 1")

    if persistent.c2bandage:
        $ achievement.grant("Finders, Keepers")

    if persistent.dirttaken:
        $ achievement.grant("Archeologist")

    if persistent.c2landscape:
        $ achievement.grant("Landscaper")

    if persistent.orb_taken:
        $ achievement.grant("Orb Finder")
        
    if persistent.c2storeaisles:
        $ achievement.grant("Window Shopper")

    if persistent.c2investigation:
        $ achievement.grant("Investigator 2")
        
    if persistent.c2pictures:
        $ achievement.grant("Memories")

    if persistent.heardaboutcancerenvelope:
        $ achievement.grant("Snoop")

    if persistent.c2legs:
        $ achievement.grant("Leg Stretcher")

    if persistent.c2eau:
        $ achievement.grant("Eau de Dragon")
        
    if persistent.c2magazine:
        $ achievement.grant("Research Material")

    if persistent.c2music:
        $ achievement.grant("Audiophile")

    if persistent.playedemera:
        $ achievement.grant("The Politician")
        
    if persistent.havemapfirst:
        $ achievement.grant("Cartographer")
        
    if persistent.base_taken:
        $ achievement.grant("Base Finder")

    if persistent.c3prank:
        $ achievement.grant("Prankster")
        
    if persistent.c3helpedkatsu:
        $ achievement.grant("Altruist")
        
    if persistent.c3interrogator:
        $ achievement.grant("Interrogator 2")
        
    if persistent.varasaved:
        $ achievement.grant("Stalker")
        
    if persistent.c3reckless:
        $ achievement.grant("Reckless")

    if persistent.c3investigator:
        $ achievement.grant("Investigator 3")

    if persistent.c3flawless:
        $ achievement.grant("Flawless Run")

    if persistent.seashells:
        $ achievement.grant("Souvenir")
        
    if persistent.playedkatsu:
        $ achievement.grant("The Artisan")
        
    if persistent.c4eggs:
        $ achievement.grant("In Loco Parentis")
        
    if persistent.ixomenassembled:
        $ achievement.grant("Sphere Builder")
        
    if persistent.playedkevin:
        $ achievement.grant("The Student")
        
    if persistent.lazy:
        $ achievement.grant("Lazy")
        
    if persistent.skip:
        $ achievement.grant("Fast Forward")
        
    if persistent.popular:
        $ achievement.grant("Popular")
        
    if persistent.c3pointless:
        $ achievement.grant("Utterly Pointless Achievement")
        
    if persistent.izumimask:
        $ achievement.grant("Unmasking")
        
    if persistent.firstending:
        $ achievement.grant("It begins")

    if persistent.neutralending:
        $ achievement.grant("Detonation")

    if persistent.remybadending:
        $ achievement.grant("Alone")

    if persistent.remygoodending:
        $ achievement.grant("Casualties of War")

    if persistent.annabadending:
        $ achievement.grant("Sacrifice")

    if persistent.annagoodending:
        $ achievement.grant("Tragic Hero")

    if persistent.lorembadending:
        $ achievement.grant("Remember")

    if persistent.loremgoodending:
        $ achievement.grant("The Plan")

    if persistent.brycebadending:
        $ achievement.grant("Catastrophy")

    if persistent.brycegoodending:
        $ achievement.grant("Murderer")

    if persistent.adinebadending:
        $ achievement.grant("Getaway")

    if persistent.adinegoodending:
        $ achievement.grant("Decisions")

    if persistent.evilending:
        $ achievement.grant("Betrayal")

    if persistent.optimist:
        $ achievement.grant("Optimist")

    if persistent.trueending:
        $ achievement.grant("Hope")
        
    $ achievement.sync()

    
    
    image movie = Movie(size=(640, 360), xalign=0.5, yalign=0.5)
    image movie2 = Movie(size=(640, 360), xalign=0.5, yalign=0.5)
    image movie3 = Movie(size = (1920, 1080), channel="intromovie", play="intro.ogv")

    transform transpa:

        alpha 0.5

    python hide:

        def gen_randmotion(count, dist, delay):

            import random

            args = [ ]

            for i in range(0, count):
                args.append(anim.State(i, None,
                                       Position(xpos=random.randrange(-dist, dist),
                                                ypos=random.randrange(-dist, dist),
                                                xanchor='left',
                                                yanchor='top',
                                                )))

            for i in range(0, count):
                for j in range(0, count):

                    if i == j:
                        continue

                    args.append(anim.Edge(i, delay, j, MoveTransition(delay)))

            return anim.SMAnimation(0, *args)

        store.randmotion = gen_randmotion(5, 5, 1.0)


init python:

    def double_vision_on(picture):

        renpy.scene()

        renpy.show(picture)

        renpy.show(picture, at_list=[transpa,randmotion], tag="blur_image")

        renpy.with_statement(dissolve)


    def double_vision_off():

        renpy.hide("blur_image")

        renpy.with_statement(dissolve)

# blurscript end here

init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

    import math

    class Shaker(object):
        
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
                    
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            
            return (int(nx), int(ny), 0, 0)
        
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
        
        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

    Shake = renpy.curry(_Shake)
#

#

screen my_scr:
    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")
    key "K_SPACE" action Hide("nonexistent_screen")
   
    key "mousedown_4" action Hide("nonexistent_screen")
    key "K_PAGEUP" action Hide("nonexistent_screen")
    key "mousedown_5" action Hide("nonexistent_screen")
    key "K_PAGEDOWN" action Hide("nonexistent_screen")
   
    key "mouseup_3" action Hide("nonexistent_screen")
    key "mouseup_1" action Hide("nonexistent_screen")

    key "K_ESCAPE" action Return("smth")
    
screen leftclick:
    key "mouseup_3" action [ShowMenu(), ToggleVariable("navmenuopen", False)]

#another screen

label start:
    
    $ cardduty = False
    $ cardenlightenment = False
    $ cardconflict = False
    $ cardgrief = False
    $ cardhope = False
    $ cardinception = False
    $ cardleadership = False
    $ cardlorem = False
    $ cardloss = False
    $ cardpassion = False
    $ cardpride = False
    $ cardsuperstition = False
    $ cardtrauma = False

    $ remydead = False
    $ annadead = False
    $ adinedead = False
    $ brycedead = False
    $ loremdead = False

    $ remystatus = "none"
    $ annastatus = "none"
    $ adinestatus = "none"
    $ brycestatus = "none"
    $ loremstatus = "none"

    $ remyscenesfinished = 0
    $ annascenesfinished = 0
    $ loremscenesfinished = 0
    $ brycescenesfinished = 0
    $ adinescenesfinished = 0

    
    $ _game_menu_screen = "navigation"
    show screen leftclick
    jump nameentry





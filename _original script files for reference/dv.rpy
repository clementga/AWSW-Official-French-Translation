label debugger_screen:

    python hide:

            ui.window(style=style.gm_root)
            ui.null()

            ui.frame(ymargin=10, xmargin=10, style=style.menu_frame)
            ui.side(['t', 'c', 'r', 'b'])

            layout.label(_("Variable Viewer"), None)

            entries = [ ]

            ebc = store.__dict__.ever_been_changed
            ebc = list(ebc)
            ebc.sort()

            ebc.remove("nvl_list")

            import repr
            aRepr = repr.Repr()
            aRepr.maxstring = 40

            for var in ebc:
                if not hasattr(store, var):
                    continue

                if var.startswith("__00"):
                    continue

                if var.startswith("_") and not var.startswith("__"):
                    continue

                val = aRepr.repr(getattr(store, var))
                s = (var + " = " + val)
                s = s.replace("{", "{{")
                s = s.replace("[", "[[")
                entries.append((0, s))

            if entries:
                vp = ui.viewport(mousewheel=True)
                layout.list(entries)
                ui.bar(adjustment=vp.yadjustment, style='vscrollbar')
            else:
                layout.prompt(_("No variables have changed since the game started."), None)
                ui.null()

            layout.button(_(u"Return to the developer menu"), None, clicked=ui.returns(True))

            ui.close()

            ui.interact()

    return
    
label image_location_picker:

    scene black

    python hide:

        image_files = [
            fn
            for dir, fn in renpy.loader.listdirfiles()
            if fn.lower().endswith(".jpg") or fn.lower().endswith(".png")
            if not fn[0] == "_"
            ]

        image_files.sort()

        xadjustment = ui.adjustment()
        yadjustment = ui.adjustment()

        while True:

            ui.frame()
            ui.vbox()

            layout.label(_(u"Image Location Picker"), None)

            ui.textbutton(_(u"Done"), clicked=ui.returns(False), size_group="files")

            ui.side(['c', 'b', 'r'], spacing=5)
            vp = ui.viewport(xadjustment=xadjustment, yadjustment=yadjustment, mousewheel=True)

            ui.vbox()

            for fn in image_files:
                ui.button(clicked=ui.returns(fn), size_group="files", xminimum=1.0)
                ui.text(fn.replace("{", "{{").replace("[", "[["), style="button_text", xalign=0.0)

            ui.close()

            ui.bar(adjustment=xadjustment, style='scrollbar')
            ui.bar(adjustment=yadjustment, style='vscrollbar')
            ui.close()

            ui.close()

            rv = ui.interact()

            if rv is False:
                renpy.jump("image_location_picker_done")

            # Now, allow the user to pick the image.

            ui.keymap(game_menu=ui.returns(True))
            ui.add(__ImageLocationPicker(rv))
            ui.interact()

        renpy.jump("image_location_picker")

label image_location_picker_done:
    return
    
label filename_list:

    python hide:
        import os
        f = file("files.txt", "w")

        for dirname, dirs, files in os.walk(config.gamedir):

            dirs.sort()
            files.sort()

            for fn in files:
                fn = os.path.join(dirname, fn)
                fn = fn[len(config.gamedir) + 1:]
                print >>f, fn.encode("utf-8", "replace")
                print fn.encode("utf-8", "replace")

        f.close()

        renpy.launch_editor(["files.txt"], transient=1)

    return
    
    
style _hyperlink_button is _default
style _hyperlink_button_text is _hyperlink

screen _inspector:
    zorder 1010
    modal True

    frame:
        style_group ""

        xmaximum 770
        xfill True

        xpadding 15
        ypadding 15

        xalign 0.5
        yalign 0.25


        has vbox

        label _("Displayable Inspector")

        null height 10

        if not tree:

            text _("Nothing to inspect.")

        else:

            viewport:
                scrollbars "both"
                child_size (1200, 0)
                yfill False
                xfill False
                mousewheel True

                has vbox

                hbox:
                    text " ":
                        min_width 350
                        xmaximum 350

                    text _("Size"):
                        min_width 85
                        underline True

                    text _("Style"):
                        min_width 125
                        underline True

                    null width 5

                    text _("Location"):
                        underline True
                        min_width 100

                null height 5

                for depth, width, height, d in tree:

                    $ t = "  " * depth + u"\u2022 " + unicode(d)
                    $ s = __format_style(d.style.parent)


                    hbox:

                        text "[t!q]":
                            min_width 350

                        text "[width:.0f]x[height:.0f]":
                            min_width 85

                        textbutton "[s!q]":
                            style "_hyperlink_button"
                            text_min_width 125
                            action Show("_style_inspector", d=d)

                        null width 5

                        if d._location:
                            $ l = __format_location(d._location)

                            textbutton "[l!q]":
                                style "_hyperlink_button"
                                text_min_width 100
                                action _EditFile(d._location[0], d._location[1])


                null height 5

        null height 20

        textbutton _("Return") action Return(True)
        key "game_menu" action Return(True)

screen _style_inspector:
    zorder 1020
    modal True

    frame:
        style_group ""

        xmaximum 700
        xfill True

        xpadding 15
        ypadding 15

        xalign 0.5
        yalign 0.25

        has vbox

        $ displayable_name = unicode(d)
        label _("Inspecting Styles of [displayable_name!q]")

        null height 10

        viewport:
            yfill False
            xfill False
            mousewheel True

            vbox:
                for name, properties in d.style.inspect():

                    if name is None:
                        text _("displayable:")
                    else:
                        $ style_name = __format_style(name)
                        text "style [style_name!q]:"


                    if not properties:
                        text _("        (no properties affect the displayable)")
                    elif name in [ ("default",), ("_default",) ]:
                        text _("        (default properties omitted)")
                    else:
                        for propname in sorted(properties):
                            $ value = __safe_repr(properties[propname])
                            text "        [propname] [value!q]"

                    null height 5


        # Code goes here.

        null height 20

        textbutton _("Return") action Hide("_style_inspector")
        key "game_menu" action Hide("_style_inspector")


init python:

    def __format_style(name):
        return name[0] + "".join([ "[%r]" % i for i in name[1:] ])

    def __format_location(l):
        if l is None:
            return ""
        else:
            fn = l[0]
            if fn.startswith("game/"):
                fn = fn[5:]
            elif fn.startswith("renpy/common"):
                fn = fn[6:]

            return "%s:%d" % (fn, l[1])

    def __safe_repr(name):
        try:
            s = unicode(repr(name))
            if len(s) > 51:
                s = s[:50] + u"\u2026"

            return s
        except:
            return _("<repr() failed>")

    def __inspect(tree):
        renpy.context_dynamic("_window")
        store._window = False

        renpy.exports.show_screen("_inspector", transient=True, tree=tree)
        renpy.ui.interact(mouse="screen", type="screen", suppress_overlay=True, suppress_underlay=True)

    config.inspector = __inspect


#below is a clear dump of developer

style list is default
style list_box is vbox
style list_row is default
style list_row_box is hbox
style list_spacer is default
style list_text is default

style list_row:
    xfill True
    ymargin 0
    background "#eee"
    hover_background "#fff"
    selected_background "#cce"

init python:
    style.list_row[1].background = "#ddd"
    style.list_row[1].hover_background = "#fff"
    style.list_row[1].selected_background = "#cce"

style list_text:
    color "#000"
    size 14

style list_spacer:
    xminimum 15

screen developer:

    zorder 1001
    modal True

    frame:
        style_group "developer"

        align (.025, .05)

        has vbox

        label _(u"Developer Menu")

        textbutton _("Reload Game (Shift+R)"):
            action ui.callsinnewcontext("_save_reload_game")
        textbutton _("Console (Shift+O)"):
            action [ Hide("developer"), _console.enter ]
        textbutton _("Variable Viewer"):
            action ui.callsinnewcontext("debugger_screen")
        textbutton _("Theme Test"):
            action ui.callsinnewcontext("theme_test")
        textbutton _("Image Location Picker"):
            action ui.callsinnewcontext("image_location_picker")
        textbutton _("Filename List"):
            action ui.callsinnewcontext("filename_list")

        if not renpy.get_screen("image_load_log"):
            textbutton _("Show Image Load Log"):
                action Show("image_load_log")
        else:
            textbutton _("Hide Image Load Log"):
                action Hide("image_load_log")

        null height 15

        textbutton _(u"Return"):
            action Hide("developer")
            size_group "developer"

style _developer_default is _default
style _developer_frame is _frame
style _developer_vbox is _vbox

style _developer_button is _button:
    size_group "developer"

style _developer_button_text is _button_text
style _developer_label is _label
style _developer_label_text is _label_text


#label debugger_screen:

#    python hide:

#        ui.window(style=style.gm_root)
#        ui.null()
#
 #       ui.frame(ymargin=10, xmargin=10, style=style.menu_frame)
  #      ui.side(['t', 'c', 'r', 'b'])
#
 #       layout.label(_("Variable Viewer"), None)
#
 #       entries = [ ]
#
 #       ebc = store.__dict__.ever_been_changed
  #      ebc = list(ebc)
   #     ebc.sort()
#
 #       ebc.remove("nvl_list")
#
 #       import repr
  #      aRepr = repr.Repr()
   #     aRepr.maxstring = 40
#
 #       for var in ebc:
  #          if not hasattr(store, var):
   #             continue
#
 #           if var.startswith("__00"):
  #              continue
#
 #           if var.startswith("_") and not var.startswith("__"):
  #              continue
#
 #           val = aRepr.repr(getattr(store, var))
  #          s = (var + " = " + val)
   #         s = s.replace("{", "{{")
    #        s = s.replace("[", "[[")
     #       entries.append((0, s))
#
 #       if entries:
  #          vp = ui.viewport(mousewheel=True)
   #         layout.list(entries)
    #        ui.bar(adjustment=vp.yadjustment, style='vscrollbar')
     #   else:
      #      layout.prompt(_("No variables have changed since the game started."), None)
       #     ui.null()
#
 #       layout.button(_(u"Return to the developer menu"), None, clicked=ui.returns(True))
#
 #       ui.close()
#
 #       ui.interact()
#
 #   return

label theme_test:

    python hide:

        # Never gets pickled
        def role(b):
            if b:
                return "selected_"
            else:
                return ""

        toggle_var = True
        adj = ui.adjustment(100, 25, page=25, adjustable=True)

        while True:

            ui.window(style=style.gm_root)
            ui.null()

            # Buttons
            ui.hbox(box_spacing=10, xpos=10, ypos=10)

            ui.vbox(box_spacing=10)

            sg = "theme_test"

            ui.frame(style='menu_frame')
            ui.vbox()
            layout.label("Button", None)
            ui.textbutton("Button", size_group=sg, clicked=ui.returns("gndn"))
            ui.textbutton("Button (Selected)", size_group=sg, clicked=ui.returns("gndn"), role=role(True))
            ui.textbutton("Small", clicked=ui.returns("gndn"), style='small_button')
            ui.close()

            ui.frame(style='menu_frame')
            ui.vbox()
            layout.label("Radio Button", None)
            ui.textbutton("True", size_group=sg, clicked=ui.returns("set"), role=role(toggle_var), style='radio_button')
            ui.textbutton("False", size_group=sg, clicked=ui.returns("unset"), role=role(not toggle_var), style='radio_button')
            ui.close()

            ui.frame(style='menu_frame')
            ui.vbox()
            layout.label("Check Button", None)
            ui.textbutton("Check Button", size_group=sg, clicked=ui.returns("toggle"), role=role(toggle_var), style='check_button')
            ui.close()

            ui.frame(style='menu_frame')
            ui.vbox(box_spacing=2)
            ui.bar(adjustment=adj, style='bar', xmaximum=200)
            ui.bar(adjustment=adj, style='slider', xmaximum=200)
            ui.bar(adjustment=adj, style='scrollbar', xmaximum=200)
            ui.close()

            ui.close() # vbox

            ui.frame(style='menu_frame')
            ui.hbox(box_spacing=2)
            ui.bar(adjustment=adj, style='vbar', ymaximum=200)
            ui.bar(adjustment=adj, style='vslider', ymaximum=200)
            ui.bar(adjustment=adj, style='vscrollbar', ymaximum=200)
            ui.close()

            ui.frame(style='menu_frame', xmaximum=0.95)
            ui.vbox(box_spacing=20)
            layout.prompt("This is a prompt. We've made this text long enough to wrap around so it fills multiple lines.", None)
            ui.close()

            ui.close() # hbox

            ui.frame(style='menu_frame', xalign=.01, yalign=.99)
            ui.textbutton(_("Return to the developer menu"), clicked=ui.returns("return"))

            rv = ui.interact()
            if rv == "return":
                break

            elif rv == "set":
                toggle_var = True
            elif rv == "unset":
                toggle_var = False
            elif rv == "toggle":
                toggle_var = not toggle_var

    return


# Not used any more, but may be in save files.
init -1050 python:
    config.missing_background = "black"


# Not used any more, but may be in save files.
screen missing_images:
    pass

init 1050 python:

    if config.developer:

        def _missing_show_callback(name, what, layer):
            if layer != 'master':
                return False

            if not renpy.count_displayables_in_layer(layer):
                return Placeholder("bg").parameterize((), what)
            else:
                return Placeholder().parameterize((), what)

        def _missing_hide_callback(name, layer):
            if layer != 'master':
                return False

            return True

        def _missing_scene_callback(layer):
            if layer != 'master':
                return False

            return True

        config.missing_scene = _missing_scene_callback
        config.missing_show = _missing_show_callback
        config.missing_hide = _missing_hide_callback


init -1050 python:

    class _FPSMeter(object):

        def _init__(self):
            self.last_frames = None
            self.last_time = None

        def _call__(self, st, at):

            if self.last_time is not None:
                frames = config.frames - self.last_frames
                time = st - self.last_time

                text = "FPS: %.1f" % (frames / time)

            else:
                text = "FPS: --.-"

            self.last_frames = config.frames
            self.last_time = st

            return Text(text, xalign=1.0), .5

label fps_meter:

    python hide:
        def fps_overlay():
            ui.add(DynamicDisplayable(_FPSMeter()))

        # We normally don't want to change this at runtime... but here
        # it's okay, because we don't want to save the FPS meter anyway.
        #
        # Do as I say, not as I do.
        config.overlay_functions.append(fps_overlay)

    return


init python:

    # This is a displayable that can keep track of the mouse coordinates,
    # and show them to the user.
    class __ImageLocationPicker(renpy.Displayable):

        def __init__(self, fn, **kwargs):
            super(__ImageLocationPicker, self).__init__(**kwargs)

            self.child = Image(fn)

            self.mouse = None
            self.point1 = None
            self.point2 = None

            self.size = (0, 0)

            self.clipboard = None

        def rectangle(self):
            x1, y1 = self.point1
            x2, y2 = self.point2

            width = self.size[0]
            height = self.size[1]

            x1 = min(x1, width)
            x2 = min(x2, width)
            y1 = min(y1, height)
            y2 = min(y2, height)

            minx = min(x1, x2)
            miny = min(y1, y2)
            maxx = max(x1, x2)
            maxy = max(y1, y2)

            w = maxx - minx
            h = maxy - miny

            return (minx, miny, w, h)

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            cr = renpy.render(self.child, width, height, st, at)
            rv.blit(cr, (0, 0))

            text = [ ]

            self.size = (cr.width, cr.height)

            if self.point1 and self.point2 and not self.point1 == self.point2:
                x, y, w, h = self.rectangle()

                if w and h:

                    sr = renpy.render(Solid("#0ff4"), w, h, st, at)
                    rv.blit(sr, (x, y))

                    # text.append("Imagemap rectangle: %r" % ((minx, miny, maxx, maxy),))
                    text.append(__("Rectangle: %r") % ((x, y, w, h),))

            if self.mouse:
                mx, my = self.mouse
                if mx < cr.width and my < cr.height:
                    text.append(__("Mouse position: %r") % (self.mouse,))

            if self.clipboard:
                text.append(self.clipboard)

            text.append(__("ESC to quit."))

            td = Text("\n".join(text), size=14, color="#fff", outlines=[ (1, "#000", 0, 0 ) ])
            tr = renpy.render(td, width, height, st, at)

            rv.blit(tr, (0, height - tr.height))

            return rv

        def event(self, ev, x, y, st):
            import pygame_sdl2 as pygame

            self.mouse = (x, y)
            renpy.redraw(self, 0)

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.point1 = (x, y)
                self.point2 = (x, y)

            elif ev.type == pygame.MOUSEMOTION and ev.buttons[0]:
                self.point2 = (x, y)

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.point2 = (x, y)

                x, y, w, h = self.rectangle()

                if w or h:
                    text = repr((x, y, w, h))
                    self.clipboard = __("Rectangle copied to clipboard.")
                else:
                    text = repr((x, y))
                    self.clipboard = __("Position copied to clipboard.")

                import pygame.scrap
                pygame.scrap.put(pygame.scrap.SCRAP_TEXT, text)



init python:
    def image_load_log_function(st, at):

        ill = list(renpy.get_image_load_log(3))

        vbox = VBox()

        for when, filename, preload in ill:
            if preload:
                color="#ffffff"
            else:
                color="#ffcccc"

            vbox.add(Text(filename.replace("{", "{{").replace("[", "[["), size=12, color=color, style="_default"))

        rv = Window(vbox, style="_frame", background="#0004", xpadding=5, ypadding=5, xminimum=200)
        return rv, .25

screen image_load_log:
    zorder 1000

    add DynamicDisplayable(image_load_log_function)



init python:
    if config.transparent_tile:
        config.underlay.append(im.Tile("_transparent_tile.png"))

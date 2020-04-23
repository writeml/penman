import sublime
import sublime_plugin

# REGION - ON PLUGIN LOADED

# TODO: replace with `on_init` event after build 4050
# See: https://github.com/sublimehq/sublime_text/issues/5

def plugin_loaded():
    for window in sublime.windows():
        for view in window.views():
            toggleSyntax(view)
        # end for
    # end for
# end def

# REGION - EVENT LISTENERS

class AutoSwitchSyntax(sublime_plugin.EventListener):
    def on_load_async(self, view):
        toggleSyntax(view)
    # end def

    def on_post_save_async(self, view):
        toggleSyntax(view)
    # end def
# end class

# REGION - HELPER METHODS

def toggleSyntax(view):
    if not view.match_selector(0, "text.plain"):
        return
    # end if

    regex = r"['\"]?writeml['\"]?\s*=\s*true"
    hasMarker = (not view.find(regex, 0, sublime.IGNORECASE).empty())

    if hasMarker:
        view.set_syntax_file("Packages/Penman/WriteML.sublime-syntax")
    # end if
# end def
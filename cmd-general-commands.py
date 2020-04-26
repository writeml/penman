import sublime
import sublime_plugin

# REGION - TOGGLE SYNTAX

syntax_map = {
    "text.writeml"        : "Packages/Penman/WriteML.sublime-syntax",
    "source.writeml-toml" : "Packages/Penman/WriteML TOML.sublime-syntax",
}

class PenmanToggleSyntaxCommand(sublime_plugin.TextCommand):
    def run(self, edit, syntax):
        # do nothing if requested syntax not supported...
        if (syntax not in syntax_map):
            print("Penman: Requested syntax '" + syntax + "' not recognized.")
            return;
        # end if

        # ...else, toggle syntax
        view = self.view
        view_settings = view.settings()
        cache_key = "penman-cached-syntax"

        if view_settings.has(cache_key) and view.match_selector(0, syntax):
            # syntax already set -- toggle back
            view.set_syntax_file(view_settings.get(cache_key))
        else:
            # cache current syntax and switch
            view_settings.set(cache_key, view_settings.get("syntax"))
            view.set_syntax_file(syntax_map[syntax])
        # end if
    # end def
# end class
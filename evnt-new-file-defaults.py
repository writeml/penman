import sublime
import sublime_plugin

# REGION - NEW FILE DEFAULT SETTINGS

class NewFileDefaultsEventListener(sublime_plugin.EventListener):
    def on_activated_async(self, view):
        # do nothing if this is an existing file
        if view.file_name() is not None:
            return;
        # end if

        penman_settings = sublime.load_settings("Penman.sublime-settings")
        default_dir = penman_settings.get("default_directory")
        default_ext = penman_settings.get("default_plain_text_extension")

        view_settings = view.settings()

        if default_dir != "":
            view_settings.set("default_dir", default_dir)
        # end if

        if default_ext != "" and view.match_selector(0, "text.plain"):
            view_settings.set("default_extension", default_ext)
        # end if
    # end def
# end class
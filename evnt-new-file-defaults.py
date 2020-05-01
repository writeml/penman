import sublime
import sublime_plugin

# REGION - NEW FILE DEFAULT SETTINGS

class NewFileDefaultsEventListener(sublime_plugin.EventListener):
    def on_activated_async(self, view):
        SetNewFileDefaults(view)
    # end def

    def on_post_text_command(self, view, command_name, args):
        SetNewFileDefaults(view)
    # end def
# end class

def SetNewFileDefaults(view):
    # do nothing if this file already has a location on disk
    if FileOnDisk(view):
        return;
    # end if

    # get all necessary settings
    view_settings = view.settings()

    penman_settings = sublime.load_settings("Penman.sublime-settings")
    default_dir = penman_settings.get("default_directory")
    default_ext = penman_settings.get("default_plain_text_extension")

    # set/unset the default directory (as needed)
    if default_dir != "":
        if AnyFilesOnDisk(view):
            view_settings.erase("default_dir")
        else:
            view_settings.set("default_dir", default_dir)
        # end if
    # end if

    # set/unset the default plain-text file extension (as needed)
    if default_ext != "":
        if view.match_selector(0, "text.plain"):
            view_settings.set("default_extension", default_ext)
        else:
            view_settings.erase("default_extension")
    # end if
# end def

def FileOnDisk(view):
    return view.file_name() is not None
# end def

def AnyFilesOnDisk(view):
    return view.window() is not None and any(
        FileOnDisk
        for win_view in view.window().views()
    )
# end def
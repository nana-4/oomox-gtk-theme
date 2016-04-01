from gi.repository import Gtk
from .helpers import get_presets


class ThemePresetsList(Gtk.ScrolledWindow):

    def on_preset_select(self, widget):
        list_index = widget.get_cursor()[0].to_string()
        self.current_theme = list(
            self.liststore[list_index]
        )[0]
        self.preset_select_callback(self.current_theme)

    def __init__(self, preset_select_callback):
        super().__init__()
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        self.preset_select_callback = preset_select_callback
        self.presets = get_presets()

        self.liststore = Gtk.ListStore(str)
        for preset_name in self.presets:
            self.liststore.append((preset_name, ))

        treeview = Gtk.TreeView(model=self.liststore, headers_visible=False)
        treeview.connect("cursor_changed", self.on_preset_select)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn(cell_renderer=renderer_text, text=0)
        treeview.append_column(column_text)

        self.add(treeview)

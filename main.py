import dearpygui.dearpygui as dpg
from webbrowser import open_new_tab
from os import _exit
from nodes import Nodes

class MainApp:
    def __init__(self):
        self.add_shortcut = dpg.mvKey_Spacebar
        self.add_menu_exists = False
        self.settings_menu_exists = False
        self.nodes = Nodes()
        self.node_library = {"Basic": ["Add", "Multiply", "Screen", "ConvertToGrayscale", "MapColor", "ChannelSplit", "ChannelJoin"], 
                            "Noise": ["Perlin", "Simplex", "Voronoi", "Worley"], 
                            "Filter": ["Blur", "Sharpen", "EdgeDetection", "Emboss", "GaussianBlur"], 
                            "Transform": ["Rotate", "Scale", "Translate", "Flip", "Mirror"], 
                            "Random": ["Seed", "Range"],
                            "Input": ["Texture", "Color"], 
                            "Output": ["Preview", "Export"]}
        dpg.create_context()
        
        with dpg.font_registry():
            default_font = dpg.add_font("Roboto-Regular.ttf", 16)
        
        dpg.create_viewport(title='NodeMage', width=1280, height=720)
        
        with dpg.window(tag="main_window", no_title_bar=True, no_move=True, no_resize=True, no_collapse=True, no_close=True):
            with dpg.menu_bar():
                with dpg.menu(label="File"):
                    dpg.add_menu_item(label="New")
                    dpg.add_menu_item(label="Save")
                    dpg.add_menu_item(label="Save As")
                    dpg.add_menu_item(label="Open")
                    dpg.add_menu_item(label="Exit", callback=self.exit)
                with dpg.menu(label="Edit"):
                    dpg.add_menu_item(label="Copy")
                    dpg.add_menu_item(label="Paste")
                    dpg.add_menu_item(label="Settings", callback=self.create_settings_menu)
                dpg.add_menu_item(label="Help", callback=self.help)
                dpg.add_menu_item(label="Add (Spacebar)", callback=self.create_add_menu)
            dpg.add_node_editor(tag="node_editor", callback=self.link_callback, delink_callback=self.delink_callback, minimap=True)
        dpg.bind_font(default_font)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("main_window", True)
        while dpg.is_dearpygui_running():
            self.update()
        dpg.destroy_context()

    def exit(self):
        _exit(0)

    # callback runs when user attempts to connect attributes
    def link_callback(self, sender, app_data):
        # app_data -> (link_id1, link_id2)
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)

    # callback runs when user attempts to disconnect attributes
    def delink_callback(self, sender, app_data):
        # app_data -> link_id
        dpg.delete_item(app_data)
    
    def add_menu_callback(self, sender, app_data, user_data):
        print(f"sender is: {sender}")
        print(f"app_data is: {app_data}")
        print(f"user_data is: {user_data}")
        self.nodes.add_node(user_data)

    def delete_add_menu(self):
        dpg.delete_item(item="add_menu_window")

    def create_add_menu(self, isOpenedFromMenu: bool = True):
        if not self.add_menu_exists:
            pos = (dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]+10) if isOpenedFromMenu else (dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1])
            with dpg.window(tag="add_menu_window", no_collapse=True, no_move=True, no_resize=True, no_title_bar=True, no_close=True, width=200, height=200, pos=pos):
                for i in self.node_library.keys():
                    with dpg.menu(label=i):
                        for j in self.node_library[i]:
                            mitem = dpg.add_menu_item(label=''.join(map(lambda x: x if x.islower() else " "+x, j)), callback=self.add_menu_callback, user_data=f'{str(i)}_{str(j)}'.lower())
                            dpg.set_item_callback(mitem, self.add_menu_callback)
                            with dpg.tooltip(mitem):
                                dpg.add_text(f'{str(i)}_{str(j)}'.lower())
            self.add_menu_exists = True

    def delete_settings_menu(self):
        dpg.delete_item(item="settings_menu_window")

    def create_settings_menu(self):
        if not self.settings_menu_exists:
            with dpg.window(label="Settings", tag="settings_menu_window", no_collapse=True, width=800, height=600, pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]-10)):
                dpg.add_text("Nothing here yet")
            self.settings_menu_exists = True

    def help(self):
        open_new_tab("https://github.com/Killereq-PL/NodeMage/wiki")

    def update(self):
        if self.add_menu_exists:
            if (not dpg.is_item_hovered("add_menu_window") and dpg.is_mouse_button_clicked(0)) or dpg.is_mouse_button_clicked(1) or dpg.is_key_pressed(dpg.mvKey_Escape):
                self.delete_add_menu()
                self.add_menu_exists = False
        if self.settings_menu_exists:
            if dpg.is_key_pressed(dpg.mvKey_Escape):
                self.delete_settings_menu()
                self.settings_menu_exists = False
        if dpg.is_key_pressed(self.add_shortcut):
            self.create_add_menu(False)
        if dpg.is_key_pressed(dpg.mvKey_F1):
            self.help()
        if dpg.is_key_pressed(dpg.mvKey_Delete):
            for item in dpg.get_selected_nodes("node_editor"):
                dpg.delete_item(item)
        dpg.render_dearpygui_frame()

if __name__ == "__main__":
    app = MainApp()
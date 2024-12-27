import dearpygui.dearpygui as dpg
import webbrowser

class MainApp:
    def __init__(self):
        self.add_shortcut = dpg.mvKey_Spacebar
        self.add_menu_exists = False
        self.settings_menu_exists = False
        dpg.create_context()
        dpg.create_viewport(title='Custom Title', width=1280, height=720)
        
        with dpg.window(tag="mainWindow", no_title_bar=True, no_move=True, no_resize=True, no_collapse=True, no_close=True):
            with dpg.menu_bar():
                with dpg.menu(label="File"):
                    dpg.add_menu_item(label="New")
                    dpg.add_menu_item(label="Save")
                    dpg.add_menu_item(label="Save As")
                    dpg.add_menu_item(label="Open")
                    dpg.add_menu_item(label="Exit")
                with dpg.menu(label="Edit"):
                    dpg.add_menu_item(label="Copy")
                    dpg.add_menu_item(label="Paste")
                    dpg.add_menu_item(label="Settings", callback=self.create_settings_menu)
                dpg.add_menu_item(label="Help", callback=self.help)
                dpg.add_menu_item(label="Add (Spacebar)", callback=self.create_add_menu)
            with dpg.node_editor(callback=self.link_callback, delink_callback=self.delink_callback):
                with dpg.node(label="Node 1"):
                    with dpg.node_attribute(label="Node A1"):
                        dpg.add_input_float(label="F1", width=150)

                    with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output):
                        dpg.add_input_float(label="F2", width=150)

                with dpg.node(label="Node 2"):
                    with dpg.node_attribute(label="Node A3"):
                        dpg.add_input_float(label="F3", width=200)

                    with dpg.node_attribute(label="Node A4", attribute_type=dpg.mvNode_Attr_Output):
                        dpg.add_input_float(label="F4", width=200)
        
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("mainWindow", True)
        while dpg.is_dearpygui_running():
            self.update()
        dpg.destroy_context()

    # callback runs when user attempts to connect attributes
    def link_callback(self, sender, app_data):
        # app_data -> (link_id1, link_id2)
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)

    # callback runs when user attempts to disconnect attributes
    def delink_callback(self, sender, app_data):
        # app_data -> link_id
        dpg.delete_item(app_data)
    
    def delete_add_menu(self):
        dpg.delete_item(item="add_menu_window")

    def create_add_menu(self):
        if not self.add_menu_exists:
            with dpg.window(tag="add_menu_window", no_collapse=True, no_move=True, no_resize=True, no_title_bar=True, no_close=True, width=200, height=200, pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]+10)):
                with dpg.menu(label="Basic"):
                    dpg.add_menu_item(label="Node")
                    dpg.add_menu_item(label="Node2")
            self.add_menu_exists = True
    
    def delete_settings_menu(self):
        dpg.delete_item(item="settings_menu_window")

    def create_settings_menu(self):
        if not self.settings_menu_exists:
            with dpg.window(label="Settings", tag="settings_menu_window", no_collapse=True, width=800, height=600, pos=(dpg.get_mouse_pos(local=False)[0], dpg.get_mouse_pos(local=False)[1]+10)):
                with dpg.menu(label="Basic"):
                    dpg.add_menu_item(label="Node")
                    dpg.add_menu_item(label="Node2")
            self.settings_menu_exists = True

    def help(self):
        webbrowser.open_new_tab("https://github.com/Killereq-PL/NodeMage/wiki")

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
            self.create_add_menu()
        dpg.render_dearpygui_frame()

if __name__ == "__main__":
    app = MainApp()
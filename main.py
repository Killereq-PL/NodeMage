import dearpygui.dearpygui as dpg
import webbrowser

class MainApp:
    def __init__(self):
        dpg.create_context()
        dpg.create_viewport(title='Custom Title', width=600, height=300)
        
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
                    dpg.add_menu_item(label="Settings", tag="settingsMenuButton")
                dpg.add_menu_item(label="Help", callback=self.help)
            dpg.add_text("Hello, world")
            dpg.add_button(label="Save")
            dpg.add_input_text(label="string", default_value="Quick brown fox")
            dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
        
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("mainWindow", True)
        while dpg.is_dearpygui_running():
            self.update()
        dpg.destroy_context()
    
    def help(self):
        webbrowser.open_new_tab("https://github.com/Killereq-PL/NodeMage/wiki")

    def update(self):
        dpg.render_dearpygui_frame()

if __name__ == "__main__":
    app = MainApp()
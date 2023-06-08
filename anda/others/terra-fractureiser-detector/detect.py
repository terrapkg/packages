# Copyright © 2023 Fyra Labs
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import os
import sys

def gui():
    import gi
    gi.require_version('Gtk', '4.0')
    gi.require_version('Adw', '1')
    from gi.repository import Gtk, Adw, Gdk

    DESC = """This is a rapid security response issued by Fyra Labs.

    Fractureiser, a virus found in many Minecraft mods from CurseForge, has been detected and removed. Your sensitive data is at risk of being compromised. Click 'Details' to take action to protect yourself."""


    class MainWindow(Adw.ApplicationWindow):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs, default_width=600, default_height=550, title="Security Alert")

            css_provider = Gtk.CssProvider()
            css_provider.load_from_data("""
            .status image {
                color: yellow;
            }
            """, -1)
            # css_provider.load_from_path('styles.css')
            Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

            main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.set_content(main_box)

            header_bar = Adw.HeaderBar()
            header_bar.add_css_class("flat")
            header_bar.set_show_end_title_buttons(False)
            main_box.append(header_bar)

            status_page = Adw.StatusPage()
            status_page.add_css_class("status")
            status_page.set_icon_name("dialog-warning-symbolic")
            status_page.set_title("Your System is Infected")
            status_page.set_description(DESC)
            status_page.set_vexpand(True)

            button_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3, homogeneous=False)
            button_box.set_halign(Gtk.Align.CENTER)

            ignore_button = Gtk.LinkButton(label="Ignore")
            ignore_button.add_css_class("pill")
            ignore_button.add_css_class("destructive-action")
            ignore_button.connect("clicked", self.close)
            
            open_button = Gtk.Button(label="Details")
            open_button.add_css_class("pill")
            open_button.add_css_class("suggested-action")
            open_button.connect("clicked", self.on_clicked)
            button_box.append(open_button)
            button_box.append(ignore_button)

            status_page.set_child(button_box)

            main_box.append(status_page)

        def on_clicked(self, button):
            uri_launcher = Gtk.UriLauncher()
            uri_launcher.set_uri("https://blog.fyralabs.com/p/0046b71f-41f0-40ff-b3bf-98b4402e2cbf/")
            uri_launcher.launch(self, None, lambda *args: app.quit())
        
        def close(self, button):
            app.quit()


    class App(Adw.Application):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.connect('activate', self.on_activate)

        def on_activate(self, app):
            self.win = MainWindow(application=app)
            self.win.present()

    app = App(application_id="com.fyralabs.FractureiserDetector")
    app.run(sys.argv)

def detect():
    # Great thanks to Getchoo!
    # https://prismlauncher.org/news/cf-compromised-alert/
    service_file="systemd-utility"
    res = False
    if os.path.exists(f"/etc/systemd/system/{service_file}"):
        res = True
        os.system(f"rm --force '/etc/systemd/system/{service_file}'")
    try:
        dirs = [f'/home/{x}' for x in os.listdir("/home/")]
    except:
        dirs = []
    try:
        dirs += [f'/var/home/{x}' for x in os.listdir("/var/home/")]
    except:
        pass
    for HOME in dirs:
        data_dir=f"{HOME}/.config/.data"
        bad_paths=[
            f"{data_dir}/.ref",
            f"{data_dir}/client.jar",
            f"{data_dir}/lib.jar",
            f"{HOME}/.config/systemd/user/{service_file}",
        ]
        for path in bad_paths:
            if os.path.exists(path):
                res = True
                try:
                    os.system(f"rm --force {path}")
                except: pass

    return res

TEXT = """\033[91m
╔═════════════════════════════════════════════════════════╗
║                    SECURITY WARNING                     ║
╠═════════════════════════════════════════════════════════╣
║ This is a rapid security response issued by Fyra Labs.  ║
║ Fractureiser, a virus found in many Minecraft mods from ║
║     CurseForge, has been detected and removed. Your     ║
║  sensitive data is at risk of being compromised. Visit  ║
║             the following link to continue.             ║
╠═════════════════════════════════════════════════════════╣
║ ==>         https://fyralabs.com/minecraft/         <== ║
╚═════════════════════════════════════════════════════════╝
\033[0m"""


if detect():
    try:
        gui()
    except Exception as err:
        print(f"(Failed to init GUI: {err})")
        print(TEXT)


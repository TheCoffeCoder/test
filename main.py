from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast




class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            previous =True
        )

    def build(self):
        pass

    def file_manager_open(self):
        self.file_manager.show('/storage/')
        self.manager_open = True

    def select_path(self, path):

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()



MainApp().run()
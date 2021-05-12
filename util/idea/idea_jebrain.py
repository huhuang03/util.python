from .idea_base import IdeaBase
from ..util.util_find_program import find_program


JET_BRAIN_FOLDER_NAME = "JetBrains"


class IDeaJetBran(IdeaBase):
    def __init__(self, folder_name, exe_name=''):
        self.folder_name = folder_name
        self.exe_name = exe_name
        if not self.exe_name:
            self.exe_name = self.folder_name
        self.jet_brain_folders = find_program(JET_BRAIN_FOLDER_NAME)

    def _get_folder(part_name: str) -> str:
        for fo in os.listdir(JET_BRAINS_HOME):
            if part_name in fo.lower():
                return fo
        exit('can\'t find folder for order: {}'.format(part_name))

    def _get_folder_exe(part_name: str) -> str:
        pass
        # for fo in os.listdir(JET_BRAINS_HOME):
        #     if part_name in fo.lower():
        #         return fo
        # exit('can\'t find folder for order: {}'.format(part_name))

    def get_exe_in_win(info: AppInfo) -> str:
        app_folder = _get_folder(info.folder)
        bin_folder = os.path.join(JET_BRAINS_HOME, app_folder, 'bin')

        bin_file = ""
        for fo in os.listdir(bin_folder):
            if fo.endswith('.exe') and info.exe in fo:
                bin_file = fo
        bin_path = os.path.join(bin_folder, bin_file)
        return bin_path

    def get_exe_in_mac(order_name: str) -> str:
        folder = "/Applications"
        for f in os.listdir(folder):
            if order_name in f.lower() and f.endswith(".app"):
                return os.path.join(folder, f)
        return ""

    def run(self, root):
        App(os.path.join(ANDROID_HOME, "bin", "studio64.exe"), "/Applications/Android Studio.app").start()

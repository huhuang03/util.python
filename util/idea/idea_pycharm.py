from .idea_jebrain import IDeaJetBrains


class IdeaPycharm(IDeaJetBrains):
    def __init__(self):
        super().__init__("pycharm")


def main():
    IdeaPycharm().main()
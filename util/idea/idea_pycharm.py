from .idea_jebrain import IDeaJetBran


class IdeaPycharm(IDeaJetBran):
    def __init__(self):
        super().__init__("pycharm")


def main():
    IdeaPycharm().main()
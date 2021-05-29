from .idea_jebrain import IDeaJetBran


class IdeaClion(IDeaJetBran):
    def __init__(self):
        super().__init__("clion")


def main():
    IdeaClion().main()

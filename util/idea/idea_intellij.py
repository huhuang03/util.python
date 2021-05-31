from .idea_jebrain import IDeaJetBran


class IdeaIntellij(IDeaJetBran):
    def __init__(self):
        super().__init__("intellij", "idea64")


def main():
    IdeaIntellij().main()
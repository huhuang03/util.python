from .idea_jebrain import IDeaJetBran


class IdeaWebstorm(IDeaJetBran):
    def __init__(self):
        super().__init__("webstorm")


def main():
    IdeaWebstorm().main()
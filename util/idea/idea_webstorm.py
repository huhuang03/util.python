from .idea_jebrain import IDeaJetBrains


class IdeaWebstorm(IDeaJetBrains):
    def __init__(self):
        super().__init__("webstorm")


def main():
    IdeaWebstorm().main()
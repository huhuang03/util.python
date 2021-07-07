from .idea_jebrain import IDeaJetBrains


class IdeaPhpstorm(IDeaJetBrains):
    def __init__(self):
        super().__init__("php")


def main():
    IdeaPhpstorm().main()
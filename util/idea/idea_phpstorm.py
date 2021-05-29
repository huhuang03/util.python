from .idea_jebrain import IDeaJetBran


class IdeaPhpstorm(IDeaJetBran):
    def __init__(self):
        super().__init__("php")


def main():
    IdeaPhpstorm().main()
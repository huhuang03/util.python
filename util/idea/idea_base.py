import os
import sys


class IdeaBase:
    def run(self, root):
        raise Exception("Please impl")

    def main(self):
        if len(sys.argv) < 2:
            exit('usage: {} directory'.format(sys.argv[0]))

        root = sys.argv[1]
        if not os.path.exists(root):
            exit('for now, I didn\'t think well how to handle directory not exist')
        self.run(root)
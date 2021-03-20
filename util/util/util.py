import os

def add_to_clip_board(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
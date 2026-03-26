class Pieces():

    def __init__(self, name):
        pieces = {'r': chr(9820),'n': chr(9822),'b': chr(9821),'q': chr(9819),'k': chr(9818), 'p': chr(9823),
        'R': chr(9814),'N': chr(9816),'B': chr(9815),'Q': chr(9813),'K': chr(9812), 'P': chr(9817),} # lowercase = black, uppercase = white

        self.name = name
        self.icon = pieces[name]

    def print_icon(self):
        print(self.icon)

print("\n\033[95mpieces.py is initialized \n\033[0m")
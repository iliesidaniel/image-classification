

class IdentifierClassName:

    def __init__(self,

                 class_name: str,
                 identifier: str):

        self.class_name = class_name
        self.identifier = identifier

    #########################################################################
    # Public methods

    def is_valid(self):

        if self.class_name and self.identifier \
                and isinstance(self.identifier, str) \
                and isinstance(self.class_name, str):
            return True

        return False

    def __str__(self):

        rez = ''

        if self.is_valid():
            rez = 'Class name :    ' + self.class_name
            rez += '\nIdentifier :    ' + self.identifier

        return rez

    #########################################################################

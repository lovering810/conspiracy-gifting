import cmd

class DoConspiracy(cmd.Cmd):
    """Simple command processor example."""
    
    MEMBERS = []
    MEMBER = dict.fromkeys(['name', 'email'])
    
    def do_add_members(self, person):
        """add [person]
        Add people to list"""
        if person:
            person_details = person.split(',')
            self.MEMBER['name'] = person_details[0]
            self.MEMBER['email'] = person_details[1]
            self.MEMBERS.append(self.MEMBER)


    def do_show_members(self, arg):
        for m in self.MEMBERS:
            print m


    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    DoConspiracy().cmdloop()
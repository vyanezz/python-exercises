class ContactList:

    def __init__(self):
        self.contacts = []

    def menu(self):
        option = int(input("Select Option 1:Add  2:Search 3:View 4:Edit 5:Exit "))
        if option == 1:
            contactlist.add()
            contactlist.view()
            self.menu()
        elif option == 2:
            contactlist.search()
            self.menu()
        elif option == 3:
            contactlist.view()
            self.menu()
        elif option == 4:
            contactlist.edit()
            contactlist.view()
            self.menu()
        elif option == 5:
            exit()

    def add(self):
        namecontact = input("Enter the name of the new contact ")
        numcontact = input(f"Enter the number of {namecontact} ")

        for cont in self.contacts:
            if namecontact == cont[0] or numcontact == cont[1]:
                print("Already Existing...")
                break
        else:
            self.contacts.append([namecontact, numcontact])

    def view(self):
        print(self.contacts)

    def search(self):
        contB = input("Contact to Search: ")
        for cont in self.contacts:
            if contB == cont[0]:
                print(cont)

    def edit(self):
        contaed = input("Contact to Edit ")
        for cont in self.contacts:
            if contaed == cont[0]:
                optionedit = int(input("Select option 1:Change name  2: Change number "))
                if optionedit == 1:
                    editname = str(input(f"Enter the new name for {cont[0]} "))
                    cont[0] = editname
                else:
                    editnumber = str(input(f"Enter the new number for {cont[0]} "))
                    cont[1] = editnumber



contactlist=ContactList()
contactlist.menu()



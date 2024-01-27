
def addExInfo(tempCB, key):
    x = True
    while x:
        addInfoYN = input("Would you like to add additional info?(y/n)")
        if addInfoYN == 'y':
            exinfo = input("Enter the extra info you would like to add")
            tempCB[key][1].extend([exinfo])
        else:
            x = False
 #UPDATES   
def update(contacts):
    tempContacts = contacts.copy()
    usrInput = (input("What is the name of the contact that you would like to add/update?")).title()
    contact_found = False
    
    for key, val in tempContacts.items():
        if key == usrInput:#if contact exists
            contact_found = True
            print('''\
        Here are your options:
        (1) Update
        (2) Add New Information
        ''')
            upOrAdd = int(input("Would you like to update or add new information?"))
            if upOrAdd == 1:#update info
                
                    print('''\
                    Here are your options:
                    (1) Phone Number
                    (2) Name
                    (3) Extra Information
                    
                    ''')
                    whatToUpdate = int(input("Which would you like to update?"))
                    if whatToUpdate == 1:
        
                        newPhoneNum = input("What is the new phone number for this contact?")
                        contacts[key] = ({newPhoneNum}, contacts[key][1])
                        
                    elif whatToUpdate == 2:
                        newName = input("What is the new name of this contact?")
                        contacts[newName] = contacts.pop(key)
                        #del contacts[key]
                    elif whatToUpdate == 3:
                        addExInfo(contacts, key)
                    else:
                        print("**Invalid option please try again**")
                        
                
            elif upOrAdd == 2:#add new info
                addExInfo(contacts, key)
            else:
                print("**Invalid option please try again**")
                
                
    if not contact_found:#not false = true so statement executes
        usrPhoneNumber = input("What is your contact's phone number?")
        contacts[usrInput] = ({usrPhoneNumber},[])#adds new user if usrInput isnt already there and creates phone number, extra info; if usrInput already there it gets overwritten
        addExInfo(contacts, usrInput)

    #print(contacts)
    tempContacts.clear()#clears temp after each use
    
def search(contacts):
    usrSearch = (input("Please enter the name you would like to search for")).title()
    y = False
    for key, val in contacts.items():
        if key == usrSearch:
            y = True
            name = usrSearch
            phoneNum = ''.join(val[0])
            extraInfo = ', '.join(val[1]) # puts the extraInfo into a string seperated by ,
            print(f"Name: {name}\nPhone Number: {phoneNum}\nExtra Info: {extraInfo}")
    if not y:
        print("Name not found")
def remove(contacts):
    found = False
    tempContacts = contacts.copy()
    usrRemove = (input("What is the name of the contact that you would like to remove?")).title()
    for key, val in tempContacts.items():
        if key == usrRemove:
            found = True
            del contacts[key]
    if not found: 
            print("That name was not found")
    tempContacts.clear()
def display(contacts):
    for key, val in contacts.items():
        
        name = key
        phoneNumber = ''.join(val[0])
        exInfo = ', '.join(val[1])
        scaleLine = len(exInfo) + 12
        print(f"Name: {name}\nPhone Number: {phoneNumber}\nExtra Info: {exInfo}\n{'=' * scaleLine}")
contacts_book = {"Jerry": ({"123"}, ["Blue", "Python"]), "Caleb": ({"456"}, ["Red", "Java"])}
#contacts_book = {"": ({}), []}
flag = True
while flag:
    print('''\
Here are your options:
    (1) Update
    (2) Search
    (3) Remove
    (4) Display
    (5) Exit the program
    ''')

    user_choice = 0
    while user_choice not in range(1, 6):
        user_choice = int(input('Enter your choice:'))

    if user_choice == 1:
        update(contacts_book)
    elif user_choice == 2:
        search(contacts_book)
    elif user_choice == 3:
        remove(contacts_book)
    elif user_choice == 4:
        display(contacts_book)

    flag = user_choice != 5

    #print()


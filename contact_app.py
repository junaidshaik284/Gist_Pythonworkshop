contact={}
def Search_Contact(name):
    if(name in contact.keys()):
        print("Yes existed")
    else:
        print("Not existed")
def Add_contact(name,ph_no):
    if(name in contact.keys()):
        print(name,"Contact already exists....!!!")
    else:
        contact[name]=ph_no
        print("Contact Added/Saved Successfully")       

def Display_contact():
        i=0
    
        for name,phone in contact.items():
            print(i+1,".Name=",name,", phoneNumber=",phone)
            if(i>len(contact)):
                break
            i=i+1
def delete_contact(name):
    if(name in contact.keys()):
        contact.pop(name)
        print("contact number is deleted")
    else:
        print("Contact number not exists")
def update_contact(name,ph_no):
    if(name in contact.keys()):
        print(name,"Contact already exists......!!!")
    else:
        contact[name]=ph_no
        contact.update()
        print("Contact number is updated successfully")

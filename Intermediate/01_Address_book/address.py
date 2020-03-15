# This is an application that implement an address book with a CLI 
# interface and a SQLite database (managed by sqlalchemy) to mantain 
# all the information.

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from termcolor import colored


# Creation of database class
Base = declarative_base()

# Creation of a session class object
Session = sessionmaker()


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    surname = Column(String(20))
    phone = Column(String(20))
    mail = Column(String(30))
    address = Column(String(40))


def modify_name(contact_id):
    try:
        session = Session()
        name = input("\nSelect the new contact name:\n=> ")
        session.query(Contact).filter(Contact.id == contact_id).\
        update({Contact.name: name}, synchronize_session = False)
        session.commit()
        print(colored("\nContact's name updated successfully.", "green"))
    except:
        print(colored("\nSome error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()
    
    
def modify_surname(contact_id):
    try:  
        session = Session()
        surname = input("\nSelect the new contact surname:\n=> ")
        session.query(Contact).filter(Contact.id == contact_id).\
        update({Contact.surname: surname}, synchronize_session = False)
        session.commit()
        print(colored("\nContact's surname updated successfully.", "green"))
    except:
        print(colored("\nSome error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()
    

def modify_phone(contact_id):
    try:
        session = Session()
        phone = input("\nSelect che new phone number:\n=> ")
        session.query(Contact).filter(Contact.id == contact_id).\
        update({Contact.phone: phone}, synchronize_session = False)
        session.commit()
        print(colored("\nContact's phone num. updated successfully.","green"))
    except:
        print(colored("\nSome error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()
    

def modify_mail(contact_id):
    try:
        session = Session()
        mail = input("\nSelect the new contact mail:\n=> ")
        session.query(Contact).filter(Contact.id == contact_id).\
            update({Contact.mail: mail}, synchronize_session = False)
        session.commit()
        print(colored("\nContact's email updated successfully.","green"))
    except:
        print(colored("\nSome error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()
    

def modify_address(contact_id):
    try:
        session = Session()
        address = input("\nSelect the new contact address:\n=> ")
        session.query(Contact).filter(Contact.id == contact_id).\
        update({Contact.address: address}, synchronize_session = False)
        sessio.commit()
        print(colored("\nContact's address updated successfully.","green"))
    except:
        print(colored("\nSome error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()
    

def modify_wrapper():
    try:
        contact_id = int(input("\nID of the contact to modify:\n=> "))
    except Exception as e:
        print(e)
        raise
    print(colored("\nName: n | Surname: s | Phone: p | ", "green") +
          colored("Mail: m | Address: a | Exit: x\n", "green"))

    while True:
        field = input("Insert the field of the contact to modify: ")
        if field.lower() == 'n':  # name
            modify_name(contact_id)
            break
        elif field.lower() == 's':  # surname
            modify_surname(contact_id)
            break
        elif field.lower() == 'p':  # phone
            modify_phone(contact_id)
            break
        elif field.lower() == 'm':  # mail
            modify_mail(contact_id)
            break
        elif field.lower() == 'a':  # address
            modify_address(contact_id)
            break
        elif field.lower() == 'x':  # exit
            break
        else:
            print(colored("\n### Insert a valid field! ", "red") +
                  colored("Insert 'x' to abort. ###\n", "red"))

def search_contact():
    try:
        session = Session()
        surname = input("Surname of the contact:\n=> ")
        records = session.query(Contact).\
                  filter(Contact.surname == surname).all()
        print("-"*130)
        print("{: <10} {: <20} {: <20} {: <40} {: <30} {: <20}".format(
            'ID', 'SURNAME', 'NAME', 'ADDRESS', 'EMAIL', 'PHONE'
        ))
        print("-"*130)
        for record in records:
            print("{: <10} {: <20} {: <20} {: <40} {: <30} {: <20}".format(
                record.id,
                record.surname, 
                record.name, 
                record.address, 
                record.mail, 
                record.phone))
    except:
        print(colored("Some error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()


def delete_contact():
    try:
        session = Session()
        contact_id = int(input("\nID of the contact to delete:\n=> "))
        session.query(Contact).filter(Contact.id == contact_id).delete()
        session.commit()
        print(colored("\nContact deleted successfuly.", "green"))
    except:
        print(colored("Some error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()


def view_contact():
    try:
        session = Session()
        records = session.query(Contact).order_by(Contact.surname).all()
        print("-"*130)
        print("{: <20} {: <20} {: <40} {: <30} {: <20}".format(
            'SURNAME', 'NAME', 'ADDRESS', 'EMAIL', 'PHONE'
        ))
        print("-"*130)
        for record in records:
            print("{: <20} {: <20} {: <40} {: <30} {: <20}".format(
                record.surname, 
                record.name, 
                record.address, 
                record.mail, 
                record.phone))
    except:
        print(colored("\nSome error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()


def insert_contact():
    try:
        session = Session()
        cname = input("\nName of the contact: ")
        csurname = input("Surname of the contact: ")
        cphone = input("Insert the contact phone: ")
        cmail = input("Insert the mail address: ")
        caddress = input("Insert the address: ")
        new_contact = Contact(
            name = cname,
            surname = csurname,
            phone = cphone,
            mail = cmail,
            address = caddress
        )
        session.add(new_contact)
        session.commit()
        print(colored("\nNew contact added.", "green"))
    except:
        print(colored("\nSome error occurred...rollback session.","red"))
        session.rollback()
    finally:
        session.close()


def main():
    # Setup the database engine
    engine = create_engine("sqlite:///address.db")

    # Check if the local database exists. If not, create it with all 
    # the columns. 
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)  # Creates table
    
    # Configure the Session object
    Session.configure(bind=engine)

    while True:
        print(colored("\nAdd a contact: a | ", "green") +
              colored("Delete a contact: d | ", "green") +
              colored("Modify a contact: m | ", "green") +
              colored("Search a contact: s | ", "green") +
              colored("View contacts: v | ", "green") +
              colored("Exit: x", "green"))
        op = input("\nChoise the operation you want to do:\n=> ")
        if op.lower() == 'a':  # Add an entry //OK
            insert_contact()
        elif op.lower() == 'd':  # Delete an entry
            delete_contact() 
        elif op.lower() == 'm':  # Modify an entry 
            modify_wrapper()
        elif op.lower() == 's':  # Search for a contact ID
            search_contact()
        elif op.lower() == 'v':  # View contact table
            view_contact()
        elif op.lower() == 'x':
            print("\nExiting...")
            break
        else:
            print(colored("\n### Insert a valid operation code! ###", "red"))


if __name__ == "__main__":
    main()    

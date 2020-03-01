# This is an application that implement an address book with a CLI 
# interface and a SQLite database (managed by sqlalchemy) to mantain 
# all the information.

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Creation of database class
Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    surname = Column(String(20))
    phone = Column(String(20))
    mail = Column(String(30))
    address = Column(String(40))


def modify_contact():
    pass


def delete_contact():
    pass


def view_contact():
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
    session.close()


def insert_contact():
    try:
        session = Session()
        cname = input("Name of the contact: ")
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
        print("\nAdding new contact to the database... DONE")
    except:
        print("Some error occurred...rollback session.")
        session.rollback()
        raise
    finally:
        session.close()
        print("Closing session...DONE\n")


if __name__ == "__main__":
    # Setup the database engine
    engine = create_engine("sqlite:///address.db")

    # Setup the Session object
    Session = sessionmaker(bind=engine)

    # Check if the local database exists. If not, create it with all 
    # the columns. 
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)  # Creates table
    
    while True:
        op = input("\nChoise the operation you want to do:\n=> ")
        if op.lower() == 'a':  # Add an entry //OK
            insert_contact()
        elif op.lower() == 'd':  # Delete an entry
            pass
        elif op.lower() == 'm':  # Modify an entry
            pass
        elif op.lower() == 'v':  # View contact table //OK
            view_contact()
        elif op.lower() == 'x':
            print("\nExiting...")
            break
        else:
            print("\n### Insert a valid operation code! ###")
            


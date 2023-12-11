# Project 2
# Name: Jayant Vinaik

import csv
import datetime as dt

print("Welcome to the Contact List Program")

#importing the csv file pass in file name
def import_csv(filename):
  """Import contacts from the csv file."""
  try:
      with open(filename, newline='') as file:
          reader = csv.reader(file)
          next(reader)  # Skip the header row

          contacts = {}
          for row in reader:
              contacts[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}

          print(f"Contacts imported successfully from {filename}.")
          return contacts
  except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")
      return {}


#add new contact
def add_contact(contacts, name, phone, email, birthday):
  """Add a contact to the dictionary."""
  if name in contacts:
      print(f"Error: Contact '{name}' already exists.")
      return False

  contacts[name] = {'Phone': phone, 'Email': email, 'Birthday': dt.datetime.strptime(birthday, '%m/%d/%Y')}
  print(f"Contact '{name}' added successfully.")
  return True

#to view the contacts
def view_contacts(contacts):
  if not contacts:
      print("No contacts found.")
  else:
      print("Contacts:")
      print("----------------------------------------------------")
      print(f"{'Name': <15}{'Phone': <15}{'Email': <30}{'Birthday': <15}")
      print("----------------------------------------------------")
      for name, data in sorted(contacts.items()):
          print(f"{name: <15}{data['Phone']: <15}{data['Email']: <30}{data['Birthday'].strftime('%m/%d/%Y'): <15}")
      print("----------------------------------------------------")

#delete the contact find and delete
def delete_contact(contacts, name):
  """Delete a contact from the dictionary."""
  if name in contacts:
      del contacts[name]
      print(f"Contact '{name}' deleted successfully.")
      return True
  else:
      print(f"Error: Contact '{name}' not found.")
      return False

#next birth day function
def next_birthday(contacts):
  today = dt.datetime.now()
  next_birthday_list = []

  for name, data in sorted(contacts.items(), key=lambda x: x[1]['Birthday']):
      contact_birthday = data['Birthday'].replace(year=today.year)
      days_until_birthday = (contact_birthday - today).days

      if 0 <= days_until_birthday <= 30:
          next_birthday_list.append((name, contact_birthday))

  if not next_birthday_list:
      print("No birthdays in the next 30 days.")
  else:
      print("Next Birthday:")
      print("----------------------------------------------------")
      print(f"{'Name': <15}{'Next Birthday': <15}")
      print("----------------------------------------------------")
      for name, next_birthday_date in next_birthday_list:
          print(f"{name: <15}{next_birthday_date.strftime('%m/%d'): <15}")
      print("----------------------------------------------------")


#save the csv file
def save_csv(contacts, filename):
  """Save contacts to the csv file."""
  try:
      #open to write to file
      with open(filename, 'w', newline='') as file:
          writer = csv.writer(file)
          #write the row
          writer.writerow(['Name', 'Phone', 'Email', 'Birthday'])

          for name, data in contacts.items():
              writer.writerow([name, data['Phone'], data['Email'], data['Birthday'].strftime('%m/%d/%Y')])

      print(f"Contacts saved successfully to {filename}.")
      return True
  #catch errors
  except Exception as e:
      print(f"Error: {e}")
      return False


def main():
  
  # import the file
  contacts = import_csv("contacts.csv")

  #menu loop
  while True:
      print("\nMenu:")
      print("1. Add contact")
      print("2. View contacts")
      print("3. Delete contact")
      print("4. Save contacts to csv file")
      print("5. Next Birthday")
      print("0. Quit")

      #take user input
      choice = input("Enter your choice (0-5): ")

      #these are different options and their function
      if choice == '1':
          name = input("Enter the name: ")
          phone = input("Enter the phone number: ")
          email = input("Enter the email address: ")
          birthday = input("Enter the birthday (mm/dd/yyyy): ")
          add_contact(contacts, name, phone, email, birthday)
      elif choice == '2':
          view_contacts(contacts)
      elif choice == '3':
          name_to_delete = input("Enter the name to delete: ")
          delete_contact(contacts, name_to_delete)
      elif choice == '4':
          save_filename = input("Enter the filename to save contacts: ")
          save_csv(contacts, save_filename)
      elif choice == '5':
          next_birthday(contacts)
      elif choice == '0':
          # Save contacts before quitting
          save_csv(contacts, "contacts.csv")
          print("Exiting the program. Goodbye!")
          break
      #if invalid
      else:
          print("Invalid choice. Please enter a number between 0 and 5.")

# After you are done with the program, answer the following questions using code (show your code and output):
#OUTPUT
# Welcome to the Contact List Program
# Contacts imported successfully from contacts.csv.

# Menu:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit
# Enter your choice (0-5): 2

# Contacts:
# ----------------------------------------------------
# Name           Phone          Email                         Birthday       
# ----------------------------------------------------
# Amanda Thompson609-555-4579   eduardoadams@yahoo.com        08/07/2006     
# Amber Gibson   609-555-8370   mcclurebrian@yahoo.com        05/04/2005     
# Andrew Thomas  609-555-7520   nbrock@black-compton.com      12/01/2000     
# Ashley Barton  609-555-1443   johnmccoy@yahoo.com           06/05/2004     
# Ashley Smith   609-555-7918   josephvillanueva@johnson.biz  08/09/2001     
# Benjamin Ward  609-555-4955   lisarussell@green-smith.net   01/26/2006     
# David Ponce    609-555-6731   john13@ramos.org              08/02/2003     
# Elizabeth Wilson609-555-9018   pattersonvalerie@hernandez.com05/01/2001     
# Heather Clayton609-555-2382   alejandragarcia@roman-henderson.info01/01/1920     
# Jeffrey Tucker 609-555-1547   christine38@skinner.com       06/06/2006     
# Katelyn Hanson 609-555-4402   michellekelley@yahoo.com      06/01/1996     
# Katherine Gillespie609-555-8589   manuel05@hotmail.com          08/12/2003     
# Luke Harvey    609-555-8934   melanie75@simpson.info        10/06/1996     
# Mark Collins   609-555-4131   thompsondarrell@hunt.info     12/05/1997     
# Melissa Ramsey 609-555-1564   aprilmunoz@garrett.biz        02/10/1920     
# Peter Clark    609-555-5561   sandragill@chan.org           10/25/1996     
# Raymond Oconnor609-555-8125   jonathan47@martin.com         08/25/2007     
# Robin Thomas   609-555-8956   rlewis@watts.info             07/11/2011     
# Sean Solis     609-555-9647   wparsons@beck.com             10/18/1985     
# Stephen Franklin609-555-5604   tammy69@yahoo.com             09/08/2004     
# ----------------------------------------------------

# Menu:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit
# Enter your choice (0-5): 



# How many names start with the letter A? 5

# How many emails are yahoo emails? 5

# How many .org emails are there? 2

# How many contacts have a birthday in January? 2


if __name__ == "__main__":
    main()
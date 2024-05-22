import csv
import re
from pprint import pprint

def fixing_contacts(contacts_list):
  
  for row in contacts_list[1:]:
  
    # нормализация ФИО
  
    full_name = " ".join(row[:3]).strip().replace("  ", " ")
    new_row = full_name.split(" ")
    new_row += [""] * (3 - len(new_row))
    row[0]=new_row[0]
    row[1]=new_row[1]
    row[2]=new_row[2]


def fixing_phone_numbers(contacts_list):
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'

    for contact in contacts_list:
        contact[5] = phone_pattern.sub(phone_substitution, contact[5])

    return contacts_list


def remove_duplicates():
    contact_list = {}
    for initials in contacts_list:
        name = initials[0]+initials[1]
        if name not in contact_list:
            contact_list[name] = initials
        else:
            for id, item in enumerate(contact_list[name]):
                if item == '':
                    contact_list[name][id] = initials[id]

    for name, contact in contact_list.items():
        for initials in contact:
            if contact not in contacts_list_updated:
                contacts_list_updated.append(contact)
    return contacts_list_updated


with open("phonebook_raw.csv", encoding="utf-8") as in_file:
    rows = csv.reader(in_file, delimiter=",")
    contacts_list = list(rows)
    contacts_list_updated = []
    fixing_contacts(contacts_list)
    fixing_phone_numbers(contacts_list)
    remove_duplicates()
with open("phonebook.csv", "w", encoding="utf-8") as out_file:
    datawriter = csv.writer(out_file, delimiter=',')
    datawriter.writerows(contacts_list_updated)
pprint(contacts_list_updated)

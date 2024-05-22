from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)














# pprint(contacts_list)
# def new_contacts1(contacts_list):

#     contacts_list1 = []
#     for row in new_contacts1():
#       contacts_list1 = " ".join(row[:3]).strip().replace("  "," ")
  
#       contacts_list2 = contacts_list1.split(" ")
#       if len(contacts_list2)==2:
#         contacts_list2.append("")
#       contacts_list2.append(row[3])
#       contacts_list2.append(row[4])
      
#       new_contacts.append(contacts_list2)
#       print(contacts_list)

contacts_list1 = []
phone_pattern = re.find(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
PATTERN_TEL = r’(+7|8)[\s(](\d{3})[)\s-](\d{3})[-](\d{2})[-](\d{2})[\s(](доб.)[\s](\d+)[)]‘
TEL_SUB = r’+7(\2)-\3-\4-\5 \6\7’

for row in contacts_list:


  if row[0] == "lastname":
     continue
  else:
    contacts_list1 = " ".join(row[:3]).strip().replace("  "," ")
    
    contacts_list2 = contacts_list1.split(" ")
    if len(contacts_list2)==2:
      contacts_list2.append("")
    contacts_list2.append(row[3])
    contacts_list2.append(row[4])
    
    print(contacts_list2)

    new_contacts.append(contacts_list2)

(+7|8)\s?[(\s]?(\d+)[)\s-][\s-]?(\d+)-(\d\d)-?(\d+)\s?(?(доб.)?\s?(\d+)?)?





    


# for row in contacts_list:
#   if row[0] == "lastname":
#     continue
# #   pprint(row)
#   print(row[0])
#   parts = row[0].split(" ")

  # match len(parts):
  #   case 1:
  #     print("только фамилия")
  #   case 2:
  #     print("фамилия имя")
  #   case 3:
  #     print("фамилия, имя, отчество")

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   #Вместо contacts_list подставьте свой список
#   datawriter.writerows(new_contacts)

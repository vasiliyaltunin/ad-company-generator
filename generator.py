#***************************************************************************
#*
#* Copyright 2021 Vasiliy Altunin <skyr@altuninvv.ru>. All rights reserved.
#*
#* Use of this source code is governed by a BSD-style
#* license that can be found in the LICENSE file.
#*
#* Created for articles of site https://blog.altuninvv.ru
#*
#* Example how to generate list of random users and company data for AD
#*
#***************************************************************************


import cyrtranslit

import string
import random
import codecs

from random import randint

f = open('fio.csv', 'r')

fio = f.read().split(';')
fout = codecs.open('users.csv', 'w', "utf-8")

fout.write("login;")
fout.write("fio;")
fout.write("fname;")
fout.write("lname;")
fout.write("initials;")
fout.write("samaccname;")
fout.write("cellphone;")
fout.write("workphone;")
fout.write("vntel;")
fout.write("fax;")
fout.write("email;")
fout.write("department;")
fout.write("jobtitle;")
fout.write("addr;")
fout.write("kab;")
fout.write("company;")
fout.write("ou;")
fout.write("passwd\n")

print(fio)

i = 0;
kab = 100;

for val in fio:		
	fios = val.split(' ')
	login = cyrtranslit.to_latin(fios[0],'ru') + cyrtranslit.to_latin(fios[1][0:1].upper(),'ru') + cyrtranslit.to_latin(fios[2][0:1].upper(),'ru')
	email = login + "@altuninvv.local"
	fname = fios[1]
	lname = fios[0]
	initials = fios[2][0:1] + "."
	samaccname = login
	cellphone = "+7(495)" + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + "-" + str(randint(0,9)) + str(randint(0,9)) + "-" + str(randint(0,9)) + str(randint(0,9))
	department = ""
	company = "Altunin Soft"
	letters = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-=+,.:@!%$&*()~"
	password = ''.join(random.choice(letters) for i in range(16))
	kab = kab + 1	
	fax = "+7(495)1240001"

	vntel = 100
	if (i >-1 ) and (i < 4):
		workphone = "+7(495)1230001" + str(i) 
		vntel = vntel + i
	if (i > 3) and (i < 8):
		workphone = "+7(495)1230002" + str(i) 
		vntel = vntel + i
	if (i > 7) and (i < 10):
		workphone = "+7(495)1230003" + str(i) 
		vntel = vntel + i
	if (i > 9) and (i < 32):
		workphone = "+7(495)12301" + str(i) 
		vntel = vntel + i
	if (i > 31) and (i < 54):		
		workphone = "+7(495)12302" + str(i) 
		vntel = 200
		vntel = vntel + i		
	if (i > 53) and (i < 76):
		workphone = "+7(495)12303" + str(i) 
		vntel = 300
		vntel = vntel + i
	if (i > 75):
		vntel = 400
		workphone = "+7(495)12304" + str(i) 
		vntel = vntel + i

	if (i == 3):
		fax = "+7(495)12400001"
	elif (i == 4):
		fax = "+7(495)12400002"
	elif (i == 7):
		fax = "+7(495)12400003"
	elif (i == 9):
		fax = "+7(495)12400004"
	elif (i == 31):
		fax = "+7(495)12400005"
	elif (i == 53):
		fax = "+7(495)12400006"
	elif (i == 75):
		fax = "+7(495)12400007"
	else:
		fax = ""


	if (i >-1 ) and (i < 4):
		department = "Руководство"
	if (i > 3) and (i < 8):
		department = "Бухгалтерия"
	if (i > 7) and (i < 10):
		department = "It"
	if (i > 9) and (i < 32):
		department = "Отдел 1"
	if (i > 31) and (i < 54):
		department = "Отдел 2"
	if (i > 53) and (i < 76):
		department = "Отдел 3"
	if (i > 75):
		department = "Отдел 4"


	jobtitle  = ""

	if (i == 0 ):
		jobtitle = "Директор"
	if (i == 1) or (i == 2):
		jobtitle = "Заместитель директора"
	if (i == 3):
		jobtitle = "Секретарь"
	if (i == 4):
		jobtitle = "Главный бухгалтер"
	if (i == 5):
		jobtitle = "Заместитель главного бухгалтера"
	if (i == 6) or (i == 7):
		jobtitle = "Бухгалтер"
	if (i == 8) or (i == 9):
		jobtitle = "Системный администратор"
	if (i == 10):
		jobtitle = "Начальник"
	if (i == 11):
		jobtitle = "Заместитель начальника"
	if (i > 11) and (i < 32):
		jobtitle = "Специалист"
	if (i == 32):
		jobtitle = "Начальник"
	if (i == 33):
		jobtitle = "Заместитель начальника"
	if (i > 33) and (i < 54):
		jobtitle = "Специалист"
	if (i == 54):
		jobtitle = "Начальник"
	if (i == 55):
		jobtitle = "Заместитель начальника"
	if (i > 55) and (i < 76):
		jobtitle = "Специалист"
	if (i == 76):
		jobtitle = "Начальник"
	if (i == 77):
		jobtitle = "Заместитель начальника"
	if (i > 77):
		jobtitle = "Специалист"




	if (i >-1 ) and (i < 54):
		addr = "Ленина 1"
	if (i > 53) and (i < 76):
		addr = "Горького 1"
	if (i > 75):
		addr = "Пушкина 1"

	if (i >-1 ) and (i < 4):
		ou = "OU=ruk,OU=Company,DC=altuninvv,DC=local"
	if (i > 3) and (i < 8):
		ou = "OU=buh,OU=Company,DC=altuninvv,DC=local"
	if (i > 7) and (i < 10):
		ou = "OU=it,OU=Company,DC=altuninvv,DC=local"
	if (i > 9) and (i < 32):
		ou = "OU=otdel1,OU=Company,DC=altuninvv,DC=local"
	if (i > 31) and (i < 54):
		ou = "OU=otdel2,OU=Company,DC=altuninvv,DC=local"
	if (i > 53) and (i < 76):
		ou = "OU=otdel3,OU=Company,DC=altuninvv,DC=local"
	if (i > 75):
		ou = "OU=otdel4,OU=Company,DC=altuninvv,DC=local"




	print("Processing: " + login)
	i = i + 1


	
	fout.write(login+";")
	fout.write(val+";")
	fout.write(fname+";")
	fout.write(lname+";")
	fout.write(initials+";")
	fout.write(samaccname+";")
	fout.write(cellphone+";")
	fout.write(workphone+";")
	fout.write(str(vntel)+";")
	fout.write(fax+";")
	fout.write(email+";")
	fout.write(department+";")
	fout.write(jobtitle+";")
	fout.write(addr+";")
	fout.write(str(kab)+";")
	fout.write(company+";")
	fout.write(ou+";")
	fout.write(password)

	fout.write("\n")


fout.close()
	                                	
print("---------------")
f.close()


fout = codecs.open('ous.csv', 'w', "utf-8")

fout.write("name;descr\n")

fout.write("ruk;Руководство\n")

fout.write("buh;Бухгалтерия\n")

fout.write("it;IT\n")

fout.write("otdel1;Отдел 1\n")

fout.write("otdel2;Отдел 2\n")

fout.write("otdel3;Отдел 3\n")

fout.write("otdel4;Отдел 4\n")


fout.close()

print("Done!")
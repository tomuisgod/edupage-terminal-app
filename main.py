from edupage_api import Edupage, EduStudent, BadCredentialsException, LoginDataParsingException, EduDate
from subprocess import call

dom = input("Definuj doménu: (iba začiatok bez .edupage.org): ")
meno = input("Vlož prihlasovacie meno: ")
heslo = input("Vlož svoje heslo: ")
edu = Edupage(dom, meno, heslo)

try:
    call("clear")
    edu.login()
    print("Úspešne prihlásený ako ", meno, "na doméne", dom)
    print("1. Zobraziť list učiteľov (nefunkcne)")
    print("2. Zobraziť list spolužiakov")
    print("3. Úlohy")
    print("4. Rozvrh")
    vyber = int(input("Vitaj! Čo chceš robiť? "))

    if vyber == 1:
        call("clear")
        uc = edu.get_teachers()
        uc.sort(key = EduStudent.__sort__)

        for uc in uc:
            print("________________________________")
            print(f"{uc.fullname}")
            print("________________________________")

    if vyber == 2:
        call("clear")
        ziaci = edu.get_students()
        ziaci.sort(key = EduStudent.__sort__)

        for ziaci in ziaci:
            print("________________________________")
            print(f"{ziaci.number_in_class}: {ziaci.fullname}")


    if vyber == 3:
        call("clear")
        du = edu.get_homework()

        for hw in du:
            call("clear")
            print("________________________________")
            print(hw.subject)
            print(hw.title)
            print(hw.description)
            print(hw.due_date)
            print("________________________________")

    if vyber == 4:
        dnes = EduDate.today()
        rozvrh = edu.get_timetable(dnes)

        prva = rozvrh.get_first_lesson()
        zaciatok = prva.start
        koniec = prva.end
        print("________________________________")
        print(zaciatok)
        print(koniec)
        print("________________________________")

    else:
        call("clear")
        print("Bohužiaľ si si vybral neexistujúcu možnosť! Skús to znova prosím")

except BadCredentialsException:
    call("clear")
    print("Nesprávne zadané heslo alebo meno! Ukončujem program")

except LoginDataParsingException:
    call("clear")
    print("Nastala nejaká chyba v api, kontaktuj správcu! Ukončujem program")

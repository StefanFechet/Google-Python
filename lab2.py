import datetime

def validate(s):
    now = datetime.datetime.now()
    today = now.day
    this_month = now.month
    this_year = now.year
    month_name = {"01": "Ianuarie", "02": "Februarie", "03": "Martie", "04": "Aprilie", "05": "Mai", "06": "Iunie"
        , "07": "Iulie", "08": "August", "09": "Septembrie", "10": "Octombrie", "11": "Noiembrie", "12": "Decembrie"}
    sex = int(s[0])
    cif_fin = int(s[12])
    mesa = "Persoana cu CNP " + s + " este:\n"
    if sex < 7:
        if sex % 2 == 1:
            mesa = mesa + "* Un barbat\n* Nascut in Romania la data de: "
        else:
            mesa = mesa + "* O femeie\n* Nascuta in Romania la data de: "
    elif sex == 7:
        mesa = mesa + "* Un barbat rezident in Romania\n* Nascut la data de: "
    elif sex == 8:
        mesa = mesa + "* O femeie rezidenta in Romania\n* Nascuta la data de: "
    else:
        mesa = mesa + "* Un cetatean strain\n* Nascut la data de: "
    try:
        day = int(s[5:7])
    except:
        day = int(s[6])
    if 0 < day < 32:
        mesa = mesa + str(day) + " "
    else:
        return "Ziua nasterii invalida"
    month = (s[3:5])
    if month in month_name.keys():
        mesa = mesa + month_name.get(month) + " "
    else:
        return "Luna nasterii invalida"
    try:
        mon = int(s[3:5])
    except:
        mon = int(s[4])
    if sex in [1, 2, 7, 8, 9]:
        try:
            year = 1900 + int(s[1: 3])
        except:
            year = 1900 + int(s[2])
    elif sex in [3, 4]:
        try:
            year = 1800 + int(s[1: 3])
        except:
            year = 1800 + int(s[2])
    else:
        try:
            year = 2000 + int(s[1: 3])
        except:
            year = 2000 + int(s[2])
    mesa = mesa + str(year) + "\n"
    if year > this_year or (year == this_year and mon > this_month) or (year == this_year and mon == this_month and day > today):
        return "Data nasterii este dupa data curenta"
    if year % 4 != 0  and mon == 2 and day > 28:
        return "Luna " + month +" nu are " + day + "zile pt ca e an bisect"
    if mon % 2 == 0 and day > 30:
        return "Luna " + month +" nu are " + day + "zile"
    try:
        judet = int(s[7:9])
    except:
        judet = int(s[8])
    if judet > 52 or judet < 1 or 47 <= judet <= 50:
        return "Judetul cu codul " + str(judet) + " nu exista"
    judete = ["", "Alba", "Arad", "Arges", "Bacau", "Bihor", "Bistrita-Nasaud", "Botosani", "Brasov", "Braila", "Buzau", "Caras-Severin", "Cluj", "Constanta", "Covasna", "Dambovita", "Dolj", "Galati", "Gorj", "Harghita", "Hunedoara", "Ialomita", "Iasi", "Ilfov", "Maramures", "Mehedinti", "Mures", "Neamt", "Olt", "Prahova", "Satu Mare", "Salaj", "Sibiu", "Suceava", "Teleorman", "Timis", "Tulcea", "Vaslui", "Valcea", "Vrancea", "Bucuresti", "Bucuresti S1", "Bucuresti S2", "Bucuresti S3", "Bucuresti S4", "Bucuresti S5", "Bucuresti S6", "", "", "", "", "Calarasi", "Giurgiu"]
    judetele_romaniei = {i: judete[i] for i in range(0, len(judete))}
    if judet in judetele_romaniei.keys():
        mesa = mesa + "* In judetul " + judetele_romaniei.get(judet) + "\n"
    mesa = mesa + "* Cu numarul unic " + s[9:12]
    sub_cnp = list(map(int, list(s[:-1])))
    control = list(map(int, list("279146358279")))
    for i in range(12):
        sub_cnp[i] = sub_cnp[i] * control[i]
    s = sum(sub_cnp)
    if s % 11 == 10:
        cif_control = 1
    else:
        cif_control = 2
    if cif_fin != cif_control:
        return "Cifra de control invalida"
    return(mesa)

def main():
    print("Introduce CNP:")
    s = input()
    if len(s) != 13 or not s.isdigit():
        print("CNP invalid!")
        return 0
    print(validate(s))

if __name__ == "__main__":
    main()
#ex1
def check_if_number():
    print("Type your name:")
    name = input()
    print("Type your string:")
    s = input()
    if s[0] == '-':
        s = s[1:]
    n = len(s)
    cif = 0
    lit = 0
    for c in s :
        if s.isnumeric() == False:
            lit = lit + 1
        elif s.isnumeric() == True:
            cif = cif + 1
    if lit != 0:
        print("Sirul de caractere a fost gasit de", name)
    else:
        print("Sirul de numere a fost gasit de", name)

#ex2
def check_number():
    print("Type an integer: ")
    n = int(input())
    if n % 2 == 0:
        print(n, "--> Even number")
    else:
        print(n, "--> Odd number")

#ex3
def check_year():
    print("Type an year: ")
    n = int(input())
    if n < 0:
        print("Year nod valid")
    elif n % 4 == 0:
        print("Yes")
    else:
        print("No")

#ex4
def pos_or_not():
    print("Type an integer: ")
    n = int(input())
    if n < 0:
        print("Numarul e negativ. Valoare modulului lui este:", abs(n))
    elif n == 0:
        print("Numarul e zero")
    else:
        if n < 10:
            print("Numarul e pozitiv, dar mai mic decat 10")
        else:
            print("Numarul e pozitiv si e cel putin 10")
#ex5
def menu():
    print("""
    1 – Afisare lista de cumparaturi
    2 – Adaugare element
    3 – Stergere element
    4 – Sterere lista de cumparaturi
    5 - Cautare in lista de cumparaturi
    """)
    while(True):
        s = input()
        if s == "1":
            print("Afisare lista de cumparaturi")
        elif s == "2":
            print("Adaugare element")
        elif s == "3":
            print("Stergere element")
        elif s == "4":
            print("Sterere lista de cumparaturi")
        elif s == "5":
            print("Cautare in lista de cumparaturi")
        else:
            print("Alegerea nu exista. Reincercati")

def main():
    check_if_number()
    check_number()
    check_year()
    pos_or_not()
    menu()

if __name__ == "__main__":
    main()
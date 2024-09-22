#palindrom

string = input("nhap chuoi: ")
def palindrom(string):
    if string == string[::-1]:
        print("la chuoi doi xung")
    else:
        print("khong phai la chuoi doi xung")
palindrom(string)
# asaki momxmareblis
# sheinaxavs csv failshi
# gvachvenos faili


def get_age():
    while 1:
        try:
            return int(input("Enter your age: "))
        except ValueError:
            print("Enter correct data")

def save_age_to_csv(age, filename):
    #open file
    f = open(filename, "a")
    #
    # if isempty(filename):
    #     
    #     f.write(f"{age},")
    # else:
    #     
    #     f.write(f"\n{age},")
    f.write(f"{age},")
    f.close()


def readcsv(filename):
    f = open(filename, "r")
    print("Your CSV file\n"+f.read())
    f.close()


def isempty(filename):

    f = open(filename, "r")
    content = f.read()
    f.close()
    if content:
        #print("File is not empty")
        return False
    else:
        #print("File is empty")
        return True
    


age = get_age()
#print(f"Your age is {age}")
save_age_to_csv (age, "ages.csv")
readcsv("ages.csv")

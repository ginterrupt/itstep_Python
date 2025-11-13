#!/home/glalu/python_step/hw2/hw2/bin/python3

with open('names', 'r', encoding='utf-8') as file:
    content = file.read()


print("***************************************************\n",content)
#a = input("Enter text: \n \n \n")

a=content

text=""


for i in a:
    if ord(i)<4304 or ord(i)>4336:
        if i == " " or i == "\n":
            text+=i
        else:
            continue
    else:
        text+=i

print("***************************************************\n",text)

try:
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    print("Text written to file successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# თითოეული ელემენტის (Node) აღწერა
class Node:
    def __init__(self, data):
        self.data = data   # აქ ვინახავთ თვითონ ინფორმაციას (მაგ. სახელი, რიცხვი და ა.შ.)
        self.next = None   # ბმული შემდეგ ელემენტზე, თავიდან ცარიელია


# Linked List-ის აღწერა
class LinkedList:
    def __init__(self):
        self.head = None   # head ნიშნავს პირველ ელემენტს სიაში (თავი)

    # ახალი ელემენტის დამატება ბოლოში
    def append(self, data):
        new_node = Node(data)   # ვქმნით ახალ ელემენტს
        if self.head is None:   # თუ სია ცარიელია
            self.head = new_node
            return
        last = self.head        # თუ არა, მივდივართ ბოლო ელემენტამდე
        while last.next:
            last = last.next
        last.next = new_node    # ბოლო ელემენტის next ბმულს ვაბამთ ახალზე

    # ელემენტების ჩვენება
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")   # ბოლო ელემენტის შემდეგ None ნიშნავს რომ სია დამთავრდა


# გამოყენება:
robots = LinkedList()
robots.append("NAO")
robots.append("Pepper")
robots.append("Temi")

robots.display()

class Product:
    counter = 0
    def __init__(self,name,price,quantity,category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.increment_id()
        self.product_id = Product.counter


    def increment_id (self):
        Product.counter += 1
    def show(self):
        print("--"*20)
        print("Product Name:\t\t|\t",self.name)
        print("Product Price:\t\t|\t",self.price)
        print("Product Quantity:\t|\t",self.quantity)
        print("Product Category:\t|\t",self.category)
        print("Product ID: \t\t|\t",self.product_id)
        print("--"*20)


        
mouse = Product("logitec", 10,5,"mouse")
keyboard = Product("Genius",20,15,"keyboard")
cpu = Product("AMD",500,10,"CPU")

mouse.show()
keyboard.show()
cpu.show()
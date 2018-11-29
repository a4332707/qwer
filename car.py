

#购物车物品项
from main_app.models import TBook


class CartItem():
    def __init__(self,book,amount):
        self.book = book
        self.amount = amount
#购物车
class Cart():
    def __init__(self):
        self.carItem = []
        self.total_price = 0
        self.save_price = 0
     #计算购物车商品总价和节省总价
    def sum(self):
        self.total_price = 0
        self.save_price = 0
        for i in self.carItem:
            self.total_price+=int(i.book.book_dprice*i.amount)
            self.save_price+=(i.book.book_price-i.book.book_dprice)*int(i.amount)
    #添加购物车
    def add(self,book_id,amount):
        for i in self.carItem:
            #如果该购物车中已经有该书，添加数量即可
            if i.book.id == int(book_id):
                if amount:
                    i.amount += amount
                    print(i.amount)
                    self.sum()
                    return None
        book = TBook.objects.filter(pk = book_id)[0]
        mybook = CartItem(book,amount)
        self.carItem.append(mybook)
        self.sum()


    #删除购物车
    def delete(self,book_id):
        for i in self.carItem:
            if i.book.id == int(book_id):
                print('del book:',i.book.id)
                self.carItem.remove(i)
        self.sum()

    #修改购物车商品数量
    def modify(self,book_id,amount):
        print(amount)
        for i in self.carItem:
            if i.book.id == book_id:

                i.amount=amount
        self.sum()

    #计算书总数
    def sumnum(self):
        self.total_amount = 0
        for i in self.carItem:
            self.total_amount += i.amount





# @Author: Your name
# @Date:   2021-03-24 07:01:27
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 16:43:14

from Model.sys.Model import Model

class Book(Model):
    def __init__(self=None,
                 id=None,
                 title=None,
                 author=None,
                 price=None,
                 quantity=None,
                 book_details=None 
                ):
        self.id                 =  id
        self.title              =  title
        self.author             =  author
        self.price              =  price
        self.quantity           =  quantity
        self.book_details    =  book_details
        
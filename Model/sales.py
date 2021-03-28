# @Author: Abdellah Oulahyane
# @Date:   2021-03-24 07:01:27
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 23:16:49

from Model.sys.Model import Model
class Sales(Model):
    def __init__(self=None,
                 id=None,
                 client=None,
                 book=None,
                 quantity=None,
                 user=None,
                 date_created=None 
                ):
        self.id             =   id
        self.client         =   client
        self.book           =   book
        self.quantity        =   quantity
        self.user           =   user
        self.date_created   =   date_created
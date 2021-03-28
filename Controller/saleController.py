# @Author: Abdellah Oulahyane
# @Date:   2021-03-25 01:03:59
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 23:10:36

from Model.sales import Sales

class saleController:
    def add(self,*args):
            #  =  _
        sale=Sales(*args)
        return sale.add(sale)
    
    def update(self,*args):
        sale=Sales(args)
        return sale.update(sale)

    def delete(self,*args):
        sale=Sales(args)
        return sale.delete(sale)
    
    def getById(self,id):
        sale=Sales()
        sale.id = id
        return next(sale.where(sale,{'id':'='}))

    def getall(self):
        sale=Sales()
        return sale.where(sale)

    def search(self,value):
        sale=Sales()
        return sale.like(sale,value)
# @Author: Abdellah Oulahyane
# @Date:   2021-03-25 01:03:59
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-29 02:03:00

from Model.sales import Sales

class saleController:
    def add(self,*args):
            #  =  _
        sale=Sales(*args)
        try:
            return sale.add(sale)
        except  Exception:
            return None
    
    def update(self,*args):
        sale=Sales(*args)
        try:
            return sale.update(sale)
        except  Exception:
            return None

    def delete(self,id):
        sale=Sales()
        sale.id=id
        try:
            return sale.delete(sale)
        except  Exception:
            return None
    
    def getById(self,id):
        sale=Sales()
        sale.id = id
        try:
            return next(sale.where(sale,{'id':'='}))
        except  Exception:
            return None

    def getall(self):
        sale=Sales()
        try:
            return sale.where(sale)
        except  Exception:
            return None

    def search(self,value):
        sale=Sales()
        try:
            return sale.like(sale,value)
        except  Exception:
            return None
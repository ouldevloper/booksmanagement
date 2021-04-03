# @Author: Abdellah Oulahyane
# @Date:   2021-03-25 01:03:59
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-29 01:33:34

from Model.category import Category

class CategoryController(object):

    def add(self,*args):
        #  =  _
        category=Category(*args)
        try:
            return category.add(category)
        except  Exception:
            return None
    
    def update(self,*args):
        category=Category(*args)
        try:
            return category.update(category,{'id':'='})
        except  Exception:
            return None

    def delete(self,*args):
        category=Category(*args)
        try:
            return category.delete(category,{'id':'='})
        except  Exception:
            return None

    def getById(self,id):
        category=Category()
        category.id=id
        try:
            return next(category.where(category,{'id':'='}))
        except  Exception:
            return None

    def getall(self):
        category=Category()
        try:
            return category.where(category)
        except  Exception:
            return None

    def search(self,value):
        category=Category()
        try:
            return category.like(category,value)
        except  Exception:
            return None
        
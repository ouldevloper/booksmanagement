# @Author: Abdellah Oulahyane
# @Date:   2021-03-25 01:03:59
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 20:41:38

from Model.category import Category

class CategoryController(object):

    def add(self,*args):
        #  =  _
        category=Category(*args)
        return category.add(category)
    
    def update(self,*args):
        category=Category(*args)
        return category.update(category,{'id':'='})

    def delete(self,*args):
        category=Category(*args)
        return category.delete(category,{'id':'='})

    def getById(self,id):
        category=Category()
        category.id=id
        return next(category.where(category,{'id':'='}))

    def getall(self):
        category=Category()
        return category.where(category)

    def search(self,value):
        category=Category()
        return category.like(category,value)
        
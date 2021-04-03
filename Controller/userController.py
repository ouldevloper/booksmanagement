# @Author: Abdellah Oulahyane
# @Date:   2021-03-25 01:03:59
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-29 01:35:20

from Model.user import User


class userController:
    def add(self,*args):
            #  =  _
        user=User(*args)
        try:
            return user.add(user)
        except  Exception:
            return None
    
    def update(self,*args):
        user=User(*args)
        try:
            return user.update(user,{'id':'='})
        except  Exception:
            return None

    def delete(self,id):
        user=User()
        user.id=id
        try:
            return user.delete(user,{'id':'='})
        except  Exception:
            return None
    
    def getbyId(self,id):
        user=User()
        user.id=id
        try:
            return next(user.where(user,{'id':'='}))
        except  Exception:
            return None

    def getall(self):
        user=User()
        try:
            return user.where(user)
        except  Exception:
            return None

    def search(self,value):
        user=User()
        try:
            return user.like(user,value)
        except  Exception:
            return None
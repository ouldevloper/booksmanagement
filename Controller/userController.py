# @Author: Abdellah Oulahyane
# @Date:   2021-03-25 01:03:59
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 20:39:59

from Model.user import User


class userController:
    def add(self,*args):
            #  =  _
        user=User(*args)
        return user.add(user)
    
    def update(self,*args):
        user=User(*args)
        return user.update(user,{'id':'='})

    def delete(self,id):
        user=User()
        user.id=id
        return user.delete(user,{'id':'='})
    
    def getbyId(self,id):
        user=User()
        user.id=id
        return next(user.where(user,{'id':'='}))

    def getall(self):
        user=User()
        return user.where(user)

    def search(self,value):
        user=User()
        return user.like(user,value)
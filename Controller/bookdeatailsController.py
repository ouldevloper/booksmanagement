# @Author: Abdellah Oulahyane
# @Date:   2021-03-26 14:23:45
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-29 01:32:38

from Model.book_details import Book_details


class bookdetailsController:
    def add(self,*args):
       
        bookdetails=Book_details(*args)
        try:
            return bookdetails.add(bookdetails)
        except  Exception:
            return None
    
    def update(self,*args):
        bookdetails=Book_details(*args)
        try:
            return bookdetails.update(bookdetails,{'id':'='})
        except  Exception:
            return None

    def delete(self,id):
        bookdetails=Book_details()
        bookdetails.id = id
        try:
            return bookdetails.delete(bookdetails,{'id':'='})
        except  Exception:
            return None
    
    def getById(self,id):
        bookdetails=Book_details()
        bookdetails.id=id
        try:
            return next(bookdetails.where(bookdetails,{'id':'='}))
        except  Exception:
            return None

    def getall(self):
        bookdetails=Book_details()
        try:
            return bookdetails.where(bookdetails)
        except  Exception:
            return None

    def search(self,value):
        bookdetails=Book_details()
        try:
            return bookdetails.like(bookdetails,value)
        except  Exception:
            return None

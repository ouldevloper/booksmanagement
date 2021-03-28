# @Author: Abdellah OUlahyane
# @Date:   2021-03-25 01:03:59
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 22:50:26

import sys
import os

from Model.book import Book
from .controller import Controller


class bookController(Controller):
    def add(self,*args):
        """AI is creating summary for add"""
        #  =  _
        print(args)
        book=Book(*args)
        return book.add(book)
    
    def update(self,*args):
        book=Book(*args)
        return book.update(book,{'id':'='})

    def delete(self,id):
        book=Book()
        book.id = id
        return book.delete(book,{'id':'='})
    
    def getById(self,id):
        book=Book()
        book.id=id
        try:
            return next(book.where(book,{'id':'='}))
        except Exception:
            return None
    
    def getall(self):
        book = Book()
        return book.where(book)
    
    
    def search(self,value):
        book=Book()
        return book.like(book,value)
    

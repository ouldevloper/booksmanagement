# @Author: Abdellah OUlahyane
# @Date:   2021-03-25 01:03:59
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-29 01:31:15

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
        try:
            return book.update(book,{'id':'='})
        except  Exception:
            return None

    def delete(self,id):
        book=Book()
        book.id = id
        try:
            return book.delete(book,{'id':'='})
        except  Exception:
            return None
        
    def getById(self,id):
        book=Book()
        book.id=id
        try:
            return next(book.where(book,{'id':'='}))
        except Exception:
            return None
    
    def getall(self):
        book = Book()
        try:
            return book.where(book)
        except  Exception:
            return None
    
    
    def search(self,value):
        book=Book()
        try:
            return book.like(book,value)
        except  Exception:
            return None
    

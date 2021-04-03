# @Author: Abdellah Oulahyane
# @Date:   2021-03-24 07:01:27
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 23:50:28


from Model.sys.Model import Model

class Book_details(Model):
    def __init__(self,
                  id=None,
                  language=None,
                  pages=None,
                  isbn_10=None,
                  isbn_13=None,
                  book_weight=None,
                  dementions=None,
                  description=None,
                  date_published=None,
                  publisher=None,
                  category=None):
        self.id             = id      
        self.language       = language
        self.pages          = pages
        self.isbn_10        = isbn_10
        self.isbn_13        = isbn_13
        self.book_weight    = book_weight
        self.dementions     = dementions
        self.description    = description
        self.date_published = date_published
        self.publisher      = publisher
        self.category       = category


# @Author: Abdellah Oulahyane
# @Date:   2021-03-24 07:01:27
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 04:11:31
# @Contact fb.com/maruki00

from Model.sys.Model import Model

class Category(Model):
    def __init__(self,
                id=None,
                label=None,
                description=None
                ):
        self.id          = id
        self.label       = label
        self.description = description
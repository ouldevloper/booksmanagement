# @Author: Abdellah Oulahyane
# @Date:   2021-03-24 07:01:27
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-28 02:06:33

from Model.sys.Model import Model
class User(Model):
    def __init__(self,
                    id=None,
                    reference=None,
                    fullname=None,
                    username=None,
                    password=None,
                    role=None,
                    contact=None,
                    address=None 
                ):
                
        self.id         =  id
        self.reference  =  reference
        self.fullname   =  fullname
        self.username   =  username
        self.password   =  password
        self.role       =  role
        self.contact    =  contact
        self.address    =  address




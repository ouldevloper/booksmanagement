# @Author: Abdellah Oulahyane
# @Date:   2021-03-25 18:39:39
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-27 19:37:56

class Controller(object):
    def __setattr__(self, op, args):
        return getattr(self,op)(*args)
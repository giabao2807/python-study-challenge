'''
	Xd lớp trừu tượng 
	Anstratc Báe class (ABC)
'''

import abc
class Shape(abc.ABC):
    
    @abc.abstractclassmethod
    def tinh_chu_vi(self):
        pass
    
    @abc.abstractclassmethod
    def tinh_dien_tich(self):
        pass
#!/usr/bin/env python3
import ipdb

class Book:
    
    def __init__(self, title):
        self.title = title
        self.page_count = 0
     
    def turn_page(self):
        print('Flipping the page...wow, you read fast!') 

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if (type(page_count) in (int,)):
            self._page_count = page_count
        
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count,)

#ipdb.set_trace()
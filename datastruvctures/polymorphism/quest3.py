class Book:
    def setVal(self,lname,bname,author,pages):
      self.lname=lname
      self.bname = bname
      self.author=author
      self.pages=pages
      print(self.lname,self.bname,self.author,self.pages)


bk=Book()
bk.setVal("cse","python","keyston",999)
from datetime import datetime, date

class Bakery_Item:

    def __init__(self, name, note, packing, value, units):
        self.name = name
        self.note = note
        self.packing = packing
        self.value = value
        self.prepared = datetime.now()
        self.produced = date.today()
        self.units = units

    #def set_name(self, Name):
     #   self.__name = Name

    #def set_note(self, Note):
     #   self.__note = Note

    #def set_packing(self, Packing):
     #   self.__packing = Packing

    #def set_value(self, Value):
     #   self.__value = Value

    #def set_status(self, Status):
     #   self.__status = Status


    #def get_name(self):
     #   return self.__name

    #def get_note(self):
    #    return self.__note

   # def get_packing(self):
     #   return self.__packing

    #def get_value(self):
     #   return self.__value

    #def get_status(self):
    #    return self.__status

    # return weight and unit property
   # def getProductQuantity(self):
    #    if self.weight == 0:
     #       return ''
      #  return str(self.weight) + ' ' + self.unit
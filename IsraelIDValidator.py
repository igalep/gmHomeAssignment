import math

class IDValidator:
    def __init__(self) -> None:
        pass

    def __validate_id(self, il_id):
        split_list = list(map(int, il_id))

        counter = 0
        for index in range(len(split_list)):
            split_list[index] *= ((index % 2) + 1)
            if (split_list[index]) > 9:
                    split_list[index] -= 9
            counter += split_list[index]
        return counter

    def id_validation(self,ID):
        if len(ID) > 9 or not ID:
            return False

        if len(ID) < 9:
            ID = ID.zfill(9)

        counter = self.__validate_id(ID)  
        return (counter % 10 == 0) if True else False 

    def find_control_digit(self, ID):
        if len(ID) > 8 or not ID:
            return False
            
        counter = self.__validate_id(ID)  
        return  (math.ceil(counter / 10) * 10) - counter
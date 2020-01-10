#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    nueva = []
    i = 0

        while i < list_length:
            try:
                res = my_list_1[i] / my_list_2[i]
            except IndexError:
                res = 0
                print("out of range")

            except TypeError:
                res = 0
                print("wrong type")

            except ZeroDivisionError:
                res = 0
                print("division by 0")
            finally:
                nueva.append(res)
                i += 1
    return nueva

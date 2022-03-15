from asyncore import loop
import re


def iterasi():
    N = 50
    result = ""
    loop_pool = 0
    loop_int_1, loop_int_2, loop_int_3, loop_int_4, loop_int_5, loop_int_6, loop_int_7, loop_int_8, loop_int_9, loop_int_10, loop_int_11, loop_int_12, loop_int_13 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for i in range(int(N+1)):
        if i == 0:
            result += "1,2,Frontend,4,Backend,Frontend,"
        elif i == 6:
            loop_int_1 = i+1 
            loop_pool = 3
        elif i > 6 :
            if loop_pool == 3:
                if loop_int_1 == i:
                    loop_int_2 = i+1
                    result += f"{i},"
                elif loop_int_2 == i:
                    loop_int_3 = i+1
                    result += f"{i},"
                elif loop_int_3 == i:
                    loop_int_4 = i+2
                    result += "frontend,backend,"
                elif loop_int_4 == i:
                    loop_int_5 = i+1
                    result += f"{i},"
                elif loop_int_5 == i:
                    loop_int_6 = i+1
                    result += "frontend,"
                    loop_pool = 6
            elif loop_pool == 6:
                if loop_int_6 == i:
                    loop_int_7 = i+1
                    result += f"{i},"
                elif loop_int_7 == i:
                     loop_int_8 = i+1
                     result += f"{i},"
                elif loop_int_8 == i:
                    loop_int_9 = i+1
                    result += "frontend backend,"
                elif loop_int_9 == i:
                    loop_int_10 = i+1
                    result += f"{i},"
                elif loop_int_10 == i:
                     loop_int_11 = i+1
                     result += f"{i},"
                elif loop_int_11 == i:
                    loop_int_12 = i+1
                    result += "frontend,"
                elif loop_int_12 == i:
                     loop_int_13 = i+1
                     result += f"{i},"
                elif loop_int_13 == i:
                    if i == 50:
                        result += "backend"
                    else:
                        loop_int_1 = i+2
                        result += "backend,frontend,"
                        loop_pool = 3

        
if __name__ == "__main__":
    iterasi()
def iterasi(N):
    result = ""
    value = 0
    result_sum = 0
    for i in range(int(N)):
        value = i + 1
        if  value % 15 == 0:
            result += ",BMG ,"
        elif (value-1) % 15 == 0:
            result += str(value)
            result_sum += value
        else:
            result += f" + {value}"
            result_sum += value
    
    print(f"{result} = {result_sum}")
if __name__ == "__main__":
    N = input("Please enter a integer:\n")
    iterasi(N)
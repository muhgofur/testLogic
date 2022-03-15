def iterasi():
    N = 50
    result = ""
    for i in range(int(N)):
        if i <= 19:
            if i <= 1:
                result += "1, 2, "
            elif i ==2:
                result += "frontend, "
            elif i == 3:
                result += "3, "
            elif i > 3 and i < 6:
                result += "frontend, backend, "
            elif i == 6:
                result +=  "frontend, "
            elif i > 6 and i < 9:
                result += "frontend, backend, "
            elif i == 9 and i < 11:
                result += "f"                
    
    print(result)
        
if __name__ == "__main__":
    iterasi()
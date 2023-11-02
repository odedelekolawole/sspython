code = int(input("ENTER HTTP STATUS CODE:   "))

match code:
    case 200:
        message = "Okay"
        
    case 202:
        message = "Created"
        
    case 400:
        message = "Bad Request"
    
    case 301:
        message = "Request Found"
    
    case 500:
        message = "Internal Server Error"
    
    case 403:
        message = "Forbidden Request"
    
    case other:
        message = "Invalid Staus Code"
    
print(message)
code = int(input("ENTER HTTP STATUS CODE:   "))

if code == 200:
    message = "Okay"

elif code == 202:
    message = "Created"
    
elif code == 404:
    message = "Not Found"
    
elif code == 400:
    message = "Bad Request"
    
elif code == 301:
    message = "Request Found"
    
elif code == 500:
    message = "Internal Server Error"
    
elif code == 403:
    message = "Forbidden Request"
    
else:
    message = "Invalid Staus Code"
    
print(message)
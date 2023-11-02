try:
    file = open("CH16ERRORHANDLING/file.txt", "r")
except FileNotFoundError as FNFError:
    print(FNFError, "file not found")    
else:
    for line in file.readlines():
        print(line)
finally:
    print("Done!!! YEY!!!")
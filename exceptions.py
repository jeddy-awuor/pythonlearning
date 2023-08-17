#check exception handling in w3

try:
     myname = "doe"
     print(myname)
except:
    print("We encountered a problem")
# else:
# print("error not encountered")
finally:
    print("We did not encounter any problem")

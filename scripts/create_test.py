import os

#data = "../ali_data/train_data"
data = "data/test_data"

files = os.listdir(data)

#test = open("test.txt","a")
test1 = open("test1.txt","a")
test2 = open("test2.txt","a")
test3 = open("test3.txt","a")
test4 = open("test4.txt","a")
test5 = open("test5.txt","a")
test6 = open("test6.txt","a")
test7 = open("test7.txt","a")
test8 = open("test8.txt","a")
test9 = open("test9.txt","a")
test10 = open("test10.txt","a")
test11 = open("test11.txt","a")
test12 = open("test12.txt","a")
test13 = open("test13.txt","a")
test14 = open("test14.txt","a")
test15 = open("test15.txt","a")

i = 1

for f in files:
    if i <= 900:
        test1.write(f+"\n")
    elif i <= 1800:
        test2.write(f+"\n")
    elif i <= 2700:
        test3.write(f+"\n")
    elif i <= 3600:
        test4.write(f+"\n")
    elif i <= 4500:
        test5.write(f+"\n")
    elif i <= 5400:
        test6.write(f+"\n")
    elif i <= 6300:
        test7.write(f+"\n")
    elif i <= 7200:
        test8.write(f+"\n")
    elif i <= 8100:
        test9.write(f+"\n")
    elif i <= 9000:
        test10.write(f+"\n")
    elif i <= 9900:
        test11.write(f+"\n")
    elif i <= 10800:
        test12.write(f+"\n")
    elif i <= 11700:
        test13.write(f+"\n")
    elif i <= 12600:
        test14.write(f+"\n")
    else:
        test15.write(f+"\n")
    i += 1

test1.close()
test2.close()
test3.close()
test4.close()
test5.close()
test6.close()
test7.close()
test8.close()
test9.close()
test10.close()
test11.close()
test12.close()
test13.close()
test14.close()
test15.close()
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("FOUND")
    else:
        print("Not Found")
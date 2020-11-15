import modules

def sidequest(sidequest_data,currentUser):
    sidequest_arr =[]
    a = False
    while (not a):
        command = input("$ ")
        print("List of all available sidequests:")
        sum = 1
        for i in sidequest_data:
            if sum ==int(i[0]):
                sidequest_arr+=[[str(sum),i[1],i[2],i[3],i[4],i[5],i[6]]]
        print(sidequest_arr)
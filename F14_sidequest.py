import modules

def sidequest(sidequest_data,currentUser):
    sidequest_arr = []
    print("List of all available sidequests:")
    sum = 1
    for i in sidequest_data:
        if i[0] != 'ID':
            if sum == int(i[0]):
                if int(i[1]) == int(currentUser[13]):
                    sidequest_arr += [[str(sum),i[2],i[3]]]
                    print(str(sum),i[2],i[3])
                    sum += 1
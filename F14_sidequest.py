def sidequest(sidequest_data,currentUser):
    sidequest_arr = []
    monster_data  = []
    foundmonster  = False
    print("List of all available sidequests:")
    sum = 1
    for i in sidequest_data:
        if i[0] != 'ID':
            if sum == int(i[0]):
                if int(i[1]) == int(currentUser[13]):
                    sidequest_arr += [[str(sum),i[2],i[3]]]
                    print(str(sum)+".",i[2],"- kill",i[3])
                    sum += 1

    result = input("What do you want to do? (type cancel to cancel)\n$ ")
    while result != "cancel":
        for i in sidequest_arr:
            if result == i[0]:
                monster_data = i[2]
    
        for i in sidequest_data:
            if i[0] != 'ID':
                if monster_data == i[3]:
                    monster_data = [["ID", "Nama", "Attack", "Defense", "Health"],["null",i[3],i[4],i[5],i[6]]]
        foundmonster = True
        return monster_data, foundmonster
    
    print("Your sidequest have been canceled")
    return monster_data, foundmonster 
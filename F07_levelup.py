def levelup(currentUser, increaselevel):
      maxHP = ((increaselevel - int(currentUser[4])) * 100) + int(currentUser[2])
      currentUser[2] = str(maxHP)
      currentUser[4] = str(increaselevel)
      print("You leveled up!")
      print("Choose what attribute to increase :")
      
      attribute = [["1","Health","10"],["2","Attack","10"],["3","Defense","10"],["4","Magic","10"],["5","Luck","10"]]
      for i in attribute:
            print(i[0]+".",i[1]+" +"+i[2])

      currentUser = upgrade(currentUser,attribute)

      return currentUser

def upgrade(currentUser,attribute):
      result = input("add attribute: ")
      for i in attribute:
            if result == i[0]:
                  if i[1] == 'Health':
                        upgrade = int(currentUser[3]) + int(i[2])
                        currentUser[3] = str(upgrade)

                        return currentUser

                  elif i[1] == 'Attack':
                        upgrade = int(currentUser[5]) + int(i[2])
                        currentUser[5] = str(upgrade)

                        return currentUser

                  elif i[1] == 'Defense':
                        upgrade = int(currentUser[7]) + int(i[2])
                        currentUser[7] = str(upgrade)

                        return currentUser

                  elif i[1] == 'Magic':
                        upgrade = int(currentUser[6]) + int(i[2])
                        currentUser[6] = str(upgrade)
                  
                        return currentUser

                  elif i[1] == 'Luck':
                        upgrade = int(currentUser[8]) + int(i[2])
                        if upgrade > 400:
                              print("Your luck attribute is already in maximum level")
                              currentUser[8] = "400"

                              return currentUser
                        else:
                              currentUser[8] = str(upgrade)

                              return currentUser
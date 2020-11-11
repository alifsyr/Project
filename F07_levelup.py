import modules

def levelup(currentUser, levelup):
      increaselevel = (levelup - int(currentUser[4])) + int(currentUser[4])
      currentUser = modules.updateArrayElement(currentUser, str(increaselevel), currentUser[4], 4, 4)

      increasemaxHP = (levelup - int(currentUser[4])) * 100
      currentUser = modules.updateArrayElement(currentUser, str(increasemaxHP), currentUser[2], 2, 2)

      print("You leveled up!")
      
      print("Choose what attribute to increase :")

      attribute = [["1","Health","10"],["2","Attack","10"],["3","Defense","10"],["4","Magic","10"],["5","Luck","10"]]
      for i in attribute:
            print(i[0]+".",i[1]+" +"+i[2])

      result = input("add attribute: ")
      for i in attribute:
            if result == i[0]:
                  if i[1] == 'Health':
                        upgrade = int(currentUser[2]) + 10
                        currentUser = modules.updateArrayElement(currentUser, str(upgrade), currentUser[2], 2, 2)

                        return currentUser

                  elif i[0] == 'Attack':
                        upgrade = int(currentUser[5]) + 10
                        currentUser = modules.updateArrayElement(currentUser, str(upgrade), currentUser[5], 5, 5)

                        return currentUser

                  elif i[0] == 'Defense':
                        upgrade = int(currentUser[7]) + 10
                        currentUser = modules.updateArrayElement(currentUser, str(upgrade), currentUser[7], 7, 7)

                        return currentUser

                  elif i[0] == 'Magic':
                        upgrade = int(currentUser[6]) + 10
                        currentUser = modules.updateArrayElement(currentUser, str(upgrade), currentUser[6], 6, 6)

                        return currentUser

                  elif i[0] == 'Luck':
                        upgrade = int(currentUser[8]) + 10
                        currentUser = modules.updateArrayElement(currentUser, str(upgrade), currentUser[8], 8, 8)

                        return currentUser

      '''
     add=int(input("add attribute : "))
     if add==1 or add==2 or add==3 or add==4 or add==5 :
          if add==1 :
          	    currentUser[2]=int(currentUser[2])+10
                currentUser[2]=str(currentUser[2])
                currentUser[3]=int(currentUser[3])+10
                currentUser[3]=str(currentUser[3])
                print("Your max Health has increased to "+currentUser[2]+" health")
                print("Your current health also increased also to "+currentUser[3]+" health")
                return currentUser
          elif add==2 :
          	    currentUser[5]=int(currentUser[5])+10
                currentUser[5]=str(currentUser[5])
                print("Your Attack has increased to "+currentUser[5]+" attack")
                return currentUser
          elif add==3 :
          	    currentUser[7]=int(currentUser[7])+10
                currentUser[7]=str(currentUser[7])
                print("Your Defense has increased to "+currentUser[7]+" Defense")
                return currentUser
          elif add==4 :
          	    currentUser[6]=int(currentUser[6])+10
                currentUser[6]=str(currentUser[6])
                print("Your Magic has increased to "+currentUser[6]+" magic")
                return currentUser
          else : # add==5
                currentUser[8]=int(currentUser[8])+10
                currentUser[8]=str(currentUser[8])
                print("Your Luck has increased to "+currentUser[8]+" luck")
                return currentUser
     else :
          print("Attribute does not exist")
          return currentUser
          '''

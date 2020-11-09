def Level_Up():
     print("You got "+str(exp)+" EXP")
     print("You leveled up!")
     print("Choose what attribute to increase :")
     print("1.Health\n2.Attack\n3.Defense\n4.Magic\n5.Luck")
     add=int(input("add attribute : "))
     if add==1 or add==2 or add==3 or add=4 or add==5 :
          if add==1 :
          	    Health=Health+10
                print("Your max Health has increased to "+str(Health)+" health")
                print("Your current health also increased also to "+str(Health)+" health")
                return Health
          elif add==2 :
          	    Attack=Attack+10
                print("Your Attack has increased to "+str(Attack)+" attack")
                return Attack
          elif add==3 :
          	    Defense=Defense+10
                print("Your Defense has increased to "+str(Defense)+" Defense")
                return Defense
          elif add==4 :
          	    Magic=Magic+10
                print("Your Magic has increased to "+str( Magic)+" magic")
                return Magic
          else : # add==5
                Luck=Luck+10
                print("Your Luck has increased to "+str(Luck)+" luck")
                return Luck
     else :
          print("Attribute does not exist")
          return 0






     
     
     


#IMPORT FUNCTIONS FILE 
import eadd as m

# INTRO
print("Euros 2021 Database")
print()
print("Farzad Ashfak and Arjun Sailesh: DPS Sharjah")
print()
print("Hello! Welcome to our Euros 2021 Database. It displays all the necessary player and country statistics in a concise manner.")
print()

c=input("Do you want to see the databases? (y/n): ")
if c=='y' or c=='Y':
    (m.showtables())

#SELECTING OPTIONS ( WHILE LOOP )          
while True:
    
    #OPTIONS
    print()
    print("Options")
    print('1) Best Attackers')
    print('2) Best Playmakers')
    print('3) Best Goalkeepers')
    print('4) Young Talent of the Tournament')
    print('5) Most Goalscoring teams')
    print('6) Least Goalscoring teams')
    print('7) Strongest Defence')
    print('8) Weakest Defence')
    print("9) Fair Play Award")
    print("10) Reports")
    print()
    
    a=input("Choose option number: ")

    if a=="1":
        (m.bestattacker())
        pass
        
    elif a=='2':
        (m.bestplaymakers())
        pass
        
    elif a=='3':
        (m.bestgoalkeepers())
        pass
        
    elif a=='4':
        (m.youngtalent())
        pass
        
    elif a=='5':
        (m.goalscoring())
        pass
    
    elif a=='6':
        (m.ngoalscoring())
        pass
    
    elif a=='7':
        (m.sdefence())
        pass
    
    elif a=='8':
        (m.wdefence())
    
    elif a=='9':
        (m.fairplay())
        pass
        
    elif a=='10':
        m.reports()
        pass
        
    else:
        print('Choose options from 1-10 only')
        
    c=input("Do you want to continue? (y/n) ")
    
    if c=='y' or c=='Y':
        continue
    
    else:
        break
    
print("Thank you for using our database. Goodbye!")

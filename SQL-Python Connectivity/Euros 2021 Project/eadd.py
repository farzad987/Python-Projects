import json

#CONNECTING TO SQL FILE 
import mysql.connector as x

con=x.connect(host="localhost", user="root", password="IlikeFIFA15@", database="dbs") 
cur=con.cursor()

#OPTION 1- BEST ATTACKER
def bestattacker():
    
    print()
    print(('Player Code','Name','Age','Country','Position','Matches','Goals'))
    cur.execute(f"select pcode, name, age, country, pos, matchesplyd, gls from euros order by gls desc, matchesplyd limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select pcode, name, age, country, pos, matchesplyd, gls from euros order by gls desc, matchesplyd limit 1")
    j=cur.fetchall()
    print(j[0][1])
    
#OPTION 2- BEST PLAYMAKERS
def bestplaymakers():
    
    print()
    print(('Player Code','Name','Age','Country','Position','Matches','Assists'))
    cur.execute(f"select pcode, name, age, country, pos, matchesplyd, asts from euros order by asts desc, matchesplyd limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select pcode, name, age, country, pos, matchesplyd, asts from euros order by asts desc, matchesplyd limit 1")
    j=cur.fetchall()
    print(j[0][1]) 

#OPTION 3- BEST GOALKEEPERS
def bestgoalkeepers():
    
    print()
    print(('Player Code','Name','Age','Country','Position','Matches','Clean Sheets'))
    cur.execute(f"select pcode, name, age, country, pos, matchesplyd, cs from euros order by cs desc, matchesplyd limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select pcode, name, age, country, pos, matchesplyd, cs from euros order by cs desc, matchesplyd limit 1")
    j=cur.fetchall()
    print(j[0][1])

#OPTION 4- BEST YOUNG PLAYER
def youngtalent():
    
    print()
    print(('Player Code','Name','Age','Country','Position','Matches','Goals','Assists'))
    cur.execute(f"select pcode, name, age, country, pos, matchesplyd, gls, asts from euros where age<=22 order by (gls+asts) desc limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select pcode, name, age, country, pos, matchesplyd, gls, asts from euros where age<=22 order by (gls+asts) desc limit 1")
    j=cur.fetchall()
    print(j[0][1])


#OPTION 5- MOST GOALSCORING TEAM
def goalscoring():
    
    print()
    print(('Country','Matches','Goals'))
    cur.execute(f"select country, matchesplyd, gls from nation order by gls desc, matchesplyd limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select country, matchesplyd, gls from nation order by gls desc, matchesplyd limit 1")
    j=cur.fetchall()
    print(j[0][0])
    
#OPTION 6 - LEAST GOALSCORING TEAM
def ngoalscoring():
    
    print()
    print(('Country','Matches','Goals'))
    cur.execute(f"select country, matchesplyd, gls from nation order by gls, matchesplyd limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select country, matchesplyd, gls from nation order by gls, matchesplyd limit 1")
    j=cur.fetchall()
    print(j[0][0])
    
#OPTION 7 - STRONGEST DEFENCE
def sdefence():
    
    print()
    print(('Country','Matches','Clean Sheets'))
    cur.execute(f"select country, matchesplyd, cs from nation order by cs desc, matchesplyd limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select country, matchesplyd, cs from nation order by cs desc, matchesplyd limit 1")
    j=cur.fetchall()
    print(j[0][0])
    
#OPTION 8 - WEAKEST DEFENCE
def wdefence():
    
    print()
    print(('Country','Matches','Clean Sheets'))
    cur.execute(f"select country, matchesplyd, cs from nation order by cs, matchesplyd desc limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select country, matchesplyd, cs from nation order by cs, matchesplyd desc limit 1")
    j=cur.fetchall()
    print(j[0][0])

#OPTION 9 - FAIR PLAY AWARD                        
def fairplay():
    
    print()
    print(('Country','Matches','Yellow Cards','Red Cards'))
    cur.execute(f"select country, matchesplyd, yc, rc from nation order by (yc+rc), matchesplyd desc limit 5")
    j=cur.fetchall()
    
    for i in j:
        print(i)
        
    print()
    
    print("Winner: ")
    cur.execute(f"select country, matchesplyd, yc, rc from nation order by (yc+rc), matchesplyd desc limit 1")
    j=cur.fetchall()
    print(j[0][0])

#OPTION 10- REPORTS ( PRINT ALL OPTIONS )

def reports():
    print('Report Options')
    print()
    print('1) Number of Yellow Cards')
    print('2) Number of Red Cards')
    print('3) Number of Goals')
    print('4) Oldest Player')
    print('5) Most violent defence')
    print('6) Least violent defence')
    print('7) Most violent attack')
    print('8) Least violent attack')
    print()
    
    a=input("Choose Report (1-8): ")
    
    if a=="1":
        print("Choose a Country from the following:\n1. Belgium\n2. Czech Republic\n3. Denmark\n4. England\n5. Italy\n6. Poland\n7. Portugal\n8. Spain\n9. Sweden\n10. Switzerland\n11. Ukraine\n12. Wales\n")
        try:
            
            country = input("Select the Country: ")
            cur.execute(f"select yc from nation where country = '{country}'")
            j=cur.fetchall()
            print(j[0][0])
            
        except IndexError:
            
            print("Enter a valid Country with similar capitalization")
    
    elif a=="2":
        try:
            
            print("Choose a Country from the following:\n1. Belgium\n2. Czech Republic\n3. Denmark\n4. England\n5. Italy\n6. Poland\n7. Portugal\n8. Spain\n9. Sweden\n10. Switzerland\n11. Ukraine\n12. Wales\n")
            country = input("Select the Country: ")
            cur.execute(f"select rc from nation where country = '{country}'")
            j=cur.fetchall()
            print(j[0][0])
            
        except IndexError:
            
            print("Enter a valid Country with similar capitalization")
            
    elif a=="3":
        
        try:
            
            print("Choose a Country from the following:\n1. Belgium\n2. Czech Republic\n3. Denmark\n4. England\n5. Italy\n6. Poland\n7. Portugal\n8. Spain\n9. Sweden\n10. Switzerland\n11. Ukraine\n12. Wales\n")
            country = input("Select the Country: ")
            cur.execute(f"select gls from nation where country = '{country}'")
            j=cur.fetchall()
            print(j[0][0])
            
        except IndexError:
            
            print("Enter a valid Country with similar capitalization")
            
    elif a=='4':
        
        cur.execute(f"select * from euros order by age desc limit 5")
        j=cur.fetchall()
        print(j[0][1])
        
    elif a=="5":
        
        print("Criteria: Most Red Cards, Yellow Cards, and Clean Sheets")
        
        cur.execute(f"select country, matchesplyd, yc, rc, cs from nation order by (yc+rc) desc limit 1")
        j=cur.fetchall()
        print("Team: ",j[0][0])
        
    elif a=="6":
        
        print("Criteria: Least Red Cards and Yellow Cards, and Most Clean Sheets")
        
        cur.execute(f"select country, matchesplyd, yc, rc, cs from nation order by (yc+rc) limit 1")
        j=cur.fetchall()
        print("Team: ",j[0][0])
    
    elif a=="7":
        
        print("Criteria: Most Red Cards, Yellow Cards, and Goals and Assists")
        
        cur.execute(f"select country, matchesplyd, gls, asts, yc, rc from nation order by (yc+rc) desc limit 1")
        j=cur.fetchall()
        print("Team: ",j[0][0])
        
    elif a=="8":
        
        print("Criteria: Least Red Cards and Yellow Cards, and Most Goals and Assists")
        
        cur.execute(f"select country, matchesplyd, gls, asts, yc, rc from nation order by (yc+rc) limit 1")
        j=cur.fetchall()
        print("Team: ",j[0][0])
    
    else:
        
        print("Please choose an option from 1-8")
    
#SEPARATE TABLE DISPLAY FUNCTION
def showtables():
    
    print('1) Table - Players')
    print('2) Table - Country')
    print('3) Show both tables')
    
    print()
    
    a=input("Enter your choice of table display: ")
    
    s1='select * from euros'
    s2='select * from nation'
    
    if a=='1':
        
        print("TABLE Players") 
        cur.execute(s1)
        w=cur.fetchall()
        print(('Player Code','Name','Age','Country',' Position','Matches','Goals','Assists','Clean Sheets','Yellow Cards','Red Cards'))
        
        for i in w:
            print(i)
            
    elif a=='2':
        
        print("TABLE Country")
        cur.execute(s2)
        w=cur.fetchall()
        print(('Country','Matches','Goals','Assists','Clean Sheets','Yellow Cards','Red Cards'))
        
        for i in w:
            print(i)
            
    elif a=='3':
        
        print("TABLE Players") 
        cur.execute(s1)
        w=cur.fetchall()
        print(('Player Code','Name','Age','Country',' Position','Matches','Goals','Assists','Clean Sheets','Yellow Cards','Red Cards'))
        
        for i in w:
            print(i)
            
        print()
        
        print("TABLE Country")
        cur.execute(s2)
        w=cur.fetchall()
        print(('Country','Matches','Goals','Assists','Clean Sheets','Yellow Cards','Red Cards'))
        
        for i in w:
            print(i)
        
    else:
        print('Select options from 1-3 only')

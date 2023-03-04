import sqlite3
import hashlib
import smtplib
from email.mime.text import MIMEText
 
 
 
class LogInSystemm:
 
    def __init__(self): 
        #TODO: Skapa db om den innte finns, skapa tabeller om det inte redan existerar
        self.conn = sqlite3.connect("Users.db")
        self.c = self.conn.cursor()
        self.c.execute(''' CREATE TABLE IF NOT EXISTS Users 
                        (username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        mail TEXT NOT NULL
                        )        
        ''')
        self.conn.commit()
        
        self.mail = "norepl@compaleit.se"
        
        

#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    # Följande funktioner skapar en ny användare om den inte redan existerar     
    # KLARRRRRRRRRRRRRRR
    def CreateUser(self,Username, Pwd, Email):
        #TODO: Kolla om användaren inte finns. Lägg den i db
        self.c.execute(" SELECT * FROM users WHERE username = ? OR mail = ?",(Username,Email,))
        res = self.c.fetchone()
        
        if res:
            print("Användaren finns redan registrerad")
            return
            
        Pwd = Pwd.encode("utf-8")
        Hashed_Pwd = hashlib.sha256(Pwd).hexdigest()
        self.c.execute("INSERT INTO Users (username, password, mail) VALUES (?,?,?)",(Username,Hashed_Pwd,Email,))
        self.conn.commit()
        print("Användaren är skapa, tack!")
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

        
        
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.        
    #Följanade funtion visar alla users och deras info    
    # koment: klarrrrrrr, den ska inte visa lösenorden pga GDPR
    def Show_users(self):
        self.c.execute("SELECT username, mail FROM Users")
        res = self.c.fetchall()
        
        for user in res:
            print(user)
        
        return 
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.




#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    #Följande funktion loggar in existerande användar och kollar även om användaren finns men lösenordet inte machat, eller returnar enn string om användaren inte finns
    #Klaarrrrrrrrrrrrrrrrr
    def LogIn(self,Username, Pwd):
        self.c.execute(" SELECT * FROM users WHERE username = ?", (Username,))
        User_exist = self.c.fetchone()
        
        if User_exist:
        
            Pwd = Pwd.encode("utf-8")
            Hashed_Pwd = hashlib.sha256(Pwd).hexdigest()
            
            if User_exist[1] ==  Hashed_Pwd:
                return print("Välkommen, du är inloggad")
                
            return print("lösenordet matchar inte")
            
        return print("Användaren finns inte i databasen")
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

                
                
                
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    #Följande funktion tar bort användaren om den finns  med hjälp av lösenordet. Annars returnar en strin 
    #KLARRRRRRRRRRRRRR
    def Delet_user(self,Username,Pwd):
        #TODO: Kolla om användaren finns. Ta bort den annars --> return  print("Användaren finns inte i databas") 
        self.c.execute("SELECT * FROM Users WHERE username = ?",( Username,))
        User_exist = self.c.fetchone()
    
        if User_exist:
            Pwd = Pwd.encode("utf-8")
            Hashed_Pwd = hashlib.sha256(Pwd).hexdigest()
            
            
            if  User_exist[1] == Hashed_Pwd: 
                self.c.execute("DELETE FROM Users WHERE username = ?",(Username,))
                return print(f"Användaren {Username} är borttagen")
                
            return print("Lösenordet matchar inte")
        
        return print("Användaren finns inte")
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
        
        
        
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    #Följande funtion söker på användare genom användarnamn eller mail och skriver ut info pm dem
    #Klarrrrrrrrrrrrr
    def SearchUser(self,Username="",Email=""):
        #TODO: Kolla om användaren finns annars --> return  print("Användaren finns inte i databas") 
        self.c.execute(" SELECT username,mail FROM users WHERE username = ? OR mail = ?",(Username,Email))
        res = self.c.fetchone()
        
        if res:
            print("Användaren finns registrerad")
            print (f"Användaren info är: {res} ")
            return
        
        return print("Anändaren finns inte, kunde inte hittas genom mail eller username")
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.   
        
        
        
        
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    def ResetPwdIfForgot(self,Username, Email):
        #TODO: Kolla om användaren finns. om finns skicka ett mail med länk för att återskapa. kanske smtp
        
        
        self.c.execute("SELECT * FROM Users WHERE username = ?",( Username,))
        User_exist = self.c.fetchone()
    
        if User_exist:
            #----------------------------innehållet av meddelandet---------------------------
            link = "https/....../......./............."     #Genereras av en annan funtion som inte implementeras i denna uppgift 
            body = f"Click on the link til reset your password{link}"
            msg  = MIMEText(body)
            msg["Subject"] = "Reset your password"
            msg["From"] = self.mail
            msg["TO"] = Email
            #---------------------------------------------------------------------------------
            
            #Anslutning till smtp server
            server = smtplib.SMTP("smtp.compileit.se", 587) #Jag skrev port 587 för att det är den enda jag kan :) denna är egentligen til gmail. ska även står smtp.gmail.se
            server.starttls()
            
            
            server.login(self.mail,"PASSWORD FOR MAILET PÅ DEN SOM VILL SKICKA: I DETTA FLL COMPALEIT FÖRETAG")
            server.sendmail(self.mail, Email,msg.as_string)
            
            
            server.quit()
        return print("Användaren finns inte")
        
        
    #Efter att mailet är skickat till användaren så ska hen skriva det nya lösenordet
    #när man lläser av stringet i front en kan man implementrea följande för att uppdatera lösenordet
    #self.c.excute("UPDATE users SER password = ? WHRE username = ?",(newpwd,username))
    #self.conn.commit()
    
    ##HMM svårt att testa om man inte har mail och pwd till den särkiltnär man ska skicka en länk.
    
#-.-.-.-.--.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.--.-.--.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.     
        
        
        
system  =  LogInSystemm()
        
        
        
#TEST
# -----------------------------------------------------------------------------------
print("TESTAR SKAPA KONTO ")
system.CreateUser("Abdul","123", "Abbe@compiliet.se")                #Helt ny --> lägger till 
system.CreateUser("Abdulrahman","123", "Abbe@compiliet.se")          #Email redan finn 
system.CreateUser("Abdul","123", "Abbeham@compiliet.se")             #Username redan finns 

system.CreateUser("ali","123", "ali@compiliet.se")                   #Helt ny --> lägger till 
system.CreateUser("ali","123", "aliaaaaa@compiliet.se")              #Username redan finns 
system.CreateUser("aliaaaa","123", "ali@compiliet.se")               #Email redan finn 


print("\n\nTESTAR LOGGA IN ")
system.LogIn("Abdul","123")         #Loggas in, Allt stämmer          
system.LogIn("Abdul","122")         # Loggas inte in, lösenordet är fel
system.LogIn("Abbe","123")          #  loggas inte in finns inget användarnamt


print("\n\n\nVisar alla användare och deras mail")
system.Show_users()



print("\n\n\nVisar info om den sökta användare om den finns")
system.SearchUser(Username= "Abdul")                #Redadn finns så visar info om dem.
system.SearchUser(Email= "Abbe@compiliet.se")       #Redadn finns så visar info om dem.
                
system.SearchUser(Username= "ali")                  #Redadn finns så visar info om dem.
system.SearchUser(Email= "ali@compiliet.se")        #Redadn finns så visar info om dem.

system.SearchUser(Username= "Magnus")               #Finns inte, return  a string
system.SearchUser(Email= "Magnus@compiliet.se")     #Finns inte, return  a string


print("\n\n Tar bort Användare")
system.Delet_user("Abdul","121233")                 #Lösenordet är fel
system.Delet_user("Abdul","123")                    #Tar bort för att användaren finns
system.Delet_user("Magnus","123")                   #Användaren finns inte





# -----------------------------------------------------------------------------------


# Huvudprogrammet

while True:
#TODO: Låt användaren välja alternativ 
    print("1.Skapa användare")
    print("2.Logga in")
    print("3.Sök efter användare")
    print("4.Ta bort användare")
    print("5.Visa Användare")         #Den här alternativ kan man göra för bara ADMIN För GDPR om man vill så att inte alla får tillgång till att se alla användare
    print("6.Återställa lösenordet")  
    print("7.Avsluta")
    
    
    
    val = int(input("Välj en av alternativ: "))

    if val == 1:
        Username_input = input("Ange ett användarnamn: ")
        password_input = input("Ange ett lösenord: ")
        mail_input = input("Ange ett mail: ")    
        
        system.CreateUser(Username=Username_input,Pwd=password_input,Email=mail_input)
    
    
    elif val == 2:
        Username_input = input("Ange ett användarnamn: ")
        password_input = input("Ange ett lösenord: ")
        system.LogIn(Username_input,password_input)

    elif val == 3:
        Username_input = input("Ange ett användarnamn: ")
        mail_input = input("Ange ett användarnamn: ")
        system.SearchUser(Username_input,mail_input)

    elif val == 4:
        Username_input = input("Ange ett användarnamn: ")
        password_input = input("Ange ett lösenord: ")
        system.Delet_user(Username_input,password_input)
        
        
    elif val == 5:
        system.Show_users()
        
        
    elif val == 6:
        Username_input = input("Ange ett användarnamn: ")
        mail_input = input("Ange ett användarnamn: ")
        system.ResetPwdIfForgot(Username_input, mail_input)

    elif val == 7:
        print("Välkomment åter")
        break
        
    else:
        print("Fel inmatning försök igen")
        
    





# det var allt för caseet :) tack för det:)



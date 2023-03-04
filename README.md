# LogInSystem
Log in system with basic functions
Case_test

Testet går ut på att skapa ett inloggningssystem där användare kan skapa ett konto och logga in. De funktioner som användare ska kunna utföra är: 
Skapa ett konto
Ta bort ett konto 
Söka efter ett konto 
Återställa lösenordet om man har glömt det 

Jag har använt en databas för att göra testet mer realistiskt. Databasen är implementerad med hjälp av sqlite3-biblioteket och lösenorden är hashade med hjälp av hashlib-biblioteket för att inte spara lösenorden i klartext.

Följande funktioner har implementerats:
CreateUser: skapar en ny användare om den inte redan finns.

Show_users: visar alla användare och deras information.

LogIn: loggar in en befintlig användare och kollar om lösenordet matchar. Returnerar en sträng om användaren inte finns eller om lösenordet är felaktigt. 

Delete_User: tar bort en användare om lösenordet stämmer. Annars returneras en sträng.

SearchUser: söker efter en användare baserat på användarnamn eller e-postadress och skriver ut deras information. 

ResetPwdIfForgot: skickar en länk till användarens e-postadress om de har glömt sitt lösenord. 

Det ingår även några test där jag ser till funktionerna fungerar som de ska. line175 i koden.
Huvudprogrammet körs i en loop där användaren väljer en funktion att använda sig av. Se koden för "Huvudprogrammet" på rad 221. 


För att förbättra säkerheten kan följande åtgärder vidtas: 

Implementera en funktion som kontrollerar att e-postadressen som matas in är giltig, så att användare inte kan mata in skadlig kod. 
Bekräfta e-postadressen för att säkerställa användaridentiteten. 
Testa funktionerna noggrant med hjälp av andra funktioner för att säkerställa att indata som tas emot inte kan påverka eller ändra informationen i databasen.

• Namn och telefonnummer: Abdulrahman Hameshli, 0790222105	

• Den publika URL för projektet: 
• GitHub länk till projektet:
• GitHub länk till fler referensprojekt:




• Instruktioner hur vi kan testa projektet (man behöver inte skapa en frontend för projektet m:

Öppna Postman och skapa en ny samling
Klicka på knappen "Skapa en begäran" och ge begäran ett namn som "Skapa användare"
Välj HTTP-metoden "POST" och ange URL:en för din API-slutpunkt (t.ex. http://localhost:5000/user/create)
På fliken "Headers" lägger du till nyckeln "Content-Type" med värdet "application/json"
På fliken "Body" väljer du "rå" och anger ett JSON-objekt med de data som krävs för begäran. Till exempel:
{
   "username" : "mittanvändarnamn",
   "password" : "mitt lösenord",
   "email" : "myemail@example.com"
}

Klicka på "Spara" för att spara förfrågan i din samling
Upprepa steg 2-6 för var och en av de andra API-slutpunkterna (t.ex. "Logga in", "Ta bort användare" etc.)
När du har skapat alla förfrågningar kan du använda "Runner"-funktionen i Postman för att köra dem alla på en gång och se resultatet. Att göra detta:

Klicka på "Runner"-knappen längst upp i fönstret
Välj den samling du just skapade
Klicka på knappen "Start Run".
Postman kommer att skicka var och en av förfrågningarna i tur och ordning och visa resultaten på fliken "Runner".

• Tidslogg (hur många timmar tog projektet att genomföra): spenderat tid på hela projektet: 2 timmar på kod och 10 min att förstå problemet. 
Det medgföljer även en video där den visar hur jag implementerar/skriver koden.  länken till videon: https://clipchamp.com/watch/QcdspFPDDaE

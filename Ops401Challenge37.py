#!/usr/bin/env python3
# Script Name:                 code challenge 37
# Author:                       Robert Gillespie
# Date of latest revision:      8/29/2023
# # Purpose:
#!/usr/bin/env python3


import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster():
    print('''
                  .---. .---.
                 :     : o   :    me want cookie!
             _..-:   o :     :-.._    /
         .-''  '  `---' `---' "   ``-.
       .'   "   '  "  .    "  . '  "  `.
      :   '.---.,,.,...,.,.,.,..---.  ' ;
      `. " `.                     .' " .'
       `.  '`.                   .' ' .'
        `.    `-._           _.-' "  .'  .----.
          `. "    '"--...--"'  . ' .'  .'  o   `.

            ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive a HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# Generate a .html file to capture the contents of the HTTP response
with open("response_page.html", "w") as html_file:
    html_file.write(response_with_cookie.text)

# Open the HTML file with the default system browser
webbrowser.open("response_page.html", new=2)  # The "new=2" parameter opens in a new tab/window

# Stretch Goal
def give_cookie_monster_hands():
    print('''
       ,,,,,,,,,,,
     ,;;%%%%%%%;,
   ,;;%%;;;;;;;;%%;,
  ,;%;;;;;%%%%%;;;;%;,
 ,;%;;;;;%%   %%;;;;;;%,
 ;%;;;;;;%     %;;;;;;;%;
 ;;;;;;;;       ;;;;;;;;;
 ;;;;;;;;       ;;;;;;;;;
 ;%;;;;;;%     %;;;;;;;%;
 `;%;;;;;%%   %%;;;;;;%;
  `;%;;;;;%%%%%;;;;;;%;
   `;;%%;;;;;;;;%%;;;
     `;;%%%%%%%;;
       `,,,,,,,,,
''')

give_cookie_monster_hands()
 
#Assisted with Chatgpt
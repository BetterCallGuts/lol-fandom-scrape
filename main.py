import requests
from bs4 import BeautifulSoup
import sys
import colorama

# champion-grid
url = "https://leagueoflegends.fandom.com/wiki/"
print("Getting champs Data ...")
res = requests.get(f"{url}League_of_Legends_Wiki")
src = res.content
soup= BeautifulSoup(src, "lxml")
#  empty lists
LIs         = []
champs_name = []
# search
champions = soup.find("div", {"id" : "champion-grid"})
champions =  champions.find_all("li")
for i in champions:
  LIs.append(i.find("a"))
  
  

for i in LIs:
  champs_name.append(str(i).split("wiki/")[1].split("/LoL")[0].lower())
  # print("\n\n\n")
  
# print(len(champs_name))


# The CLi Itself
program = True

while program:
  
  search   = input("What champ do you want('ex' to exit):")

  if search == "ex":
    program = False
    break

  elif search.lower() in champs_name:
    
    # The Program
    counter  = 1
    res      = requests.get(f"{url}{search.lower()}/LoL")
    src      = res.content
    soup     = BeautifulSoup(src, "lxml")

    abilities= soup.find_all("div", {"class" : "ability-info-container"})

    for i in abilities:
      title   = i.find("span", {"class" : "mw-headline"})
      content = i.find("div", {'style': "width:100%; display:grid; grid-template-columns: 78px 3fr 1.4fr; row-gap: 0.5em;"})
      content = content.find_all("p")
      if counter == 1:
        ab_name = "Passive"
      elif counter == 2:
        ab_name = "Q"
      
      elif counter == 3:
        ab_name = "W"
      
      elif counter == 4:
        ab_name = "E"
      else:
        ab_name = "R"
      # print("_"*40)
      print(colorama.Back.LIGHTCYAN_EX, colorama.Fore.BLACK ,f"{title.text}    {ab_name}", colorama.Back.RESET , colorama.Fore.RESET)
      # print("*"*10)
      for l in content:
        print(colorama.Back.LIGHTMAGENTA_EX, colorama.Fore.BLACK , l.text, colorama.Back.RESET , colorama.Fore.RESET)
      # print("_"*40)
      # print(content.text.strip(" ").strip("\n"))
      # print("_"* 40)
      counter += 1
    
  else:
    print("PLZ Enter a valid Champ name!")


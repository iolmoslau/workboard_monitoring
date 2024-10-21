import requests
from bs4 import BeautifulSoup

session  = requests.Session()

# creating a session
login_url = "https://bc35.atrieveerp.com/authenticationservice-Burnaby/Account/Login?ReturnUrl=%2Fauthenticationservice-Burnaby%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Ddotnetportalclient%26redirect_uri%3Dhttps%253A%252F%252Fbc35.atrieveerp.com%252Fburnaby%252Fpublic%252FExternalLogin.aspx%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520profile%2520offline_access%26state%3DNjM4NjQ4NzYwMTYxNTg2OTA4MjI3NzA2Njg3%26responseMode%3Dfragment%26nonce%3DNjM4NjQ4NzYwMTYxNTg2OTA4MjI3NzA2Njg3"

# access login page
response = session.get(login_url)

#extract token:
soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('input', {'name': '__RequestVerificationToken'})['value']
return_url = soup.find('input',{'name':'ReturnUrl'})['value']

#definind log in credentials and token
payload = {
    "Username":"E22438",
    "Password":"******",
    "__RequestVerificationToken":token,
    "ReturnUrl":return_url}

#logging in

login_response = session.post(login_url,data = payload,allow_redirects = True)

#check if login was successful:

if login_response.ok:
    
    print("Login successful!")

else:
    print("Login not successful")
    


workboard_url = "https://bc35.atrieveerp.com/burnaby/servlet/Broker?env=ads&template=ads.JobShop1.xml"

workboard_response = session.get(workboard_url)

with open("workboard_output.html", "w", encoding="utf-8") as file:
    file.write(workboard_response.text)


# menu_url = "https://bc35.atrieveerp.com/burnaby/servlet/Broker"

# menu_response = session.get(menu_url)

# soup = BeautifulSoup(menu_response.text,'lxml')

# workboard_link = soup.find('a',{'id':'workboard-34'})


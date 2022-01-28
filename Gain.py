import requests

print(""" _____                                            
|_   _|                                           
  | | _ __   ___ _ __ ___  __ _ ___  ___          
  | || '_ \ / __| '__/ _ \/ _` / __|/ _ \         
 _| || | | | (__| | |  __/ (_| \__ \  __/         
 \___/_| |_|\___|_|  \___|\__,_|___/\___|         
                                                  
              Telegram Ch :- @Berlin_Tools
              Instagram :- @Hmd787800                                  
          __      _ _                             
         / _|    | | |                            
        | |_ ___ | | | _____      _____ _ __ ___  
        |  _/ _ \| | |/ _ \ \ /\ / / _ \ '__/ __| 
        | || (_) | | | (_) \ V  V /  __/ |  \__ \ 
        |_| \___/|_|_|\___/ \_/\_/ \___|_|  |___/ 
                                                  
                                                 """)
target = input('- Enter UserName > ')
headgetID = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'mid=YbysKAALAAGnsY7iGX9WEyOe8AaT; ig_did=EF4C2AFE-037F-4E1B-A158-C08728818708; ig_nrcb=1; ds_user_id=50787014839; csrftoken=UToGyPsqeTDVOZ7RVJNpWfFjMVUkdHn3; sessionid=50787014839%3Ajhdr3dv7iFRPYb%3A21; rur="RVA\05450787014839\0541672416874:01f7f7d72f9624862a45b7c7ed6092af21b367cd6ec4806e50222845967307214f80dac8"',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
    }
    
getid = requests.get(f'https://www.instagram.com/{target}/?__a=1',headers=headgetID,data={'__a': '1'}).json()
id = str(getid['logging_page_id']).split("_")[1]

print(f'- Done Grabbed Id  > {id}')

url = f"http://13.87.68.101/technical-deb/?uname={id}&submit=submit"    

head = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip,deflate,br',
    'accept-language':'en-US,en;q=0.9,ar;q=0.8',
    'content-length':'0',
    'content-type':'application/x-www-form-urlencoded',
    'referer':'http://13.87.68.101/technical-deb/',
    'sec-fetch-site':'same-origin',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73" ,
}
while True:
    req = requests.get(url,headers=head).status_code
  
    if req == 200:
        print('- Done Increase Followers > 50 ')
    else:
        print('- Erorr Increase Followers ')

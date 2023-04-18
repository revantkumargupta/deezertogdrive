# deezertogdrivebot
Telegram Deezer Bot



clone this repo or dow whatever and make this repo private 


Install the required packages using "pip install -r requirements.txt"

  
  
 
 do this thing in keys.py  
 
 
 
api_id = "<your_telegram_api_id>"

api_hash = "<your_telegram_api_hash>"

bot_token = "<your_telegram_bot_token>"

service_file = "client_secrets.json"     no need to rename this thing,leave as it is

db_url = "<your_mongodb_connection_string>"

deezer_api = "<your_deezer_api_key>"

Run the bot using python main.py.






deezer api means deezer ARL 


for db url you can follow this step 
first create account in mongo db
then assign or create a user in it 
https://photos.app.goo.gl/5CGHS4r26FUXmsjw9






for service account

remove already present client_secrets.json
go to google cloud console
create a service account and download that service account file in json format
rename that json file to "client_secrets.json"
upload that client_secrets.json file to your repository
don't forget to add your service account in your shared drive with content manager/manager permissions 



for google drive support
go to line 124 ,you will se id ,that is your shared drive/teamdrive id 
https://photos.app.goo.gl/jMYVjNqeXf3Dds7n9
for eg i got this link https://drive.google.com/drive/folders/0AMjb_3kLleNAUk9PVA
my teamdrive /shared drive is 0AMjb_3kLleNAUk9PVA
so just replace this string "0AMjb_3kLleNAUk9PVA" in that code
https://photos.app.goo.gl/s2qNnFqwSJpL3ci96




and in line 125 you have to get folder id means create any folder and get id of that folder 
for eg i got this link https://drive.google.com/drive/folders/1yltuyFBLxUPmwVPDd5tlx0zL4z0BKr8A
so my folder id is 1yltuyFBLxUPmwVPDd5tlx0zL4z0BKr8A
just replace with your folder id in that line of code 

https://photos.app.goo.gl/1wAnxqs3hD85YxCS6





for index link
go to line 131 
copy index link of your folder from which you have got id 
and replace with mine

https://photos.app.goo.gl/wihavxbBJgKgtSN87






now do same thing for line 169 ,170,176,192,193,199,260,261,267,305,306,312,328,329,335

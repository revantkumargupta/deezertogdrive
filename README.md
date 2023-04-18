# deezertogdrivebot
Telegram Deezer Bot:

Clone this repo or do whatever you want and make this repo private.

Install the required packages using "pip install -r requirements.txt".

Do this thing in keys.py:

api_id = "<your_telegram_api_id>"

api_hash = "<your_telegram_api_hash>"

bot_token = "<your_telegram_bot_token>"

service_file = "client_secrets.json" (no need to rename this thing, leave as it is)

db_url = "<your_mongodb_connection_string>"

deezer_api = "<your_deezer_api_key>" (deezer API means Deezer ARL)

Run the bot using python main.py.

For the db URL, you can follow these steps: First, create an account in MongoDB, then assign or create a user in it.
https://photos.app.goo.gl/5CGHS4r26FUXmsjw9

For the service account:

Remove the already present client_secrets.json. Go to the Google Cloud Console, create a service account, and download that service account file in JSON format. Rename that JSON file to "client_secrets.json". Upload that client_secrets.json file to your repository. Don't forget to add your service account in your shared drive with content manager/manager permissions.

For Google Drive support,
go to line 124. You will see an ID, that is your shared drive/team drive ID.
https://photos.app.goo.gl/jMYVjNqeXf3Dds7n9

For example, I got this link https://drive.google.com/drive/folders/0AMjb_3kLleNAUk9PVA. My team drive/shared drive is 0AMjb_3kLleNAUk9PVA. So, just replace this string "0AMjb_3kLleNAUk9PVA" in that code. For example, if you want to replace the team drive ID with "abcd1234," replace the original ID with "abcd1234."
https://photos.app.goo.gl/s2qNnFqwSJpL3ci96

In line 125, you have to get the folder ID, which means creating any folder and getting the ID of that folder. For example, I got this link https://drive.google.com/drive/folders/1yltuyFBLxUPmwVPDd5tlx0zL4z0BKr8A, so my folder ID is 1yltuyFBLxUPmwVPDd5tlx0zL4z0BKr8A. Just replace it with your folder ID in that line of code.

https://photos.app.goo.gl/1wAnxqs3hD85YxCS6

For the index link, go to line 131, copy the index link of your folder from which you have got the ID, and replace it with mine.
https://photos.app.goo.gl/wihavxbBJgKgtSN87

Now do the same thing for lines 169, 170, 176, 192, 193, 199, 260, 261, 267, 305, 306, 312, 328, 329, and 335.

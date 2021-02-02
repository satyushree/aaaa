from tobrot.sample_config import Config

#read readme too before filling these stuffs

class Config(Config):
    TG_BOT_TOKEN= "1641612309:AAGPMdSG76CTmXo7QQD9S0DXTXeeq54foMA" #imp
    APP_ID = 1309280 #imp
    API_HASH = "af327dd857e0e65f80fefcf6d0af4afd" #imp
    AUTH_CHANNEL = [-1001454182978, 1087968824] #imp replace your_id with your id from telegram or delete
    INDEX_LINK = "https://bold-scene-480b.satyu.workers.dev"
    GLEECH_COMMAND = "gleech@MyTorrentDrive_BOT"
    YTDL_COMMAND = 'ytdl@MyTorrentDrive_BOT'
    TELEGRAM_LEECH_COMMAND_G = "tleech@MyTorrentDrive_BOT"
    CLONE_COMMAND_G = "gclone@MyTorrentDrive_BOT"
    PYTDL_COMMAND_G = "pytdl@MyTorrentDrive_BOT"
    DESTINATION_FOLDER = "TorrentLeech-Gdrive"
    LEECH_COMMAND = "leech@MyTorrentDrive_BOT"
    RCLONE_CONFIG = """type = drive
scope = drive
root_folder_id = 12qn5SetJIfHoynqKi2hZPyIZfNfyI5d-
token = {"access_token":"ya29.a0AfH6SMAc6ULOacGMj_Mb23RM0UyvIukd3G0YRRPlIP4PPmon-HzDZQbRF2Rltd4N-jxIrf205sOnnqNRhXZ9_JsK1XeeRkEN8atiw4qAvYgcrEMChDAe28hozu5faCwZlJe0OVFqQ7rK-F41zGT2HqAjsHEKLeUoZ1IYtTgxAkA","token_type":"Bearer","refresh_token":"1//0gZPPb-gbNfvACgYIARAAGBASNwF-L9IrOFk3k6aawk9ScEyIOw8ow5nh8ZT2AFd0zHHykDpozCR60UF4qlEyQSPw2fDCTV22bd4","expiry":"2021-02-02T18:03:44.3770858+05:30"}
team_drive = 0AKZow1MUSd9aUk9PVA
client_id = 703529436612-guk8u72akf33ln7dvifdpcadtibvb62t.apps.googleusercontent.com
client_secret = 0FoKBycxKRWeaDwlsuOUXAvR"""
    #put your config(replacing new lines with \n) in triple quote like above: """<your one liner config>"""

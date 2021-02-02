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
root_folder_id =
token = {"access_token":"ya29.A0AfH6SMCvaLMWW6iZacHYL43lGmR9QlSDfKXEFqCq52KTFmogEsc6EjFwcFIesczqQQNF52H9WVi1jGZgDWJF3R_19Rs-_hAcy7YeXIN-Tl3SNLB_dx4VmVPrGfvSJg3iACECKghtI4XTDBFZwtX8XD6esv9r","token_type":"Bearer","refresh_token":"1//0gdQV7KM1nnJrCgYIARAAGBASNwF-L9IralYTN1yMMrIcDDtrYLc4rBhVWENhbR-qJQxa1v0DzgfmUkYBtAW4PiZYoMqGx_IMObc","expiry":"2021-02-02T10:59:43.6364416+05:30"}
team_drive = 0AKZow1MUSd9aUk9PVA """
    #put your config(replacing new lines with \n) in triple quote like above: """<your one liner config>"""

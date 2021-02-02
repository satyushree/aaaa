from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1641612309:AAGPMdSG76CTmXo7QQD9S0DXTXeeq54foMA"
    APP_ID = 1309280
    API_HASH = "af327dd857e0e65f80fefcf6d0af4afd"
    OWNER_ID = 1243382770
    AUTH_CHANNEL = [-1001454182978]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
scope = drive
root_folder_id =
token = {"access_token":"ya29.A0AfH6SMCvaLMWW6iZacHYL43lGmR9QlSDfKXEFqCq52KTFmogEsc6EjFwcFIesczqQQNF52H9WVi1jGZgDWJF3R_19Rs-_hAcy7YeXIN-Tl3SNLB_dx4VmVPrGfvSJg3iACECKghtI4XTDBFZwtX8XD6esv9r","token_type":"Bearer","refresh_token":"1//0gdQV7KM1nnJrCgYIARAAGBASNwF-L9IralYTN1yMMrIcDDtrYLc4rBhVWENhbR-qJQxa1v0DzgfmUkYBtAW4PiZYoMqGx_IMObc","expiry":"2021-02-02T10:59:43.6364416+05:30"}
team_drive = 0AKZow1MUSd9aUk9PVA
"""

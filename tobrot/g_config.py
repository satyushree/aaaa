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
root_folder_id = 12qn5SetJIfHoynqKi2hZPyIZfNfyI5d-
token = {"access_token":"ya29.a0AfH6SMAc6ULOacGMj_Mb23RM0UyvIukd3G0YRRPlIP4PPmon-HzDZQbRF2Rltd4N-jxIrf205sOnnqNRhXZ9_JsK1XeeRkEN8atiw4qAvYgcrEMChDAe28hozu5faCwZlJe0OVFqQ7rK-F41zGT2HqAjsHEKLeUoZ1IYtTgxAkA","token_type":"Bearer","refresh_token":"1//0gZPPb-gbNfvACgYIARAAGBASNwF-L9IrOFk3k6aawk9ScEyIOw8ow5nh8ZT2AFd0zHHykDpozCR60UF4qlEyQSPw2fDCTV22bd4","expiry":"2021-02-02T18:03:44.3770858+05:30"}
team_drive = 0AKZow1MUSd9aUk9PVA
client_id = 703529436612-guk8u72akf33ln7dvifdpcadtibvb62t.apps.googleusercontent.com
client_secret = 0FoKBycxKRWeaDwlsuOUXAvR
"""

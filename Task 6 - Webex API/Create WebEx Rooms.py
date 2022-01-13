import requests 
import json

# Original file (C) Yvan Rooseleer

access_token = "MDg0MzE4NzgtZWIxMy00YzQyLThhNDUtMjRiMjY4YWY4YTc1ZjhkZWZiYzYtNTA4_PF84_consumer"

groups_struc = {
 "groups": [
      { "group": { "group_id": "E1" , "group_name": "netacad_devasc_skills_DdV" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Diederik", "email": "webex@diederik.nl"},
                     {"person_id": "P-2" , "person_name": "Marcus", "email": "yvan.rooseleer@biasc.be>"}
                     ]
                 }
      }
   ]
}

url = 'https://api.ciscospark.com/v1/rooms'

headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }

def CreateSpace():
    for rec in groups_struc["groups"]:
        create_group_name = rec["group"]["group_name"]
        print("Creating ... " + create_group_name)
        payload_space={"title": create_group_name}
        res_space = requests.post(url, headers=headers, json=payload_space)

        NEW_SPACE_ID = res_space.json()["id"]
        for mbr in rec["group"]["members"]:
            room_id = NEW_SPACE_ID
            person_email = mbr["email"] 
            url2 = 'https://api.ciscospark.com/v1/memberships'
            payload_member = {'roomId': room_id, 'personEmail': person_email}
            res_member = requests.post(url2, headers=headers, json=payload_member)
        return res_space

def FindRoom():
    webex_rooms = requests.get('https://api.ciscospark.com/v1/rooms', headers=headers)
    print(f"* {webex_rooms=}")
    webex_rooms_json = webex_rooms.json()
    webex_room_id = None
    for i in webex_rooms_json["items"]:
        if i["title"] == "netacad_devasc_skills_DdV":
            print("- found room",i["title"],"its id is",i["id"])
            webex_room_id = i["id"]
            return(webex_room_id)

CreateSpace()
webex_room_id=FindRoom()

webex_message_json = {
    "roomId": webex_room_id,
    "text": "Here are my screenshots of netacad-devasc skills-based exam"
    }
messageUrl="https://api.ciscospark.com/v1/messages"
webex_session = requests.Session()
webex_headers={"Authorization": "Bearer " + access_token}
webex_session.headers.update(webex_headers)
webex_message = webex_session.post(url=messageUrl,json=webex_message_json)
print(f"* {webex_message=}")
print(f"* {webex_message.json()=}")



import requests 
import json

# Original file (C) Yvan Rooseleer

access_token = "OGU4ZmQ1MDYtMzYxMS00ODBhLWI2NzMtZmRlNDVlY2E2YzY4ZjVhZDYyNTMtZjQ1_PF84_consumer"

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


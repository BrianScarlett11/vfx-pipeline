import os
import datetime

for root, dirs, files in os.walk('Assets'):

    ver_list=[]

    if files:
        typename = root.split("\\")
        asset_type = typename[1]
        asset_name = typename[2]
       
        for version_number in files:
            first_split = version_number.split(f'{asset_name}_v')
            second_split = first_split[1].split(".usda")

            current_version = float(second_split[0])

            ver_list.append(current_version)
        
        date_created_unix = os.path.getctime(f"{root}\\{version_number}")
        timestamp = datetime.datetime.fromtimestamp(date_created_unix)
        date_created = (timestamp.strftime('%d-%m-%Y  %H:%M:%S'))
        print(f"Name: {asset_name} | Type: {asset_type} | Version: {ver_list} | Date Created: {date_created}")
      
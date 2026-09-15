import os
import datetime

def get_assets():

    assets = []

    for root, dirs, files in os.walk(os.path.join(os.path.dirname(__file__), "Assets")):


        if files:
            typename = root.split("/")
            asset_type = typename[-2]
            asset_name = typename[-1]
       
            for version_number in files:
                if not version_number.endswith(".usda"):
                    continue
    
                first_split = version_number.split(f'{asset_name}_v')
                second_split = first_split[1].split(".usda")

                current_version = float(second_split[0])

                date_created_unix = os.path.getctime(f"{root}/{version_number}")
                timestamp = datetime.datetime.fromtimestamp(date_created_unix)
                date_created = (timestamp.strftime('%d-%m-%Y  %H:%M:%S'))

                assets.append({"Name": asset_name, "Type": asset_type, "Version": current_version, "Date": date_created})
        
        


    
    return assets 
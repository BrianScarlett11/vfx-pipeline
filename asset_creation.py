import sys
import os

from pxr import Sdf, Usd, UsdGeom

#make a file directory of the asset
def create_asset(asset_name, asset_type, asset_LOD):
    directory_name = "Assets"
    nested_directory = (f"{directory_name}/{asset_type}/{asset_name}")

    try:
        os.makedirs(nested_directory)
        print(f"Nested directories '{nested_directory}' created successfully.")
    except FileExistsError:
        print(f"One or more directories in '{nested_directory}' already exist.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{nested_directory}'.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

    dir_list = os.listdir(nested_directory)
    ver_list = []

#create a new USD file in the directory
    if len(dir_list) == 0:
        final_version = 1.0

        stage = Usd.Stage.CreateNew(f"{nested_directory}/{asset_name}_v1.0.usda")

    else:
        for version_number in dir_list:
            first_split = version_number.split(f'{asset_name}_v')
            second_split = first_split[1].split(".usda")

            current_version = float(second_split[0])

            ver_list.append(current_version)
    
        next_version = max(ver_list)+1

        final_version = next_version

        stage = Usd.Stage.CreateNew(f"{nested_directory}/{asset_name}_v{next_version}.usda")

    stage.SetMetadata("comment", f"VFX Asset: {asset_name}")

#create a simple object in that file
    xform = UsdGeom.Xform.Define(stage, f"/Assets/{asset_type}/{asset_name}")

    prim = xform.GetPrim()
    prim.SetMetadata("kind", "component")
    prim.CreateAttribute("asset:version", Sdf.ValueTypeNames.String).Set(f"{final_version}")

#create Level of Detail variants
    variant_set = prim.GetVariantSets().AddVariantSet("LOD")

    #create dictionary of LOD variants and its subdivisionlevel
    lod_variants = {
        "1_high": 4,
        "2_medium": 2,
        "3_low": 0
    }

    for key, value in lod_variants.items():
        variant_set.AddVariant(key)
        variant_set.SetVariantSelection(key)
        with variant_set.GetVariantEditContext():
            prim.CreateAttribute("lod:subdivisionLevel", Sdf.ValueTypeNames.Int).Set(value)

#convert LOD selection into the formatted variants
    if asset_LOD == "High":
        LOD_key = "1_high"
    elif asset_LOD == "Medium":
        LOD_key = "2_medium"
    else:
        LOD_key = "3_low"
        

    variant_set.SetVariantSelection(f"{LOD_key}")
    
  

#save it
    stage.GetRootLayer().Save()

    print("Asset created successfully")
    print(f"Open {nested_directory}/{asset_name}.usda to see what's inside")
# Automation (ArcGIS API for Python) means to add content to Portal Group.
# Intended for use with Sites creation and testing.

########## ########## ##########

# Imports
from arcgis.gis import GIS

########## ########## ##########

# PARAMS

# Portal ID of Group to which items should be added
group_id = "1f8060c34d5940419e3a33235c2eb752"

# Max items to look through in Portal to attempt adding to Group
max_srch = 250

########## ########## ##########

# Login with Pro
gis = GIS("pro", verify_cert = False)

# Get Group
group_itm = gis.groups.get(group_id)

# Get Portal content and loop through
itms = gis.content.search(query="*", max_items=max_srch)

# Loop through items from Portal content search
for itm in itms:
    
    # Try adding each item to group; if error, print and move on
    try:
        itm.share(groups=group_itm)
    except Exception as e:
        print(e)
    else:
        print(f"Succeeded sharing item {itm.title}!")

# Automation (ArcGIS API for Python) means to add tags to Portal items.
# Intended for use with Sites creation and testing.

########## ########## ##########

# Imports
from arcgis.gis import GIS

########## ########## ##########

# PARAMS

# New tag(s) to add to items as string.
# Multiple tags can be either comma separated string or list.
new_tags = # Example list of tags: ["naip", "imagery"]

# Max items to look through in Portal to attempt adding tags
max_srch = 1000

########## ########## ##########

# Login with Pro
gis = GIS("pro", verify_cert = False)

# Get Portal content and loop through
itms = gis.content.search(query="*", max_items=max_srch)

# Loop through items from Portal content search
for itm in itms:
    
    # Ignore items that don't have "NAIP" in the title
    # Prefer this over content search query since results
    # are more concrete; query is more fuzzy per esri docs
    if not "NAIP" in itm.title.upper():
        continue
    
    try:
        itm.update(item_properties={"tags": new_tags})
    except Exception as e:
        print(e)
    else:
        print(f"Successfully added tags to item {itm.title}")
    

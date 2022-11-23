# Automation (ArcGIS API for Python) means to add content to Portal Group.
# Intended for use with Sites creation and testing.

########## ########## ##########

# Imports
from arcgis.gis import GIS

########## ########## ##########

# Login with Pro
gis = GIS("pro", verify_cert = False)

# Get the JSON categories for the org
cat_schema = gis.admin.category_schema

cats = cat_schema.schema["categorySchema"][0]["categories"]

# Make list of just the cat titles
# Note that this does NOT include subcategories! Would need additional work here
cat_titles = [c["title"] for c in cats]

# Print titles to have something to choose from when assigning below
for ct in cat_titles:
    print(ct)

########## ########## ########## ########## ########## ##########

# If running in an ArcGIS Notebook, paste the code below in a new block
# Run the first block (above) to get the category titles,
# Then choose category/ies and add as params in 2nd block below

########## ########## ########## ########## ########## ##########

# PARAMS

# Max items to look through in Portal to attempt adding to Group
max_srch = 5000

assign_cat = # Sample category string/list: ["Imagery, basemaps, and Earth cover"]

########## ########## ##########

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
        cat_schema.categorize_item(itm, assign_cat)
    except Exception as e:
        print(e)
    else:
        print(f"Successfully applied category to itm {itm.title}")

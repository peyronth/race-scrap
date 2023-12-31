import os
from scriptlist import supportedWebsites as supportedWebsites

testResults = {}

# For each website, test the script with the exampleUrl and check if an excel file is created at returned path
for webSiteName in supportedWebsites:
    print("Testing " + webSiteName + "...")
    currentWebsite = webSiteName
    currentUrl = supportedWebsites[currentWebsite]["exampleUrl"]
    # Launch the script
    returnedPaths = supportedWebsites[currentWebsite]["script"](currentUrl)
    # Check if the file is created
    testResult = False
    for path in returnedPaths:
        if os.path.isfile(path):
            testResult = True
        else:
            testResult = False
            break
    testResults[currentWebsite] = testResult


# Save results as markdown table in versions/compatibility.md and rename actual compatibility.md
import datetime
import shutil
import pandas as pd

# Create a dataframe with the test results
filename = "versions/compatibility.md"
df = pd.DataFrame(testResults.items(), columns=['Website', 'Compatibility'])
# Convert boolean to string and replace true by U+2705 and false by U+274C
df['Compatibility'] = df['Compatibility'].replace({True: ':white_check_mark:', False: ':x:'})
# Sort by website name
df = df.sort_values(by=['Website'])
# Convert to markdown table
table = df.to_markdown(index=False)
# Rename actual compatibility.md
if os.path.isfile(filename):
    shutil.move(filename, "versions/compatibility_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".md")
# Save the table in versions/compatibility.md
with open(filename, "w") as file:
    file.write(table)
   


#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Sophia Bryson (sab159@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Solicit search date from user
user_date = input("Enter date (M/D/YYYY) to search for Sara: ")

# Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

# Create a file object from the file
file_object = open(file_name, 'r') #read only

# Read contents of data file into a list
line_list = file_object.readlines()

# Close the file (it's saved into the list)
file_object.close()

# Create to empty dictionary objects
date_dict = {}
coord_dict = {} 

# Iterate through all lines in the linelist
for lineString in line_list: #inserts value of first line into variable 'lineString'
    
    # if lineString[0] == "#" or lineString[0] == "u": continue #skips lines that are commented (header)
    if lineString[0] in ("#", "u"): continue #same as above, but using membership rules
    
    # now pull out specific items from that string - split into data items
    lineData = lineString.split() #creates list object with 18 items
    
    # then can use indices to access desired items from each row - extract items into variables
    # records (columns) of interest: UID, date, location class (quality), lat & long
    record_id = lineData[0] #record ID (this is a string, not a number)
    obs_date = lineData[2]  #date of observation
    obs_lc = lineData[4]    #observation location class (quality marker)
    obs_lat = lineData[6]   #observed latitude
    obs_long = lineData[7]  #observed longitude

    # skip if location classification value is unacceptable
    if obs_lc not in ("1", "2", "3"): #acceptable values
        continue                      #skips to next iteration if value is not among acceptable values
    
    #print location of Sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, long:{obs_long} on {obs_date}")
    
    #add items to dictionaries
    date_dict[record_id] = obs_date #UID used as key, date passed as value 
    coord_dict[record_id] = (obs_lat, obs_long) #UID as key, lat/long pair as value

#Create empty list to store keys corresponding with user date
matching_keys=[]   
    
#Loop through items in the date_dict, and collect keys for matching ones
for date_item in date_dict.items():
    
    #Get the key and date components of dictionary item
    the_key, the_date = date_item #sepatates tuple into two values
    
    #Check if the date matches the user-specified date
    if the_date == user_date:
        #if so, add key to the list
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching_keys
for matching_key in matching_keys: 
    obs_lat, obs_long = coord_dict[matching_key] #split tuple into two variables
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat}, lon:{obs_long} on {user_date}")

    



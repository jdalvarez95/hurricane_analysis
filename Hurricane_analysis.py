#!/usr/bin/env python
# coding: utf-8

# In[1]:


# %load "~/Notebooks/hurricane_analysis_starting/script.py"
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[2]:


#Update damages function
def update_damages(lst_damages):
    upd_damages_lst = []
    for figure in lst_damages:
        if figure == "Damages not recorded":
            upd_damages_lst.append(figure)
        elif figure[-1] == "B":
            new_figure = float(figure.replace("B", ""))
            upd_figure = new_figure*1000000000
            upd_damages_lst.append(upd_figure)
        elif figure[-1] == "M":
            new_figure = float(figure.replace("M", ""))
            upd_figure = new_figure*1000000
            upd_damages_lst.append(upd_figure)

    return upd_damages_lst
new_damages = update_damages(damages)


# In[3]:


#Hurricane Dictionary
hurr_dict = {}
for name in names:
    i = names.index(name)
    hurr_dict[name] ={"Name":name, "Month":months[i], "Year":years[i], "Max Sustained Wind":max_sustained_winds[i],                      "Areas Affected":areas_affected[i], "Damage":new_damages[i], "Deaths":deaths[i]}


# In[4]:


#Construct dictionary by year function

dic_year = {}
for hurricane in hurr_dict:
    current_year = hurr_dict[hurricane]["Year"]
    current_cane = hurr_dict[hurricane]
    #print(current_cane)
    if not current_year in dic_year.keys():
        dic_year[current_year] = [current_cane]
    else: 
        dic_year[current_year].append(current_cane)
print(dic_year[1932])


# In[5]:


# Count affected areas function here:
aff_areas = {}
for name in names:
    for area in hurr_dict[name]["Areas Affected"]:
        if not area in aff_areas.keys():
            aff_areas[area] = 1
        else:
            aff_areas[area] += 1

print(aff_areas)


# In[6]:


# Find most affected area function here:
def most_aff_area(aff_areas):
    curr_count = 0
    most_aff = "The most hitted areas are: "
    for area in aff_areas:
        value = aff_areas[area]
        if value > curr_count:
            curr_count = value
            most_aff += area +" with " + str(curr_count) + " hurricanes since 1924"
        elif value == curr_count:
            most_aff += " and " + area
    return most_aff

print(most_aff_area(aff_areas))


# In[7]:


# Greatest number of deaths function here:
hurr_most_deaths = ""
def most_deaths(dic_hurr):
    num_deaths = 0
    for hurricane in dic_hurr:
        #print(hurricane)
        if dic_hurr[hurricane]["Deaths"] > num_deaths:
            hurr_most_deaths = hurricane
            num_deaths = dic_hurr[hurricane]["Deaths"]
            
    return [hurr_most_deaths, num_deaths]
print(most_deaths(hurr_dict))
    


# In[8]:


# Categorization by mortality here:
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
def cat_mort(hurricanes):
    mort_scale_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
    
    for hurricane in hurricanes:
        #print(hurricanes[hurricane]["Deaths"])
        if hurricanes[hurricane]["Deaths"] == mortality_scale[0]:
            mort_scale_dict[0].append(hurricane)
        elif hurricanes[hurricane]["Deaths"] > mortality_scale[0] and hurricanes[hurricane]["Deaths"] <= mortality_scale[1]:
            mort_scale_dict[1].append(hurricane)
        elif hurricanes[hurricane]["Deaths"] > mortality_scale[1] and hurricanes[hurricane]["Deaths"] <= mortality_scale[2]:
            mort_scale_dict[2].append(hurricane)
        elif hurricanes[hurricane]["Deaths"] > mortality_scale[2] and hurricanes[hurricane]["Deaths"] <= mortality_scale[3]:
            mort_scale_dict[3].append(hurricane)
        elif hurricanes[hurricane]["Deaths"] > mortality_scale[3]:
            mort_scale_dict[3].append(hurricane)
    return mort_scale_dict
#print(hurr_dict)       
print(cat_mort(hurr_dict))


# In[9]:


# Greatest damage function:
def great_damage(hurricanes):
    great_cost = 0
    hurr_great_damages = ""
    for hurricane in hurricanes:
        if hurricanes[hurricane]["Damage"] == "Damages not recorded":
            continue
        elif hurricanes[hurricane]["Damage"] > great_cost:  
            great_cost = hurricanes[hurricane]["Damage"]
            hurr_great_damages = hurricanes[hurricane]["Name"]
            
    return "The hurricane with the greatest damages was " + hurr_great_damages + ", it cost approximately " + str(great_cost) + " dollars."
print(great_damage(hurr_dict))


# In[10]:


# Categorization by damage:
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
def cat_dam(hurricanes):
    dam_scale_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
    
    for hurricane in hurricanes:
        #print(hurricanes[hurricane]["Deaths"])
        if hurricanes[hurricane]["Damage"] == "Damages not recorded":
            continue
        elif hurricanes[hurricane]["Damage"] == damage_scale[0]:
            dam_scale_dict[0].append(hurricane)
        elif hurricanes[hurricane]["Damage"] > damage_scale[0] and hurricanes[hurricane]["Damage"] <= damage_scale[1]:
            dam_scale_dict[1].append(hurricane)
        elif hurricanes[hurricane]["Damage"] > damage_scale[1] and hurricanes[hurricane]["Damage"] <= damage_scale[2]:
            dam_scale_dict[2].append(hurricane)
        elif hurricanes[hurricane]["Damage"] > damage_scale[2] and hurricanes[hurricane]["Damage"] <= damage_scale[3]:
            dam_scale_dict[3].append(hurricane)
        elif hurricanes[hurricane]["Damage"] > damage_scale[3]:
            dam_scale_dict[3].append(hurricane)
    return dam_scale_dict
#print(hurr_dict)       
print(cat_dam(hurr_dict))


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

# write your update damages function here:

def updated_damages(damage_list):
    new_damage = []
    for i in damage_list:
        if i == 'Damages not recorded':
            new_damage.append(i)
        elif i[-1] == 'B':
            new_damage.append(float(i[:-1])*1000000000)
        else: # la otra es M, si se agregan datos hay que chequear acá
            new_damage.append(float(i[:-1])*1000000)
    return new_damage

new_damages = updated_damages(damages)
print(new_damages)

# write your construct hurricane dictionary function here:

def hurricane_dictionary(name_list,month_list,year_list,max_wind_list,areas_list,damage_list,death_list):
    hurri_dictionary = {}
    for i in range(len(name_list)):
        hurri_dictionary[name_list[i]] = {'Name': name_list[i], 
                                        'Month': month_list[i], 
                                        'Year': year_list[i], 
                                        'Max Sustained Wind': max_wind_list[i], 
                                        'Areas Affected': areas_list[i], 
                                        'Damage': damage_list[i], 
                                        'Deaths': death_list[i]}
    return hurri_dictionary

hurricanes_dict = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
print(hurricanes_dict)
print('.')
print('.')
print('.')
print('.')
# write your construct hurricane by year dictionary function here:

def hurricane_per_year(hurri_dictionary):
    dict_per_year = {}
    current_year = []
    aux = 0
    for key in hurri_dictionary:
        current_cane = []
        current_year_aux = hurri_dictionary[key]['Year']
        if not current_year_aux in current_year:
            current_year.append(current_year_aux)
            for k in hurri_dictionary:
                if (hurri_dictionary[k]['Year'] == current_year_aux):
                    current_cane.append(hurri_dictionary[k].copy())
            dict_per_year[current_year_aux] = current_cane
    return dict_per_year

print(hurricane_per_year(hurricanes_dict)[1932])
print('.')
print('.')
# write your count affected areas function here:

def count_affected_areas(hurri_dictionary):
    areas_aux = []
    list_num_of_times = []
    for key in hurri_dictionary:
        for l in range(len(hurri_dictionary[key].get('Areas Affected'))):
            if hurri_dictionary[key].get('Areas Affected')[l] in areas_aux:
                continue
            else:
                num_of_times = 0
                areas_aux.append(hurri_dictionary[key].get('Areas Affected')[l])
                for k in hurri_dictionary:
                    if hurri_dictionary[key].get('Areas Affected')[l] in hurri_dictionary[k].get('Areas Affected'):
                        num_of_times += 1
                list_num_of_times.append(num_of_times)
    dict_num_of_times = dict(zip(areas_aux, list_num_of_times))

    return dict_num_of_times

print(count_affected_areas(hurricanes_dict))

# write your find most affected area function here:
def area_most_affected(dict_num_of_times):
    maximo = 0
    key_aux = ''
    for k in dict_num_of_times:
        if dict_num_of_times.get(k) > maximo:
            maximo = dict_num_of_times.get(k)
            key_aux = k
    print('The area most affected by hurricanes is '+key_aux+', and it was affected '+str(maximo)+ ' times.')

    return key_aux, maximo

area_most_affected(count_affected_areas(hurricanes_dict))
# write your greatest number of deaths function here:
print('.')
print('.')
print('.')

def most_deadly_hurricane(hurri_dictionary):
    maximo = 0
    key_aux = ''
    for k in hurri_dictionary:
        if hurri_dictionary.get(k).get('Deaths') > maximo:
            maximo = hurri_dictionary.get(k).get('Deaths')
            key_aux = k
            print(k)
    print('The hurricane '+key_aux+' had the maximum number of deaths, taking the life of '+str(maximo)+ ' people.')
    return key_aux, maximo

most_deadly_hurricane(hurricanes_dict)
print('.')

# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortality(hurri_dictionary, mort_scale):

    rating = []
    hurri_aux = []
    for k in hurri_dictionary:
        if hurri_dictionary.get(k).get('Deaths') < mort_scale.get(1):
            rating.append(1)
            hurri_aux.append(k)
        elif hurri_dictionary.get(k).get('Deaths') < mort_scale.get(2):
            rating.append(2)
            hurri_aux.append(k)
        elif hurri_dictionary.get(k).get('Deaths') < mort_scale.get(3):
            rating.append(3)
            hurri_aux.append(k)
        elif hurri_dictionary.get(k).get('Deaths') < mort_scale.get(4):
            rating.append(4)
            hurri_aux.append(k)
        else:
            rating.append(5)
            hurri_aux.append(k)

    hurri_aux_rating_list = []
    for i in range(1,6):
        hurri_aux_rating = []
        for j, value in enumerate(rating):
            if value == i:
                hurri_aux_rating.append(hurri_aux[j])
        hurri_aux_rating_list.append(hurri_aux_rating)
    
    return dict(zip(range(1,6),hurri_aux_rating_list))

print('.')
print('.')
print(mortality(hurricanes_dict, mortality_scale))

# write your greatest damage function here:

def most_damage_hurricane(hurri_dictionary):
    maximo = 0
    key_aux = ''
    for k in hurri_dictionary:
        if hurri_dictionary.get(k).get('Damage') != 'Damages not recorded':
            if hurri_dictionary.get(k).get('Damage') > maximo:
                maximo = hurri_dictionary.get(k).get('Damage')
                key_aux = k
                print(k)
    print('The hurricane '+key_aux+' had the maximum damages value, about '+str(maximo)+ ' dollars.')
    return key_aux, maximo

most_damage_hurricane(hurricanes_dict)

# write your catgeorize by damage function here:

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_rating(hurri_dictionary, dam_scale):

    rating = []
    hurri_aux = []
    for k in hurri_dictionary:
        if hurri_dictionary.get(k).get('Damage') == 'Damages not recorded':
            rating.append(0)
            hurri_aux.append(k)
        elif hurri_dictionary.get(k).get('Damage') < dam_scale.get(1):
            rating.append(1)
            hurri_aux.append(k)
        elif hurri_dictionary.get(k).get('Damage') < dam_scale.get(2):
            rating.append(2)
            hurri_aux.append(k)
        elif hurri_dictionary.get(k).get('Damage') < dam_scale.get(3):
            rating.append(3)
            hurri_aux.append(k)
        elif hurri_dictionary.get(k).get('Damage') < dam_scale.get(4):
            rating.append(4)
            hurri_aux.append(k)
        else:
            rating.append(5)
            hurri_aux.append(k)

    hurri_aux_rating_list = []
    for i in range(6):
        hurri_aux_rating = []
        for j, value in enumerate(rating):
            if value == i:
                hurri_aux_rating.append(hurri_aux[j])
        hurri_aux_rating_list.append(hurri_aux_rating)
    
    return dict(zip(range(6),hurri_aux_rating_list))

print('.')
print('.')
print(damage_rating(hurricanes_dict, damage_scale))
from tkinter import *
from tkinter import ttk
import copy

# creates the window of tkinter
window = Tk()
window.configure(background='white')
window.title('Thing')
window.geometry("750x500")

# declares current_attraction_index, a variable to keep track of which screen we are on
current_attraction_index = 0



# this function runs whenever the "search" button is pressed
def search():

    # clears the lists of matches and attractions in the selected city
    matches = []
    in_city = []

    # gets all of the data and makes sure it's valid
    state = state_dropdown.get()
    state_boolean = not (state == "Select a State")
    city = cities_dropdown.get()
    city_boolean = not (city == "Select a State First" or city == "Select a City" or city == "Any")
    max_p = max_price_slider.get()
    type = type_dropdown.get()
    type_boolean = not (type == "Select a Type" or type == "Any")
    rating = rating_slider.get()
    inside = 1 == inside_choice.get()

    # checks if data entered is valid and then searches through the data to find acceptable places based on input
    if (inside):
        for i in attractions:
            match_counter = 0
            non_matches = []
            if((i[1] == city or (not city_boolean)) and (i[2] == state or (not state_boolean))):
                if(i[3] <= max_p):
                    match_counter += 1
                else:
                    non_matches.append("Price")

                if(i[4] == type or (not type_boolean)):
                    match_counter += 1
                else:
                    non_matches.append("Type")

                if(i[5]):
                    match_counter += 1
                else:
                    non_matches.append("Inside")

                if(i[6] >= rating):
                    match_counter += 1
                else:
                    non_matches.append("Rating")

                in_city.append([i, match_counter, non_matches])
            
            
            if((i[1] == city or (not city_boolean)) and (i[2] == state or (not state_boolean)) and (i[3] <= max_p) and (i[4] == type or (not type_boolean)) and (i[5]) and (i[6] >= rating)):
                matches.append(i)
    else:
        for i in attractions:
            match_counter = 1
            non_matches = []
            if((i[1] == city or (not city_boolean)) and (i[2] == state or (not state_boolean))):
                if(i[3] <= max_p):
                    match_counter += 1
                else:
                    non_matches.append("Price")

                if(i[4] == type or (not type_boolean)):
                    match_counter += 1
                else:
                    non_matches.append("Type")

                if(i[6] >= rating):
                    match_counter += 1
                else:
                    non_matches.append("Rating")

                in_city.append([i, match_counter, non_matches])
            
            if((i[1] == city or (not city_boolean)) and (i[2] == state or (not state_boolean)) and (i[3] <= max_p) and (i[4] == type or (not type_boolean)) and (i[6] >= rating)):
                matches.append(i)

    print(matches)    



def update_attraction(index):
    if (index == 0):
        back_button.place_forget()
    
    if (index == len(matches) - 1):
        next_button.place_forget()

    print("update", current_attraction_index)

# runs when the next button is pressed to show the next attraction
def next():
    global current_attraction_index
    current_attraction_index += 1
    print("next")
    update_attraction(current_attraction_index)
    

def back():
    global current_attraction_index
    current_attraction_index -= 1
    print("back")
    update_attraction(current_attraction_index)



# changes the possible selections of the city based on which state the user picked
def pick_cities(e):
    state = state_dropdown.get()
    if(state == "Nebraska"):
        cities_dropdown['values'] = ne_cities   
    elif(state == "California"):
        cities_dropdown['values'] = ca_cities
    elif(state == "New York"):
        cities_dropdown['values'] = ny_cities
    elif(state == "Texas"):
        cities_dropdown['values'] = tx_cities
    elif(state == "Florida"):
        cities_dropdown['values'] = fl_cities

    cities_dropdown.configure(state = 'normal')
    cities_dropdown.set("Select a City")

    
# initializes all the city and state options for each state
states_options = ["Nebraska", "California", "New York", "Texas", "Florida"]
ne_cities = ["Any", "Lincoln", "Omaha", "Scottsbluff", "North Platt"]
ca_cities = ["Any", "San Francisco", "Los Angeles", "San Jose", "Anaheim"]
ny_cities = ["Any", "New York City"]
tx_cities = ["Any", "Houston", "Dallas", "Austin", "San Antonio", "Fort Worth"]
fl_cities = ["Any", "Miami", "Orlando", "Tampa", "Key West"]
type_options = ["Any", "Educational", "Sightseeing", "Nature", "Pleasure"]

# stores the data for the possible places to go
attractions = [["Golden State Bridge", "San Francisco", "California", 0, "Sightseeing", False, 4.8],
                ["Yosemite National Park", "San Franciso", "California", 15, "Nature", False, 4.8],
                ["Disneyland", "Anaheim", "California", 250, "Pleasure", False, 4.8],
                ["Death Valley National Park", "Los Angeles", "California", 30, "Nature", False, 4.7],
                ["Big Sur", "San Jose", "California", 10, "Nature", False, 4.5],
                ["Lake Tahoe", "San Francisco", "California", 10, "Nature", False, 4.8],
                ["Sequoia National Park", "Los Angeles", "California", 35, "Nature", False, 4.8],
                ["Redwood National Park", "San Francisco", "California", 0, "Nature", False, 4.8],
                ["Joshua Tree National Park", "Los Angeles", "California", 30, "Nature", False, 4.8],
                ["Universal Studios Hollywood", "Los Angeles", "California", 110, "Pleasure", False, 4.6],
                ["Hearst Castle", "San Francisco", "California", 35, "Educational", True, 4.6],
                ["Santa Catalina Island", "Los Angeles", "California", 0, "Sightseeing", False, 4.6],
                ["Channel Islands National Park", "Los Angeles", "California", 0, "Sightseeing", False, 4.7],
                ["The Getty Center", "Los Angeles", "California", 0, "Educational", True, 4.8],
                ["Statue of Liberty", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["Central Park", "New York City", "New York", 0, "Nature", False, 4.8],
                ["Rockefeller Center", "New York City", "New York", 40, "Sightseeing", True, 4.7],
                ["Metropolitan Museum of Art", "New York City", "New York", 25, "Educational", True, 4.8],
                ["Broadway", "New York City", "New York", 100, "Sightseeing", False, 4.5],
                ["Empire State Building", "New York City", "New York", 36, "Sightseeing", True, 4.7],
                ["9/11 Memorial", "New York City", "New York", 30, "Educational", False, 4.9],
                ["High Line", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["Times Square", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["Brooklyn Bridge", "New York City", "New York", 0, "Sightseeing", False, 4.8],
                ["Fifth Avenue", "New York City", "New York", 0, "Sightseeing", False, 4.8],
                ["Grand Central Terminal", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["One World Observatory", "New York City", "New York", 43, "Pleasure", True, 4.7],
                ["The Frick Collection", "New York City", "New York", 20, "Educational", True, 4.6],
                ["New York Public Library", "New York City", "New York", 0, "Educational", True, 4.7],
                ["Wall Street", "New York City", "New York", 0, "Sightseeing", True, 4.6],
                ["Radio City Music Hall", "New York City", "New York", 31, "Pleasure", True, 4.7],
                ["St. Patrick's Cathedral", "New York City", "New York", 10, "Sightseeing", True, 4.8],
                ["Carnegie Hall", "New York City", "New York", 300, "Sightseeing", True, 4.7],
                ["Bryant Park", "New York City", "New York", 0, "Sightseeing", False, 4.7],
                ["Walt Disney World", "Orlando", "Florida", 110, "Pleasure", False, 4.7],
                ["Kennedy Space Center", "Orlando", "Florida", 50, "Educational", False, 4],
                ["Universal Studios", "Orlando", "Florida", 110, "Pleasure", False, 4.7],
                ["Miami Beach", "Miami", "Florida", 0, "Pleasure", False, 4.4],
                ["Everglades National Park", "Miami", "Florida", 0, "Nature", False, 4.6],
                ["Daytona 500 International Speedway", "Orlando", "Florida", 20, "Sightseeing", False, 4.7],
                ["SeaWorld Orlando", "Orlando", "Florida", 80, "Educational", False, 4.5],
                ["Busch Gardens Tampa", "Tampa", "Florida", 15, "Pleasure", False, 4.5],
                ["Duval Street", "Key West", "Florida", 0, "Sightseeing", False, 4.6],
                ["St. Augustine's Historic District", "Key West", "Flordia", 0, "Sightseeing", False, 1],
                ["Edison and Ford Winter Estates", "Miami", "Florida", 20, "Sightseeing", True, 4.7],
                ["Salvador Dali Museum", "Tampa", "Florida", 20, "Educational", True, 4.7],
                ["Big Bend National Park", "San Antonio", "Texas", 15, "Nature", False, 4.8],
                ["The Alamo", "San Antonio", "Texas", 0, "Educational", False, 4.6],
                ["San Antonio's River Walk", "San Antonio", "Texas", 0, "Sightseeing", False, 4.7],
                ["Space Center Houston", "Houston", "Texas", 30, "Educational", False, 4.6],
                ["Padre Island National Seashore", "San Antonio", "Texas", 20, "Nature", False, 4.4],
                ["Texas State Capitol", "Austin", "Texas", 0, "Sightseeing", True, 4.7],
                ["Sixth Floor Museum", "Dallas", "Texas", 15, "Educational", True, 4.6],
                ["Fort Worth Stockyards", "Fort Worth", "Texas", 0, "Sightseeing", True, 4.7],
                ["Galveston Beach", "Houston", "Texas", 10, "Sightseeing", False, 4.5],
                ["USS Lexington", "San Antonio", "Texas", 20, "Educational", True, 4.8],
                ["Cadillac Ranch", "Dallas", "Texas", 0, "Sightseeing", False, 4.4],
                ["Natural Bridge Caverns", "San Antonio", "Texas", 30, "Nature", False, 4.7],
                ["Houston's Museum District", "Houston", "Texas", 20, "Educational", True, 4.5],
                ["Gruene Historic District", "San Antonio", "Texas", 10, "Sightseeing", False, 4.3],
                ["Dallas Arboretum", "Dallas", "Texas", 10, "Sightseeing", False, 4.3],
                ["Henry Doorly Zoo", "Omaha", "Nebraska", 20, "Educational", False, 4.8],
                ["Old Market in Omaha", "Omaha", "Nebraska", 0, "Sightseeing", False, 4.4],
                ["Strategic Air and Space Museum", "Omaha", "Nebraska", 15, "Educational", True, 4.7],
                ["Chimney Rock Historic Site", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.2],
                ["Haymarket District in Lincoln", "Lincoln", "Nebraska", 0, "Sightseeing", False, 4.7],
                ["Nebraska State Capitol", "Lincoln", "Nebraska", 0, "Sightseeing", True, 4.5],
                ["Lied Center", "Lincoln", "Nebraska", 50, "Pleasure", True, 4.3],
                ["Sheldon Museum of Art", "Lincoln", "Nebraska", 0, "Educational", True, 4.5],
                ["National Museum of Roller Skating", "Lincoln", "Nebraska", 0, "Educational", True, 3.9],
                ["Scottsbluff National Monument", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.8],
                ["Golden Spike Tower", "North Platte", "Nebraska", 10, "Sightseeing", False, 4.7],
                ["Carhenge", "Scottsbluff", "Nebraska", 0, "Sightseeing", False, 4.6]]

matches = []
in_city = []
current_attraction_index = 0


# creates backup of the attractions list
attractions_backup = copy.deepcopy(attractions)

# initializes variables to store user's input
state_choice= StringVar(window)
city_choice = StringVar(window)
max_price = DoubleVar(window)
type_choice = StringVar(window)
rating_choice = DoubleVar(window)
inside_choice = IntVar()


# creates the dropdown where users select their state
state_dropdown = ttk.Combobox(window, width = 16, textvariable = state_choice)
state_dropdown['values'] = states_options
state_dropdown.set("Select a State")
state_dropdown.place(x = 10, y = 70)  
state_dropdown.bind("<<ComboboxSelected>>", pick_cities)

# creates the dropdown where users select their city
cities_dropdown = ttk.Combobox(window, width = 16, values = ["Select a State First"])
cities_dropdown.current(0)
cities_dropdown.place(x = 10, y = 110)
cities_dropdown.configure(state = 'disabled')

# creates the dropdown where users select their type of attraction
type_dropdown = ttk.Combobox(window, width = 16, value = type_options)
type_dropdown.set("Select a Type")
type_dropdown.place(x = 10, y = 150)

# creates the dropdown where users select wheter or not they want to be outside
inside_check = Checkbutton(window, text = "Inside Only", variable = inside_choice)
inside_check.place(x = 10, y = 190)

# creates the slider where users decide the maximum price of their attraction
max_price_slider = Scale(window, variable = max_price, from_ = 0, to = 300, orient = HORIZONTAL, resolution = 5)
max_price_slider.place(x = 10, y = 250)
max_price_slider.set(300)
max_price_slider.configure(background = 'white')

max_text = Text(window, background = 'white', borderwidth = 0, height = 1, width = 9, font = ("Arial", 10))
max_text.place(x = 10, y = 230)
max_text.insert('end', 'Max Price')
max_text.configure(state = 'disabled')

# creates the slider where users decide the rating they want their attraction to be
rating_slider = Scale(window, variable = rating_choice, from_ = 0, to = 5, orient = HORIZONTAL, resolution = 0.1)
rating_slider.place(x = 10, y = 320)
rating_slider.configure(background = 'white')

rating_text = Text(window, background = 'white', borderwidth = 0, height = 1, width = 14, font = ("Arial", 10))
rating_text.place(x = 10, y = 300)
rating_text.insert('end', 'Minimum Rating')
rating_text.configure(state = 'disabled')

# creates the button users click to search once they have finished their entering
search_button = Button(window, text = 'Search', command = search)
search_button.place(x = 50, y = 420)

# separates the sidebar from the main display
separator = ttk.Separator(window, orient = 'vertical')
separator.place(relx=0.2, rely=0, relwidth=.001, relheight=1)

# next and back button to go through matching attractions
next_button = Button(window, text = "Next >", command = next)
next_button.place(x = 675, y = 20)

back_button = Button(window, text = "< Back", command = back)
back_button.place(x = 175, y = 20)

# text box to show the title of the shown attraction
title_text = Text(window, background='white', 
                  borderwidth=0, height = 1, 
                  width = 32, font = ("Arial", 19))
title_text.place(x=223, y=18)
title_text.tag_configure("center_title", justify='center')
title_text.insert('end', 'Daytona 500 International Speedway')
title_text.tag_add("center_title", "1.0", "end")
title_text.configure(state='disabled')

# about text box to give some info about the attraction
about_text = Text(window, background='white', 
                  borderwidth=0, height = 10,
                  width=20, font=("Arial", 14))
about_text.place(x=220, y = 100)
# about_text.insert('end', 'Daytona International Speedway is a race track in Daytona Beach, Florida, United States. Since opening in 1959, it has been the home of the Daytona 500, the most prestigious race in NASCAR as well as its season opening event.')
about_text.configure(state='disabled')



window.mainloop()
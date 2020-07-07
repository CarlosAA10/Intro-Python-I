"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({
    "lat": 42, 
    "lon": -125,
    "name": "a fourth place"
})

print(waypoints,'the new waypoint')
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.
waypoints[0] = {
    "lat": 42,
    "lon": -130, 
    "name": "not a real place"
}

print(waypoints,' the new waypoints')
# YOUR CODE HERE

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for x in waypoints: 
    for k, v in x.items():
        print(v,'the values')



# in class notes for 06/02/2020

names_and_ages = [
    ("Chung", 21), 
    ("Mung", 34), 
    ("Frank", 23), 
    ("Goombarthur", 21), 
    ("Gucci Gumbus", 54), 
    ("Torito", 18),
]

# transfer the above list into a dictionary whose keys are the names
#and values are the ages

# d = {}
#with a for loop
# taking advantage of Python's automatic destructuring of tuples

# for name, age in names_and_ages: 
#     # assign the name as a key to our dict with the age as value 
#     d[name] = age

# print(d)

d = {name:age for name, age in names_and_ages}

print(d)
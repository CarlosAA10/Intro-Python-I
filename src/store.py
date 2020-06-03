

class Store():
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    
    def __str__(self):  
        output = f"{self.name}\n"
        for d in self.departments:
            output += " id:" + str(d.get_id()) + ", \n"
        return output

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Department {self.id}: {self.name}"
    # add a way for a user to select departments


departments = [
    Department(1,"Running"),
    Department(2, "Fishing"),
    Department(3, "Bseball"),
]

my_store = Store("The Dugout",departments )

print(my_store)

selection = input("Select a department number: ")
print(f"You selected Department {selection}, {departments[selection-1].get_name()}")
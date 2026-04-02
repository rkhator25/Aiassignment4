districts = [
    "Adilabad","Bhadradri","Hyderabad","Jagtial","Jangaon","Jayashankar",
    "Jogulamba","Kamareddy","Karimnagar","Khammam","Komaram Bheem",
    "Mahabubabad","Mahabubnagar","Mancherial","Medak","Medchal",
    "Mulugu","Nagarkurnool","Nalgonda","Narayanpet","Nirmal",
    "Nizamabad","Peddapalli","Rajanna","Rangareddy","Sangareddy",
    "Siddipet","Suryapet","Vikarabad","Wanaparthy","Warangal Rural",
    "Warangal Urban","Yadadri"
]

neighbors = {
    "Hyderabad": ["Rangareddy", "Medchal"],
    "Rangareddy": ["Hyderabad", "Vikarabad", "Mahabubnagar"],
    "Nizamabad": ["Kamareddy", "Nirmal"],
    "Warangal Urban": ["Warangal Rural", "Jangaon"],
 
}

colors = ['Red', 'Green', 'Blue', 'Yellow']

def is_valid(district, color, assignment):
    for n in neighbors.get(district, []):
        if n in assignment and assignment[n] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    unassigned = [d for d in districts if d not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

solution = backtrack({})
print("Telangana Coloring:")
print(solution)

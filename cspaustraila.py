states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  
}

colors = ['Red', 'Green', 'Blue']

def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment

    unassigned = [s for s in states if s not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

solution = backtrack({})
print("Australia Coloring Solution:")
print(solution)

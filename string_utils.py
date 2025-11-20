def count_atoms_in_molecule(molecular_formula):
    atom_count = {}
    for i in split_before_each_uppercases(molecular_formula):
      atom , count= split_at_first_digit(i)
      atom_count[atom] = count
    return atom_count

def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count

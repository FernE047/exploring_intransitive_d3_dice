with open("./data/dice_set_cases.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

class State:
    def __init__(self, terms:list[str], operator:list[str]) -> None:
        self.terms = terms
        self.operator = operator

    def next_states(self) -> list["State"]:
        states: list["State"] = []
        for i in range(len(self.operator)):
            if self.operator[i] == "≤":
                new_terms_eq = self.terms.copy()
                new_operator_eq = self.operator.copy()
                new_operator_eq[i] = '='
                states.extend(State(new_terms_eq, new_operator_eq).next_states())
                new_terms_lt = self.terms.copy()
                new_operator_lt = self.operator.copy()
                new_operator_lt[i] = '<'
                states.extend(State(new_terms_lt, new_operator_lt).next_states())
                break
        if all(op != '≤' for op in self.operator):
            states.append(self)
        return states
    
    def sort_equalities(self) -> None:
        i = 0
        while i < len(self.operator):
            if self.operator[i] == '=':
                j = i + 1
                while j < len(self.operator) and self.operator[j] == '=':
                    j += 1
                equal_terms = self.terms[i:j+1]
                equal_terms.sort()
                self.terms[i:j+1] = equal_terms
                i = j
            else:
                i += 1

    def __str__(self) -> str:
        return self.terms[0] + self.operator[0] + self.terms[1] + self.operator[1] + self.terms[2] + self.operator[2] + self.terms[3] + self.operator[3] + self.terms[4] + self.operator[4] + self.terms[5] + self.operator[5] + self.terms[6] + self.operator[6] + self.terms[7] + self.operator[7] + self.terms[8]


unique_lines: set[str] = set()
for line in lines:
    line = line.strip()
    terms = line.split(" ≤ ")
    #there's 9 terms, 8 comparisons, we want to generate all the cases distinguishing between < and =
    state = State(terms, ['≤'] * 8)
    for final_state in state.next_states():
        final_state.sort_equalities()
        new_line = str(final_state)
        unique_lines.add(new_line)
print(len(unique_lines))
#sort lines by amount of equalities first, then lexicographically
lines_sorted = sorted(sorted(unique_lines), key=lambda x: (x.count("="), x))
with open("./data/dice_set_all_cases.txt", "w", encoding="utf-8") as file:
    for line in lines_sorted:
        file.write(line + "\n")
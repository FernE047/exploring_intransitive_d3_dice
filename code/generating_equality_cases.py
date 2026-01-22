PREFIXNAME = "two_dice"

with open(f"./data/{PREFIXNAME}_cases.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


class State:
    def __init__(self, terms: list[str], operator: list[str] | None = None) -> None:
        self.terms = terms
        if operator is None:
            self.operator = ["≤"] * (len(self.terms)-1)
        else:
            self.operator = operator

    def next_states(self) -> list["State"]:
        states: list["State"] = []
        for i in range(len(self.operator)):
            if self.operator[i] == "≤":
                new_terms_eq = self.terms.copy()
                new_operator_eq = self.operator.copy()
                new_operator_eq[i] = "="
                states.extend(State(new_terms_eq, new_operator_eq).next_states())
                new_terms_lt = self.terms.copy()
                new_operator_lt = self.operator.copy()
                new_operator_lt[i] = "<"
                states.extend(State(new_terms_lt, new_operator_lt).next_states())
                break
        if all(op != "≤" for op in self.operator):
            states.append(self)
        return states

    def sort_equalities(self) -> None:
        i = 0
        while i < len(self.operator):
            if self.operator[i] == "=":
                j = i + 1
                while j < len(self.operator) and self.operator[j] == "=":
                    j += 1
                equal_terms = self.terms[i : j + 1]
                equal_terms.sort()
                self.terms[i : j + 1] = equal_terms
                i = j
            else:
                i += 1

    def __str__(self) -> str:
        text = ""
        for index in range(len(self.operator)):
            text += f"{self.terms[index]} {self.operator[index]} "
        text += self.terms[-1]
        return text


unique_lines: set[str] = set()
for line in lines:
    line = line.strip()
    terms = line.split(" ≤ ")
    state = State(terms)
    for final_state in state.next_states():
        final_state.sort_equalities()
        new_line = str(final_state)
        unique_lines.add(new_line)
print(len(unique_lines))
# sort lines by amount of equalities first, then lexicographically
lines_sorted = sorted(sorted(unique_lines), key=lambda x: (x.count("="), x))
with open(f"./data/{PREFIXNAME}_all_cases.txt", "w", encoding="utf-8") as file:
    for line in lines_sorted:
        file.write(line + "\n")

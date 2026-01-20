class State:
    def __init__(
        self,
        groups: list[list[str]] | None = None,
        order: dict[int, int] | None = None,
        current_index: int = 0,
        string_coming: str = "",
    ) -> None:
        self.string_coming = string_coming
        self.order: dict[int, int]
        self.current_index: int = current_index
        if groups is None:
            self.groups = [["x", "y", "z"] * 3]
        else:
            self.groups = groups
        if order is None:
            self.order = {}
        else:
            self.order = order

    def next_states(self) -> list["State"]:
        states: list["State"] = []
        for i in range(len(self.groups)):
            if len(self.groups[i]) == 0:
                continue
            new_groups = [group.copy() for group in self.groups]  # deep copy
            new_order = self.order.copy()
            new_index = self.current_index
            if i not in new_order:
                new_order[i] = new_index
                new_index += 1
            char = new_groups[i].pop(0) + "_" + str(new_order[i])
            text = ""
            if self.string_coming:
                text = self.string_coming + " < " + char
            else:
                text = char
            new_state = State(new_groups, new_order, new_index, text)
            states.append(new_state)
        return states

    def calculate_possibilities(self) -> list["State"]:
        possibilities: list["State"] = []
        values: set[str] = set()
        if all(len(group) == 0 for group in self.groups):
            if self.string_coming not in values:
                values.add(self.string_coming)
                possibilities.append(self)
        else:
            for next_state in self.next_states():
                poss = next_state.calculate_possibilities()
                for p in poss:
                    if p.string_coming not in values:
                        values.add(p.string_coming)
                        possibilities.append(p)
        return possibilities

    def __str__(self) -> str:
        return self.string_coming

initial_state = State()
possibilities = initial_state.calculate_possibilities()
len(possibilities)
for possibility in possibilities:
    print(possibility)

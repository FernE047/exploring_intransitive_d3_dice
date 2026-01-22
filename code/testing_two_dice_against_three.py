intransitive_cases: list[str] = []
with open("./data/intransitive_cases.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        intransitive_cases.append(line.strip())


class TwoDiceState:
    def __init__(self, comparison: str) -> None:
        self.comparison = comparison

    def pair_wise_comparisons(self) -> list[tuple[str, str, str]]:
        comparisons: list[tuple[str, str, str]] = []
        term_left = ""
        term_right = ""
        operation = ""
        for index in range(len(self.comparison)):
            char = self.comparison[index]
            if char in ("<", "=", "≤"):
                if term_left and term_right and operation:
                    comparisons.append((term_left, operation, term_right))
                    term_left = term_right
                    term_right = ""
                operation = char
            else:
                if not operation:
                    term_left += char
                else:
                    term_right += char
        if term_left and term_right and operation:
            comparisons.append((term_left, operation, term_right))
        return comparisons

    def is_intransitive(self, intransitive_case: str) -> bool:
        comparisons = self.pair_wise_comparisons()
        print(comparisons)
        for pair_wise in comparisons:
            left, operation, right = pair_wise
            left_index = intransitive_case.index(left)
            right_index = intransitive_case.index(right)
            if left_index > right_index:
                return False
            case_part = intransitive_case[left_index : right_index + len(right)]
            if "<" in case_part:
                if operation == "=":
                    return False
            else:
                if operation == "<":
                    return False
        return True  # all pair-wise comparisons satisfied


class TwoDiceStates:
    def __init__(
        self, original_comparison: str, state_1: TwoDiceState, state_2: TwoDiceState, state_3: TwoDiceState
    ) -> None:
        self.original_comparison = original_comparison
        self.state_1 = state_1
        self.state_2 = state_2
        self.state_3 = state_3
        self.states = [state_1, state_2, state_3]  # for easier iteration
        self.intransitive_cases: list[str] = []

    def is_intransitive(self, intransitive_cases: list[str]) -> bool:
        for case in intransitive_cases:
            for i,state in enumerate(self.states):
                if state.is_intransitive(case):
                    case_replaced = ""
                    if i == 0:
                        case_replaced = case.replace("x", "t").replace("y", "w").replace("z", "v")
                    elif i == 1:
                        case_replaced = case.replace("x", "t").replace("z", "w").replace("y", "v")
                    else:
                        case_replaced = case.replace("y", "t").replace("z", "w").replace("x", "v")
                    self.intransitive_cases.append(case_replaced)
        return len(self.intransitive_cases) > 0


class TwoDiceRawState:
    def __init__(self, comparison: str) -> None:
        self.comparison = comparison

    def create_state(self) -> TwoDiceStates:
        cases: list[TwoDiceState] = []
        cases.append(TwoDiceState(self.comparison.replace("t", "x").replace("w", "y")))
        cases.append(TwoDiceState(self.comparison.replace("t", "x").replace("w", "z")))
        cases.append(TwoDiceState(self.comparison.replace("t", "y").replace("w", "z")))
        return TwoDiceStates(self.comparison, cases[0], cases[1], cases[2])


two_dice_cases: list[TwoDiceStates] = []
with open("./data/two_dice_all_cases.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        raw_state = TwoDiceRawState(line.strip())
        two_dice_cases.append(raw_state.create_state())

two_dices_intransitive_cases: list[TwoDiceStates] = []
two_dices_discarded_cases: list[TwoDiceStates] = []

for two_dice_case in two_dice_cases:
    if two_dice_case.is_intransitive(intransitive_cases):
        two_dices_intransitive_cases.append(two_dice_case)
    else:
        two_dices_discarded_cases.append(two_dice_case)

with open("./data/two_dice_intransitive_cases.txt", "w", encoding="utf-8") as file:
    for case in two_dices_intransitive_cases:
        file.write(f"{case.original_comparison}\n")
with open("./data/two_dice_discarded_cases.txt", "w", encoding="utf-8") as file:
    for case in two_dices_discarded_cases:
        file.write(f"{case.original_comparison}\n")
with open("./data/two_dice_intransitive_detailed_cases.txt", "w", encoding="utf-8") as file:
    for case in sorted(two_dices_intransitive_cases, key=lambda c: len(c.intransitive_cases), reverse=True):
        file.write(f"Original comparison: {case.original_comparison}\n")
        for intransitive_case in case.intransitive_cases:
            file.write(f"    Intransitive case: {intransitive_case}\n")
        file.write("\n")

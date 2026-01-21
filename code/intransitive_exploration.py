class Die:
    """Base class for all dice types."""

    def __init__(
        self, sides: tuple[str, str, str], comparison: str | None = None
    ) -> None:
        self.sides = tuple(sorted(sides))
        self.comparison = comparison

    def set_comparison(self, comparison: str) -> None:
        self.comparison = comparison

    def compare_value(self, side_a: str, side_b: str) -> int:
        if self.comparison is None:
            raise ValueError("Comparison not set for this die.")
        side_a_index = self.comparison.index(side_a)
        side_b_index = self.comparison.index(side_b)
        min_index = min(side_a_index, side_b_index)
        max_index = max(side_a_index, side_b_index)
        current_comparison = self.comparison[min_index : max_index + 2]
        if "<" not in current_comparison:
            return 0
        if side_a_index < side_b_index:
            return -1
        return 1

    def compare(self, other: "Die") -> int:
        wins = 0
        losses = 0
        for side_a in self.sides:
            for side_b in other.sides:
                result = self.compare_value(side_a, side_b)
                if result == 1:
                    wins += 1
                elif result == -1:
                    losses += 1
        if wins > losses:
            return 1
        elif losses > wins:
            return -1
        else:
            return 0


class DiceSet:
    """A set of three dice to check for intransitivity."""

    def __init__(self, die_a: Die, die_b: Die, die_c: Die) -> None:
        self.die_a = die_a
        self.die_b = die_b
        self.die_c = die_c

    def is_intransitive(self) -> bool:
        result_ab = self.die_a.compare(self.die_b)
        result_bc = self.die_b.compare(self.die_c)
        result_ca = self.die_c.compare(self.die_a)
        final_result = result_ab + result_bc + result_ca
        return (
            final_result == 3 or final_result == -3
        )  # there is 3 wins or 3 losses forming a cycle

    def set_comparisons(self, comparison: str) -> None:
        self.die_a.set_comparison(comparison)
        self.die_b.set_comparison(comparison)
        self.die_c.set_comparison(comparison)


die_a = Die(("x₀", "x₁", "x₂"))
die_b = Die(("y₀", "y₁", "y₂"))
die_c = Die(("z₀", "z₁", "z₂"))
dice_set = DiceSet(die_a, die_b, die_c)
comparisons: list[str] = []
with open("./data/dice_set_all_cases.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        comparisons.append(line)
intransitive_cases: list[str] = []
for comparison in comparisons:
    dice_set.set_comparisons(comparison)
    if dice_set.is_intransitive():
        intransitive_cases.append(comparison)

print(f"Found {len(intransitive_cases)} intransitive dice sets:")

with open(
    "./data/intransitive_cases.txt", "w", encoding="utf-8"
) as file:
    for case in intransitive_cases:
        print(case)
        file.write(case + "\n")
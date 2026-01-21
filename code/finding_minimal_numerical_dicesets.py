comparisons: list[str] = []
with open("./data/intransitive_cases.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        comparisons.append(line.strip())
translation_dict_0 = {"x": 0, "y": 1, "z": 2}
translation_dict_1 = {"₀": 0, "₁": 1, "₂": 2}
DiceData = tuple[int, int, int]
DiceSetData = tuple[DiceData, DiceData, DiceData]
dice_sets: list[DiceSetData] = []
for comparison in comparisons:
    die_1 = [0] * 3
    die_2 = [0] * 3
    die_3 = [0] * 3
    dies = [die_1, die_2, die_3]
    for index, unique_values_terms in enumerate(comparison.split("<")):
        if "=" in unique_values_terms:
            terms = unique_values_terms.split("=")
        else:
            terms = [unique_values_terms]
        for term in terms:
            die:list[int] = dies[translation_dict_0[term[0]]]
            die[translation_dict_1[term[1]]] = index + 1
    dice_sets.append(((die_1[0], die_1[1], die_1[2]), (die_2[0], die_2[1], die_2[2]), (die_3[0], die_3[1], die_3[2])))
with open("./data/minimal_numerical_dice_sets.txt", "w", encoding="utf-8") as file:
    for dice_set in dice_sets:
        line = f"{str(dice_set)}\n"
        file.write(line)
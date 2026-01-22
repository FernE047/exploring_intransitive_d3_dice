Initial Problem recap: given two three sided dice X, Y. can we find a third die Z such that X > Y, Y > Z, and Z > X? where ">" means "is more likely to roll a higher number than". if we can find, on what configurations of numbers on the dice this is possible? on what configurations is this impossible?

we still need some stepping stones to reach that goal. given the 71 intransitive dicesets found, once we get all two 3-sided dice configurations (X, Y), we can check if there is a third die Z that makes the diceset (X, Y, Z) intransitive, using the cases already found.

Problem IV: given two dice T and W, what are all the possible comparison arrangements between then?
remembering:
w₀ ≤ w₁ ≤ w₂
t₀ ≤ t₁ ≤ t₂

We can use the same strategy as paper_1 problem I.

first we calculate all cases with ≤ using `code/counting_possibilities.py` now changed so it can calculate cases of N dices. output saved on `data/two_dice_cases.txt`. there's a total of 10 cases
then we calculate the cases distinguishing equalitys and less than comparisions on `code\generating_equality_cases.py`, it gives us 152 cases, output saved on `data/two_dice_all_cases.txt`

Problem IV is solved.


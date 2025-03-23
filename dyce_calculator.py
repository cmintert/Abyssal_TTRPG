from dyce import H, P
from dyce.evaluation import expandable, PResult
from numerary.types import SupportsInt

# Create a 20-sided die
d20 = H(20)
d4 = H(4)

# Create a pool of d4

temptation_dice_pool = 4

# Create a pool of 3d20
pool_3d20 = 3 @ P(d20)
pool_d4 = temptation_dice_pool @ P(d4)


@expandable
def conditional_selection(p_3d20: PResult, p_d4: PResult) -> PResult:
    # Check if any d4 shows a 4
    has_four = any(outcome == 4 for outcome in p_d4.roll)

    # Sort the 3d20 roll
    sorted_roll = sorted(p_3d20.roll)

    if has_four:
        # If a 4 shows up, take the lowest value (index 0)
        return sorted_roll[0]
    else:
        # Otherwise take the middle value (index 1)
        return sorted_roll[1]

# Calculate the distribution
if temptation_dice_pool > 0:
    result_distribution = conditional_selection(pool_3d20, pool_d4)
else:
    result_distribution = pool_3d20.h(1)

# Display statistics
print("Section Start")
print("-"*20)
print(f"Statistics for 3D20 roll in Abyssal TTRPG, with {temptation_dice_pool} Temptation dice:")
print(f"Average value: {result_distribution.mean()}")
print(f"Standard deviation: {result_distribution.stdev()}")
print(result_distribution.format(scaled=True))
print("-"*20)

print("Probability distribution of at least:")
for outcome in result_distribution:
    at_least = result_distribution.ge(outcome)
    probability = at_least[True] / at_least.total
    print(f"{outcome}| {probability * 100:.2f}% | {'#' * int(probability * 30)}")
print("-"*20)

print("Probability distribution of at most:")
for outcome in result_distribution:
    at_least = result_distribution.le(outcome)
    probability = at_least[True] / at_least.total
    print(f"{outcome}| {probability * 100:.2f}% | {'#' * int(probability * 30)}")
print("-"*20)

print("Section End")
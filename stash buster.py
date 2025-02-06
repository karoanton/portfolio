# Generate crochet projects to eliminate yarn from existing stash
# Input: Amount of yarn (length (meters or yards) or weight (grams)) and weight (thickness of yarn
# Output: List of projects that require that much yarn at maximum


def stash_buster(weight, yardage):
    if weight == 1:
        if yardage <= 4150:
            return "You can make an afghan or large blanket with your yarn!"
        if yardage <= 3400:
            return "You can make an adult sweater with your yarn!"
        if yardage <= 1700:
            return "You can make a baby blanket with your yarn!"
        if yardage <= 850:
            return "You can make a shawl or scarf with your yarn!"
        if yardage <= 500:
            return "You can make a pair of socks with your yarn!"
        elif yardage <= 350:
            return "You can make a hat with your yarn!"

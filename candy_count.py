# candy_count.py
# Counts my Halloween Candy.

name = "Hunter"
chocolate = 12
gummies = 8
lollipops = 5
sour_worms = 6
given_away = 4

total = chocolate + gummies + lollipops + sour_worms
left = total - given_away

print("Candy report for ", name)
print("Total pieces: ", total)
print("Pieces left after sharing: ", left)
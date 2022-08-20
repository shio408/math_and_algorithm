A = list(map(int, input().split()))
red_card = A.count(1)
yellow_card = A.count(2)
blue_card = A.count(3)

red_card_pattern = red_card * (red_card - 1) / 2
yellow_card_pattern = yellow_card * (yellow_card - 1) / 2
blue_card_pattern = blue_card * (blue_card - 1) / 2
print(int(red_card_pattern + yellow_card_pattern + blue_card_pattern))

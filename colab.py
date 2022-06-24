from deck123 import deck
from numgene import hand_gen

list_of_nums=hand_gen(7)
#print(list_of_nums)

stack_of_cards=deck()

for i in list_of_nums:
    current_card=stack_of_cards[i]
    print(current_card.title)












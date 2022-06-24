
import random




def hand_gen(how_many):
    rolls=0
    num_list=[]
    while rolls<how_many:
    
        rand_num=random.randint(0, 59)
        if rand_num not in num_list:
            num_list.append(rand_num)
            rolls+=1

    return num_list
            




#print(num_list[3])




    





    






    
    

        


          

    
# num = 0
# while num < 10:
#     print(num)
#     num += 1




#import random
#rand_num = random.randint(0,50)
#my_num = 50
#while rand_num != my_num:
#    print(rand_num)
#    rand_num = random.randint(0,50)
#print("You've found {}!".format(my_num))



product_list = [
    ['Iphone',5800],
    ['MAC Pro',12800],
    ['Bike',800],
    ['Coffee',32],
    ['PhthonBooke',120]
]
shopping_list = []
salary = input("please input your salary :")
if salary.isdigit():
    salary = int(salary)
    while True:
       for index,item in enumerate(product_list):
           print(index,item)
       user_choice = input("选择您要购买的商品：")
       if user_choice.isdigit():
           user_choice = int(user_choice)
           if user_choice < len(product_list) and user_choice >= 0 :
               p_item = product_list[user_choice]
               if p_item[1] < salary: #买的起
                    salary -= p_item[1]
                    shopping_list.append(p_item)
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
               else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
           else:
               print("Your input is not exist,please input again")
               salary = int(input("please input your salary :"))
       elif user_choice == "q":
           print("You have shopped %s" % shopping_list)
           exit()




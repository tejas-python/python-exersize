# students ={'tejas':['id002',27,'A'],"vc":['id002',34,'C'],'vishal':['id005',22,'B'],'sumukha':['id006',88,"F"],'samrth':['id004',20,'A']}
films ={
    "tarzon" :[5,4],
    "ghost rider":[12,5],
    "infinity war":[15,9],
    "end game":[8,2]
}
while True:
    choise = input("Which flim you want to watch: ").strip().lower()
    if choise in films:
        age = int(input("how old are you ? ").strip())
        if age >= films[choise][0]:
            if films[choise][1] >0:
                print("enjoy the film")
                films[choise][1] -= 1
            else:
                print("we are sold out")



        else:
            print('too young to watch the film')


    else:
        print('we dont have that film')
    

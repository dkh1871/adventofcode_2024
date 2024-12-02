def create_lists(file_path:str) -> list|list:
    list_1 = list()
    list_2 = list()

    with open(file_path, 'r') as f:
        for i in f:
            split_list = i.split(' ')
            list_1.append(int(split_list[0]))
            list_2.append(int(split_list[3]))

    return list_1, list_2

def find_dist(l1:list, l2:list) -> None:
   dist_list = list()
   l1.sort()
   l2.sort()

   i = 0

   while i < 1000:
       dist_list.append(abs(l1[i]-l2[i]))
       i += 1

   print(f'len of dist_list is {len(dist_list)}') 
   print(sum(dist_list))   

def get_similarity(l1:list,l2:list) -> None:
    sim_score = 0

    for val in l1:
        sim_score = sim_score + (val * l2.count(val))

    print(f"The Sim Score is {sim_score}")


def main() -> None:
   l1, l2 = create_lists("input.txt")

   print(f'len of list 1 is {len(l1)}')
   print(f'len of list 2 is {len(l2)}')
   
   find_dist(l1,l2)
   get_similarity(l1,l2)



if __name__ == "__main__":
    main()
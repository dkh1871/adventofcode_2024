def load_data(file_path: str) -> list[list[int]]:
    output_list: list[list[int]] = list()
    0
    with open(file_path, 'r') as f:
        for line in f:
            add_list: list[int] = list()
            for val in line.split(' '):
                add_list.append(int(val))
            
            output_list.append(add_list)

    return output_list

def process_date_for_puzzel1(data:list[list[int]]) -> list[list[int]] | list[list[int]]:
    good_list: list[int] = list()
    bad_list: list[int] = list()
    
    for dataset in data:
        print(f'for dataset: {dataset} incress check {is_incressing(dataset)}'
              f' and decress check {is_dcresing(dataset)}')
        
        if is_incressing(dataset) == True or is_dcresing(dataset) == True:
            good_list.append(dataset)
        elif check_permu(dataset) == True:
            print(f'for dataset {dataset} passed purmu check')
            good_list.append(dataset)
        else:
            bad_list.append(dataset)

    return good_list, bad_list

def is_incressing(dataset: list[int]) -> bool:
    for index, value in enumerate(dataset[:-1]):
        if value >= dataset[index +1]:
            return False
        if (dataset[index +1] - value) > 3:
            return False   
    return True 

def is_dcresing(dataset: list[int]) -> bool:
    for index, value in enumerate(dataset[:-1]):
        if value <= dataset[index +1]:
            return False
        if (value - dataset[index +1]) > 3:
            return False   
    return True 

def check_permu(dataset: list[int]) -> bool:
    for index, value in enumerate(dataset):
        new_list = dataset.copy()
        new_list.pop(index)
        if is_incressing(new_list) == True or is_dcresing(new_list) == True:
            return True 
    
    return False
        


def main() -> None:
   data = load_data('input.txt')
   print(len(data))


   glist , blist = process_date_for_puzzel1(data)
   print(f'good list len {len(glist)}')
   print(f'Bad list len {len(blist)}')

if __name__ == "__main__":
    main()

def make_rules_dict() -> dict[int,list[int]]:
    rules_dic: dict[int,list[int]] = dict()

    with open('rules.txt','r') as fl:
        '''
        create a dict for each x value in the rules
        each y should not be printed prior to x
        '''
        for line in fl:
            splt_line = line.replace('\n','').split('|')
            key = int(splt_line[0])
            val = int(splt_line[1])
            
            if key in rules_dic:
                rules_dic[key].append(val)
            else:
                rules_dic[key]= [val]
    
    return rules_dic

def format_input_line(line:str) -> list[int]:
    '''
    returns a list from a text line
    '''
    outlist = list()
    for val in line.replace('/n','').split(','):
        outlist.append(int(val))
    return outlist

def line_in_right_order(line:list[int], rules:dict[int|list[int]]) -> bool | tuple[int]:
    '''
    loop through each line and check each value to 
    all values that came before. if prexisiting value 
    is on the rules list return false as it breaks the rules.
    return a tuple of 
    '''
    i = 0

    while i < len(line):
        for list_val in line[0:i]:
            if list_val in rules[line[i]]:
               return False, (line[i],list_val)

        i += 1

    return True, (0,0)


def fix_line_order(line:list[int], fix_pair:tuple[int]) -> None:
    '''
    updates list fixing the order
        remove the value from the list
        insert it prior to the value it should go before
    '''
    line.pop(line.index(fix_pair[0]))
    line.insert(line.index(fix_pair[1]),fix_pair[0])

def get_median(line:list[int]) -> int:

    if len(line) % 2 != 0:
        return line[int(len(line)/2)]


def main():
    rules = make_rules_dict()
    total_sum = 0
    toatl_sum_part_2 = 0

    with open('updates.txt','r') as fl:
        for line in fl:
            orgnl_line = format_input_line(line)
            wrkng_line = orgnl_line.copy()

            runs_to_fix = 0

            while True:
                vaild_line, fix_pair = line_in_right_order(wrkng_line, rules)

                if vaild_line == True:
                    break
                
                fix_line_order(wrkng_line, fix_pair)
                runs_to_fix += 1

            
            if sum(orgnl_line) != sum(wrkng_line):
                print('Test Failed .... Orginal line and working line have differnt sums')
                print(f'o-line: {orgnl_line}')
                print(f'w-line: {wrkng_line}')
                exit()

            if runs_to_fix == 0:
                total_sum += get_median(wrkng_line)
            
            if runs_to_fix > 0:
                toatl_sum_part_2 += get_median(wrkng_line)


            print(f'o-line: {orgnl_line} | part1 value : {total_sum}')
            print(f'w-line: {wrkng_line} | runs to fix : {runs_to_fix} | part2_value : {toatl_sum_part_2}' )
            

if __name__=="__main__":
    main()


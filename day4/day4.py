## created to francescopeluso for solution on the digangles.
## created to mgtezak for helping me figure out part 2.

import re

def create_matrix()->list:
    maxtrix = list()
    with open('input.txt','r') as f:
        for line in f:
            maxtrix.append(line.strip())
    
    return maxtrix

def create_search_matrix(base_matrix:list) -> list:
    
    search_list = list()

    rows,cols =len(base_matrix), len(base_matrix[0])

    for i in base_matrix:
        search_list.append(''.join(i))

    #createa vertical list
    for x in range(0,cols):
        new_list=list()
        for y in range(0,rows):
            new_list.append(base_matrix[y][x])

        search_list.append(''.join(new_list))

    #start in top right 
    for d in range(-(rows-1), cols):
        new_list = list()
        for i in range(max(0,d), min(rows,cols+d)):
            new_list.append(base_matrix[i][i-d])
        search_list.append(''.join(new_list))

    #start in top left
    for d in range(rows + cols -1):
        new_list = list()
        for i in range(max(0,d - cols + 1), min(rows, d+1)):
            new_list.append(base_matrix[i][d-i])
        search_list.append(''.join(new_list))
    
    return search_list

def part_one():
    search_list = create_search_matrix(create_matrix())

    cnt = 0
    for i in search_list:
        cnt += len(re.findall('XMAS', i))
        cnt += len(re.findall('SAMX', i))

    return cnt


def main():

    print(part_one())

    matrix = create_matrix()
    rows,cols =len(matrix), len(matrix[0])

    cnt = 0

    for y in range(1,rows-1):
        for x in range(1,cols-1):

            if matrix[y][x] == 'A':
                ul = matrix[y-1][x-1]
                ur = matrix[y-1][x+1]
                ll = matrix[y+1][x-1]
                lr = matrix[y+1][x+1]

                if sorted([ul,ur,ll,lr]) == ['M','M','S','S'] and ul !=lr:
                    cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()
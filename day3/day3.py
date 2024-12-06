import re 
import string

def muli(x:int,y:int) -> int:
    return x*y


def process_line(line:str):
    output = 0
    remove_list = str.maketrans('','','mul()')
    iteams = re.findall('mul\(\d{1,3},\d{1,3}\)',line)
    for i in iteams:
        splt_val = i.translate(remove_list).split(',')
        output += muli(int(splt_val[0]),int(splt_val[1]))

    return output
    


def main() -> None:
    list_to_mul = list()
    with open('input.txt','r') as f:
        data = [line.rstrip() for line in f]

    for line in data:
        line += 'do()'
        line = re.sub("don't\(\).+?do\(\)", '', line)
        list_to_mul.append(process_line(line))


    print(sum(list_to_mul))

if __name__ == "__main__":
    main()
import sys

def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            all_list=[]
            for line in f:
                items=[ item for item in line.strip().split(" ")] 
                all_list.append(items)
        input_list=[]
        for list in all_list:
            if len(list) > 1:
                input_list.append(list)
        return input_list
    except FileNotFoundError:
        print(f"ERROR: There is either no such a file namely {sys.argv[1]} or this program does not have permission to read it!")
        print("Program is going to terminate!")

def solve_func(list):
    move=[]
    operations=['*','/','+','-']
    for sub_list in list:
        if len(sub_list) != 3:
            move.append("ERROR: Line format is erroneous!")
        else:
            try: 
                float_item=float(sub_list[0])
            except ValueError:
                move.append(sub_list) 
                move.append("ERROR: First operand is not a number!")
            try:
                float_item2=float(sub_list[2])
            except ValueError:    
                move.append(sub_list) 
                move.append("ERROR: Second operand is not a number!")    
                break
            if sub_list[1] == '*':
                    move.append(sub_list)
                    move.append(f"={float(sub_list[0])*float(sub_list[2]):.2f}")
            elif sub_list[1]=='+':
                    move.append(sub_list)
                    move.append(f"={float(sub_list[0])+float(sub_list[2]):.2f}")
            elif sub_list[1]=='/':
                    move.append(sub_list)
                    move.append(f"={float(sub_list[0])/float(sub_list[2]):.2f}")
            elif sub_list[1]=='-':
                    move.append(sub_list)
                    move.append(f"={float(sub_list[0])-float(sub_list[2]):.2f}")
            else:
                move.append(sub_list) 
                move.append("ERROR: There is no such an operator!")    
    return move

def write_output(file_name, input):
    with open(file_name, 'w') as f:
        list= solve_func(input)
        for lst in list:
            f.write(str(lst) + '\n')
def main():
    if len(sys.argv)!=3:
        print("ERROR: This program needs two command line arguments to run, where first one is the input file and the second one is the output file!")
        print("Sample run command is as follows: python3 calculator.py input.txt output.txt")
        print("Program is going to terminate!")
    else:
        input=(sys.argv[1])
        output=(sys.argv[2])
        input_list= read_file(input)
        write_output(output, input_list)
        
if __name__ == '__main__':
    main()



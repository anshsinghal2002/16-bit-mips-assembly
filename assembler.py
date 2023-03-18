import Instruction_Word_100
label_dict={}


def label(file):
    file_to_assemble = open(file,'r') 
    lines = []
    for line in file_to_assemble:
        new_line = ''
        for ch in line:
            if ch=="#":
                break
            else:
                new_line+=ch
        if new_line!='\n' and new_line!='':
            lines.append(new_line)
    for i,line in enumerate(lines):
        if line.split()[0][0]=="!":
            label_dict[line.split()[0]]=i
    f = open('test.asm','w')
    for i, line in enumerate(lines):
        line=line.split()
        if '\n' in line:
            line.remove('\n')
        if i in label_dict.values():
            line=line[1:]
        if line[-1].isnumeric() or line[-1][1:].isnumeric():
            f.write(' '.join(line))
        else:
            new_num = calc_label(line[-1],i)
            new_line = line[:-1]+[str(new_num)]
            f.write(' '.join(new_line))
        f.write('\n')
    f.close()

        
    file_to_assemble.close()

def calc_label(label,curr_line_no):
    return label_dict[label]-curr_line_no-1
def main():
    file='test_files/'+'testbranch.asm'
    label(file)
    file_to_assemble = open('test.asm','r') 
    translator = Instruction_Word_100.Translator()
    f=open('output.hex','w')
    f.write('v2.0 raw\n')
    for line in file_to_assemble:
        machine_code = translator.compile(line)
        print (machine_code)
        f.write(machine_code)
        f.write(' ')
    f.close()
    file_to_assemble.close()

if __name__ == "__main__":
    main()

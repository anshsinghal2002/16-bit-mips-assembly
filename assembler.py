import Instruction_Word

def main():
    file_to_assemble = open('test_files/'+'Basic-R-Type-rev2.asm','r') 
    translator = Instruction_Word.Translator()
    f=open('output.hex','w')
    f.write('v2.0 raw\n')
    for line in file_to_assemble:
        print (line)
        machine_code = translator.compile(line)
        if machine_code!='ERROR':
            print (translator.bs2hex(machine_code))
            f.write(translator.bs2hex(machine_code))
            f.write(' ')
    f.close()
    file_to_assemble.close()

if __name__ == "__main__":
    main()

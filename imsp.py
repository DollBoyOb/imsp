import sys
heap = [0]*9
f = open(sys.argv[1]).readlines()
n = 0

while n!=len(f):
    com = f[n].split()

    match com[0]:
        case "0": 
            if com[1] == "1": print(chr(int("".join(com[2:])[::-1])), end="")
            if com[1] == "2":
                num = "".join(com[3:])
                leng = len(num)
                num = str((int(num) - int(com[2]*leng)) + (10**leng))[1:]

                print(chr(int(num, int(com[1]))), end="")
            if com[1] == "3": print(heap[int(com[2])], end="")
            if com[1] == "4": 
                heap[int(com[2])] = input()
                if heap[int(com[2])].isdigit(): heap[int(com[2])] = int(heap[int(com[2])])
        case "1": 
            if int(com[2]) == 3:
                heap[int(com[1])] = heap[int(com[3])][heap[int(com[4])]]
            elif int(com[2]) == 2:
                heap[int(com[1])] = heap[int(com[3])]
            elif int(com[2]) == 1:
                heap[int(com[1])] = int(com[3])
            elif int(com[2]) == 0:
                heap[int(com[1])] = chr(int("".join(com[3:])[::-1]))
        case "2":
            ops = ["+", "-", "*", "/", "%"]            
            eval_str = str(heap[int(com[1])])+ops[int(com[2])]+str(heap[int(com[3])])
            
            # Checks if both cells is string
            if [type(heap[int(com[1])]), type(heap[int(com[3])])] == [str,str]: 
                eval_str = str(f" '{heap[int(com[1])]}'{ops[int(com[2])]}'{heap[int(com[3])]}' ")
            
            heap[int(com[4])] = eval(eval_str)
        case "3":
            eqs = ["==", "<", ">", "!="]
            # Example: 1-eval("30<10") = 1-False = 1
            # n is a pointer, and in this example, pointer just skips next line of code
            n+=(1-eval(str(f" '{heap[int(com[1])]}'{eqs[int(com[2])]}'{heap[int(com[3])]}' "))) 
        case "4":
            n = int(com[1])-1
        case "5": break

    n+=1

# python3



class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    #text = sys.stdin.read()
    with open("Testing_file.txt") as f:
        text = f.read()
    opening_brackets_stack = []
    flag =0
    for i, item in enumerate(text):
        #print ([i.bracket_type for i in opening_brackets_stack])
        if item == '(' or item == '[' or item == '{':
            c = Bracket(item, i)
            opening_brackets_stack.append(c)

        if item == ')' or item == ']' or item == '}':
            try: #in case that the stack is empty
                a = opening_brackets_stack.pop()
                if a.Match(item):
                    continue
                else:
                    flag =1
                    print (i+1)
                    break
            except:
                flag=1
                print(i+1)
                break
    if flag==0:
        if (len(opening_brackets_stack) ==0):
            print ("Success")
        else:
            a = opening_brackets_stack.pop()
            print (a.position+1)
        
    
    
    

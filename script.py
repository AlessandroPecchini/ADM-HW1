# es1: Say "Hello, World!" With Python
def es1():
    print("Hello, World!")

# es2: Python If-Else
def es2():

    import math
    import os
    import random
    import re
    import sys

    if __name__ == '__main__':
        n = int(input().strip())
        if n%2 == 1:
            print("Weird")
        elif n<=5:
            print("Not Weird")
        elif n<=20:
            print("Weird")
        else:
            print("Not Weird")

# es3: Arithmetic Operators
def es3():
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        print(f'{a+b}\n{a-b}\n{a*b}')

# es4: Python: Division
def es4():
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
        print(f'{a//b}\n{a/b}')

# es5: Loops
def es5():
    if __name__ == '__main__':
        n = int(input())
        for i in range(n):
            print(i**2)


# es6: Write a function
def es6():
    def is_leap(year):
        quattro = year%4==0
        cento = year%100==0
        qcento = year%400==0
        leap = quattro and qcento
        return leap or (quattro and not cento)
        
    year = int(input())
    print(is_leap(year))


# es7: Print Function
def es7():
    if __name__ == '__main__':
        n = int(input())
        out = ""
        for i in range(1, n+1):
            out+=str(i)
        print(out)


# es8: List Comprehensions
def es8():
    if __name__ == '__main__':
        x = int(input())
        y = int(input())
        z = int(input())
        n = int(input())
        print([[i, j , k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])


# es9: Find the Runner-Up Score!
def es9():
    if __name__ == '__main__':
        n = int(input())
        arr = list(map(int, input().split()))
        if len(arr)>0:
                
            ret = min(arr)
            max_v = max(arr)
            for s in arr:
                if s > ret and s < max_v:
                    ret = s
            print(ret)

# es10: Nested Lists
def es10():
    if __name__ == '__main__':
        names = []
        scores = []
        sec_min = None
        for _ in range(int(input())):
            names.append(input())
            score = float(input())
            scores.append(score)
        sec_min = min([s for s in scores if s > min(scores)])
        ret = [names[i] for i in range(len(scores)) if scores[i]==sec_min]
        for n in sorted(ret):
            print(n)


# es11: finding the percentage
def es11():
    if __name__ == '__main__':
        n = int(input())
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        averaged = {x: sum(student_marks[x])/(len(student_marks[x])*1.0) for x in student_marks.keys()}
        query_name = input()
        print("{:.2f}".format(averaged[query_name]))


# es12: sWAP cASE
def es12():
    def swap_case(s):
        ret = ""
        for c in s:
            ret += c.upper() if c.islower() else c.lower()
            
        return ret

    if __name__ == '__main__':
        s = input()
        result = swap_case(s)
        print(result)


# es13: String Split and Join
def es13():
    def split_and_join(line):
        return '-'.join(line.split(" "))

    if __name__ == '__main__':
        line = input()
        result = split_and_join(line)
        print(result)

# es14: What's Your Name?
def es14():
    #
    # Complete the 'print_full_name' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts following parameters:
    #  1. STRING first
    #  2. STRING last
    #

    def print_full_name(first, last):
        print(f"Hello {first} {last}! You just delved into python.")

    if __name__ == '__main__':
        first_name = input()
        last_name = input()
        print_full_name(first_name, last_name)


# es15: Mutations
def es15():
    def mutate_string(string, position, character):
        return string[:position] + character + string[position+1:]

    if __name__ == '__main__':
        s = input()
        i, c = input().split()
        s_new = mutate_string(s, int(i), c)
        print(s_new)


# es16: Find a String
def es16():
    def count_substring(string, sub_string):
        count = 0
        for i in range(len(string)-len(sub_string)+1):
            if string[i:i+len(sub_string)] == sub_string:
                count += 1
        return count

    if __name__ == '__main__':
        string = input().strip()
        sub_string = input().strip()
        
        count = count_substring(string, sub_string)
        print(count)

# es17: String Validators
def es17():
    def contains_true(s, func):
        for ch in s:
            if func(f"{ch}"):
                return True
        return False

    if __name__ == '__main__':
        s = input()
        digit = contains_true(s, str.isdigit)
        alpha = contains_true(s, str.isalpha)
        alnum = digit or alpha
        lower = contains_true(s, str.islower)
        upper = contains_true(s, str.isupper)
        for b in [alnum, alpha, digit, lower, upper]:
            print(b)
            

# es18: Text Alignments
def es18():
    #Replace all ______ with rjust, ljust or center. 

    thickness = int(input()) #This must be an odd number
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# es19: Text Wrap
def es19():
    import textwrap

    def wrap(string, max_width):
        ret = ""
        for i in range(len(string)):
            if i>0 and (i)%(max_width) == 0:
                ret+='\n'
            ret+= string[i]
        return ret

    if __name__ == '__main__':
        string, max_width = input(), int(input())
        result = wrap(string, max_width)
        print(result)

# es20: Designer Door
def es20():
    # Enter your code here. Read input from STDIN. Print output to STDOUT

    def add_caps(string, cap):
        return cap + string + cap

    def add_ends(string) : return add_caps(string, '.|.')

    def remove_caps (string, cap):
        return string[len(cap): len(string)-len(cap)]
    def remove_ends(string): return remove_caps(string, '.|.')

    datas = input()
    n, m = map(lambda x: int(x), datas.split(' '))
    initial = '.|.'

    # Adding the first line
    lines = [initial.center(m, '-')]

    last_line = initial

    # Adding the lines 'till WELCOME
    for l in range(1, n//2):
        last_line = add_ends(last_line)
        lines.append(last_line.center(m, '-'))
        
    # Adding the central line and the first of the decreasing lines
    lines.append('WELCOME'.center(m, '-'))
    lines.append(last_line.center(m, '-'))

    # Adding the decreasing lines 'till the end
    for l in range(1, n//2):
        last_line = remove_ends(last_line)
        lines.append(last_line.center(m, '-'))

    print('\n'.join(lines))


# es21: String Formatting
def es21():
    def print_formatted(number):
    # your code goes here
        max_width = len(bin(number))-2
        for i in range(1, number+1):
            print(f"{str(i).rjust(max_width)} {oct(i)[2:].rjust(max_width)} {hex(i)[2:].upper().rjust(max_width)} {bin(i)[2:].rjust(max_width)}")

    if __name__ == '__main__':
        n = int(input())
        print_formatted(n)

# es22: Introduction to Sets 
def es22():
    def average(array):
        # your code goes here
        h = set(array)
        return sum(h)/len(h)

    if __name__ == '__main__':
        n = int(input())
        arr = list(map(int, input().split()))
        result = average(arr)
        print(result)

# es23:  Merge the Tools
def es23():
    def once_string(string, start=0, end=None):
        if end is None:
            end = len(string)
        choosen = set()
        ret = ""
        for i in range(start, end):
            ch = string[i]
            if ch not in choosen:
                choosen.add(ch)
                ret += ch
        return ret
    def merge_the_tools(string, k):
        # your code goes here
        for i in range(0, len(string)-k+1, k):
            print(once_string(string,i, i+k))
            

    if __name__ == '__main__':
        string, k = input(), int(input())
        merge_the_tools(string, k)


# es24: The Minion Game
def es24():
    def minion_game(string):
    # your code goes here
        letter_vowels = {'A', 'E', 'I', 'O', 'U'}
        kevin = 0
        stuart = 0
        
        for i in range(len(string)):
            if string[i] in letter_vowels:
                kevin += len(string)-i
            else:
                stuart += len(string)-i
        print(f"Kevin {kevin}" if kevin > stuart else f"Stuart {stuart}" if kevin<stuart else "Draw")
        
    if __name__ == '__main__':
        s = input()
        minion_game(s)

# es25: Capitalize!
def es25():
    import math
    import os
    import random
    import re
    import sys

    # Complete the solve function below.
    def solve(s):
        ret = ""
        for n in s.split(' '):
            ret+= n.capitalize() + " "
        return ret[:-1]

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        s = input()

        result = solve(s)

        fptr.write(result + '\n')

        fptr.close()


# es26: Alphabet Rangoli
def es26():
    def add_rangoli(string, ch):
        l = len(string)
        if l%2 == 0:
            return ""
            #raise ValueError(f"This function works only with even-sized strings")
        middle = string[l//2]
        return string[:l//2] + middle + '-' + ch + '-' + middle + string[l//2+1:]

    def rm_rangoli(string):
        l = len(string)
        if l%2 == 0:
            return ""
            #raise ValueError(f"This function works only with even-sized strings")
        if l < 5: return ""

        if l == 5:
            return string[0]
        return string[:l//2] + string[l//2+4:]

    def print_rangoli(size):
        # your code goes here
        width = 4*size-3 
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        last_line = alphabet[size-1]
        lines = [last_line.center(width, '-')]
        for l in range(size-2, -1, -1):
            last_line = add_rangoli(last_line, alphabet[l])
            lines.append(last_line.center(width, '-'))
        for l in range(size-1):
            last_line = rm_rangoli(last_line)
            lines.append(last_line.center(width, '-'))
            
        print('\n'.join(lines))
            
        
    if __name__ == '__main__':
        n = int(input())
        print_rangoli(n)

# es27: Symmmetric Difference
def es27():
        # Enter your code here. Read input from STDIN. Print output to STDOUT
    m = input()
    m_set = set(map(int, input().split()))
    n = input()
    n_set = set(map(int, input().split()))
    for val in sorted(m_set.union(n_set).difference(m_set.intersection(n_set))):
        print(val)

# es28: No Idea!
def es28():
        # Enter your code here. Read input from STDIN. Print output to STDOUT
    input()
    n_arr= map(int, input().split())
    a_set = set(map(int, input().split()))
    b_set = set(map(int, input().split()))
    ret = 0
    for v in n_arr:
        if v in a_set:
            ret += 1
        elif v in b_set:
            ret -= 1
    print(ret)


# es29: Set. add()!
def es29():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    n = int(input())
    cs = set()
    for _ in range(n):
        cs.add(input())
    print(len(cs))


# es30: Set .discard(), .remove() & .pop()
def es30():
    n = int(input())
    s = set(map(int, input().split()))
    n_op = int(input())
    for _ in range(n_op):
        line = input()
        if ' ' in line:
            op, val = line.split()
            if op == 'remove':
                s.remove(int(val))
            else:
                s.discard(int(val))
        else:
            s.pop()
        
    print(sum(s))

# es31: Set .union() Operation
def es31():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    input()
    e = set(input().split())
    input()
    f = set(input().split())
    print(len(e|f))


# es32: The Captain's Room
def es32():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    k = input()
    rooms = list(map(int, input().split()))
    captain = set(rooms)
    found = set()
    for r in list(rooms):
        if r in found:
            captain.discard(r)
        else:
            found.add(r)
    print(captain.pop())


# es 33: Set Mutations
def es33():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    input()
    a = set(map(int,input().split()))
    n_op = int(input())
    for _ in range(n_op):
        op, _ = input().split()
        b = set(map(int,input().split()))
        if op == 'intersection_update':
            a.intersection_update(b)
        elif op == 'update':
            a.update(b)
        elif op == 'symmetric_difference_update':
            a.symmetric_difference_update(b)
        else:
            a.difference_update(b)
    print(sum(a))


# es34: Set .symmetric_difference() Operation
def es34():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    input()
    e = set(input().split())
    input()
    f = set(input().split())
    print(len(e^f))


# es35: Set .difference() Operation
def es35():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    input()
    e = set(input().split())
    input()
    f = set(input().split())
    print(len(e-f))


# es36: Set .intersection() Operation
def es36():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    input()
    e = set(input().split())
    input()
    f = set(input().split())
    print(len(e&f))


# es37: Collections.namedtuple()
def es37():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from collections import namedtuple
    n = int(input())
    Studente = namedtuple('Studente', input())
    print(sum([float(Studente(*input().split()).MARKS) for _ in range(n)])/n)


# es38: DefaultDict Tutorial
def es38():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from collections import defaultdict

    n, m = map(int, input().split())
    a = defaultdict(set)
    for i in range(n):
        w = input()
        a[w].add(i+1)
    for _ in range(m):
        w = input()
        print(f"{' '.join(map(str, sorted(a[w])))}" if len(a[w])>0 else "-1")


# es389: collections.Counter()
def es39():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from collections import Counter

    input()
    warehouse = Counter(map(int, input().split()))
    c = int(input())
    tot = 0
    for _ in range(c):
        size, val = map(int, input().split())
        if warehouse[size] > 0:
            tot += val
            warehouse[size] -= 1
    print(tot)


# es40: Check Strict Superset
def es40():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    a = set(map(int, input().split()))
    n = int(input())
    ret = True
    for _ in range(n):
        b = set(map(int, input().split()))
        if len(a)>len(b) and b.intersection(a)==b:
            continue
        ret = False
        break

    print(ret)


# es41: Check Subset
def es41():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    tc = int(input())
    for _ in range(tc):
        input()
        a = set(map(int, input().split()))
        input()
        b = set(map(int, input().split()))
        print(a.intersection(b)==a)

# es42: Company Logo
def es42():
    import math
    import os
    import random
    import re
    import sys

    from collections import Counter

    if __name__ == '__main__':
        c = Counter(input())
        max_three = [(None, 0), (None, 0), (None, 0)]
        count = 0
        for k,v in sorted(c.items(), key=lambda t: (-1*t[1], ord(t[0]))):
            print(f"{k} {v}")
            count += 1
            if count >= 3:
                break


# es43: Piling Up!
def es43():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    t = int(input())
    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))
        m = max(blocks[0], blocks[-1])
        out = "Yes"
        for i in range(1, n-1):
            if blocks[i] > m:
                out = "No" 
                break
        print(out)


# es44: Collections.Deque()
def es44():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from collections import deque
    n = int(input())
    d = deque()
    for _ in range(n):
        line = input()
        if ' ' in line:
            word, val = line.split()
            if word=='append':
                d.append(val)
            else:
                d.appendleft(val)
        else:
            if line=='pop':
                d.pop()
            else:
                d.popleft()
    print(' '.join(d))


# es45: Word Order
def es45():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from collections import OrderedDict
    words = OrderedDict()
    n = int(input())
    for _ in range(n):
        w = input()
        words[w] = words.get(w, 0) + 1
    print(f"{len(words)}\n{' '.join(map(str, words.values()))}")


# es46: Collections.OrderedDict()
def es46():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from collections import OrderedDict
    summary = OrderedDict()
    for _ in range(int(input())):
        line = input().split()
        prod = ' '.join(line[:-1])
        price = int(line[-1])

        summary[prod] = summary.get(prod, 0) + price
        
    for k in summary:
        print(f"{k} {summary[k]}")


# es47: Calendar Module
def es47():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import calendar
    mm, dd, yyyy = map(int,input().split())
    week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    print(week[calendar.weekday(yyyy, mm, dd)])


# es48: Time Delta
def es48():
    import math
    import os
    import random
    import re
    import sys
    import datetime
    # Complete the time_delta function below.
    #Day dd Mon yyyy hh:mm:ss +xxxx
    def time_delta(t1, t2):
        dt1 = datetime_object = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
        dt2 = datetime_object = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z").astimezone(dt1.tzinfo)
        return str(abs(int((dt1-dt2).total_seconds())))
            
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        t = int(input())

        for t_itr in range(t):
            t1 = input()

            t2 = input()

            delta = time_delta(t1, t2)

            fptr.write(delta + '\n')

        fptr.close()


# es49: Exceptions
def es49():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    t = int(input())
    for _ in range(t):
        try:
            a, b = map(int, input().split())
            print(a//b)
        except (ZeroDivisionError, ValueError) as e:
            print(f"Error Code: {e}")


# es50: Zipped!
def es50():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    n, x = map(int, input().split())
    marks = [list(map(float,input().split())) for _ in range(x)]
    zipped = zip(*marks)
    #print(list(zipped))
    avgs = [sum(z)/x for z in zipped]
    for avg in avgs:
        print("{:.1f}".format(avg))


# es51: Athlete Sort
def es51():
    import math
    import os
    import random
    import re
    import sys



    if __name__ == '__main__':
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        arr = []

        for _ in range(n):
            arr.append(list(map(int, input().rstrip().split())))

        k = int(input())
        for l in sorted(arr, key=lambda line: line[k]):
            print(' '.join(map(str, l)))


# es52: ginortS
def es52():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    print(''.join(sorted(sorted(input()), key=lambda c: (c.islower(), c.isalpha(), c.isdigit() and int(c)%2==1), reverse=True)))


# es53: Map and Lambda functions
def es53():
    cube = lambda x: x**3# complete the lambda function 
    fib_base = [0, 1]
    def fibonacci(n):
        # return a list of fibonacci numbers
        if n == 0:
            return []
        if n==1:
            return [fib_base[0]]
        if n == 2:
            return fib_base
        
        ret = fib_base[:]
        for i in range(1, n-1):
            ret.append(ret[i-1]+ret[i])
        return ret
        
        
    if __name__ == '__main__':
        n = int(input())
        print(list(map(cube, fibonacci(n))))


# es54: Birthday Candles
def es54():
    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'birthdayCakeCandles' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts INTEGER_ARRAY candles as parameter.
    #
    from collections import Counter
    def birthdayCakeCandles(candles):
        # Write your code here
        return Counter(candles)[max(candles)]

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        candles_count = int(input().strip())

        candles = list(map(int, input().rstrip().split()))

        result = birthdayCakeCandles(candles)

        fptr.write(str(result) + '\n')

        fptr.close()


# es55: Detecting floating point numbers
def es55():
    # Enter your code here. Read input from STDIN. Print output to STDOUT

    import re

    for _ in range(int(input())):
        line = input()
        rm = re.match(r'(\+|-)?\d*\.\d+$', line)
        print(bool(rm))


# es56: re.Split()
def es56():
    regex_pattern = r"\.|,"	# Do not delete 'r'.
    import re
    print("\n".join(re.split(regex_pattern, input())))

# es 57: Group(), Groups() & Groupdict()
def es57():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    pattern = r".*?(?P<ch>[A-Za-z0-9])(?P=ch)+"
    match = re.match(pattern, input())
    print(match.groupdict().get('ch', ['-1'])[0] if match is not None else '-1')


# es58: Re.findall() & Re.finditer()
def es58():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    reg = r"(?<=[^aeiouAEIOU])([aeiouAEIOU][aeiouAEIOU]+)(?=[^aeiouAEIOU])"
    mathces = re.findall(reg,input())
    if len(mathces) == 0:
        print(-1)
    else:
        for m in mathces:
            print(m)


# es59: Re.start() & Re.end()
def es59():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    s = input()
    k = input()
    start = 0
    found = False
    while start <= len(s):
        match = re.search(k, s[start:])
        
        if not match:
            if not found:
                print("(-1, -1)")
            break
        else:
            found = True
            print(f"({start + match.start()}, {start + match.end()-1})")
            start += match.start()+1


# es60: Regex Substitution
def es60():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    for _ in range(int(input())):
        print(re.sub(r"(?<=\s)(&&)(?:\s)", 'and ', re.sub(r"(?<=\s)(\|\|)(?:\s)", 'or ', input())))


# es61: Validating Roman Numerals
def es61():
    regex_pattern = r"^M{0,3}(?:C[MD]|D?C{0,3})(?:X[CL]|L?X{0,3})(?:I[XV]|V?I{0,3})$"
    import re
    print(str(bool(re.match(regex_pattern, input()))))


# es62: HTML Parser - part1
def es62():
    from html.parser import HTMLParser

    # create a subclass and override the handler methods
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            tag=tag.strip()
            print(f"Start : {tag}")
            self.print_attributes(attrs)
        def handle_endtag(self, tag):
            tag = tag.strip()
            print(f"End   : {tag}")
        def handle_startendtag(self, tag, attrs):
            tag = tag.strip()
            print(f"Empty : {tag}")
            self.print_attributes(attrs)

        def print_attributes(self, attrs):
            #print(f"Attributi passati: {attrs}")
            for k,v in attrs:
                print(f"-> {k.strip()} > {str(v).strip()}")
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    for i in range(int(input())):
        l = input()
        #print(l)
        parser.feed(l)

# es63: HTML Parser -part2
def es63():
    from html.parser import HTMLParser

    class MyHTMLParser(HTMLParser):
    
    
        def handle_data(self, data):
            #return super().handle_data(data)
            if len(data.strip()) == 0:
                return
            print(">>> Data")
            print(data)

        def handle_comment(self, data):
            #return super().handle_comment(data)
            if len(data.strip()) == 0:
                return
            print(">>> " + ("Multi" if '\n' in data else "Single") + "-line Comment")
            print(data)# if not data.startswith(' ') else data[1:])
    
    
    html = ""       
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
        
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()


# es64: Detect HTML Tags, Attributes and Attribute Values
def es64():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    from html.parser import HTMLParser

    def print_attrs(attrs):
        for k,v in attrs:
            print(f"-> {k.strip()} > {v.strip()}")

    class MyParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print(tag)
            print_attrs(attrs)
            #return super().handle_starttag(tag, attrs)
        
        def handle_startendtag(self, tag, attrs):
            #print(f"STARTEND: {tag}, {attrs}")
            return self.handle_starttag(tag, attrs)
        
    mp = MyParser()
    for _ in range(int(input())):
        line = input()
        
        mp.feed(line)


# es65: Validating UID
def es65():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    for _ in range(int(input())):
        if re.match(r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$", input()):
            print("Valid")
        else:
            print("Invalid")


# es66: Validating Credit Card Numbers
def es66():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re

    for _ in range(int(input().strip())):
        l = input()
        match = bool(re.search(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$', l))
        print("Valid" if match else "Invalid")


# es67: Validating Postal Codes
def es67():
    regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

    import re
    P = input()

    print (bool(re.match(regex_integer_in_range, P)) 
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# es68: Matrix Script
def es68():

    import math
    import os
    import random
    import re
    import sys

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []
    for_column = ["" for _ in range(m)]

    def replace_sym(string):
        #print(f"String: {string}")
        patt = r"(?<=[a-zA-Z0-9])([!@#$%&\s]+)(?=[a-zA-Z0-9])"
        #for f in re.findall(r"[a-zA-Z0-9]([!@#$%&\s]+)[a-zA-Z0-9]", string):
            #print(f)
        print(f"{re.sub(patt, ' ', string)}")

    for _ in range(n):
        matrix_item = input()
        for i in range(m):
            for_column[i] += matrix_item[i]
        matrix.append(matrix_item)

    replace_sym(''.join(for_column))


# es69: XML 1 -find the score
def es69():
    import sys
    import xml.etree.ElementTree as etree

    def get_attr_number(node):
        return len(node.attrib) + sum(get_attr_number(ch) for ch in node)

    if __name__ == '__main__':
        sys.stdin.readline()
        xml = sys.stdin.read()
        tree = etree.ElementTree(etree.fromstring(xml))
        root = tree.getroot()
        print(get_attr_number(root))

# es70: XML2 - Find the Maximum Depth
def es70():
    import xml.etree.ElementTree as etree

    maxdepth = 0
    def depth(elem, level):
        global maxdepth
        #print(f"I'm {elem.tag} of level: {level} wit maxdepth: {maxdepth}")
        if len(elem) == 0:
            maxdepth = max(maxdepth, level + 1)
        else:
            for ch in elem:
                depth(ch, level+1)

        # your code goes here

    if __name__ == '__main__':
        n = int(input())
        xml = ""
        for i in range(n):
            xml =  xml + input() + "\n"
        tree = etree.ElementTree(etree.fromstring(xml))
        depth(tree.getroot(), -1)
        print(maxdepth)

# es71: Standardize Mobile Number Using Decorators
def es71():
    def wrapper(f):
    #print(f"Called wrapper with function: {f}")
        def fun(l):
            #print(f"Called fun with l: {l} and function: {f}")
            ret = [f"{pn[len(pn)-10:][:5]} {pn[len(pn)-10:][5:]}" for pn in l]
            #print(sorted(ret))
            return f([f"+91 {n}" for n in ret])
        return fun

    @wrapper
    def sort_phone(l):
        print(*sorted(l), sep='\n')

    if __name__ == '__main__':
        l = [input() for _ in range(int(input()))]
        sort_phone(l) 

# es72: Decorators 2 - Name Directory
def es72():
    import operator

    def person_lister(f):
        #print(f"Called pl from function: {f}")
        def inner(people):
            #print(f"Called inner from f: {f} and people: {people} and type: {type(people)}")
            if people is None: return None
            return [f(p) for p in sorted(people, key= lambda l: int(l[2]))]
        return inner

    @person_lister
    def name_format(person):
        return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

    if __name__ == '__main__':
        people = [input().split() for i in range(int(input()))]
        print(*name_format(people), sep='\n')

# es73: Array
def es73():
    import numpy

    def arrays(arr):
        # complete this function
        # use numpy.array
        return numpy.array(list(reversed(arr)), float)

    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)


# es74: Shape() and reShape()
def es74():
    import numpy
    print(numpy.array(list(map(int, input().split()))).reshape(3,3))


# es75: Transpose and Flatten
def es75():
    import numpy

    mat = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
    print(numpy.array(mat).transpose())
    print(numpy.array(mat).flatten())


# es76: Concatenate
def es76():
    import numpy
    n, m, _ = map(int, input().split())
    arr1 = numpy.array([list(map(int, input().split()))for _ in range(n)])
    arr2 = numpy.array([list(map(int, input().split()))for _ in range(m)])
    print(numpy.concatenate((arr1,arr2)))


# es77: Zeros and Ones
def es77():
    import numpy


    shape = tuple(map(int, input().split()))
    print(numpy.zeros(shape, int))
    print(numpy.ones(shape, int))


# es78: Eye and Identity
def es78():
    import numpy
    numpy.set_printoptions(legacy='1.13', suppress= True)
    print(numpy.eye(*map(int, input().split())))


# es79: Array Mathematichs
def es79():
    import numpy
    numpy.set_printoptions(legacy='1.13', suppress=True)
    n, m = map(int, input().split())
    a = [numpy.array([list(map(int, input().split())) for _ in range(n)])]
    b = [numpy.array([list(map(int, input().split())) for _ in range(n)])]
    functions = [numpy.add, numpy.subtract, numpy.multiply, numpy.floor_divide, numpy.mod, numpy.power]

    for f in functions:
        print(f(a,b)[0])


# es80: Floor, Ceil and Rint
def es80():
    import numpy
    numpy.set_printoptions(legacy='1.13', suppress=True)
    a = numpy.array(list(map(float, input().split())))
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))


# es81: Sum and Prod
def es81():
    import numpy

    print(numpy.product(
            numpy.sum(
                numpy.array([
                        list(map(int, input().split())) for _ in range(int(input().split()[0]))
                    ]),
                    axis=0
                )
            )
        )


# es 82: Min and Max
def es82():
    import numpy

    print(numpy.max(
            numpy.min(
                numpy.array([
                    list(map(int, input().split())) for _ in range(int(input().split()[0]))
                ]),
                axis=1
            )
        )
    )


# es83: Mean, Var, and Std
def es83():
    import numpy
    import math
    a = numpy.array(
                [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
            )
    print(numpy.mean(a, axis=1))
    print(numpy.var(a, axis=0))
    print(round(numpy.std(a), 11))

# es84: Dot and Cross
def es84():
    import numpy
    n = int(input())
    arr1 = numpy.array([list(map(int, input().split()))for _ in range(n)])
    arr2 = numpy.array([list(map(int, input().split()))for _ in range(n)])
    print(numpy.matmul(arr1, arr2))


# es85: Inner and Outer
def es85():
    import numpy
    arr1 = numpy.array(list(map(int, input().split())))
    arr2 = numpy.array(list(map(int, input().split())))
    print(numpy.inner(arr1, arr2))
    print(numpy.outer(arr1, arr2))


# es86: Polynomials
def es86():
    import numpy
    pol = list(map(float, input().split()))
    x = int(input())
    print(numpy.polyval(pol, x))


# es87: Linear Algebra
def es87():
    import numpy

    n = int(input())
    arr1 = numpy.array([list(map(float, input().split()))for _ in range(n)])
    print(round(numpy.linalg.det(arr1), 2))


# es88: Recursive Digit Sum
def es88():
    import math
    import os
    import random
    import re
    import sys

    def superDigit(n, k):
        # Write your code here
        s = sum(map(int, n)) * k
        while s >= 10:
            s = sum(map(int, str(s)))
        return s
            
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        first_multiple_input = input().rstrip().split()

        n = first_multiple_input[0]

        k = int(first_multiple_input[1])

        result = superDigit(n, k)

        fptr.write(str(result) + '\n')

        fptr.close()


# es89: number Line Jumps
def es89():
    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'kangaroo' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts following parameters:
    #  1. INTEGER x1
    #  2. INTEGER v1
    #  3. INTEGER x2
    #  4. INTEGER v2
    #

    def kangaroo(x1, v1, x2, v2):
        if v1<=v2 or (x2-x1)%(v2-v1)!= 0:
            return 'NO'
        else:
            return 'YES'

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        first_multiple_input = input().rstrip().split()

        x1 = int(first_multiple_input[0])

        v1 = int(first_multiple_input[1])

        x2 = int(first_multiple_input[2])

        v2 = int(first_multiple_input[3])

        result = kangaroo(x1, v1, x2, v2)

        fptr.write(result + '\n')

        fptr.close()


# es90: Viral Advertising
def es90():
    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'viralAdvertising' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts INTEGER n as parameter.
    #

    def viralAdvertising(n):
        # Write your code here
        if n==1:
            return 2
        else:
            last = 2
            cum = 2
            for i in range(n-1):
                last = last*3
                last = last//2
                cum += last
            return cum

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input().strip())

        result = viralAdvertising(n)

        fptr.write(str(result) + '\n')

        fptr.close()


# es91: Insertion sort -part 1
def es91():
    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'insertionSort1' function below.
    #
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. INTEGER_ARRAY arr
    #

    def insertionSort1(n, arr):
        # Write your code here
        n=n-1
        last = arr[n]
        if arr[n-1] < last:
            print(arr)
            return
        arr[n] = arr[n-1]
        for i in range(n, 0, -1):
            #print(F"i:{i} arr[i]: {arr[i]} last: {last}")
            if arr[i-1]<last:
                arr[i] = last
                print(' '.join(map(str, arr)))
                return
            else:
                arr[i] = arr[i-1]
                print(' '.join(map(str, arr)))
        arr[0] = last
        print(' '.join(map(str, arr)))

    if __name__ == '__main__':
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        insertionSort1(n, arr)


# es92: Insertion Sort -part 2
def es92():
    import math
    import os
    import random
    import re
    import sys

    #
    # Complete the 'insertionSort2' function below.
    #
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. INTEGER_ARRAY arr
    #

    def insert(arr, v):
        if len(arr) == 0:
            return [v]
        if len(arr) == 1:
            if arr[0] < v:
                return arr + [v]
            else:
                return [v] + arr
        if arr[-1] < v:
            return arr + [v]
        for i in range(len(arr)-2, -1, -1):
            #print(f"inside: arr[i]: {arr[i]} v: {v} arr: {arr}")
            if arr[i] < v:
                return arr[:i+1] + [v] + arr[i+1:]
        return [v] + arr 

    def insertionSort2(n, arr):
        # Write your code here
        for i in range(1, n):
            #print(f"i: {i} arr: {arr} arr[:i]: {arr[:i]} arr[i]: {arr[i]} arr[i+1:]: {arr[i+1:]}")
            arr = insert(arr[:i], arr[i]) + arr[i+1:]
            print(' '.join(map(str, arr)))

    if __name__ == '__main__':
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        insertionSort2(n, arr)


# es93: Lists
def es93():
    if __name__ == '__main__':
        N = int(input())
        arr = []
        for _ in range(N):
            line = input()
            if ' ' not in line:
                if line=='print':
                    print(arr)
                elif line == 'sort':
                    arr.sort()
                elif line == 'pop':
                    arr.pop()
                else:
                    arr.reverse()
            else:
                spline = line.split()
                if spline[0] == 'insert':
                    i, e = map(int, spline[1:])
                    arr.insert(i, e)
                elif spline[0] == 'remove':
                    arr.remove(int(spline[1]))
                else:
                    arr.append(int(spline[1]))


# es94: Tuple
def es94():
    if __name__ == '__main__':
        n = int(input())
        integer_list = map(int, input().split())
        print(hash(tuple(integer_list)))


# 95: Validating phone numbers
def es95():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    for _ in range(int(input())):
        if re.match(r"[789]{1}\d{9}$", input()):
            print('YES')
        else:
            print('NO')


# es96:Validating and Parsing Email Addresses
def es96():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    pattern = r"[A-Za-z]{1}[a-zA-Z0-9\.-_]+ <([a-z]{1}[a-z0-9\.\-_]+@[a-z]+\.[a-z]{1,3})>$"
    for _ in range(int(input())):
        line = input()
        if re.match(pattern , line):
            print(line)


# es97: Hex Color Code
def es97():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    pattern = r"([\w-]+:.*?|,\s+)(#{1}[0-9A-Fa-f]{6}|#{1}[0-9A-Fa-f]{3})"
    for _ in range(int(input())):
        for c in re.findall(pattern, input()):
            print(c[-1])
            
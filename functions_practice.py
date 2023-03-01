def hello():
    print('What it do babyyyyy?')

def pack(arg1,arg2,arg3):
    return[arg1,arg2,arg3]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f'First I eat {list[0]}.')
            else:
                print(f'Next I eat {list[i]}.')
    
hello()
print(pack(1,2,3))
print(pack('un','deux','trois'))
eat_lunch(['ice cream'])
eat_lunch(['cake','booty','muffins'])
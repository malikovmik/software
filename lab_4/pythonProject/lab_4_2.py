import random

def kubik():
    result = random.randint(1, 6)
    print(result)
    if result in (5, 6):
        print('Вы победили')
    elif result in (1, 2):
        print('Вы проиграли')
    else:
        return kubik()

if __name__=='__main__':
    kubik()

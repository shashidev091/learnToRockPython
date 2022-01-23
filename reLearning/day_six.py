# def find_prime_number(number):
#     if number % 2 == 0:
#         print("Prime number")
#     else:
#         print("")

def encode_msg():
    alphabets = list('abcdefghijklmnopqrstuvwxyz')

    cypher_type = input("Enter encode or decode\n")
    number = int(input('Enter no. to split \n'))
    msg = input('Input message \n')

    if cypher_type == 'encode':
        for index, item in enumerate(msg):
            idx = alphabets.index(item) + number
            if idx > len(alphabets):
                idx -= 26
                print(idx)
            msg = msg.replace(item, alphabets[idx])
    elif cypher_type == 'decode':
        for index, item in enumerate(msg):
            idx = alphabets.index(item) - number
            if idx > len(alphabets):
                idx += 26
                print(idx)
            msg = msg.replace(item, alphabets[idx])
    else:
        print("wrong input")
        return
    print(msg)


encode_msg()

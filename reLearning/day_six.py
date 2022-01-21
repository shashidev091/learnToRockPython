# def find_prime_number(number):
#     if number % 2 == 0:
#         print("Prime number")
#     else:
#         print("")

def encode_msg():
    alphabets = list('abcdefghijklmnopqrstuvwxyz')

    cypher_type = input("Enter encode or decode\n")
    number = input('Enter no. to split')

    msg = input('Input message')

    for item, index in enumerate(msg):
        msg[index] = ''



encode_msg()

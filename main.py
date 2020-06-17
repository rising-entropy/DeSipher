from os import system, name
import msvcrt
import rsa
import sys
from itertools import chain
import operator


def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res



def unpackTuple(tup): 
    res = [] 
    for i in chain(*tup): 
        res.append(i) 
    return res 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def Generate_Keys():
    clear()
    print("\n\n*************************Key Generation*************************\n")
    (pubkey, privkey) = rsa.newkeys(512)
    print("Your Public Keys 'n' and 'e' respectively are:")
    print(pubkey)
    print("\nYour Private Keys are:")
    print(privkey)
    print("Warning: Don't share your Private Keys with Anyone!")
    print("Press Any Key to Go Back")
    msvcrt.getch()
    home()



def Encrypt_Dat():
    clear()
    print("\n\n*************************Encryption*************************\n")
    print("Enter the Message to Encrypt:")
    contents = []
    while True:
        try:
            line = input()
            line.lstrip()
            line.rstrip()
            if len(line) == 0:
                break
        except EOFError:
            break
        contents.append(line)
    print("Enter 'n' of Receiver:")
    n = input()
    print("Enter 'e' of Receiver:")
    e = input()
    encry = []
    print("\nEncoded Message is:")
    for line in contents:
        mess = ConvertToInt(line)
        mess = pow(mess, int(e), int(n))
        encry.append(mess)
    for line in encry:
        print(line)
    
    print("\nPress Any Key to Continue.")
    msvcrt.getch()

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod


def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

def Decrypt(ciphertext, p, q, exponent):
  n = p*q
  m = (p-1)*(q-1)
  d = InvertModulo(exponent, m)
  return ConvertToStr(PowMod(ciphertext, d, n))


def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def Decrypt_Dat():
    clear()
    print("\n\n*************************Decryption*************************\n")
    print("Enter Message to Decrypt:")
    obey = []
    while True:
        try:
            line = input()
            line.lstrip()
            line.rstrip()
            if len(line) == 0:
                break
        except EOFError:
            break
        obey.append(int(line))
    
    print("\nEnter Private Key 'p':")
    p = int(input())
    print("\nEnter Private Key 'q':")
    q = int(input())
    print("\nEnter Your Public Key 'e':")
    e = int(input())

    print("\n\nMessage as Decrypted:")
    for line in obey:
        print(Decrypt(line, p, q, e))
    
    print("\nPress Any Key to Continue.")
    msvcrt.getch()
    home()

def home():
    clear()
    print("\n\n*************************DeSipher*************************\n")
    print("Choose your Action:")
    print("\t1. Encrypt Data.")
    print("\t2. Decrypt Data.")
    print("\t3. Generate Public and Private Keys.")
    print("\t4. Help with Process.")
    print("\t5. Credits.")
    print("\t6. Exit.")
    print("\nYour Choice: ", end='')
    inp = input()
    if inp == '1':
        Encrypt_Dat()
    elif inp == '2':
        Decrypt_Dat()
    elif inp == '3':
        Generate_Keys()
    elif inp == '4':
        Help_Me()
    elif inp == '5':
        Creds()
    elif inp == '6':
        sys.exit()
    else:
        print("Invalid Choice.")
        print("Try Again.")
        print("Press Any Key To Continue.")
        msvcrt.getch()
        home()

def Help_Me:
    clear()
    print("\n\n*************************Help*************************\n")
    print("The RSA Algorithm works on 2 important principles:")
    print("""\t1. You can't brute force a VERY large number. Hence the process is very secure.""")
    print("\t2. You can't decipher the code without the Private Keys.")
    print("\nI particularly found this note very Helpful with Implementation: \nhttp://www.math.toronto.edu/mathnet/soar/Spring/PDF/RSA.pdf")
    print("\nThis is also very-well explained in :\nhttps://www.coursera.org/learn/number-theory-cryptography")
    print("\n\nPress Any Key to Continue.")
    msvcrt.getch()
    home()


def Creds():
    clear()
    print("\n\nThis Project is made by me DevangK AKA rising-entropy")
    print("This is a passion project made after getting insired from 'The Imitation Game'.")
    print("I really hope this project inspires you towards Cryptography too and Thanks a lot for using this!")
    print("\n\nReach Me at: risingentropy20@gmail.com")
    print("\n\n\nPress Any Key to Continue.")
    msvcrt.getch()
    home()

home()

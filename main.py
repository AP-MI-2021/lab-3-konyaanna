def citire_lista():
    """
    functia citeste o lista
    :return: lista citita
    """
    l = []
    n = int(input("dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l

def is_prime(x):
    '''
    determina daca un numar este prim sau nu
    :param x: numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if (x < 2):
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(5)is True
    assert is_prime(7) is True
    assert is_prime(15) is False



def toate_nrprime (l):
    """
    verifica daca toate nr dintr-o lista sunt prime
    :param l: o lista de nr intregi
    :return: True, daca toate nr din lista sunt prime sau False in caz contrar
    """
    for i in range(len(l)):
        if is_prime(l[i])==False:
            return False
    return True
def test_is_toate_nrprime():
    assert toate_nrprime([5,7,13])is True
    assert toate_nrprime([7,41,37]) is True
    assert toate_nrprime([15,7,22]) is False


def get_longest_all_primes(l):
    """
        functia determina cea mai lunga subsecventa de numere prime
        :param lista: lista de numere intregi
        :return: cea mai lunga subsecventa de numere prime din lista
        """
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toate_nrprime(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max

#def test_get_longest_all_primes():
    #assert get_longest_all_primes([5,7,13,10,11])==[5,7,13]
    #assert get_longest_all_primes([7,41,37,5,9,8,7,3])==[7,41,37,5]
    #assert get_longest_all_primes([15,7,22])==[7]


def nrdivizori(x):
    '''
    determina nr de divizori ai unui nr
    :param x: numar intreg
    :return: nr de divizori ai lui x
    '''
    cont=0
    for i in range(1, x + 1):
        if x % i == 0:
            cont=cont+1
    return cont

def test_nrdivizori():
    assert nrdivizori(5)==2
    assert nrdivizori(4)==3
    assert nrdivizori(20)==6



def toate_nrdivizori (l):
    """
    verifica daca toate nr dintr-o lista au acelasi nr de divizori
    :param l: o lista de nr intregi
    :return: True, daca toate nr din lista au acelasi nr de divizori sau False in caz contrar
    """
    for i in range(len(l)-1):
        if nrdivizori(l[i])!=nrdivizori(l[i+1]):
            return False
    return True

def test_toate_nrdivizori():
    assert toate_nrdivizori([5,7,13])is True
    assert toate_nrdivizori([7,42,37]) is False
    assert toate_nrdivizori([15,7,22]) is False


def get_longest_same_div_count(l):
    """
        functia determina cea mai lunga subsecventa de numere cu acelasi nr de divizori
        :param lista: lista de numere intregi
        :return: cea mai lunga subsecventa de numere cu acelasi nr de divizori din lista
        """
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toate_nrdivizori(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([5,7,13,10,11])==[5,7,13]
    assert get_longest_same_div_count([7,41,37,5,9,8,7,3])==[7,41,37,5]
    assert get_longest_same_div_count([15,7,22,33,55])==[22,33,55]

def is_palindrome(n):
    '''
    functia verifica daca un numar este palindrom sau nu
    :param n: numar intreg
    :return: True, daca n este palindrom sau False, in caz contrar
    '''
    copie_n = n
    oglindit_n = 0
    while n > 0:
        oglindit_n = oglindit_n * 10 + n % 10
        n = n // 10
    if copie_n == oglindit_n:
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(5)is True
    assert is_palindrome(717) is True
    assert is_palindrome(1532) is False



def toate_palindrome (l):
    """
    verifica daca toate nr dintr-o lista sunt palindroame
    :param l: o lista de nr intregi
    :return: True, daca toate nr din lista sunt palindroame sau False in caz contrar
    """
    for i in range(len(l)):
        if is_palindrome(l[i])==False:
            return False
    return True

def test_is_toate_palindrome():
    assert toate_palindrome([515,7,131])is True
    assert toate_palindrome([7,414,37]) is False
    assert toate_palindrome([15,7,22]) is False


def get_longest_all_palindromes(l):
    """
        functia determina cea mai lunga subsecventa de numere palindroame
        :param lista: lista de numere intregi
        :return: cea mai lunga subsecventa de numere palindroame din lista
        """
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toate_palindrome(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([5,717,33,10,11])==[5,717,33]
    assert get_longest_all_palindromes([7,41,37,51,9,8,7,3])==[9,8,7,3]
    assert get_longest_all_palindromes([15,78,22])==[22]


def main():
    print("2.Toate numerele sunt prime")
    print("12.Toate numerele același număr de divizori")
    print("5.Toate numerele sunt palindroame")
    print("0.iesire")
    while True:
        optiune=int(input("dati optiune:"))
        if optiune==2:
            l=citire_lista()
            test_is_prime()
            test_is_toate_nrprime()
            #test_get_longest_all_primes()
            print(get_longest_all_primes(l))
        elif optiune==12:
            l=citire_lista()
            test_nrdivizori()
            test_toate_nrdivizori()
            test_get_longest_same_div_count()
            print(get_longest_same_div_count(l))
        elif optiune==5:
            l=citire_lista()
            test_is_palindrome()
            test_is_toate_palindrome()
            test_get_longest_all_palindromes()
            print(get_longest_all_palindromes(l))
        elif optiune==0:
            break
        else:
            print("optiune gresita")

main()


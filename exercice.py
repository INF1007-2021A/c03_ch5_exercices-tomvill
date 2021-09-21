#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0 :
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    lst = []
    for i in prefixes:
        lst.append(i + suffixe)
    return lst


def prime_integer_summation() -> int:
    sum_prime_nb = 0
    i = 0
    nb_prime = 2
    while i < 100 :
        is_prime_nb = True

        for n in range(2, (int(nb_prime/2)+1)) :
            if nb_prime % n == 0 and is_prime_nb :
                is_prime_nb = False
        if is_prime_nb :
            sum_prime_nb += nb_prime
            i += 1
        nb_prime += 1
    return sum_prime_nb


def factorial(number: int) -> int:
    result = 1
    for i in range(1, number + 1) :
        result *= i  
    return result


def use_continue() -> None:
    for  i in range(1, 11):
        if i == 5 :
            continue
        print(i)
    


def verify_ages(groups: List[List[int]]) -> List[bool]:
    lst = []
    for grps in groups:
        flag = True

        if len(grps) > 10 or len(grps) <= 3 :
            flag = False
        else :
            for ages in grps :
                if ages == 25 :
                    flag = True
                    break
                else:
                    if ages < 18 :
                        flag = False
                    if ages > 70 :
                        for i in grps :
                            if i == 50 :
                                flag = False
                
        lst.append(flag)
    return lst


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()

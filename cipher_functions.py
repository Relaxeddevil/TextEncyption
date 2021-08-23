"""CSC108 Assignment 2 functions"""

from typing import List

# Used to determine whether to encrypt or decrypt
ENCRYPT = 'e'
DECRYPT = 'd'


def clean_message(message: str) -> str:
    """Return a string with only uppercase letters from message with non-
    alphabetic characters removed.
    
    >>> clean_message('Hello world!')
    'HELLOWORLD'
    >>> clean_message("Python? It's my favourite language.")
    'PYTHONITSMYFAVOURITELANGUAGE'
    >>> clean_message('88test')
    'TEST'
    """
    message = message.upper()
    new_message = ''

    for char in message:

        if char.isalpha():
            new_message += char
            message = new_message

        else:
            message = new_message

    return message


def encrypt_letter(letter: str, keystream: int) -> str:
    """Return a str which is an encrypted version of letter.
    letter is shifted forward in alphabet by keystream

    >>> encrypt_letter('A', 7)
    'H'
    >>> encrypt_letter('A', 8)
    'I'
    """
    ord_diff = ord(letter) - ord('A')

    new_char_ord = (ord_diff + keystream) % 26

    return chr(new_char_ord + ord('A'))


def decrypt_letter(letter: str, keystream: int) -> str:
    """Returns a str which is an decrypted version of
    letter. letter is shifted back in the alphabet
     by keystream

    >>> decrypt_letter('H', 7)
    'A'
    >>> decrypt_letter('I', 8)
    'A'
    """
    ord_diff = ord(letter) - ord('A')

    new_char_ord = (ord_diff - keystream) % 26

    return chr(new_char_ord + ord('A'))


def is_valid_deck(deck: List[int]) -> bool:
    """Returns a bool of whether or not deck is
    a valid deck . ie consecutive numbers,
    greater than 3 items, and all items in list are of type int

    >>> is_valid_deck([1,2,3])
    True
    >>> is_valid_deck([1,2])
    False
    """
    check_deck = []
    check_deck.extend(deck)
    check_deck.sort()
    return len(check_deck) >= 3 and \
           all(isinstance(item, int) for item in check_deck) \
           and len(check_deck) == check_deck[-1]


def swap_cards(deck: List[int], index: int) -> None:
    """Does not return anything, mutates deck so that the
    card at index is swapped with the card that follows it

    >>> deck = [1,2,3,4]
    >>> swap_cards(deck, 0)
    >>> deck
    [2, 1, 3, 4]
    >>> deck = [1,2,3,4]
    >>> swap_cards(deck, 1)
    >>> deck
    [1, 3, 2, 4]
    """
    if index == len(deck) - 1:
        swap = deck[index]
        deck[index] = deck[0]
        deck[0] = swap

    else:
        swap = deck[index]
        deck[index] = deck[index + 1]
        deck[index + 1] = swap


def get_small_joker_value(deck: List[int]) -> int:
    """Returns the value of the second largest
    card in deck as an int

    >>> get_small_joker_value([1,2,3,4,5])
    4
    >>> get_small_joker_value([10,12,14,20])
    14
    """

    big_joker = deck[0]
    small_joker = None
    for number in deck[1:]:
        if number > big_joker:
            small_joker = big_joker
            big_joker = number
        elif small_joker is None or small_joker \
                < number:
            small_joker = number

    return small_joker


def get_big_joker_value(deck: List[int]) -> int:
    """Returns the value of the largest card in deck
    as an int

    >>> get_big_joker_value([1,2,3,4,5])
    5
    >>> get_big_joker_value([1,2,3,4])
    4
    """
    return max(deck)


def move_small_joker(deck: List[int]) -> None:
    """Swaps the small joker card with the card that
     follows it in deck. Does not return anything only mutates

    >>> deck = [1,2,3,4,5,6]
    >>> move_small_joker(deck)
    >>> deck
    [1, 2, 3, 4, 6, 5]
    >>> deck = [5,2,3,4,1,6]
    >>> move_small_joker(deck)
    >>> deck
    [2, 5, 3, 4, 1, 6]
    """
    big_joker = deck[0]
    small_joker = None

    for number in deck[1:]:
        if number > big_joker:
            small_joker = big_joker
            big_joker = number
        elif small_joker is None or small_joker \
                < number:
            small_joker = number

    index = deck.index(small_joker)

    if index == len(deck) - 1:
        swap = deck[index]
        deck[index] = deck[0]
        deck[0] = swap

    else:
        swap = deck[index]
        deck[index] = deck[index + 1]
        deck[index + 1] = swap


def move_big_joker(deck: List[int]) -> None:
    """Moves the big joker two spots forward in
    the given deck, does not return, only mutates

    >>> deck = [1,6,3,4,5,2]
    >>> move_big_joker(deck)
    >>> deck
    [1, 3, 4, 6, 5, 2]

    >>> deck = [1,6,8,9,3,4,5,2]
    >>> move_big_joker(deck)
    >>> deck
    [1, 6, 8, 3, 4, 9, 5, 2]
    """

    index = deck.index(max(deck))
    swap_cards(deck, index)
    index = deck.index(max(deck))
    swap_cards(deck, index)


def triple_cut(deck: List[int]) -> None:
    """Performs a triple cut (divide deck into 3
    and swap left and right parts) on the given deck
    splitting it at the index of the first joker and
    index right after the second joker

    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25,  3,  6,\
     28,  9, 12, 15, 18, 21, 24,  2, 27, 5,  8, 11,\
 14, 17, 20, 23, 26]
    >>> triple_cut(deck)
    >>> deck
    [5, 8, 11, 14, 17, 20, 23, 26, 28, 9, 12, 15, 18, 21,\
 24, 2, 27, 1, 4, 7,\
 10, 13, 16, 19, 22, 25, 3, 6]
    >>> deck = [2, 19, 7, 10, 13, 16, 4, 22, 25,  3,  6,\
 28,  9, 12, 15, 18, \
    21, 26,  1, 27,  5,  8, 11, 14, 17, 20, 23,24]
    >>> triple_cut(deck)
    >>> deck
    [5, 8, 11, 14, 17, 20, 23, 24, 28, 9, 12, 15, 18, 21,\
 26, 1, 27, 2, 19, 7,\
 10, 13, 16, 4, 22, 25, 3, 6]
    """

    small_joker_index = deck.index(get_small_joker_value(deck))
    big_joker_index = deck.index(max(deck))

    if big_joker_index > small_joker_index:
        left_joker = small_joker_index
        right_joker = big_joker_index

    else:
        right_joker = small_joker_index
        left_joker = big_joker_index

    left_list = deck[:left_joker]
    right_list = deck[right_joker + 1:]
    middle_list = deck[left_joker:right_joker + 1]
    del deck[:]
    deck.extend(right_list)
    deck.extend(middle_list)
    deck.extend(left_list)


def insert_top_to_bottom(deck: List[int]) -> None:
    """Find the bottom card and take its value. Take
    the first x cards from the top of the deck,
    x being the value of the bottom card. Put
    them directly on top of the bottom card:

    >>> deck = [5, 8, 11, 14, 17, 20, 23, 26, 28, 9, 12,\
     15, 18, 21, 24,\
     2, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7,\
 10, 13, 16, 19,\
 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> deck = [5, 8, 11, 14, 17, 20, 23, 24, 28, 9, 12,\
     15, 18, 21, 26,\
     1, 27, 2, 19, 7, 10, 13, 16, 4, 22, 25, 3, 6]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [23, 24, 28, 9, 12, 15, 18, 21, 26, 1, 27, 2, 19,\
 7, 10, 13, 16, 4,\
 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    """
    last = deck[-1]

    if last == max(deck):
        last = last - 1
        first_part = deck[:last]
        second_part = deck[last: -1]
        del deck[:]
        deck.extend(second_part)
        deck.extend(first_part)
        deck.append(last + 1)

    else:
        first_part = deck[:last]
        second_part = deck[last: - 1]
        del deck[:]
        deck.extend(second_part)
        deck.extend(first_part)
        deck.append(last)


def get_card_at_top_index(deck: List[int]) -> int:
    """Using card value at top of the deck, return
    the value of the card at that specific index.
    If card at top of deck is big joker (largest
    card in deck) use value of small joker
    instead(second largest card)

    >>> deck = [23, 26, 28, 9, 12, 15, 18, 21, 24,\
     2, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 5,\
      8, 11, 14, 17, 20, 6]
    >>> get_card_at_top_index(deck)
    11
    >>> deck = [5, 8, 11, 14, 17, 20, 23, 24, 28, 9,\
     12, 15, 18, 21, 26, 1, 27, 2, 19, 7, 10, 13, 16,\
      4, 22, 25, 3, 6]
    >>> get_card_at_top_index(deck)
    20
    """
    top_card = deck[0]

    if top_card == max(deck):
        top_card = get_small_joker_value(deck)
        keystream = deck[top_card]
    else:
        keystream = deck[top_card]

    return keystream


def get_next_keystream_value(deck: List[int]) -> int:
    """Repeats all steps of algorithm on a given deck
    until valid keystream in produced (one which
    is not either of the jokers) and return the keystream

    >>> deck = [5, 8, 11, 14, 17, 20, 23, 24, 28, 9, 12,\
     15, 18, 21, 26, 1, 27, 2, 19, 7, 10, 13, 16, 4, 22,\
      25, 3, 6]
    >>> get_next_keystream_value(deck)
    13
    >>> deck = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27,\
     1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17,\
      20, 6]
    >>> get_next_keystream_value(deck)
    9
    """
    move_small_joker(deck)
    move_big_joker(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    keystream = get_card_at_top_index(deck)

    special_cases = False

    if keystream == get_small_joker_value(deck) or keystream \
            == get_big_joker_value(deck):
        special_cases = True

    while special_cases:
        move_small_joker(deck)
        move_big_joker(deck)
        triple_cut(deck)
        insert_top_to_bottom(deck)
        keystream = get_card_at_top_index(deck)

        if keystream == get_small_joker_value(deck) or keystream \
                == get_big_joker_value(deck):
            special_cases = True

        else:
            special_cases = False

    return keystream


def process_messages(deck: List[int], message: List[str], eord: str) \
        -> List[str]:
    """Given a deck and a message in form of lists returns a list
    of the message encrypted or decrypted depending on
    third parameter.

    >>> deck = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7,\
     10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> message = ['He,', '', 'LLo']
    >>> process_messages(deck, message, 'e')
    ['Q', 'B', 'S', 'V', 'N']
    >>> deck = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7,\
     10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> message = ['Q', 'B', 'S', 'V', 'N']
    >>> process_messages(deck, message, 'd')
    ['H', 'E', 'L', 'L', 'O']
    """

    message_str = ''.join(message)

    del message[:]

    message.extend(list(clean_message(message_str)))
    keystream_numbers = []
    solved_list = []
    a = 0

    for _ in message:
        keystream_numbers.append(get_next_keystream_value(deck))

    if eord == 'e':

        for letter in message:
            solved_list.append(encrypt_letter(letter, keystream_numbers[a]))
            a += 1

    if eord == 'd':

        for letter in message:
            solved_list.append(decrypt_letter(letter, keystream_numbers[a]))
            a += 1

    return solved_list


# This if statement should always be the last thing in the file, below all of
# your functions:

if __name__ == '__main__':
    """Did you know that you can get Python to automatically run and check
    your docstring examples? These examples are called "doctests".

    To make this happen, just run this file! The two lines below do all
    the work.

    For each doctest, Python does the function call and then compares the
    output to your expected result.
    
    NOTE: your docstrings MUST be properly formatted for this to work!
    In particular, you need a space after each >>>. Otherwise Python won't
    be able to detect the example.
    """

    import doctest

    doctest.testmod()

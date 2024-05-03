def blackjack_hand_total(cards: list[int]) -> int:
    total = sum(cards)
    
    if total > 21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
            return sum(cards)
    else:
        return total

list = [8, 3, 10]
blackjack_hand_total(list)

###############################

def construct_rectangle(area: float) -> list[float]:
    min_diff = area -1
    result = [area, 1]
    
    for i in range(2, int(area**0.5) + 1):
        if area % i == 0:
            j = area // i
            if j >= i and j - i < min_diff:
                min_diff = j - i
                result = [j, i]
    return result

###############################

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    word = ""
    word_freq = {}
    for char in text:
        if char in [" ", ".", ",", ":", ";", "?", "!"]:
            if word not in stopwords and word !="":
                if word not in word_freq.keys():
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
            word = ""
        else:
            word += char.lower()
    return word_freq

###############################

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    x = len(nums)
    num_set = set(nums)
    missing = []
    
    for i in range (1, x + 1):
        if i not in num_set:
            missing.append(i)
            
    return missing
    
find_disappeared_numbers([4,3,2,7,8,2,3,1])

###############################

def is_subsequence(s: str, t: str) -> bool:
    first_sus = list(s)
    second_sus = list(t)
    
    j = 0
    i = 0
    
    while i < len(first_sus) and j < len(second_sus):
        if first_sus[i] == second_sus[j]:
            i += 1
        j += 1
   
    return i == len(first_sus)
    
is_subsequence("abc", "ahbgdc")

###############################

def even_odd_pattern(nums: list[int]) -> list[int]:
    even = [x for x in nums if x % 2 == 0]
    odd = [x for x in nums if x % 2 != 0]
    result = even + odd
    return result

###############################

def prime_factors(n: int) -> list[int]:
    factors = []
    x = 2
    while n>1:
        while n % x == 0:
            factors.append(x)
            n //= 2
        x += 1
    return factors
    
prime_factors(10)

###############################

def third_max(nums: list[int]) -> int:
    first_max = second_max = third_max = float('-inf')
    
    for num in nums:
        if num > first_max:
            third_max = second_max
            second_max = first_max
            first_max = num
        elif second_max < num < first_max:
            third_max = second_max
            second_max = num
        elif third_max < num < second_max:
            third_max = num
        
    if third_max != float('-inf'):
        return third_max
    else:
        return first_max
        
jewels = [3, 2, 1]
third_max(jewels)
def remove_even_numbers(lst):
    lst = [x for x in lst if x % 2 != 0]
    return lst
def main():  
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    numbers = remove_even_numbers(numbers)
    print("Remaining numbers after removing even numbers:")
    for number in numbers:
        print(number)
if __name__ == "__main__":
    main()

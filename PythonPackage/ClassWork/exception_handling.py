lst = [1, 2, 3]
try:
    d = 4 + "I "
    s = lst[9]
    print("I did well")
except IndexError as e:
    print(f"Error occurred: {e}")
except (TypeError, ValueError) as e:
    print(f"Error of no type: {e}")
finally:
    print("I am from Finally")

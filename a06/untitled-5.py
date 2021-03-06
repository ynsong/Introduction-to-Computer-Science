def ternary_search (L, key):
        left = 0
        right = len(L) - 1
        while left <= right:
                ind1 = left
                ind2 = left + (right - left) // 3
                ind3 = left + 2 * (right - left) // 3
                n = 0
                if key == L[left]:
                        n += 1
                        print("Checking if " + str(key) + " is equal to " + str(left))
                        print("Search successful")
                        print(str(key) + " is located at index " + str(left))
                        print("A total of " + str(n) + " comparisons were made")
                        return
                elif key == L[right]:
                        n += 1
                        print("Checking if " + str(key) + " is equal to " + str(right))
                        print("Search successful")
                        print(str(key) + " is located at index " + str(right))
                        print("A total of " + str(n) + " comparisons were made")
                        return
                elif key < L[left] or key > L[right]:
                        n += 1
                        print("Search not successful")
                        print("A total of " + str(n) + " comparisons were made")
                        return
                elif key <= L[ind2]:
                        n += 1
                        print("Checking if " + str(key) + " is less than " + str(L[ind2]))
                        right = ind2 -1
                elif key > L[ind2] and key <= L[ind3]:
                        n += 1
                        print("Checking if " + str(key) + " is less than " + str(L[ind2]))
                        print("Checking if " + str(key) + " is equal to " + str(L[ind3]))
                        print("Checking if " + str(key) + " is less than " + str(L[ind3]))         
                        left = ind2 + 1
                        right = ind3
                else:
                        n += 1 
                        print("Checking if " + str(key) + " is less than " + str(L[ind3]))         
                        left = ind3 + 1
        return
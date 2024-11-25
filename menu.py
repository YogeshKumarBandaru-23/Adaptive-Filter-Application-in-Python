import filter1
import filter2
import filter3
import filter4
import cartoonify_with_filter
import catoonify

print("1. Filter 1")
print("2. Filter 2")
print("3. Filter 3")
print("4. Filter 4")
print("5. Cartoonify")
print("6. Cartoonify with applied filters")
while True:
    choice = int(input("Enter the choice of filter to be tried"))
    if choice == 1:
        filter1.filter1()
    elif choice == 2:
        filter2.filter()
    elif choice == 3:
        filter3.filter()
    elif choice == 4:
        filter4.filter()
    elif choice == 5:
        catoonify.cartoonify_video()
    elif choice == 6:
        cartoonify_with_filter.cartoonify_video()
    else:
        break
    print("1. Filter 1")
    print("2. Filter 2")
    print("3. Filter 3")
    print("4. Filter 4")
    print("5. Cartoonify")
    print("6. Cartoonify with applied filters")

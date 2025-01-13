print("Activity(1)\nAds and data(2)\nApp Settings(3)\nDM's(4)\nIncome + Wallet Transactions(5)\nPosts(6)\nProfile(7)\nTikTok Live(8)\nTikTok Shopping(9)\n")
view = input('What would you like to see? ("q" to quit) >>> ')
while True:
    #Option 1
    if view == '1': 
        activity_option = int(input("Browsing History(1)\nComments(2)\nFavorite effects, hashtags, sounds, videos(3)\nFollowers(4)\nFollowing(5)\nOther(6)\n>>>"))
        if activity_option == 1:
            print('browsing history')
        elif activity_option == 2: 
            print("comments")
        elif activity_option == 3:
            print('favorites')
        elif activity_option == 4:
            print('followers')
        elif activity_option == 5:
            print("following")
        elif activity_option == 6: 
            print('other')
        else: 
            print("Please choose one of the options (1-6)")


    #Option 2
    elif view == '2':
        print('show all')
    
    #Option 3
    elif view == '3':
        settings = int(input('Blocked accounts(1)\nSettings(2)\n>>>'))
        if settings == 1:
            print("Blocked accounts")
        elif settings == 2: 
            print("Settings")
        else: 
            print("Please choose one of the 2 options")
    
    #Option 4
    elif view == '4':
        print("show all")

    #Option 5
    elif view == '5':
        print('show all')

    #Option 6
    elif view == '6':
        posts = int(input('Posts(1)\nRecently deleted posts(2)\n>>>'))
        if posts == 1:
            print("posts")
        elif posts == 2: 
            print("Recently deleted")
        else: 
            print("Please choose one of the 2 options")

    #Option 7
    elif view == '7':
        profile = int(input('Profile info(1)\nOther(2)\n>>>'))
        if profile == 1: 
            print("Profile info")
        elif profile == 2: 
            print("Other")
        else: 
            print("Please choosse one of the 2 options")

    #Option 8
    elif view == '8':
        live = int(input('Live history *comments, watched lives, etc*(1)\nOther(2)\n>>>'))
        if live == 1: 
            print("live history")
        elif live == 2: 
            print("Other")
        else: 
            print("Please choose 1 of the 2 options")

    elif view == '9':
        shop = int(input('Orders(1)\nBrowsing History(2)\nShopping Cart(3)\nReviews(4)\nOther(5)\n>>>'))
        if shop == 1: 
            print('orders')
        elif shop == 2: 
            print("browsing history")
        elif shop == 3: 
            print("cart")
        elif shop == 4: 
            print("reviews")
        elif shop == 5: 
            print('other')
        else: 
            print("Please choose one of the options (1-5)")
    
    #Quit
    elif view =="q":
        break

    else: 
        print('Please pick a number 1-9')
    view = input('\n\n\n\nWhat would you like to see? ("q to quit") >>> ')
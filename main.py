print("Activity(1)\nAds and data(2)\nApp Settings(3)\nDM's(4)\nIncome + Wallet Transactions(5)\nPosts(6)\nProfile(7)\nTikTok Live(8)\nTikTok Shopping(9)\n")
view = input('What would you like to see? ("q" to quit) >>> ')
while True:
    #Option 1
    if view == '1': 
        activity_option = print("Browsing History(1)\nComments(2)\nFavorite effects, hashtags, sounds, videos(3)\nFollowers(4)\nFollowing(5)\nOther(6)")


    #Option 2
    elif view == '2':
        print('show all')
    
    #Option 3
    elif view == '3':
        print('Blocked accounts(1)\nSettings(2)')
    
    #Option 4
    elif view == '4':
        print("show all")

    #Option 5
    elif view == '5':
        print('show all')

    #Option 6
    elif view == '6':
        print('Posts(1)\nRecently deleted posts(2)')

    #Option 7
    elif view == '7':
        print('Profile info(1)\nOther(2)')

    #Option 8
    elif view == '8':
        print('Live history *comments, watched lives, etc*(1)\nOther(2)')

    elif view == '9':
        print('Orders(1)\nBrowsing History(2)\nShopping Cart(3)\nReviews(4)\nOther(5)')
    
    #Quit
    elif view =="q":
        break

    else: 
        print('Please pick a number 1-9')
    view = input('What would you like to see? ("q to quit") >>> ')
view = input('What would you like to see? ("list" for list of options) >>> ')
while True:
    if view == "list":
        print("Activity(1)\nAds and data(2)\nApp Settings(3)\nDM's(4)\nIncome + Wallet Transactions(5)\nPosts(6)\nProfile(7)\nTikTok Live(8)\nTikTok Shopping(9)\n")
        

    elif view == '1': 
        print("Browsing History(1)\nComments(2)\nFavorite effects, hashtags, sounds, videos(3)\nFollowers(4)\nFollowing(5)\nOther(6)")

    elif view =="q":
        break

    else: 
        print("new test")
    view = input('What would you like to see? ("list" for list of options) >>> ')
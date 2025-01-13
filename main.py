file1_path = "TikTok_Data_1735588272\Tiktok\Activity\Favorite Effects.txt"
file2_path = "TikTok_Data_1735588272\Tiktok\Activity\Favorite HashTags.txt"
file3_path = "TikTok_Data_1735588272\Tiktok\Activity\Favorite Sounds.txt"
file4_path = "TikTok_Data_1735588272\Tiktok\Activity\Favorite Videos.txt"
file5_path = "TikTok_Data_1735588272\Tiktok\Activity\Hashtag.txt"
file6_path = "TikTok_Data_1735588272\Tiktok\Activity\Like List.txt"
file7_path = "TikTok_Data_1735588272\Tiktok\Activity\Location Reviews.txt"
file8_path = "TikTok_Data_1735588272\Tiktok\Activity\Login History.txt"
file9_path = "TikTok_Data_1735588272\Tiktok\Activity\Purchases.txt"
file10_path = "TikTok_Data_1735588272\Tiktok\Activity\Searches.txt"
file11_path = "TikTok_Data_1735588272\Tiktok\Activity\Status.txt"










print("Activity(1)\nAds and data(2)\nApp Settings(3)\nDM's(4)\nIncome + Wallet Transactions(5)\nPosts(6)\nProfile(7)\nTikTok Live(8)\nTikTok Shopping(9)\n")
view = input('What would you like to see? ("q" to quit) >>> ')
while True:
    # Option 1: Activity
    if view == '1':
        activity_option = int(input("Browsing History(1)\nComments(2)\nFavorite effects, hashtags, sounds, videos(3)\nFollowers(4)\nFollowing(5)\nShare History(6)\nOther(7)\n>>>"))
        if activity_option == 1:
            with open("TikTok_Data_1735588272\Tiktok\Activity\Browsing History.txt", "r", encoding='utf-8') as file:
                content = file.read()
                print("\n\nBrowsing History: " + content)

        elif activity_option == 2:
            with open("TikTok_Data_1735588272\Tiktok\Activity\Comments.txt", "r", encoding='utf-8') as file:
                content = file.read()
                print("\n\nComments: " + content)

        elif activity_option == 3:
            with open(file1_path, "r", encoding='utf-8') as file1:
                content1 = file1.read()
                print("\n\nEffects: " + content1)

            with open(file2_path, "r", encoding='utf-8') as file2:
                content2 = file2.read()
                print("\n\nHashtags: " + content2)

            with open(file3_path, "r", encoding='utf-8') as file3:
                content3 = file3.read()
                print("\n\nSounds: " + content3)

            with open(file4_path, "r", encoding='utf-8') as file4:
                content4 = file4.read()
                print("\n\nVideos: " + content4)

        elif activity_option == 4:
            with open("TikTok_Data_1735588272\Tiktok\Activity\Follower.txt", "r", encoding='utf-8') as file:
                content = file.read()
                print("\n\nFollowers: " + content)

        elif activity_option == 5:
            with open("TikTok_Data_1735588272\Tiktok\Activity\Following.txt", "r", encoding='utf-8') as file:
                content = file.read()
                print("\n\nFollowing: " + content)

        elif activity_option == 6:
            with open("TikTok_Data_1735588272\Tiktok\Activity\Share History.txt", "r", encoding='utf-8') as file:
                content = file.read()
                print("\n\nShare History: " + content)

        elif activity_option == 7:
            with open(file5_path, "r", encoding='utf-8') as file5:
                content5 = file5.read()
                print("\n\nHashtags: " + content5)

            with open(file6_path, "r", encoding='utf-8') as file6:
                content6 = file6.read()
                print("\n\nLike list: " + content6)

            with open(file7_path, "r", encoding='utf-8') as file7:
                content7 = file7.read()
                print("\n\nLocation Reviews?: " + content7)

            with open(file8_path, "r", encoding='utf-8') as file8:
                content8 = file8.read()
                print("\n\nLogin History: " + content8)

            with open(file9_path, "r", encoding='utf-8') as file9:
                content9 = file9.read()
                print("\n\nPurchases: " + content9)

            with open(file10_path, "r", encoding='utf-8') as file10:
                content10 = file10.read()
                print("\n\nSearches: " + content10)

            with open(file11_path, "r", encoding='utf-8') as file11:
                content11 = file11.read()
                print("\n\nStatus: " + content11)
        else:
            print("Please choose one of the options (1-6)")

    #Option 2
    elif view == '2':
        with open("", "r") as file:
            content = file.read()
            print(content)
    
    #Option 3
    elif view == '3':
        settings = int(input('Blocked accounts(1)\nSettings(2)\n>>>'))
        if settings == 1:
            with open("", "r") as file:
                content = file.read()
                print(content)
        elif settings == 2: 
           with open("", "r") as file:
                content = file.read()
                print(content)
        else: 
            print("Please choose one of the 2 options")
    
    #Option 4
    elif view == '4':
        with open("", "r") as file:
                content = file.read()
                print(content)

    #Option 5
    elif view == '5':
        with open("", "r") as file:
                content = file.read()
                print(content)

    #Option 6
    elif view == '6':
        posts = int(input('Posts(1)\nRecently deleted posts(2)\n>>>'))
        if posts == 1:
            with open("", "r") as file:
                content = file.read()
                print(content)
        elif posts == 2: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        else: 
            print("Please choose one of the 2 options")

    #Option 7
    elif view == '7':
        profile = int(input('Profile info(1)\nOther(2)\n>>>'))
        if profile == 1: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        elif profile == 2: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        else: 
            print("Please choosse one of the 2 options")

    #Option 8
    elif view == '8':
        live = int(input('Live history *comments, watched lives, etc*(1)\nOther(2)\n>>>'))
        if live == 1: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        elif live == 2: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        else: 
            print("Please choose 1 of the 2 options")

    elif view == '9':
        shop = int(input('Orders(1)\nBrowsing History(2)\nShopping Cart(3)\nReviews(4)\nOther(5)\n>>>'))
        if shop == 1: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        elif shop == 2: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        elif shop == 3: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        elif shop == 4: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        elif shop == 5: 
            with open("", "r") as file:
                content = file.read()
                print(content)
        else: 
            print("Please choose one of the options (1-5)")
    
    #Quit
    elif view =="q":
        break

    else: 
        print('Please pick a number 1-9')
    view = input('\n\n\n\nWhat would you like to see? ("q to quit") >>> ')

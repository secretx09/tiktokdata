browsing_history = "TikTok_Data_1735588272\Tiktok\Activity\Browsing History.txt"
comments = "TikTok_Data_1735588272\Tiktok\Activity\Comments.txt"
followers = "TikTok_Data_1735588272\Tiktok\Activity\Follower.txt"
following = "TikTok_Data_1735588272\Tiktok\Activity\Following.txt"
share_history = "TikTok_Data_1735588272\Tiktok\Activity\Share History.txt"
fav_effect = "TikTok_Data_1735588272\Tiktok\Activity\Favorite Effects.txt"
fav_hash = "TikTok_Data_1735588272\Tiktok\Activity\Favorite HashTags.txt"
fav_sound = "TikTok_Data_1735588272\Tiktok\Activity\Favorite Sounds.txt"
fav_video = "TikTok_Data_1735588272\Tiktok\Activity\Favorite Videos.txt"
hashtags = "TikTok_Data_1735588272\Tiktok\Activity\Hashtag.txt"
like_list = "TikTok_Data_1735588272\Tiktok\Activity\Like List.txt"
loc_review = "TikTok_Data_1735588272\Tiktok\Activity\Location Reviews.txt"
login_history = "TikTok_Data_1735588272\Tiktok\Activity\Login History.txt"
purchases = "TikTok_Data_1735588272\Tiktok\Activity\Purchases.txt"
searches = "TikTok_Data_1735588272\Tiktok\Activity\Searches.txt"
status = "TikTok_Data_1735588272\Tiktok\Activity\Status.txt"
ad_interest = "TikTok_Data_1735588272\Tiktok\Ads and data\Ad Interests.txt"
ad_response = "TikTok_Data_1735588272\Tiktok\Ads and data\Instant Form Ads Responses.txt"
off_tiktok_activity = "TikTok_Data_1735588272\Tiktok\Ads and data\Off TikTok Activity.txt"










print("Activity(1)\nAds and data(2)\nApp Settings(3)\nDM's(4)\nIncome + Wallet Transactions(5)\nPosts(6)\nProfile(7)\nTikTok Live(8)\nTikTok Shopping(9)\n")
view = input('What would you like to see? ("q" to quit) >>> ')
while True:
    # Option 1: Activity
    if view == '1':
        activity_option = int(input("Browsing History(1)\nComments(2)\nFavorite effects, hashtags, sounds, videos(3)\nFollowers(4)\nFollowing(5)\nShare History(6)\nOther(7)\n>>>"))
        if activity_option == 1:
            with open(browsing_history, "r", encoding='utf-8') as history:
                browse_his = history.read()
                print("\n\nBrowsing History: " + browse_his)

        elif activity_option == 2:
            with open(comments, "r", encoding='utf-8') as comment:
                comment_his = comment.read()
                print("\n\nComments: " + comment_his)

        elif activity_option == 3:
            with open(fav_effect, "r", encoding='utf-8') as effect:
                fav_effects = effect.read()
                print("\n\nEffects: " + fav_effects)

            with open(fav_hash, "r", encoding='utf-8') as hash:
                fav_hashs = hash.read()
                print("\n\nHashtags: " + fav_hashs)

            with open(fav_sound, "r", encoding='utf-8') as sounds:
                fav_sounds = sounds.read()
                print("\n\nSounds: " + fav_sounds)

            with open(fav_video, "r", encoding='utf-8') as videos:
                fav_videos = videos.read()
                print("\n\nVideos: " + fav_videos)

        elif activity_option == 4:
            with open(followers, "r", encoding='utf-8') as follows:
                followed_by = file.read()
                print("\n\nFollowers: " + followed_by)

        elif activity_option == 5:
            with open(following, "r", encoding='utf-8') as follow:
                following_acc = follow.read()
                print("\n\nFollowing: " + following_acc)

        elif activity_option == 6:
            with open(share_history, "r", encoding='utf-8') as share:
                share_his = share.read()
                print("\n\nShare History: " + share_his)

        elif activity_option == 7:
            with open(hashtags, "r", encoding='utf-8') as hashs:
                hashtag = hashs.read()
                print("\n\nHashtags: " + hashtag)

            with open(like_list, "r", encoding='utf-8') as like_lists:
                l_l = like_lists.read()
                print("\n\nLike list: " + l_l)

            with open(loc_review, "r", encoding='utf-8') as location:
                loc_rev = location.read()
                print("\n\nLocation Reviews?: " + loc_rev)

            with open(login_history, "r", encoding='utf-8') as logins:
                log_his = logins.read()
                print("\n\nLogin History: " + log_his)

            with open(purchases, "r", encoding='utf-8') as purchase:
                purchased = purchase.read()
                print("\n\nPurchases: " + purchased)

            with open(searches, "r", encoding='utf-8') as search:
                searched = search.read()
                print("\n\nSearches: " + searched)

            with open(status, "r", encoding='utf-8') as stats:
                stattus = stats.read()
                print("\n\nStatus: " + stattus)
        else:
            print("Please choose one of the options (1-6)")

    #Option 2
    elif view == '2':
        with open(ad_interest, "r", encoding='utf-8') as file12:
            content12 = file12.read()
            print("\n\nAd Interests: " + content12)

        with open(ad_response, "r", encoding='utf-8') as file13:
            content13 = file13.read()
            print("\n\nAd form responses: " + content13)

        with open(off_tiktok_activity, "r", encoding='utf-8') as file14:
            content14 = file14.read()
            print("\n\nOff TikTok Activity: " + content14)
    
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

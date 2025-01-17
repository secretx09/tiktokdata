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
block_list = "TikTok_Data_1735588272\Tiktok\App Settings\Block List.txt"
accsettings = "TikTok_Data_1735588272\Tiktok\App Settings\Settings.txt"
direct_messages = "TikTok_Data_1735588272\Tiktok\Direct Messages\Direct Messages.txt"
transaction_history = "TikTok_Data_1735588272\Tiktok\Income+ Wallet Transactions\Transaction History.txt"
post = "TikTok_Data_1735588272\Tiktok\Posts\Post.txt"
rdp = "TikTok_Data_1735588272\Tiktok\Posts\Recently Deleted Posts.txt"
profile_info = "TikTok_Data_1735588272\Tiktok\Profile\Profile Info.txt"
ai_moji = "TikTok_Data_1735588272\Tiktok\Profile\AI-Moji.txt"
auto_info = "TikTok_Data_1735588272\Tiktok\Profile\Autofill.txt"
live_his = "TikTok_Data_1735588272\Tiktok\TikTok Live\Watch Live History.txt"
golive_his = "TikTok_Data_1735588272\Tiktok\TikTok Live\Go Live History.txt"
golive_sets = "TikTok_Data_1735588272\Tiktok\TikTok Live\Go Live settings.txt"
watchlive_sets = "TikTok_Data_1735588272\Tiktok\TikTok Live\Watch Live settings.txt"







print("Activity(1)\nAds and data(2)\nApp Settings(3)\nDM's(4)\nIncome + Wallet Transactions(5)\nPosts(6)\nProfile(7)\nTikTok Live(8)\nTikTok Shopping(9)\n")
view = input('What would you like to see? ("q" to quit) >>> ')
while True:
    # Option 1: Activity
    if view == '1':
        activity_option = int(input("Browsing History(1)\nComments(2)\nFavorite effects, hashtags, sounds, videos(3)\nFollowers(4)\nFollowing(5)\nShare History(6)\nOther(7)\n>>>"))
        if activity_option == 1:
            with open(browsing_history, "r", encoding='utf-8') as history:
                history = history.read()
                print("\n\nBrowsing History: " + history)

        elif activity_option == 2:
            with open(comments, "r", encoding='utf-8') as comment:
                comment = comment.read()
                print("\n\nComments: " + comment)

        elif activity_option == 3:
            with open(fav_effect, "r", encoding='utf-8') as effect:
                effects = effect.read()
                print("\n\nEffects: " + effect)

            with open(fav_hash, "r", encoding='utf-8') as hash:
                hash = hash.read()
                print("\n\nHashtags: " + hash)

            with open(fav_sound, "r", encoding='utf-8') as sounds:
                sounds = sounds.read()
                print("\n\nSounds: " + sounds)

            with open(fav_video, "r", encoding='utf-8') as videos:
                videos = videos.read()
                print("\n\nVideos: " + videos)

        elif activity_option == 4:
            with open(followers, "r", encoding='utf-8') as followed_by:
                followed_by = followed_by.read()
                print("\n\nFollowers: " + followed_by)

        elif activity_option == 5:
            with open(following, "r", encoding='utf-8') as following:
                following = following.read()
                print("\n\nFollowing: " + following)

        elif activity_option == 6:
            with open(share_history, "r", encoding='utf-8') as shared:
                shared = shared.read()
                print("\n\nShare History: " + shared)

        elif activity_option == 7:
            with open(hashtags, "r", encoding='utf-8') as hashs:
                hashs = hashs.read()
                print("\n\nHashtags: " + hashs)

            with open(like_list, "r", encoding='utf-8') as like_lists:
                like_lists = like_lists.read()
                print("\n\nLike list: " + like_lists)

            with open(loc_review, "r", encoding='utf-8') as location:
                location = location.read()
                print("\n\nLocation Reviews?: " + location)

            with open(login_history, "r", encoding='utf-8') as logins:
                logins = logins.read()
                print("\n\nLogin History: " + logins)

            with open(purchases, "r", encoding='utf-8') as purchased:
                purchased = purchased.read()
                print("\n\nPurchases: " + purchased)

            with open(searches, "r", encoding='utf-8') as search:
                search = search.read()
                print("\n\nSearches: " + search)

            with open(status, "r", encoding='utf-8') as stats:
                stats = stats.read()
                print("\n\nStatus: " + stats)
        else:
            print("Please choose one of the options (1-6)")

    #Option 2
    elif view == '2':
        with open(ad_interest, "r", encoding='utf-8') as interest:
            ad_int = interest.read()
            print("\n\nAd Interests: " + ad_int)

        with open(ad_response, "r", encoding='utf-8') as response:
            ad_res = response.read()
            print("\n\nAd form responses: " + ad_res)

        with open(off_tiktok_activity, "r", encoding='utf-8') as off_activity:
            off_tiktok = off_activity.read()
            print("\n\nOff TikTok Activity: " + off_tiktok)
    
    #Option 3
    elif view == '3':
        settings = int(input('Blocked accounts(1)\nSettings(2)\n>>>'))
        if settings == 1:
            with open(block_list, "r", encoding='utf-8') as blocked:
                blocked_list = blocked.read()
                print(blocked_list)
        elif settings == 2: 
           with open(accsettings, "r", encoding='utf-8') as account_settings:
                acc_sets = account_settings.read()
                print(acc_sets)
        else: 
            print("\n\nPlease choose one of the 2 options")
    
    #Option 4
    elif view == '4':
        with open(direct_messages, "r", encoding='utf-8') as dms:
                messages = dms.read()
                print("\n\n" +messages)

    #Option 5
    elif view == '5':
        with open(transaction_history, "r", encoding='utf-8') as transactions:
                trans_his = transactions.read()
                print("\n\n" + trans_his)

    #Option 6
    elif view == '6':
        posts = int(input('Posts(1)\nRecently deleted posts(2)\n>>>'))
        if posts == 1:
            with open(post, "r", encoding='utf-8') as posts:
                posts = posts.read()
                print("\n\n" + posts)
        elif posts == 2: 
            with open(rdp, "r", encoding='utf-8') as recently_deleted:
                recent_deleted = recently_deleted.read()
                print("\n\n" + recent_deleted)
        else: 
            print("Please choose one of the 2 options")

    #Option 7
    elif view == '7':
        profile = int(input('Profile info(1)\nOther(2)\n>>>'))
        if profile == 1: 
            with open(profile_info, "r", encoding='utf-8') as prof_info:
                print("\n\n" + prof_info.read())
        elif profile == 2: 
            with open(ai_moji, "r", encoding='utf-8') as ai_emoji:
                print("\n\n" + ai_emoji.read())

            with open(auto_info, "r", encoding='utf-8') as auto_fill:
                print("\n\n" + auto_fill.read())
        else: 
            print("Please choosse one of the 2 options")

    #Option 8
    elif view == '8':
        live = int(input('Live history *comments, watched lives, etc*(1)\nOther(2)\n>>>'))
        if live == 1: 
            with open(live_his, "r", encoding='utf-8') as live_history:
                print("\n\n" + live_history.read())
        elif live == 2: 
            with open(golive_his, "r", encoding='utf-8') as golive_history:
                print("\n\n" + golive_history.read())

            with open(golive_sets, "r", encoding='utf-8') as golive_settings:
                print("\n\n" + golive_settings.read())

            with open(watchlive_sets, "r", encoding='utf-8') as watchlive_settings:
                print("\n\n" + watchlive_settings.read())
        else: 
            print("Please choose 1 of the 2 options")

    elif view == '9':
        shop = int(input('Orders(1)\nBrowsing History(2)\nShopping Cart(3)\nReviews(4)\nOther(5)\n>>>'))
        if shop == 1: 
            with open("", "r", encoding='utf-8') as file:
                content = file.read()
                print(content)
        elif shop == 2: 
            with open("", "r", encoding='utf-8') as file:
                content = file.read()
                print(content)
        elif shop == 3: 
            with open("", "r", encoding='utf-8') as file:
                content = file.read()
                print(content)
        elif shop == 4: 
            with open("", "r", encoding='utf-8') as file:
                content = file.read()
                print(content)
        elif shop == 5: 
            with open("", "r", encoding='utf-8') as file:
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

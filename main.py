import os
import tkinter as tk
from tkinter import ttk

def find_txt_file(filename):
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == filename:
                return os.path.relpath(os.path.join(root, file))
    return None

browsing_history = True
while browsing_history == True:
    filename_to_search = "Browsing History.txt"
    browsing_history = find_txt_file(filename_to_search)

comments = True
while comments == True:
    filename_to_search = "Comments.txt"
    comments = find_txt_file(filename_to_search)

followers = True
while followers == True:
    filename_to_search = "Follower.txt"
    followers = find_txt_file(filename_to_search)

following = True
while following == True:
    filename_to_search = "Following.txt"
    following = find_txt_file(filename_to_search)

share_history = True
while share_history == True:
    filename_to_search = "Share History.txt"
    share_history = find_txt_file(filename_to_search)

fav_effect = True
while fav_effect == True:
    filename_to_search = "Favorite Effects.txt"
    fav_effect = find_txt_file(filename_to_search)

fav_hash = True
while fav_hash == True:
    filename_to_search = "Favorite HashTags.txt"
    fav_hash = find_txt_file(filename_to_search)

fav_sound = True
while fav_sound == True:
    filename_to_search = "Favorite Sounds.txt"
    fav_sound = find_txt_file(filename_to_search)

fav_video = True
while fav_video == True:
    filename_to_search = "Favorite Videos.txt"
    fav_video = find_txt_file(filename_to_search)

hashtags = True
while hashtags == True:
    filename_to_search = "Hashtag.txt"
    hashtags = find_txt_file(filename_to_search)

like_list = True
while like_list == True:
    filename_to_search = "Like List.txt"
    like_list = find_txt_file(filename_to_search)

loc_review = True
while loc_review == True:
    filename_to_search = "Location Reviews.txt"
    loc_review = find_txt_file(filename_to_search)

login_history = True
while login_history == True:
    filename_to_search = "Login History.txt"
    login_history = find_txt_file(filename_to_search)

purchases = True
while purchases == True:
    filename_to_search = "Purchases.txt"
    purchases = find_txt_file(filename_to_search)

searches = True
while searches == True:
    filename_to_search = "Searches.txt"
    searches = find_txt_file(filename_to_search)

status = True
while status == True:
    filename_to_search = "Status.txt"
    status = find_txt_file(filename_to_search)

ad_interest = True
while ad_interest == True:
    filename_to_search = "Ad Interests.txt"
    ad_interest = find_txt_file(filename_to_search)

ad_response = True
while ad_response == True:
    filename_to_search = "Instant Form Ads Responses.txt"
    ad_response = find_txt_file(filename_to_search)

off_tiktok_activity = True
while off_tiktok_activity == True:
    filename_to_search = "Off TikTok Activity.txt"
    off_tiktok_activity = find_txt_file(filename_to_search)

block_list = True
while block_list == True:
    filename_to_search = "Block List.txt"
    block_list = find_txt_file(filename_to_search)

accsettings = True
while accsettings == True:
    filename_to_search = "Settings.txt"
    accsettings = find_txt_file(filename_to_search)

direct_messages = True
while direct_messages == True:
    filename_to_search = "Direct Messages.txt"
    direct_messages = find_txt_file(filename_to_search)

transaction_history = True
while transaction_history == True:
    filename_to_search = "Transaction History.txt"
    transaction_history = find_txt_file(filename_to_search)

post = True
while post == True:
    filename_to_search = "Post.txt"
    post = find_txt_file(filename_to_search)

rdp = True
while rdp == True:
    filename_to_search = "Recently Deleted Posts.txt"
    rdp = find_txt_file(filename_to_search)

profile_info = True
while profile_info == True:
    filename_to_search = "Profile Info.txt"
    profile_info = find_txt_file(filename_to_search)

ai_moji = True
while ai_moji == True:
    filename_to_search = "AI-Moji.txt"
    ai_moji = find_txt_file(filename_to_search)

auto_info = True
while auto_info == True:
    filename_to_search = "Autofill.txt"
    auto_info = find_txt_file(filename_to_search)

live_his = True
while live_his == True:
    filename_to_search = "Watch Live History.txt"
    live_his = find_txt_file(filename_to_search)

golive_his = True
while golive_his == True:
    filename_to_search = "Go Live History.txt"
    golive_his = find_txt_file(filename_to_search)

golive_sets = True
while golive_sets == True:
    filename_to_search = "Go Live settings.txt"
    golive_sets = find_txt_file(filename_to_search)

watchlive_sets = True
while watchlive_sets == True:
    filename_to_search = "Watch Live settings.txt"
    watchlive_sets = find_txt_file(filename_to_search)

orders = True
while orders == True:
    filename_to_search = "Order History.txt"
    orders = find_txt_file(filename_to_search)

product_lookup_history = True
while product_lookup_history == True:
    filename_to_search = "Product Browsing History.txt"
    product_lookup_history = find_txt_file(filename_to_search)

cart = True
while cart == True:
    filename_to_search = "Shopping Cart List.txt"
    cart = find_txt_file(filename_to_search)

reviews = True
while reviews == True:
    filename_to_search = "Product Reviews.txt"
    reviews = find_txt_file(filename_to_search)

communication = True
while communication == True:
    filename_to_search = "Communication with shops.txt"
    communication = find_txt_file(filename_to_search)

payment_info = True
while payment_info == True:
    filename_to_search = "Current Payment Information.txt"
    payment_info = find_txt_file(filename_to_search)

customer_support = True
while customer_support == True:
    filename_to_search = "Customer support history.txt"
    customer_support = find_txt_file(filename_to_search)

disputes = True
while disputes == True:
    filename_to_search = "Order dispute history.txt"
    disputes = find_txt_file(filename_to_search)

return_refunds = True
while return_refunds == True:
    filename_to_search = "Returns and Refunds History.txt"
    return_refunds = find_txt_file(filename_to_search)

saved_address = True
while saved_address == True:
    filename_to_search = "Saved Address Information.txt"
    saved_address = find_txt_file(filename_to_search)

vouchers = True
while vouchers == True:
    filename_to_search = "Vouchers.txt"
    vouchers = find_txt_file(filename_to_search)



print("Activity(1)\nAds and data(2)\nApp Settings(3)\nDM's(4)\nIncome + Wallet Transactions(5)\nPosts(6)\nProfile(7)\nTikTok Live(8)\nTikTok Shopping(9)\n")
view = input('What would you like to see? ("q" to quit) >>> ')
while True:
    # Option 1: Activity
    if view == '1':
        activity_option = int(input("Browsing History(1)\nComments(2)\nFavorite effects, hashtags, sounds, videos(3)\nFollowers(4)\nFollowing(5)\nShare History(6)\nOther(7)\n>>>"))
        if activity_option == 1:
            with open(browsing_history, "r", encoding='utf-8') as history:
                print("\n\nBrowsing History: " + history.read())

        elif activity_option == 2:
            with open(comments, "r", encoding='utf-8') as comment:
                print("\n\nComments: " + comment.read())

        elif activity_option == 3:
            with open(fav_effect, "r", encoding='utf-8') as effect:
                print("\n\nEffects: " + effect.read())

            with open(fav_hash, "r", encoding='utf-8') as hash:
                print("\n\nHashtags: " + hash.read())

            with open(fav_sound, "r", encoding='utf-8') as sounds:
                print("\n\nSounds: " + sounds.read())

            with open(fav_video, "r", encoding='utf-8') as videos:
                print("\n\nVideos: " + videos.read())

        elif activity_option == 4:
            with open(followers, "r", encoding='utf-8') as followed_by:
                print("\n\nFollowers: " + followed_by.read())

        elif activity_option == 5:
            with open(following, "r", encoding='utf-8') as following:
                print("\n\nFollowing: " + following.read())

        elif activity_option == 6:
            with open(share_history, "r", encoding='utf-8') as shared:
                print("\n\nShare History: " + shared.read())

        elif activity_option == 7:
            with open(hashtags, "r", encoding='utf-8') as hashs:
                print("\n\nHashtags: " + hashs.read())

            with open(like_list, "r", encoding='utf-8') as like_lists:
                print("\n\nLike list: " + like_lists.read())

            with open(loc_review, "r", encoding='utf-8') as location:
                print("\n\nLocation Reviews?: " + location.read())

            with open(login_history, "r", encoding='utf-8') as logins:
                print("\n\nLogin History: " + logins.read())

            with open(purchases, "r", encoding='utf-8') as purchased:
                print("\n\nPurchases: " + purchased.read())

            with open(searches, "r", encoding='utf-8') as search:
                print("\n\nSearches: " + search.read())

            with open(status, "r", encoding='utf-8') as stats:
                print("\n\nStatus: " + stats.read())
        else:
            print("Please choose one of the options (1-6)")

    #Option 2
    elif view == '2':
        with open(ad_interest, "r", encoding='utf-8') as interest:
            print("\n\nAd Interests: " + interest.read())

        with open(ad_response, "r", encoding='utf-8') as response:
            print("\n\nAd form responses: " + response.read())

        with open(off_tiktok_activity, "r", encoding='utf-8') as off_activity:
            print("\n\nOff TikTok Activity: " + off_activity.read())
    
    #Option 3
    elif view == '3':
        settings = int(input('Blocked accounts(1)\nSettings(2)\n>>>'))
        if settings == 1:
            with open(block_list, "r", encoding='utf-8') as blocked:
                print("\n\nBlocked Accounts: " + blocked.read())
        elif settings == 2: 
           with open(accsettings, "r", encoding='utf-8') as account_settings:
                print("\n\nSettings: " + account_settings.read())
        else: 
            print("\n\nPlease choose one of the 2 options")
    
    #Option 4
    elif view == '4':
        with open(direct_messages, "r", encoding='utf-8') as dms:
                print("\n\nDMS: " + dms.read())

    #Option 5
    elif view == '5':
        with open(transaction_history, "r", encoding='utf-8') as transactions:
                print("\n\nTransactions: " + transactions.read())

    #Option 6
    elif view == '6':
        posts = int(input('Posts(1)\nRecently deleted posts(2)\n>>>'))
        if posts == 1:
            with open(post, "r", encoding='utf-8') as posts:
                print("\n\nPosts: " + posts.read())
        elif posts == 2: 
            with open(rdp, "r", encoding='utf-8') as recently_deleted:
                print("\n\nRecently Deleted Posts: " + recently_deleted.read())
        else: 
            print("Please choose one of the 2 options")

    #Option 7
    elif view == '7':
        profile = int(input('Profile info(1)\nOther(2)\n>>>'))
        if profile == 1: 
            with open(profile_info, "r", encoding='utf-8') as prof_info:
                print("\n\nProfile Info: " + prof_info.read())
        elif profile == 2: 
            with open(ai_moji, "r", encoding='utf-8') as ai_emoji:
                print("\n\nAI Emoji: " + ai_emoji.read())

            with open(auto_info, "r", encoding='utf-8') as auto_fill:
                print("\n\nAuto Fill Info: " + auto_fill.read())
        else: 
            print("Please choosse one of the 2 options")

    #Option 8
    elif view == '8':
        live = int(input('Live history *comments, watched lives, etc*(1)\nOther(2)\n>>>'))
        if live == 1: 
            with open(live_his, "r", encoding='utf-8') as live_history:
                print("\n\nLive History: " + live_history.read())
        elif live == 2: 
            with open(golive_his, "r", encoding='utf-8') as golive_history:
                print("\n\nGo Live History: " + golive_history.read())

            with open(golive_sets, "r", encoding='utf-8') as golive_settings:
                print("\n\nGo Live Settings: " + golive_settings.read())

            with open(watchlive_sets, "r", encoding='utf-8') as watchlive_settings:
                print("\n\nWatch Live Settings: " + watchlive_settings.read())
        else: 
            print("Please choose 1 of the 2 options")

    elif view == '9':
        shop = int(input('Orders(1)\nBrowsing History(2)\nShopping Cart(3)\nReviews(4)\nOther(5)\n>>>'))
        if shop == 1: 
            with open(orders, "r", encoding='utf-8') as order_history:
                print("\n\nOrder History: " + order_history.read())
        elif shop == 2: 
            with open(product_lookup_history, "r", encoding='utf-8') as plh:
                print("\n\nProduct Lookup History: " + plh.read())
        elif shop == 3: 
            with open(cart, "r", encoding='utf-8') as shopping_cart:
                print("\n\nShopping Cart: " + shopping_cart.read())
        elif shop == 4: 
            with open(reviews, "r", encoding='utf-8') as review_history:
                print("\n\nProduct reviews: " + review_history.read())
        elif shop == 5: 
            with open(communication, "r", encoding='utf-8') as shop_communication:
                print("\n\nShop Communication: " + shop_communication.read())

            with open(payment_info, "r", encoding='utf-8') as pay_info:
                print("\n\nPayment Info: " + pay_info.read())

            with open(customer_support, "r", encoding='utf-8') as support:
                print("\n\nCustomer Support: " + support.read())

            with open(disputes, "r", encoding='utf-8') as issues:
                print("\n\nDisputes: " + issues.read())

            with open(return_refunds, "r", encoding='utf-8') as returns:
                print("\n\nReturns/Refunds: " + returns.read())

            with open(saved_address, "r", encoding='utf-8') as addresses:
                print("\n\nSaved Addresses: " + addresses.read())

            with open(vouchers, "r", encoding='utf-8') as coupons:
                print("\n\nVouchers/Coupons: " + coupons.read())
        else: 
            print("Please choose one of the options (1-5)")
    
    #Quit
    elif view =="q":
        break

    else: 
        print('Please pick a number 1-9')
    view = input('\n\n\n\nWhat would you like to see? ("q to quit") >>> ')
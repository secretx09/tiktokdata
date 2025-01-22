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

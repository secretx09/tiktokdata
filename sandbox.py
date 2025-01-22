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
orders = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Order History.txt"
product_lookup_history = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Product Browsing History.txt"
cart = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Shopping Cart List.txt"
reviews = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Product Reviews.txt"
communication = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Communication with shops.txt"
payment_info = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Current Payment Information.txt"
customer_support = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Customer support history.txt"
disputes = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Order dispute history.txt"
return_refunds = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Returns and Refunds History.txt"
saved_address = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Saved Address Information.txt"
vouchers = "TikTok_Data_1735588272\Tiktok\TikTok Shopping\Vouchers.txt"


print(browsing_history)
print(comments)
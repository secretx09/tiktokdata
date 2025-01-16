class Main():
    def __init__(self):

        self.history = {}
        self.load_live_history()
    def load_live_history(self):
        with open(r'TikTok_Data_1735588272\Tiktok\TikTok Live\Watch Live History.txt', 'r', encoding='utf-8') as f:
            collecting_comments = False
            for line in f:
                line = line.strip()
                if line:
                    if line.startswith('Date and time:'):
                        
                        his_key = line[15:]
                    elif line.startswith("Comments you sent"):
                        comments = {}
                        collecting_comments = True
                    elif line.startswith("Questions you sent"):
                        questsions = []
                        collecting_comments = False

                    elif collecting_comments: 
                        
                        comment_key = line[:21]
                        comments[comment_key] = line[23:]

    def print_live_history(self):
        for key, value in self.history.items():
            print(key, value)

main = Main()
main.print_live_history()
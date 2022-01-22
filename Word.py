import datetime

class Word:
    def __init__(self, content, last_mentioned_on, google_results, part_of_speech):
        self.content = content
        
        if (last_mentioned_on == ''):
            self.last_mentioned_on = None
        else:
            self.last_mentioned_on = datetime.datetime.strptime(last_mentioned_on[:10], '%Y-%m-%d')
         
        self.google_results = google_results 
        
        if (part_of_speech == '' or part_of_speech == None):
            self.part_of_speech = None
        else:            
            self.part_of_speech = part_of_speech   
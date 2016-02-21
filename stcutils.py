# -*- coding: utf-8 -*-


# <teamID>-J-R[priority].txt
# <SYSDESC>[insert a short description in English here]</SYSDESC>
# [TweetID] 0 [RetrievedTweetID] [Rank] [Score][RunName]\n


class RunFile():

    def __init__(self, team_id, priority):
        self.team_id = team_id
        self.priority = priority
        self.results = []

    def set_desc(self, text):
        self.description = text

    def add(self, result):
        self.results.append(result)

    def format_for_stc(result):
        # TODO
        # convert result to formated text
        return text_formated

    def save(self):
        filename = '{0}-J-R{1}.txt'.format(self.team_id, self.priority)
        with open(filename, 'wb') as f:
            f.write('<SYSDESC>{}</SYSDESC>\n'.format(self.description))
            lines = [format_for_stc(result) for result in self.results]
            text = '\n'.join(lines)
            f.write(text)

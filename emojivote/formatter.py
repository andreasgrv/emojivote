import random


emojis = [':sunny:',
          ':umbrella:',
          ':cloud:',
          ':snowflake:',
          ':snowman:',
          ':zap:',
          ':cyclone:',
          ':foggy:',
          ':ocean:',
          ':cat:',
          ':dog:',
          ':mouse:',
          ':hamster:',
          ':rabbit:',
          ':wolf:',
          ':frog:',
          ':tiger:',
          ':koala:',
          ':bear:',
          ':pig:',
          ':cow:',
          ':boar:',
          ':monkey:',
          ':horse:',
          ':camel:',
          ':sheep:',
          ':elephant:',
          ':panda_face:',
          ':snake:',
          ':chicken:',
          ':penguin:',
          ':bug:',
          ':honeybee:',
          ':ant:',
          ':beetle:',
          ':octopus:',
          ':snail:',
          ':tropical_fish:',
          ':fish:',
          ':whale:',
          ':dolphin:',
          ':cd:',
          ':dvd:',
          ':fountain:',
          ':jack_o_lantern:',
          ':ghost:',
          ':bell:',
          ':balloon:',
          ':crystal_ball:',
          ':vhs:',
          ':minidisc:'
          ]


class SlackFormatter(object):
    """Format the relevant data fields in a way that looks good on Slack.
    Kudos to Kate McCurdy for coming up with the format."""
    def __init__(self, items):
        super(SlackFormatter, self).__init__()
        self.items = items

    def __repr__(self):
        snippets = []
        emoji_idxs = random.sample(range(len(emojis)), len(self.items))
        paper_emojis = [emojis[idx] for idx in emoji_idxs]
        for item, emoji in zip(self.items, paper_emojis):
            snippet = []
            snippet.append('%s *%s* ' % (emoji, item['title']))
            snippet.append('_%s_ ' % item['authors'])
            snippet.append(item['url'])
            snippet.append('%s' % item['abstract'])
            snippets.append('\n'.join(snippet))
        return '\n\n'.join(snippets)

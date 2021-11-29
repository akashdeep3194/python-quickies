from typing import Dict
import re
from os import read

class Solution():

    #Assumption is that the file contains username in the beginning of the line with <>
    def mostActive(self,path):

        user_messages: Dict[str, int] = {}
        user_with_max_msgs = None
        max_message_count = -1

        with open(path, mode='r') as messages_in_conversation:

            for message in messages_in_conversation:
                search_result = re.search('^<(.+?)>:', message)

                if not search_result:
                    continue
                user_name = search_result.group(1)
                user_message_count =user_messages.get(user_name, 0) + 1
                user_messages[user_name] = user_message_count

                if max_message_count < user_message_count:
                    max_message_count = user_message_count
                    user_with_max_msgs = user_name
        print("Most active user is:",user_with_max_msgs)
        return user_with_max_msgs

s = Solution()


if __name__ == '__main__':
    s.mostActive("chats.txt")

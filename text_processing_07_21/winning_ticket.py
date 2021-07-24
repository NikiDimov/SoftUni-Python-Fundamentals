import re

line = input().split(', ')

pattern = r'[$]{6,10}|[@]{6,10}|[#]{6,10}|[\^]{6,10}'
for ticket in line:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print('invalid ticket')
        continue
    left_text, right_text = ticket[:10], ticket[10:]
    left_result, right_result = re.findall(pattern, left_text), re.findall(pattern, right_text)
    if left_result and right_result and left_result[0][0] == right_result[0][0]:
        output = f"ticket \"{ticket}\" - {len(min(left_result[0], right_result[0]))}{left_result[0][0]}"
        if len(left_result[0]) == 10 and len(right_result[0]) == 10:
            output += " Jackpot!"
        print(output)
    else:
        print(f"ticket \"{ticket}\" - no match")

import re

participants_dict = {}
participants = input().split(", ")

pattern_participant = r'[A-Za-z]+'
pattern_d = r'\d'
info = input()
while not info == "end of race":
    result = re.findall(pattern_participant, info)
    result_d = re.findall(pattern_d, info)
    result_d = [int(el) for el in result_d]
    participant = ''.join(result)
    if participant in participants:
        if participant not in participants_dict:
            participants_dict[participant] = sum(result_d)
        else:
            participants_dict[participant] += sum(result_d)

    info = input()
participants_dict = dict(sorted(participants_dict.items(), key=lambda x: -x[1]))
final_result = [k for k in participants_dict]
final_result = final_result[:3]
print(f"1st place: {final_result[0]}\n2nd place: {final_result[1]}\n3rd place: {final_result[2]}")
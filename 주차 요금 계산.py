# 2022 KAKAO BLIND RECRUITMENT
# Level 2

import math
from collections import defaultdict

def solution(fees, records):
    # fees: 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
    # records: 시간 / 차량번호 / IN or OUT
    state_dic = defaultdict(int)
    time_dic = defaultdict(int)
    check_dic = defaultdict(int)
    answer = []
    
    # 입차 후 출차 시간 누적 계산
    for record in records:
        time, number, io = record.split()
        
        if io == "IN":
            state_dic[number] = int(time[:2]) * 60 + int(time[3:])
            check_dic[number] = 2
        else:
            time_dic[number] += int(time[:2]) * 60 + int(time[3:]) - state_dic[number]
            check_dic[number] = 1
    
    # 입차만 하고 출차가 없는 차량들
    for key, val in check_dic.items():
        if val == 2:
            time_dic[key] += 23 * 60 + 59 - state_dic[key]
    
    # 요금 부과
    for key, val in sorted(time_dic.items()):
        if val <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((val - fees[0]) / fees[2]) * fees[3])

    return answer
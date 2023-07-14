from collections import defaultdict

class Request:
    def __init__(self, sender, receive_time, status='sent'):
        self.sender = sender
        self.receive_time = receive_time
        self.status = status

class RateLimiter:
    def __init__(self, time_range, threshold):
        self.time_range = time_range
        self.th_request_cnt = threshold
        self.logs = []

    def should_process_request(self, request: Request):
        p = len(self.logs) - 1
        cnt = 1
        request.status = 'Pass'
        while p >= 0:
            if request.receive_time - self.logs[p].receive_time >= self.time_range:
                break
            cnt += 1 if self.logs[p].status == 'Pass' else 0
            p -= 1
            if cnt > self.th_request_cnt:
                request.status = 'Failure'
                break
        self.logs.append(request)
        return request.status == 'Pass'
    
rl = RateLimiter(3, 3)
print(rl.should_process_request(Request('A', 1)))
print(rl.should_process_request(Request('B', 2)))
print(rl.should_process_request(Request('C', 2)))
print(rl.should_process_request(Request('D', 3)))
print(rl.should_process_request(Request('A', 4)))
print(rl.should_process_request(Request('F', 5)))
print(rl.should_process_request(Request('G', 5)))
print(rl.should_process_request(Request('I', 10)))
                    



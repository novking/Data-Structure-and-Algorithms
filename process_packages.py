# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        if len(self.finish_time_)>=self.size:
            print ("this is finish time", len(self.finish_time_))
            if self.finish_time_[0]>request.arrival_time:
                return Response(True, -1)
            else:
                a = max((self.finish_time_ + request.process_time),(request.arrival_time + request.process_time))
                self.finish_time_.append(a)
                self.finish_time_ = self.finish_time_[1:]
                return Response(False, request.arrival_time)
        else:
            try:
                lastOne= self.finish_time_[-1]
            except:
                lastOne=0
            if lastOne<=request.arrival_time:
                self.finish_time_.append(request.arrival_time+request.process_time)
            else:
                self.finish_time_.append(lastOne+request.process_time)
            print ("this is finish time", len(self.finish_time_))
            return Response(False, request.arrival_time)
        

def ReadRequests(count):
    requests = []

    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    while True:
        size, count = map(int, input().strip().split())
        if count<1:
            print ()
            continue
        requests = ReadRequests(count)
    
        buffer = Buffer(size)
        responses = ProcessRequests(requests, buffer)
    
        PrintResponses(responses)

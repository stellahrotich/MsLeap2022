# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import queue
def solution(T):
    if T == [0]:
        return 1
    
    #create adjacency list - dictionary
    path = {}
    for i in range(1, len(T)):
        if i in path:
            path[i].append(T[i])
        else:
            path[i] = [T[i]]
        if T[i] in path:
            path[T[i]].append(i)
        else:
            path[T[i]] = [i]
    #bfs
    q = queue.Queue()
    q.put((0, False, 0)) #initialize the current node, ticket o use and numer of paths
    visited = set()
    max_number_of_path = 0
    while not q.empty():
        current, use_ticket, number_of_paths = q.get()
        if number_of_paths > max_number_of_path:
            max_number_of_path = number_of_paths

        for node in path[current]:
            #check if node is visited, then skip
            if (current, node) in visited or (node, current) in visited: 
                continue
            if node % 2 != 0 and use_ticket: #check if ticket is used
                continue
            if node % 2 != 0: # odd number, use one special ticket
                q.put((node, True, number_of_paths + 1))
            else:
                q.put((node, use_ticket, number_of_paths + 1))
            visited.add((current, node)) # mark as visited
    return max_number_of_path + 1

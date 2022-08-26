import heapq
import math

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):

    distance = 0
    coord_from = [[0,0] for i in range(7)]
    coord_to = [[0,0] for i in range(7)]

    for i in range(len(from_state)):
      if(from_state[i]!=0):
        coord_from[from_state[i]-1] = [int(i/3), i%3]
      if(to_state[i]!=0):
        coord_to[to_state[i]-1] = [int(i/3), i%3]

    for i in range(len(coord_from)):
      distance += abs(coord_from[i][0] - coord_to[i][0]) + abs(coord_from[i][1] - coord_to[i][1])
    return distance




def print_succ(state):
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    succ_states = []
    poss = []
    for i in range(len(state)):
      if(state[i]==0):
        if(i%3==1):
          poss = [i+1, i-1, i+3, i-3]
        elif(i%3==0):
          poss = [i+1, i-3, i+3]
        else:
          poss = [i-1, i+3, i-3]
        for j in poss:
          if j<=8 and j>=0:
            temp = state.copy()
            if(not (temp[i]==0 and temp[j]==0)):
              temp[i]=temp[j]
              temp[j] = 0
              succ_states.append(temp)        
   
    return sorted(succ_states)

def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """

    CLOSE = []
    OPEN = []
    VISITED = []
    h = get_manhattan_distance(state)
    start = (h, state, (0, h, -1))
    heapq.heappush(OPEN, start)
    parent = 0  
    while True:
        if not OPEN:
            break
        pop = heapq.heappop(OPEN)
        CLOSE.append(pop)
        
        if pop[1]==[1, 2, 3, 4, 5, 6, 7, 0, 0]:
            break

        g_curr = pop[2][0] + 1

        next = get_succ(pop[1])
        for x in next:
            h_next = get_manhattan_distance(x)
            node_new = (g_curr + h_next, x, (g_curr, h_next, parent))
            if x in VISITED:
                continue

            heapq.heappush(OPEN, node_new)

        VISITED.extend(next)
        parent += 1

    node = CLOSE[-1]
    trace = []
    while node[2][2] > 0:
        node = CLOSE[node[2][2]]
        trace.append(node)

    trace.append(start)
    trace.reverse()
    trace.append(pop)

    for node in trace:  # trace print
      print('{} h={} moves: {}'.format(node[1], node[2][1], node[2][0]))
    print('Max queue length: {}'.format(len(OPEN)))

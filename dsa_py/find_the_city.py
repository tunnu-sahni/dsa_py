# find the city with the smallest number of neighbors at a threshold distance

def find_city(n, m, edges, distance_threshold):
    dist = [[float('inf')] * n for _ in range(n)]

    for edges in edges:
        dist[edges[0]][edges[1]] == edges[2]
        dist[edges[1]][edges[0]] == edges[2]

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][k])

    cnt_city = n
    city_no = -1

    for city in range(n):
        cnt = 0
        for adj_city in range(n):
            if dist[city][adj_city] <= distance_threshold:
                cnt += 1

        if cnt <= cnt_city:
            cnt_city = cnt
            city_no = city

    return city_no

def main():
    n = 4
    m = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distance_threshold = 4

    city_no = find_city(n, m, edges, distance_threshold)

    print("The answer is node:", city_no)

if __name__ == "__main__":
    main()
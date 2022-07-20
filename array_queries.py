def get_element_sum(A, B, a_idx, b_idx):
    return A[a_idx] * B[b_idx] * (a_idx + b_idx + 2)
    
def get_F_matrix(A, B, N, M):
    F = []
    total_sum = 0
    for a_idx in range(N):
        f = []
        for b_idx in range(M):
            sum = get_element_sum(A, B, a_idx, b_idx)
            total_sum += sum
            f.append(sum)
        F.append(f)
    return total_sum % 998244353, F

def update_data_A(i, M, A, B, F, total_sum):
    for idx in range(M):
        total_sum -= F[i][idx]
        F[i][idx] = get_element_sum(A, B, i, idx)
        total_sum += F[i][idx]
    return total_sum 

def update_data_B(j, N, A, B, F, total_sum):
    for idx in range(N):
        total_sum -= F[idx][j]
        F[idx][j] = get_element_sum(A, B, idx, j)
        total_sum += F[idx][j]
    return total_sum
 
def array_queries (N, M, A, B, Q, queries):
    ans = []
    total_sum, F = get_F_matrix(A, B, N, M)
    ans.append(total_sum)
 
    for query in queries:
        query_type = query[0]
        i = query[1] - 1
        j = query[2] - 1

        if query_type == 1:
            A[i], B[j] = B[j], A[i]
            total_sum = update_data_B(j, N, A, B, F, update_data_A(i, M, A, B, F, total_sum))
 
        elif query_type == 2:
            A[i], A[j] = A[j], A[i]
            total_sum = update_data_A(j, M, A, B, F, update_data_A(i, M, A, B, F, total_sum))

        else:
            B[i], B[j] = B[j], B[i]
            total_sum = update_data_B(j, N, A, B, F, update_data_B(i, N, A, B, F, total_sum))

        ans.append(total_sum % 998244353)

    return ans
 
 
T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for i in range(Q)]
 
    out_ = array_queries(N, M, A, B, Q, queries)
    print (' '.join(map(str, out_)))
H, W, N, M = map(int, input().split())

h_div_n = H // (N + 1)
w_div_m = W // (M + 1)
h_mod_n = 1 if H % (N + 1) else 0
w_mod_m = 1 if W % (M + 1) else 0
print((h_div_n + h_mod_n) * (w_div_m + w_mod_m))

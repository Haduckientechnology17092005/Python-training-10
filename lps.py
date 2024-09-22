def longest_palindromic_subsequence(s):
    n = len(s)
    # Tạo bảng 2D để lưu độ dài LPS
    dp = [[0] * n for _ in range(n)]
    
    # Các ký tự đơn lẻ là palindrome có độ dài 1
    for i in range(n):
        dp[i][i] = 1
    
    # Điền bảng DP
    for length in range(2, n + 1):  # length từ 2 đến n
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]  # Độ dài LPS

def min_insertions_to_palindrome(s):
    lps_length = longest_palindromic_subsequence(s)
    return len(s) - lps_length

# Ví dụ sử dụng
s = "hahahihie"
print("Số ký tự cần thêm:", min_insertions_to_palindrome(s))

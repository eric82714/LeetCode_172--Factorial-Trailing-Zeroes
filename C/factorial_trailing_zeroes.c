int trailingZeroes(int n){
    long long ans = 0, a = 5;
        
    while(a <= n) {
        ans += (n / a);
        a *= 5;
    }
    return ans;
}

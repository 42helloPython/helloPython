func solution(_ num:Int) -> Int {
    var num = num
    for i in 1...500 {
        if num % 2 == 0 {
            num /= 2
        } else {
            num *= 3
            num += 1
        }
        if num == 1 { return i }
    }
    return -1
}

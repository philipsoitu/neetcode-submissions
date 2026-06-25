type Bounds struct {
    lower int
    upper int
}

func longestConsecutive(nums []int) int {
    hm := map[int]*Bounds{}

    for _, x := range nums {
        if _, exists := hm[x]; exists {
            continue
        }

        left, hasLeft := hm[x-1]
        right, hasRight := hm[x+1]

        switch {
        case hasLeft && hasRight:
            left.upper = right.upper
            for i := right.lower; i <= right.upper; i++ {
                hm[i] = left
            }
            hm[x] = left

        case hasLeft:
            left.upper = x
            hm[x] = left

        case hasRight:
            right.lower = x
            hm[x] = right

        default:
            hm[x] = &Bounds{x, x}
        }
    }

    ans := 0
    for _, b := range hm {
        length := b.upper - b.lower + 1
        if length > ans {
            ans = length
        }
    }

    return ans
}
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)  # Initialize segment tree array with a large enough size
        self.build(0, 0, self.n - 1, arr)
    
    def build(self, ind, low, high, arr):
        if low == high:
            self.seg[ind] = arr[low]
            return
        
        mid = (low + high) // 2
        self.build(2 * ind + 1, low, mid, arr)
        self.build(2 * ind + 2, mid + 1, high, arr)
        self.seg[ind] = min(self.seg[2 * ind + 1], self.seg[2 * ind + 2])

    def query(self, ind, low, high, l, r):
        # No overlap
        if low > r or high < l:
            return float('inf')
        
        # Complete overlap
        if low >= l and high <= r:
            return self.seg[ind]
        
        # Partial overlap
        mid = (low + high) // 2
        left = self.query(2 * ind + 1, low, mid, l, r)
        right = self.query(2 * ind + 2, mid + 1, high, l, r)
        return min(left, right)

    def update(self, ind, low, high, idx, value):
        if low == high:
            # Leaf node; update the segment tree node
            self.seg[ind] = value
            return
        
        mid = (low + high) // 2
        if idx <= mid:
            # If the index to be updated is in the left child
            self.update(2 * ind + 1, low, mid, idx, value)
        else:
            # If the index to be updated is in the right child
            self.update(2 * ind + 2, mid + 1, high, idx, value)
        
        # After the child is updated, update the current node
        self.seg[ind] = min(self.seg[2 * ind + 1], self.seg[2 * ind + 2])

    def range_query(self, l, r):
        return self.query(0, 0, self.n - 1, l, r)

    def point_update(self, idx, value):
        self.update(0, 0, self.n - 1, idx, value)

# Example usage
arr = [1, 3, 2, 7, 9, 11]
segment_tree = SegmentTree(arr)

# Perform a range minimum query
print("Min in range (1, 4):", segment_tree.range_query(1, 4))  # Output: 2

# Update the array and segment tree
segment_tree.point_update(2, 6)  # Update index 2 to value 6

# Perform the query again after the update
print("Min in range (1, 4) after update:", segment_tree.range_query(1, 4))  # Output: 6

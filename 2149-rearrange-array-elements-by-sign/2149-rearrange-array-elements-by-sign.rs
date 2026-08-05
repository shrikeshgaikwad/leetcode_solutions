impl Solution {
    pub fn rearrange_array(mut nums: Vec<i32>) -> Vec<i32> {
        let mut positives = Vec::new();
        let mut negatives = Vec::new();

        for &num in nums.iter() {
            if num > 0 {
                positives.push(num);
            } else {
                negatives.push(num);
            }
        }

        let mut j = 0;
        for i in 0..positives.len() {
            nums[j] = positives[i];
            nums[j + 1] = negatives[i];
            j += 2;
        }

        nums
    }
}
class Solution {
    public int heightChecker(int[] heights) {
        int[] templist = heights.clone();
        Arrays.sort(templist);
        int counter = 0;
        for(int i = 0; i<heights.length;i++){
            if (templist[i] != heights[i]){counter++;}
        }
        return counter;
    }
}

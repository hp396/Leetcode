class Solution {
    public int[] countBits(int num) {
        int[] output = new int[num+1];
        //ArrayList<Integer> result = new ArrayList();
        for (int i = 0;i<=num;i++){
            char[] binch = (Integer.toBinaryString(i)).toCharArray();
            // char[] binch = bin.;
            int count = 0;
            for (char c :binch){
                if (c=='1'){
                    count++;
                }
            }
            output[i]=count;
        }      
        return output;
    }
}
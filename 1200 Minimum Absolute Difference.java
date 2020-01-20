class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> list1 = new ArrayList<List<Integer>>();;
        Arrays.sort(arr);
        int minab = 5000000;
        for (int i = 0; i<arr.length-1;i++){
            if(Math.abs(arr[i]-arr[i+1])<minab){
                minab = Math.abs(arr[i]-arr[i+1]);
            }
        }
        for(int i = 0; i<arr.length-1;i++){
            if(Math.abs(arr[i]-arr[i+1])==minab){
                list1.add(Arrays.asList(arr[i],arr[i+1]));
            }
        }
        return list1;   
    }
}

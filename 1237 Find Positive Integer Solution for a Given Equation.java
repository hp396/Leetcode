/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     public int f(int x, int y);
 * };
 */
class Solution {
    public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        for (int x = 1;  x<= 1000;x++){
                if (customfunction.f(x,1)>z){
                    break;
                }            
            for (int y = 1; y <= 1000; y++){
                if (customfunction.f(x,y)>z){         //Breaks since the function will return higher value as x/y goes higher and it makes a lot of difference for time complexity!
                    break;
                }
                List<Integer> append = new ArrayList<Integer>();
                if (customfunction.f(x,y) == z){
                    append.add(x);
                    append.add(y);
                    output.add(append);
                }
            }
        }
        return output;
    }
}

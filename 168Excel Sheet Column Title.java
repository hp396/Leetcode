class Solution {
    public String convertToTitle(int n) {
        int div = n;
        String output = "";
        int mod;
        while (div > 0){
            modulo = (div-1) % 26;
            //System.out.println(mod);
            output = String.valueOf((char)(65+mod))+output;
            dividend = (int)((div - mod) / 26);
        }
        return output;
    }
}

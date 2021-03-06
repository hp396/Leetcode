class Solution {
    public String frequencySort(String s) {
        Map<Character,Integer> mymap = new HashMap<Character, Integer>();
        for(Character ch: s.toCharArray()){
            if(mymap.containsKey(ch)){
                mymap.put(ch, mymap.get(ch) + 1);
            }else{
                mymap.put(ch,1);
            }
        }
        System.out.println(mymap);
        String output = "";
        while(!(mymap.isEmpty())){
            Character key = Collections.max(mymap.entrySet(), Map.Entry.comparingByValue()).getKey();
            for(int i = mymap.get(key); i!=0;i--){
                output= output + key;
            }
            mymap.remove(key);
        }
        return output;
    }
}
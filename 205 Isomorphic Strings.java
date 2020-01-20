class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character,Character> outputhash = new HashMap<>();
        boolean key;
        boolean value;
        for (int i =0;i<s.length();i++){
            key = outputhash.containsKey(s.charAt(i));              //Boolean key exists
            value = outputhash.containsValue(t.charAt(i));          //Boolean value exists
            if(key || value){                                       //If key or value exists
                if(key && value){                                   //If they both exist then the key should have the same value
                    if(!(outputhash.get(s.charAt(i)).equals(t.charAt(i)))){
                        return false;    
                    }
                }
                //If only one of them exists then return false
                else if(key && !value){                             
                    return false;
                }else if(!key && value){
                    return false;
                }
            }else{      //add to hashmap if both dont exist
                outputhash.put(s.charAt(i),t.charAt(i));
            }
        }
        return true;
    }
}

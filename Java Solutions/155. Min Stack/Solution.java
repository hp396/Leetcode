class MinStack {
    ArrayList<Integer> stack = new ArrayList<Integer>();
    
    int MIN = Integer.MAX_VALUE;
    /** initialize your data structure here. */
    public MinStack() {
    }
    
    public void push(int x) {
        this.stack.add(x);
    }
    
    public void pop() {
        this.stack.remove(stack.size()-1);
    }
    
    public int top() {
        return this.stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return Collections.min(stack);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
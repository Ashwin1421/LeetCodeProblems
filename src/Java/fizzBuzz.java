class Solution {
    public List<String> fizzBuzz(int n) {
            List<String> result = new LinkedList<>();
            for(int i=1;i<=n;i++){
                if((i % 3 == 0) && (i % 5 != 0)){
                    result.add(i-1,"Fizz");
                } else
                if((i % 5 == 0) && (i % 3 != 0)){
                    result.add(i-1, "Buzz");
                } else
                if( (i % 3 == 0) && (i % 5 == 0)){
                    result.add(i-1, "FizzBuzz");
                } else {
                    result.add(i-1, Integer.toString(i));
                }

            }
            return result;
        }
}
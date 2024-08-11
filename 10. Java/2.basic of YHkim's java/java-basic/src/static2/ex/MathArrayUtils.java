package static2.ex;

public class MathArrayUtils {
    private static int[] values;

    public MathArrayUtils() {
    }

    public static int sum(int[] values){
        int total = 0;
        for (int value : values){
            total += value;
        }
        return total;
    }

    public static float average(int[] values){
        return sum(values) / values.length;
    }

    public static int max(int[] values){
        int tmp = 0;
        //int tmp = value[0];
        for (int value : values){
            if(value > tmp){
                tmp = value;
            }
        }
        return tmp;
    }

    public static int min(int[] values){
        int tmp = max(values);
        //int tmp = value[0];
        for(int value : values){
            if(value < tmp){
                tmp = value;
            }
        }
        return tmp;
    }
}

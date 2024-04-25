using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
        int[] answer = new int[commands.GetLength(0)];
        List<int> list = new List<int>();
        for (int i = 0; i < commands.GetLength(0) ; i++)
        {
            int start = commands[i,0];
            int end = commands[i,1];
            int num = commands[i,2];
            
            for (int j = start-1; j <= end-1; j ++ )
            {
                list.Add(array[j]);
            }
            
            // foreach ( int z in list )
            // {
            //     Console.WriteLine(z);
            // }
            // Console.WriteLine("end");
            
            list.Sort();
            answer[i] = list[num-1];
            list.Clear();

        }
        
        return answer;
    }
}
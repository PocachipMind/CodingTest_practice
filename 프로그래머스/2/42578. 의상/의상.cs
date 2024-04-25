using System;
using System.Collections.Generic;

public class Solution {
    public int solution(string[,] clothes) {
        int answer = 1;
        
        Dictionary<string,int> dic = new Dictionary<string, int>();
        
        for (int i = 0 ; i < clothes.GetLength(0); i++)
        {
            string kind = clothes[i,1];
            
            if (dic.ContainsKey(kind))
            {
                // System.Console.WriteLine(kind);
                dic[kind] += 1;
            }
            else
            {
                dic.Add(kind,1);
            }
        }
        foreach ( var Val in dic )
        {
            Console.WriteLine(Val.Value);
            answer *= Val.Value+1;
        }
        
        return answer-1;
    }
}
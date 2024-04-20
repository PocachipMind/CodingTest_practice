#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {

    vector<int> answer;

    // for ( int i = 0 ; i < commands.size(); i++) 도 가능
    for (auto i : commands)
    {
        vector<int> temp;

        for (int j = 0; j <= i[1]-i[0]; j++)
        {
            temp.push_back(array[i[0]-1+j]);
        }
        sort(temp.begin(), temp.end());
        answer.push_back(temp[i[2]-1]);

    }


    return answer;
}
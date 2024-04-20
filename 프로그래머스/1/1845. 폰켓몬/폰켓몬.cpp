#include <vector>
#include <cmath>
#include <set>

using namespace std;

int solution(vector<int> nums)
{
    set <int>i (nums.begin(),nums.end());
    int pick = i.size();
    int lennums = nums.size()/2;
    
    if (pick < lennums)
    {
        return pick;
    }
    else return lennums;

}
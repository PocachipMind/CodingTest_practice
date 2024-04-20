#include<vector>
#include<queue>
using namespace std;

class Node{
    public:
    int x;
    int y;
    int dist;
    Node(int x,int y,int dist)
    {
        this->x = x;
        this->y = y;
        this->dist = dist;
    }
};

int solution(vector<vector<int> > maps)
{
    int dx[] = {0,0,-1,1};
    int dy[] = {-1,1,0,0};
    
    queue<Node> q;
    
    q.push(Node(0,0,1));
    
    while (!q.empty())
    {
        Node now = q.front();
        q.pop(); 
        
        if (now.x == maps.size()-1 && now.y == maps[0].size()-1)
        {
            return now.dist;
        }
        
        for (int i = 0 ; i < 4 ; i++)
        {
            int nx = now.x + dx[i];
            int ny = now.y + dy[i];
            
            if (nx < 0 || nx >= maps.size() ||ny < 0 || ny >= maps[0].size())
            {
                continue;
            }
            
            if (maps[nx][ny] == 1)
            {
                q.push(Node(nx,ny,now.dist+1));
                maps[nx][ny] = now.dist+1;
            }
            
        }
    }
    
    return -1;
}
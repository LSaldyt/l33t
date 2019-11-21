// https://www.hackerrank.com/challenges/frog-in-maze/problem
#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

struct Point
{
    int i;
    int j;
    Point(int set_i, int set_j) : i(set_i), j(set_j) {}
};

struct Tunnel
{
    int i0, j0, i1, j1;
    Tunnel(int set_i0, int set_j0, int set_i1, int set_j1) : i0(set_i0), j0(set_j0), i1(set_i1), j1(set_j1) {}
};

using Tunnels = vector<Tunnel>;

struct Cell
{
    double probability;
    char type;
    bool visited;
    vector<Point> dependents;

    Cell(char set_type) : type(set_type), probability(0), visited(false) {}
};

using PointQueue = queue<Point>;

using Grid = vector<vector<Cell>>;

bool checkPoint(Point p, int n, int m, Grid& grid)
{
    auto & cell = grid[p.i][p.j];
    return (p.i >= 0 and p.i < n and p.j >= 0 and p.j < m and cell.type != '#' and cell.type != '*' and !cell.visited);
}

vector<Point> getAdjacent(int i, int j, int n, int m, Grid& grid)
{
    vector<Point> adj;
    vector<Point> checked;
    adj.push_back(Point(i+1, j));
    adj.push_back(Point(i,j+1));
    adj.push_back(Point(i - 1, j));
    adj.push_back(Point(i, j - 1));

    for (auto p : adj)
    {
        if (checkPoint(p, n, m, grid))
        {
            checked.push_back(p);
        }
    }

    return checked; // By value!
}

void visit(int n, int m, int i, int j, PointQueue& pointQueue, vector<vector<Cell>>& probmap)
{
    auto adjacent = getAdjacent(i, j, n, m, probmap);
    double rootProb = probmap[i][j].probability;
    double adjProb  = rootProb / adjacent.size();
    for (auto adj : adjacent)
    {
        auto& cell = probmap[adj.i][adj.j];
        if (cell.type == 'A')
        {
            std::cout << adjProb << std::endl;
        }
        else
        {
            cell.probability = adjProb;
            cell.visited = true;
        }
        pointQueue.push(adj);
    }
}

void solution(int n, int m, int k, vector<string> rows, Tunnels tunnels)
{
    PointQueue pointQueue;
    vector<vector<Cell>> probmap;
    int i = 0;
    for (auto row : rows)
    {
        probmap.push_back(vector<Cell>());
        int j = 0;
        for (auto cell_type : row)
        {
            probmap[i].push_back(Cell(cell_type));
            if (cell_type == '%')
            {
                pointQueue.push(Point(i, j));
                probmap[i][j].probability = 1.0;
                probmap[i][j].visited = true;
            }
            if (cell_type == '*')
            {
                probmap[i][j].probability = 0.0;
                probmap[i][j].visited = true;
            }
            j++;
        }
        i++;
    }

    while(pointQueue.size() > 0)
    {
        Point point = pointQueue.front();
        pointQueue.pop();
        visit(n, m, point.i, point.j, pointQueue, probmap);
    }
}


int main()
{
    string nmk_temp;
    getline(cin, nmk_temp);

    vector<string> nmk = split_string(nmk_temp);

    int n = stoi(nmk[0]);

    int m = stoi(nmk[1]);

    int k = stoi(nmk[2]);

    vector<string> rows;
    rows.reserve(n);

    for (int n_itr = 0; n_itr < n; n_itr++) {
        string row;
        getline(cin, row);

        rows.push_back(row);
    }

    Tunnels tunnels;
    for (int k_itr = 0; k_itr < k; k_itr++) {
        string i1J1I2J2_temp;
        getline(cin, i1J1I2J2_temp);

        vector<string> i1J1I2J2 = split_string(i1J1I2J2_temp);

        int i1 = stoi(i1J1I2J2[0]);

        int j1 = stoi(i1J1I2J2[1]);

        int i2 = stoi(i1J1I2J2[2]);

        int j2 = stoi(i1J1I2J2[3]);

        tunnels.push_back(Tunnel(i1, j1, i2, j2));
    }
    solution(n, m, k, rows, tunnels);

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}


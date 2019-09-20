#include <vector>
#include <iostream>

using std::vector;

template <class T>
void rotate_matrix(vector<vector<T>>& matrix)
{
    int n = matrix.size();
    for (int i = 0; i < n / 2; i++) 
    {
        for (int j = i; j < n - 1; j++)
        {
            int a = i;
            int b = j;
            T rotator = matrix[a][b];
            do {
                int x = b;
                int y = n - 1 - a;
                T temp = matrix[x][y];
                matrix[x][y] = rotator;
                a = x;
                b = y;
                rotator = temp;
            } while (a != i and b != j);
        }
    }
}

template <class T>
void print_matrix(vector<vector<T>>& matrix)
{
    for (auto row : matrix)
    {
        for (auto item : row)
        {
            std::cout << item << ", ";
        }
        std::cout << std::endl;
    }
}

int main()
{
    vector<vector<int>> matrix = {{1,2,3}, {4, 5, 6}, {7, 8, 9}};
    print_matrix(matrix);
    rotate_matrix(matrix);
    std::cout << std::endl;
    print_matrix(matrix);
}

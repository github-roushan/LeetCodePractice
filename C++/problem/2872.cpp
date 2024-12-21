#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution
{
public:
    int maxKDivisibleComponents(int n, vector<vector<int>> &edges, vector<int> &values, int k)
    {
        // Create an adjacency list to represent the graph
        vector<vector<int>> graph(n);

        // Populate the graph with edges
        for (auto &vec : edges)
            graph[vec[0]].push_back(vec[1]), graph[vec[1]].push_back(vec[0]);

        // Start DFS from node 0 with no parent (-1)
        // The pair contains the (sum of values in current_component, total_components so far)
        pair<int, int> pi = countPossibleComponents(0, -1, graph, values, k);

        // Return the total number of components divisible by k
        return pi.second;
    }

    // DFS function to compute the sum of values in the component and count the valid components
    pair<int, int> countPossibleComponents(int node, int parent, vector<vector<int>> &graph, vector<int> &values, int k)
    {
        int curSum = values[node]; // Start with the current node's value
        int totalComponents = 0;   // Initialize the count of valid components

        // Explore each neighbor of the current node
        for (int i = 0; i < graph[node].size(); i++)
        {
            // Skip the parent node to avoid revisiting
            if (graph[node][i] == parent)
                continue;

            // Recursively explore the child node and accumulate the sum and valid components
            pair<int, int> pi = countPossibleComponents(graph[node][i], node, graph, values, k);
            curSum += pi.first;
            totalComponents += pi.second;
        }

        // If the current component sum is divisible by k, count it as a valid component
        if (curSum % k == 0)
            totalComponents++;

        // Return the sum modulo k and the total count of valid components
        return make_pair(curSum % k, totalComponents);
    }
};

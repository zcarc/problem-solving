#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {

    queue<int> waiting_trucks;
    queue<int> bridge_on;
    int sum_bridge_on = 0;
    int time = 0;

    for (int i = 0; i < truck_weights.size(); i++) {
      waiting_trucks.push(truck_weights.at(i));
    }

    while (!waiting_trucks.empty()) {
      if (bridge_on.size() < bridge_length) {
        if (sum_bridge_on + waiting_trucks.front() <= weight) {
          int waiting_truck = waiting_trucks.front();
          bridge_on.push(waiting_truck);
          sum_bridge_on += waiting_truck;
          waiting_trucks.pop();
        }
        else {
          bridge_on.push(0);
        }
        time++;
      }
      else {
        int out_bridge = bridge_on.front();
        sum_bridge_on -= out_bridge;
        bridge_on.pop();
      }

    }

    return time + bridge_length;
}
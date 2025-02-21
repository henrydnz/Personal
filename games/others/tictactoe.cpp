#include <bits/stdc++.h>
#include <stdlib.h>

using namespace std;

int board[3][3];
map<int, char> cell{{0, '_'}, {1, 'X'}, {2, 'O'}};

int check() {       //checks win

    //check diag and antdiag
    if (board[1][1]) {  
        if((board[0][0]==board[1][1])&&(board[1][1]==board[2][2])) return board[1][1];
        if((board[2][0]==board[1][1])&&(board[1][1]==board[0][2])) return board[1][1];
    }
    //check rows and columns
    for (int i = 0; i < 3; i++) {
        if((board[i][0]==board[i][1])&&(board[i][1]==board[i][2])) return board[i][0];
        if((board[0][i]==board[1][i])&&(board[1][i]==board[2][i])) return board[0][i];
    }

    return 0;
}

void draw() {       //draws table

    cout<<"  A B C\n";
    for(int i = 0; i < 3; i++) {
        cout << i+1 << " ";
        for(int j = 0; j < 3; j++)
            cout << cell[board[i][j]] << " ";
        cout << "\n";
    }
    cout << "\n";
}

void round() {
    char c; int n, player=0;
    draw();
    while(1) {
        cout<< cell[player+1] << ", input your coordinates (a,b,c,1,2,3): ";
        cin >> c >> n;
        if(!board[n-1][c-97]) {
            board[n-1][c-97] = player+1;
            system("CLS");
            draw();
            if(check()) {
                cout << cell[check()] <<" won";
                return;
            }
            if(player) player = 0;
            else player = 1;
        } 
        else cout << "this cell is occupied\n";
    }
}

int main() {
    round();
}
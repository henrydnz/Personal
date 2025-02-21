
#include <bits/stdc++.h>
using namespace std;

// Função para imprimir a grid
void imprimirGrid(string grid[4][4]) {
    cout << " " << grid[0][0] << " | " << grid[0][1] << " | " << grid[0][2] << " | " << grid[0][3] << endl;
    cout << "-----------" << endl;
    cout << " " << grid[1][0] << " | " << grid[1][1] << " | " << grid[1][2] << " | " << grid[1][3] << endl;
    cout << "-----------" << endl;
    cout << " " << grid[2][0] << " | " << grid[2][1] << " | " << grid[2][2] << " | " << grid[2][3] << endl;
    cout << "-----------" << endl;
    cout << " " << grid[3][0] << " | " << grid[3][1] << " | " << grid[3][2] << " | " << grid[3][3] << endl;
}

// Função para verificar vitória
bool verificarVitoria(string grid[4][4], string jogador) {
    // Verificar linhas
    for (int i = 0; i < 4; i++) {
        if (grid[i][0] == jogador && grid[i][1] == jogador && grid[i][2] == jogador && grid[i][3] == jogador) {
            return true;
        }
    }
    // Verificar colunas
    for (int i = 0; i < 4; i++) {
        if (grid[0][i] == jogador && grid[1][i] == jogador && grid[2][i] == jogador && grid[3][i] == jogador) {
            return true;
        }
    }
    // Verificar diagonais
    if ((grid[0][0] == jogador && grid[1][1] == jogador && grid[2][2] == jogador && grid[3][3] == jogador) ||
        (grid[0][3] == jogador && grid[1][2] == jogador && grid[2][1] == jogador && grid[3][0] == jogador)) {
        return true;
    }
    return false;
}

int main() {
    string grid[4][4] = {
                        {"1", "2", "3", "4"},
                        {"5", "6", "7", "8"},
                        {"9", "10", "11", "12"},
                        {"13", "14", "15", "16"}                                                               
                        };
    string jogador = "X";
    int jogadas = 0;

    while (jogadas < 16) {
        imprimirGrid(grid);
        cout << "Jogador " << jogador << ", escolha uma posição (1-16): ";
        int posicao;
        cin >> posicao;

        // Converter posição para coordenadas
        int linha = (posicao - 1) / 4;
        int coluna = (posicao - 1) % 4;

        // Verificar se posição está vazia
        if (grid[linha][coluna] != "X" && grid[linha][coluna] != "O") {
            grid[linha][coluna] = jogador;
            jogadas++;

            // Verificar vitória
            if (verificarVitoria(grid, jogador)) {
                imprimirGrid(grid);
                cout << "Jogador " << jogador << " venceu!" << endl;
                return 0;
            }

            // Alternar jogador
            jogador = (jogador == "X") ? "O" : "X";
        } else {
            cout << "Posição ocupada! Escolha outra." << endl;
        }
    }

    imprimirGrid(grid);
    cout << "Empate!" << endl;
    return 0;
}

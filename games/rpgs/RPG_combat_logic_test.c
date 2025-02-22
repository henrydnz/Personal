//exploring rpg pvp design in c

#include <stdio.h>

void stats(int atk, int hp) {
    printf("player atk: %d\n", atk);
    printf("player hp: %d\n", hp);
}

int luta (int atk, int hp, int enemyatk, int enemyhp) {
    while (1) {
        printf("1 - attack\n2 - block\n");
        int c; scanf("%d", &c);
        if (c == 1) {
            enemyhp-=atk;
            if(enemyhp<=0) break;
            hp-=enemyatk;
            if(hp<=0) {
                printf("you died...");
                return 0;
            }
        }
        printf("---\n");
        printf("goblin - %dhp\n", enemyhp);
        printf("player - %dhp\n", hp);
    }
    printf("X.X goblin died\n");
    return hp;
}

int main() {

    printf("========== GOBLIN FOREST ==========\n\n");

    int atk=5, hp=20;

    stats(atk, hp);

    printf("\n== ENCOUNTER: Goblin (%datk / %dhp)\n", 3, 20);

    hp = luta (atk, hp, 3, 20);
    
    stats(atk, hp);

}
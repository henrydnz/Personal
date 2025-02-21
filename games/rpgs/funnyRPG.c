// fiz na aula

#include <stdio.h>

int main() {
    do 
    {
        // comeco
        printf("\n\nbem vindo ao jogo\n");
        printf("voce ta na masmorra pra matar O  MOSTO\n");
        printf("escolhe sua arma\n");
        
        // escolher arma
        printf("1 = espada\n");
        printf("0 = arco\n");
        printf("escolha: ");
        int arma; 
        scanf("%d", &arma);
        if (arma) printf("voce escolheu espada\n");
        else printf("voce escolheu arco\n");
        
        // batalha
        printf("o mostro ta vino mate ele por favor pa salva princisa\n");
        printf("o que voce quer fazer\n");
        // espada
        if (arma) {         
            printf("1 - chegar perto do mosto pra bater\n");
            printf("0 - fica parado\n");
            printf("escolha: ");
            int escolha1;
            scanf("%d", &escolha1);
            // chegando perto 
            if (escolha1) {
                printf("vc ta do lado dele escolhe onde atacar\n");
                printf("1 - atacar na garganta\n");
                printf("0 - atacar na barriga\n");
                printf("escolha: ");
                int escolha2;
                scanf("%d", &escolha2);
                // garganta
                if (escolha2) {
                    printf("mato dai a princiesa gostou de voce\n");
                    printf("1 - beijar\n");
                    printf("0 - ignorar e ir embora\n");
                    printf("escolha: ");            
                    int escolha3;
                    scanf("%d", &escolha3);
                    // beijo
                    if (escolha3) {
                        printf("voces casaram e viveram felizes por 7 anos\n");
                        printf("depois ela te traiu e voce morreu de depressao\ngame over\n");
                    }
                    // ir embora
                    else {
                        printf("voce foi embora da masmorra virou gigachad e ganhou na vida\ngame win\n");
                    }
                }
                // barriga
                else printf("ele tava gravido os filhos dele te mataram\ngame over\n");
            }
            // parado
            else printf("ele chegou e te matou\ngame over\n");
        }
        // arco
        else {          
            printf("atira ondde");
            printf("1 - atirar no pe\n");
            printf("0 - atirar na cabeca\n");
            printf("escolha: ");
            int escolha4;
            scanf("%d", &escolha4);
            // cabeca
            if (escolha4) printf("ele te mato burro o pe nao da dano\ngame over\n");
            //
            else {
                printf("mato dai a princiesa gostou de voce\n");
                printf("1 - beijar\n");
                printf("0 - ignorar e ir embora\n");
                printf("escolha: ");
                int escolha5;
                scanf("%d", &escolha5);
                // beijo
                if (escolha5) {
                    printf("voces casaram e viveram felizes por 7 anos\n");
                    printf("depois ela te traiu e voce morreu de depressao\ngame over\n");
                }
                // ir embora
                else {
                    printf("voce foi embora da masmorra virou gigachad e ganhou na vida\ngame win\n");
                }
            }
        }
    }
    while(1);
}
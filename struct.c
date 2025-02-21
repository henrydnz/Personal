    #include <stdio.h>
    #include <ctype.h>
    #include <string.h>
    #include <stdlib.h>
    #define max_movie_name_len 30
    #define max_room_amm 10
    #define max_movie_amm 50

    typedef struct{
        int code;
        char name[max_movie_name_len];
        int room_amm;
        int rooms[max_room_amm];
    }movie;

    void menu(){
        printf("(R)egister movie\n");
        printf("(S)how movies\n");
        printf("(E)xit\n");

    }

    void register_movie(movie movie_list[max_movie_amm], int *movie_amm){
        int movie_code = *movie_amm;    
        movie_list[movie_code].code = movie_code+1; 
        
        printf("Input movie name: ");
        scanf("%[^\n]%*c", movie_list[movie_code].name);
        
        printf("Input the ammount of rooms that will stream %s (max is 10): ", movie_list[movie_code].name);
        scanf("%d%*c", &movie_list[movie_code].room_amm);

        printf("Input the rooms: ");
        for(int i=0; i<movie_list[movie_code].room_amm; i++){
            scanf("%d%*c", &movie_list[movie_code].rooms[i]);
        }

        (*movie_amm)++;
    }

    void show_movies(movie movie_list[max_movie_amm], int movie_amm){
        if(!movie_amm) {
            printf("No movies registered yet!\n\n");
        }
        else
        {
            for(int i=0; i<movie_amm; i++){
                printf("%d - %s\n", movie_list[i].code, movie_list[i].name);
                printf("    Rooms streaming this movie: ");
                for(int j=0; j<movie_list[i].room_amm; j++){
                    printf("%d ", movie_list[i].rooms[j]);
                }
                printf("\n\n");
            }
            printf("\n\n");
        }
    }

    void search_room(movie movie_list[max_movie_amm], int movie_amm){
        int search;
        scanf("%d%*c", &search);
        //n fiz
        
    }

    void action(char op, movie movie_list[max_movie_amm], int *movie_amm){
        switch(tolower(op)){
            case 'r':
                register_movie(movie_list, movie_amm);
                system("cls");
                printf("Movie was registered successfully!\n\n");
                break;
            case 's':
                show_movies(movie_list, *movie_amm);
                break;
        }
    }

    int main() {
        movie movie_list[max_movie_amm];
        char op = 'a';
        int movie_amm = 0;
        
        system("cls");
        while(tolower(op)!='e'){
            menu();
            scanf("%c%*c", &op);
            system("cls");
            action(op, movie_list, &movie_amm);
        }

        return 0;
    }
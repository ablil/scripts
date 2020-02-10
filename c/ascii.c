#include <stdio.h>

void displayAscii(){
		for ( int i = 18; i < 127; i++){
				if ( i % 6 == 0)
						puts("");
				printf("%d: %c\t", i, (char)i);
		}
		puts("");
}

int main(int argc, char **argv){
		puts("Ascii table starting from character 18");
		displayAscii();
		return 0;
}
